# Ghi chú cho người soạn — Bài 05

## Tuyến giảng

- Lõi L05-00–L05-37: đúng 98 phút; L05-38 là trang kết luận 2 phút, nằm sau tuyến mở rộng trong cấu trúc mạch nhưng thuộc tuyến lõi về thời lượng (tổng lõi gồm L05-38 vẫn 100 phút).
- Mở rộng L05-X01–L05-X05: 20 phút; có thể bỏ nguyên cụm dọc.
- Không đưa mã trang, thời lượng, tuyến cắt, trạng thái rà soát hoặc đáp án chi tiết lên mặt trang và ghi chú diễn giả.
- Khi so sánh kiến trúc, luôn hỏi cùng bốn đại lượng: kích thước tensor, tham số, MAC và đường đạo hàm.
- Trong mỗi cụm lõi, nhấn xuống; ở trang cuối cụm, nhấn phải sang trang đầu cụm kế tiếp. Tuyến lõi: tại L05-37 nhấn End tới L05-38, trang cuối toàn deck; dừng ở đó nếu cắt tuyến mở rộng. Tuyến mở rộng: tại L05-37 nhấn phải sang L05-X01, nhấn xuống qua L05-X02–L05-X05, rồi nhấn xuống tới L05-38.

## Đáp án và điểm dừng tương tác

- L05-10: FC6 nối mọi cặp 9216–4096 nên giữ nhiều trọng số; tích chập 2 dùng nhân 5×5 trên $27^2$ vị trí nên giữ nhiều MAC. Chờ khoảng 30 giây.
- L05-23: không ghép được nhánh $N×32×(H-2)×W$ với các nhánh $N×C_i×H×W$; phải sửa đệm. Chờ khoảng 30 giây.
- L05-31: cộng cần cùng N,C,H,W; ghép theo C chỉ cần cùng N,H,W. Chờ khoảng 30 giây.
- L05-36: khối đầu ở giai đoạn 2–4 tăng kênh và giảm nửa không gian, nên nhánh tắt cần phép chiếu. Chờ khoảng 20 giây.
- L05-37: khi suy luận cuối cùng, toàn bộ mô-đun ở chế độ suy luận.

## Quy tắc và phạm vi nội bộ

- LeNet trên slide là biến thể giáo trình 28×28 có đệm ở tầng đầu; không hòa với dấu vết LeNet-5 nguyên bản 32×32.
- AlexNet dùng duy nhất bảng sửa đổi 227×227, tích chập 1 có 64 kênh; không ghép số từ bản gốc hai GPU.
- GoogLeNet có ba tích chập trong phần gốc và chín khối Inception chia 2–5–2; L05-21 phải giữ dấu vết toàn mạng.
- ResNet-18 đếm một tích chập đầu, 16 tích chập trong tám khối cơ bản và một tầng đầy đủ cuối. Không đếm BN, ReLU, gộp hoặc phép cộng; phép chiếu được ghi riêng theo quy ước kiến trúc.
- L05-X04 mới giới thiệu hậu kích hoạt và tiền kích hoạt. L05-X05 chỉ nối giao diện véc-tơ sang Bài 07, không dạy mô hình chuỗi.
- Với học chuyển giao, luôn tách hai câu hỏi: tham số nào có gradient và mô-đun nào ở chế độ huấn luyện/suy luận. Khi tinh chỉnh, chính sách BN phải được ghi rõ.

## Bài tập 50 phút

### So sánh AlexNet, VGG và ResNet — 20 phút

Cho sinh viên điền bảng gồm mẫu khối, cách giảm độ phân giải, nơi tập trung tham số, đường đạo hàm và giới hạn. Đáp án cốt lõi: AlexNet dùng tầng riêng lẻ và đầu đầy đủ lớn; VGG lặp khối 3×3; ResNet thêm nhánh đồng nhất/chiếu. Không chấp nhận kết luận “mới hơn nên tốt hơn” nếu không có giao thức.

### Kích thước và MAC của AlexNet — 15 phút

Cho đầu vào 3×227×227, tích chập 1 có 64 nhân 11×11, bước trượt 4, đệm 2; sau đó gộp 3×3, bước trượt 2. Đáp án: tích chập 1 cho 64×56×56; gộp 1 cho 64×27×27; tích chập 1 có 72.855.552 MAC cho một mẫu. Yêu cầu ghi công thức lấy phần nguyên dưới.

### Khối thặng dư đổi kích thước — 10 phút

Thiết kế $56×56×64→28×28×128$. Nhánh chính dùng tầng đầu bước trượt 2; nhánh tắt dùng chiếu 1×1, bước trượt 2, tạo 128 kênh. Hai nhánh phải cùng $N×128×28×28$ trước phép cộng. Không cho phép phát rộng.

### Đóng băng hoặc tinh chỉnh — 5 phút

Tình huống: tập mới nhỏ và gần nguồn; tập mới lớn nhưng khác miền. Đáp án định hướng: trường hợp đầu đóng băng phần lớn thân, đặt thân ở chế độ suy luận và học đầu mới; trường hợp sau tinh chỉnh nhiều tầng hơn hoặc toàn bộ, đồng thời chọn rõ BN dùng thống kê cố định hay cập nhật. Khi suy luận, toàn bộ mô-đun ở chế độ suy luận.

- L05-33: mặt trang chỉ giữ hai thẻ đồng nhất và phép chiếu cùng dòng nhắc quy ước gradient cột và tiên quyết Jacobian Bài 02–03; trường hợp hậu kích hoạt $J_z=D_{\mathrm{ReLU}}(s)J_s$ nằm trong ghi chú diễn giả.
- L05-20: công thức MAC dùng $H_s,W_s$ là kích thước không gian đầu ra; $|W|$ là số trọng số. Công thức chỉ đúng khi các tích chập cùng kích thước đầu ra.
- L05-26: không lặp lại con số 6272; tham chiếu ví dụ ở trang trước và tập trung trục giảm, phát rộng.
- L05-36: ghi chú diễn giả có câu nối sang học chuyển giao (tái dùng thân đã học → hai quyết định gradient/chế độ).

## Điểm cần kiểm tra sau chỉnh sửa

- Nếu đổi AlexNet, phải tính lại toàn bộ chuỗi kích thước, tổng tham số và MAC; không ghép bản gốc với bản sửa đổi.
- Nếu đổi nhánh Inception, phải kiểm tra cùng H,W trước ghép và cộng lại số kênh theo trục 1.
- Nếu đổi BN, phải kiểm tra trục N,H,W, hình dạng $\gamma/\beta$, $\epsilon$, thống kê cố định và chế độ suy luận. Không khóa một quy tắc cập nhật cụ thể khi nguồn không khóa.
- Nếu đổi khối ResNet, phải kiểm tra kích thước hai nhánh, vị trí bước trượt, phép chiếu và cấu trúc toán tử tiền/hậu kích hoạt.
- Không dùng bảng lỗi, FLOP hoặc xếp hạng nếu không bổ sung giao thức đã được người dùng duyệt.
