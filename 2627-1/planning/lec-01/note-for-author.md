# Ghi chú dành cho người soạn Bài 01

## Tuyến giảng

Tuyến lõi đi thẳng từ một khó khăn kỹ thuật đến một cơ chế có thể tính được:

1. Không biết viết quy tắc cho một số ánh xạ đầu vào–đầu ra.
2. Bốn mốc lịch sử nối với bốn thay đổi kỹ thuật, rồi học máy dùng dữ liệu để ước lượng tham số của một họ mô hình.
3. Dữ liệu, tham số và dự đoán được phân biệt trước khi khóa bài toán phân loại nhị phân có giám sát.
4. Một mô hình dùng biến đổi afin chỉ tạo biên phẳng; XOR là phản ví dụ tối thiểu.
5. Hợp thành nhiều biến đổi afin vẫn là một biến đổi afin.
6. Hàm kích hoạt phi tuyến tạo biểu diễn mới; MLP hiện đại đặt hàm kích hoạt ở đơn vị ẩn và tạo logit ở tầng ra.
7. Một lượt lan truyền xuôi 2–2–1 giải XOR và cho phép kiểm tra kích thước tensor, giá trị, tham số.

Không dùng phần mở rộng để vá khái niệm lõi. Dành đúng 16 phút cho L01-00–09. Sau L01-02, dùng 2 phút hiện có để thảo luận nhanh một ứng dụng trong ba ví dụ trên trang; không cộng thêm thời gian, rút bớt phần diễn giải ở L01-03 nếu cần. Nghỉ ngắn sau L01-18, sau khi đã khóa cấu trúc MLP và kích thước tensor, rồi mới chọn hàm kích hoạt. Nếu chỉ có 100 phút, kết thúc ở L01-33. Nếu có thêm 20 phút, đi liền mạch qua L01-X01–X06: kiểm tra kích thước tensor qua ba tầng → sâu/rộng → biên nhiều mảnh → xấp xỉ phổ dụng → biểu diễn phân tán → kiểm tra. Không nhảy riêng vào một trang giữa tuyến mở rộng. Cách chốt tuyến 120 phút ở L01-X06: thu hồi câu hỏi mở đầu về tác vụ khó viết quy tắc, chốt rằng MLP là một cách xây hệ thống từ dữ liệu, rồi chấm ba câu kiểm tra cuối trước khi kết thúc.

## Điểm cần nhấn và lỗi dễ mắc

- Gọi $Wx+b$ là biến đổi afin. Chỉ $Wx$ là tuyến tính theo nghĩa toán học.
- Quy ước nhãn và ngưỡng: deck dùng nhãn $\{0,1\}$ với hàm chỉ thị, khác slide nguồn dùng $\{-1,1\}$ với sgn; perceptron gán nhãn 1 khi $z=0$; dự đoán cứng lấy bằng ngưỡng $0.5$ trên xác suất.
- Tham số XOR $W_1,b_1$ xuất hiện lần đầu ở L01-24, trước khi mạng đầy đủ hiện ở L01-29; nhấn rằng chuỗi L01-25–28 dùng đúng bộ này.
- Không gọi logit là xác suất trước khi áp dụng sigmoid hoặc softmax.
- Tách tham số khỏi siêu tham số; kích thước lô không làm tăng số tham số.
- Khóa quy ước dữ liệu theo hàng: mỗi hàng của $X$ là $x_i^\top$, ma trận trọng số nhân bên phải.
- Tách huấn luyện khỏi suy luận; chỉ pha huấn luyện cập nhật $\theta$.
- ReLU áp dụng theo phần tử và không đổi kích thước tensor.
- ReLU không khả vi tại 0; phát biểu đúng là khả vi gần như mọi nơi.
- Perceptron ngưỡng cứng dùng để giải thích lịch sử và hình học. MLP hiện đại trong bài dùng ReLU ở đơn vị ẩn, tạo logit rồi mới đổi thành dự đoán.
- Hàm tầng ra phụ thuộc bài toán. Softmax chuẩn hóa theo trục lớp trong từng hàng $Z\in\mathbb R^{B\times k}$; hàm mất mát ổn định số thường nhận logit.
- Khi cần tính softmax tường minh, trừ $m_i=\max_r Z_{ir}$ khỏi mọi logit trong hàng $i$ trước khi lấy mũ.
- Nguồn chỉ nêu xấp xỉ phổ dụng ở mức khái quát. Không thêm điều kiện chi tiết ngoài nguồn; chỉ chốt rằng mệnh đề không bảo đảm tìm tham số, dữ liệu cần có hay khả năng khái quát.
- Biểu diễn ẩn có thể phân tán; không buộc mỗi đơn vị mang một khái niệm riêng.

## Đáp án kiểm tra trên deck

### ReLU trên vector

$\operatorname{ReLU}([-2,0,3])=[0,0,3]$.

### Huấn luyện, dữ liệu và dự đoán

- Nhãn $y$ tham gia tính mất mát và $\theta$ được cập nhật trong huấn luyện.
- Trong $\hat y=f_\theta(x)$, $x$ được quan sát, $\theta$ được học và $\hat y$ được tạo ra.

### Kích thước tensor trung gian

Với $B=16,d=8,h=12,k=4$: $W_1:8\times12$, $H:16\times12$, $W_2:12\times4$, $Z:16\times4$.

### Chọn hàm kích hoạt

- Đơn vị ẩn: ReLU là lựa chọn điển hình trong bài.
- Một logit nhị phân: sigmoid.
- $k$ lớp loại trừ nhau: softmax theo trục lớp của từng hàng.

### Một hàng XOR trước khi hiện bảng

Với $(x_1,x_2)=(0,1)$: $H=(1,0)$, logit $0.5$, $p\approx0.622$, $\hat y=1$.

### Chuỗi biến đổi afin rồi ReLU của XOR

Với $W_1=\begin{bmatrix}1&1\\1&1\end{bmatrix}$ và $b_1=[0,-1]$, bốn hàng của $A=XW_1+b_1$ là $(0,-1),(1,0),(1,0),(2,1)$. ReLU chỉ thay $(0,-1)$ bằng $(0,0)$; ba vị trí còn lại không đổi.

### Kích thước tensor và số tham số cuối bài

Với $X\in\mathbb R^{32\times10}$, $h=20$, $k=3$:

- $W_1\in\mathbb R^{10\times20}$, $b_1\in\mathbb R^{20}$;
- $H\in\mathbb R^{32\times20}$;
- $W_2\in\mathbb R^{20\times3}$, $b_2\in\mathbb R^3$;
- $Z\in\mathbb R^{32\times3}$;
- tổng tham số: $10\cdot20+20+20\cdot3+3=283$.

XOR cần hàm phi tuyến vì mọi chuỗi chỉ gồm biến đổi afin rút thành một biến đổi afin. Bao lồi của hai lớp XOR giao nhau, nên biên của một biến đổi afin không thể tách nghiêm ngặt hai lớp.

## Bài tập 50 phút

### Hoạt động 1: XOR, 10 phút

Đề: Vẽ bốn điểm Boolean và chứng minh trực quan rằng không có một đường thẳng phân tách hai lớp XOR.

Cách tổ chức: 4 phút làm cá nhân, 3 phút so sánh theo cặp, 3 phút chữa.

Đáp án: hai điểm dương $(0,1),(1,0)$ nằm ở hai góc đối diện; hai điểm âm $(0,0),(1,1)$ nằm ở hai góc còn lại. Bao lồi của hai lớp giao nhau tại $(0.5,0.5)$, nên không có siêu phẳng phân tách nghiêm ngặt.

### Hoạt động 2: vẽ MLP và ghi kích thước tensor, 20 phút

Đề: Lô dữ liệu có $B=16$, mỗi mẫu có $d=8$ đặc trưng. MLP có hai tầng ẩn lần lượt 12 và 5 đơn vị ReLU, sau đó tạo 4 logit. Vẽ mạng ở mức tầng, ghi kích thước của tensor và tham số, rồi tính số tham số. Mỗi hàng của $X$ là $x_i^\top$.

Đáp án:

- $X:16\times8$;
- $W_1:8\times12$, $b_1:12$, $H_1:16\times12$;
- $W_2:12\times5$, $b_2:5$, $H_2:16\times5$;
- $W_3:5\times4$, $b_3:4$, $Z:16\times4$;
- số tham số: $8\cdot12+12+12\cdot5+5+5\cdot4+4=197$.

Lỗi cần bắt: cộng kích thước lô vào số tham số; đảo kích thước của $W$; áp dụng softmax theo chiều lô.

### Hoạt động 3: biến đổi afin và ReLU, 15 phút

Đề: Với $H=XW_1+b_1$ và $Y=HW_2+b_2$, rút gọn $Y$ về một biến đổi afin của $X$. Sau đó giải thích vì sao thay $H$ bằng $\operatorname{ReLU}(XW_1+b_1)$ làm phép rút gọn thất bại.

Đáp án:

$$
Y=X(W_1W_2)+(b_1W_2+b_2).
$$

Khi có ReLU, không tồn tại một ma trận cố định có thể thay $\operatorname{ReLU}(XW_1+b_1)$ cho mọi $X$, vì ánh xạ thay đổi hệ số theo dấu của từng tiền kích hoạt. Hàm trở thành tuyến tính từng đoạn.

### Hoạt động 4: quiz, 5 phút

1. Đại lượng nào được cập nhật trong huấn luyện? Đáp án: tham số $\theta$.
2. ReLU có đổi kích thước tensor không? Đáp án: không, vì áp dụng theo phần tử.
3. Một logit nhị phân trở thành xác suất bằng hàm nào? Đáp án: sigmoid.
4. MLP $d$–$h$–$k$ có bao nhiêu tham số? Đáp án: $dh+h+hk+k$.

## Nguồn và trạng thái kiểm chứng

- Nguồn chính: `lec05_multilayer.pdf`, tr. 2–35; ở L01-X02, trang 35 chỉ làm bằng chứng cho độ sâu, còn trang 29 làm bằng chứng cho độ rộng.
- Nguồn phụ: `lec01_intro.pdf`, tr. 3–15, 17–24; `lec02_linear_part1.pdf`, tr. 15–21.
- Nguồn kiểm chứng: `hocsau_draft.pdf`, PDF tr. 25–45, 55–56, 66–73, 83–90.
- Ví dụ XOR đã tự tính lại theo cả bốn hàng; chi tiết nằm trong `review-log.md`.
- Không có code demo, raster hoặc kết quả thực nghiệm.
- Điều hướng: dừng ở L01-33 cho tuyến 100 phút; đi tiếp L01-X01–X06 cho tuyến 120 phút; không quay lại trang mở rộng cũ đã bỏ.
- Bản chỉnh sửa đã xử lý báo cáo phản biện; vẫn cần điều phối viên hoàn tất kiểm định trực quan và kiểm tra chạy cục bộ trước bàn giao.

## Ghi chú nội bộ cho lecture note

### Bản đồ ngữ nghĩa NT01–NT09

Ánh xạ `data-slide-id` theo đặc tả: NT01 L01-00–05; NT02 L01-06–09; NT03 L01-10–12; NT04 L01-13,L01-25; NT05 L01-14–16; NT06 L01-17–18,L01-31–32 và bài luyện mở rộng L01-X01; NT07 L01-19–23; NT08 L01-24–30,L01-33; NT09 L01-X02–X06. NT06 hoàn tất nội dung cốt lõi ở L01-32; L01-X01 chỉ củng cố. L01-33 là kiểm tra kết thúc tuyến lõi, không thuộc chủ đề bổ sung NT09.

### Đáp án nội bộ

Biên $w=(1,-1)$, $b=-0.5$ tương đương $x_2=x_1-0.5$; kiểm tra dấu theo $z$. Khi tăng $h$ từ $20$ lên $40$, giữ nguyên $Z:32\times3$; tổng tham số thành $10\cdot40+40+40\cdot3+3=563$. Với mẫu XOR $(0,1)$: $A=(1,0)$, $H=(1,0)$, $z=0.5$, $p\approx0.622$, $\hat y=1$. Mạng XOR có $9$ tham số; ví dụ cấu hình $B=32,d=10,h=20,k=3$ có $283$ tham số. Các phép tính này phục vụ kiểm chứng số, không xuất hiện dưới dạng mã trong nội dung công khai.

### Nguồn cần giữ

lec01_intro slide 3–15, 17–24; lec02_linear_part1 slide 15–21; lec05_multilayer slide 2–35; GT PDF trang 25–45, 55–56, 66–73, 83–90; DOCX Buổi 1. Việc tra cứu ngược theo mục lục các nguồn này là cần thiết khi hiệu đính từng phần, ngoài luồng tự kiểm định nghĩa đã được phê duyệt.

### Kiểm tra hai SVG

Lecture note dùng hai SVG: `xor-points.svg` và `xor-mlp.svg`. Kiểm tra `role`, `title`, `desc`, văn bản thay thế và đường dẫn hợp lệ trong thư mục tài nguyên. Nếu thiếu hoặc lệch đường dẫn, phải ghi nhận trước khi chốt phiên bản công khai.

### `$no-ai-slop` và nội dung công khai

Trong nội dung công khai không có mã NT, thời lượng, trạng thái kiểm chứng, chỉ dẫn người viết/diễn giả, từ “dossier”, dấu vết AI hoặc câu hỏi tu từ. Câu tự kiểm được giữ vì có mục đích học tập rõ ràng.

### Mạch khái niệm theo `$quill`

Mạch tường thuật: XOR → giới hạn afin → phi tuyến → MLP → sức biểu diễn → Buổi 02. Các ký hiệu $A,H,z,p,\hat y$ được dùng xuyên suốt để thống nhất giữa slide và bài tập kiểm chứng.
