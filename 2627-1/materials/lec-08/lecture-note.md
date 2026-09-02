# Buổi 08: Các kiến trúc mạng nơ-ron truy hồi hiện đại

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- trình bày cấu trúc và cơ chế hoạt động của bộ nhớ ngắn dài hạn (long short-term memory, LSTM) và đơn vị truy hồi có cổng (gated recurrent unit, GRU);
- phân tích ưu điểm và giới hạn của LSTM, GRU so với RNN cơ bản khi xử lý phụ thuộc dài hạn;
- phân biệt trạng thái ô với trạng thái ẩn, đồng thời kiểm tra kích thước tensor trong một bước tính;
- mô tả mạng truy hồi sâu, mạng hai chiều và bộ mã hóa–giải mã cho dịch máy;
- phân biệt mặt nạ giữ trạng thái nguồn với mặt nạ chọn token đích trong hàm mất mát.

Kiến thức tiên quyết: RNN cơ bản, lan truyền ngược theo thời gian (BPTT), tích Jacobian, sigmoid, tanh, tích Hadamard, phép nhân ma trận theo lô và phát tự động.

Tuyến lõi gồm 100 phút về LSTM, GRU, mạng sâu, mạng hai chiều và bộ mã hóa–giải mã. Phần mở rộng 20 phút đối chiếu biểu diễn, số tham số, sinh tự hồi quy và lựa chọn kiến trúc. Bài tập 50 phút được tách riêng.

## Ký hiệu và hợp đồng tensor

Mỗi mẫu là một hàng. Với lô $N$ chuỗi nguồn được đệm đến $T$ bước, chuỗi đích được đệm đến $T'$ bước và phép nhúng có chiều $D_e$:

| Đại lượng | Kích thước | Nghĩa |
|---|---|---|
| $X$ | $N\times T\times D_x$ | Đầu vào theo lô và thời gian |
| $X_t$ | $N\times D_x$ | Lát cắt đầu vào tại bước $t$ |
| $H_t,C_t$ | $N\times D_h$ | Trạng thái ẩn và trạng thái ô |
| $L_n$ | vô hướng nguyên | Độ dài thật của mẫu $n$, $L_n\le T$ |
| $I_t,F_t,O_t,G_t$ | $N\times D_h$ | Cổng vào, quên, ra và ứng viên của LSTM |
| $R_t,Z_t,\widetilde H_t$ | $N\times D_h$ | Hai cổng và ứng viên của GRU |
| $E(y_{t'-1})$ | $N\times D_e$ | Nhúng token đích trước bước giải mã $t'$ |
| $M^{src}_{n,t}$ | vô hướng trong $\{0,1\}$ | Bước nguồn hợp lệ hay vị trí đệm |
| $M^{tgt}_{n,t'}$ | vô hướng trong $\{0,1\}$ | Token đích có tham gia mất mát hay không |

Nếu không có trạng thái được cung cấp, LSTM dùng $H_0=C_0=0\in\mathbb R^{N\times D_h}$. Mọi tensor trong cùng phép tính phải có kiểu dữ liệu và thiết bị tương thích.

Với trạng thái tổng quát $S_t$, đặt $S_t=H_t$ cho RNN hoặc GRU và $S_t=(H_t,C_t)$ cho LSTM. Mặt nạ nguồn chọn giữa trạng thái do ô đề xuất và trạng thái trước:

$$
S_t^{(n)}=M^{src}_{n,t}\widehat S_t^{(n)}+\left(1-M^{src}_{n,t}\right)S_{t-1}^{(n)}.
$$

$\widehat S_t$ là trạng thái được tính trước khi áp dụng mặt nạ. Ở vị trí đệm, cả $H_t$ và $C_t$ của LSTM được giữ nguyên.

::: exercise Câu hỏi kiểm tra
Với LSTM, vì sao chỉ giữ $H_t$ ở vị trí đệm là chưa đủ?
:::

::: solution
Vì bước sau còn nhận $C_t$. Nếu $C_t$ bị cập nhật bởi dữ liệu đệm, trạng thái nội bộ của mẫu đã kết thúc vẫn bị thay đổi.
:::

## Khái niệm trọng tâm

### Cụm 1: Từ đường gradient dài đến trạng thái có cổng

Trong RNN cơ bản, tín hiệu qua nhiều bước chứa tích các Jacobian. Tích này có thể co về 0 hoặc tăng nhanh. Một cơ chế cho phụ thuộc dài cần hai khả năng đồng thời: giữ thông tin cũ với ít biến đổi và chỉ ghi thông tin mới khi phù hợp.

![So sánh đường trạng thái của RNN cơ bản và LSTM](img/lec-08/bridge-gradient.svg)

LSTM tách trạng thái thành hai đại lượng:

- $C_t$ là trạng thái ô, tạo đường tích lũy nội bộ theo thời gian;
- $H_t$ là trạng thái ẩn, công bố phần thông tin mà tầng khác hoặc đầu ra sử dụng.

Hai trạng thái có cùng kích thước nhưng không cùng vai trò. Cổng sigmoid nhận giá trị trong $(0,1)$ và điều chỉnh từng thành phần bằng tích Hadamard. Giá trị gần 0 làm nhánh đóng hơn; giá trị gần 1 làm nhánh mở hơn. Cổng không phải công tắc nhị phân.

### Cụm 2: Xây ô LSTM từ bốn tín hiệu

Ô LSTM dùng một ứng viên và ba cổng:

![Bốn tín hiệu tạo trạng thái của LSTM](img/lec-08/lstm-build.svg)

Ứng viên đề xuất nội dung mới:

$$
G_t=\tanh\!\left(X_tW_{xg}+H_{t-1}W_{hg}+b_g\right).
$$

Cổng vào điều chỉnh phần ứng viên được ghi; cổng ra điều chỉnh phần trạng thái ô được công bố; cổng quên điều chỉnh phần trạng thái ô cũ được giữ:

$$
I_t=\sigma\!\left(X_tW_{xi}+H_{t-1}W_{hi}+b_i\right),
$$

$$
O_t=\sigma\!\left(X_tW_{xo}+H_{t-1}W_{ho}+b_o\right),
$$

$$
F_t=\sigma\!\left(X_tW_{xf}+H_{t-1}W_{hf}+b_f\right).
$$

Trạng thái mới là tổng của nhánh giữ cũ và nhánh ghi mới:

$$
C_t=F_t\odot C_{t-1}+I_t\odot G_t,
\qquad H_t=O_t\odot\tanh(C_t).
$$

![Luồng hoàn chỉnh qua trạng thái ô và trạng thái ẩn](img/lec-08/lstm-cell.svg)

Bốn phép biến đổi affine có tham số riêng nhưng nhận cùng $X_t$ và $H_{t-1}$. Với $q\in\{i,f,o,g\}$:

$$
W_{xq}\in\mathbb R^{D_x\times D_h},\quad
W_{hq}\in\mathbb R^{D_h\times D_h},\quad
b_q\in\mathbb R^{1\times D_h}.
$$

$b_q$ được phát từ một hàng thành $N$ hàng. Phát tự động là phép dùng lại một trục có kích thước 1 trên các hàng của lô mà không sao chép dữ liệu về mặt khái niệm. Mọi cổng, ứng viên, $C_t$ và $H_t$ đều có kích thước $N\times D_h$.

### Cụm 3: Một bước LSTM bằng số

Xét ví dụ vô hướng với $c_{t-1}=0{,}3$ và các tiền kích hoạt

$$
a_i=0{,}2,\quad a_f=1{,}0,\quad a_o=-0{,}4,\quad a_g=0{,}6.
$$

Các tín hiệu của ô là

| Tín hiệu | Phép tính | Giá trị |
|---|---|---:|
| $I_t$ | $\sigma(0{,}2)$ | $0{,}5498$ |
| $F_t$ | $\sigma(1{,}0)$ | $0{,}7311$ |
| $O_t$ | $\sigma(-0{,}4)$ | $0{,}4013$ |
| $G_t$ | $\tanh(0{,}6)$ | $0{,}5370$ |

Hai nhánh cập nhật đóng góp

$$
F_tc_{t-1}=0{,}7311\cdot0{,}3=0{,}2193,
$$

$$
I_tG_t=0{,}5498\cdot0{,}5370\approx0{,}2953.
$$

Do đó

$$
c_t=0{,}2193+0{,}2953=0{,}5146,
$$

$$
\tanh(c_t)=0{,}4735,
\qquad h_t=0{,}4013\cdot0{,}4735=0{,}1900.
$$

::: exercise Câu hỏi kiểm tra
Nếu chỉ đổi $O_t$ thành 0 và giữ các đại lượng khác, $c_t$ và $h_t$ thay đổi thế nào?
:::

::: solution
$c_t$ vẫn bằng $0{,}5146$ vì cổng ra nằm sau cập nhật trạng thái ô; $h_t$ trở thành 0.
:::

### Cụm 4: Nhánh gradient trực tiếp của LSTM

Xét một hàng $n$ và giữ các cổng cùng ứng viên cố định trên cạnh trực tiếp. Jacobian từ trạng thái ô trước đến trạng thái ô mới là

$$
J_{t,n}^{C}:=\left.
\frac{\partial c_t^{(n)}}{\partial c_{t-1}^{(n)}}
\right|_{f_t^{(n)},i_t^{(n)},g_t^{(n)}}
=\operatorname{diag}\!\left(f_t^{(n)}\right).
$$

![Nhánh trực tiếp và các nhánh gián tiếp của gradient LSTM](img/lec-08/gradient-paths.svg)

Qua nhiều bước, hệ số trên nhánh trực tiếp là tích theo từng thành phần:

$$
J_{T\leftarrow t,n}^{C}
=\operatorname{diag}\!\left(\prod_{k=t+1}^{T}f_k^{(n)}\right).
$$

Ví dụ,

$$
0{,}95\cdot0{,}8\cdot0{,}9\cdot1\cdot0{,}7=0{,}4788.
$$

Đây chỉ là nhánh trực tiếp. Đạo hàm toàn phần còn cộng các đường qua $H_{t-1}$, các cổng, sigmoid, tanh và trọng số. LSTM tạo một đường thuận lợi hơn RNN cơ bản, nhưng không bảo đảm giữ mọi phụ thuộc dài và không loại bỏ gradient triệt tiêu hoặc bùng nổ.

::: exercise Câu hỏi kiểm tra
Mệnh đề “LSTM luôn giữ được phụ thuộc dài hạn vì có trạng thái ô” sai ở đâu?
:::

::: solution
Các cổng quên nhỏ liên tiếp vẫn làm tích trên nhánh trực tiếp suy giảm. Đạo hàm toàn phần còn phụ thuộc các nhánh và tham số khác.
:::

### Cụm 5: GRU gộp bộ nhớ vào một trạng thái

GRU không truyền một trạng thái ô riêng. Cổng đặt lại $R_t$ điều chỉnh phần trạng thái cũ tham gia tạo ứng viên; cổng cập nhật $Z_t$ điều chỉnh mức ứng viên thay trạng thái cũ.

![Hai cổng và đường trộn trạng thái trong GRU](img/lec-08/gru-cell.svg)

Theo quy ước của slide nguồn:

$$
R_t=\sigma\!\left(X_tW_{xr}+H_{t-1}W_{hr}+b_r\right),
$$

$$
Z_t=\sigma\!\left(X_tW_{xz}+H_{t-1}W_{hz}+b_z\right),
$$

$$
\widetilde H_t=\tanh\!\left(X_tW_{xh}+(R_t\odot H_{t-1})W_{hh}+b_h\right),
$$

$$
H_t=(1-Z_t)\odot H_{t-1}+Z_t\odot\widetilde H_t.
$$

Vì vậy $Z_t$ gần 1 ưu tiên ứng viên mới; $Z_t$ gần 0 ưu tiên trạng thái cũ.

Với $x_t=0{,}5$, $h_{t-1}=-0{,}2$, $a_r=0{,}3$, $a_z=0{,}7$, $W_{xh}=W_{hh}=1$ và $b_h=0$:

$$
R_t=0{,}5744,\qquad Z_t=0{,}6682,
$$

$$
\widetilde h_t=\tanh\!\left(0{,}5+0{,}5744(-0{,}2)\right)=0{,}3671,
$$

$$
h_t=(1-0{,}6682)(-0{,}2)+0{,}6682(0{,}3671)=0{,}1790.
$$

Các giá trị được tính từ số đầy đủ rồi làm tròn đến bốn chữ số thập phân.

Giáo trình đặt cổng cập nhật trên nhánh trạng thái cũ:

$$
H_t=Z_g\odot H_{t-1}+(1-Z_g)\odot\widetilde H_t.
$$

Hai quy ước tương đương khi đồng thời đặt $Z_s=1-Z_g$. Nếu cổng được tạo bởi sigmoid, $\sigma(-a)=1-\sigma(a)$, nên đổi quy ước còn đòi hỏi đổi dấu tiền kích hoạt cùng trọng số và độ lệch tạo ra nó.

Theo phương trình của bài, một phép affine có

$$
B=D_xD_h+D_h^2+D_h
$$

tham số. RNN cơ bản dùng $B$, GRU dùng $3B$, LSTM dùng $4B$. Phép đếm này không bao gồm tầng đầu ra và có thể khác cách đóng gói độ lệch của một API cụ thể.

::: exercise Câu hỏi kiểm tra
Theo quy ước slide, nếu $Z_t=0{,}2$ thì hệ số nhánh giữ trực tiếp là bao nhiêu? Đây có phải đạo hàm toàn phần không?
:::

::: solution
Hệ số là $1-Z_t=0{,}8$. Đây chưa phải đạo hàm toàn phần vì còn các đường qua cổng và ứng viên.
:::

### Cụm 6: Nhiều tầng và hai chiều

Sau khi xác định cơ chế của một ô, ta mở rộng mạng theo trục tầng và theo chiều thời gian.

Mạng truy hồi sâu thêm một trục tầng. Tầng $\ell$ nhận $H_t^{(\ell-1)}$ ở cùng bước và trạng thái của chính tầng đó ở bước trước:

$$
H_t^{(0)}=X_t,\qquad
S_t^{(\ell)}=\Phi^{(\ell)}\!\left(H_t^{(\ell-1)},S_{t-1}^{(\ell)}\right).
$$

![Cạnh theo thời gian và cạnh giữa các tầng](img/lec-08/stacked-rnn.svg)

Các tầng có tham số riêng; cùng một tầng dùng chung tham số theo thời gian. Với LSTM, mỗi tầng cần cả $H_t^{(\ell)}$ và $C_t^{(\ell)}$.

::: exercise Câu hỏi kiểm tra
Với LSTM tầng 2, $N=8$ và $D_2=32$, $H_t^{(2)}$, $C_t^{(2)}$ và $S_t^{(2)}$ có kích thước hoặc cấu trúc nào?
:::

::: solution
$H_t^{(2)}$ và $C_t^{(2)}$ đều có kích thước $8\times32$; $S_t^{(2)}=(H_t^{(2)},C_t^{(2)})$.
:::

Mạng hai chiều đọc cùng chuỗi theo hai hướng rồi nối trạng thái:

$$
H_t=[\overrightarrow H_t\,\|\,\overleftarrow H_t]
\in\mathbb R^{N\times2D_h}.
$$

![Hai hướng đọc trên cùng một chuỗi](img/lec-08/bidirectional.svg)

Trạng thái tại $t$ chứa ngữ cảnh từ cả hai phía của chuỗi đã biết. Vì hướng nghịch cần dữ liệu tương lai, cấu hình này không dùng trực tiếp cho dự đoán trực tuyến khi các bước tương lai chưa xuất hiện.

::: exercise Câu hỏi kiểm tra
Nhận dạng từng khung âm thanh ngay khi khung đến có dùng được trạng thái nghịch đầy đủ không?
:::

::: solution
Không, nếu hệ thống chưa nhận được các khung tương lai. Ngân sách độ trễ quyết định lượng ngữ cảnh tương lai có thể dùng.
:::

### Cụm 7: Bộ mã hóa–giải mã cho dịch máy

Dịch máy có chuỗi nguồn $x_1,\ldots,x_T$ và chuỗi đích $y_1,\ldots,y_{T'}$ không căn chỉnh theo cùng chỉ số. Sau khi tra cứu nhúng, bộ mã hóa GRU đọc $X_t$ và lấy trạng thái cuối hợp lệ của từng mẫu:

$$
H_t^{enc}=\operatorname{GRU}_{enc}(X_t,H_{t-1}^{enc}),\qquad
Q_n=H_{L_n}^{enc,(n)},\quad Q\in\mathbb R^{N\times D_h}.
$$

![Bộ mã hóa và bộ giải mã GRU](img/lec-08/encoder-decoder.svg)

Ngữ cảnh $Q$ chỉ khởi tạo trạng thái giải mã:

$$
S_0=Q,\qquad
S_{t'}=\operatorname{GRU}_{dec}\!\left(E(y_{t'-1}),S_{t'-1}\right),
$$

$$
A_{t'}=S_{t'}W_y+b_y,\qquad
P_{t'}=\operatorname{softmax}_{V}(A_{t'}).
$$

Ở đây $E(y_{t'-1})\in\mathbb R^{N\times D_e}$, $S_{t'}\in\mathbb R^{N\times D_h}$, $W_y\in\mathbb R^{D_h\times V}$ và $A_{t'}\in\mathbb R^{N\times V}$. Softmax tính theo trục từ vựng $V$. Ký hiệu $W_y,b_y$ dành cho tầng chiếu từ vựng, tách biệt với $W_{xo},W_{ho},b_o$ của cổng ra LSTM.

Khi huấn luyện, học theo đáp án (teacher forcing) đưa token đích đúng ở bước trước vào bộ giải mã. Khi suy luận, đầu vào là token mô hình vừa dự đoán. Hai chế độ có thể tạo lịch sử đầu vào khác nhau.

Mất mát chỉ tính trên token đích hợp lệ:

$$
\mathcal L=
\frac{\sum_{n,t'}M^{tgt}_{n,t'}\,\operatorname{CE}(A_{n,t'},y_{n,t'})}
{\sum_{n,t'}M^{tgt}_{n,t'}}.
$$

Chéo entropy được tính ổn định trực tiếp từ logit $A$; không tính softmax rồi lấy log thủ công. $M^{tgt}$ chỉ chọn token trong mất mát, còn $M^{src}$ giữ trạng thái nguồn tại vị trí đệm.

::: exercise Câu hỏi kiểm tra
Ở bước giải mã thứ hai, đầu vào là gì khi huấn luyện và khi suy luận?
:::

::: solution
Huấn luyện dùng $E(y_1)$; suy luận dùng $E(\widehat y_1)$.
:::

## Phần mở rộng: bốn đối chiếu triển khai

### Biểu diễn hai chiều cho phân loại

Với văn bản đã có đủ, biểu diễn mẫu $n$ có thể ghép trạng thái cuối của hướng thuận và trạng thái tương ứng toàn chuỗi của hướng nghịch:

$$
u_n^{cls}=
[\overrightarrow H_{L_n}^{(n)}\,\|\,\overleftarrow H_1^{(n)}]
\in\mathbb R^{1\times2D_h}.
$$

Xếp các hàng $u_n^{cls}$ thành $U^{cls}\in\mathbb R^{N\times2D_h}$ trước tầng phân loại.

![Ghép hai hướng để phân loại cảm xúc](img/lec-08/sentiment.svg)

### Chi phí của ô

Với $D_x=3$ và $D_h=4$:

$$
B=3\cdot4+4^2+4=32.
$$

Theo quy ước một độ lệch cho mỗi phép affine, RNN cơ bản có 32 tham số trong ô, GRU có 96 và LSTM có 128.

### Sinh tự hồi quy

Bộ giải mã bắt đầu từ $\langle bos\rangle$, dùng dự đoán trước làm đầu vào kế tiếp và dừng riêng cho từng mẫu khi sinh $\langle eos\rangle$ hoặc đạt độ dài tối đa. Đây là hành vi suy luận, không phải học theo đáp án.

### Chọn kiến trúc theo điều kiện sử dụng

Không có một ô truy hồi tốt nhất cho mọi dữ liệu. RNN cơ bản có phép cập nhật gọn; GRU dùng ít phép affine hơn LSTM; LSTM truyền thêm trạng thái ô; mạng hai chiều dùng được ngữ cảnh tương lai khi toàn chuỗi đã có.

::: exercise Câu hỏi kiểm tra
Gán nhãn từng token trên văn bản đã có đủ cần ngữ cảnh hai phía. Nêu một cấu hình hợp lệ và kích thước đầu ra trước, sau khi ghép hai hướng.
:::

::: solution
Có thể dùng GRU hoặc LSTM hai chiều. Mỗi hướng tạo tensor $N\times T\times D_h$; sau khi ghép theo trục đặc trưng, đầu ra có kích thước $N\times T\times2D_h$.
:::

## Tóm tắt và tự kiểm tra

- LSTM truyền $(H_t,C_t)$; GRU chỉ truyền $H_t$.
- Cổng tạo nhánh lưu giữ có điều kiện, nhưng không bảo đảm gradient luôn ổn định.
- Quy ước cổng cập nhật của GRU phải được khóa trước khi giải thích giá trị gần 0 hoặc gần 1.
- Mạng sâu thêm trục tầng; mạng hai chiều thêm hướng thời gian và cần dữ liệu tương lai.
- Bộ mã hóa–giải mã cơ sở nén chuỗi nguồn vào $Q$; $M^{src}$ và $M^{tgt}$ có hai vai trò khác nhau.

::: exercise Tự kiểm 1
Với $N=8,D_x=16,D_h=32$, $X_tW_{xi}$ và $b_i$ có kích thước nào trước khi cộng?
:::

::: solution
$X_tW_{xi}$ có kích thước $8\times32$; $b_i$ có kích thước $1\times32$ và được phát theo trục lô.
:::

::: exercise Tự kiểm 2
Với $N=4,D_h=32,V=10\,000$, $Q$ và $A_{t'}$ có kích thước nào?
:::

::: solution
$Q\in\mathbb R^{4\times32}$ và $A_{t'}\in\mathbb R^{4\times10\,000}$.
:::

## Bài tập 50 phút

1. **Tính một bước LSTM — 20 phút.** Tính lại bộ số của Cụm 3, sau đó lặp quy trình với một bộ tiền kích hoạt mới; đối chiếu kết quả làm tròn bốn chữ số.
2. **Phân tích đường gradient — 10 phút.** Tính tích cổng quên đã cho và giải thích vì sao đó chỉ là hệ số của nhánh trực tiếp.
3. **So sánh LSTM và GRU — 10 phút.** Với cùng $D_x,D_h$ và quy ước độ lệch của bài, so sánh trạng thái truyền đi, số phép affine, số tham số và hai quy ước cổng cập nhật $Z_s=1-Z_g$.
4. **Chọn mạng hai chiều — 10 phút.** Phân loại bốn tác vụ thành ngoại tuyến hoặc trực tuyến, rồi xác định trường hợp có thể dùng đầy đủ ngữ cảnh hai phía.

## Nguồn

- DOCX đề cương, mục III.2, Buổi 8: tên bài, LLO15–LLO16, phạm vi và hoạt động.
- `lec14_rnn.pdf`, trang 25–33: LSTM và GRU; trang 35–40: mạng nhiều tầng và hai chiều; dải đã duyệt 58–62, trong đó bài này dùng trang 58–59 cho bộ mã hóa–giải mã.
- `hocsau_draft.pdf`, trang PDF 226–245: LSTM, GRU, mạng sâu, hai chiều, bộ mã hóa–giải mã và mặt nạ.
- `hocsau_draft.pdf`, trang PDF 315–317: phân loại cảm xúc bằng mạng hai chiều.
