# Buổi 04: Mạng nơ-ron tích chập

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- Giải thích hai giả định của mạng nơ-ron tích chập (CNN): tính cục bộ và chia sẻ tham số.
- Phân biệt tầng kết nối đầy đủ với kết nối cục bộ và đếm tham số của từng loại.
- Phát biểu tính tương đương dịch chuyển có điều kiện của bản đồ đặc trưng.
- Tính đầu ra của tương quan chéo một kênh từ đầu vào, nhân và độ lệch cho trước.
- Chỉ rõ lý do các thư viện học sâu thường dùng tương quan chéo thay vì tích chập toán học.

Kiến thức tiên quyết: mô hình perceptron nhiều lớp (MLP), lan truyền ngược, tối ưu hóa cơ bản, ký hiệu tensor theo thứ tự trục và chiều lô.

## Ký hiệu và quy ước

- Tensor đầu vào $X\in\mathbb R^{N\times C_{in}\times H_{in}\times W_{in}}$ theo NCHW: $N$ mẫu, $C_{in}$ kênh, $H_{in}$ chiều cao, $W_{in}$ chiều rộng.
- Nhân $W\in\mathbb R^{C_{out}\times C_{in}\times K_h\times K_w}$ theo OIHW; độ lệch $b\in\mathbb R^{C_{out}}$. Ở cụm một kênh, $K$ được dùng như nhân $K_h\times K_w$; khi tổng quát, $K$ nối với lát $W_{o,c,:,:}$.
- $\widetilde X$ là tensor sau khi đệm 0; mọi chỉ số trong công thức tổng quát phải hợp lệ trên $\widetilde X$.
- Đệm $P_t,P_b,P_l,P_r\in\mathbb Z_{\ge0}$; bước trượt $S_h,S_w\in\mathbb Z_{>0}$.
- Đầu ra $Y\in\mathbb R^{N\times C_{out}\times H_{out}\times W_{out}}$.
- MAC là một phép nhân–cộng (multiply–accumulate); không đồng nhất MAC với FLOPs.

## Khái niệm trọng tâm

### Cụm 1: Từ MLP đến hai giả định của CNN

MLP nhận đầu vào ảnh bằng cách làm phẳng thành một véc-tơ. Làm phẳng giữ nguyên giá trị điểm ảnh nhưng không mã hóa hay khai thác tường minh quan hệ cục bộ giữa các vị trí. Hai quan sát dẫn tới CNN:

- **Tính cục bộ**: một đặc trưng (cạnh, góc) thường được quyết định bởi một vùng nhỏ kề nhau, không phải toàn ảnh.
- **Chia sẻ tham số**: cùng một đặc trưng xuất hiện ở nhiều vị trí, nên một nhân dùng chung cho mọi vị trí là hợp lý.

Tầng kết nối đầy đủ cho mỗi đầu ra dùng trọng số riêng cho mọi vị trí. Kết nối cục bộ cho mỗi đầu ra chỉ nhìn một cửa sổ $K_h\times K_w$. Tầng tích chập áp dụng kết nối cục bộ và dùng chung một nhân trên toàn bản đồ đặc trưng.

**Ví dụ đếm tham số.** Với ảnh một kênh $32\times32$ và tầng ẩn $100$, tầng đầy đủ cần $100(32\cdot32+1)=102\,500$ tham số. Với $C_{out}$ nhân $5\times5$, tầng tích chập cần $C_{out}(5\cdot5+1)$ tham số. Tổng quát hơn, số tham số là $C_{out}(C_{in}K_hK_w+1)$: nó phụ thuộc số kênh và kích thước nhân, không phụ thuộc kích thước không gian của ảnh.

Một nhân dùng chung tạo cùng một kiểu phản hồi ở mọi vị trí; kết quả vẫn có cấu trúc không gian để các tầng sau tiếp tục xử lý.

Tầng tích chập có tính **tương đương dịch chuyển có điều kiện**: dịch đặc trưng trong cửa sổ kéo theo dịch đặc trưng trong bản đồ đầu ra. Đây không phải bất biến tuyệt đối; biên, vùng đệm và bước trượt có thể làm thay đổi quan hệ này gần biên ảnh.

::: exercise Câu hỏi kiểm tra
Ảnh $W_{in}=32$, đầu vào một kênh. Tầng đầy đủ có $512$ đầu ra; tích chập có $C_{out}=16$ nhân $3\times3$ kèm độ lệch. Chênh lệch số tham số là bao nhiêu?
:::

::: hint
Đếm riêng tham số của tầng đầy đủ rồi của tích chập; chú ý độ lệch một chiều.
:::

::: solution
Tầng đầy đủ: $512(32\cdot32+1)=525\,312$. Tích chập: $16(3\cdot3+1)=160$. Chênh lệch $525\,152$.
:::

![So sánh tầng đầy đủ và tầng tích chập](img/lec-04/mlp-vs-conv.svg)

![Kết nối cục bộ và chia sẻ tham số](img/lec-04/locality-sharing.svg)

![Một bộ tham số được dùng tại nhiều vị trí](img/lec-04/parameter-sharing.svg)

![Tương đương dịch chuyển có điều kiện](img/lec-04/equivariance.svg)

### Cụm 2: Tương quan chéo một kênh

Trước khi đi vào nhiều kênh, xét phép toán của một cửa sổ nhân trên một kênh.

Thư viện học sâu thường tính **tương quan chéo**: nhân không bị lật. Tích chập toán học lật nhân theo hai trục rồi mới nhân. Với tham số được học, việc lật chỉ đổi cách đánh chỉ số của nhân.

**Ví dụ tính được.** Cho $X=[[0,1,2],[3,4,5],[6,7,8]]$, $K=[[0,1],[2,3]]$, $b=0$, không đệm, bước trượt $1$.

::: example
Ô trên trái: $Y_{00}=0\cdot0+1\cdot1+3\cdot2+4\cdot3=0+1+6+12=19$. Trượt cửa sổ $2\times2$ khắp $X$ thu được $Y=[[19,25],[37,43]]$.
:::

Với một kênh, không đệm và bước trượt 1:

$$Y_{i,j}=b+\sum_{u=0}^{K_h-1}\sum_{v=0}^{K_w-1}X_{i+u,j+v}\,K_{u,v}.$$

Mỗi giá trị đầu ra là tổng có trọng số của các điểm ảnh trong cửa sổ; nhân hoạt động như bộ lọc cục bộ dùng chung.

::: exercise Câu hỏi kiểm tra
Với cùng $X$ trên, dùng $K=[[1,0],[-1,1]]$, $b=0$. Tính $Y$.
:::

::: hint
Tính $Y_{00}=0\cdot1+1\cdot0+3\cdot(-1)+4\cdot1$, rồi trượt như ví dụ.
:::

::: solution
$Y=[[1,2],[4,5]]$.
:::

![Cửa sổ tương quan chéo trượt trên đầu vào](img/lec-04/cross-correlation-slide.svg)

### Cụm 3: Hình học đầu ra

Phép tính một cửa sổ chưa cho biết toàn tầng tạo bao nhiêu ô đầu ra. Trước khi đếm, cần cố định thứ tự trục. Tensor đặc trưng theo NCHW: số mẫu $N$, số kênh $C$, chiều cao $H$, chiều rộng $W$. Công thức xử lý chiều cao và chiều rộng độc lập:

$$
H_{out}=\left\lfloor\frac{H_{in}+P_t+P_b-K_h}{S_h}\right\rfloor+1,
$$

$$
W_{out}=\left\lfloor\frac{W_{in}+P_l+P_r-K_w}{S_w}\right\rfloor+1.
$$

Phần dư bị bỏ; phép tính không tạo cửa sổ một phần ở biên cuối. Ít nhất một cửa sổ tồn tại khi

$$
H_{in}+P_t+P_b\ge K_h,\qquad W_{in}+P_l+P_r\ge K_w.
$$

::: example Ví dụ tính được
Cho $X:2\times3\times6\times7$, $C_{out}=4$, nhân $3\times3$, đệm 1 ở bốn phía và bước trượt 2 ở hai chiều. Khi đó

$$
H_{out}=\left\lfloor\frac{6+1+1-3}{2}\right\rfloor+1=3,
\qquad
W_{out}=\left\lfloor\frac{7+1+1-3}{2}\right\rfloor+1=4.
$$

Vì $N$ giữ nguyên và số kênh ra bằng $C_{out}$, ta có $Y:2\times4\times3\times4$.
:::

::: derivation Điều kiện giữ kích thước khi bước trượt 1
Đặt $S_h=S_w=1$. Điều kiện $H_{out}=H_{in}$ cho

$$
H_{in}+P_t+P_b-K_h+1=H_{in},
$$

suy ra $P_t+P_b=K_h-1$. Tương tự, $P_l+P_r=K_w-1$. Khi nhân có kích thước lẻ, tổng đệm là số chẵn nên có thể chia đều cho hai phía. Nhân $3\times3$ cần đệm 1 ở mỗi phía.
:::

![Quy ước trục NCHW](img/lec-04/axis-convention.svg)

![Đệm và bước trượt](img/lec-04/padding-stride.svg)

::: exercise Câu hỏi kiểm tra
Cho $X:1\times1\times5\times5$, nhân $3\times3$, đệm 1 ở bốn phía. Kích thước đầu ra là bao nhiêu khi bước trượt bằng 1 và khi bước trượt bằng 2?
:::

::: solution
Với bước trượt 1, đầu ra giữ kích thước $5\times5$. Với bước trượt 2, $H_{out}=W_{out}=\lfloor(5+1+1-3)/2\rfloor+1=3$.
:::

### Cụm 4: Nhiều kênh, tham số và chi phí

Một kênh ra quét theo không gian và gom thông tin qua trục kênh vào. Tại mỗi vị trí, ta dùng một lát nhân cho từng kênh vào, cộng các đóng góp rồi thêm một độ lệch. Với tensor đã đệm $\widetilde X$, công thức tổng quát là

$$
Y_{n,o,i,j}=b_o+
\sum_{c=0}^{C_{in}-1}
\sum_{u=0}^{K_h-1}
\sum_{v=0}^{K_w-1}
W_{o,c,u,v}\,\widetilde X_{n,c,iS_h+u,jS_w+v}.
$$

Trong đó $0\le i<H_{out}$ và $0\le j<W_{out}$.

Mỗi kênh ra $o$ có một bộ lọc $W_{o,:,:,:}$ gồm một lát $W_{o,c,:,:}$ cho từng kênh vào $c$.

::: example Ví dụ hai kênh
Cho $X:1\times2\times3\times3$, $C_{out}=1$, nhân $2\times2$, không đệm, bước trượt 1 và $b_0=0$, với

$$
X_{0,0,:,:}=\begin{bmatrix}1&2&3\\4&5&6\\7&8&9\end{bmatrix},
\quad
W_{0,0,:,:}=\begin{bmatrix}1&2\\3&4\end{bmatrix},
$$

$$
X_{0,1,:,:}=\begin{bmatrix}0&1&2\\3&4&5\\6&7&8\end{bmatrix},
\quad
W_{0,1,:,:}=\begin{bmatrix}0&1\\2&3\end{bmatrix}.
$$

Ở ô trên trái, hai kênh đóng góp lần lượt 37 và 19, nên $Y_{0,0,0,0}=56$. Trượt hai cửa sổ đồng bộ cho

$$
Y_{0,0,:,:}=\begin{bmatrix}56&72\\104&120\end{bmatrix}.
$$

Mỗi ô cộng $C_{in}K_hK_w=2\cdot2\cdot2=8$ tích.
:::

Số tham số khi có độ lệch:

$$
C_{out}(C_{in}K_hK_w+1).
$$

Số MAC cho một mẫu và cho cả lô:

$$
\operatorname{MAC}_{sample}=H_{out}W_{out}C_{out}C_{in}K_hK_w,
\qquad
\operatorname{MAC}_{batch}=N\operatorname{MAC}_{sample}.
$$

Với ví dụ hình học ở Cụm 3, tầng có $4(3\cdot3\cdot3+1)=112$ tham số, thực hiện $3\cdot4\cdot4\cdot3\cdot3\cdot3=1296$ MAC cho mỗi mẫu và 2592 MAC cho lô hai mẫu. Độ lệch và hàm kích hoạt không được tính trong biểu thức MAC này.

![Tổng qua nhiều kênh vào](img/lec-04/multichannel-sum.svg)

![Nhiều bộ lọc tạo nhiều kênh ra](img/lec-04/multioutput-filters.svg)

::: exercise Câu hỏi kiểm tra
Cho $X:1\times3\times5\times5$, $C_{out}=8$, nhân $3\times3$, không đệm, bước trượt 1 và có độ lệch. Tính số tham số và MAC cho một mẫu.
:::

::: solution
$H_{out}=W_{out}=3$. Số tham số là $8(3\cdot3\cdot3+1)=224$; số MAC là $3\cdot3\cdot8\cdot3\cdot3\cdot3=1944$.
:::

### Cụm 5: Phép gộp

Sau tầng có tham số, ta xét một phép tóm tắt cửa sổ không có tham số học được. Phép gộp chạy độc lập trên từng kênh: không cộng chéo kênh như tầng tích chập.

- Gộp cực đại lấy phần tử lớn nhất trong cửa sổ.
- Gộp trung bình lấy trung bình số học của các phần tử trong cửa sổ.

::: example Ví dụ tính được
Cho

$$
X=\begin{bmatrix}
1&1&2&4\\
5&6&7&8\\
3&2&1&0\\
1&2&3&4
\end{bmatrix},
$$

cửa sổ $2\times2$, bước trượt 2. Kết quả là

$$
\operatorname{MaxPool}(X)=\begin{bmatrix}6&8\\3&4\end{bmatrix},
\qquad
\operatorname{AvgPool}(X)=\begin{bmatrix}3.25&5.25\\2&2\end{bmatrix}.
$$

Chẳng hạn, cửa sổ dưới trái chứa $3,2,1,2$, nên cực đại là 3 và trung bình là 2.
:::

Phép gộp thường giảm độ phân giải khi cửa sổ và bước trượt làm số vị trí đầu ra ít đi. Nó có thể giảm nhạy với một số dịch chuyển nhỏ nhưng không tạo bất biến tuyệt đối: dịch qua ranh giới cửa sổ vẫn có thể đổi đầu ra mạnh.

![Cửa sổ gộp](img/lec-04/pooling-window.svg)

::: exercise Câu hỏi kiểm tra
Với ma trận trên và cùng cửa sổ $2\times2$, nếu bước trượt đổi thành 1 thì đầu ra có kích thước nào? Số kênh và số tham số thay đổi ra sao?
:::

::: solution
Đầu ra có kích thước $3\times3$. Số kênh được giữ nguyên và phép gộp không có tham số học được.
:::

### Cụm 6: Trường tiếp nhận

Phép gộp và bước trượt làm một đơn vị sâu phụ thuộc vào vùng đầu vào lớn dần. Trường tiếp nhận của một đơn vị là vùng trên đầu vào, hoặc trên tầng được chọn làm tham chiếu, có thể ảnh hưởng đến đơn vị đó. Gọi $r_l$ là kích thước vùng và $j_l$ là khoảng cách trên cùng tầng tham chiếu giữa hai đơn vị kề nhau ở tầng $l$. Khi $r_0=j_0=1$:

$$
r_l=r_{l-1}+(K_l-1)j_{l-1},
\qquad
j_l=j_{l-1}S_l.
$$

Nhân kích thước $K_l$ phủ $K_l$ vị trí cách nhau $j_{l-1}$ trên tầng tham chiếu, nên vùng được nới thêm $(K_l-1)j_{l-1}$.

::: example Ví dụ tính được
Ba tầng dùng nhân $3\times3$ và bước trượt 1. Khoảng nhảy luôn bằng 1, còn trường tiếp nhận tăng

$$
r_1=3,\qquad r_2=5,\qquad r_3=7.
$$

Theo cả hai chiều, một đơn vị ở tầng ba có trường tiếp nhận lý thuyết $7\times7$ trên đầu vào.
:::

![Truy hồi trường tiếp nhận](img/lec-04/receptive-field-recurrence.svg)

![Trường tiếp nhận khi bước trượt 1](img/lec-04/receptive-field-stride1.svg)

::: exercise Câu hỏi kiểm tra
Cho ba tầng với $(K,S)=(3,1),(3,2),(3,1)$. Tính $(r_l,j_l)$ sau mỗi tầng.
:::

::: hint
Ở mỗi tầng, dùng $j_{l-1}$ trong công thức của $r_l$, sau đó cập nhật $j_l$.
:::

::: solution
Các cặp lần lượt là $(3,1)$, $(5,2)$ và $(9,2)$.
:::

### Cụm 7: Từ tầng tích chập đến mạng hoàn chỉnh

Kích thước, chi phí và trường tiếp nhận cho phép kiểm tra từng tầng trước khi ghép mạng. Thân mạng nối nhiều khối tích chập và kích hoạt để tạo tensor đặc trưng. Đầu dự đoán chuyển đặc trưng cuối thành logit, tức điểm số chưa chuẩn hóa cho từng lớp. Hàm kích hoạt là thành phần thiết yếu: chồng nhiều phép tuyến tính mà không có kích hoạt vẫn chỉ cho một phép tuyến tính.

![Thân mạng và đầu dự đoán](img/lec-04/cnn-backbone-head.svg)

#### Phần tự chọn

- **Nhân phát hiện cạnh:** một nhân sai phân nhỏ phản hồi mạnh tại nơi cường độ thay đổi theo hướng của nhân. Đây là minh họa bằng nhân cố định, không phải kết luận rằng mọi nhân học được đều phát hiện cạnh.
- **Tích chập $1\times1$:** trộn các kênh tại cùng vị trí; với bước trượt 1 và không đệm, phép toán đổi $C_{in}$ thành $C_{out}$ mà giữ nguyên kích thước không gian.
- **Gradient qua gộp cực đại:** khi cực đại là duy nhất, toàn bộ gradient thượng nguồn đi về vị trí đạt cực đại; các vị trí khác nhận 0. Trường hợp hòa phụ thuộc quy ước của toán tử.
- **Dấu vết LeNet:** tích chập đầu đệm 2 giữ $28\times28$, phép gộp đưa về $14\times14$, tích chập thứ hai không đệm đưa về $10\times10$, phép gộp tiếp theo đưa về $5\times5$. Với 16 kênh, làm phẳng cho $16\cdot5\cdot5=400$ đặc trưng.
- **Huấn luyện:** ảnh đi qua thân mạng và đầu dự đoán để tạo logit; mất mát so sánh logit với nhãn; lan truyền ngược tính gradient; bộ tối ưu cập nhật nhân, độ lệch và tham số đầu dự đoán. Phép gộp không có tham số nhưng vẫn truyền gradient.

![Dấu vết kích thước LeNet](img/lec-04/lenet-shape-trace.svg)

::: exercise Câu hỏi kiểm tra
Tích chập $1\times1$ và phép gộp cực đại ảnh hưởng đến số kênh và kích thước không gian theo hai cách nào?
:::

::: solution
Tích chập $1\times1$ có thể đổi số kênh nhưng giữ kích thước không gian khi bước trượt 1. Phép gộp giữ số kênh nhưng thường giảm kích thước không gian.
:::

## Từ công thức đến triển khai

Khi dùng API tích chập, cần kiểm tra sáu điểm:

1. Xác nhận đầu vào theo NCHW và trọng số theo OIHW, hoặc chuyển trục nếu thư viện dùng quy ước khác.
2. Xác nhận thư viện tính tương quan chéo, tức không lật nhân.
3. Đọc đúng thứ tự vùng đệm và bước trượt theo hai chiều.
4. Tính trước $H_{out},W_{out}$ rồi đối chiếu với kích thước API trả về.
5. Xác nhận tầng có độ lệch hay không trước khi đếm tham số.
6. Đặt đúng chế độ huấn luyện hoặc suy luận nếu thân mạng chứa tầng phụ thuộc chế độ.

Mạch triển khai của một mô hình tích chập vẫn tách rõ: lan truyền xuôi tạo logit, dựng hàm mất mát, lan truyền ngược và bước cập nhật.

## Tự kiểm tra

Làm phẳng ảnh giữ các giá trị nhưng không khai thác tường minh quan hệ cục bộ. CNN xử lý giới hạn đó bằng kết nối cục bộ và chia sẻ tham số. Bốn phép kiểm dưới đây giúp đối chiếu thiết kế ở từng tầng: thứ tự trục; kích thước đầu ra; số tham số và MAC; trường tiếp nhận.

::: exercise Câu hỏi về thứ tự trục
Cho $X:2\times3\times7\times7$ theo NCHW và $W:5\times3\times3\times3$ theo OIHW. Xác định $N,C_{in},C_{out},K_h,K_w$ và kích thước hai trục đầu của $Y$.
:::

::: solution
$N=2$, $C_{in}=3$, $C_{out}=5$, $K_h=K_w=3$. Hai trục đầu của $Y$ là $2\times5$.
:::

::: exercise Câu hỏi tổng hợp 1
Cho $X:2\times3\times7\times7$, $C_{out}=5$, nhân $3\times3$, đệm 1 ở bốn phía và bước trượt 2. Tính kích thước đầu ra, số tham số và MAC cho một mẫu.
:::

::: hint
Tính kích thước không gian trước, sau đó dùng $C_{in}=3$ và $C_{out}=5$.
:::

::: solution
$H_{out}=W_{out}=\lfloor(7+1+1-3)/2\rfloor+1=4$. Đầu ra có kích thước $2\times5\times4\times4$; tầng có $5(3\cdot3\cdot3+1)=140$ tham số và thực hiện $4\cdot4\cdot5\cdot3\cdot3\cdot3=2160$ MAC cho mỗi mẫu.
:::

::: exercise Câu hỏi tổng hợp 2
Hai tầng có $(K,S)=(3,2)$ rồi $(3,1)$. Từ $(r_0,j_0)=(1,1)$, tính trường tiếp nhận và khoảng nhảy sau từng tầng.
:::

::: solution
Sau tầng một, $(r_1,j_1)=(3,2)$. Sau tầng hai, $(r_2,j_2)=(3+2\cdot2,2)=(7,2)$.
:::

## Tài liệu tham khảo

- Đề cương học phần, mục III.2 → Buổi 4.
- `source-materials/slides/lec08_cnn.pdf`, PDF 3–29, 38–42, 44–50 và 52–53.
- `source-materials/textbooks/hocsau_draft.pdf`, PDF 110–135, mục 4.1–4.7.
