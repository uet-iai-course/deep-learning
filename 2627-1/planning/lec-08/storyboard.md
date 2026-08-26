# Storyboard Bài 08

## Bản đồ hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính toán | Triển khai/ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Dữ kiện truyền | Câu nối |
|---|---|---|---|---|---|---|---|---|---|
| Đường lưu giữ | L08-02–03 | L08-02–04 | không áp dụng: kế thừa tích Jacobian của Bài 07 | L08-05–06 | L08-05–06 | L08-06 | BPTT và gradient dài → hai trạng thái, độ dài thật và mặt nạ nguồn | $X_t,H_{t-1},C_{t-1},L_n,M^{src}$ | “Hợp đồng đã khóa; ta xây từng tín hiệu của ô.” |
| Cơ chế LSTM | L08-07 | L08-07–11 | L08-12–15 | L08-16–17 | L08-15–17 | L08-17; L08-15 chỉ là hoạt động trong ví dụ | Nhu cầu giữ/ghi → một bước LSTM rồi phương trình và kiểm tra kích thước | $a_i,a_f,a_o,a_g$ → $I,F,O,G,C,H$ | “Đường cập nhật cộng cho phép tách một nhánh gradient.” |
| Gradient LSTM | L08-18 | L08-18–19 | L08-20 với $F=(.95,.8,.9,1,.7)$ | L08-18–20 | L08-20 | L08-21 | Ô hoàn chỉnh → nhánh trực tiếp và đạo hàm toàn phần | $F_t$, tích $.4788$, các đường qua $H$ | “Có thể đơn giản hóa cơ chế cổng nhưng phải khóa quy ước.” |
| Cơ chế GRU | L08-22 | L08-22–23 | L08-24,26 | L08-25,27–29 | L08-28–29 | L08-29 | LSTM → GRU một trạng thái → ví dụ → phương trình → đổi quy ước | $R,Z,\widetilde H,H$; $Z_s=1-Z_g$, $a_s=-a_g$ | “Trạng thái có cổng có thể xếp tầng hoặc đọc theo hai hướng.” |
| Mạng truy hồi sâu | L08-30 | L08-30 | L08-31 | L08-31 | L08-30–31 | L08-31 có câu hỏi kích thước và fragment | Một tầng → nhiều tầng với trạng thái tổng quát | $S=H$ hoặc $(H,C)$; $D_{\ell-1}\to D_\ell$ | “Thêm hướng đọc là một lựa chọn khác với thêm tầng.” |
| RNN hai chiều | L08-32 | L08-32–33 | L08-33 | L08-32 | L08-33 | L08-33 | Chuỗi đã biết đủ → biểu diễn hai phía | $\overrightarrow H_t,\overleftarrow H_t,H_t\in\mathbb R^{N\times2D_h}$ | “Hai chuỗi không căn chỉnh cần tách đọc và sinh.” |
| Dịch máy | L08-34 | L08-34–36 | L08-37 | L08-35–38 | L08-36–39 | L08-39 có câu hỏi hợp đồng và fragment | Hai chuỗi khác độ dài → GRU mã hóa, GRU giải mã, logit và mất mát | $L_n,Q,S,A,M^{src},M^{tgt}$ | Kết thúc tuyến lõi. |
| Ứng dụng và đối chiếu mở rộng | L08-X01 | L08-X01 | L08-X02–X03 | L08-X01–X03 | L08-X01–X03 | L08-X04 | Cơ chế lõi → gộp cảm xúc, chi phí, vết sinh tự hồi quy | $q_n$, số tham số, $\langle bos\rangle\to\hat y_1\to\hat y_2$ | Kết thúc bài. |

Các bước được gộp khi cùng một tensor hoặc đồ thị phục vụ cả trực giác và ứng dụng. Cụm đường lưu giữ kế thừa trực tiếp tích Jacobian của Bài 07. L08-12–15 là ví dụ LSTM; L08-15 chỉ là hoạt động tính trong ví dụ, còn L08-17 mới khép chu trình bằng kiểm tra kích thước. Cụm GRU khóa dữ kiện ở L08-24 trước phương trình L08-25. L08-31 và L08-39 đều có câu hỏi cùng phản hồi dạng fragment, nên cụm mạng sâu và dịch máy có kiểm tra thực sự.

## Thời lượng và điều hướng

| Trang | Phút | Tuyến | Vai trò trung tâm | Điều hướng |
|---|---:|---|---|---|
| L08-00 | 2 | Lõi | Mở bài | Xuống |
| L08-01 | 2 | Lõi | LLO và tiên quyết | Phải |
| L08-02 | 3 | Lõi | Cầu nối gradient | Xuống |
| L08-03 | 3 | Lõi | Nhu cầu giữ và cập nhật | Xuống |
| L08-04 | 2 | Lõi | Hai trạng thái của LSTM | Xuống |
| L08-05 | 3 | Lõi | Hợp đồng tensor | Xuống |
| L08-06 | 2 | Lõi | Khởi tạo và mặt nạ nguồn | Phải |
| L08-07 | 2 | Lõi | Bản đồ bốn tín hiệu LSTM | Xuống |
| L08-08 | 2 | Lõi | Ứng viên | Xuống |
| L08-09 | 2 | Lõi | Cổng vào | Xuống |
| L08-10 | 2 | Lõi | Cổng ra | Xuống |
| L08-11 | 3 | Lõi | Cổng quên và ô hoàn chỉnh | Xuống |
| L08-12 | 3 | Lõi | Dữ kiện ví dụ LSTM | Xuống |
| L08-13 | 2 | Lõi | Tính các cổng | Xuống |
| L08-14 | 2 | Lõi | Tính trạng thái ô | Xuống |
| L08-15 | 3 | Lõi | Tính trạng thái ẩn và kiểm tra | Xuống |
| L08-16 | 3 | Lõi | Phương trình tổng quát | Xuống |
| L08-17 | 2 | Lõi | Kích thước và phát tự động | Phải |
| L08-18 | 2 | Lõi | Đạo hàm nhánh trực tiếp | Xuống |
| L08-19 | 3 | Lõi | Đạo hàm toàn phần | Xuống |
| L08-20 | 3 | Lõi | Ví dụ và tích cổng quên | Xuống |
| L08-21 | 2 | Lõi | Kiểm tra giới hạn mệnh đề | Phải |
| L08-22 | 3 | Lõi | Động cơ GRU | Xuống |
| L08-23 | 2 | Lõi | Hai cổng GRU | Xuống |
| L08-24 | 3 | Lõi | Dữ kiện và hai cổng GRU | Xuống |
| L08-25 | 2 | Lõi | Phương trình GRU | Xuống |
| L08-26 | 3 | Lõi | Tính ứng viên và trạng thái GRU | Xuống |
| L08-27 | 3 | Lõi | Ánh xạ hai quy ước | Xuống |
| L08-28 | 2 | Lõi | Số tham số | Xuống |
| L08-29 | 3 | Lõi | Kiểm tra so sánh | Phải |
| L08-30 | 2 | Lõi | RNN sâu | Xuống |
| L08-31 | 3 | Lõi | Shape theo tầng | Phải |
| L08-32 | 2 | Lõi | RNN hai chiều | Xuống |
| L08-33 | 3 | Lõi | Điều kiện có tương lai | Phải |
| L08-34 | 2 | Lõi | Hai chuỗi không căn chỉnh | Xuống |
| L08-35 | 3 | Lõi | Bộ mã hóa | Xuống |
| L08-36 | 3 | Lõi | Bộ giải mã | Xuống |
| L08-37 | 2 | Lõi | Học theo đáp án | Xuống |
| L08-38 | 3 | Lõi | Mất mát có mặt nạ | Xuống |
| L08-39 | 3 | Lõi | Kiểm tra hợp đồng mã hóa–giải mã | Phải để vào mở rộng |
| L08-X01 | 5 | Mở rộng | Phân tích cảm xúc | Xuống |
| L08-X02 | 5 | Mở rộng | Ví dụ số tham số | Xuống |
| L08-X03 | 5 | Mở rộng | Vết sinh tự hồi quy | Xuống |
| L08-X04 | 5 | Mở rộng | Kiểm tra lựa chọn kiến trúc | Kết thúc |

Tổng tuyến lõi: **100 phút**. Tổng tuyến mở rộng: **20 phút**. Bài tập tách riêng: **50 phút**.

## Bài tập 50 phút

| Hoạt động | Phút | Đầu vào | Sản phẩm |
|---|---:|---|---|
| Tính một bước LSTM | 20 | Bộ số ở L08-12 và một bộ tiền kích hoạt mới | $I,F,O,G,C,H$ có bốn chữ số |
| Phân tích đường gradient | 10 | Dãy giá trị $F_1,\ldots,F_5$ | Tích nhánh trực tiếp và phát biểu giới hạn |
| So sánh LSTM và GRU | 10 | $D_x,D_h$ và hai phương trình | Số tham số, số trạng thái, quy ước cổng |
| Chọn RNN hai chiều | 10 | Bốn tình huống trực tuyến/ngoại tuyến | Lựa chọn có lý do và kích thước đầu ra |

## Điều hướng

- Đi xuống trong từng cụm khái niệm.
- Đi phải tại L08-01, 06, 17, 21, 29, 31, 33 và 39.
- L08-39 là điểm dừng tuyến lõi. Đi phải sang L08-X01 rồi đi xuống đến L08-X04 cho tuyến mở rộng.
