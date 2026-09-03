# Buổi 11: Kiến trúc Transformer

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- trình bày luồng dữ liệu qua bộ mã hóa và bộ giải mã Transformer;
- giải thích vai trò của truy vấn, khóa và giá trị trong tự chú ý;
- tính một phép chú ý có tích vô hướng được co giãn, đúng trục softmax và đúng mặt nạ;
- truy vết kích thước tensor qua chú ý nhiều đầu;
- giải thích mã hóa vị trí sin–cos, mạng truyền thẳng theo vị trí, đường dư và chuẩn hóa tầng;
- phân biệt tự chú ý của bộ mã hóa, tự chú ý nhân quả của bộ giải mã và chú ý chéo.

Kiến thức tiên quyết: phép nhân ma trận, softmax, chuẩn hóa, đạo hàm, kiến trúc mã hóa–giải mã và cơ chế chú ý của Buổi 10.

## Ký hiệu và hợp đồng tensor

| Ký hiệu | Kích thước | Nghĩa |
|---|---|---|
| $B$ | vô hướng nguyên | Cỡ lô |
| $T_s,T_t$ | vô hướng nguyên | Độ dài nguồn và đích |
| $T_q,T_k$ | vô hướng nguyên | Số vị trí truy vấn và khóa |
| $D$ | vô hướng nguyên | Chiều mô hình |
| $H_a$ | vô hướng nguyên | Số đầu chú ý |
| $d_k,d_v$ | vô hướng nguyên | Chiều khóa và giá trị của mỗi đầu |
| $Q,K,V$ | $B\times T_q\times d_k$, $B\times T_k\times d_k$, $B\times T_k\times d_v$ | Truy vấn, khóa và giá trị của một đầu |
| $S,A$ | $B\times T_q\times T_k$ | Điểm đã co giãn và trọng số chú ý |
| $O$ | $B\times T_q\times d_v$ | Đầu ra của một đầu |
| $B_M$ | $B\times1\times T_q\times T_k$ | Mặt nạ cộng, nhận giá trị $0$ hoặc $-\infty$ và phát qua trục đầu |
| $C$ | $B\times T_q\times D$ | Kết quả ghép các đầu |
| $PE$ | $T\times D$ | Mã hóa vị trí |
| $H^{enc},H^{dec}$ | $B\times T_s\times D$, $B\times T_t\times D$ | Đầu ra cuối của hai ngăn xếp |
| $M^{tgt}$ | $B\times T_t$ | Mặt nạ token đích tham gia hàm mất mát |

Với một đầu chú ý,

$$
S=\frac{QK^\top}{\sqrt{d_k}},\qquad
A=\operatorname{softmax}_{T_k}(S+B_M),\qquad
O=AV.
$$

Softmax chạy trên trục khóa. Mỗi hàng truy vấn hợp lệ phải có ít nhất một khóa hợp lệ.

## Khái niệm trọng tâm

### Cụm 1: Từ chú ý chéo đến tự chú ý

Trong chú ý chéo của Buổi 10, truy vấn đến từ chuỗi đích, còn khóa và giá trị đến từ chuỗi nguồn. Tự chú ý dùng cùng một tensor đầu vào để tạo cả ba vai trò.

![Chú ý chéo và tự chú ý khác nhau ở nguồn tạo truy vấn, khóa và giá trị](img/lec-11/attention-bridge.svg)

Với $X\in\mathbb R^{B\times T\times D}$,

$$
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V,
$$

trong đó $W_Q,W_K\in\mathbb R^{D\times d_k}$ và $W_V\in\mathbb R^{D\times d_v}$.

![Ba phép chiếu tạo truy vấn, khóa và giá trị từ cùng tensor đầu vào](img/lec-11/qkv-projection.svg)

Truy vấn mô tả điều một vị trí đang tìm. Khóa mô tả điều mỗi vị trí cung cấp để so khớp. Giá trị mang nội dung được tổng hợp. Với hàng truy vấn thứ $i$,

$$
o_i=\sum_{j=1}^{T_k}A_{i,j}v_j.
$$

::: exercise Câu hỏi kiểm tra
Trong một ví dụ khởi động độc lập, cho $X=\begin{bmatrix}1&0\\0&1\end{bmatrix}$ và $W_Q=W_K=I_2$. Hãy tính $Q,K$ và nêu trục được rút gọn trong $QK^\top$.
:::

::: solution
$Q=K=X$. Trong $QK^\top$, chiều $d_k=2$ được rút gọn; kết quả có kích thước $2\times2$ khi tạm bỏ trục lô.
:::

### Cụm 2: Một vết tính tự chú ý hoàn chỉnh

Xét $B=1,T=3,D=4,d_k=d_v=2$ và tạm bỏ trục lô:

$$
X=\begin{bmatrix}1&0&1&0\\0&1&0&1\\1&1&0&0\end{bmatrix}.
$$

Các ma trận dưới đây được chọn để phép tính tay ngắn; chúng không phải một bộ trọng số tối ưu hay duy nhất. Đầu thứ nhất dùng

$$
W_Q^{(1)}=W_K^{(1)}=
\begin{bmatrix}1&0\\0&1\\0&0\\0&0\end{bmatrix},\qquad
W_V^{(1)}=
\begin{bmatrix}0&0\\0&0\\1&0\\0&1\end{bmatrix}.
$$

Do đó

$$
Q^{(1)}=K^{(1)}=
\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix},\qquad
V^{(1)}=
\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}.
$$

![Mỗi hàng truy vấn được so với mọi hàng khóa](img/lec-11/score-matrix.svg)

Tích vô hướng và điểm đã co giãn là

$$
Q^{(1)}K^{(1)\top}=
\begin{bmatrix}1&0&1\\0&1&1\\1&1&2\end{bmatrix},
$$

$$
S^{(1)}=\frac{Q^{(1)}K^{(1)\top}}{\sqrt2}
\approx
\begin{bmatrix}.707&0&.707\\0&.707&.707\\.707&.707&1.414\end{bmatrix}.
$$

Hệ số $\sqrt{d_k}$ hạn chế độ lớn của điểm khi $d_k$ tăng, nhờ đó giảm nguy cơ softmax bão hòa. Lập luận này dựa trên giả thiết các thành phần có phương sai được kiểm soát; nó không bảo đảm mọi phân phối điểm đều giống nhau.

Không có mặt nạ, softmax theo từng hàng cho

$$
A^{(1)}\approx
\begin{bmatrix}.401&.198&.401\\.198&.401&.401\\.248&.248&.503\end{bmatrix}.
$$

![Trọng số chú ý nhân với giá trị để tạo đầu ra](img/lec-11/attention-output.svg)

$$
O^{(1)}=A^{(1)}V^{(1)}
\approx
\begin{bmatrix}.401&.198\\.198&.401\\.248&.248\end{bmatrix}.
$$

Hàng thứ ba của $V^{(1)}$ bằng không. Vì vậy, trọng số lớn trên khóa thứ ba không tạo đóng góp vào đầu ra trong ví dụ này.

::: exercise Câu hỏi kiểm tra
Từ $Q^{(1)},K^{(1)},V^{(1)}$ ở trên, hãy tính lại hàng thứ ba của $A^{(1)}$ và $O^{(1)}$. Kiểm tra tổng trọng số trước khi làm tròn.
:::

::: solution
Hàng điểm đã co giãn là $(.707,.707,1.414)$. Softmax cho xấp xỉ $(.248,.248,.503)$; dùng số chưa làm tròn thì tổng bằng 1. Nhân với $V^{(1)}$ cho hàng đầu ra xấp xỉ $(.248,.248)$.
:::

### Cụm 3: Mặt nạ xác định tập khóa hợp lệ

Mặt nạ luận lý và mặt nạ cộng biểu diễn cùng một quyết định. Trong quy ước của phần này, mặt nạ luận lý bằng 1 khi khóa được phép tham gia. Nó được đổi thành $0$ ở vị trí hợp lệ và $-\infty$ ở vị trí bị chặn, rồi cộng trước softmax.

![Mặt nạ luận lý được chuyển thành mặt nạ cộng trước softmax](img/lec-11/mask-contract.svg)

Đặt trọng số bị chặn về 0 sau softmax mà không chuẩn hóa lại sẽ làm tổng hàng sai. Nếu cả hàng nhận $-\infty$, softmax không xác định; chương trình phải bảo đảm có ít nhất một khóa hợp lệ hoặc đưa đầu ra của truy vấn đó về không.

Trong bộ giải mã, mặt nạ nhân quả chỉ cho truy vấn $i$ đọc khóa $j\le i$:

$$
M^{causal}_{i,j}=\mathbf 1[j\le i],\qquad
B_M=
\begin{bmatrix}
0&-\infty&-\infty\\
0&0&-\infty\\
0&0&0
\end{bmatrix}.
$$

![Mặt nạ nhân quả ba vị trí có dạng tam giác dưới](img/lec-11/causal-mask.svg)

Áp dụng mặt nạ này vào vết tính ở Cụm 2:

$$
A^{(1)}_{causal}\approx
\begin{bmatrix}1&0&0\\.330&.670&0\\.248&.248&.503\end{bmatrix},
\quad
O^{(1)}_{causal}\approx
\begin{bmatrix}1&0\\.330&.670\\.248&.248\end{bmatrix}.
$$

Ở hàng thứ hai, mặt nạ giữ hai điểm $(0,.707)$ nên softmax cho $(.330,.670)$. Hàng thứ ba không đổi vì cả ba khóa đều hợp lệ.

Mặt nạ đệm chặn khóa đệm trước softmax. Mặt nạ hàm mất mát loại token đệm khỏi tổng và mẫu số của chéo entropy. Hai mặt nạ phục vụ hai phép tính khác nhau.

::: exercise Câu hỏi kiểm tra
Vì sao hàng thứ ba của $A^{(1)}_{causal}$ không đổi, còn hàng thứ nhất trở thành $(1,0,0)$?
:::

::: solution
Truy vấn thứ ba được đọc cả ba khóa nên tập chuẩn hóa không đổi. Truy vấn thứ nhất chỉ được đọc khóa đầu tiên; softmax trên một phần tử cho trọng số 1.
:::

### Cụm 4: Ba loại chú ý và chú ý nhiều đầu

#### Ba nguồn tensor

![Nguồn của truy vấn, khóa và giá trị trong ba loại chú ý](img/lec-11/three-attention-types.svg)

| Loại chú ý | Nguồn $Q$ | Nguồn $K,V$ | Kích thước $A$ |
|---|---|---|---|
| Tự chú ý bộ mã hóa | Chuỗi nguồn | Chuỗi nguồn | $B\times T_s\times T_s$ |
| Tự chú ý nhân quả bộ giải mã | Chuỗi đích | Chuỗi đích | $B\times T_t\times T_t$ |
| Chú ý chéo | Trạng thái bộ giải mã | Đầu ra bộ mã hóa | $B\times T_t\times T_s$ |

Trong cả ba trường hợp, softmax chạy trên trục khóa, tức trục cuối của $A$. Mặt nạ khóa nguồn phát theo các trục lô, đầu và truy vấn nhưng chặn theo cột khóa.

Sau khi phân biệt nguồn của $Q,K,V$, ta mở rộng một đầu thành nhiều đầu chạy song song.

#### Từ một đầu đến nhiều đầu

Chú ý nhiều đầu thực hiện nhiều phép chiếu song song, ghép kết quả theo chiều đặc trưng rồi chiếu về chiều mô hình:

$$
\operatorname{MHA}(Q_{in},K_{in},V_{in})
=\operatorname{Concat}(O^{(1)},\ldots,O^{(H_a)})W_O+b_O.
$$

![Các đầu chú ý chạy song song, được ghép rồi chiếu ra](img/lec-11/multihead-flow.svg)

Thường chọn $H_ad_k=H_ad_v=D$. Với $D=4,H_a=2,d_k=d_v=2$, đầu thứ hai trong vết tính dùng

$$
Q^{(2)}=K^{(2)}=
\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix},\qquad
V^{(2)}=
\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}.
$$

Kết quả không mặt nạ là

$$
A^{(2)}\approx
\begin{bmatrix}.503&.248&.248\\.248&.503&.248\\.333&.333&.333\end{bmatrix},
\quad
O^{(2)}\approx
\begin{bmatrix}.752&.497\\.497&.752\\.667&.667\end{bmatrix}.
$$

Ghép $O^{(1)}$ và $O^{(2)}$ cho $C\in\mathbb R^{1\times3\times4}$. Nếu $W_O=I_4,b_O=0$, đầu ra chú ý nhiều đầu bằng $C$.

Không tính độ lệch, bốn phép chiếu $W_Q,W_K,W_V,W_O$ có $4D^2$ tham số. Nếu cả bốn có độ lệch, tổng là $4D^2+4D$. Giữ $D$ cố định rồi đổi số đầu không làm thay đổi tổng tham số chiếu.

::: exercise Câu hỏi kiểm tra
Với $D=8,H_a=4$, hãy tính $d_k=d_v$ và số tham số chiếu khi có độ lệch.
:::

::: solution
$d_k=d_v=D/H_a=2$. Tổng số tham số là $4D^2+4D=4\cdot64+32=288$.
:::

### Cụm 5: Vị trí, mạng truyền thẳng, đường dư và chuẩn hóa

Tự chú ý không mặt nạ là tương đương theo hoán vị: hoán vị các hàng đầu vào làm đầu ra hoán vị theo cùng cách. Muốn phân biệt thứ tự, Transformer gốc cộng mã hóa vị trí sin–cos vào nhúng:

$$
PE_{p,2i}=\sin\!\left(\frac{p}{10000^{2i/D}}\right),\qquad
PE_{p,2i+1}=\cos\!\left(\frac{p}{10000^{2i/D}}\right).
$$

Với $D=4$,

$$
PE_0=[0,1,0,1],
$$

$$
PE_1\approx[.841,.540,.010,1],\qquad
PE_2\approx[.909,-.416,.020,1].
$$

Các cặp chiều có $i$ nhỏ biến đổi nhanh hơn theo vị trí; $i$ lớn cho tần số thấp hơn. Có thể liên hệ các cặp biến đổi chậm với bit bậc cao trong biểu diễn nhị phân: chúng giữ cấu trúc trên khoảng vị trí dài hơn. Tensor $PE\in\mathbb R^{T\times D}$ được phát qua trục lô:

$$
H_0=X+PE.
$$

![Mã hóa vị trí được cộng vào từng hàng của tensor đầu vào](img/lec-11/positional-encoding.svg)

Phép chú ý đầu tiên nhận $H_0$ thay cho $X$ nhưng giữ nguyên hợp đồng kích thước đã truy vết. Sau chú ý, mạng truyền thẳng áp dụng cùng một phép biến đổi độc lập tại từng vị trí:

$$
\operatorname{FFN}(h)=\operatorname{ReLU}(hW_1+b_1)W_2+b_2,
$$

với $W_1\in\mathbb R^{D\times D_{ff}}$ và $W_2\in\mathbb R^{D_{ff}\times D}$. Chú ý trộn thông tin giữa các vị trí; mạng truyền thẳng biến đổi riêng vectơ tại mỗi vị trí.

Đường dư yêu cầu hai nhánh cùng kích thước. $\operatorname{Drop}$ là phép bỏ ngẫu nhiên dùng để điều chuẩn: nó bật khi huấn luyện và tắt khi đánh giá.

$$
R=H+\operatorname{Drop}(F(H)).
$$

Với từng vectơ vị trí $r\in\mathbb R^D$, chuẩn hóa tầng chạy trên chiều đặc trưng:

$$
\mu=\frac1D\sum_jr_j,\qquad
\sigma^2=\frac1D\sum_j(r_j-\mu)^2,
$$

$$
\operatorname{LN}(r)=\gamma\odot
\frac{r-\mu}{\sqrt{\sigma^2+\varepsilon}}+\beta,
\qquad \gamma,\beta\in\mathbb R^D,\quad\varepsilon>0.
$$

Kiến trúc nguồn dùng chuẩn hóa sau đường dư:

$$
U=\operatorname{LN}\!\left(H+\operatorname{Drop}(\operatorname{MHA}(H))\right),
$$

$$
H'=\operatorname{LN}\!\left(U+\operatorname{Drop}(\operatorname{FFN}(U))\right).
$$

![Khối Transformer dùng đường dư và chuẩn hóa sau mỗi nhánh](img/lec-11/transformer-block-postnorm.svg)

::: exercise Câu hỏi kiểm tra
Một tensor có kích thước $B\times T\times D$ đi qua chú ý nhiều đầu, đường dư, chuẩn hóa tầng và FFN. Kích thước nào được giữ nguyên, và chuẩn hóa tầng rút gọn trên trục nào?
:::

::: solution
Kích thước ngoài của khối vẫn là $B\times T\times D$. Chuẩn hóa tầng tính trung bình và phương sai trên chiều đặc trưng $D$ cho từng cặp mẫu–vị trí; nó không trộn lô hay vị trí.
:::

### Cụm 6: Ngăn xếp bộ mã hóa và bộ giải mã

Đặt $H^{src}_0$ là nhúng nguồn đã cộng mã hóa vị trí. Mỗi tầng bộ mã hóa thực hiện tự chú ý, đường dư, chuẩn hóa, rồi FFN, đường dư và chuẩn hóa:

$$
M_\ell=\operatorname{MHA}(H^{src}_{\ell-1},H^{src}_{\ell-1},H^{src}_{\ell-1}),
$$

$$
U_\ell=\operatorname{LN}(H^{src}_{\ell-1}+\operatorname{Drop}(M_\ell)),
$$

$$
H^{src}_\ell=\operatorname{LN}(U_\ell+\operatorname{Drop}(\operatorname{FFN}(U_\ell))),
\qquad H^{enc}=H^{src}_{L_{enc}}.
$$

![Mỗi tầng bộ mã hóa giữ kích thước nguồn và được lặp thành ngăn xếp](img/lec-11/encoder-stack.svg)

Đặt $G_0$ là nhúng đích đã dịch một vị trí và cộng mã hóa vị trí. Mỗi tầng bộ giải mã có ba nhánh:

$$
U_\ell=\operatorname{LN}\!\left(G_{\ell-1}+\operatorname{Drop}(\operatorname{MHA}_{causal}(G_{\ell-1},G_{\ell-1},G_{\ell-1}))\right),
$$

$$
C_\ell=\operatorname{LN}\!\left(U_\ell+\operatorname{Drop}(\operatorname{MHA}(U_\ell,H^{enc},H^{enc}))\right),
$$

$$
G_\ell=\operatorname{LN}\!\left(C_\ell+\operatorname{Drop}(\operatorname{FFN}(C_\ell))\right),
\qquad H^{dec}=G_{L_{dec}}.
$$

![Mỗi tầng bộ giải mã gồm tự chú ý nhân quả, chú ý chéo và mạng truyền thẳng](img/lec-11/decoder-stack.svg)

Tự chú ý nhân quả lấy $Q,K,V$ từ trạng thái đích trước tầng. Chú ý chéo lấy $Q$ từ bộ giải mã nhưng lấy $K,V$ từ $H^{enc}$. FFN nhận trạng thái sau chú ý chéo.

::: exercise Câu hỏi kiểm tra
Nếu $T_s=5,T_t=3$, hãy nêu kích thước ma trận trọng số của tự chú ý bộ giải mã và chú ý chéo.
:::

::: solution
Tự chú ý bộ giải mã có $A\in\mathbb R^{B\times H_a\times3\times3}$. Chú ý chéo có $A\in\mathbb R^{B\times H_a\times3\times5}$. Trong cả hai, softmax chạy trên trục cuối.
:::

### Cụm 7: Đầu ra, huấn luyện và suy luận

Chuỗi đích được dịch một vị trí:

Chuỗi đầu vào là `<bos> tôi học`; chuỗi nhãn là `tôi học <eos>`.

`<bos>` và `<eos>` lần lượt đánh dấu bắt đầu và kết thúc chuỗi.

Điểm từ vựng là

$$
Z=H^{dec}W_{vocab}+b_{vocab}
\in\mathbb R^{B\times T_t\times|V_{tgt}|}.
$$

Đặt $M^{tgt}_{n,t}=1$ cho token đích hợp lệ, kể cả EOS, và bằng 0 cho đệm. Với $N_M=\sum_{n,t}M^{tgt}_{n,t}>0$,

$$
\mathcal L=-\frac1{N_M}\sum_{n,t}M^{tgt}_{n,t}
\operatorname{logsoftmax}(Z_{n,t,:})_{Y^{out}_{n,t}}.
$$

Softmax trong hàm mất mát chạy trên trục từ vựng. Khi triển khai, dùng chéo entropy hợp nhất hoặc log-softmax ổn định thay vì tính xác suất rồi lấy log. Khi huấn luyện bằng học theo đáp án (teacher forcing), toàn bộ vị trí đích được tính song song dưới mặt nạ nhân quả. Khi suy luận, bộ giải mã bắt đầu từ BOS, sinh từng token và dừng tại EOS hoặc giới hạn độ dài. Bỏ ngẫu nhiên bật khi huấn luyện và tắt khi đánh giá.

::: exercise Câu hỏi kiểm tra
Mặt nạ nhân quả và mặt nạ hàm mất mát khác nhau ở đại lượng bị tác động như thế nào?
:::

::: solution
Mặt nạ nhân quả thay đổi tập khóa trước softmax chú ý. Mặt nạ hàm mất mát quyết định token đích nào tham gia tổng và mẫu số của chéo entropy.
:::

## Mở rộng: Đối xứng, chi phí và cấu trúc vị trí

Như đã nêu ở Cụm 5, nếu không có mã hóa vị trí hay mặt nạ phụ thuộc vị trí, tự chú ý hoán vị đầu ra theo cùng phép hoán vị của đầu vào. Mã hóa vị trí phá đối xứng này bằng cách gắn một tín hiệu khác nhau cho từng hàng.

Với tự chú ý có $T_q=T_k=T$, hai phép nhân ma trận chính có chi phí

$$
QK^\top:\ \Theta(BH_aT^2d_k),\qquad
AV:\ \Theta(BH_aT^2d_v).
$$

Ma trận trọng số có $BH_aT^2$ phần tử. Vì vậy, tăng $T$ từ 128 lên 512 làm hạng theo $T^2$ tăng 16 lần. Đây là chi phí của khối chú ý, không phải tổng chi phí của toàn mô hình.

Với chiều mô hình $D$ và nhân tích chập rộng $k$, các hạng chi phối thường được so sánh như sau:

| Cơ chế | Chi phí mỗi tầng | Số bước tuần tự | Đường truyền dài nhất |
|---|---:|---:|---:|
| Mạng truy hồi | $O(TD^2)$ | $O(T)$ | $O(T)$ |
| Tích chập | $O(kTD^2)$ | $O(1)$ | $O(\log_k T)$ với kiến trúc mở rộng vùng nhìn theo tầng |
| Tự chú ý | $O(T^2D)$ | $O(1)$ | $O(1)$ |

Bảng chỉ mô tả một tầng và các giả thiết kiến trúc tương ứng; nó không đủ để kết luận cơ chế nào luôn nhanh hoặc tốt hơn.

Với $\omega_i=10000^{-2i/D}$, mỗi cặp sin–cos thỏa

$$
\begin{bmatrix}PE_{p+k,2i}\\PE_{p+k,2i+1}\end{bmatrix}
=
\begin{bmatrix}
\cos(k\omega_i)&\sin(k\omega_i)\\
-\sin(k\omega_i)&\cos(k\omega_i)
\end{bmatrix}
\begin{bmatrix}PE_{p,2i}\\PE_{p,2i+1}\end{bmatrix}.
$$

Phép quay này chỉ phụ thuộc độ lệch $k$, không phụ thuộc vị trí tuyệt đối $p$. Đây là một tính chất của tín hiệu sin–cos, không phải bảo đảm rằng mô hình luôn học được mọi quan hệ vị trí tương đối.

## Tổng kết

- Chú ý nối trực tiếp các vị trí trong một tầng, thay cho đường truyền trạng thái tuần tự bên trong mạng truy hồi.
- Tự chú ý tạo $Q,K,V$ từ cùng tensor; chú ý chéo dùng truy vấn đích và khóa–giá trị nguồn.
- Điểm được chia cho $\sqrt{d_k}$, cộng mặt nạ rồi softmax trên trục khóa.
- Chú ý nhiều đầu thay đổi cách chia chiều nhưng giữ tổng chiều mô hình khi $H_ad_k=H_ad_v=D$.
- Mã hóa vị trí bổ sung thứ tự; FFN biến đổi theo vị trí; đường dư và chuẩn hóa giữ hợp đồng kích thước của khối.
- Bộ mã hóa lặp tự chú ý và FFN. Bộ giải mã lặp tự chú ý nhân quả, chú ý chéo và FFN.
- Huấn luyện tính các vị trí đích song song; suy luận tự hồi quy vẫn sinh tuần tự.
- Buổi 12 sẽ phân biệt các biến thể chỉ dùng bộ mã hóa, chỉ dùng bộ giải mã và cách chúng hỗ trợ mô hình ngôn ngữ lớn.

## Bài tập 50 phút

1. **Tính một phép tự chú ý, 20 phút.** Cho $B=1,T=2,D=d_k=d_v=2$, $X=I_2$, $W_Q=W_K=W_V=I_2$ và không có mặt nạ. Tính $Q,K,V,S,A,O$, làm tròn $A$ đến ba chữ số và ghi kích thước có trục lô.
2. **Kết hợp mặt nạ, 10 phút.** Một lô có $B=2,T=3$. Mẫu thứ nhất có ba token hợp lệ; mẫu thứ hai có hai token hợp lệ và vị trí cuối là đệm. Với tự chú ý nhân quả, hãy viết mặt nạ giữ/chặn của từng mẫu rồi chuyển thành mặt nạ cộng kích thước $B\times1\times3\times3$. Nêu vị trí bị loại khỏi hàm mất mát của mẫu thứ hai.
3. **Truy vết nhiều đầu, 10 phút.** Cho $B=2,T=5,D=8,H_a=2,d_k=d_v=4$. Ghi kích thước $Q,K,V$, điểm, trọng số, đầu ra từng đầu, tensor sau ghép và tensor sau $W_O\in\mathbb R^{8\times8}$. Đếm tham số chiếu khi không dùng độ lệch.
4. **Kiểm chứng bằng PyTorch, 10 phút.** Trên CPU với PyTorch 2.13, cài đặt năm bước thủ công: $QK^\top$, chia $\sqrt{d_k}$, áp dụng mặt nạ, softmax theo trục khóa cuối và nhân $V$. So sánh với `torch.nn.functional.scaled_dot_product_attention` bằng `torch.testing.assert_close`. Dùng tensor dạng $(B,H_a,T,d_k)$ với $d_k=d_v$, đặt `dropout_p=0.0` và dùng cùng mặt nạ giữ. Với `torch.nn.MultiheadAttention`, đặt `batch_first=True`; lưu ý mặt nạ Boolean của API này dùng `True` để chặn, ngược với mặt nạ Boolean của hàm chú ý tích vô hướng được co giãn.

## Nguồn

- Đề cương học phần, mục III.2, Buổi 11: tên buổi, LLO21–LLO22 và phạm vi kiến trúc Transformer.
- `source-materials/slides/lec15_attention.pdf`, trang PDF 28–48: tự chú ý, mặt nạ, chú ý nhiều đầu và các thành phần Transformer.
- `source-materials/slides/lec16_transformer.pdf`, trang PDF 4–17, 22, 26, 28, 33 và 36: bộ mã hóa, bộ giải mã, vị trí, chú ý nhiều đầu, FFN, chuẩn hóa tầng và kiến trúc đầy đủ.
- `source-materials/textbooks/hocsau_draft.pdf`, trang PDF 263–270: chú ý tích vô hướng được co giãn, mặt nạ và mã hóa vị trí.
- `source-materials/textbooks/hocsau_draft.pdf`, trang PDF 271–276: đường dư, chuẩn hóa, ngăn xếp mã hóa–giải mã và huấn luyện.
- Tài liệu PyTorch 2.13 lưu trong kho cho `torch.nn.functional.scaled_dot_product_attention` và `torch.nn.MultiheadAttention`: chữ ký API, kích thước, mặt nạ Boolean, `batch_first`, `is_causal`, `dropout_p` và đầu ra.
