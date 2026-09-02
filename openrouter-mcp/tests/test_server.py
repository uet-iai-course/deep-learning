from __future__ import annotations

import asyncio
import os
import tempfile
import unittest
from pathlib import Path

from mcp import Client

from openrouter_mcp.bridge import (
    ROLE_SYSTEM_PROMPTS,
    TASK_PROFILES,
    _await_with_heartbeats,
    _parser,
    _tool_progress_context,
    allowed_tool_names,
    load_openrouter_api_key,
    resolve_model,
)
from openrouter_mcp.server import mcp


class ReadOnlyServerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.outside_tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "AGENTS.md").write_text("alpha\nbeta responsibility\n", encoding="utf-8")
        outside = Path(self.outside_tempdir.name) / "secret.txt"
        outside.write_text("must not be exposed\n", encoding="utf-8")
        (self.root / "outside-link.txt").symlink_to(outside)
        os.environ["MCP_REPO_ROOT"] = str(self.root)

    def tearDown(self) -> None:
        os.environ.pop("MCP_ALLOW_WRITE", None)
        os.environ.pop("MCP_WRITE_POLICY", None)
        os.environ.pop("MCP_MAX_WRITE_CHARS", None)
        os.environ.pop("OPENROUTER_ENV_FILE", None)
        self.tempdir.cleanup()
        self.outside_tempdir.cleanup()

    def test_tools_list_read_and_search(self) -> None:
        async def scenario() -> None:
            async with Client(mcp, raise_exceptions=True) as client:
                listed = await client.list_tools()
                names = {tool.name for tool in listed.tools}
                self.assertEqual(
                    names,
                    {
                        "list_files",
                        "read_text_file",
                        "search_text",
                        "write_text_file",
                        "replace_text_file",
                    },
                )

                read_result = await client.call_tool(
                    "read_text_file", {"path": "AGENTS.md"}
                )
                self.assertEqual(read_result.structured_content["total_lines"], 2)
                self.assertIn("2: beta responsibility", read_result.structured_content["text"])

                search_result = await client.call_tool(
                    "search_text", {"query": "RESPONSIBILITY"}
                )
                self.assertEqual(search_result.structured_content["count"], 1)
                self.assertEqual(search_result.structured_content["matches"][0]["line"], 2)

        asyncio.run(scenario())

    def test_write_requires_writer_mode_and_stays_in_root(self) -> None:
        async def scenario() -> None:
            async with Client(mcp) as client:
                disabled = await client.call_tool(
                    "write_text_file", {"path": "worker-check.txt", "content": "no"}
                )
                self.assertTrue(disabled.is_error)

                os.environ["MCP_ALLOW_WRITE"] = "1"
                written = await client.call_tool(
                    "write_text_file", {"path": "tmp/worker-check.txt", "content": "ok\n"}
                )
                self.assertFalse(written.is_error)
                self.assertEqual(
                    (self.root / "tmp" / "worker-check.txt").read_text(encoding="utf-8"),
                    "ok\n",
                )
                escaped = await client.call_tool(
                    "write_text_file", {"path": "../escaped.txt", "content": "no"}
                )
                self.assertTrue(escaped.is_error)

                replaced = await client.call_tool(
                    "replace_text_file",
                    {
                        "path": "tmp/worker-check.txt",
                        "old": "ok",
                        "new": "done",
                        "expected_replacements": 1,
                    },
                )
                self.assertFalse(replaced.is_error)
                self.assertEqual(
                    (self.root / "tmp" / "worker-check.txt").read_text(encoding="utf-8"),
                    "done\n",
                )
                mismatch = await client.call_tool(
                    "replace_text_file",
                    {
                        "path": "tmp/worker-check.txt",
                        "old": "missing",
                        "new": "no",
                        "expected_replacements": 1,
                    },
                )
                self.assertTrue(mismatch.is_error)

        asyncio.run(scenario())

    def test_all_project_roles_are_defined(self) -> None:
        self.assertEqual(set(ROLE_SYSTEM_PROMPTS), {"reader", "reviewer", "writer"})

    def test_create_once_policy_rejects_overwrite_and_replace(self) -> None:
        async def scenario() -> None:
            os.environ["MCP_ALLOW_WRITE"] = "1"
            os.environ["MCP_WRITE_POLICY"] = "create-once"
            async with Client(mcp) as client:
                first = await client.call_tool(
                    "write_text_file", {"path": "draft.md", "content": "first\n"}
                )
                self.assertFalse(first.is_error)
                second = await client.call_tool(
                    "write_text_file", {"path": "draft.md", "content": "second\n"}
                )
                self.assertTrue(second.is_error)
                replaced = await client.call_tool(
                    "replace_text_file",
                    {"path": "draft.md", "old": "first", "new": "changed"},
                )
                self.assertTrue(replaced.is_error)
                self.assertEqual(
                    (self.root / "draft.md").read_text(encoding="utf-8"), "first\n"
                )

        asyncio.run(scenario())

    def test_max_write_chars_rejects_oversized_output(self) -> None:
        async def scenario() -> None:
            os.environ["MCP_ALLOW_WRITE"] = "1"
            os.environ["MCP_MAX_WRITE_CHARS"] = "5"
            async with Client(mcp) as client:
                accepted = await client.call_tool(
                    "write_text_file", {"path": "short.md", "content": "12345"}
                )
                self.assertFalse(accepted.is_error)
                rejected = await client.call_tool(
                    "write_text_file", {"path": "long.md", "content": "123456"}
                )
                self.assertTrue(rejected.is_error)
                self.assertFalse((self.root / "long.md").exists())

        asyncio.run(scenario())

    def test_task_profiles_fit_worker_jobs(self) -> None:
        self.assertGreater(TASK_PROFILES["source"].max_rounds, TASK_PROFILES["plan"].max_rounds)
        self.assertGreater(
            TASK_PROFILES["source"].timeout_seconds,
            TASK_PROFILES["plan"].timeout_seconds,
        )
        self.assertGreater(TASK_PROFILES["write"].max_tokens, TASK_PROFILES["review"].max_tokens)
        self.assertLess(TASK_PROFILES["recheck"].max_tokens, TASK_PROFILES["review"].max_tokens)
        self.assertLess(
            TASK_PROFILES["recheck"].timeout_seconds,
            TASK_PROFILES["review"].timeout_seconds,
        )
        self.assertEqual(TASK_PROFILES["review"].empty_answer_retries, 1)
        self.assertEqual(TASK_PROFILES["review"].reasoning_effort, "low")

    def test_role_specific_parser_cannot_be_overridden(self) -> None:
        args = _parser("reader").parse_args(["task"])
        self.assertEqual(args.role, "reader")
        self.assertEqual(args.progress, "jsonl")
        self.assertEqual(args.task_profile, "general")
        self.assertIsNone(args.max_rounds)
        with self.assertRaises(SystemExit):
            _parser("reader").parse_args(["--role", "writer", "task"])

    def test_only_writer_receives_write_tool_schema(self) -> None:
        self.assertNotIn("write_text_file", allowed_tool_names("reader"))
        self.assertNotIn("write_text_file", allowed_tool_names("reviewer"))
        self.assertIn("write_text_file", allowed_tool_names("writer"))
        self.assertNotIn("replace_text_file", allowed_tool_names("reader"))
        self.assertIn("replace_text_file", allowed_tool_names("writer"))

    def test_retired_stealth_model_maps_to_disclosed_model(self) -> None:
        model, warning = resolve_model("stealth/ox-alpha")
        self.assertEqual(model, "z-ai/glm-5.3-flash")
        self.assertIn("retired", warning)

    def test_parent_traversal_is_rejected(self) -> None:
        async def scenario() -> None:
            async with Client(mcp) as client:
                result = await client.call_tool(
                    "read_text_file", {"path": "../outside.txt"}
                )
                self.assertTrue(result.is_error)

        asyncio.run(scenario())

    def test_symlink_outside_repository_is_not_exposed(self) -> None:
        async def scenario() -> None:
            async with Client(mcp) as client:
                listed = await client.call_tool("list_files", {})
                self.assertNotIn(
                    "outside-link.txt", listed.structured_content["files"]
                )
                searched = await client.call_tool(
                    "search_text", {"query": "must not be exposed"}
                )
                self.assertEqual(searched.structured_content["count"], 0)

        asyncio.run(scenario())

    def test_env_files_are_never_exposed_or_written(self) -> None:
        (self.root / ".env").write_text("SECRET=value\n", encoding="utf-8")
        (self.root / ".env.local").write_text("LOCAL_SECRET=value\n", encoding="utf-8")

        async def scenario() -> None:
            async with Client(mcp) as client:
                listed = await client.call_tool("list_files", {})
                self.assertNotIn(".env", listed.structured_content["files"])
                self.assertNotIn(".env.local", listed.structured_content["files"])

                searched = await client.call_tool("search_text", {"query": "SECRET"})
                self.assertEqual(searched.structured_content["count"], 0)

                read = await client.call_tool("read_text_file", {"path": ".env"})
                self.assertTrue(read.is_error)

                os.environ["MCP_ALLOW_WRITE"] = "1"
                written = await client.call_tool(
                    "write_text_file", {"path": ".env", "content": "no"}
                )
                self.assertTrue(written.is_error)
                replaced = await client.call_tool(
                    "replace_text_file",
                    {"path": ".env", "old": "SECRET", "new": "no"},
                )
                self.assertTrue(replaced.is_error)

        asyncio.run(scenario())

    def test_progress_context_omits_queries_and_content(self) -> None:
        context = _tool_progress_context(
            "search_text",
            {"path": "2627-1", "query": "secret phrase", "max_results": 10},
        )
        self.assertEqual(
            context,
            {"tool": "search_text", "path": "2627-1", "max_results": 10},
        )
        write_context = _tool_progress_context(
            "write_text_file", {"path": "out.md", "content": "bí mật"}
        )
        self.assertEqual(write_context["path"], "out.md")
        self.assertNotIn("content", write_context)
        self.assertGreater(write_context["content_bytes"], 0)
        replace_context = _tool_progress_context(
            "replace_text_file",
            {
                "path": "out.md",
                "old": "secret old",
                "new": "secret new",
                "expected_replacements": 1,
            },
        )
        self.assertNotIn("old", replace_context)
        self.assertNotIn("new", replace_context)
        self.assertGreater(replace_context["old_bytes"], 0)

    def test_api_key_loads_from_repo_env_without_exposing_file(self) -> None:
        previous = os.environ.pop("OPENROUTER_API_KEY", None)
        try:
            (self.root / ".env").write_text(
                "OTHER=value\nOPENROUTER_API_KEY='test-key'\n",
                encoding="utf-8",
            )
            self.assertEqual(load_openrouter_api_key(str(self.root)), "test-key")
            self.assertEqual(os.environ["OPENROUTER_API_KEY"], "test-key")
        finally:
            os.environ.pop("OPENROUTER_API_KEY", None)
            if previous is not None:
                os.environ["OPENROUTER_API_KEY"] = previous

    def test_api_key_loads_from_coordinator_env_for_narrow_writer_root(self) -> None:
        previous = os.environ.pop("OPENROUTER_API_KEY", None)
        coordinator_env = self.root / ".env"
        coordinator_env.write_text(
            "OTHER=value\nOPENROUTER_API_KEY=test-key\n", encoding="utf-8"
        )
        os.environ["OPENROUTER_ENV_FILE"] = str(coordinator_env)
        narrow_root = Path(self.outside_tempdir.name)
        try:
            self.assertEqual(load_openrouter_api_key(str(narrow_root)), "test-key")
        finally:
            os.environ.pop("OPENROUTER_API_KEY", None)
            if previous is not None:
                os.environ["OPENROUTER_API_KEY"] = previous

    def test_await_heartbeats_and_absolute_timeout(self) -> None:
        async def scenario() -> None:
            heartbeats: list[float] = []
            result = await _await_with_heartbeats(
                asyncio.sleep(0.03, result="done"),
                timeout_seconds=0.2,
                heartbeat_seconds=0.01,
                on_heartbeat=heartbeats.append,
            )
            self.assertEqual(result, "done")
            self.assertGreaterEqual(len(heartbeats), 1)
            with self.assertRaises(TimeoutError):
                await _await_with_heartbeats(
                    asyncio.sleep(0.1),
                    timeout_seconds=0.02,
                    heartbeat_seconds=0.01,
                    on_heartbeat=lambda _: None,
                )

        asyncio.run(scenario())


if __name__ == "__main__":
    unittest.main()
