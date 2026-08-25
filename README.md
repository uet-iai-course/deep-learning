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
python3 -m reloadserver 8765
```

Mở:

- `http://localhost:8765/`
- `http://localhost:8765/2627-1/`
- `http://localhost:8765/2627-1/lecture-template.html`

`lecture-template.html` chỉ là nền kỹ thuật. Khi tạo bài mới, phải thay toàn bộ placeholder, mã trang, ghi chú, nguồn và chân trang.
