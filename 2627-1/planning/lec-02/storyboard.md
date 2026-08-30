# Storyboard Bài 02

## Bản đồ hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính toán | Triển khai/ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|
| Đồ thị và quy tắc chuỗi | L02-02–05 | L02-04–06 | L02-05–06, L02-09–13 | L02-07–08, L02-14 | L02-14 | L02-07, L02-13 |
| Tensor và tầng afin | L02-15–16 | L02-17–20 | L02-18, L02-20 | L02-16–23 | L02-21–23 | L02-24 |
| Softmax và entropy chéo | L02-25–27 | L02-28–29 | L02-25–29 | L02-30–32 | L02-33–36 | L02-32, L02-38 |
| Trạng thái huấn luyện | L02-33–36 | L02-37 | Ví dụ MLP L02-25–36 | L02-37 | L02-37 | L02-38 |
| Mở rộng | L02-X01, L02-X04 | L02-X02, L02-X04 | L02-X05 | L02-X01, L02-X05 | L02-X04–X05 | L02-X05 |

Đầu vào chung: đạo hàm một biến, phép nhân ma trận, MLP, ReLU (tiên quyết từ Bài 01), softmax và logarit ở mức nhập môn. Sản phẩm cuối: giải thích và kiểm tra một bước huấn luyện từ $X,Y$ đến $J$, gradient và cập nhật. Ví dụ vô hướng chính giữ $x=3,y=-4,z=2,w=-1$ từ L02-05 đến L02-12. L02-13 dùng đồ thị và dữ kiện độc lập. Ví dụ MLP giữ nguyên $X,Y,W_1,b_1,W_2,b_2$ từ L02-25 đến L02-36.

## Tuyến lõi, 100 phút

| Trang | Phút | Tiên quyết | Sản phẩm học tập | Tensor/dữ kiện truyền tiếp | Bước chu trình và câu nối |
|---|---:|---|---|---|---|
| L02-00 | 1 | Đề cương | Khóa chủ đề | MLP, gradient | Vấn đề; chuyển sang mục tiêu |
| L02-01 | 2 | Đạo hàm, ma trận, MLP | Biết đầu vào và đầu ra của bài | Quy ước lô theo hàng | Vấn đề + kiểm tra tiên quyết |
| L02-02 | 2 | MLP | Đọc chuỗi $X\to H\to Z\to J$ | $X,H,Z,J$ | Vấn đề; cần gradient tham số |
| L02-03 | 2 | Gradient | Phân biệt xuôi, ngược, cập nhật | $J,\theta$ | Ứng dụng; ghi phụ thuộc |
| L02-04 | 2 | Hàm hợp | Đọc DAG và thứ tự tô-pô | Nút, cạnh | Trực giác; tách biểu thức |
| L02-05 | 2 | Cộng, nhân, max | Tách $f$ thành $q,r,s$ | $x,y,z,w,q,r,s,f$ | Trực giác; chạy xuôi |
| L02-06 | 3 | L02-05 | Tính $f=-20$, biết giá trị phải lưu | $x,y,z,w,q,r,s$ | Ví dụ; chuẩn bị đạo hàm cục bộ |
| L02-07 | 2 | Đạo hàm hàm hợp | Tính tích đạo hàm trên một đường | $dy/dx,dz/dy$ | Hình thức + kiểm tra; viết theo nút |
| L02-08 | 2 | L02-07 | Dùng đạo hàm thượng nguồn × đạo hàm cục bộ và cộng-gán | $\bar v,\partial v/\partial u$ | Hình thức; quay lại ví dụ |
| L02-09 | 2 | L02-06,08 | Kéo gradient qua cộng | $\bar s,\bar q,\bar r$ | Tính toán; sang cổng nhân |
| L02-10 | 2 | L02-09 | Kéo gradient qua nhân | $x,y,\bar q$ | Tính toán; sang max |
| L02-11 | 2 | L02-09 | Kéo gradient qua max, nêu điểm gãy | $z,w,\bar r$ | Tính toán; sang phân nhánh |
| L02-12 | 2 | L02-08 | Cộng đóng góp từ nhiều đường | Hai nhánh gradient | Hình thức; kiểm bằng đồ thị mới |
| L02-13 | 3 | L02-09–12 | Tự tính gradient của ví dụ độc lập | $x=4,y=-6,z=-1,w=2.5$ | Ví dụ + kiểm tra; khái quát |
| L02-14 | 3 | L02-04–13 | Mô tả thuật toán lan truyền ngược và VJP cục bộ | DAG, giá trị lưu | Triển khai; chuyển sang tensor |
| L02-15 | 2 | Gradient vô hướng | Khóa kích thước gradient tensor | $U,G_U$ | Vấn đề + quy ước; sang Jacobian |
| L02-16 | 3 | Đạo hàm vector | Đọc VJP theo covector hàng | $G_z^{row},J_f,G_x^{row}$ | Hình thức; khai thác cấu trúc |
| L02-17 | 2 | L02-16 | Rút Jacobian chéo thành Hadamard | $x,z,G_z$ | Trực giác + hình thức; sang ReLU |
| L02-18 | 2 | ReLU | Dùng mặt nạ tiền kích hoạt | $A,G_H,G_A$ | Ví dụ + triển khai; sang afin |
| L02-19 | 2 | Lô theo hàng | Khóa miền, kích thước, phát rộng | $X,W,b,Z$ | Vấn đề; mở chỉ số |
| L02-20 | 3 | Tổng hữu hạn | Đọc phụ thuộc của $Z_{ic}$ | $X_{ij},W_{jc},b_c$ | Ví dụ + trực giác; lấy đạo hàm |
| L02-21 | 2 | L02-20 | Suy $G_X=G_ZW^\top$ | $G_Z,W$ | Hình thức; đổi biến cần đạo hàm |
| L02-22 | 2 | L02-20 | Suy $G_W=X^\top G_Z$ | $X,G_Z$ | Hình thức; xử lý bias |
| L02-23 | 2 | Phát rộng | Suy $G_b=\sum_iG_{Z,i:}$ | $G_Z$ | Hình thức + triển khai; kiểm kích thước |
| L02-24 | 2 | L02-19–23 | Kiểm ba kích thước gradient | $B,d,k$ | Kiểm tra; dùng cho MLP |
| L02-25 | 3 | MLP, nhãn nhất vị | Khóa dữ liệu, nhãn, tham số | $X,Y,W_1,b_1,W_2,b_2$ | Vấn đề + ví dụ; tính tầng ẩn |
| L02-26 | 3 | Afin, ReLU | Tính $A,H$ và biết cần giữ $X,A$ | $X,A,H$ | Ví dụ + triển khai; sang tầng ra |
| L02-27 | 2 | L02-26 | Tính điểm số, giữ $H,W_2$ | $H,W_2,Z$ | Ví dụ; chuẩn hóa lớp |
| L02-28 | 3 | Mũ và xác suất | Tính softmax theo trục lớp | $Z,P$ | Trực giác + ví dụ; dựng mất mát ổn định |
| L02-29 | 3 | Logarit | Tính log-softmax/LSE trực tiếp từ điểm số | $Z,Y,J$ | Hình thức + triển khai; lấy đạo hàm |
| L02-30 | 3 | Softmax | Suy Jacobian cục bộ softmax | $P,\delta_{rc}$ | Hình thức; ghép entropy chéo |
| L02-31 | 5 | L02-29–30, quy tắc chuỗi | Suy $G_Z=(P-Y)/B$ | $P,Y,B,G_Z$ | Hình thức/tính toán; thế số |
| L02-32 | 3 | L02-31 | Kiểm gradient điểm số và tổng hàng | $G_Z$ | Ví dụ + kiểm tra; qua tầng ra |
| L02-33 | 4 | Tầng afin lượt ngược | Tính $G_{W_2},G_{b_2}$ bằng $H$ đã giữ | $H,G_Z$ | Triển khai; kéo về $H$ |
| L02-34 | 5 | ReLU lượt ngược | Tính $G_H,G_A$ bằng $W_2$ cũ và $A$ | $G_Z,W_2,A$ | Tính toán; sang tầng ẩn |
| L02-35 | 3 | Tầng afin lượt ngược | Tính $G_{W_1},G_{b_1}$ bằng $X$ | $X,G_A$ | Tính toán; đủ gradient |
| L02-36 | 2 | Gradient đầy đủ | Cập nhật đồng thời | $G_\theta,\eta$ | Ứng dụng; sang trạng thái vòng lặp |
| L02-37 | 3 | Vòng lặp huấn luyện | Tách chế độ mô hình, ghi gradient, đặt gradient về 0 | Trạng thái mô hình và gradient | Triển khai; kiểm lỗi |
| L02-38 | 2 | Toàn bộ tuyến lõi | Sửa bốn lỗi phổ biến | Trục lớp, lô, đặt gradient về 0, tham số cũ | Kiểm tra; chuyển sang trang kết |
| L02-39 | 2 | Toàn bộ tuyến lõi | Thu hồi $X\to H\to Z\to J\to$ gradient $\to$ cập nhật và ba tiêu chí kiểm | $X,H,Z,J,G_\theta,\eta$ | Kiểm tra; kết thúc tuyến lõi, nối sang Bài 03 |

Tổng lõi: 100 phút. L02-31 giữ 5 phút vì có ba bước công thức; L02-33 giữ 4 phút; L02-38 giảm từ 3 xuống 2 phút để bù cho L02-39.

Thao tác tuyến lõi: từ L02-38 nhấn mũi tên phải hai lần để đi qua mạch mở rộng và đến L02-39. Tuyến đầy đủ vào L02-X01 rồi đi dọc qua L02-X02, L02-X04, L02-X05; sau L02-X05 nhấn mũi tên phải để đến L02-39. Mã trang X03 được giữ trống (không dùng) để không đổi mã các trang còn lại; đây là lý do giữ khoảng mã ổn định.

Các bước không áp dụng: L02-00–01 chỉ định hướng nên không cần ví dụ số; L02-15–17 là cầu nối hình thức nên triển khai được gộp vào L02-18–24; L02-37 không tạo công thức mới nên hình thức được gộp với ví dụ vòng lặp.

## Tuyến mở rộng/có thể cắt, 20 phút

Có thể bỏ toàn bộ phần này: từ L02-38 đi thẳng sang L02-39. Điều hướng ngang đến phần cuối; không đi riêng L02-X02 khi chưa giới thiệu sigmoid ở L02-X01.

| Trang | Phút | Tiên quyết | Sản phẩm | Dữ kiện truyền | Bước chu trình |
|---|---:|---|---|---|---|
| L02-X01 | 5 | Cổng và quy tắc chuỗi | Gộp chuỗi cổng thành sigmoid | $a,\sigma(a),G_h$ | Hình thức + triển khai |
| L02-X02 | 5 | L02-X01 | Nhận biết đạo hàm cục bộ nhỏ; khóa ranh giới Bài 03 | $\sigma'(a)$ | Trực giác + kiểm tra phạm vi |
| L02-X04 | 5 | Lan truyền ngược | Nêu đánh đổi lưu và tính lại | Giá trị kích hoạt cần giữ | Triển khai; không đi vào lưu điểm kiểm tra |
| L02-X05 | 5 | Sai phân trung tâm | Kiểm tra đạo hàm bằng $e_j$, sai số tương đối, tránh điểm gãy | $\theta,\varepsilon,e_j,g_j$ | Ví dụ + kiểm tra |

## Bảng sáu mạch ngoài 1-1

| Mạch ngoài | Trang | Vai trò |
|---|---|---|
| Mở đầu | L02-00–05 | Khóa phạm vi, mục tiêu, tiên quyết, đồ thị và tách biểu thức |
| Cổng vô hướng | L02-06–14 | Ví dụ xuôi, quy tắc chuỗi, cổng cộng/nhân/max, thuật toán lan truyền ngược |
| Tensor/afin | L02-15–24 | Kích thước gradient, VJP, ReLU, ba công thức tầng afin |
| MLP xuyên suốt | L02-25–38 | Ví dụ 2–2–3 từ $X,Y$ đến cập nhật và trạng thái huấn luyện |
| Mở rộng có thể cắt | L02-X01, X02, X04, X05 | Sigmoid, bộ nhớ, kiểm tra đạo hàm |
| Kết luận | L02-39 | Thu hồi một bước huấn luyện và ba tiêu chí kiểm |

## Bài tập 50 phút, tách khỏi deck

| Hoạt động | Phút | Sản phẩm |
|---|---:|---|
| Dựng đồ thị tính toán | 10 | DAG với giá trị trung gian và thứ tự xuôi/ngược |
| Lan truyền ngược bằng tay | 15 | Gradient mọi lá từ các cổng cục bộ |
| ReLU và tầng afin | 15 | Kích thước $G_X,G_W,G_b$ và mặt nạ đúng |
| Tìm và sửa lỗi | 10 | Bản sửa bốn lỗi về trục, hệ số và thứ tự cập nhật |

## Rà lân cận sau thay đổi cấu trúc

- L02-04–10: ví dụ lan truyền xuôi nay đứng trước quy tắc chuỗi; chuyển ý từ tách nút → thế số → đạo hàm cục bộ → lan truyền ngược không còn đảo trình tự.
- L02-18–26: phép suy afin theo chỉ số ở lõi; hai trang trước chuẩn bị ReLU và quy ước lô theo hàng, hai trang sau dùng trực tiếp công thức.
- L02-27–35: log-softmax, Jacobian softmax và quy tắc chuỗi đứng trước $G_Z$; phần số được tách để mỗi trang giữ một phép tính trung tâm.
- L02-35–38: đủ gradient → cập nhật → trạng thái vòng lặp → kiểm tra; không trộn chế độ mô hình với ghi gradient.
- L02-38 → L02-39: tuyến lõi bỏ qua mở rộng; L02-39 thu hồi chuỗi và nối sang Bài 03 mà không mở bộ tối ưu.
