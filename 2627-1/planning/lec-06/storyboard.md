# Storyboard Bài 06

## Bản đồ hành trình

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính toán | Triển khai/ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Dữ kiện truyền | Câu nối |
|---|---|---|---|---|---|---|---|---|---|
| Biểu diễn | L06-02 | L06-03 | L06-02–03 (gộp: ví dụ chữ số trực tiếp tạo trực giác) | L06-04 | L06-04 | L06-05 | Điểm ảnh và dữ liệu chưa nhãn → phân biệt mục tiêu thay thế với tác vụ đích | $x\to z$, chưa dùng nhãn lớp | “Muốn đánh giá mã, trước hết phải mô tả máy tạo mã.” |
| Kiến trúc | L06-06 | L06-06 | L06-07–08 | L06-09 | L06-09 | L06-10 | Ảnh MNIST → hợp đồng tensor và bốn lớp tuyến tính | $X_{\mathrm{img}}\to X\to H_e\to Z\to H_d\to\hat X$ | “Kích thước đúng cho phép so từng phần tử tái tạo.” |
| Mất mát | L06-11 | L06-11 | L06-12 | L06-13 | L06-14 | L06-15 | Một mẫu $D=4$ → SSE/MSE → lô MNIST $D=784$ | 0.18, 0.045, $N,D$ | “Giảm lỗi tái tạo chưa ngăn được đường tắt sao chép.” |
| Nút thắt | L06-16 | L06-17 | L06-16–17 (gộp: hai sơ đồ đối chứng) | L06-18–19 | L06-19 | L06-20 | Nghiệm đồng nhất → vai trò và giới hạn của $d$ | $d<784$, lỗi kiểm định, tác vụ đích | “Ta có thể ràng buộc kiến trúc, mã hoặc dữ liệu.” |
| Ba biến thể | L06-21–22 | L06-22 | L06-23–24 | L06-25–26 | L06-25–26 | L06-27 | Nút thắt → mã thấp chiều, phạt mềm/top-$k$, khử nhiễu | $d,k,\lambda,X,\widetilde X$; top-$k$ theo mẫu; đầu vào nhiễu–đích sạch | “Giá trị của mã được kiểm tra bằng tác vụ có nhãn.” |
| Tái sử dụng | L06-28 | L06-28 | L06-29–30 | L06-31 | L06-32 | L06-33 | Bộ mã hóa đã tiền huấn luyện → chính sách đóng băng/tinh chỉnh | $\theta^\star,\psi$, cập nhật tham số, chế độ mô-đun | “Mã hữu ích vẫn chưa biến bộ giải mã thành mô hình sinh.” |
| Lấy mẫu | L06-34 | L06-35 | L06-34–35 (gộp: vùng mã là ví dụ hình học) | L06-36 | L06-37 | L06-38 | Mã do bộ mã hóa tạo → giới hạn của mã tùy ý | $z^{(n)}=f_\theta(x^{(n)})$ so với $z$ tùy ý | Kết thúc tuyến lõi; phần mở rộng đào sâu hình học và đánh giá. |
| Mở rộng | L06-X01 | L06-X01 | L06-X01, X03–X04 | L06-X02 | L06-X05 | L06-X01 | Chuỗi lõi → chi phí thao tác, PCA, vùng hoạt động và phi tuyến | $210/6=35=\mathrm{XXXV}$; $d,k,\Omega$; $K$ | X01 kiểm tra mở rộng; X05 ứng dụng và tổng kết giao thức đánh giá. |

Không có bước “không áp dụng”: mỗi cụm lõi thực hiện đủ sáu bước. Một số bước được gộp vì cùng một sơ đồ vừa cung cấp dữ kiện vừa tạo trực giác; việc tách riêng sẽ lặp nội dung.

## Thời lượng và điều hướng

| Trang | Phút | Tuyến | Vai trò trung tâm | Điều hướng |
|---|---:|---|---|---|
| L06-00 | 2 | Lõi | Mở vấn đề dữ liệu ít nhãn | Xuống |
| L06-01 | 2 | Lõi | LLO, tiên quyết, sản phẩm học tập | Phải |
| L06-02 | 2 | Lõi | Biểu diễn đổi độ khó phép toán | Xuống |
| L06-03 | 3 | Lõi | Điểm ảnh → mã → tác vụ | Xuống |
| L06-04 | 2 | Lõi | Mục tiêu tự giám sát | Xuống |
| L06-05 | 3 | Lõi | Kiểm tra: tái tạo khác phân loại | Phải; chờ 45 giây |
| L06-06 | 2 | Lõi | Ba phần của autoencoder | Xuống |
| L06-07 | 3 | Lõi | Chuỗi kích thước MNIST | Xuống |
| L06-08 | 2 | Lõi | Kiến trúc MLP minh họa | Xuống |
| L06-09 | 3 | Lõi | Ma trận, độ lệch, kích hoạt | Xuống |
| L06-10 | 2 | Lõi | Kiểm tra kích thước | Phải; chờ 60 giây |
| L06-11 | 2 | Lõi | Phân biệt SSE và MSE | Xuống |
| L06-12 | 3 | Lõi | Ví dụ 0.18 và 0.045 | Xuống |
| L06-13 | 3 | Lõi | MSE lô theo Frobenius | Xuống |
| L06-14 | 3 | Lõi | Bước huấn luyện và kiểm định | Xuống |
| L06-15 | 2 | Lõi | Kiểm tra phép lấy trung bình | Phải; chờ 45 giây |
| L06-16 | 2 | Lõi | Nghiệm đồng nhất | Xuống |
| L06-17 | 3 | Lõi | Autoencoder có mã thấp chiều | Xuống |
| L06-18 | 2 | Lõi | Năng lực và ghi nhớ | Xuống |
| L06-19 | 2 | Lõi | Chọn $d$ bằng kiểm định | Xuống |
| L06-20 | 3 | Lõi | Kiểm tra giới hạn nút thắt | Phải; chờ 45 giây |
| L06-21 | 2 | Lõi | Ba điểm can thiệp | Xuống |
| L06-22 | 3 | Lõi | Phân biệt phạt mềm và top-$k$ cứng | Xuống |
| L06-23 | 2 | Lõi | Ví dụ top-$k$ | Xuống |
| L06-24 | 3 | Lõi | Luồng khử nhiễu | Xuống |
| L06-25 | 3 | Lõi | Kỳ vọng khử nhiễu và ước lượng lô | Xuống |
| L06-26 | 2 | Lõi | So sánh và hình thức ba biến thể | Xuống |
| L06-27 | 2 | Lõi | Kiểm tra top-$k$ và đích sạch | Phải; chờ 60 giây |
| L06-28 | 3 | Lõi | Bỏ giải mã, giữ mã hóa | Xuống |
| L06-29 | 3 | Lõi | Đóng băng | Xuống |
| L06-30 | 3 | Lõi | Tinh chỉnh | Xuống |
| L06-31 | 3 | Lõi | Gradient và chế độ | Xuống |
| L06-32 | 2 | Lõi | Giao thức kiểm định | Xuống |
| L06-33 | 3 | Lõi | Kiểm tra trạng thái mô hình | Phải; chờ 60 giây |
| L06-34 | 3 | Lõi | Mã thật và mã tùy ý | Xuống |
| L06-35 | 3 | Lõi | Khoảng trống không gian mã | Xuống |
| L06-36 | 3 | Lõi | Không có phân phối sinh mặc định | Xuống |
| L06-37 | 3 | Lõi | Bảng kiểm sử dụng mã | Xuống |
| L06-38 | 3 | Lõi | Kiểm tra tổng hợp | Phải để vào mở rộng; chờ 60 giây |
| L06-X01 | 4 | Mở rộng | Tính $210/6$ trong hai biểu diễn | Xuống; chờ 45 giây |
| L06-X02 | 4 | Mở rộng | Quan hệ tuyến tính với PCA | Xuống |
| L06-X03 | 4 | Mở rộng | Phân biệt $d$, $k$, $\Omega$ và vùng hoạt động | Xuống |
| L06-X04 | 4 | Mở rộng | Đa tạp phi tuyến | Xuống |
| L06-X05 | 4 | Mở rộng | Ứng dụng và tổng kết giao thức đánh giá | Kết thúc |

Tổng tuyến lõi: **100 phút**. Tổng tuyến mở rộng: **20 phút**. Bài tập: **50 phút**, tách khỏi 120 phút trình chiếu.

## Chu trình bài tập 50 phút

| Bước | Thời lượng | Đầu vào | Sản phẩm |
|---|---:|---|---|
| Hoàn thiện sơ đồ và kích thước | 10 | MNIST, $N=16$, $d=32$, bốn lớp tuyến tính | Sơ đồ bộ mã hóa–mã tiềm ẩn–bộ giải mã và toàn bộ kích thước; số tham số là phần tùy chọn |
| Tính SSE/MSE | 15 | Hai mẫu bốn chiều | MSE lô có mẫu số đúng |
| Phân tích đồng nhất và nút thắt | 10 | Lỗi tái tạo bằng 0, $d<784$ | Điều được khuyến khích và điều chưa bảo đảm |
| Chọn biến thể | 10 | Ba tình huống thiết kế | Mã thấp chiều, thưa hoặc khử nhiễu |
| Thiết kế tác vụ đích | 5 | Bộ mã hóa đóng băng | Tham số cập nhật và chế độ từng mô-đun |

## Navigation

- Các trang trong một cụm là ngăn xếp dọc; dùng mũi tên xuống.
- Chỉ dùng mũi tên phải ở trang cuối cụm: L06-01, 05, 10, 15, 20, 27, 33, 38.
- L06-38 là điểm dừng tuyến lõi. Nhấn phải để vào L06-X01, rồi nhấn xuống đến L06-X05.
