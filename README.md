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

## Kiểm định tự động

GitHub Actions chạy kiểm định khi học liệu hoặc mã kiểm thử thay đổi. Workflow gồm hai cổng tuần tự:

1. kiểm định tĩnh cấu trúc 13 buổi, index, planning, RevealJS, SVG, liên kết và dấu vết quy trình trong nội dung công khai;
2. dựng toàn bộ deck và lecture note bằng Chromium ở khung rộng/hẹp, kiểm tra KaTeX, ảnh, tràn khung, bản in và biên an toàn của viewer.

Chạy cổng tĩnh tại máy cục bộ:

```bash
npm run test:static
```

Chạy đầy đủ với Node.js 20 trở lên:

```bash
npm ci
npx playwright install --with-deps chromium
npm test
```

Playwright tự mở máy chủ chỉ trên `127.0.0.1:8765`. Khi kiểm định trình duyệt thất bại trên GitHub Actions, báo cáo, ảnh chụp và trace được lưu trong artifact `playwright-report` trong 14 ngày.
