# Ghi chú dành cho người soạn Bài 01

## Tuyến giảng

Tuyến lõi đi thẳng từ một khó khăn kỹ thuật đến một cơ chế có thể tính được:

1. Không biết viết quy tắc cho một số ánh xạ đầu vào–đầu ra.
2. Bốn mốc lịch sử nối với bốn thay đổi kỹ thuật, rồi học máy dùng dữ liệu để ước lượng tham số của một họ mô hình.
3. Dữ liệu, tham số và dự đoán được phân biệt trước khi khóa bài toán phân loại nhị phân có giám sát.
4. Một mô hình affine chỉ tạo biên phẳng; XOR là phản ví dụ tối thiểu.
5. Xếp chồng affine vẫn là affine.
6. Hàm không affine tạo biểu diễn mới; MLP hiện đại đặt activation ở đơn vị ẩn và tạo logit ở tầng ra.
7. Một forward pass 2–2–1 giải XOR và cho phép kiểm tra shape, giá trị, tham số.

Không dùng phần mở rộng để vá khái niệm lõi. Dành đúng 16 phút cho L01-00–09. Nghỉ ngắn sau L01-18, sau khi đã khóa cấu trúc MLP và shape, rồi mới chọn activation. Nếu chỉ có 100 phút, kết thúc ở L01-33. Nếu có thêm 20 phút, đi liền mạch qua L01-X01–X06: kiểm shape ba tầng → sâu/rộng → biên nhiều mảnh → xấp xỉ phổ dụng → biểu diễn phân tán → kiểm tra. Không nhảy riêng vào một trang giữa tuyến mở rộng.

## Điểm cần nhấn và lỗi dễ mắc

- Gọi $Wx+b$ là phép affine. Chỉ $Wx$ là tuyến tính theo nghĩa toán học.
- Không gọi logit là xác suất trước khi áp dụng sigmoid hoặc softmax.
- Tách tham số khỏi siêu tham số; batch size không làm tăng số tham số.
- Khóa quy ước batch-first: mỗi hàng của $X$ là $x_i^\top$, ma trận trọng số nhân bên phải.
- Tách huấn luyện khỏi suy luận; chỉ pha huấn luyện cập nhật $\theta$.
- ReLU áp dụng theo phần tử và không đổi shape.
- ReLU không khả vi tại 0; phát biểu đúng là khả vi gần như mọi nơi.
- Perceptron ngưỡng cứng dùng để giải thích lịch sử và hình học. MLP hiện đại trong bài dùng ReLU ở đơn vị ẩn, tạo logit rồi mới đổi thành dự đoán.
- Hàm tầng ra phụ thuộc bài toán. Softmax chuẩn hóa theo trục lớp trong từng hàng $Z\in\mathbb R^{B\times k}$; loss ổn định số thường nhận logits.
- Khi cần tính softmax tường minh, trừ $m_i=\max_r Z_{ir}$ khỏi mọi logit trong hàng $i$ trước khi lấy mũ.
- Nguồn chỉ nêu xấp xỉ phổ dụng ở mức khái quát. Không thêm điều kiện chi tiết ngoài nguồn; chỉ chốt rằng mệnh đề không bảo đảm tìm tham số, dữ liệu cần có hay khả năng khái quát.
- Biểu diễn ẩn có thể phân tán; không buộc mỗi đơn vị mang một khái niệm riêng.

## Đáp án kiểm tra trên deck

### ReLU trên vector

$\operatorname{ReLU}([-2,0,3])=[0,0,3]$.

### Huấn luyện, dữ liệu và dự đoán

- Nhãn $y$ tham gia tính mất mát và $\theta$ được cập nhật trong huấn luyện.
- Trong $\hat y=f_\theta(x)$, $x$ được quan sát, $\theta$ được học và $\hat y$ được tạo ra.

### Shape trung gian

Với $B=16,d=8,h=12,k=4$: $W_1:8\times12$, $H:16\times12$, $W_2:12\times4$, $Z:16\times4$.

### Chọn activation

- Đơn vị ẩn: ReLU là lựa chọn điển hình trong bài.
- Một logit nhị phân: sigmoid.
- $k$ lớp loại trừ nhau: softmax theo trục lớp của từng hàng.

### Một hàng XOR trước khi hiện bảng

Với $(x_1,x_2)=(0,1)$: $H=(1,0)$, logit $0.5$, $p\approx0.622$, $\hat y=1$.

### Chuỗi affine rồi ReLU của XOR

Với $W_1=\begin{bmatrix}1&1\\1&1\end{bmatrix}$ và $b_1=[0,-1]$, bốn hàng của $A=XW_1+b_1$ là $(0,-1),(1,0),(1,0),(2,1)$. ReLU chỉ thay $(0,-1)$ bằng $(0,0)$; ba vị trí còn lại không đổi.

### Shape và số tham số cuối bài

Với $X\in\mathbb R^{32\times10}$, $h=20$, $k=3$:

- $W_1\in\mathbb R^{10\times20}$, $b_1\in\mathbb R^{20}$;
- $H\in\mathbb R^{32\times20}$;
- $W_2\in\mathbb R^{20\times3}$, $b_2\in\mathbb R^3$;
- $Z\in\mathbb R^{32\times3}$;
- tổng tham số: $10\cdot20+20+20\cdot3+3=283$.

XOR cần phép không affine vì mọi chuỗi chỉ gồm affine rút thành một phép affine. Bao lồi của hai lớp XOR giao nhau, nên một biên affine không thể tách nghiêm ngặt hai lớp.

## Bài tập 50 phút

### Hoạt động 1: XOR, 10 phút

Đề: Vẽ bốn điểm Boolean và chứng minh trực quan rằng không có một đường thẳng phân tách hai lớp XOR.

Cách tổ chức: 4 phút làm cá nhân, 3 phút so sánh theo cặp, 3 phút chữa.

Đáp án: hai điểm dương $(0,1),(1,0)$ nằm ở hai góc đối diện; hai điểm âm $(0,0),(1,1)$ nằm ở hai góc còn lại. Bao lồi của hai lớp giao nhau tại $(0.5,0.5)$, nên không có siêu phẳng phân tách nghiêm ngặt.

### Hoạt động 2: vẽ MLP và ghi shape, 20 phút

Đề: Batch có $B=16$, mỗi mẫu có $d=8$ đặc trưng. MLP có hai tầng ẩn lần lượt 12 và 5 đơn vị ReLU, sau đó tạo 4 logit. Vẽ mạng ở mức tầng, ghi shape của tensor và tham số, rồi tính số tham số. Mỗi hàng của $X$ là $x_i^\top$.

Đáp án:

- $X:16\times8$;
- $W_1:8\times12$, $b_1:12$, $H_1:16\times12$;
- $W_2:12\times5$, $b_2:5$, $H_2:16\times5$;
- $W_3:5\times4$, $b_3:4$, $Z:16\times4$;
- số tham số: $8\cdot12+12+12\cdot5+5+5\cdot4+4=197$.

Lỗi cần bắt: cộng batch size vào số tham số; đảo shape của $W$; áp dụng softmax theo chiều batch.

### Hoạt động 3: affine và ReLU, 15 phút

Đề: Với $H=XW_1+b_1$ và $Y=HW_2+b_2$, rút gọn $Y$ về một phép affine của $X$. Sau đó giải thích vì sao thay $H$ bằng $\operatorname{ReLU}(XW_1+b_1)$ làm phép rút gọn thất bại.

Đáp án:

$$
Y=X(W_1W_2)+(b_1W_2+b_2).
$$

Khi có ReLU, không tồn tại một ma trận cố định có thể thay $\operatorname{ReLU}(XW_1+b_1)$ cho mọi $X$, vì ánh xạ thay đổi hệ số theo dấu của từng tiền kích hoạt. Hàm trở thành tuyến tính từng đoạn.

### Hoạt động 4: quiz, 5 phút

1. Đại lượng nào được cập nhật trong huấn luyện? Đáp án: tham số $\theta$.
2. ReLU có đổi shape không? Đáp án: không, vì áp dụng theo phần tử.
3. Một logit nhị phân trở thành xác suất bằng hàm nào? Đáp án: sigmoid.
4. MLP $d$–$h$–$k$ có bao nhiêu tham số? Đáp án: $dh+h+hk+k$.

## Nguồn và trạng thái kiểm chứng

- Nguồn chính: `lec05_multilayer.pdf`, tr. 2–35; trang 35 chỉ dùng cho mạng sâu hơn hai tầng, không dùng làm bằng chứng về độ rộng.
- Nguồn phụ: `lec01_intro.pdf`, tr. 3–15, 17–24; `lec02_linear_part1.pdf`, tr. 15–21.
- Nguồn kiểm chứng: `hocsau_draft.pdf`, PDF tr. 25–45, 55–56, 66–73, 83–90.
- Ví dụ XOR đã tự tính lại theo cả bốn hàng; chi tiết nằm trong `review-log.md`.
- Không có code demo, raster hoặc kết quả thực nghiệm.
- Điều hướng: dừng ở L01-33 cho tuyến 100 phút; đi tiếp L01-X01–X06 cho tuyến 120 phút; không quay lại trang mở rộng cũ đã bỏ.
- Bản chỉnh sửa đã xử lý báo cáo phản biện; vẫn cần điều phối viên hoàn tất kiểm định trực quan và kiểm tra chạy cục bộ trước bàn giao.
