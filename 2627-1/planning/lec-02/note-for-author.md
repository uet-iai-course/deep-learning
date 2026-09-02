# Ghi chú dành cho người soạn Bài 02

## Tuyến giảng

Tuyến lõi đi theo một đường duy nhất:

1. MLP là chuỗi phép tính; huấn luyện cần gradient theo từng tham số.
2. Đồ thị tính toán tách quan hệ phụ thuộc thành các nút và cạnh.
3. Ví dụ vô hướng chạy xuôi trước khi quy tắc chuỗi được thực hiện cục bộ dưới dạng đạo hàm thượng nguồn × đạo hàm cục bộ.
4. Các cổng cộng, nhân, max và nhiều nhánh khóa dấu, hướng truyền và phép cộng gradient.
5. Gradient tensor có cùng kích thước với tensor; Jacobian chỉ là cầu nối hình thức.
6. Quy ước lô theo hàng và phép suy theo chỉ số dẫn đến ba công thức của tầng afin.
7. Ví dụ MLP 2–2–3 giữ nguyên mọi tensor qua lan truyền xuôi, log-softmax, entropy chéo, suy $G_Z$, lan truyền ngược và cập nhật.
8. Kết thúc bằng việc tách chế độ mô hình, ghi gradient, đặt gradient về 0 và cập nhật.
9. Trang kết L02-39 thu hồi chuỗi $X\to H\to Z\to J\to$ gradient $\to$ cập nhật cùng ba tiêu chí kiểm được, rồi nối sang Bài 03.

Nếu chỉ có 100 phút, đi L02-00–38 rồi bỏ qua mạch mở rộng để sang L02-39. Nếu còn 20 phút, đi L02-X01, L02-X02, L02-X04, L02-X05 rồi L02-39; cả hai tuyến đều kết thúc ở L02-39. Không nhảy vào riêng L02-X02 vì phần bão hòa sigmoid cần công thức ở L02-X01; không dùng L02-X04 để mở sang kỹ thuật lưu điểm kiểm tra ngoài nguồn.

## Điểm cần nhấn và lỗi dễ mắc

- Gradient luôn ghi rõ theo biến nào. $G_U=\partial J/\partial U$ có cùng kích thước với $U$.
- Trong đồ thị nhiều nhánh, dùng cộng-gán; không ghi đè gradient đã tích lũy.
- Với max hòa và ReLU tại 0, đạo hàm không duy nhất. Bài chọn ReLU tại 0 bằng 0 và tránh max hòa trong ví dụ.
- Khóa quy ước lô theo hàng: $X:B\times d$, trọng số nhân bên phải.
- Độ lệch phát rộng ở lượt xuôi nên gradient độ lệch cộng theo trục lô.
- Softmax chạy theo trục lớp. Tính entropy chéo bằng log-softmax/log-sum-exp trực tiếp từ điểm số, không lấy log của xác suất đã làm tròn.
- Suy $G_Z=(P-Y)/B$ bằng quy tắc chuỗi; hệ số $1/B$ đến từ trung bình lô.
- Logits không phải xác suất.
- Tính đủ mọi gradient bằng tham số cũ rồi mới cập nhật. Không cập nhật $W_2$ trước khi tính $G_H$.
- Đặt gradient tham số về 0 trước mỗi lô. Không đồng nhất chế độ mô hình với việc bật/tắt ghi gradient.
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
2. $G_b$ rút gọn trục lô.
3. Đặt gradient tham số về 0 trước lô mới.
4. Không cập nhật $W_2$ trước khi tính $G_H$; mọi gradient phải dùng cùng bộ tham số cũ.

### L02-39

Ba tiêu chí kiểm được của một bước huấn luyện:

1. Tính đúng đại lượng và kích thước: mỗi gradient cùng kích thước với tensor của nó.
2. Dùng đúng giá trị đã lưu và tham số cũ: mặt nạ ReLU từ $A$; $G_{W_1}$ từ $X$; $G_H$ từ $W_2$ cũ.
3. Chỉ cập nhật sau khi đủ gradient; không cập nhật giữa chừng lượt ngược.

Câu nối: Bài 03 dùng gradient này để bàn bộ tối ưu và tốc độ học; Bài 02 dừng ở một bước cập nhật.

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

1. Softmax của $Z:B\times k$ chuẩn hóa theo trục lô.
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
- Không có mã trình diễn, ảnh raster hoặc phụ thuộc mạng cốt lõi.
- Deck đã hoàn tất kiểm định storyboard và năm phản biện độc lập. Lecture note đã qua năm phản biện riêng, hai tái kiểm định toán và mạch viết, cùng lượt `$no-ai-slop` và `$quill`; chỉ cập nhật chỉ mục sau khi QA Markdown/viewer đạt.
- Sau vòng sửa mới: tuyến lõi 40 trang gồm L02-39; hai tuyến điều hướng đều kết thúc ở L02-39; L02-31 là 5 phút và L02-33 là 4 phút để giữ đúng 100+20 phút.

## Quyết định riêng cho lecture note

- Khối lời giải là nội dung tự học và phải gập mặc định trong viewer; không chuyển đáp án chi tiết lên mặt slide.
- Ví dụ kiểm tra dùng đúng $f=2(xy+\max(z,w))$ tại $x=4,y=-6,z=-1,w=2.5$; đáp án theo thứ tự $x,y,z,w$ là $-12,8,0,2$.
- Sai số tương đối của phép kiểm gradient dùng mẫu số $\max(\tau,|g_j^{\mathrm{num}}|+|g_j|)$. Với số đầy đủ đã lưu ở nhật ký, hiệu tuyệt đối là khoảng $5.68\times10^{-11}$ và sai số tương đối khoảng $7.24\times10^{-10}$.
- Ghi chú chỉ dùng bốn SVG hiện có: đồ thị cổng vô hướng, cộng gradient nhiều nhánh, tầng afin lượt ngược và MLP 2–2–3. Không có ngoại lệ raster.
- Mọi mã T02-N, trạng thái worker, chỉ dẫn cắt tuyến và quyết định biên tập chỉ thuộc planning; không đưa vào tài liệu công khai hoặc ghi chú diễn giả.
