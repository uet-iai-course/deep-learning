# Buổi 07: Mạng nơ-ron hồi quy

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- trình bày cấu trúc và nguyên lý hoạt động của một mạng nơ-ron hồi quy (recurrent neural network, RNN) cơ bản;
- giải thích trạng thái ẩn và cách trạng thái này truyền thông tin quá khứ;
- mô tả lan truyền ngược theo thời gian (backpropagation through time, BPTT);
- kiểm tra kích thước tensor, trải mạng theo thời gian và tính một ví dụ RNN vô hướng;
- phân tích nguyên nhân gradient triệt tiêu hoặc bùng nổ qua tích Jacobian;
- phân biệt BPTT toàn phần với BPTT cắt ngắn.

Đề cương gán BPTT mã `LLO3`, trùng với `LLO3` của Buổi 02. Tài liệu giữ nguyên mã này để bảo toàn truy nguyên; đây là lỗi đánh số của đề cương, không phải một chuẩn đầu ra mới.

Kiến thức tiên quyết: quy tắc chuỗi, Jacobian, tích véc-tơ–Jacobian, chuẩn véc-tơ–ma trận, lan truyền ngược, MLP, hàm tanh và phép nhân ma trận theo lô.

Tuyến lõi gồm 100 phút về dữ liệu chuỗi, ô RNN, lan truyền xuôi, BPTT và ổn định gradient. Phần bổ sung 20 phút xét mô hình ngôn ngữ, RNN nhiều tầng và hai chiều. Bài tập 50 phút được tách riêng.

## Ký hiệu và hợp đồng tensor

Tài liệu dùng quy ước mỗi mẫu là một hàng.

| Đại lượng | Kích thước | Nghĩa |
|---|---|---|
| $X$ | $N\times T\times D_x$ | Lô gồm $N$ chuỗi hoặc đoạn, mỗi đoạn có $T$ bước |
| $X_t$ | $N\times D_x$ | Toàn bộ lô tại bước $t$ |
| $A_t,H_t$ | $N\times D_h$ | Tiền kích hoạt và trạng thái ẩn |
| $O_t$ | $N\times D_y$ | Logit hoặc đầu ra tuyến tính |
| $W_x$ | $D_x\times D_h$ | Trọng số đầu vào–trạng thái |
| $W_h$ | $D_h\times D_h$ | Trọng số truy hồi |
| $W_y$ | $D_h\times D_y$ | Trọng số trạng thái–đầu ra |
| $b_h,b_y$ | $D_h,D_y$ | Độ lệch phát theo trục lô |
| $H_0$ | $N\times D_h$ | Trạng thái đầu |

Các công thức xét một lô đã chọn có cùng $T$ và mọi bước đều hợp lệ. Ghép các chuỗi khác độ dài bằng đệm, mặt nạ hoặc chia ngăn nằm ngoài phạm vi bài.

Trong phần BPTT:

- $\bar O_t=\partial\mathcal L/\partial O_t$ là gradient tại đầu ra;
- $\bar H_t=\partial\mathcal L/\partial H_t$ là gradient tại trạng thái;
- $G_t=\partial\mathcal L/\partial A_t$ là gradient tại tiền kích hoạt;
- với ví dụ vô hướng, $\delta_t$ chính là $G_t$.

## Khái niệm trọng tâm

### Cụm 1: Dữ liệu chuỗi và trạng thái

Thứ tự là một phần của dữ liệu chuỗi. Đổi vị trí các từ, khung âm thanh hoặc sự kiện có thể đổi ý nghĩa của toàn mẫu. Một MLP trên cửa sổ có độ dài cố định $\tau$ chỉ nhận $x_{t-\tau+1},\ldots,x_t$, nên bỏ qua lịch sử xa hơn $\tau$ bước.

RNN thay cửa sổ cố định bằng một trạng thái được cập nhật:

$$
h_t=f_\theta(x_t,h_{t-1}).
$$

$h_t$ có kích thước cố định dù số bước đã quan sát tăng. Nó là một tóm tắt do mô hình học, không phải bản sao nguyên văn của toàn bộ quá khứ.

![Trạng thái truyền ngữ cảnh theo chuỗi](img/lec-07/sequence-context.svg)

Với tensor lô, $X_t=X[:,t,:]\in\mathbb R^{N\times D_x}$. Phép chọn $t$ loại trục thời gian nhưng giữ trục lô và đặc trưng.

::: exercise Câu hỏi kiểm tra
Cho $X\in\mathbb R^{32\times20\times64}$. Kích thước của $X_7$ là gì, và trục nào đã được chọn?
:::

::: solution
$X_7\in\mathbb R^{32\times64}$. Phép lấy bước $t=7$ chọn trục thời gian; 32 mẫu và 64 đặc trưng vẫn được giữ.
:::

Trạng thái chỉ có ý nghĩa khi quy tắc cập nhật, kích thước và điều kiện đầu được xác định rõ.

### Cụm 2: Ô RNN, kích thước và tham số dùng chung

Xét ví dụ vô hướng ba bước với $x=(1,0,-1)$, $h_0=0$, $w_x=0{,}5$, $w_h=0{,}8$ và $w_y=1{,}2$. Bước đầu cho

$$
a_1=0{,}5\cdot1+0{,}8\cdot0=0{,}5,
\qquad h_1=\tanh(0{,}5)=0{,}4621.
$$

$h_1$ vừa là kết quả của bước đầu vừa là dữ kiện cho bước tiếp theo. Cùng bộ số sẽ được dùng cho lan truyền xuôi và BPTT.

Một ô RNN cơ bản theo quy ước hàng thực hiện

$$
A_t=X_tW_x+H_{t-1}W_h+b_h,
$$

$$
H_t=\tanh(A_t),\qquad O_t=H_tW_y+b_y.
$$

![Luồng tensor qua một ô RNN](img/lec-07/cell-shapes.svg)

Hai tích $X_tW_x$ và $H_{t-1}W_h$ đều có kích thước $N\times D_h$. Độ lệch $b_h$ được phát thành $N$ hàng. $W_h$ vuông vì trạng thái trước và sau có cùng số chiều $D_h$.

$H_0$ là điều kiện biên. Với các chuỗi độc lập, lựa chọn thường gặp là $H_0=0$. Nếu trạng thái được cung cấp từ bên ngoài, nó phải có cùng kích thước, kiểu dữ liệu và thiết bị với phép tính.

Khi trải quan hệ truy hồi theo thời gian, các ô tính toán khác nhau nhưng dùng chung $W_x$, $W_h$, $W_y$, $b_h$ và $b_y$.

![RNN được trải theo thời gian](img/lec-07/unroll.svg)

::: exercise Câu hỏi kiểm tra
Một RNN có $D_h=8$ được trải thành bốn bước. Có bao nhiêu ma trận $W_h$ độc lập, và kích thước của nó là gì?
:::

::: solution
Chỉ có một ma trận dùng chung ở cả bốn bước; $W_h\in\mathbb R^{8\times8}$.
:::

Mạng đã trải cung cấp đồ thị hữu hạn để tính cả lan truyền xuôi và lan truyền ngược.

### Cụm 3: Dạng ánh xạ và lan truyền xuôi

Vị trí đầu vào và đầu ra quyết định nơi tạo mất mát. Có bốn họ ánh xạ; họ nhiều–sang–nhiều gồm trường hợp căn chỉnh và không căn chỉnh.

![Bốn dạng ánh xạ đầu vào–đầu ra](img/lec-07/architectures.svg)

- Một–sang–một là trường hợp truyền thẳng thông thường.
- Một–sang–nhiều nhận một đầu vào và tạo một chuỗi đầu ra.
- Nhiều–sang–một dùng cả chuỗi để dự đoán một đích, chẳng hạn nhãn cảm xúc.
- Nhiều–sang–nhiều căn chỉnh đặt một đích ở mỗi bước, chẳng hạn nhãn từ loại.
- Nhiều–sang–nhiều không căn chỉnh có trục đầu ra riêng, chẳng hạn dịch máy.

Với nhiều–sang–một,

$$
\mathcal L=\frac1N\sum_{n=1}^{N}\ell\!\left(Y^{(n)},O_T^{(n)}\right).
$$

Với nhiều–sang–nhiều căn chỉnh,

$$
\mathcal L=\frac1{NT}\sum_{n=1}^{N}\sum_{t=1}^{T}
\ell\!\left(Y_t^{(n)},O_t^{(n)}\right).
$$

Nếu $O_t$ là logit phân lớp, entropy chéo phải được tính trực tiếp từ logit theo trục $D_y$ bằng phép log-softmax ổn định số.

Lan truyền xuôi bắt đầu từ $H_0$, rồi tính lần lượt $A_t,H_t,O_t$ theo $t=1,\ldots,T$. Các tham số được dùng lại, còn kích hoạt phải lưu riêng cho từng bước nếu cần BPTT.

::: example Ví dụ vô hướng ba bước

Cho

$$
x=(1,0,-1),\quad h_0=0,\quad w_x=0{,}5,\quad
w_h=0{,}8,\quad w_y=1{,}2,
$$

$$
h_t=\tanh(w_xx_t+w_hh_{t-1}),\qquad
o_3=w_yh_3,\qquad y=0{,}4,
$$

$$
\mathcal L=\frac12(o_3-y)^2.
$$

Kết quả tính bằng giá trị đầy đủ rồi làm tròn bốn chữ số:

| $t$ | $a_t$ | $h_t$ |
|---:|---:|---:|
| 1 | $0{,}5000$ | $0{,}4621$ |
| 2 | $0{,}3697$ | $0{,}3537$ |
| 3 | $-0{,}2170$ | $-0{,}2137$ |

$o_3=-0{,}2564$ và $\mathcal L=0{,}2154$.

Ví dụ đặt hai độ lệch bằng 0 để tập trung vào đường truy hồi.

![Lan truyền xuôi của ví dụ vô hướng](img/lec-07/scalar-forward.svg)
:::

::: exercise Câu hỏi kiểm tra
Phân loại cảm xúc của cả câu và gán nhãn từ loại cho từng từ thuộc hai dạng ánh xạ nào?
:::

::: solution
Phân loại cảm xúc là nhiều–sang–một. Gán nhãn từ loại là nhiều–sang–nhiều căn chỉnh.
:::

::: exercise Câu hỏi kiểm tra
Nếu đổi $x_1$ nhưng giữ $x_2,x_3$, những đại lượng nào ở bước 3 có thể đổi?
:::

::: solution
$h_1,h_2,h_3,o_3$ và mất mát đều có thể đổi vì ảnh hưởng đi theo đường $x_1\to h_1\to h_2\to h_3\to o_3$.
:::

Đường ảnh hưởng xuôi qua các trạng thái cũng là đường mà gradient đi ngược.

### Cụm 4: Lan truyền ngược theo thời gian

BPTT là lan truyền ngược trên mạng đã trải. Một tham số xuất hiện ở nhiều bước tính toán, nên gradient của tham số đó là tổng các đóng góp theo thời gian.

![Một tham số nhận gradient từ nhiều bước](img/lec-07/shared-weights.svg)

Với một mất mát tổng quát, đặt $G_{T+1}=0$. Khi đi từ $t=T$ về $1$,

$$
\bar H_t=\bar O_tW_y^\top+G_{t+1}W_h^\top,
$$

$$
G_t=\bar H_t\odot(1-H_t\odot H_t).
$$

Gradient tham số được cộng dồn:

$$
\frac{\partial\mathcal L}{\partial W_y}
=\sum_t H_t^\top\bar O_t,
\qquad
\frac{\partial\mathcal L}{\partial W_x}
=\sum_t X_t^\top G_t,
$$

$$
\frac{\partial\mathcal L}{\partial W_h}
=\sum_t H_{t-1}^\top G_t.
$$

Hai gradient độ lệch là tổng theo thời gian và theo các hàng của lô:

$$
\frac{\partial\mathcal L}{\partial b_y}
=\sum_t\mathbf 1_N^\top\bar O_t,
\qquad
\frac{\partial\mathcal L}{\partial b_h}
=\sum_t\mathbf 1_N^\top G_t.
$$

Nếu mất mát lấy trung bình theo $N$ hoặc $NT$, hệ số đó đã nằm trong $\bar O_t=\partial\mathcal L/\partial O_t$ và do đó truyền vào $G_t$.

Nếu chỉ bước cuối chịu mất mát thì $\bar O_t=0$ với $t<T$. Các bước sớm vẫn nhận gradient qua hạng $G_{t+1}W_h^\top$.

Với ví dụ vô hướng,

$$
\bar o_3=o_3-y=-0{,}6564,
$$

$$
\delta_3=\bar o_3w_y(1-h_3^2)=-0{,}7517,
$$

$$
\delta_2=\delta_3w_h(1-h_2^2)=-0{,}5261,
\qquad
\delta_1=\delta_2w_h(1-h_1^2)=-0{,}3310.
$$

![Tín hiệu gradient của ví dụ ba bước](img/lec-07/scalar-bptt.svg)

Các gradient tham số là

$$
\frac{\partial\mathcal L}{\partial w_x}
=\sum_{t=1}^{3}\delta_tx_t=0{,}4207,
$$

$$
\frac{\partial\mathcal L}{\partial w_h}
=\sum_{t=1}^{3}\delta_th_{t-1}=-0{,}5090,
\qquad
\frac{\partial\mathcal L}{\partial w_y}=\bar o_3h_3=0{,}1403.
$$

Đạo hàm trực tiếp của $w_h$ tại một bước chỉ xét cạnh $w_hh_{t-1}$. Đạo hàm toàn phần còn gồm việc $w_h$ đã làm đổi các trạng thái trước đó. BPTT tính đạo hàm toàn phần bằng cách cộng mọi đường hợp lệ trên đồ thị.

![Đạo hàm trực tiếp và đạo hàm toàn phần](img/lec-07/direct-total.svg)

::: exercise Câu hỏi kiểm tra
Vì sao $\partial\mathcal L/\partial W_h$ là tổng theo $t$ dù mô hình chỉ có một ma trận $W_h$?
:::

::: solution
Cùng $W_h$ được dùng ở mọi bước trên mạng đã trải. Mỗi lần dùng tạo một đóng góp gradient, và các đóng góp được cộng về cùng tham số.
:::

Việc nhân liên tiếp các toán tử truy hồi quyết định độ lớn của tín hiệu học từ quá khứ xa.

### Cụm 5: Tích Jacobian và phụ thuộc dài hạn

Với một mẫu đơn, đổi công thức hàng sang véc-tơ cột:

$$
h_t^{\mathrm{col}}
=\tanh\!\left(W_h^\top h_{t-1}^{\mathrm{col}}+W_x^\top x_t^{\mathrm{col}}+b_h\right).
$$

Do đó phép cập nhật tạo ánh xạ nhiễu loạn

$$
\Delta h_t
=\operatorname{diag}(1-h_t^2)W_h^\top\Delta h_{t-1}
$$

theo quy ước véc-tơ cột. Gọi toán tử tại bước $t$ là $J_t$, ảnh hưởng từ $h_k$ đến $h_T$ chứa tích

$$
J_TJ_{T-1}\cdots J_{k+1}.
$$

![Tích Jacobian qua nhiều bước](img/lec-07/gradient-product.svg)

Độ lớn của tích phụ thuộc đồng thời vào $W_h$, đạo hàm tanh tại từng trạng thái và hướng của véc-tơ đang truyền. Vì vậy không thể kết luận gradient chỉ từ một phần tử hay chỉ từ chuẩn của $W_h$.

Trong ví dụ vô hướng, đường từ $h_0$ đến $h_3$ có ba hệ số truy hồi:

$$
0{,}6292\cdot0{,}6999\cdot0{,}7635\approx0{,}3362.
$$

Nếu mỗi bước chỉ giữ lại hệ số $0{,}8$, sau 20 bước còn

$$
0{,}8^{20}\approx0{,}0115,
$$

tức khoảng $1{,}15\%$ tín hiệu ban đầu.

Đây là phép minh họa vô hướng với một hệ số cố định, không phải kết luận cho mọi hướng trong một RNN ma trận.

![Tích co và tích giãn qua thời gian](img/lec-07/vanish-explode.svg)

- Gradient triệt tiêu khi các hướng liên quan bị co lặp lại, khiến bước xa nhận tín hiệu học rất nhỏ.
- Gradient bùng nổ khi một số hướng bị giãn lặp lại, khiến cập nhật mất ổn định.
- Hai hiện tượng nói về đạo hàm khi huấn luyện; chúng không có nghĩa trạng thái xuôi luôn bằng 0 hoặc vô hạn.

![Phụ thuộc dài hạn cần đường gradient dài](img/lec-07/long-dependency.svg)

::: exercise Câu hỏi kiểm tra
Nếu mỗi bước nhân độ lớn gradient với $0{,}8$, sau 20 bước còn lại khoảng bao nhiêu phần trăm? Kết quả này gợi ý hiện tượng nào?
:::

::: solution
$0{,}8^{20}\approx0{,}0115$, tức khoảng $1{,}15\%$. Đây là một ví dụ về gradient triệt tiêu.
:::

Chuỗi dài còn tạo áp lực bộ nhớ vì BPTT toàn phần phải giữ kích hoạt của nhiều bước.

### Cụm 6: BPTT toàn phần và BPTT cắt ngắn

BPTT toàn phần giữ đồ thị và truyền gradient qua tối đa $T$ bước. Bộ nhớ kích hoạt chính tăng gần theo $O(TND_h)$.

![Kích hoạt được giữ cho BPTT toàn phần](img/lec-07/bptt-memory.svg)

BPTT cắt ngắn chia chuỗi thành các đoạn dài $K$. Trạng thái cuối đoạn được chuyển sang đoạn sau trong lượt xuôi, nhưng bị tách khỏi đồ thị trước khi lan truyền ngược cho đoạn mới.

![BPTT toàn phần và BPTT cắt ngắn](img/lec-07/bptt-full-truncated.svg)

| Tiêu chí | Toàn phần | Cắt ngắn độ dài $K$ |
|---|---|---|
| Đường gradient | Tối đa $T$ bước | Tối đa $K$ bước mỗi đoạn |
| Bộ nhớ kích hoạt | Gần $O(TND_h)$ | Gần $O(KND_h)$ |
| Gradient | Đúng với đồ thị toàn chuỗi | Xấp xỉ, bỏ đường qua ranh giới |

Cắt ngắn không đổi phép cập nhật trạng thái trong lượt xuôi. Nó thay đồ thị được dùng để lấy đạo hàm, đổi bộ nhớ và thời gian lấy gradient để chấp nhận mất tín hiệu tín dụng xa.

::: exercise Câu hỏi kiểm tra
Với các đoạn dài $K=3$, $h_3$ có ảnh hưởng đến lượt xuôi ở bước 4 không? Gradient từ bước 6 có truyền về bước 2 không?
:::

::: solution
$h_3$ vẫn là đầu vào của bước 4. Gradient từ đoạn chứa bước 6 bị ngắt tại ranh giới, nên không truyền về bước 2.
:::

Giới hạn tín dụng xa của đường trạng thái tạo động cơ cho các kiến trúc có cổng. Cơ chế trạng thái vừa học cũng cho phép tham số hóa các phân phối điều kiện trong mô hình ngôn ngữ.

## Phần bổ sung: Mô hình ngôn ngữ và kiến trúc RNN

### Phân rã xác suất chuỗi

Quy tắc chuỗi cho

$$
p(x_1,\ldots,x_T)
=p(x_1)\prod_{t=2}^{T}p(x_t\mid x_{1:t-1}).
$$

Một mô hình ngôn ngữ RNN dùng $h_{t-1}$ làm biểu diễn nén của tiền tố để tham số hóa phân phối của $x_t$. Với ký hiệu rời rạc $v$,

$$
p_\theta(x_t=v\mid x_{1:t-1})
=\operatorname{softmax}(O_{t-1})_v.
$$

Trạng thái không đồng nhất với tiền tố; nó chỉ là thông tin mà mô hình giữ lại qua các phép cập nhật.

### Căn chỉnh đầu vào và đầu ra

Trong nhiều–sang–nhiều căn chỉnh, mỗi $x_t$ có một $y_t$ cùng vị trí. Trong trường hợp không căn chỉnh, độ dài và vị trí đầu ra có thể khác đầu vào, nên phải dùng một trục đầu ra riêng. Bài này chỉ phân loại hai đồ thị; cơ chế chú ý được dành cho Buổi 10.

### RNN nhiều tầng

Với tầng $\ell$,

$$
H_t^{(0)}=X_t,
$$

$$
H_t^{(\ell)}
=\tanh\!\left(
H_t^{(\ell-1)}W_x^{(\ell)}
+H_{t-1}^{(\ell)}W_h^{(\ell)}
+b_h^{(\ell)}
\right).
$$

Mỗi tầng có trạng thái và tham số riêng. Trong cùng một tầng, tham số vẫn được dùng chung theo thời gian. Độ sâu theo tầng và độ dài theo thời gian là hai trục khác nhau.

### RNN hai chiều

RNN hai chiều tạo một trạng thái từ tiền tố và một trạng thái từ hậu tố, rồi ghép chúng cho đầu ra tại vị trí $t$. Cơ chế này cần biết cả hai phía của chuỗi, nên không phù hợp cho dự đoán trực tuyến khi đầu vào tương lai chưa xuất hiện.

::: exercise Câu hỏi kiểm tra
Một hệ dự đoán ký hiệu tiếp theo tại thời điểm thực có thể dùng trạng thái hai chiều không?
:::

::: solution
Không, nếu các ký hiệu tương lai chưa có. Trạng thái chiều ngược phụ thuộc vào phần tương lai của chuỗi.
:::

RNN nhiều tầng hoặc hai chiều vẫn dùng đường cập nhật truy hồi cơ bản. LSTM và GRU thay đổi đường trạng thái bằng các cơ chế có cổng; đó là nội dung Buổi 08.

![Từ tích Jacobian dài đến kiến trúc có cổng](img/lec-07/bridge-gates.svg)

## Tóm tắt

- RNN cập nhật một trạng thái có kích thước cố định để truyền ngữ cảnh qua thời gian.
- Kích thước tensor phải được khóa trước khi viết phép nhân, độ lệch và mất mát.
- Mạng được trải có nhiều ô tính toán nhưng các bước dùng chung tham số.
- Dạng ánh xạ quyết định mất mát nằm ở $O_T$ hay ở dãy $O_{1:T}$.
- BPTT đi ngược từ $T$ về 1 và cộng mọi đóng góp vào tham số chung.
- Tích Jacobian giải thích vì sao tín hiệu học từ quá khứ xa có thể triệt tiêu hoặc bùng nổ.
- BPTT cắt ngắn giữ luồng trạng thái xuôi nhưng ngắt gradient ở ranh giới đoạn.

Trạng thái truy hồi khắc phục giới hạn cửa sổ cố định về mặt độ dài biểu diễn, nhưng khả năng giữ thông tin xa vẫn phụ thuộc vào việc học và độ ổn định của đường Jacobian.

## Tự kiểm

- Tự tính lại ví dụ vô hướng bằng giá trị chưa làm tròn và đối chiếu ba gradient tham số.
- Với một tensor lô tự chọn, kiểm tra kích thước của mọi tích trong lượt xuôi và BPTT.
- Giải thích bằng một câu vì sao BPTT cắt ngắn vẫn truyền trạng thái qua ranh giới nhưng không truyền gradient qua ranh giới đó.

## Bài tập 50 phút

### Bài 1 — Trải mạng và kiểm tra kích thước (15 phút)

Cho $N=16$, $T=4$, $D_x=5$, $D_h=3$ và $D_y=2$. Vẽ mạng được trải bốn bước; ghi kích thước của $X_t,H_t,O_t,W_x,W_h,W_y$ và $H_0$. Sản phẩm là một sơ đồ có đủ tensor và tham số dùng chung.

### Bài 2 — BPTT bằng tay (20 phút)

Dùng lại ví dụ vô hướng $x=(1,0,-1)$, $h_0=0$, $w_x=0{,}5$, $w_h=0{,}8$, $w_y=1{,}2$, $y=0{,}4$. Tính lần lượt $a_t,h_t,o_3,\mathcal L$, rồi $\bar o_3,\delta_3,\delta_2,\delta_1$ và ba gradient tham số. Sản phẩm là bảng tính có ghi rõ thứ tự xuôi và ngược.

### Bài 3 — Phân tích đường gradient (10 phút)

Xét hai ví dụ vô hướng: mỗi bước nhân độ lớn gradient với $0{,}8$ hoặc với $1{,}2$. Tính $0{,}8^{10}$, $0{,}8^{20}$, $1{,}2^{10}$ và $1{,}2^{20}$; sau đó giải thích hai xu hướng. Sản phẩm là phép tính và một kết luận có điều kiện; không suy rộng sang mọi hướng hoặc mọi chuỗi.

### Bài 4 — Phân loại dạng ánh xạ (5 phút)

Phân loại bốn bài toán: phân loại cảm xúc, gán nhãn từ loại, tạo chú thích ảnh và dịch máy. Với mỗi bài toán, ghi một–sang–nhiều, nhiều–sang–một hoặc nhiều–sang–nhiều; nếu là nhiều–sang–nhiều, chỉ rõ có căn chỉnh theo bước hay không.

## Nguồn

- DOCX đề cương, Buổi 7: tên bài, LLO13, LLO14, mã LLO3, phạm vi và hoạt động.
- `lec14_rnn.pdf`, trang 3–23: dữ liệu chuỗi, ô RNN, trải mạng, lan truyền xuôi, BPTT và vấn đề gradient.
- `lec14_rnn.pdf`, trang 35–40 và 42: các dạng ánh xạ, RNN nhiều tầng, hai chiều và mô hình ngôn ngữ.
- `hocsau_draft.pdf`, trang PDF 199–224: chuỗi, trạng thái ẩn, hợp đồng tensor, mô hình ngôn ngữ, BPTT và BPTT cắt ngắn.
