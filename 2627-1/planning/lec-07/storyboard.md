# Storyboard Bài 07

## Chu trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính toán | Triển khai/ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Dữ kiện truyền | Câu nối |
|---|---|---|---|---|---|---|---|---|---|
| Ngữ cảnh chuỗi | L07-02–03 | L07-04 | L07-04 | L07-05 | L07-05 | L07-06 | Lô đang xét có mẫu cùng $T$ → tensor lô | $N,T,D_x,X_t$, mọi bước hợp lệ | “Tensor đã khóa; ta cần phép cập nhật trạng thái.” |
| Ô RNN | L07-07 | L07-07–09 | L07-07–08 | L07-09–12 | L07-13 | L07-13 | Ví dụ vô hướng → quan hệ truy hồi có kích thước đúng → tham số dùng chung | $a_1,h_1$ rồi $W_x,W_h,W_y,H_0$ | “Một quan hệ truy hồi có thể phục vụ nhiều dạng ánh xạ.” |
| Dạng ánh xạ | L07-14 | L07-14 | L07-15–16 | L07-15–16 | L07-14–16 | L07-17 | Đồ thị vào/ra → vị trí đặt mất mát và kiểu đích | $O_T$ hoặc $O_{1:T}$; chỉ số lớp so với đích liên tục; softmax theo $D_y$ | “Dùng bộ số đã mở để tính toàn bộ lan truyền xuôi.” |
| Lan truyền xuôi | L07-07–08 | L07-07–08 | L07-07–08 | L07-18 | L07-19–20 | L07-21 | Ví dụ đã mở → thuật toán → triển khai bằng số → kiểm tra đường ảnh hưởng | $0.4621,0.3537,-0.2137,-0.2564,0.2154$ | “Đường ảnh hưởng xuôi trở thành đường gradient ngược.” |
| BPTT | L07-22 | L07-22 | L07-23–24, L07-27–28 | L07-25–26, L07-28 | L07-25–28 | L07-29 | Đồ thị vô hướng → vòng $T\to1$ → gradient trạng thái và tham số | $\bar o_3\to\delta_3\to\delta_2\to\delta_1$; $\delta_t=G_t$; ba gradient tham số | “Chuỗi dài biến các đường này thành tích Jacobian.” |
| Ổn định gradient | L07-30 | L07-30 | L07-31–32 | L07-30–32 | L07-33 | L07-34 | BPTT ba bước → hành vi khi số bước tăng | $J_t$, $0.3362$, $0.8^{20}$ | “Giới hạn độ dài lan truyền ngược đổi chi phí và tín dụng.” |
| BPTT cắt ngắn | L07-35 | L07-36 | L07-36 | L07-37 | L07-35–37 | L07-38 | Chuỗi dài → hai chính sách BPTT | $T,K$, trạng thái xuôi, ranh giới gradient | “Khó khăn đường trạng thái dẫn sang kiến trúc có cổng.” |
| Cầu nối | L07-39 | L07-39 | không áp dụng: chỉ đặt câu hỏi thiết kế cho bài sau | không áp dụng: không dạy công thức cổng | L07-39 | không áp dụng: kiểm tra đã hoàn tất ở L07-38 | Giới hạn RNN cơ bản → câu hỏi cho Bài 08 | tích Jacobian dài | Kết thúc toàn deck; slide cuối. |
| Ứng dụng và đối chiếu lõi (rút gọn) | L07-X01 | L07-X02 | L07-X01–X02 | L07-X01 | L07-X01–X02 | không áp dụng: chỉ nối hai ứng dụng với cơ chế lõi, không thêm thuật toán | RNN cơ bản → từng nhân tử $p_\theta(x_t\mid x_{<t})$; dạng căn chỉnh → không căn chỉnh | Xác suất chuỗi, softmax đầu ra và quan hệ vị trí giám sát | “Từ ứng dụng chuyển sang hai lựa chọn thiết kế kiến trúc.” |
| Thiết kế kiến trúc (rút gọn) | L07-X03 | L07-X03–X04 | L07-X04 | L07-X03 | L07-X03–X04 | L07-X04 | Trục thời gian → thêm trục tầng và hai hướng | $H_t^{(0)}$, kích thước từng tầng, điều kiện có tương lai | X04 kiểm tra trục tầng và tính nhân quả; sau đó chuyển tới L07-39 để kết thúc toàn deck. |

Các bước gộp dùng cùng dữ kiện cho trực giác và ví dụ; tách riêng sẽ lặp hình hoặc ký hiệu. Cụm cầu nối không lặp kiểm tra vì chỉ đặt câu hỏi thiết kế cho bài sau. X01–X02 và X03–X04 là hai nhánh rút gọn độc lập: nhánh đầu nối ứng dụng với cơ chế lõi, nhánh sau thêm lựa chọn kiến trúc. Hai trang X01–X02 không cần đủ sáu bước vì chỉ tái dùng phân rã xác suất, softmax và vị trí giám sát đã có; X03–X04 giữ kiểm tra vì thêm trục tầng và điều kiện nhân quả. Mạch 7 có chức năng kép: bốn trang mở rộng có thể cắt và một trang kết luận bắt buộc. Tuyến lõi chỉ đi qua L07-39; tuyến đầy đủ đi qua X01–X04 rồi cùng khép tại L07-39.

Cụm lan truyền xuôi tái dùng bộ số của cụm ô RNN: $x=(1,0,-1)$, $h_0=0$, $w_x=0.5$, $w_h=0.8$, $w_y=1.2$ mở ở L07-07–08 được dùng lại ở L07-19–20 và tiếp tục cho cụm BPTT (L07-23–24, L07-27–28) và cụm ổn định gradient (L07-31).

## Thời lượng và điều hướng

| Trang | Phút | Tuyến | Vai trò trung tâm | Điều hướng |
|---|---:|---|---|---|
| L07-00 | 2 | Lõi | Mở vấn đề chuỗi | Xuống |
| L07-01 | 2 | Lõi | LLO và tiên quyết | Xuống |
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
| L07-17 | 2 | Lõi | Kiểm tra dạng ánh xạ | Xuống; chờ 45 giây |
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
| L07-38 | 2 | Lõi | Kiểm tra trạng thái/gradient | End tới L07-39 (lõi) hoặc Phải vào L07-X01 (đầy đủ); chờ 60 giây |
| L07-X01 | 5 | Mở rộng | Phân rã xác suất chuỗi | Xuống |
| L07-X02 | 5 | Mở rộng | Căn chỉnh và không căn chỉnh | Xuống |
| L07-X03 | 5 | Mở rộng | RNN nhiều tầng và kích thước từng tầng | Xuống |
| L07-X04 | 5 | Mở rộng | Kiểm tra hai chiều, trục tầng và nhân quả | Xuống tới L07-39 |
| L07-39 | 2 | Lõi | Cầu nối kiến trúc có cổng; slide cuối toàn deck | Kết thúc deck |

Tổng tuyến lõi: **100 phút** (15+17+20+21+14+11+2 theo bảy mạch: mở đầu 15, ô RNN 17, dạng ánh xạ và lan truyền xuôi 20, BPTT 21, ổn định gradient 14, BPTT cắt ngắn 11, cầu nối 2). Tổng tuyến mở rộng: **20 phút**. Bài tập tách riêng: **50 phút**.

## Bài tập 50 phút

| Hoạt động | Phút | Đầu vào | Sản phẩm |
|---|---:|---|---|
| Trải mạng và kích thước | 15 | $N,T,D_x,D_h,D_y$ | Đồ thị bốn bước và bảng tensor |
| BPTT bằng tay | 20 | Ví dụ vô hướng ba bước | $h_t,o_3,L,\delta_t$ và ba gradient |
| Phân tích gradient | 10 | $0.8^{20}$ và $1.2^{20}$ | So sánh thang và giới hạn của ví dụ vô hướng |
| Phân loại dạng ánh xạ | 5 | Bốn tình huống chuỗi | Một–nhiều/nhiều–một/nhiều–nhiều |

## Điều hướng

- Quy ước trình bày dùng mũi tên xuống trong từng cụm; RevealJS không chặn phím Phải ở các trang khác.
- Ở cuối năm mạch đầu, dùng mũi tên phải tại L07-06, L07-13, L07-21, L07-29 và L07-34 để sang mạch kế.
- Tuyến lõi: tại L07-38 nhấn End để tới L07-39; binding End tìm đúng chỉ số ngang–dọc của L07-39 rồi gọi `Reveal.slide(h,v)`.
- Tuyến đầy đủ: từ L07-38 nhấn Phải vào L07-X01, đi Down qua X02–X04 rồi Down tới L07-39.
- Phím Phải có binding riêng tại sáu ranh giới: L07-06→07, L07-13→14, L07-21→22, L07-29→30, L07-34→35 và L07-38→X01. Binding lấy chỉ số trang đích rồi gọi `Reveal.slide(h,v)`, vì RevealJS mặc định giữ chỉ số dọc khi sang mạch kế. Ở mọi trang khác, binding gọi `Reveal.right()`.
- Có thể cắt toàn bộ X01–X04; khi cắt, L07-39 vẫn được giữ bằng phím End từ L07-38.
