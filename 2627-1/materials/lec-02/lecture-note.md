# Buổi 02 — Lan truyền và đồ thị tính toán

## Mục tiêu và kiến thức tiên quyết

Sau khi đọc, người học có thể:

- mô tả lan truyền xuôi, hàm mất mát, lan truyền ngược và một bước cập nhật MLP;
- dựng đồ thị tính toán cho biểu thức đơn giản và áp dụng quy tắc chuỗi;
- giải thích gradient thượng nguồn, đạo hàm cục bộ và phép cộng gradient nhiều nhánh;
- kiểm kích thước gradient qua ReLU và tầng afin theo lô;
- theo dõi một MLP nhỏ từ $X,Y$ đến $J$, gradient và cập nhật.

Tiên quyết: đạo hàm một biến, quy tắc chuỗi, phép nhân ma trận, MLP, ReLU, softmax, logarit. Jacobian được giới thiệu trong bài, không phải tiên quyết.

## Ký hiệu và quy ước

- $B,d,h,k$: kích thước lô, số đặc trưng, số đơn vị ẩn, số lớp.
- Dữ liệu theo hàng: $X\in\mathbb R^{B\times d}$, hàng $i$ là một mẫu.
- $A=XW_1+b_1$, $H=\operatorname{ReLU}(A)$, $Z=HW_2+b_2$, $P=\operatorname{softmax}(Z)$ theo trục lớp trong từng hàng.
- $Y\in\{0,1\}^{B\times k}$ là nhãn nhất vị.
- $J$ là hàm mất mát vô hướng lấy trung bình theo lô; $J_f$ mới là Jacobian của $f$.
- $G_U=\partial J/\partial U$ có cùng kích thước với $U$; ở đồ thị vô hướng có thể viết $\bar u=\partial J/\partial u$.
- Độ chệch được quảng bá theo chiều lô. $\eta$ là tốc độ học.
- Phân biệt điểm số $Z$ với xác suất $P$, lan truyền xuôi với lan truyền ngược, gradient với tham số.

## Khái niệm trọng tâm

### Từ MLP đến nhu cầu gradient

Mạch tính toán của một MLP đi theo chuỗi $X\to A\to H\to Z\to P\to J$. Lan truyền xuôi tính dự đoán và mất mát. Lan truyền ngược tính gradient của cùng hàm $J$ theo từng tham số. Cập nhật chỉ diễn ra sau khi có đủ gradient:

$$
\theta\leftarrow\theta-\eta G_\theta,
\qquad \theta=\{W_1,b_1,W_2,b_2\}.
$$

Lan truyền diễn ra trên đồ thị có hướng không chu trình. Mỗi nút là một đại lượng trung gian; mỗi cạnh cho biết một biến là đầu vào của một phép toán. Thứ tự tô-pô của đồ thị cho phép định nghĩa thứ tự duyệt xuôi và ngược. Bài này không khảo sát các bộ tối ưu.

### Ví dụ vô hướng chạy xuôi và quy tắc chuỗi

Xét:

$$
f=2\bigl(xy+\max(z,w)\bigr),\quad
q=xy,\ r=\max(z,w),\ s=q+r,\ f=2s.
$$

Với $x=3,y=-4,z=2,w=-1$: $q=-12,r=2,s=-10,f=-20$. Khi duyệt xuôi, cần lưu $x,y$ cho cổng nhân và nhánh thắng của cực đại để dùng lại ở lan truyền ngược.

Quy tắc chuỗi được viết dưới dạng cộng-gán:

$$
\bar u\mathrel{+}=\bar v\frac{\partial v}{\partial u}.
$$

Dấu cộng-gán là bắt buộc khi một biến đi vào nhiều nhánh, vì gradient của $J$ theo $u$ là tổng đóng góp từ mọi đường qua $u$. Với $\bar f=1$: $\bar s=2$, $\bar q=\bar r=2$, $\bar x=-8$, $\bar y=6$, $\bar z=2$, $\bar w=0$. Ba hành vi đáng chú ý: cổng cộng truyền nguyên gradient cả hai phía; cổng nhân đổi vai trò hai đầu vào (gradient theo $x$ là $y\bar q$, gradient theo $y$ là $x\bar q$); cổng cực đại chỉ truyền qua nhánh thắng, nhánh thua nhận gradient 0.

![Đồ thị tính toán vô hướng thể hiện lan truyền xuôi giá trị và lan truyền ngược gradient qua các cổng nhân, cộng, cực đại.](img/lec-02/scalar-gate-forward-backward.svg)

![Phép cộng gradient khi một biến đi vào nhiều nhánh: tổng đóng góp từ từng đường truyền ngược.](img/lec-02/branch-gradient-accumulation.svg)

Khi cực đại hòa ($z=w$) hay tại điểm gãy của ReLU, không tồn tại một đạo hàm cổ điển duy nhất. Bài này chọn đạo hàm ReLU bằng 0 tại điểm gãy và không dùng trường hợp cực đại hòa trong ví dụ số.

::: exercise Câu hỏi kiểm tra
Với $f=2\bigl(xy+\max(z,w)\bigr)$ tại $x=4,y=-6,z=-1,w=2.5$, dùng quy tắc chuỗi để tính $\bar x,\bar y,\bar z,\bar w$.
:::

::: solution
Kết quả ngắn để tự đối chiếu: gradient theo $x,y,z,w$ lần lượt là $-12,8,0,2$. Cực đại chọn nhánh $w$ vì $2.5>-1$.
:::

### Thuật toán lan truyền ngược

Lan truyền ngược gồm bốn bước:

1. duyệt xuôi theo thứ tự tô-pô và lưu giá trị cần thiết cho bước ngược;
2. khởi tạo gradient đầu ra bằng 1, các bộ tích lũy còn lại bằng 0;
3. duyệt nút theo thứ tự tô-pô ngược;
4. nhân gradient thượng nguồn với đạo hàm cục bộ và cộng vào từng đầu vào.

Bước ngược là quy hoạch động trên đồ thị: mỗi nút được xử lý đúng một lần khi gradient thượng nguồn đã hoàn tất. Nhờ đó không cần liệt kê mọi đường từ đầu ra về một biến.

### Từ số vô hướng sang tensor và tích vector–Jacobian

Nếu $U\in\mathbb R^{a\times b}$ thì $G_U\in\mathbb R^{a\times b}$, cùng kích thước với $U$. Với $z=f(x)$, quy ước Jacobian có hàng là đầu ra, cột là đầu vào:

$$
J_f=\frac{\partial z}{\partial x}\in\mathbb R^{N\times M},
\qquad G_x^{\mathrm{row}}=G_z^{\mathrm{row}}J_f.
$$

Lan truyền ngược không dựng ma trận Jacobian dày đặc; nó tính tích vector–Jacobian (VJP) theo cấu trúc cục bộ của từng cổng. Với phép toán theo phần tử, Jacobian là ma trận chéo, nên:

$$
G_x=G_z\odot g'(x).
$$

Với ReLU:

$$
G_A=G_H\odot\mathbf 1[A>0].
$$

Bài này chọn đạo hàm ReLU bằng 0 tại $A=0$. Mặt nạ dùng tiền kích hoạt $A$ đã lưu ở lan truyền xuôi, không dùng dấu của gradient thượng nguồn.

### Tầng afin theo lô

Với $Z=XW+b$, khai triển theo chỉ số:

$$
Z_{ic}=\sum_{j=1}^{d}X_{ij}W_{jc}+b_c.
$$

Suy theo chỉ số trước rồi gộp thành dạng ma trận:

$$
G_X=G_ZW^\top,\qquad
G_W=X^\top G_Z,\qquad
G_b=\sum_{i=1}^{B}G_{Z,i:}.
$$

$G_b$ cộng theo trục lô vì cùng $b_c$ được dùng ở mọi hàng. Vì vậy, gradient theo $b_c$ là tổng đóng góp từ cả $B$ hàng.

![Lan truyền ngược qua tầng afin theo lô: các tích ma trận và phép cộng theo trục lô.](img/lec-02/affine-layer-backward.svg)

::: exercise Câu hỏi kiểm tra
Với tầng afin $Z=XW+b$ và $B=8,d=5,k=3$, hãy nêu kích thước của $G_X,G_W,G_b$.
:::

::: solution
$G_X$ là $8\times5$, $G_W$ là $5\times3$, $G_b$ có 3 phần tử (cộng theo trục lô).
:::

### Softmax, log-softmax và entropy chéo

Softmax theo trục lớp, kèm trừ cực đại từng hàng để ổn định số:

$$
P_{ic}=\frac{\exp(Z_{ic}-m_i)}{\sum_r\exp(Z_{ir}-m_i)},
\qquad m_i=\max_r Z_{ir}.
$$

Log-sum-exp ổn định:

$$
\operatorname{LSE}(Z_{i:})=m_i+\log\sum_r e^{Z_{ir}-m_i},
\qquad \log P_{ic}=Z_{ic}-\operatorname{LSE}(Z_{i:}).
$$

Mất mát trung bình theo lô:

$$
J=-\frac1B\sum_{i,c}Y_{ic}\log P_{ic}.
$$

Đạo hàm cục bộ của softmax:

$$
\frac{\partial P_{ir}}{\partial Z_{ic}}=P_{ir}(\delta_{rc}-P_{ic}).
$$

::: derivation Suy diễn chi tiết
Suy gradient theo điểm số cho một mẫu $\ell_i=-\sum_c Y_{ic}\log P_{ic}$ và áp dụng quy tắc chuỗi qua trung gian $P_{ir}$:

$$
\frac{\partial\ell_i}{\partial Z_{ic}}=\sum_r\frac{\partial\ell_i}{\partial P_{ir}}\frac{\partial P_{ir}}{\partial Z_{ic}}
=\sum_r\left(-\frac{Y_{ir}}{P_{ir}}\right)P_{ir}(\delta_{rc}-P_{ic})
=-\sum_rY_{ir}\delta_{rc}+\sum_rY_{ir}P_{ic}.
$$

Vì $Y_{i:}$ là một véc-tơ nhất vị nên $\sum_rY_{ir}\delta_{rc}=Y_{ic}$ và $\sum_rY_{ir}=1$. Do đó:

$$
\frac{\partial\ell_i}{\partial Z_{ic}}=P_{ic}-Y_{ic}.
$$

Gộp cả lô với hệ số trung bình $1/B$:

$$
G_Z=\frac{P-Y}{B}.
$$
:::

Hệ số $1/B$ xuất hiện vì $J$ lấy trung bình theo lô; nếu định nghĩa $J$ là tổng thì không có hệ số này. Không tính $\log(\operatorname{softmax}(Z))$ qua xác suất đã làm tròn; dùng trực tiếp $\log P_{ic}=Z_{ic}-\operatorname{LSE}(Z_{i:})$.

### Ví dụ MLP 2–2–3 xuyên suốt

Dữ kiện:

$$
X=\begin{bmatrix}1&2\\-2&1\end{bmatrix},\quad
Y=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix},
$$

$$
W_1=\begin{bmatrix}1&-1\\1&1\end{bmatrix},\quad b_1=[0,-0.5],
\qquad
W_2=\begin{bmatrix}1&0&-1\\0&1&-1\end{bmatrix},\quad b_2=[0,0,0].
$$

Lan truyền xuôi:

$$
A=\begin{bmatrix}3&0.5\\-1&2.5\end{bmatrix},\quad
H=\begin{bmatrix}3&0.5\\0&2.5\end{bmatrix},\quad
Z=\begin{bmatrix}3&0.5&-3.5\\0&2.5&-2.5\end{bmatrix}.
$$

$$
P\approx\begin{bmatrix}0.9229&0.0758&0.0014\\0.0754&0.9184&0.0062\end{bmatrix},
\qquad J\approx0.0827.
$$

Gradient tại điểm số:

$$
G_Z\approx\begin{bmatrix}-0.0386&0.0379&0.0007\\0.0377&-0.0408&0.0031\end{bmatrix}.
$$

Kiểm tra: tổng mỗi hàng $G_Z$ bằng 0, vì tổng mỗi hàng của $P$ và của $Y$ đều bằng 1.

Kết quả lan truyền ngược, giữ cùng thứ tự lớp:

$$
G_{W_2}\approx\begin{bmatrix}-0.1157&0.1136&0.0021\\0.0750&-0.0830&0.0081\end{bmatrix},\quad
G_{b_2}\approx[-0.0009,-0.0029,0.0038].
$$

$$
G_H\approx\begin{bmatrix}-0.0393&0.0372\\0.0346&-0.0439\end{bmatrix},\quad
G_A\approx\begin{bmatrix}-0.0393&0.0372\\0&-0.0439\end{bmatrix}.
$$

$$
G_{W_1}\approx\begin{bmatrix}-0.0393&0.1249\\-0.0785&0.0305\end{bmatrix},\quad
G_{b_1}\approx[-0.0393,-0.0067].
$$

Mọi gradient được tính bằng cùng bộ tham số cũ (trước khi cập nhật). Với $\eta=0.1$, $(W_1)_{11}$ đổi từ 1 thành khoảng $1.0039$.

![Lan truyền xuôi và ngược qua MLP 2–2–3, thể hiện giá trị các tensor và gradient theo từng lớp.](img/lec-02/mlp-example-backward.svg)

### Một bước huấn luyện và trạng thái

Thứ tự trong một bước: lô mới → xóa gradient cũ → lan truyền xuôi → mất mát → lan truyền ngược → cập nhật. Hai khái niệm phải tách biệt: chế độ mô hình (huấn luyện/suy luận) và việc ghi gradient. Cập nhật tham số chỉ xảy ra trong huấn luyện. Với MLP hiện tại, tầng afin và ReLU không đổi hành vi giữa huấn luyện và suy luận, nhưng khái niệm trạng thái vẫn cần tách.

::: exercise Câu hỏi kiểm tra
Trong một bước huấn luyện, hãy nêu bốn lỗi thường gặp và cách nhận ra chúng từ giá trị/kích thước tensor.
:::

::: solution
Bốn lỗi để tự đối chiếu: (1) softmax tính theo sai trục (không theo trục lớp trong từng hàng); (2) $G_b$ không rút gọn theo trục lô nên kích thước sai; (3) không đặt gradient về 0 trước mỗi lô làm tích lũy sai từ lô trước; (4) cập nhật $W_2$ trước khi tính $G_H$ khiến gradient lớp sau dùng sai tham số.
:::

### Đi sâu thêm

Hàm sigmoid có đạo hàm cục bộ:

$$
\sigma'(a)=\sigma(a)(1-\sigma(a)).
$$

Khi $a$ bão hòa thì tích này nhỏ, nên đạo hàm cục bộ của sigmoid nhỏ. Đây chỉ là quan sát cục bộ; bài này không phân tích sự suy giảm gradient của toàn mạng.

Bộ nhớ là một chi phí thực của lan truyền ngược: phải giữ đầu vào tầng afin, tiền kích hoạt/mặt nạ ReLU và đại lượng cho mất mát. Lưu ít hơn có thể phải tính lại ở bước ngược.

Kiểm tra gradient số bằng sai phân trung tâm:

$$
g_j^{\mathrm{num}}=\frac{J(\theta+\varepsilon e_j)-J(\theta-\varepsilon e_j)}{2\varepsilon}.
$$

So sánh bằng sai số tương đối

$$
\operatorname{err}_{\mathrm{rel}}=
\frac{|g_j^{\mathrm{num}}-g_j|}
{\max(\tau,|g_j^{\mathrm{num}}|+|g_j|)},
$$

trong đó $\tau$ là một số dương nhỏ để xử lý trường hợp cả hai gradient gần 0. Đây là phép kiểm số trên ví dụ đã tính; nên tránh điểm gãy (như đầu vào ReLU bằng 0) và thử vài $\varepsilon$ quanh $10^{-4}$. Với $(W_1)_{11}$, gradient số và gradient giải tích đều xấp xỉ $-0.0392639281$; hiệu tuyệt đối khoảng $5.68\times10^{-11}$ và sai số tương đối khoảng $7.24\times10^{-10}$.

## Từ công thức đến triển khai

Các bước lan truyền xuôi, hàm mất mát, lan truyền ngược và bước cập nhật đã được nối với ký hiệu tensor của ví dụ MLP 2–2–3: $X\to A\to H\to Z\to P\to J$, rồi $G_Z\to G_{W_2},G_{b_2},G_H\to G_{W_1},G_{b_1}$ và cuối cùng cập nhật theo $\theta\leftarrow\theta-\eta G_\theta$. Phép toán được mô tả trực tiếp dưới dạng công thức và kích thước tensor. Buổi 03 tiếp tục các chủ đề tối ưu và huấn luyện.

## Tự kiểm tra

- Đúng đại lượng và kích thước: $G_U$ cùng kích thước với $U$; $G_b$ cộng theo trục lô.
- Kiểm tra các giá trị đã lưu: đầu vào tầng afin, mặt nạ ReLU, nhánh thắng cực đại.
- Cộng đủ các nhánh khi một biến đi vào nhiều cổng.
- Chỉ cập nhật tham số sau khi đủ gradient theo cùng bộ tham số cũ.
- Phân biệt quy ước tổng (entropy chéo theo tổng) và trung bình (theo lô).

## Tài liệu tham khảo

- `lec06_backprop.pdf`, trang chiếu 3–16 và 18–35;
- `lec07_backprop_part2.pdf`, trang chiếu 8–31;
- `lec05_multilayer.pdf`, trang chiếu 28–34;
- `lec04_multiclass.pdf`, trang chiếu 12–19;
- giáo trình PDF 31–32, 68–73, 90–96;
- DOCX `III.2 → Buổi 2`.

Đọc trước theo DOCX: Goodfellow và cộng sự, *Deep Learning*; Zhang và cộng sự, *Dive into Deep Learning*.
