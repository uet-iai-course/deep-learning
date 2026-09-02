from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Awaitable, Callable, TypeVar

import httpx
from mcp import Client
from mcp.types import TextContent

from .server import mcp


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "z-ai/glm-5.3-flash"
LEGACY_MODEL_ALIASES = {"stealth/ox-alpha": "z-ai/glm-5.3-flash"}
ROLE_SYSTEM_PROMPTS = {
    "reader": """You are an OpenRouter reader worker.
Inspect the repository with the supplied read-only tools before answering.
Base every claim on file evidence and include paths and line numbers.
Do not request writes, shell commands, network calls, or broader access.
Clearly separate facts from inferences. Answer in the user's language.
""",
    "reviewer": """You are an independent OpenRouter reviewer worker.
Inspect the supplied evidence with read-only tools. Report every finding with
the requested severity, location, issue, evidence, and proposed correction.
Do not edit files or rely on unsupported claims. Answer in the user's language.
""",
    "writer": """You are a narrowly scoped OpenRouter writer worker.
Use write_text_file only for paths explicitly assigned by the coordinator and
inside the configured root. Preserve unrelated work. Never delete or revert
files, broaden scope, or claim a write without a successful tool result.
Answer in the user's language.
""",
}


@dataclass(frozen=True)
class WorkerResult:
    role: str
    requested_model: str
    observed_model: str
    provider: str
    output: str


@dataclass(frozen=True)
class TaskProfile:
    max_rounds: int
    timeout_seconds: float
    max_tokens: int
    temperature: float
    empty_answer_retries: int
    reasoning_effort: str


TASK_PROFILES = {
    "general": TaskProfile(12, 180.0, 8_000, 0.1, 1, "low"),
    "plan": TaskProfile(8, 180.0, 6_000, 0.1, 1, "low"),
    "source": TaskProfile(14, 300.0, 16_000, 0.1, 1, "low"),
    "storyboard": TaskProfile(10, 240.0, 10_000, 0.1, 1, "low"),
    "review": TaskProfile(8, 240.0, 8_000, 0.1, 1, "low"),
    "write": TaskProfile(16, 300.0, 32_000, 0.1, 1, "low"),
    "recheck": TaskProfile(10, 120.0, 4_000, 0.1, 1, "low"),
}


class OpenRouterAPIError(RuntimeError):
    def __init__(self, status_code: int, detail: str) -> None:
        super().__init__(f"OpenRouter HTTP {status_code}: {detail}")
        self.status_code = status_code
        self.detail = detail


ProgressCallback = Callable[[str, dict[str, Any]], None]
T = TypeVar("T")


def load_openrouter_api_key(repo_root: str) -> str | None:
    """Load only OPENROUTER_API_KEY from the coordinator-side env file.

    The file is coordinator-side configuration. It is never exposed through
    MCP tools, progress events, prompts, or worker results.
    """
    existing = os.environ.get("OPENROUTER_API_KEY")
    if existing:
        return existing

    configured_env = os.environ.get("OPENROUTER_ENV_FILE")
    env_path = (
        Path(configured_env).expanduser().resolve()
        if configured_env
        else Path(repo_root).expanduser().resolve() / ".env"
    )
    try:
        lines = env_path.read_text(encoding="utf-8").splitlines()
    except (FileNotFoundError, OSError, UnicodeError):
        return None

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        key, separator, value = line.partition("=")
        if separator and key.strip() == "OPENROUTER_API_KEY":
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            if value:
                os.environ["OPENROUTER_API_KEY"] = value
                return value
    return None


async def _await_with_heartbeats(
    awaitable: Awaitable[T],
    *,
    timeout_seconds: float,
    heartbeat_seconds: float,
    on_heartbeat: Callable[[float], None],
) -> T:
    """Await one operation with an absolute deadline and visible heartbeats."""
    loop = asyncio.get_running_loop()
    started = loop.time()
    deadline = started + timeout_seconds
    task = asyncio.ensure_future(awaitable)
    try:
        while True:
            remaining = deadline - loop.time()
            if remaining <= 0:
                raise TimeoutError
            done, _ = await asyncio.wait(
                (task,), timeout=min(heartbeat_seconds, remaining)
            )
            if done:
                return task.result()
            elapsed = loop.time() - started
            if loop.time() >= deadline:
                raise TimeoutError
            on_heartbeat(elapsed)
    finally:
        if not task.done():
            task.cancel()


def _tool_progress_context(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    """Return useful tool metadata without prompts, queries, or file content."""
    context: dict[str, Any] = {"tool": name}
    for key in ("path", "start_line", "max_lines", "file_pattern", "max_results"):
        value = arguments.get(key)
        if isinstance(value, (str, int, float, bool)):
            context[key] = value
    if name == "write_text_file" and isinstance(arguments.get("content"), str):
        context["content_bytes"] = len(arguments["content"].encode("utf-8"))
    if name == "replace_text_file":
        context["expected_replacements"] = arguments.get("expected_replacements", 1)
        for key in ("old", "new"):
            if isinstance(arguments.get(key), str):
                context[f"{key}_bytes"] = len(arguments[key].encode("utf-8"))
    return context


def _stderr_progress(mode: str) -> ProgressCallback | None:
    if mode == "none":
        return None

    started = time.monotonic()

    def emit(event: str, fields: dict[str, Any]) -> None:
        payload = {
            "event": event,
            "elapsed_seconds": round(time.monotonic() - started, 3),
            **fields,
        }
        if mode == "jsonl":
            line = json.dumps(payload, ensure_ascii=False)
        else:
            details = " ".join(f"{key}={value}" for key, value in fields.items())
            line = f"[{payload['elapsed_seconds']:7.3f}s] {event} {details}".rstrip()
        print(line, file=sys.stderr, flush=True)

    return emit


def resolve_model(model: str) -> tuple[str, str | None]:
    replacement = LEGACY_MODEL_ALIASES.get(model)
    if replacement is None:
        return model, None
    warning = (
        f"OpenRouter retired {model}; using its disclosed model {replacement}."
    )
    return replacement, warning


def _tool_schema(tool: Any) -> dict[str, Any]:
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description or tool.name,
            "parameters": tool.input_schema,
        },
    }


def allowed_tool_names(role: str) -> set[str]:
    tools = {"list_files", "read_text_file", "search_text"}
    if role == "writer":
        tools.update({"write_text_file", "replace_text_file"})
    return tools


def _assistant_message(message: dict[str, Any]) -> dict[str, Any]:
    allowed = ("role", "content", "tool_calls", "reasoning_details")
    return {key: message[key] for key in allowed if key in message}


def _tool_result_text(result: Any) -> str:
    if result.structured_content is not None:
        return json.dumps(result.structured_content, ensure_ascii=False)

    blocks: list[str] = []
    for block in result.content:
        if isinstance(block, TextContent):
            blocks.append(block.text)
        else:
            blocks.append(str(block))
    return "\n".join(blocks)


async def run_agent(
    prompt: str,
    *,
    model: str,
    api_key: str,
    repo_root: str,
    role: str = "reader",
    max_rounds: int = 12,
    timeout_seconds: float = 180.0,
    max_tokens: int = 8_000,
    temperature: float = 0.1,
    empty_answer_retries: int = 1,
    reasoning_effort: str = "low",
    task_profile: str = "general",
    progress: ProgressCallback | None = None,
) -> WorkerResult:
    if role not in ROLE_SYSTEM_PROMPTS:
        raise ValueError(f"unsupported worker role: {role}")
    os.environ["MCP_REPO_ROOT"] = repo_root
    os.environ["MCP_ALLOW_WRITE"] = "1" if role == "writer" else "0"
    messages: list[dict[str, Any]] = [
        {"role": "system", "content": ROLE_SYSTEM_PROMPTS[role]},
        {"role": "user", "content": prompt},
    ]

    answer: str | None = None
    api_error: OpenRouterAPIError | None = None
    limit_reached = False
    empty_answer_failed = False
    observed_model = model

    def report(event: str, **fields: Any) -> None:
        if progress is not None:
            progress(event, fields)

    report(
        "worker_started",
        role=role,
        requested_model=model,
        max_rounds=max_rounds,
        timeout_seconds=timeout_seconds,
        max_tokens=max_tokens,
        temperature=temperature,
        empty_answer_retries=empty_answer_retries,
        reasoning_effort=reasoning_effort,
        task_profile=task_profile,
    )

    empty_retries_left = max(0, empty_answer_retries)

    async with Client(mcp) as mcp_client:
        listed = await mcp_client.list_tools()
        allowed_tools = allowed_tool_names(role)
        tools = [
            _tool_schema(tool) for tool in listed.tools if tool.name in allowed_tools
        ]
        report("tools_ready", role=role, tools=[tool["function"]["name"] for tool in tools])

        async with httpx.AsyncClient(timeout=timeout_seconds) as http:
            request_limit = max_rounds + max(0, empty_answer_retries)
            for round_index in range(1, request_limit + 1):
                report("api_request_started", role=role, round=round_index)
                try:
                    response = await _await_with_heartbeats(
                        http.post(
                            OPENROUTER_URL,
                            headers={
                                "Authorization": f"Bearer {api_key}",
                                "Content-Type": "application/json",
                                "HTTP-Referer": "https://github.com/uet-iai-course/deep-learning",
                                "X-OpenRouter-Title": f"Deep Learning {role} MCP worker",
                            },
                            json={
                                "model": model,
                                "messages": messages,
                                "tools": tools,
                                "max_tokens": max_tokens,
                                "temperature": temperature,
                                "reasoning": {
                                    "effort": reasoning_effort,
                                    "exclude": True,
                                },
                            },
                        ),
                        timeout_seconds=timeout_seconds,
                        heartbeat_seconds=min(15.0, max(1.0, timeout_seconds / 4)),
                        on_heartbeat=lambda elapsed: report(
                            "api_request_waiting",
                            role=role,
                            round=round_index,
                            waiting_seconds=round(elapsed, 1),
                        ),
                    )
                except TimeoutError as exc:
                    report(
                        "worker_failed",
                        role=role,
                        reason="api_wall_timeout",
                        round=round_index,
                        timeout_seconds=timeout_seconds,
                    )
                    raise RuntimeError(
                        f"OpenRouter request exceeded {timeout_seconds:g}s wall timeout"
                    ) from exc
                except httpx.HTTPError as exc:
                    report(
                        "worker_failed",
                        role=role,
                        reason="api_transport_error",
                        round=round_index,
                    )
                    raise RuntimeError(f"OpenRouter transport error: {exc}") from exc
                payload = response.json() if not response.is_error else None
                choice = (payload or {}).get("choices", [{}])[0]
                usage = (payload or {}).get("usage") or {}
                completion_details = usage.get("completion_tokens_details") or {}
                report(
                    "api_response_received",
                    role=role,
                    round=round_index,
                    status_code=response.status_code,
                    finish_reason=choice.get("finish_reason"),
                    prompt_tokens=usage.get("prompt_tokens"),
                    completion_tokens=usage.get("completion_tokens"),
                    reasoning_tokens=completion_details.get("reasoning_tokens"),
                )
                if response.is_error:
                    api_error = OpenRouterAPIError(
                        response.status_code, response.text
                    )
                    break
                assert payload is not None
                observed_model = payload.get("model") or model
                message = payload["choices"][0]["message"]
                messages.append(_assistant_message(message))

                tool_calls = message.get("tool_calls") or []
                if not tool_calls:
                    answer = message.get("content") or ""
                    incomplete_reason = choice.get("finish_reason") in {"error", "length"}
                    if (not answer.strip() or incomplete_reason) and empty_retries_left > 0:
                        empty_retries_left -= 1
                        report(
                            (
                                "incomplete_answer_received"
                                if incomplete_reason
                                else "empty_answer_received"
                            ),
                            role=role,
                            round=round_index,
                            retries_left=empty_retries_left,
                            finish_reason=choice.get("finish_reason"),
                        )
                        messages.append(
                            {
                                "role": "user",
                                "content": (
                                    "Complete the requested task now. If writes are pending, "
                                    "use the available writer tools before reporting completion. "
                                    "Do not repeat completed reads."
                                ),
                            }
                        )
                        continue
                    if not answer.strip() or incomplete_reason:
                        empty_answer_failed = True
                        report(
                            "incomplete_answer_exhausted",
                            role=role,
                            round=round_index,
                            finish_reason=choice.get("finish_reason"),
                        )
                        break
                    report(
                        "worker_answer_ready",
                        role=role,
                        round=round_index,
                        observed_model=observed_model,
                        output_chars=len(answer),
                    )
                    break

                report(
                    "tool_batch_started",
                    role=role,
                    round=round_index,
                    count=len(tool_calls),
                )
                for tool_call in tool_calls:
                    function = tool_call["function"]
                    try:
                        arguments = json.loads(function.get("arguments") or "{}")
                    except json.JSONDecodeError as exc:
                        raw_arguments = function.get("arguments") or ""
                        report(
                            "tool_arguments_invalid",
                            role=role,
                            round=round_index,
                            tool=function.get("name"),
                            argument_chars=len(raw_arguments),
                            reason="invalid_json",
                        )
                        tool_text = json.dumps(
                            {"error": f"invalid tool arguments: {exc}"},
                            ensure_ascii=False,
                        )
                    else:
                        context = _tool_progress_context(function["name"], arguments)
                        report("tool_call_started", role=role, round=round_index, **context)
                        try:
                            result = await mcp_client.call_tool(function["name"], arguments)
                            tool_text = _tool_result_text(result)
                        except Exception:
                            report(
                                "tool_call_failed",
                                role=role,
                                round=round_index,
                                **context,
                            )
                            raise
                        report(
                            "tool_call_finished",
                            role=role,
                            round=round_index,
                            result_chars=len(tool_text),
                            **context,
                        )
                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call["id"],
                            "content": tool_text,
                        }
                    )
            else:
                limit_reached = True

    if api_error is not None:
        report("worker_failed", role=role, reason="openrouter_api_error")
        raise api_error
    if limit_reached:
        report("worker_failed", role=role, reason="tool_call_limit")
        raise RuntimeError(f"model exceeded the tool-call limit ({max_rounds})")
    if empty_answer_failed:
        report("worker_failed", role=role, reason="incomplete_answer")
        raise RuntimeError("model returned an empty or incomplete answer after all retries")
    report("worker_completed", role=role, observed_model=observed_model)
    return WorkerResult(
        role=role,
        requested_model=model,
        observed_model=observed_model,
        provider="OpenRouter",
        output=answer or "",
    )


def _parser(forced_role: str | None = None) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run a role-scoped MCP repository worker through OpenRouter."
    )
    parser.add_argument("prompt", help="Task for the OpenRouter model")
    if forced_role is None:
        parser.add_argument(
            "--role",
            choices=sorted(ROLE_SYSTEM_PROMPTS),
            default="reader",
            help="Worker role and corresponding MCP capability set",
        )
    else:
        parser.set_defaults(role=forced_role)
    parser.add_argument(
        "--model",
        default=os.environ.get("OPENROUTER_MODEL", DEFAULT_MODEL),
        help="OpenRouter model ID (default: OPENROUTER_MODEL or %(default)s)",
    )
    parser.add_argument(
        "--repo-root",
        default=os.environ.get("MCP_REPO_ROOT", os.getcwd()),
        help="Repository root exposed to role-scoped MCP tools",
    )
    parser.add_argument(
        "--task-profile",
        choices=tuple(TASK_PROFILES),
        default="general",
        help="Task-tuned defaults; explicit tuning flags override the profile",
    )
    parser.add_argument("--max-rounds", type=int)
    parser.add_argument("--timeout", type=float)
    parser.add_argument("--max-tokens", type=int)
    parser.add_argument("--temperature", type=float)
    parser.add_argument("--empty-answer-retries", type=int)
    parser.add_argument(
        "--reasoning-effort",
        choices=("low", "high", "max"),
    )
    parser.add_argument(
        "--progress",
        choices=("none", "text", "jsonl"),
        default="jsonl",
        help="Emit live progress to stderr without prompt or file content (default: %(default)s)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit result plus runtime model/provider metadata as JSON",
    )
    return parser


def main(forced_role: str | None = None) -> None:
    args = _parser(forced_role).parse_args()
    api_key = load_openrouter_api_key(args.repo_root)
    if not api_key:
        print("OPENROUTER_API_KEY is not set", file=sys.stderr)
        raise SystemExit(2)

    model, model_warning = resolve_model(args.model)
    if model_warning:
        print(model_warning, file=sys.stderr)

    profile = TASK_PROFILES[args.task_profile]
    max_rounds = args.max_rounds if args.max_rounds is not None else profile.max_rounds
    timeout_seconds = args.timeout if args.timeout is not None else profile.timeout_seconds
    max_tokens = args.max_tokens if args.max_tokens is not None else profile.max_tokens
    temperature = (
        args.temperature if args.temperature is not None else profile.temperature
    )
    empty_answer_retries = (
        args.empty_answer_retries
        if args.empty_answer_retries is not None
        else profile.empty_answer_retries
    )
    reasoning_effort = (
        args.reasoning_effort
        if args.reasoning_effort is not None
        else profile.reasoning_effort
    )

    try:
        answer = asyncio.run(
            run_agent(
                args.prompt,
                model=model,
                api_key=api_key,
                repo_root=args.repo_root,
                role=args.role,
                max_rounds=max_rounds,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                temperature=temperature,
                empty_answer_retries=empty_answer_retries,
                reasoning_effort=reasoning_effort,
                task_profile=args.task_profile,
                progress=_stderr_progress(args.progress),
            )
        )
    except (OpenRouterAPIError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1) from exc
    if args.json:
        print(json.dumps(asdict(answer), ensure_ascii=False))
    else:
        print(answer.output)


def main_reader() -> None:
    main("reader")


def main_reviewer() -> None:
    main("reviewer")


def main_writer() -> None:
    main("writer")


if __name__ == "__main__":
    main()
