# Buổi 14: Siêu học tập

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- giải thích động lực của siêu học tập và mục tiêu đánh giá sau thích nghi;
- thiết lập một lượt tác vụ với tập hỗ trợ, tập truy vấn và các tham số $N$, $K$, $R$, $B$;
- mô tả mạng Siamese và mạng nguyên mẫu theo biểu diễn, khoảng cách và hàm mất mát;
- truy vết vòng trong, vòng ngoài của MAML và so sánh ba phương pháp trên cùng dữ liệu.

Kiến thức tiên quyết: phân phối xác suất, đạo hàm, quy tắc chuỗi, sigmoid, entropy chéo nhị phân, softmax ổn định, kích thước tensor, phép phát tán và cách chia dữ liệu huấn luyện–kiểm định–kiểm tra. Nội dung bài giảng kéo dài 120 phút; bài tập 50 phút được trình bày riêng ở cuối tài liệu.

## Từ ít mẫu đến phân phối tác vụ

Xét một bài toán có năm lớp ảnh mới, mỗi lớp chỉ có một ảnh có nhãn. Dữ liệu này không đủ để huấn luyện một bộ phân loại mới từ đầu. Mô hình cần tận dụng kinh nghiệm từ nhiều tác vụ trước để thích nghi với tác vụ mới.

Học ít mẫu (few-shot learning) mô tả điều kiện dữ liệu. Học chuyển giao thường bắt đầu bằng tiền huấn luyện trên nguồn dữ liệu lớn rồi mới thích nghi. Siêu học tập (meta-learning) đưa chất lượng sau thích nghi vào chính mục tiêu huấn luyện.

Trong một tác vụ $\mathcal T$, mẫu tuân theo $p_{\mathcal T}(x,y)$. Các tác vụ lại được lấy từ một phân phối:

$$
\mathcal T\sim p(\mathcal T),\qquad (x,y)\sim p_{\mathcal T}(x,y).
$$

Đơn vị huấn luyện là một lượt tác vụ (episode). Mỗi lượt mô phỏng điều kiện sẽ gặp khi đánh giá: một tập nhỏ để thích nghi, sau đó một tập khác để đo chất lượng.

## Hợp đồng của một lượt tác vụ

Với tác vụ $\mathcal T_i$:

- tập hỗ trợ $S_i$ dùng để thích nghi hoặc tạo đại diện lớp;
- tập truy vấn $Q_i$ dùng để tính mục tiêu sau thích nghi;
- hai tập rời nhau theo mẫu: $S_i\cap Q_i=\varnothing$.

Một bài toán $N$ lớp, $K$ mẫu ($N$-way $K$-shot) có $K$ mẫu hỗ trợ cho mỗi lớp. Gọi $R$ là số mẫu truy vấn mỗi lớp và $B$ là số tác vụ trong một lô. Nhãn được đánh lại cục bộ từ $0$ đến $N-1$ trong từng tác vụ.

$$
X^S:[B,N,K,D_x],\qquad X^Q:[B,N,R,D_x],
$$

$$
Y^S:[B,N,K],\qquad Y^Q:[B,N,R].
$$

Không trộn mẫu giữa hai tác vụ khi tạo đại diện lớp hoặc cập nhật vòng trong. Việc chia tác vụ huấn luyện, kiểm định và kiểm tra phụ thuộc câu hỏi đánh giá: có thể tách theo lớp, miền hoặc cá thể tác vụ. Tác vụ kiểm định dùng để chọn siêu tham số; tác vụ kiểm tra chỉ dùng cho đánh giá cuối.

![Một lượt tác vụ tách tập hỗ trợ và tập truy vấn](img/lec-14/episode-contract.svg)

### Ví dụ G

G là một lượt 2 lớp, 2 mẫu: $N=2$, $K=2$, $R=1$, $B=1$. Biểu diễn một chiều được cho sẵn:

| Lớp cục bộ | Hỗ trợ | Truy vấn |
|---|---:|---:|
| A = 0 | $0,2$ | $2{,}5$ |
| B = 1 | $4,6$ | $4{,}5$ |

Các số của G chỉ phục vụ truy vết công thức, không phải kết quả thực nghiệm.

::: exercise Câu hỏi kiểm tra
Với $B=3$, $N=2$, $K=2$, $R=1$, lô có bao nhiêu mẫu hỗ trợ và bao nhiêu mẫu truy vấn?
:::

::: solution
Có $BNK=12$ mẫu hỗ trợ và $BNR=6$ mẫu truy vấn. Mỗi tác vụ vẫn được xử lý riêng.
:::

Với phương pháp tạo trạng thái thích nghi $A_\theta(S)$, mục tiêu chung đo chất lượng của trạng thái đó trên tập truy vấn:

$$
\min_\theta\ \mathbb E_{\mathcal T,S,Q}
\left[\mathcal L^Q_{\mathcal T}\bigl(A_\theta(S)\bigr)\right].
$$

ProtoNet và MAML hiện thực hóa $A_\theta$ theo hai cách khác nhau. Mạng Siamese dưới đây học mất mát theo cặp; muốn dự đoán $N$ lớp còn cần một quy tắc tổng hợp.

## Mạng Siamese: học xác minh từng cặp

Mỗi cặp gồm hai mẫu $(x_i,x_j)$ đi qua cùng bộ mã hóa $f_\theta$. Từ G, có thể tạo cặp cùng lớp $(x_i,x_j)=(2{,}5;2)$ với nhãn $z=1$ và cặp khác lớp $(x_i,x_j)=(2{,}5;4)$ với nhãn $z=0$. Một hàm so sánh sau đó tạo điểm $s_b$.

![Hai nhánh Siamese dùng chung bộ mã hóa](img/lec-14/siamese.svg)

Xác suất cùng lớp của cặp thứ $b$ là

$$
p_b=\sigma(s_b)=P(z_b=1\mid x_i,x_j).
$$

Với $B_p$ cặp, hàm mất mát entropy chéo nhị phân là

$$
\mathcal L_{pair}
=\frac1{B_p}\sum_{b=1}^{B_p}
\left[-z_b\log p_b-(1-z_b)\log(1-p_b)\right].
$$

$B_p$ là số cặp, khác $B$ là số tác vụ. Khi triển khai, hàm mất mát nên nhận trực tiếp điểm $s_b$ để ổn định số. Cách lấy mẫu cặp cũng cần được xác định vì số cặp khác lớp thường lớn hơn số cặp cùng lớp.

Mạng Siamese là một bộ xác minh cặp. Độ chính xác trên cặp không tự tạo thành độ chính xác phân loại $N$ lớp; cần thêm một quy tắc tổng hợp điểm theo lớp.

::: exercise Câu hỏi kiểm tra
Cặp $(2{,}5;2)$ có nhãn nào? Nếu xác suất cùng lớp tăng từ $0{,}6$ lên $0{,}9$, hàm mất mát của cặp tăng hay giảm?
:::

::: solution
Cặp này cùng lớp nên $z=1$. Hàm mất mát giảm từ $-\log 0{,}6$ xuống $-\log 0{,}9$.
:::

## Mạng nguyên mẫu: một đại diện cho mỗi lớp

Mạng nguyên mẫu (Prototypical Network, ProtoNet) mã hóa cả hỗ trợ và truy vấn; $D$ là kích thước biểu diễn nhúng của $f_\theta$ và có thể khác $D_x$:

$$
Z^S=f_\theta(X^S):[B,N,K,D],\qquad
Z^Q=f_\theta(X^Q):[B,N,R,D].
$$

Đại diện của lớp $n$ là trung bình theo đúng trục $K$:

$$
C_{b,n,:}=\frac1K\sum_{k=1}^{K}Z^S_{b,n,k,:},
\qquad C:[B,N,D].
$$

Tập truy vấn không tham gia phép trung bình này. Với G, $c_A=1$ và $c_B=5$.

![Mạng nguyên mẫu mã hóa hỗ trợ, tạo đại diện lớp rồi so khoảng cách](img/lec-14/protonet.svg)

Làm phẳng hai trục truy vấn $N,R$ thành $NR$, rồi phát tán với trục lớp:

$$
[B,NR,1,D]-[B,1,N,D]
\longrightarrow[B,NR,N,D].
$$

Cộng bình phương theo $D$ tạo $d:[B,NR,N]$. Điểm chưa chuẩn hóa là $\ell=-d$, và log-softmax được tính theo trục lớp:

$$
\log P_{b,q,n}
=\ell_{b,q,n}-\log\sum_{n'=1}^{N}\exp(\ell_{b,q,n'}).
$$

Nhãn $Y^Q$ được làm phẳng từ $[B,N,R]$ thành $[B,NR]$ theo đúng thứ tự đã dùng cho $Z^Q$. Sau khi lấy phần tử theo nhãn truy vấn, hàm mất mát lấy trung bình truy vấn trong từng tác vụ rồi trung bình qua $B$ tác vụ:

$$
\mathcal L_{proto}
=\frac1B\sum_{b=1}^{B}\frac1{NR}
\sum_{q=1}^{NR}-\log P_{b,q,Y^Q_{b,q}}.
$$

Đạo hàm đi qua nhánh truy vấn và nhánh hỗ trợ qua phép trung bình tạo đại diện lớp. Không ngắt đạo hàm tại $C$.

### Truy vết G

Với truy vấn A bằng $2{,}5$:

$$
d_A=(2{,}5-1)^2=2{,}25,\qquad
d_B=(2{,}5-5)^2=6{,}25,
$$

$$
P(A\mid2{,}5)
=\frac{e^{-2{,}25}}{e^{-2{,}25}+e^{-6{,}25}}
\approx0{,}9820.
$$

Với truy vấn B bằng $4{,}5$, hai khoảng cách là $12{,}25$ và $0{,}25$, do đó $P(B\mid4{,}5)\approx0{,}999994$. Hàm mất mát của G là

$$
\mathcal L_G
=\frac{-\log 0{,}9820-\log 0{,}999994}{2}
\approx0{,}00908.
$$

::: exercise Câu hỏi kiểm tra
Điều gì sai nếu đưa truy vấn A vào phép trung bình tạo $c_A$?
:::

::: solution
Nhãn truy vấn đã đi vào bước thích nghi. Hợp đồng hỗ trợ–truy vấn bị phá và kết quả đánh giá bị rò rỉ.
:::

## MAML: thích nghi bằng cập nhật tham số

ProtoNet tạo đại diện lớp từ tập hỗ trợ. Siêu học tập bất khả tri mô hình (Model-Agnostic Meta-Learning, MAML) tạo tham số thích nghi $\phi$ bằng một hoặc nhiều bước gradient. Phép thích nghi vì thế cần mô hình và hàm mất mát khả vi theo tham số.

Trên G, dùng bộ phân loại logistic

$$
P_\phi(B\mid h)=\sigma\bigl(w(h-3)+b\bigr),
\qquad \phi=(w,b).
$$

Nhãn A là 0, B là 1; khởi tạo $\theta=(0,0)$ và tốc độ vòng trong $\alpha=1$. Với bốn mẫu hỗ trợ $h=(0,2,4,6)$, nhãn $(0,0,1,1)$:

$$
\nabla_\theta\mathcal L_S(\theta)=(-1,0).
$$

Cập nhật vòng trong chỉ dùng tập hỗ trợ:

$$
\phi=\theta-\alpha\nabla_\theta\mathcal L_S(\theta)
=(1,0).
$$

Với $\phi=(1,0)$, truy vấn A bằng $2{,}5$ có $P(A)\approx0{,}6225$; truy vấn B bằng $4{,}5$ có $P(B)\approx0{,}8176$. Cả hai đúng lớp và

$$
\mathcal L_Q(\phi)
=-\frac12\left[\log 0{,}6225+\log 0{,}8176\right]
\approx0{,}3377.
$$

![Vòng trong thích nghi trên hỗ trợ và vòng ngoài tối ưu trên truy vấn](img/lec-14/maml-loop.svg)

## Mục tiêu vòng ngoài và đạo hàm siêu cấp

Với một lô $B$ tác vụ:

$$
\phi_i=\theta-\alpha\nabla_\theta\mathcal L_{S_i}(\theta),
\qquad
\mathcal L_{meta}=\frac1B\sum_{i=1}^{B}\mathcal L_{Q_i}(\phi_i).
$$

Mỗi $\mathcal L_{Q_i}$ đã là trung bình các truy vấn trong tác vụ $i$. Một bước huấn luyện gồm:

1. lấy một lô tác vụ và đặt gradient vòng ngoài về 0;
2. tạo bản sao $\phi_i^0=\theta$ cho từng tác vụ;
3. tính mất mát hỗ trợ và cập nhật $\phi_i$ khả vi;
4. tính mất mát truy vấn bằng $\phi_i$;
5. trung bình qua tác vụ, lan truyền ngược và cập nhật $\theta$.

$\phi_i$ là trạng thái tạm thời của tác vụ, không phải tham số lâu dài trong bộ tối ưu vòng ngoài. MAML chính xác lấy đạo hàm qua quan hệ $\theta\to\phi_i(\theta)\to\mathcal L_{Q_i}$. Với một bước cập nhật, Jacobian có dạng $\partial\phi_i/\partial\theta=I-\alpha H_i$, trong đó $H_i$ là Hessian của mất mát hỗ trợ. MAML bậc nhất (FO-MAML) dùng xấp xỉ

$$
\frac{\partial\phi_i}{\partial\theta}\approx I,
$$

tức bỏ hạng $\alpha H_i$ nhưng vẫn giữ $\nabla_{\phi_i}\mathcal L_{Q_i}$.

Ở tác vụ kiểm tra mới, sao chép $\theta$, chỉ dùng hỗ trợ để tạo $\phi_{test}$, rồi đánh giá truy vấn. Dùng nhãn truy vấn trong vòng trong là rò rỉ trong tác vụ; dùng tác vụ kiểm tra để chọn $\alpha$, kiến trúc hoặc điểm lưu mô hình là rò rỉ qua tác vụ.

::: exercise Câu hỏi kiểm tra
Tại sao không được cập nhật trực tiếp $\theta$ bằng mất mát hỗ trợ của từng tác vụ trong lô?
:::

::: solution
Mỗi tác vụ cần một $\phi_i$ riêng cùng xuất phát từ $\theta$. Sửa $\theta$ tại chỗ làm các tác vụ phụ thuộc thứ tự và phá mục tiêu trung bình truy vấn qua tác vụ.
:::

## So sánh ba phương pháp

Ba phương pháp dùng tập hỗ trợ để tạo ba dạng trạng thái khác nhau.

| Phương pháp | Trạng thái sau hỗ trợ | Dự đoán truy vấn | Đường đạo hàm khi huấn luyện |
|---|---|---|---|
| Siamese | Tham số chung không đổi; hỗ trợ là tập tham chiếu | Điểm từng cặp; cần quy tắc tổng hợp cho $N$ lớp | Từ mất mát cặp |
| ProtoNet | Đại diện lớp $C$ | Softmax theo khoảng cách | Qua truy vấn và đại diện hỗ trợ |
| MAML | Tham số thích nghi $\phi$ | Bộ phân loại $f_\phi$ | Qua cập nhật vòng trong |

Trên tác vụ mới, Siamese phải mã hóa các cặp cần so sánh; ProtoNet mã hóa, lấy trung bình và tính khoảng cách; MAML cần lan truyền xuôi–ngược trên hỗ trợ trước khi dự đoán truy vấn. Lựa chọn phụ thuộc cấu trúc tác vụ và ngân sách thích nghi, không có phương pháp luôn tốt hơn.

## Phần mở rộng

### Ví dụ I: MAML chính xác và MAML bậc nhất

Một ví dụ vô hướng tách MAML chính xác khỏi FO-MAML. Cho $f_\theta(x)=\theta x$, mẫu hỗ trợ $(1,2)$, mẫu truy vấn $(2,4)$, mất mát nửa bình phương, $\theta=0$ và $\alpha=0{,}5$. Khi đó

$$
\nabla_\theta\mathcal L_S=-2,\qquad
\nabla^2_\theta\mathcal L_S=1,\qquad
\phi=1,\qquad
\nabla_\phi\mathcal L_Q=-4.
$$

Đạo hàm siêu cấp chính xác là $(1-0{,}5\cdot1)(-4)=-2$, còn FO-MAML cho $-4$. Khi tham số có nhiều chiều, phép tính chính xác chỉ cần tích Hessian–vector; không cần dựng toàn bộ ma trận Hessian.

### Gợi ý ít mẫu

Gợi ý ít mẫu (few-shot prompting) đưa ví dụ vào ngữ cảnh đầu vào và thường không cập nhật trọng số. Siêu học tập ít mẫu dùng tập hỗ trợ có nhãn để tạo đại diện hoặc cập nhật tham số. Hai khái niệm không đồng nhất.

### Thay đổi số mẫu hỗ trợ

Nếu $K$ lúc kiểm tra khác $K$ lúc huấn luyện, cấu trúc lượt tác vụ đã đổi; hiệu quả cần được đánh giá riêng theo từng $K$.

### Vùng địa lý như một tác vụ

Trong bài toán lớp phủ đất, có thể xem mỗi vùng địa lý là một tác vụ: dữ liệu ít mẫu có nhãn của vùng mới là hỗ trợ, còn ảnh còn lại là truy vấn. Cách đóng khung này không tự tạo ra kết luận về hiệu năng.

## Tổng hợp

Siêu học tập tối ưu chất lượng sau thích nghi trên một phân phối tác vụ. Tập hỗ trợ tạo trạng thái thích nghi; tập truy vấn đo trạng thái đó. Siamese học xác minh cặp, ProtoNet tạo đại diện lớp, còn MAML cập nhật tham số. So sánh hợp lệ phải giữ nguyên lượt tác vụ, phép chia tác vụ và ngân sách thích nghi.

## Bài tập 50 phút

1. Trong 10 phút, xác định $N$, $K$, $R$, $B$, tập hỗ trợ, tập truy vấn và một phép chia tác vụ hợp lệ.
2. Trong 15 phút, giữ $c_A=1$, $c_B=5$ nhưng thay truy vấn bằng $3$; tính khoảng cách, log-softmax và hàm mất mát nếu nhãn đúng là A.
3. Trong 15 phút, dùng lại bộ phân loại logistic của G với $\alpha=0{,}5$; tính $\phi$, mất mát truy vấn và viết mục tiêu vòng ngoài của MAML.
4. Trong 10 phút, so sánh ProtoNet với MAML theo trạng thái thích nghi, đường đạo hàm và chi phí trên tác vụ mới.

## Nguồn

- Stanford CS330, *Optimization-Based Meta-Learning*, PDF 4–24; tình huống mở rộng PDF 26–31.
- Stanford CS330, *Metric-Based Meta-Learning*, PDF 4–17 và 34–37.
- Berkeley CS294-112, *Meta-Learning*, PDF 4–5 và 18–23.
- Stanford CS330, *Homework 2: ProtoNet and MAML*, PDF 1–9.
- `source-materials/textbooks/hocsau_draft.pdf`, PDF 288–293.
