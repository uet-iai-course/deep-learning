from __future__ import annotations

import os
import hashlib
from pathlib import Path
from typing import Any

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError


MAX_FILE_BYTES = 1_000_000
MAX_LINES_PER_READ = 2_000
MAX_RESULTS = 500
MAX_WRITE_BYTES = 1_000_000

mcp = MCPServer(
    "deep-learning-role-scoped",
    instructions=(
        "Repository access is constrained to the configured root. Read-only "
        "workers use list_files, read_text_file, and search_text. The "
        "write_text_file tool is enabled only for an explicitly selected writer."
    ),
)


def repository_root() -> Path:
    configured = os.environ.get("MCP_REPO_ROOT")
    return Path(configured or Path.cwd()).resolve()


def _resolve_repo_path(path: str) -> Path:
    if not path or path == ".":
        candidate = repository_root()
    else:
        requested = Path(path)
        if requested.is_absolute():
            raise ToolError("path must be relative to the repository root")
        candidate = (repository_root() / requested).resolve()

    root = repository_root()
    if candidate != root and root not in candidate.parents:
        raise ToolError("path escapes the repository root")
    return candidate


def _relative(path: Path) -> str:
    return path.relative_to(repository_root()).as_posix()


def _is_within_repository(path: Path) -> bool:
    root = repository_root()
    return path == root or root in path.parents


def _is_hidden_internal(path: Path) -> bool:
    relative_parts = path.relative_to(repository_root()).parts
    return any(
        part in {".git", ".venv"} or part == ".env" or part.startswith(".env.")
        for part in relative_parts
    )


def _write_enabled() -> bool:
    return os.environ.get("MCP_ALLOW_WRITE") == "1"


@mcp.tool()
async def list_files(
    path: str = ".", pattern: str = "**/*", max_results: int = 200
) -> dict[str, Any]:
    """List repository files below path that match a pathlib glob pattern."""
    base = _resolve_repo_path(path)
    if not base.exists():
        raise ToolError(f"path does not exist: {path}")
    if not base.is_dir():
        raise ToolError(f"path is not a directory: {path}")

    limit = max(1, min(max_results, MAX_RESULTS))
    files: list[str] = []
    for candidate in sorted(base.glob(pattern)):
        resolved = candidate.resolve()
        if not _is_within_repository(resolved):
            continue
        if resolved.is_file() and not _is_hidden_internal(resolved):
            files.append(_relative(resolved))
            if len(files) >= limit:
                break
    return {"files": files, "count": len(files), "limit": limit}


@mcp.tool()
async def read_text_file(
    path: str, start_line: int = 1, max_lines: int = 400
) -> dict[str, Any]:
    """Read a bounded range of UTF-8 text lines from one repository file."""
    target = _resolve_repo_path(path)
    if _is_hidden_internal(target):
        raise ToolError("reading internal .git, .venv, or .env paths is not allowed")
    if not target.is_file():
        raise ToolError(f"not a file: {path}")
    if target.stat().st_size > MAX_FILE_BYTES:
        raise ToolError(f"file exceeds {MAX_FILE_BYTES} bytes: {path}")

    first = max(1, start_line)
    count = max(1, min(max_lines, MAX_LINES_PER_READ))
    try:
        lines = target.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError as exc:
        raise ToolError(f"file is not UTF-8 text: {path}") from exc

    selected = lines[first - 1 : first - 1 + count]
    numbered = "\n".join(
        f"{line_number}: {line}"
        for line_number, line in enumerate(selected, start=first)
    )
    return {
        "path": _relative(target),
        "start_line": first,
        "end_line": first + len(selected) - 1 if selected else first - 1,
        "total_lines": len(lines),
        "text": numbered,
    }


@mcp.tool()
async def search_text(
    query: str,
    path: str = ".",
    file_pattern: str = "**/*",
    case_sensitive: bool = False,
    max_results: int = 100,
) -> dict[str, Any]:
    """Find a literal text string in bounded UTF-8 repository files."""
    if not query:
        raise ToolError("query must not be empty")
    base = _resolve_repo_path(path)
    if not base.is_dir():
        raise ToolError(f"path is not a directory: {path}")

    needle = query if case_sensitive else query.casefold()
    limit = max(1, min(max_results, MAX_RESULTS))
    matches: list[dict[str, Any]] = []
    for candidate in sorted(base.glob(file_pattern)):
        resolved = candidate.resolve()
        if (
            not _is_within_repository(resolved)
            or not resolved.is_file()
            or _is_hidden_internal(resolved)
        ):
            continue
        if resolved.stat().st_size > MAX_FILE_BYTES:
            continue
        try:
            lines = resolved.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(lines, start=1):
            haystack = line if case_sensitive else line.casefold()
            if needle in haystack:
                matches.append(
                    {"path": _relative(resolved), "line": line_number, "text": line}
                )
                if len(matches) >= limit:
                    return {"matches": matches, "count": len(matches), "limit": limit}
    return {"matches": matches, "count": len(matches), "limit": limit}


@mcp.tool()
async def write_text_file(path: str, content: str) -> dict[str, Any]:
    """Write one UTF-8 file inside the configured root when writer mode is enabled."""
    if not _write_enabled():
        raise ToolError("write_text_file is disabled for this worker role")
    if not path or path == ".":
        raise ToolError("path must name a file relative to the configured root")
    encoded = content.encode("utf-8")
    if len(encoded) > MAX_WRITE_BYTES:
        raise ToolError(f"content exceeds {MAX_WRITE_BYTES} bytes")

    target = _resolve_repo_path(path)
    if _is_hidden_internal(target):
        raise ToolError("writing internal .git, .venv, or .env paths is not allowed")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(encoded)
    return {
        "path": _relative(target),
        "bytes": len(encoded),
        "sha256": hashlib.sha256(encoded).hexdigest(),
    }


@mcp.tool()
async def replace_text_file(
    path: str,
    old: str,
    new: str,
    expected_replacements: int = 1,
) -> dict[str, Any]:
    """Replace exact UTF-8 text in one existing file when writer mode is enabled."""
    if not _write_enabled():
        raise ToolError("replace_text_file is disabled for this worker role")
    if not old:
        raise ToolError("old text must not be empty")
    if expected_replacements < 1:
        raise ToolError("expected_replacements must be at least 1")

    target = _resolve_repo_path(path)
    if _is_hidden_internal(target):
        raise ToolError("editing internal .git, .venv, or .env paths is not allowed")
    if not target.is_file():
        raise ToolError(f"not a file: {path}")
    if target.stat().st_size > MAX_FILE_BYTES:
        raise ToolError(f"file exceeds {MAX_FILE_BYTES} bytes: {path}")

    try:
        content = target.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ToolError(f"file is not UTF-8 text: {path}") from exc
    actual_replacements = content.count(old)
    if actual_replacements != expected_replacements:
        raise ToolError(
            "replacement count mismatch: "
            f"expected {expected_replacements}, found {actual_replacements}"
        )

    updated = content.replace(old, new)
    encoded = updated.encode("utf-8")
    if len(encoded) > MAX_WRITE_BYTES:
        raise ToolError(f"updated content exceeds {MAX_WRITE_BYTES} bytes")
    target.write_bytes(encoded)
    return {
        "path": _relative(target),
        "replacements": actual_replacements,
        "bytes": len(encoded),
        "sha256": hashlib.sha256(encoded).hexdigest(),
    }


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
