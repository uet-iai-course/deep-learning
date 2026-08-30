# Storyboard Bài 10

## Chức năng và kết nối của bảy mạch

| Mạch | Trang | Chức năng | Kết nối vào | Đầu ra cho mạch sau |
|---|---|---|---|---|
| 1 | L10-00–03 | Đặt bài toán nút thắt ngữ cảnh cố định | Bộ mã hóa–giải mã đã học | Bộ giải mã cần truy xuất trạng thái nguồn theo bước |
| 2 | L10-04–07 | Mô tả chu trình truy xuất, định nghĩa chú ý tổng quát và khóa Q/K/V | Nhu cầu truy xuất | Định nghĩa $\operatorname{Attention}(q,\{(k_i,v_i)\})$ và hợp đồng $H,S^-,E,A,C$ |
| 3 | L10-08–13 | Cho một vết tính kiểm tra được | Hợp đồng tensor | Điểm cần được tạo bởi hàm học được |
| 4 | L10-14–18 | Xây hàm điểm và masked softmax | Điểm và giá trị của vết số | Ngữ cảnh hợp lệ $c_{t'}$ |
| 5 | L10-19–26 | Nối chú ý vào giải mã và giới hạn cách đọc căn chỉnh | $c_{t'}$ | Sáu phép tính của một bước giải mã |
| 6 | L10-27–31 | Tổng hợp thuật toán, gradient, chi phí và kiểm tra | Toàn bộ đường tính | Nhánh ứng dụng hoặc kết luận chung |
| 7 | L10-X01–X04, L10-32 | Kiểm tra khả năng chuyển miền; kết luận chung | Q/K/V trong dịch máy | Cầu sang Bài 11 từ nguồn tạo Q/K/V |

## Bản đồ chu trình học tập

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính toán | Triển khai/ứng dụng | Kiểm tra | Dữ kiện truyền |
|---|---|---|---|---|---|---|---|
| Nút thắt và truy xuất | L10-02–03 | L10-04–05 | L10-04–06 | L10-06–07 | L10-05–07 | L10-06 là kiểm tra trực giác trước khi L10-07 khóa kích thước | $s_{t'-1}$ truy xuất $H_{1:T_s}$ qua định nghĩa tổng quát thay ngữ cảnh cố định |
| Vết số tổng hợp | L10-08 | L10-08–09 | L10-08–12 | L10-09–12 | L10-11–12 | L10-13 | $e=(1,2,0)$ → $\alpha$ → $c$ |
| Điểm và mặt nạ | L10-14 | L10-14 | L10-18 dùng lại vết số | L10-15–17 | L10-16–18 | L10-18 | $S^-,H,M^{src},D_a$ → $E,A,C$ |
| Bộ giải mã | L10-19 | L10-19–20 | L10-21–22 | L10-19–21 | L10-20–22 | L10-23 | $c_{t'}$ → $s_{t'}$ → logit; token đúng hoặc dự đoán |
| Căn chỉnh và giới hạn | L10-24 | L10-24 | L10-25 | L10-24–25 | L10-24–26 | L10-26 | Ba hàng trọng số; mỗi hàng là phân phối trên nguồn |
| Thuật toán và tổng hợp | L10-27 | L10-27 | L10-31 dùng lại toàn bộ vết | L10-27–29 | L10-28–30 | L10-29 kiểm tra chi phí theo cặp; L10-31 kiểm tra toàn vết | Mặt nạ nguồn/đích, đạo hàm, chi phí và đối chiếu thiết kế |
| Ứng dụng mở rộng | L10-X01 | L10-X01–X03 | L10-X01–X03 | L10-X02 áp dụng định nghĩa tổng quát sang nhiều miền; L10-X03 căn chỉnh cặp văn bản | L10-X01–X03 | L10-X04 | Token nguồn, vùng ảnh hoặc token câu kia làm khóa/giá trị |
| Kết luận và cầu nối | L10-32 | L10-32 | không áp dụng: trang thu hồi mạch đã học | L10-32 | L10-32 | không áp dụng: Bài 11 tiếp tục | Nút thắt → truy xuất theo bước → Q/K/V → cùng một chuỗi |

L10-08 mở bộ số trước công thức softmax ở L10-09. L10-14 tạo trực giác mạng điểm trước công thức và bảng kích thước L10-15. Mạch 7 có chức năng kép: bốn trang mở rộng kiểm tra khả năng chuyển miền, còn L10-32 là kết luận bắt buộc của cả hai tuyến. L10-32 chỉ nêu nguồn tạo Q/K/V để nối Bài 11, không triển khai tự chú ý.

## Thời lượng và điều hướng

| Trang | Phút | Tuyến | Vai trò trung tâm | Điều hướng |
|---|---:|---|---|---|
| L10-00 | 2 | Lõi | Mở bài | Xuống |
| L10-01 | 3 | Lõi | LLO và tiên quyết | Xuống |
| L10-02 | 3 | Lõi | Nút thắt cố định | Xuống |
| L10-03 | 3 | Lõi | Nhu cầu truy xuất | Phải tới L10-04 |
| L10-04 | 3 | Lõi | Chu trình chú ý | Xuống |
| L10-05 | 4 | Lõi | Sơ đồ chú ý chéo | Xuống |
| L10-06 | 3 | Lõi | Q/K/V và kiểm tra | Xuống |
| L10-07 | 4 | Lõi | Hợp đồng tensor | Phải tới L10-08 |
| L10-08 | 3 | Lõi | Dữ kiện vết số | Xuống |
| L10-09 | 3 | Lõi | Softmax ổn định | Xuống |
| L10-10 | 4 | Lõi | Tính trọng số | Xuống |
| L10-11 | 4 | Lõi | Tính ngữ cảnh | Xuống |
| L10-12 | 2 | Lõi | Tổ hợp lồi | Xuống |
| L10-13 | 2 | Lõi | Kiểm tra tổng hợp | Phải tới L10-14 |
| L10-14 | 3 | Lõi | Trực giác điểm cộng | Xuống |
| L10-15 | 4 | Lõi | Công thức và tham số | Xuống |
| L10-16 | 4 | Lõi | Phát tự động | Xuống |
| L10-17 | 3 | Lõi | Mặt nạ trước softmax | Xuống |
| L10-18 | 2 | Lõi | Vết số có đệm | Phải tới L10-19 |
| L10-19 | 3 | Lõi | Cập nhật giải mã | Xuống |
| L10-20 | 4 | Lõi | Logit và mất mát | Xuống |
| L10-21 | 3 | Lõi | Học theo đáp án | Xuống |
| L10-22 | 3 | Lõi | Suy luận tự hồi quy | Xuống |
| L10-23 | 3 | Lõi | Kiểm tra hai chế độ | Xuống |
| L10-24 | 3 | Lõi | Ma trận căn chỉnh | Xuống |
| L10-25 | 4 | Lõi | Ba hàng điểm | Xuống |
| L10-26 | 3 | Lõi | Giới hạn diễn giải | Phải tới L10-27 |
| L10-27 | 4 | Lõi | Thuật toán một bước | Xuống |
| L10-28 | 3 | Lõi | Đường đạo hàm và hai mặt nạ | Xuống |
| L10-29 | 3 | Lõi | Đánh đổi giữa chi phí theo cặp và truy xuất động | Xuống |
| L10-30 | 2 | Lõi | Đối chiếu hai biến thể cơ sở | Xuống |
| L10-31 | 2 | Lõi | Kiểm tra toàn vết | End tới L10-32 hoặc Phải vào L10-X01 |
| L10-X01 | 5 | Mở rộng | Mô tả ảnh | Xuống |
| L10-X02 | 5 | Mở rộng | Tập khóa–giá trị | Xuống |
| L10-X03 | 5 | Mở rộng | Cặp văn bản | Xuống |
| L10-X04 | 5 | Mở rộng | Kiểm tra ánh xạ | Xuống tới L10-32 |
| L10-32 | 1 | Lõi | Kết luận và cầu sang Bài 11 | Kết thúc |

Tổng tuyến lõi: **100 phút**. Tổng tuyến mở rộng: **20 phút**. Bài tập tách riêng: **50 phút**.

## Bài tập 50 phút

| Hoạt động | Phút | Đầu vào | Sản phẩm |
|---|---:|---|---|
| Phân tích nút thắt | 10 | Hai thiết kế ngữ cảnh | Hai hạn chế cụ thể và một cơ chế khắc phục |
| Tính chú ý trên ma trận nhỏ | 20 | Vết $H,e$ và một mặt nạ | $\alpha,c$ đúng trục, đúng số |
| Đọc căn chỉnh | 15 | Ma trận $3\times3$ | Ba nhận xét có điều kiện, không suy diễn nhân quả |
| Giới hạn diễn giải | 5 | Một mệnh đề về ô lớn nhất | Phản biện ngắn và đề xuất kiểm tra can thiệp |

## Điều hướng

- Đi xuống trong từng mạch. Phím Phải được định tuyến lại tại sáu ranh giới L10-03→04, 07→08, 13→14, 18→19, 26→27 và 31→X01 để không phụ thuộc chỉ số dọc Reveal đã nhớ.
- Tuyến lõi: tại L10-31, nhấn End để đến L10-32 và kết thúc.
- Tuyến đầy đủ: tại L10-31, nhấn Phải để vào L10-X01; đi xuống qua X02, X03, X04 rồi đến L10-32.
- End luôn đến L10-32; các phím khác giữ hành vi mặc định.

## Lý do tồn tại và đầu ra kiểm chứng

| Cụm trang | Lý do tồn tại | Đầu ra kiểm chứng được |
|---|---|---|
| L10-00–01 | Khóa vấn đề, LLO và tiên quyết trước ký hiệu | Người học nêu được hai sản phẩm cần đạt |
| L10-02–04 | Tách baseline, nút thắt và chu trình thay thế | Xác định trạng thái cuối hợp lệ, $s_0$, và ba bước score–softmax–sum |
| L10-05–07 | Nối trực giác với định nghĩa chú ý tổng quát, Q/K/V và hợp đồng theo lô | Gán đúng nguồn của Q/K/V và kích thước $H,S^-,E,A,C$ |
| L10-08–13 | Tạo vết số xuyên suốt trước khi mở mạng score | Tính đúng $\alpha,c$, trục rút gọn và tính chất tổ hợp lồi |
| L10-14–18 | Mở hàm điểm, broadcasting và masked softmax | Kiểm được phép nhân vector hàng, phép co $D_a$ và vết có padding |
| L10-19–23 | Nối context sang decoder, logit, train và inference | Viết đúng shape đầu ra, target shift, EOS và active mask |
| L10-24–26 | Đọc heatmap có nhãn nhưng giới hạn suy diễn | Phân biệt dữ liệu tự xây, căn chỉnh mềm và bằng chứng nhân quả |
| L10-27–31 | Khép thuật toán, loss, gradient, chi phí và trace | Nêu sáu bước, ba đường gradient, reduction và độ phức tạp |
| L10-X01–X04 | Kiểm tra khả năng chuyển cơ chế sang miền khác | Ánh xạ đúng Q/K/V và trục softmax cho ảnh, tập và cặp văn bản |
| L10-32 | Thu hồi nút thắt, truy xuất theo bước và Q/K/V; tạo cầu tối thiểu sang Bài 11 | Nêu được cơ chế đã học và điểm đổi nguồn Q/K/V ở bài sau |
