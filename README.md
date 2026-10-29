# Học sâu · Học kỳ 1, 2026–2027

Kho này là nền RevealJS để xây dựng slide deck cho học phần **Học sâu**.

## Đưa tài liệu nguồn vào kho

Chép tài liệu vào các thư mục phù hợp:

```text
source-materials/
├── slides/       # PPTX, PDF hoặc slide HTML
├── textbooks/    # textbook, chương sách, lecture notes
├── papers/       # paper dùng để kiểm chứng hoặc bổ sung
└── resources/    # hình, dữ liệu, code và tài sản liên quan
```

Sau đó chỉ định rõ tệp hoặc nhóm tệp cần dùng cho một bài. Quy trình trong `AGENTS.md` không tự chọn bài khi chưa có chỉ dẫn.

## Gói web

```text
2627-1/
├── index.html
├── lecture-template.html
├── lecture-style.css
├── revealjs/
├── plugin/
├── vendor/
├── img/
└── planning/
```

Chạy máy chủ tại thư mục gốc:

```bash
../.venv/bin/python -m reloadserver 8765
```

Mở:

- `http://localhost:8765/`
- `http://localhost:8765/2627-1/`
- `http://localhost:8765/2627-1/lecture-template.html`

`lecture-template.html` chỉ là nền kỹ thuật. Khi tạo bài mới, phải thay toàn bộ placeholder, mã trang, ghi chú, nguồn và chân trang.

## Kiểm định

Kiểm định chạy cục bộ bằng công cụ dùng chung của workspace (`../tools/courses/deep-learning/`, không nằm trong kho này) và môi trường `../.venv`. Có hai cổng tuần tự:

1. kiểm định tĩnh cấu trúc 13 buổi, index, planning, RevealJS, SVG, liên kết và dấu vết quy trình trong nội dung công khai;
2. dựng toàn bộ deck và lecture note bằng Chromium (Playwright cho Python) ở khung rộng/hẹp, kiểm tra KaTeX, ảnh, tràn khung, bản in và biên an toàn của viewer.

Chạy từ thư mục gốc của kho:

```bash
../.venv/bin/python ../tools/courses/deep-learning/scripts/validate_course.py
../.venv/bin/python -m pytest ../tools/courses/deep-learning/tests
```

Kiểm định trình duyệt tự mở máy chủ tĩnh trên một cổng trống của `127.0.0.1`.
