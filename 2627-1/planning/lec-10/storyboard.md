# Storyboard Bài 10

## Bản đồ chu trình học tập

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính toán | Triển khai/ứng dụng | Kiểm tra | Dữ kiện truyền |
|---|---|---|---|---|---|---|---|
| Nút thắt và truy xuất | L10-02–03 | L10-04–05 | L10-04–06 | L10-06–07 | L10-05–07 | L10-06 | $s_{t'-1}$ truy xuất $H_{1:T_s}$ thay ngữ cảnh cố định |
| Vết số tổng hợp | L10-08 | L10-08–09 | L10-08–12 | L10-09–12 | L10-11–12 | L10-13 | $e=(1,2,0)$ → $\alpha$ → $c$ |
| Điểm và mặt nạ | L10-14 | L10-14 | L10-18 dùng lại vết số | L10-15–17 | L10-16–18 | L10-18 | $S^-,H,M^{src},D_a$ → $E,A,C$ |
| Bộ giải mã | L10-19 | L10-19–20 | L10-21–22 | L10-19–21 | L10-20–22 | L10-23 | $c_{t'}$ → $s_{t'}$ → logit; token đúng hoặc dự đoán |
| Căn chỉnh và giới hạn | L10-24 | L10-24 | L10-25 | L10-24–25 | L10-24–26 | L10-26 | Ba hàng trọng số; mỗi hàng là phân phối trên nguồn |
| Thuật toán và tổng hợp | L10-27 | L10-27 | L10-31 dùng lại toàn bộ vết | L10-27–29 | L10-28–30 | L10-31 | Mặt nạ nguồn/đích, đạo hàm, chi phí và kết luận có điều kiện |
| Cầu nối tự chú ý | L10-32 | L10-32 | không áp dụng: chỉ khóa nguồn Q/K/V | L10-32 | L10-32 | không áp dụng: Bài 11 tiếp tục | Chú ý chéo → Q/K/V cùng một chuỗi |
| Ứng dụng mở rộng | L10-X01 | L10-X01–X03 | L10-X01–X03 | L10-X02–X03 | L10-X01–X03 | L10-X04 | Token nguồn, vùng ảnh hoặc token câu kia làm khóa/giá trị |

L10-08 mở bộ số trước công thức softmax ở L10-09. L10-14 tạo trực giác mạng điểm trước công thức và bảng kích thước L10-15. L10-32 là cầu nối một trang; không triển khai self-attention của Bài 11.

## Thời lượng và điều hướng

| Trang | Phút | Tuyến | Vai trò trung tâm | Điều hướng |
|---|---:|---|---|---|
| L10-00 | 2 | Lõi | Mở bài | Xuống |
| L10-01 | 3 | Lõi | LLO và tiên quyết | Xuống |
| L10-02 | 3 | Lõi | Nút thắt cố định | Xuống |
| L10-03 | 3 | Lõi | Nhu cầu truy xuất | Xuống |
| L10-04 | 3 | Lõi | Chu trình chú ý | Xuống |
| L10-05 | 4 | Lõi | Sơ đồ chú ý chéo | Xuống |
| L10-06 | 3 | Lõi | Q/K/V và kiểm tra | Xuống |
| L10-07 | 4 | Lõi | Hợp đồng tensor | Xuống |
| L10-08 | 3 | Lõi | Dữ kiện vết số | Xuống |
| L10-09 | 3 | Lõi | Softmax ổn định | Xuống |
| L10-10 | 4 | Lõi | Tính trọng số | Xuống |
| L10-11 | 4 | Lõi | Tính ngữ cảnh | Xuống |
| L10-12 | 2 | Lõi | Tổ hợp lồi | Xuống |
| L10-13 | 2 | Lõi | Kiểm tra tổng hợp | Xuống |
| L10-14 | 3 | Lõi | Trực giác điểm cộng | Xuống |
| L10-15 | 4 | Lõi | Công thức và tham số | Xuống |
| L10-16 | 4 | Lõi | Phát tự động | Xuống |
| L10-17 | 3 | Lõi | Mặt nạ trước softmax | Xuống |
| L10-18 | 2 | Lõi | Vết số có đệm | Xuống |
| L10-19 | 3 | Lõi | Cập nhật giải mã | Xuống |
| L10-20 | 4 | Lõi | Logit và mất mát | Xuống |
| L10-21 | 3 | Lõi | Học theo đáp án | Xuống |
| L10-22 | 3 | Lõi | Suy luận tự hồi quy | Xuống |
| L10-23 | 3 | Lõi | Kiểm tra hai chế độ | Xuống |
| L10-24 | 3 | Lõi | Ma trận căn chỉnh | Xuống |
| L10-25 | 4 | Lõi | Ba hàng điểm | Xuống |
| L10-26 | 3 | Lõi | Giới hạn diễn giải | Xuống |
| L10-27 | 4 | Lõi | Thuật toán một bước | Xuống |
| L10-28 | 3 | Lõi | Đường đạo hàm và hai mặt nạ | Xuống |
| L10-29 | 3 | Lõi | Chi phí theo cặp | Xuống |
| L10-30 | 2 | Lõi | So sánh thiết kế | Xuống |
| L10-31 | 2 | Lõi | Kiểm tra toàn vết | Xuống |
| L10-32 | 1 | Lõi | Cầu nối tự chú ý | Phải sang mở rộng |
| L10-X01 | 5 | Mở rộng | Mô tả ảnh | Xuống |
| L10-X02 | 5 | Mở rộng | Tập khóa–giá trị | Xuống |
| L10-X03 | 5 | Mở rộng | Cặp văn bản | Xuống |
| L10-X04 | 5 | Mở rộng | Kiểm tra ánh xạ | Kết thúc |

Tổng tuyến lõi: **100 phút**. Tổng tuyến mở rộng: **20 phút**. Bài tập tách riêng: **50 phút**.

## Bài tập 50 phút

| Hoạt động | Phút | Đầu vào | Sản phẩm |
|---|---:|---|---|
| Phân tích nút thắt | 10 | Hai thiết kế ngữ cảnh | Hai hạn chế cụ thể và một cơ chế khắc phục |
| Tính chú ý trên ma trận nhỏ | 20 | Vết $H,e$ và một mặt nạ | $\alpha,c$ đúng trục, đúng số |
| Đọc căn chỉnh | 15 | Ma trận $3\times3$ | Ba nhận xét có điều kiện, không suy diễn nhân quả |
| Giới hạn diễn giải | 5 | Một mệnh đề về ô lớn nhất | Phản biện ngắn và đề xuất kiểm tra can thiệp |

## Điều hướng

- Đi xuống liên tục trong tuyến lõi L10-00–L10-32; các chuyển đoạn được nói trong ghi chú diễn giả, không đổi hướng điều hướng.
- Chỉ đi phải tại L10-32 để sang L10-X01, rồi đi xuống đến L10-X04 cho tuyến mở rộng.

## Lý do tồn tại và đầu ra kiểm chứng

| Cụm trang | Lý do tồn tại | Đầu ra kiểm chứng được |
|---|---|---|
| L10-00–01 | Khóa vấn đề, LLO và tiên quyết trước ký hiệu | Người học nêu được hai sản phẩm cần đạt |
| L10-02–04 | Tách baseline, nút thắt và chu trình thay thế | Xác định trạng thái cuối hợp lệ, $s_0$, và ba bước score–softmax–sum |
| L10-05–07 | Nối trực giác với Q/K/V và hợp đồng batch-first | Gán đúng nguồn của Q/K/V và shape $H,S^-,E,A,C$ |
| L10-08–13 | Tạo vết số xuyên suốt trước khi mở mạng score | Tính đúng $\alpha,c$, trục rút gọn và tính chất tổ hợp lồi |
| L10-14–18 | Mở hàm điểm, broadcasting và masked softmax | Kiểm được phép nhân vector hàng, phép co $D_a$ và vết có padding |
| L10-19–23 | Nối context sang decoder, logit, train và inference | Viết đúng shape đầu ra, target shift, EOS và active mask |
| L10-24–26 | Đọc heatmap có nhãn nhưng giới hạn suy diễn | Phân biệt dữ liệu tự xây, căn chỉnh mềm và bằng chứng nhân quả |
| L10-27–31 | Khép thuật toán, loss, gradient, chi phí và trace | Nêu sáu bước, ba đường gradient, reduction và độ phức tạp |
| L10-32 | Tạo cầu nối tối thiểu sang Bài 11 | Phân biệt nguồn Q/K/V của cross-attention và self-attention |
| L10-X01–X04 | Kiểm tra khả năng chuyển cơ chế sang miền khác | Ánh xạ đúng Q/K/V và trục softmax cho ảnh, tập và cặp văn bản |
