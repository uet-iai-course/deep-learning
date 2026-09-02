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

## Bảy mạch và ánh xạ mạch

Tổng lõi 100 phút gồm 98 phút cho L05-00–L05-37 và 2 phút kết luận L05-38; mở rộng 20 phút.

| Mạch | Trang | Phút |
|---|---|---:|
| 1. Mở đầu + LeNet | L05-00–03 | 8 |
| 2. AlexNet | L05-04–10 | 20 |
| 3. VGG | L05-11–15 | 11 |
| 4. GoogLeNet/Inception | L05-16–23 | 20 |
| 5. Chuẩn hóa theo lô | L05-24–28 | 14 |
| 6. ResNet + học chuyển giao | L05-29–37 | 25 |
| 7. Mở rộng + kết luận | L05-X01–X05, L05-38 | 20 + 2 |

Mạch 6 gồm hai cụm trong storyboard: ResNet 22 phút và học chuyển giao 3 phút. L05-38 thuộc mạch 7 và giữ 2 phút kết luận riêng, không cộng lặp vào cụm học chuyển giao.

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

## Bản đồ chủ đề lecture note

| Note-topic-id | Nhãn | Vai trò và nguồn | Ánh xạ deck |
|---|---|---|---|
| L05-T01 | cốt lõi | Khóa bốn trục so sánh: kích thước tensor, tham số, MAC và đường đạo hàm; đề cương Buổi 5, `source.md` | L05-00–01, L05-38 |
| L05-T02 | cốt lõi | LeNet làm mốc khối và dấu vết kích thước; GT PDF 132–135 | L05-02–03 |
| L05-T03 | cốt lõi | AlexNet sửa đổi 227×227/64 kênh, tham số và MAC; `lec09` PDF 5–9, GT PDF 136–143 | L05-04–10 |
| L05-T04 | cốt lõi | VGG-16, khối 3×3 lặp và trường tiếp nhận 7×7; `lec09` PDF 11–14, GT PDF 143–146 | L05-11–15 |
| L05-T05 | cốt lõi | Inception và GoogLeNet: phần gốc, bốn nhánh, ghép kênh, 2–5–2 và gộp toàn cục; `lec09` PDF 15–23, GT PDF 149–152 | L05-16–23 |
| L05-T06 | cốt lõi | Chuẩn hóa theo lô trên N,H,W, phát rộng theo kênh và hai chế độ; `lec10` PDF 25–32, GT PDF 153–158 | L05-24–28 |
| L05-T07 | cốt lõi | ResNet: suy giảm, nhánh đồng nhất/chiếu, Jacobian, khối cơ bản/cổ chai và ResNet-18; `lec09` PDF 26–34, GT PDF 158–163 | L05-29–36 |
| L05-T08 | cầu nối | Học chuyển giao tách gradient, chế độ mô-đun và chính sách BN; nguồn phụ đã duyệt `lec09` PDF 44–46 | L05-37 |
| L05-T09 | bổ sung | Kết quả lịch sử phụ thuộc giao thức, bộ phân loại phụ, diễn giải nhiều đường, hậu/tiền kích hoạt và giao diện véc-tơ; chỉ làm rõ giới hạn đã có nguồn | L05-X01–X05 |
| L05-T10 | đọc thêm | NiN, DenseNet, ResNeXt và `lec09` PDF 36–43 nằm ngoài phạm vi; chỉ ghi ranh giới đọc, không soạn mệnh đề hay đưa lên slide | Không đưa lên slide |

Quyết định hợp nhất hai bản đồ độc lập: giữ T01–T08 theo tuyến chính; gộp các chi tiết có thể cắt thành T09; chuyển các họ ngoài phạm vi sang T10 và không triển khai nội dung. Công thức BN từ GT và vấn đề suy giảm trước ResNet là phần bổ sung có nguồn đã duyệt, không đổi ranh giới LLO. Không thêm lịch sử dài, bảng xếp hạng hoặc số benchmark thiếu giao thức.

## Quy ước tensor và phép đếm

| Ký hiệu | Nghĩa |
|---|---|
| $X\in\mathbb{R}^{N\times C\times H\times W}$ | Tensor theo NCHW: lô, kênh, cao, rộng |
| $W\in\mathbb{R}^{C_{out}\times C_{in}\times K_h\times K_w}$ | Trọng số tích chập theo OIHW |
| $P$ | Số tham số học được; tính độ lệch khi kiến trúc có độ lệch |
| MAC | Một phép nhân rồi cộng tích lũy; nếu quy đổi theo quy ước đã nêu thì $1\ \mathrm{MAC}\approx2\ \mathrm{FLOP}$ |
| $F(x;W)$ | Nhánh thặng dư; $s=x+F(x;W)$ khi hai nhánh cùng kích thước |
| $P(x)$ | Phép chiếu trên nhánh tắt khi đổi kênh hoặc độ phân giải |
| $J_F,J_P\in\mathbb R^{d_{out}\times d_{in}}$ | Ma trận đạo hàm của $F,P$ theo $x$ sau khi véc-tơ hóa; có thể là ma trận chữ nhật khi kích thước đổi |
| $\bar x=J_s^\top\bar s$ | Tích Jacobian chuyển vị–véc-tơ trong lan truyền ngược với quy ước gradient cột |
| $\gamma,\beta\in\mathbb{R}^{C}$ | Tham số BN, phát rộng thành $1\times C\times1\times1$ |

Không gọi MAC là FLOP. Không quy đổi nếu chưa nêu quy ước đếm.

## Ranh giới

- Không dạy NiN, DenseNet, ResNeXt hoặc kiến trúc ngoài dải đã khóa.
- Không dùng bảng lỗi hoặc xếp hạng để tuyên bố hơn kém khi giao thức không đầy đủ.
- Không tạo mã nguồn, notebook hoặc trình diễn huấn luyện.
- Không đưa chỉ dẫn người soạn, thời lượng, tuyến cắt hoặc đáp án chi tiết lên mặt trang hay ghi chú diễn giả.
- Hậu kích hoạt và tiền kích hoạt chỉ xuất hiện trên mặt trang ở L05-X04; ghi chú L05-30/33 được phép nhắc ở mức điều kiện.
- Ví dụ mô tả ảnh ở L05-X05 chỉ là giao diện véc-tơ trừu tượng; cơ chế chuỗi thuộc Bài 07.
