# Storyboard Bài 07

## Chu trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính toán | Triển khai/ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Dữ kiện truyền | Câu nối |
|---|---|---|---|---|---|---|---|---|---|
| Ngữ cảnh chuỗi | L07-02–03 | L07-04 | L07-04 | L07-05 | L07-05 | L07-06 | Lô đang xét có mẫu cùng $T$ → tensor lô | $N,T,D_x,X_t$, mọi bước hợp lệ | “Tensor đã khóa; ta cần phép cập nhật trạng thái.” |
| Ô RNN | L07-07 | L07-07–09 | L07-07–08 | L07-09–12 | L07-13 | L07-13 | Ví dụ vô hướng → quan hệ truy hồi có kích thước đúng → tham số dùng chung | $a_1,h_1$ rồi $W_x,W_h,W_y,H_0$ | “Một quan hệ truy hồi có thể phục vụ nhiều dạng ánh xạ.” |
| Dạng ánh xạ | L07-14 | L07-14 | L07-15–16 | L07-15–16 | L07-14–16 | L07-17 | Đồ thị vào/ra → vị trí đặt mất mát và kiểu đích | $O_T$ hoặc $O_{1:T}$; chỉ số lớp so với đích vectơ | “Dùng bộ số đã mở để tính toàn bộ lan truyền xuôi.” |
| Lan truyền xuôi | L07-07–08 | L07-07–08 | L07-07–08 | L07-18 | L07-19–20 | L07-21 | Ví dụ đã mở → thuật toán → triển khai bằng số → kiểm tra đường ảnh hưởng | $0.4621,0.3537,-0.2137,-0.2564,0.2154$ | “Đường ảnh hưởng xuôi trở thành đường gradient ngược.” |
| BPTT | L07-22 | L07-22 | L07-23–24, L07-27–28 | L07-25–26, L07-28 | L07-25–28 | L07-29 | Đồ thị vô hướng → vòng $T\to1$ → gradient trạng thái và tham số | $\delta_t=G_t$, $\bar O_t,\bar H_t,G_t$; ba gradient tham số | “Chuỗi dài biến các đường này thành tích Jacobian.” |
| Ổn định gradient | L07-30 | L07-30 | L07-31–32 | L07-30–32 | L07-33 | L07-34 | BPTT ba bước → hành vi khi số bước tăng | $J_t$, $0.3362$, $0.8^{20}$ | “Giới hạn độ dài lan truyền ngược đổi chi phí và tín dụng.” |
| BPTT cắt ngắn | L07-35 | L07-36 | L07-36 | L07-37 | L07-35–37 | L07-38 | Chuỗi dài → hai chính sách BPTT | $T,K$, trạng thái xuôi, ranh giới gradient | “Khó khăn đường trạng thái dẫn sang kiến trúc có cổng.” |
| Cầu nối | L07-39 | L07-39 | không áp dụng: chỉ đặt câu hỏi thiết kế cho bài sau | không áp dụng: không dạy công thức cổng | L07-39 | không áp dụng: kiểm tra đã hoàn tất ở L07-38 | Giới hạn RNN cơ bản → câu hỏi cho Bài 08 | tích Jacobian dài | Kết thúc tuyến lõi. |
| Ứng dụng và đối chiếu lõi (rút gọn) | L07-X01 | L07-X02 | L07-X01–X02 | L07-X01 | L07-X02 | không áp dụng: chỉ đối chiếu hai ứng dụng với cơ chế lõi, không thêm thuật toán | RNN cơ bản → phân rã xác suất; dạng căn chỉnh → không căn chỉnh | Hai nhánh dữ kiện độc lập: xác suất chuỗi và quan hệ vị trí đầu ra | “Từ ứng dụng chuyển sang hai lựa chọn thiết kế kiến trúc.” |
| Thiết kế kiến trúc (rút gọn) | L07-X03 | L07-X03–X04 | L07-X04 | L07-X03 | L07-X03–X04 | L07-X04 | Trục thời gian → thêm trục tầng và hai hướng | $H_t^{(0)}$, kích thước từng tầng, điều kiện có tương lai | X04 kiểm tra đồng thời trục tầng và tính nhân quả; kết thúc bài. |

Các bước gộp dùng cùng dữ kiện cho trực giác và ví dụ; tách riêng sẽ lặp hình hoặc ký hiệu. Cụm cầu nối không lặp kiểm tra vì chỉ đặt câu hỏi thiết kế cho bài sau. X01–X02 và X03–X04 là hai nhánh rút gọn độc lập: nhánh đầu chỉ đối chiếu ứng dụng với lõi, nhánh sau thêm lựa chọn kiến trúc và kết thúc bằng kiểm tra X04.

## Thời lượng và điều hướng

| Trang | Phút | Tuyến | Vai trò trung tâm | Điều hướng |
|---|---:|---|---|---|
| L07-00 | 2 | Lõi | Mở vấn đề chuỗi | Xuống |
| L07-01 | 2 | Lõi | LLO và tiên quyết | Phải |
| L07-02 | 2 | Lõi | Khóa giả thiết cùng $T$ cho lô đang xét | Xuống |
| L07-03 | 2 | Lõi | Cửa sổ so với trạng thái | Xuống |
| L07-04 | 2 | Lõi | Trực giác trạng thái | Xuống |
| L07-05 | 2 | Lõi | Hợp đồng tensor cho các mẫu đã chọn cùng $T$ | Xuống |
| L07-06 | 3 | Lõi | Kiểm tra trục và kích thước | Phải; chờ 45 giây |
| L07-07 | 2 | Lõi | Mở ví dụ vô hướng | Xuống |
| L07-08 | 2 | Lõi | Hoạt động tính trong ví dụ trước khi khái quát | Xuống |
| L07-09 | 2 | Lõi | Hai đầu vào của ô RNN | Xuống |
| L07-10 | 2 | Lõi | Công thức ma trận theo lô | Xuống |
| L07-11 | 3 | Lõi | Bảng kích thước | Xuống |
| L07-12 | 3 | Lõi | Trạng thái đầu | Xuống |
| L07-13 | 3 | Lõi | Trải mạng và kiểm tra chia sẻ tham số | Phải; chờ 45 giây |
| L07-14 | 3 | Lõi | Bốn dạng ánh xạ | Xuống |
| L07-15 | 2 | Lõi | Mất mát nhiều–sang–một | Xuống |
| L07-16 | 3 | Lõi | Mất mát căn chỉnh và hai kiểu đích | Xuống |
| L07-17 | 2 | Lõi | Kiểm tra dạng ánh xạ | Phải; chờ 45 giây |
| L07-18 | 2 | Lõi | Hình thức: thuật toán lan truyền xuôi | Xuống |
| L07-19 | 3 | Lõi | Sơ đồ ví dụ ba bước | Xuống |
| L07-20 | 3 | Lõi | Triển khai thuật toán bằng bộ số | Xuống |
| L07-21 | 2 | Lõi | Kiểm tra đường phụ thuộc xuôi | Phải; chờ 45 giây |
| L07-22 | 2 | Lõi | BPTT và tham số dùng chung | Xuống |
| L07-23 | 2 | Lõi | Đồ thị gradient vô hướng | Xuống |
| L07-24 | 3 | Lõi | Ba delta và chiều đi ngược | Xuống |
| L07-25 | 3 | Lõi | Vòng BPTT $T\to1$ và $\bar H_t$ | Xuống |
| L07-26 | 3 | Lõi | Gradient trọng số và độ lệch | Xuống |
| L07-27 | 3 | Lõi | Cộng gradient tham số của ví dụ | Xuống |
| L07-28 | 3 | Lõi | Trực tiếp so với toàn phần | Xuống |
| L07-29 | 2 | Lõi | Kiểm tra chia sẻ tham số | Phải; chờ 45 giây |
| L07-30 | 3 | Lõi | Tích Jacobian | Xuống |
| L07-31 | 3 | Lõi | Tích ba bước bằng 0.3362 | Xuống |
| L07-32 | 3 | Lõi | Triệt tiêu/bùng nổ | Xuống |
| L07-33 | 3 | Lõi | Phụ thuộc dài hạn | Xuống |
| L07-34 | 2 | Lõi | Kiểm tra $0.8^{20}$ | Phải; chờ 45 giây |
| L07-35 | 3 | Lõi | Chi phí BPTT toàn phần | Xuống |
| L07-36 | 3 | Lõi | BPTT cắt ngắn | Xuống |
| L07-37 | 3 | Lõi | So sánh $T$ và $K$ | Xuống |
| L07-38 | 2 | Lõi | Kiểm tra trạng thái/gradient | Xuống; chờ 60 giây |
| L07-39 | 2 | Lõi | Cầu nối kiến trúc có cổng | Phải để vào mở rộng |
| L07-X01 | 5 | Mở rộng | Phân rã xác suất chuỗi | Xuống |
| L07-X02 | 5 | Mở rộng | Căn chỉnh và không căn chỉnh | Xuống |
| L07-X03 | 5 | Mở rộng | RNN nhiều tầng và kích thước từng tầng | Xuống |
| L07-X04 | 5 | Mở rộng | Kiểm tra hai chiều, trục tầng và nhân quả | Kết thúc; chờ 45 giây |

Tổng tuyến lõi: **100 phút**. Tổng tuyến mở rộng: **20 phút**. Bài tập tách riêng: **50 phút**.

## Bài tập 50 phút

| Hoạt động | Phút | Đầu vào | Sản phẩm |
|---|---:|---|---|
| Trải mạng và kích thước | 15 | $N,T,D_x,D_h,D_y$ | Đồ thị bốn bước và bảng tensor |
| BPTT bằng tay | 20 | Ví dụ vô hướng ba bước | $h_t,o_3,L,\delta_t$ và ba gradient |
| Phân tích gradient | 10 | $0.8^{20}$ và $1.2^{20}$ | So sánh thang và giới hạn của ví dụ vô hướng |
| Phân loại dạng ánh xạ | 5 | Bốn tình huống chuỗi | Một–nhiều/nhiều–một/nhiều–nhiều |

## Navigation

- Dùng mũi tên xuống trong từng cụm.
- Dùng mũi tên phải ở L07-01, 06, 13, 17, 21, 29, 34 và 39.
- L07-39 là điểm dừng tuyến lõi. Nhấn phải sang L07-X01 rồi đi xuống đến L07-X04.
