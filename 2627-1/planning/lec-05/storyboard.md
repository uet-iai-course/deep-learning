# Bảng phân cảnh Bài 05

## Tuyến lõi — 100 phút

| Mã | Phút | Bước học tập | Luận điểm hoặc phép tính | Dữ kiện truyền | Nguồn |
|---|---:|---|---|---|---|
| L05-00 | 2 | Vấn đề | Kiến trúc phân bổ kích thước, tham số, MAC và đường đạo hàm | NCHW | đề cương |
| L05-01 | 2 | Hình thức | NCHW là lô–kênh–cao–rộng; khóa quy ước MAC | $1$ MAC ≈ $2$ FLOP nếu quy đổi | `source.md` |
| L05-02 | 3 | Ví dụ | LeNet: hai khối 5×5–sigmoid–gộp trung bình rồi ba tầng đầy đủ | $1×28^2→10$; cảnh báo bản gốc 32 | GT 132–135 |
| L05-03 | 1 | Kiểm tra | Ảnh và dữ liệu lớn hơn dồn chi phí vào đâu | LeNet → AlexNet | GT 136–139 |
| L05-04 | 3 | Vấn đề/hình thức | AlexNet sửa đổi khóa nhân, bước trượt, đệm và kênh | ảnh 227; tích chập 1 có 64 kênh | `lec09` 5–8 |
| L05-05 | 3 | Ví dụ | Dấu vết phần tích chập đến $256×6^2$ | 9216 phần tử | `lec09` 8 |
| L05-06 | 3 | Tính toán | FC6 có 37.748.736 trọng số và 4096 độ lệch | 9216→4096 | `lec09` 8–9 |
| L05-07 | 3 | Tính toán | Tái lập tham số tích chập 1/2 và tổng 61.100.840 | cùng quy ước có độ lệch | tính lại |
| L05-08 | 3 | Tính toán | Tái lập MAC tích chập 1/2 và tổng 716.767.232 | kích thước L05-05 + nhân L05-04 | tính lại |
| L05-09 | 3 | Triển khai | ReLU, gộp cực đại, bỏ nút ngẫu nhiên và GPU có vai trò riêng | cơ chế huấn luyện/suy luận | `lec09` 5–8; GT 140–142 |
| L05-10 | 2 | Kiểm tra | FC6 tập trung tham số; tích chập 2 tập trung MAC | chờ 30 giây rồi hiện đáp án | `lec09` 9 |
| L05-11 | 2 | Vấn đề | VGG-16 lặp năm khối có 2–2–3–3–3 tích chập | 3×3, đệm 1 | `lec09` 11–12 |
| L05-12 | 3 | Trực giác | Ba nhân 3×3 cho trường tiếp nhận 7×7 | bước trượt 1, độ giãn 1 | `lec09` 12 |
| L05-13 | 2 | Tính toán | $49K^2$ so với $27K^2$ trọng số | không độ lệch | `lec09` 12 |
| L05-14 | 3 | Ví dụ | Dấu vết VGG-16 qua năm khối và đầu FC6–FC8 | 224→7; 64→512 | GT 143–146 |
| L05-15 | 1 | Kiểm tra | Lợi ích, chi phí và giới hạn của khối đều đặn | đầu đầy đủ vẫn lớn | `lec09` 13–14 |
| L05-16 | 2 | Vấn đề | Một chuỗi chỉ dùng một thang không gian mỗi tầng | VGG → đa nhánh | `lec09` 18 |
| L05-17 | 2 | Tính toán | Phần gốc có đúng ba tích chập và 124.096 trọng số | $3×224^2→192×28^2$ | `lec09` 16–17 |
| L05-18 | 3 | Trực giác/ví dụ | Bốn nhánh, dữ kiện kênh và hình học giữ $H,W$ | 64/128/32/32; 96/16 | `lec09` 18; GT 149–151 |
| L05-19 | 3 | Hình thức | Ghép theo trục kênh tạo $N×256×H×W$ | cùng $N,H,W$ | GT 150–151 |
| L05-20 | 3 | Tính toán | 163.328 so với 393.216 trọng số; MAC tích chập bằng $H_s\cdot W_s\cdot|W|$ | chỉ đúng khi các tích chập cùng kích thước đầu ra; $W_s$ là bề rộng không gian | tính lại |
| L05-21 | 3 | Triển khai | Toàn GoogLeNet: phần gốc → 2–5–2 Inception → gộp toàn cục → lớp | 9 khối, 28→14→7 | GT 149–152 |
| L05-22 | 2 | Tính toán | 1.024.000 trọng số tầng phân loại so với 102.760.448 trọng số FC6 VGG | trọng số với trọng số | `lec09` 20–23 |
| L05-23 | 2 | Kiểm tra | Nhánh sai $H$ không ghép được | chờ 30 giây rồi hiện đáp án | `lec09` 18–20 |
| L05-24 | 2 | Vấn đề | Kích hoạt trung gian đổi thang trong huấn luyện | mạng sâu → BN | `lec10` 25–26 |
| L05-25 | 3 | Ví dụ/hình thức | $X:8×64×28×28$ cho 6272 giá trị mỗi kênh, rồi tổng quát hóa theo N,H,W | $\epsilon,\gamma,\beta$ | GT 153–156 |
| L05-26 | 3 | Trực giác kích thước | Minh họa ba trục giảm và phát rộng theo kênh, tham chiếu ví dụ trang trước | $1×64×1×1$ | GT 155–156 |
| L05-27 | 3 | Triển khai | Huấn luyện dùng thống kê lô; suy luận dùng thống kê cố định | cách ước lượng phụ thuộc khung | `lec10` 27–28; GT 156–158 |
| L05-28 | 3 | Kiểm tra | Đổi chế độ, kích thước hoặc thành phần lô có thể đổi đầu ra | không giới thiệu ResNet sớm | `lec10` 27–31 |
| L05-29 | 2 | Vấn đề | Mạng sâu hơn có thể tăng lỗi huấn luyện | không đồng nhất quá khớp | `lec09` 26–29 |
| L05-30 | 3 | Trực giác | Nhánh tắt đồng nhất: $s=x+F(x)$ | $s$ trước kích hoạt | `lec09` 29; GT 159–160 |
| L05-31 | 3 | Kiểm tra/hình thức | Cộng cần cùng N,C,H,W; ghép chỉ cần cùng N,H,W | chờ 30 giây rồi hiện đáp án | GT 159–160 |
| L05-32 | 3 | Triển khai | Phép chiếu 1×1 làm hai nhánh khớp kích thước | $s=P(x)+F(x)$ | GT 160–161 |
| L05-33 | 4 | Hình thức | Véc-tơ hóa tensor; $I+J_F$, $J_P+J_F$, tích Jacobian chuyển vị–véc-tơ $\bar x=J_s^\top\bar s$; nhắc quy ước gradient cột và tiên quyết Jacobian Bài 02–03 | $J_F,J_P\in\mathbb R^{d_{out}\times d_{in}}$; trường hợp hậu kích hoạt đưa xuống ghi chú | suy ra; `lec09` 29 |
| L05-34 | 3 | Tính toán | Một ánh xạ 3×3 so với cả nhánh cổ chai | 589.824/69.632 mỗi vị trí | `lec09` 30 |
| L05-35 | 2 | Triển khai | So cấu trúc khối cơ bản với khối cổ chai; không tái dùng tỷ lệ 8,47 cho toàn khối | hai 3×3 so với 1×1–3×3–1×1 | `lec09` 30; GT 161–162 |
| L05-36 | 2 | Triển khai/kiểm tra | ResNet-18: phần gốc → bốn giai đoạn 2–2–2–2 → gộp toàn cục; câu nối sang học chuyển giao | chờ 20 giây; chiếu ở giai đoạn 2–4 | `lec09` 31; GT 161–163 |
| L05-37 | 3 | Ứng dụng | Học chuyển giao tách gradient khỏi chế độ mô-đun | thân cố định/đầu mới; chính sách BN | `lec09` 44–46 |
| L05-38 | 2 | Kiểm tra | Chọn kiến trúc theo bốn trục | toàn bộ mạch | tổng hợp |

Tổng lõi: **100 phút**.

## Tuyến mở rộng — 20 phút

| Mã | Phút | Nội dung | Vai trò | Nguồn |
|---|---:|---|---|---|
| L05-X01 | 4 | Kết quả lịch sử và cảnh báo giao thức | Bối cảnh, không xếp hạng tuyệt đối | `lec09` 33 |
| L05-X02 | 4 | Bộ phân loại phụ GoogLeNet | Phụ thuộc cấu hình huấn luyện | `lec09` 23 |
| L05-X03 | 4 | Diễn giải nhiều đường của ResNet | Trực giác nghiên cứu | `lec09` 32 |
| L05-X04 | 4 | Hậu kích hoạt và tiền kích hoạt | Chỉ xuất hiện sau cụm ResNet | `lec10` 31–32 |
| L05-X05 | 4 | Véc-tơ đặc trưng nối sang mô tả ảnh | Cầu nối trừu tượng sang Bài 07 | `lec09` 45 |

Tổng mở rộng: **20 phút**.

## Chu trình học tập, dữ kiện và điều hướng

| Cụm | Sáu bước và mã trang | Đầu vào → sản phẩm | Dữ kiện truyền | Bước gộp hoặc không áp dụng | Câu nối | Thời lượng/điều hướng |
|---|---|---|---|---|---|---|
| LeNet rút gọn | Vấn đề L05-00–01 → trực giác/ví dụ L05-02 → hình thức gộp ở L05-02 → triển khai không áp dụng → kiểm tra L05-03 | CNN cơ bản → mốc khối và dấu vết để so AlexNet | 28 so với 32; 5×5–sigmoid–gộp trung bình; 120–84–10 | Không có mã vì nguồn không yêu cầu; hình thức gộp với dấu vết để tránh lặp Bài 04 | “Ảnh lớn hơn dồn chi phí vào đâu?” | 8 phút; xuống L05-00→03, phải ở L05-03 |
| AlexNet | Vấn đề L05-04 → trực giác/dấu vết L05-05 → ví dụ L05-06 → hình thức/tính L05-07–08 → triển khai L05-09 → kiểm tra L05-10 | đặc tả toán tử → tổng tham số và MAC tái lập được | 227, 64, 9216, 4096 | Hình thức và tính toán gộp vì mỗi công thức dùng trực tiếp dấu vết | “Khối VGG thay lựa chọn từng tầng bằng quy tắc lặp.” | 20 phút; xuống L05-04→10, chờ 30 giây ở L05-10, phải ở cuối cụm |
| VGG | Vấn đề L05-11 → trực giác/ví dụ trường tiếp nhận L05-12 → hình thức/tính L05-13 → triển khai bằng dấu vết L05-14 → kiểm tra L05-15 | khối 3×3 → phép tính trọng số → dấu vết năm khối và đầu đầy đủ | 2–2–3–3–3; 224→7 | Ví dụ trực giác và trường tiếp nhận gộp ở L05-12; không có mã vì nguồn không yêu cầu | “Một chuỗi chưa xử lý nhiều thang trong cùng khối.” | 11 phút; xuống L05-11→15, phải ở L05-15 |
| GoogLeNet/Inception | Vấn đề L05-16 → ví dụ phần gốc L05-17 → trực giác/ví dụ khối L05-18 → hình thức L05-19 → tính L05-20 → triển khai L05-21 → tính/so L05-22 → kiểm tra L05-23 | phần gốc + một khối → dấu vết đủ 9 khối và đầu phân loại | $192×28^2$, 64/128/32/32, 2–5–2 | Ví dụ phần gốc đứng trước khối để cung cấp $C_{in}=192$; L05-21 thay bảng nhánh lặp | “Mạng nhiều tầng tiếp theo cần phân biệt thống kê huấn luyện và suy luận.” | 20 phút; xuống L05-16→23, chờ 30 giây ở L05-23, phải ở cuối cụm |
| Chuẩn hóa theo lô | Vấn đề L05-24 → ví dụ và hình thức L05-25 → trực giác hóa sau công thức L05-26 → triển khai L05-27 → kiểm tra L05-28 | $X:NCHW$ → 6272 giá trị/kênh → công thức → hai chế độ | $8×64×28×28$, 6272, $1×64×1×1$ | Ví dụ số đứng trước công thức ngay trên L05-25; L05-26 củng cố công thức bằng hình trục giảm và phát rộng | “Chuẩn hóa kiểm soát thang kích hoạt; ResNet thêm đường truyền trực tiếp.” | 14 phút; xuống L05-24→28, phải ở L05-28 |
| ResNet | Vấn đề L05-29 → trực giác L05-30 → ví dụ/điều kiện L05-31–32 → hình thức L05-33 → tính L05-34 → triển khai L05-35 → triển khai/kiểm tra L05-36 | $x,F,P$ → kích thước hai nhánh → Jacobian và tích $J^\top v$ → dấu vết ResNet-18 | $s=x+F$, $s=P+F$, $J_s$, 2–2–2–2 | L05-31 gộp điều kiện với kiểm tra; L05-36 gộp dấu vết với câu hỏi phép chiếu | “Thân đã học có thể tái dùng nhưng gradient và chế độ là hai lựa chọn.” | 22 phút; xuống L05-29→36, chờ 30 giây ở L05-31 và 20 giây ở L05-36, phải ở cuối cụm |
| Học chuyển giao | Vấn đề/ví dụ L05-37 → trực giác/hình thức/triển khai/kiểm tra gộp L05-37; tổng hợp riêng L05-38 | tập mới nhỏ, gần miền nguồn → cấu hình thân/đầu và BN | gradient; huấn luyện/suy luận | Không có phép tính số trong nguồn; gộp chu trình trên một trang để giữ vai trò cầu nối ngắn | Bảng bốn trục ở L05-38 tổng hợp toàn bài | 3 phút; L05-38 là 2 phút kết luận riêng. Lõi: tại L05-37 nhấn End tới L05-38; mở rộng: tại L05-37 nhấn phải sang L05-X01, xuống qua L05-X05 rồi xuống tới L05-38 |

Điều hướng lõi: trong mỗi cụm, nhấn xuống để đi qua các trang; tại trang cuối cụm, nhấn phải để sang trang đầu cụm kế tiếp. Tuyến lõi kết thúc tại L05-37: nhấn End để tới L05-38, trang cuối toàn deck, và dừng ở đó nếu cắt tuyến mở rộng. Tuyến mở rộng: tại L05-37 nhấn phải sang L05-X01, nhấn xuống lần lượt qua L05-X02–L05-X05, rồi nhấn xuống một lần nữa để tới L05-38.

## Bài tập 50 phút riêng

1. So sánh AlexNet, VGG và ResNet theo cùng bốn trục: 20 phút.
2. Tính kích thước và MAC của một đoạn AlexNet: 15 phút.
3. Thiết kế khối thặng dư $56^2×64\rightarrow28^2×128$ có phép chiếu: 10 phút.
4. Chọn đóng băng hoặc tinh chỉnh và chính sách BN cho nhiệm vụ mới: 5 phút.
