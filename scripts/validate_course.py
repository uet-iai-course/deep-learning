#!/usr/bin/env python3
"""Kiểm định tĩnh học liệu Học sâu trước khi dựng bằng trình duyệt."""

from __future__ import annotations

import html
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TERM = ROOT / "2627-1"
LECTURES = ("01", "02", "03", "04", "05", "06", "07", "08", "10", "11", "12", "13", "14")
PLANNING_FILES = ("outline.md", "storyboard.md", "review-log.md", "note-for-author.md")
PUBLIC_META = re.compile(
    r"OpenRouter|DeepSeek|(?<![A-Za-z])GLM(?![A-Za-z])|MCP_[A-Z_]+|"
    r"tuyến\s+(?:lõi|mở\s+rộng)|có\s+thể\s+cắt|lộ\s+trình\s+của\s+bài|"
    r"người\s+soạn|ghi\s+chú\s+diễn\s+giả|chặn\s+bàn\s+giao|TODO|FIXME",
    re.IGNORECASE,
)
PROHIBITED_HEADING_ENGLISH = re.compile(
    r"\b(?:forward pass|backward pass|training loop|inference|shape|workflow|overview)\b",
    re.IGNORECASE,
)


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.deck_by_lecture: dict[str, Path] = {}
        self.slide_total = 0
        self.svg_total = 0

    def fail(self, path: Path | str, message: str) -> None:
        try:
            label = Path(path).resolve().relative_to(ROOT)
        except (ValueError, TypeError):
            label = path
        self.errors.append(f"{label}: {message}")

    def require_file(self, path: Path) -> None:
        if not path.is_file():
            self.fail(path, "thiếu tệp")
        elif path.stat().st_size == 0:
            self.fail(path, "tệp rỗng")

    def validate_layout(self) -> None:
        for number in LECTURES:
            decks = sorted(TERM.glob(f"lecture-{number}-*.html"))
            if len(decks) != 1:
                self.fail(TERM, f"Bài {number} phải có đúng một deck, tìm thấy {len(decks)}")
                continue
            self.deck_by_lecture[number] = decks[0]
            self.require_file(TERM / f"materials/lec-{number}/lecture-note.md")
            for filename in PLANNING_FILES:
                self.require_file(TERM / f"planning/lec-{number}/{filename}")

        forbidden = list(TERM.glob("lecture-09-*.html")) + list(TERM.glob("lecture-15-*.html"))
        for path in forbidden:
            self.fail(path, "không được xây deck cho Bài 09 hoặc 15")
        if (ROOT / "quill.json").exists():
            self.fail(ROOT / "quill.json", "quy trình cấm khởi tạo quill.json")

    def validate_index(self) -> None:
        path = TERM / "index.html"
        self.require_file(path)
        source = path.read_text(encoding="utf-8")
        order = re.findall(r'<span\s+class="term-label">Bài\s+(\d+)</span>', source)
        expected = [str(int(number)) for number in LECTURES]
        if order != expected:
            self.fail(path, f"thứ tự bài phải là {expected}, nhận {order}")

        deck_links = re.findall(r'href="(lecture-(\d{2})-[a-z0-9-]+\.html)"', source)
        note_links = re.findall(r'href="material-viewer\.html\?doc=materials/lec-(\d{2})/lecture-note\.md&amp;deck=(lecture-(\d{2})-[a-z0-9-]+\.html)"', source)
        if len(deck_links) != len(LECTURES):
            self.fail(path, f"cần {len(LECTURES)} liên kết deck, nhận {len(deck_links)}")
        if len(note_links) != len(LECTURES):
            self.fail(path, f"cần {len(LECTURES)} liên kết lecture note, nhận {len(note_links)}")

        for href, number in deck_links:
            expected_deck = self.deck_by_lecture.get(number)
            if expected_deck is None or href != expected_deck.name:
                self.fail(path, f"liên kết deck Bài {number} không khớp tệp đích: {href}")
        for note_number, href, deck_number in note_links:
            if note_number != deck_number:
                self.fail(path, f"liên kết note/deck lệch số bài {note_number}/{deck_number}")
            expected_deck = self.deck_by_lecture.get(note_number)
            if expected_deck is None or href != expected_deck.name:
                self.fail(path, f"liên kết viewer Bài {note_number} không khớp deck: {href}")

    @staticmethod
    def outer_section_count(source: str) -> tuple[int, int]:
        start = source.find('<div class="slides">')
        end = source.find('<div class="footer">', start)
        if start < 0 or end < 0:
            return -1, -1
        depth = 0
        outer = 0
        for match in re.finditer(r"</?section\b[^>]*>", source[start:end]):
            if match.group().startswith("</"):
                depth -= 1
                if depth < 0:
                    return outer, depth
            else:
                if depth == 0:
                    outer += 1
                depth += 1
        return outer, depth

    def validate_local_reference(self, owner: Path, value: str) -> None:
        decoded = html.unescape(value)
        parsed = urllib.parse.urlsplit(decoded)
        if parsed.scheme or parsed.netloc or decoded.startswith(("#", "data:", "mailto:")):
            return
        target = (owner.parent / urllib.parse.unquote(parsed.path)).resolve()
        if not target.exists():
            self.fail(owner, f"tham chiếu cục bộ bị hỏng: {value}")

    def validate_deck(self, number: str, path: Path) -> None:
        source = path.read_text(encoding="utf-8")
        required = {
            'lang="vi"': "thiếu ngôn ngữ tiếng Việt",
            "width:1280": "thiếu chiều rộng Reveal 1280",
            "height:720": "thiếu chiều cao Reveal 720",
            'controlsLayout:"edges"': "controlsLayout không phải edges",
            "slideNumber:true": "chưa bật số trang",
            "hashOneBasedIndex:true": "chưa bật hash một-based",
            "hash:true": "chưa bật hash",
            "throwOnError:true": "KaTeX chưa bật throwOnError",
            "RevealNotes": "thiếu RevealNotes",
            "RevealHighlight": "thiếu RevealHighlight",
            "RevealMath.KaTeX": "thiếu RevealMath.KaTeX",
        }
        compact = re.sub(r"\s+", "", source)
        for token, message in required.items():
            if re.sub(r"\s+", "", token) not in compact:
                self.fail(path, message)

        outer, depth = self.outer_section_count(source)
        if depth != 0:
            self.fail(path, f"ngăn xếp section không cân bằng, depth={depth}")
        if not 5 <= outer <= 7:
            self.fail(path, f"cần 5–7 section ngoài, nhận {outer}")

        slide_ids = re.findall(r'data-slide-id="([^"]+)"', source)
        if not slide_ids:
            self.fail(path, "không có data-slide-id")
        if len(slide_ids) != len(set(slide_ids)):
            self.fail(path, "data-slide-id bị trùng")
        notes = len(re.findall(r'<aside\s+class="notes">', source))
        if notes != len(slide_ids):
            self.fail(path, f"số ghi chú {notes} không khớp số trang {len(slide_ids)}")
        self.slide_total += len(slide_ids)

        headings = re.findall(r"<h[123]\b[^>]*>(.*?)</h[123]>", source, re.DOTALL | re.IGNORECASE)
        for heading in headings:
            text = re.sub(r"<[^>]+>", " ", html.unescape(heading))
            if PROHIBITED_HEADING_ENGLISH.search(text):
                self.fail(path, f"tiêu đề còn cụm tiếng Anh cần Việt hóa: {text.strip()}")

        if PUBLIC_META.search(source):
            match = PUBLIC_META.search(source)
            self.fail(path, f"nội dung công khai còn dấu vết quy trình: {match.group(0)!r}")
        if not re.search(rf'<div\s+class="footer">[^<]*Bài\s+(?:{number}|{int(number)})\s*</div>', source):
            self.fail(path, "chân trang thiếu hoặc sai số bài")

        for tag in re.findall(r"<(?:script|link|img)\b[^>]*>", source, re.IGNORECASE):
            for value in re.findall(r'(?:src|href)="([^"]+)"', tag):
                parsed = urllib.parse.urlsplit(html.unescape(value))
                if parsed.scheme in {"http", "https"} or parsed.netloc:
                    self.fail(path, f"tài nguyên cốt lõi phụ thuộc mạng: {value}")
                else:
                    self.validate_local_reference(path, value)

        for src in re.findall(r'<img\b[^>]*src="([^"]+)"', source, re.IGNORECASE):
            clean = urllib.parse.urlsplit(html.unescape(src)).path.lower()
            if not clean.endswith(".svg"):
                self.fail(path, f"ảnh không phải SVG: {src}")

    @staticmethod
    def validate_directives(markdown: str) -> list[str]:
        errors: list[str] = []
        opened: tuple[str, int] | None = None
        fence: str | None = None
        allowed = {"example", "derivation", "proof", "exercise", "hint", "solution"}
        for line_number, line in enumerate(markdown.splitlines(), 1):
            fence_match = re.match(r"^ {0,3}(```|~~~)", line)
            if fence_match:
                marker = fence_match.group(1)
                fence = None if fence == marker else marker if fence is None else fence
                continue
            if fence or line.startswith(("    ", "\t")):
                continue
            stripped = line.strip()
            if stripped == ":::":
                if opened is None:
                    errors.append(f"dòng {line_number}: dấu đóng ::: không có dấu mở")
                opened = None
                continue
            match = re.match(r"^:::\s*(\S+)", stripped)
            if not match:
                continue
            kind = match.group(1)
            if kind not in allowed:
                errors.append(f"dòng {line_number}: loại directive không hỗ trợ {kind!r}")
            if opened is not None:
                errors.append(f"dòng {line_number}: directive lồng trong khối mở ở dòng {opened[1]}")
            opened = (kind, line_number)
        if opened is not None:
            errors.append(f"dòng {opened[1]}: directive {opened[0]!r} chưa đóng")
        return errors

    def validate_note(self, number: str, path: Path) -> None:
        source = path.read_text(encoding="utf-8")
        if len(re.findall(r"^#\s+\S", source, re.MULTILINE)) != 1:
            self.fail(path, "lecture note phải có đúng một heading cấp một")
        if PUBLIC_META.search(source):
            match = PUBLIC_META.search(source)
            self.fail(path, f"nội dung công khai còn dấu vết quy trình: {match.group(0)!r}")
        for error in self.validate_directives(source):
            self.fail(path, error)
        for alt, src in re.findall(r"!\[([^]]*)\]\(([^)]+)\)", source):
            if not alt.strip():
                self.fail(path, f"hình thiếu alt text: {src}")
            clean = urllib.parse.urlsplit(src).path
            if not re.fullmatch(rf"img/lec-{number}/[A-Za-z0-9][A-Za-z0-9._-]*\.svg", clean):
                self.fail(path, f"hình nằm ngoài thư mục SVG của bài: {src}")
            self.validate_local_reference(TERM / "material-viewer.html", src)

    def validate_svg(self, path: Path) -> None:
        try:
            root = ET.parse(path).getroot()
        except (ET.ParseError, OSError) as error:
            self.fail(path, f"SVG không đọc được: {error}")
            return
        children = {element.tag.rsplit("}", 1)[-1] for element in root}
        if root.attrib.get("role") != "img":
            self.fail(path, 'SVG phải có role="img"')
        if "title" not in children or "desc" not in children:
            self.fail(path, "SVG phải có title và desc trực tiếp")
        self.svg_total += 1

    def validate_review_contract(self, number: str) -> None:
        path = TERM / f"planning/lec-{number}/review-log.md"
        if not path.is_file():
            return
        source = path.read_text(encoding="utf-8")
        requirements = {
            "DeepSeek": r"DeepSeek",
            "GLM": r"z-ai/glm-5\.3-flash|GLM",
            "OpenRouter": r"OpenRouter",
            "no-ai-slop": r"no-ai-slop",
            "quill": r"quill",
            "giới hạn writer": r"MCP_WRITE_POLICY|MCP_MAX_WRITE_CHARS|create-once|phạm vi DeepSeek|giới hạn DeepSeek|không (?:được )?sửa kho|một đầu ra",
        }
        for label, pattern in requirements.items():
            if not re.search(pattern, source, re.IGNORECASE):
                self.fail(path, f"thiếu bằng chứng {label}")

    def run(self) -> int:
        self.validate_layout()
        self.validate_index()
        for number, deck in self.deck_by_lecture.items():
            self.validate_deck(number, deck)
            self.validate_note(number, TERM / f"materials/lec-{number}/lecture-note.md")
            self.validate_review_contract(number)
        for svg in sorted((TERM / "img").glob("lec-*/*.svg")):
            self.validate_svg(svg)

        if self.errors:
            print(f"FAILED: {len(self.errors)} lỗi", file=sys.stderr)
            for error in self.errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        print(
            f"PASS: {len(LECTURES)} buổi, {self.slide_total} trang chiếu, "
            f"{self.svg_total} SVG, index và planning hợp lệ."
        )
        return 0


if __name__ == "__main__":
    raise SystemExit(Validation().run())
