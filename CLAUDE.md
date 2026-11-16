# CLAUDE.md

This repo holds the RevealJS lecture decks, lecture notes and planning files for **Học sâu** (UET.AI3056), semester 1 of 2026–2027 (`2627-1/`).

The workspace file `../CLAUDE.md` carries the rules shared by every course: environment, static-site rules, shared CSS, writing style, `no-ai-slop`/`quill`, the sub-agent policy, visual verification and git basics. This file holds only what is specific to this course. `AGENTS.md` is the full, authoritative specification, written in Vietnamese; `prompt_lecture_note_deck.md` is the `/goal` workflow (lecture note first, then deck). Precedence: the user's instructions first, then `AGENTS.md` (and `prompt_lecture_note_deck.md` when that workflow runs), then this file, then `../CLAUDE.md`. For new or rebuilt decks, `NGUYEN-TAC-TRANG-CHIEU.md` (NT1–NT28) ranks above the slide rules in `AGENTS.md` and this file, except the parameters in `AGENTS.md` §"Tham số trang chiếu của học phần"; existing decks keep the old rules until a logged revision the user asks for. Read the relevant section of `AGENTS.md` before any deck or note work.

## Repo map

| Path | Contents |
|---|---|
| `NGUYEN-TAC-TRANG-CHIEU.md` | Shared slide principles NT1–NT28; byte-identical copy of `../shared/docs/nguyen-tac-trang-chieu.md`, never edited here |
| `source.md` | Session-by-session source map: files and page ranges for each of the 13 sessions. **Read the session's entry in full before planning.** |
| `source-materials/{slides,textbooks,papers,resources}/` | Sources; the syllabus DOCX is in `resources/`, the course textbook draft is `textbooks/hocsau_draft.pdf` (binaries untracked) |
| `2627-1/lecture-NN-<ten-bai>.html` | One RevealJS deck per session (01–08, 10–14) |
| `2627-1/lecture-template.html` | Technical base for every deck; replace every placeholder |
| `2627-1/lecture-style.css` | Shared stylesheet, identical in every course; synced from `../shared/css/`, never edited here |
| `2627-1/lecture-course.css` | This course's deck styles (when present), loaded after `lecture-style.css` |
| `2627-1/revealjs/`, `plugin/`, `vendor/{katex,marked,dompurify}/` | Local runtime |
| `2627-1/img/lec-NN/` | SVG assets for each lecture |
| `2627-1/planning/lec-NN/` | `outline.md`, `storyboard.md`, `review-log.md`, `note-for-author.md` |
| `2627-1/materials/lec-NN/lecture-note.md` | Lecture note rendered by `material-viewer.{html,css,js}`; template in `materials/_templates/` |
| `2627-1/index.html` | Course index; one card per finished lecture |
| `.codex/` | Codex setup; the OpenRouter bridge it uses is `../tools/openrouter-mcp/` |
| `../tools/courses/deep-learning/` | Validator and browser tests (workspace tooling, not in this repo) |

## Commands

```bash
../.venv/bin/python -m reloadserver 8765          # from repo root; preview only (final deck checks: temporary http.server, NT28)
# deck: http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html
# note: http://localhost:8765/2627-1/material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html

../.venv/bin/python ../tools/courses/deep-learning/scripts/validate_course.py   # static gate: structure, index, planning, SVG, links
../.venv/bin/python -m pytest ../tools/courses/deep-learning/tests              # browser gate: every deck and note, wide/narrow, print
git diff --check
```

Both gates must pass before a deck or note is handed over. There is no CI on GitHub any more; these local runs replace it.

## Course-specific rules

- **Sessions:** decks exist only for sessions 01–08 and 10–14. Never build deck 09 (mid-term review) or 15 (wrap-up), never renumber, never reuse those numbers. `NN` is always two digits.
- **Source priority** (`AGENTS.md` §"Thứ tự ưu tiên nguồn"): user instruction → syllabus DOCX (sessions, topics, LLO, scope, boundaries; trace by `III.2 → Buổi N → field`) → the slides and page ranges `source.md` maps to the session (content and order) → `hocsau_draft.pdf`, papers, code → template and CSS → `AGENTS.md` conventions. The first draft Vietnamises exactly the mapped pages and keeps the slides' flow; the textbook only restores prerequisites, checks formulas, shapes and assumptions. Log every deviation in `review-log.md`.
- For a mapped session, the mapped files are the chosen source; don't ask again. Sessions 06, 13 and 14 have 13 user-approved extra PDFs (see `source.md`); stop and ask only if one is missing, unreadable, or content outside the approved ranges is needed. Never use `lec12_detection_intro.pdf`, `lec13_detection.pdf`, `lec18_diffusion.pdf`, `lec19_diffusion_editing.pdf` or `lec20_diffusion_systems.pdf` without explicit approval.
- Keep the two syllabus inconsistencies as they are (session 07 repeats `LLO3`; mid-term placed in week 8 vs session 09). Don't reconcile them.
- **Planning files:** four per lecture; `note-for-author.md` holds teaching routes, cut options, detailed answers, implementation hints and open checks — never on the slide face or in speaker notes, except that new or rebuilt decks put "Lời giải:" on the slide face and short answers in speaker notes (NT15, NT24).
- **Timing:** each session is two 50-minute lecture periods plus one 50-minute exercise period. The deck covers 120 minutes: a 100-minute core route and a 20-minute extension that can be cut. The exercise period is designed separately.
- **CSS:** decks link `lecture-style.css` then `lecture-course.css` (if the course has one). Use the existing colours, fonts, spacing, cards, grids and footer; no per-lecture design systems. Layout reference (never copy content, assets or CSS): `https://github.com/uet-iai-course/machine-learning`, `SLIDE_STYLE_GUIDE.md` and its `2526-2/lecture-*.html`.
- **RevealJS config:** `lang="vi"`, 1280×720, `controlsLayout: "edges"`, `slideNumber: true`, `hashOneBasedIndex: true`, `hash: true`; local `RevealMath.KaTeX`, `RevealNotes`, `RevealHighlight`; outer `<section>` per strand (5–7 strands incl. opening and conclusion), inner per slide; unique `data-slide-id`; footer at the end of `.slides`.
- **Titles:** no mixed English when a stable Vietnamese phrase exists ("Lan truyền xuôi phải giữ đúng kích thước tensor", not "Forward pass phải giữ đúng shape"). English stays only for names, models/architectures, APIs, standard symbols and common abbreviations (MLP, CNN, ReLU, LSTM, Transformer). Before handover, list every `h1`–`h3` and check each one.
- **Learning cycle per core concept:** vấn đề → trực giác → ví dụ → hình thức/tính toán → triển khai/ứng dụng → kiểm tra (`AGENTS.md` §"Cấu trúc học tập").
- **Deep-learning content standards** (`AGENTS.md` §"Tiêu chuẩn nội dung Học sâu"): state domain, dtype, shape, axis order, batch dimension, broadcasting and device before using a tensor; separate forward pass, loss, backward pass, optimizer step, train vs eval mode; check derivative variables, Jacobian/gradient shapes, signs and mean-vs-sum; name softmax/normalisation axes and stabilisation; for conv check channel order, kernel, stride, padding, dilation, output shape, receptive field; for attention give Q/K/V and head shapes, softmax axis, scale, mask, residual and normalisation. Recompute every shape, parameter count, gradient, loss and numeric example.
- **Code:** no demos the source doesn't have unless the user asks; keep source APIs and behaviour; show input/output shapes, train/eval mode, device and randomness when they matter; no long training runs or large downloads without the user's go-ahead.
- **Bullets:** at most two lines at 16:9.

## Sub-agents (course settings)

The policy in `../CLAUDE.md` applies. `AGENTS.md` §"Điều phối mô hình trong dự án" describes the **Codex** setup (OpenRouter reader/reviewer/writer workers through `../.venv/bin/openrouter-mcp-*`); that setup applies to Codex sessions only. In Claude Code, workflow roles are Claude sub-agents at effort `high`, following the stages of `AGENTS.md` §"Quy trình đa tác tử" (plan, source analysis and mapping, draft, storyboard gate, five independent reviews, revise, final check).

## Git (course settings)

- Within `prompt_lecture_note_deck.md` the user allows commit and push after each finished lecture note or deck (note commit first, deck commit second, each on `origin/main`). Outside that workflow, ask.
- A deck commit holds the HTML, SVGs, the four planning files, the index entry and shared changes that truly had to change.

## Done means

Follow `AGENTS.md` §"Tiêu chí hoàn thành": source flow kept and deviations logged; Vietnamese passed `no-ai-slop`; four planning files in place; every figure SVG or an approved raster exception; five independent reports with every required fix done; formulas, shapes, gradients, numbers, pseudocode and code checked; both local gates pass; `index.html` links finished lectures only. The handoff lists deck file, local URL, source files, redrawn figures, checks run, intended deviations, exceptions and remaining limits.
