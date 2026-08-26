# Bài 05 — Các kiến trúc mạng tích chập hiện đại

## Phạm vi và sản phẩm học tập

- Chuẩn đầu ra: LLO9–LLO10 trong đề cương, Buổi 5.
- Tuyến trình chiếu: 100 phút lõi và 20 phút mở rộng có thể cắt nguyên cụm.
- Bài tập: 50 phút riêng, không cộng vào thời lượng trình chiếu.
- Người học mô tả được LeNet, AlexNet, VGG, GoogLeNet/Inception và ResNet bằng kích thước tensor, số tham số, MAC và đường truyền đạo hàm.
- Người học phân tích được giới hạn mà mỗi thay đổi kiến trúc xử lý, cùng điều kiện và giới hạn của kết luận.

## Nguồn đã chọn

1. Đề cương học phần, III.2 → Buổi 5: tên bài, LLO9–10 và phạm vi.
2. `source.md`, Buổi 05: thứ tự kiến trúc, dải trang và cảnh báo.
3. Nguồn chính `lec09_cnn_architectures.pdf`, PDF 3–9, 11–23, 26–34.
4. Nguồn phụ `lec09_cnn_architectures.pdf`, PDF 44–46; `lec10_training.pdf`, PDF 25–32.
5. Giáo trình `hocsau_draft.pdf`, PDF 132–146 và 149–163, chỉ các mục LeNet, AlexNet, VGG, GoogLeNet, chuẩn hóa theo lô và ResNet.
6. Không dùng `lec09_cnn_architectures.pdf` PDF 36–43, NiN, DenseNet, ResNeXt, ảnh trang trí hoặc bảng định lượng thiếu giao thức.

## Hành trình khái niệm

LeNet làm mốc khối và kích thước → AlexNet tăng quy mô nhưng dồn tham số vào tầng đầy đủ → VGG chuẩn hóa thiết kế thành khối nhỏ lặp lại → Inception phân bổ tính toán qua nhiều nhánh và GoogLeNet xếp chín khối thành toàn mạng → chuẩn hóa theo lô tách thống kê huấn luyện/suy luận → ResNet thêm đường đồng nhất và bốn giai đoạn → học chuyển giao tái dùng tham số.

Mỗi cụm đi theo cùng một trục: giới hạn → thay đổi kiến trúc → kích thước tensor → tham số/MAC/đạo hàm → giới hạn mới.

## Ánh xạ nội dung

| Cụm | Nguồn | Quyết định |
|---|---|---|
| LeNet | GT PDF 132–135 | Dùng biến thể GT trên MNIST 28×28; hiện cấu trúc 5×5–sigmoid–gộp trung bình và cảnh báo bản gốc 32×32 |
| AlexNet | `lec09`, PDF 5–9; GT PDF 136–143 | Khóa biến thể sửa đổi: đầu vào 227, tích chập 1 có 64 kênh; hiện đặc tả toán tử và tự tính kích thước, tham số, MAC |
| VGG | `lec09`, PDF 11–14; GT PDF 143–146 | Khóa VGG-16; hiện số tầng 2–2–3–3–3 và dấu vết đến đầu FC6–FC8 |
| GoogLeNet/Inception | `lec09`, PDF 15–23; GT PDF 149–152 | Sửa phần gốc còn ba tích chập; hiện điều kiện giữ $H,W$, phép ghép, chi phí khối và toàn mạng 2–5–2 Inception |
| Chuẩn hóa theo lô | `lec10`, PDF 25–32; GT PDF 153–158 | Giảm theo N,H,W cho từng kênh; phương sai lượt xuôi dùng mẫu số $NHW$; thống kê cố định được ước lượng khi học; không khóa cách cập nhật cụ thể |
| ResNet | `lec09`, PDF 26–34; GT PDF 158–163 | Tách suy giảm khỏi quá khớp; kiểm tra cộng/chiếu, ba ma trận đạo hàm, khối cơ bản/cổ chai và dấu vết ResNet-18 |
| Học chuyển giao | `lec09`, PDF 44–46 | Dùng tình huống cụ thể; tách tham số có gradient khỏi chế độ mô-đun và chính sách BN |

## Quy ước tensor và phép đếm

| Ký hiệu | Nghĩa |
|---|---|
| $X\in\mathbb{R}^{N\times C\times H\times W}$ | Tensor theo NCHW: lô, kênh, cao, rộng |
| $W\in\mathbb{R}^{C_{out}\times C_{in}\times K_h\times K_w}$ | Trọng số tích chập theo OIHW |
| $P$ | Số tham số học được; tính độ lệch khi kiến trúc có độ lệch |
| MAC | Một phép nhân rồi cộng tích lũy; nếu quy đổi theo quy ước đã nêu thì $1\ \mathrm{MAC}\approx2\ \mathrm{FLOP}$ |
| $F(x;W)$ | Nhánh thặng dư; $s=x+F(x;W)$ khi hai nhánh cùng kích thước |
| $P(x)$ | Phép chiếu trên nhánh tắt khi đổi kênh hoặc độ phân giải |
| $J_F,J_P\in\mathbb R^{d_{out}\times d_{in}}$ | Ma trận đạo hàm của $F,P$ theo $x$ sau khi vectơ hóa; có thể là ma trận chữ nhật khi kích thước đổi |
| $\bar x=J_s^\top\bar s$ | Tích Jacobian chuyển vị–vectơ trong lan truyền ngược với quy ước gradient cột |
| $\gamma,\beta\in\mathbb{R}^{C}$ | Tham số BN, phát rộng thành $1\times C\times1\times1$ |

Không gọi MAC là FLOP. Không quy đổi nếu chưa nêu quy ước đếm.

## Ranh giới

- Không dạy NiN, DenseNet, ResNeXt hoặc kiến trúc ngoài dải đã khóa.
- Không dùng bảng lỗi hoặc xếp hạng để tuyên bố hơn kém khi giao thức không đầy đủ.
- Không tạo mã nguồn, notebook hoặc trình diễn huấn luyện.
- Không đưa chỉ dẫn người soạn, thời lượng, tuyến cắt hoặc đáp án chi tiết lên mặt trang hay ghi chú diễn giả.
- Hậu kích hoạt và tiền kích hoạt chỉ xuất hiện ở L05-X04, sau khi hoàn tất cụm ResNet.
- Ví dụ mô tả ảnh ở L05-X05 chỉ là giao diện vectơ trừu tượng; cơ chế chuỗi thuộc Bài 07.
