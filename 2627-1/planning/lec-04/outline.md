# Bài 04 — Mạng nơ-ron tích chập

## Phạm vi và mục tiêu

- Chuẩn phạm vi: đề cương III.2 → Buổi 4, LLO7–LLO8.
- Đối tượng: sinh viên đã học MLP, lan truyền ngược và tối ưu hóa cơ bản.
- Tuyến trình chiếu: 100 phút lõi, 20 phút mở rộng/có thể cắt.
- Bài tập: 50 phút riêng.
- Sản phẩm: giải thích tính cục bộ và chia sẻ tham số; tính tương quan chéo; suy kích thước đầu ra, số tham số, số phép nhân–cộng; tính phép gộp và trường tiếp nhận.

## Nguồn đã chọn

1. `source-materials/resources/UET_Đề cương học phần_UET.AI3056_Học sâu_7460108.01.24.2506.docx`, III.2 → Buổi 4.
2. `source-materials/slides/lec08_cnn.pdf`, PDF 3–29, 38–42, 44–50, 52–53.
3. `source-materials/textbooks/hocsau_draft.pdf`, PDF 110–135.
4. Không dùng `lec08_cnn.pdf`, PDF 31–36; không dạy độ giãn.

## Hành trình khái niệm

MLP làm phẳng ảnh nhưng không mã hóa tường minh quan hệ cục bộ → kết nối cục bộ → chia sẻ tham số → tương quan chéo → vùng đệm và bước trượt → nhiều kênh → số tham số và MAC → phép gộp → trường tiếp nhận → tích chập với kích hoạt → thân mạng và đầu dự đoán → kết luận bốn phép kiểm.

## Bảy mạch

| # | Mạch | Vai trò | Kết nối vào | Kết nối ra | Dải slide | Phút |
|---|---|---|---|---|---|---:|
| 1 | Mở đầu: vấn đề làm phẳng và hai giả định | Nêu vấn đề tầng đầy đủ trên ảnh, giới thiệu quy ước, đưa ra cục bộ và chia sẻ | Đầu bài | Sang mạch 2: “hai giả định này thành phép tính nào?” | L04-00–07 | 20 |
| 2 | Tương quan chéo một kênh | Biến hai giả định thành phép tính kiểm chứng được trên ma trận nhỏ | Từ L04-07 | Sang mạch 3: “khóa trục và hình học cho cả lô” | L04-08–15 | 20 |
| 3 | Kích thước, nhiều kênh và chi phí | Mở rộng phép tính sang đệm, bước trượt, trục kênh, tham số và MAC | Từ L04-15 | Sang mạch 4: “sang phép tóm tắt không có tham số” | L04-16–28 | 34 |
| 4 | Phép gộp | Tóm tắt cửa sổ không tham số, giới hạn về bất biến | Từ L04-28 | Sang mạch 5: “đo vùng phụ thuộc của đơn vị sâu” | L04-29–32 | 11 |
| 5 | Trường tiếp nhận và thân mạng | Truy hồi $r,j$, ví dụ bước trượt, cầu nối thân–đầu mạng | Từ L04-32 | Sang mạch 6 (mở rộng) hoặc mạch 7 (kết luận) | L04-33–37 | 12 |
| 6 | Mở rộng có thể cắt | Biến thể: nhân cạnh, 1×1, gradient qua gộp, dấu vết LeNet, huấn luyện | Từ L04-37 (nhấn phải) | Sang mạch 7 (nhấn phải sau X05) | L04-X01–X05 | 20 |
| 7 | Kết luận | Bốn phép kiểm, thu hồi vấn đề mở đầu | Từ L04-37 (tuyến lõi: End) hoặc từ X05 (tuyến đầy đủ: nhấn phải) | Kết thúc deck | L04-38 | 3 |

Tuyến lõi mạch 1–5 cộng mạch 7 = 100 phút; mạch 6 mở rộng = 20 phút; toàn tuyến = 120 phút; bài tập 50 phút tách riêng.

## Ánh xạ nguồn

| Cụm | Nguồn | Quyết định |
|---|---|---|
| MLP và ảnh | slide PDF 3–5; GT PDF 110–112 | Sửa thành làm phẳng giữ giá trị nhưng không mã hóa hoặc khai thác tường minh quan hệ cục bộ |
| Cục bộ, chia sẻ, tương đương dịch chuyển | slide PDF 5–7; GT PDF 111–114 | Sửa “bất biến” thành tương đương dịch chuyển ở bản đồ đặc trưng; nêu ngoại lệ biên và bước trượt |
| Tương quan chéo | GT PDF 116–119 | Ví dụ một kênh lấy từ GT PDF 116–119 thay ví dụ tương quan chéo slide S8–16 vì nhỏ, đủ dữ kiện và kiểm tra được |
| Vùng đệm, bước trượt, kích thước | slide PDF 17–20; GT PDF 119–123 | Dùng vùng đệm bốn phía, bước trượt hai chiều; không đưa độ giãn; công thức trường tiếp nhận stride-2 ở slide PDF 50 sai/không tổng quát nên thay bằng truy hồi $r,j$ đã kiểm chứng |
| Nhiều kênh và nhiều đầu ra | slide PDF 21–29; GT PDF 123–126 | Khóa NCHW/OIHW; tổng qua mọi kênh vào; slide S29 đổi ký hiệu $K,L$ sang $C_{in},C_{out}$ |
| Chi phí | slide PDF 29; GT PDF 126–127 | Tách tham số và MAC; không đổi MAC thành FLOPs |
| Phép gộp | slide PDF 38–42; GT PDF 127–130 | Tách theo kênh, không tham số, không tuyên bố bất biến tuyệt đối |
| Trường tiếp nhận | slide PDF 44–50 | Dùng truy hồi tổng quát $r,j$ thay công thức riêng lẻ |
| Thân mạng và đầu dự đoán | slide PDF 52–53; GT PDF 131–132 | Cầu nối từ tensor đặc trưng tới logits |
| LeNet và huấn luyện | GT PDF 131–135 | Chỉ dùng ở tuyến mở rộng; không lịch sử hoặc kết quả định lượng; không dùng ví dụ học nhân GT 4.2.3 vì nguồn chính đã đủ trực giác và không cần mở thí nghiệm học nhân |

## Quy ước tensor và ký hiệu

| Đại lượng | Kích thước/quy ước |
|---|---|
| $X$ | $N\times C_{in}\times H_{in}\times W_{in}$, thứ tự NCHW |
| $W$ | $C_{out}\times C_{in}\times K_h\times K_w$, thứ tự OIHW |
| $K$ | một nhân trong ví dụ một kênh; khi tổng quát hóa, nó tương ứng một lát của $W$ |
| $\widetilde X$ | tensor $X$ sau khi đệm 0, dùng để tránh chỉ số âm hoặc ngoài miền |
| $b$ | $C_{out}$ |
| $Y$ | $N\times C_{out}\times H_{out}\times W_{out}$ |
| $P_t,P_b,P_l,P_r$ | đệm trên, dưới, trái, phải |
| $S_h,S_w$ | bước trượt theo chiều cao, rộng; thuộc $\mathbb{Z}_{>0}$ |
| MAC | một phép nhân–cộng; không đồng nhất với FLOPs |
| $r_l,j_l$ | kích thước trường tiếp nhận và khoảng nhảy hiệu dụng ở tầng $l$ |

## Ranh giới

- Không tạo mã trình diễn.
- Không dùng raster.
- Ma trận, công thức và phép tính dựng bằng HTML/KaTeX, không đưa vào SVG.
- Không dạy độ giãn, tích chập theo nhóm hoặc tích chập riêng từng kênh trong tuyến này.
