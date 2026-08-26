# Ghi chú dành cho người soạn Bài 02

## Tuyến giảng

Tuyến lõi đi theo một đường duy nhất:

1. MLP là chuỗi phép tính; huấn luyện cần gradient theo từng tham số.
2. Đồ thị tính toán tách quan hệ phụ thuộc thành các nút và cạnh.
3. Ví dụ vô hướng chạy xuôi trước khi quy tắc chuỗi được thực hiện cục bộ dưới dạng upstream × local.
4. Các cổng cộng, nhân, max và nhiều nhánh khóa dấu, hướng truyền và phép cộng gradient.
5. Gradient tensor có cùng kích thước với tensor; Jacobian chỉ là cầu nối hình thức.
6. Quy ước batch-first và phép suy theo chỉ số dẫn đến ba công thức của tầng afin.
7. Ví dụ MLP 2–2–3 giữ nguyên mọi tensor qua forward, log-softmax, entropy chéo, suy $G_Z$, backward và cập nhật.
8. Kết thúc bằng việc tách chế độ mô hình, ghi gradient, zero-grad và cập nhật.

Nếu chỉ có 100 phút, dừng ở L02-38. Nếu còn 20 phút, đi L02-X01, L02-X02, L02-X04, L02-X05. Không nhảy vào riêng L02-X02 vì phần bão hòa sigmoid cần công thức ở L02-X01; không dùng L02-X04 để mở sang kỹ thuật checkpointing ngoài nguồn.

## Điểm cần nhấn và lỗi dễ mắc

- Gradient luôn ghi rõ theo biến nào. $G_U=\partial J/\partial U$ có cùng kích thước với $U$.
- Trong đồ thị nhiều nhánh, dùng cộng-gán; không ghi đè gradient đã tích lũy.
- Với max hòa và ReLU tại 0, đạo hàm không duy nhất. Bài chọn ReLU tại 0 bằng 0 và tránh max hòa trong ví dụ.
- Khóa quy ước batch-first: $X:B\times d$, trọng số nhân bên phải.
- Bias phát rộng ở forward nên gradient bias cộng theo trục batch.
- Softmax chạy theo trục lớp. Tính entropy chéo bằng log-softmax/log-sum-exp trực tiếp từ logits, không lấy log của xác suất đã làm tròn.
- Suy $G_Z=(P-Y)/B$ bằng quy tắc chuỗi; hệ số $1/B$ đến từ trung bình batch.
- Logits không phải xác suất.
- Tính đủ mọi gradient bằng tham số cũ rồi mới cập nhật. Không cập nhật $W_2$ trước khi tính $G_H$.
- Đặt gradient tham số về 0 trước mỗi batch. Không đồng nhất chế độ mô hình với việc bật/tắt ghi gradient.
- Không mở sang cực tiểu địa phương, momentum, Adam, điều chuẩn hay gradient triệt tiêu qua mạng sâu; để bài 03.

## Đáp án kiểm tra trên deck

### L02-07

$dz/dx=(-2)(3)=-6$.

### L02-13

Max chọn $x=4$. Gradient theo $x,y,z,w$ lần lượt là $1.5,0,4,4$.

### L02-24

Với $B=8,d=5,k=3$: $G_X:8\times5$, $G_W:5\times3$, $G_b:3$.

### L02-32

Tổng mỗi hàng $G_Z$ bằng 0 vì tổng hàng $P$ và $Y$ đều bằng 1.

### L02-38

1. Softmax chạy theo trục lớp trong từng hàng.
2. $G_b$ rút gọn trục batch.
3. Đặt gradient tham số về 0 trước batch mới.
4. Không cập nhật $W_2$ trước khi tính $G_H$; mọi gradient phải dùng cùng bộ tham số cũ.

## Bài tập 50 phút

### Hoạt động 1: dựng đồ thị, 10 phút

Đề: Với $u=ab$, $v=u+c$, $J=v^2$, hãy vẽ DAG, ghi thứ tự lan truyền xuôi và tô-pô ngược.

Cách tổ chức: 4 phút cá nhân, 3 phút so cặp, 3 phút chữa.

Đáp án: $a,b\to u$; $u,c\to v$; $v\to J$. Xuôi: $u,v,J$. Ngược: $J,v,u$, rồi các lá $a,b,c$.

### Hoạt động 2: lan truyền ngược bằng tay, 15 phút

Đề: Dùng $a=2,b=-3,c=1$ cho đồ thị trên. Tính $J$ và gradient theo $a,b,c$.

Đáp án: $u=-6$, $v=-5$, $J=25$. $\bar v=2v=-10$; $\bar u=-10$; $\bar c=-10$; $\bar a=\bar u b=30$; $\bar b=\bar u a=-20$.

### Hoạt động 3: ReLU và tầng afin, 15 phút

Đề: $X:4\times3$, $W:3\times2$, $b:2$, $Z=XW+b$, $H=\operatorname{ReLU}(Z)$ và $G_H:4\times2$. Ghi công thức và kích thước $G_Z,G_X,G_W,G_b$.

Đáp án:

- $G_Z=G_H\odot\mathbb1[Z>0]:4\times2$;
- $G_X=G_ZW^\top:4\times3$;
- $G_W=X^\top G_Z:3\times2$;
- $G_b=\sum_iG_{Z,i:}:2$.

### Hoạt động 4: tìm và sửa lỗi, 10 phút

Cho bốn phát biểu:

1. Softmax của $Z:B\times k$ chuẩn hóa theo trục batch.
2. Với mất mát trung bình, $G_Z=P-Y$.
3. $G_b=G_Z$ vì bias phát rộng.
4. Có thể cập nhật $W_2$ rồi dùng $W_2$ mới để tính $G_H$.

Đáp án sửa:

1. Chuẩn hóa theo trục lớp trong từng hàng.
2. $G_Z=(P-Y)/B$.
3. $G_b=\sum_iG_{Z,i:}$.
4. Tính toàn bộ gradient bằng bộ tham số cũ, rồi cập nhật.

## Nguồn và trạng thái kiểm chứng

- Nguồn chính: `lec06_backprop.pdf`, tr. 3–16, 18–35; `lec07_backprop_part2.pdf`, tr. 8–31.
- Nguồn phụ: `lec05_multilayer.pdf`, tr. 28–34; `lec04_multiclass.pdf`, tr. 12–19.
- Nguồn kiểm chứng: `hocsau_draft.pdf`, PDF tr. 31–32, 68–73, 90–96.
- Ví dụ vô hướng và MLP đã tính lại; chi tiết và sai khác nằm trong `review-log.md`.
- Không có code demo, raster hoặc phụ thuộc mạng cốt lõi.
- Đã hoàn tất kiểm định storyboard, bốn phản biện độc lập và vòng chỉnh sửa. Cần điều phối viên chạy kiểm định hiển thị cuối trước khi cập nhật chỉ mục.
