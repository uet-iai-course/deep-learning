# Buổi 03 — Tối ưu hóa mạng nơ-ron đa lớp

## Mục tiêu và kiến thức tiên quyết

Sau khi hoàn thành buổi này, người học có thể:

- đọc đường cong huấn luyện/xác thực, nhận ra bốn dấu hiệu bất thường và đề xuất một phép kiểm tra nhỏ cho từng dấu hiệu;
- phân biệt ba lớp vấn đề: lỗi số học, gradient triệt tiêu hoặc bùng nổ và quá khớp;
- tính một bước cập nhật SGD, Mômen, RMSprop và Adam từ trạng thái đã cho;
- chọn khởi tạo Glorot/Xavier hoặc Kaiming dựa trên giả thiết về kích hoạt;
- giải thích điều chuẩn L2, L1 và dropout kèm điều kiện áp dụng;
- tính chuẩn hóa theo lô cho tensor $B\times D$ và phân biệt chế độ huấn luyện với suy luận;
- thiết kế so sánh cấu hình bằng tập xác thực rồi khóa tập kiểm tra cho lần đánh giá cuối.

Kiến thức tiên quyết gồm đại số tuyến tính, giải tích (đạo hàm, quy tắc chuỗi), xác suất, Python và học máy nhập môn (hàm mất mát, hạ gradient, tập huấn luyện/xác thực/kiểm tra). Buổi này dùng các quy ước tensor: ma trận trọng số $W\in\mathbb R^{n_{out}\times n_{in}}$, dữ liệu một lô $X\in\mathbb R^{B\times D}$ với trục đầu luôn là chiều lô $B$.

## Ký hiệu và quy ước

Các ký hiệu dùng trong toàn buổi:

- $w_t$: vector tham số tại bước $t$; $g_t=\nabla_w L_{\mathcal B_t}(w_{t-1})$: gradient trung bình trên lô nhỏ $\mathcal B_t$.
- $\eta_t$: tốc độ học; $B$: kích thước lô; $D$: số đặc trưng.
- $P$: số tham số vô hướng của mô hình, với $w\in\mathbb R^P$; $\varepsilon>0$: hằng số nhỏ tránh chia cho số gần 0.
- $u_t$: vận tốc Mômen; $s_t$: trung bình trượt của $g_t\odot g_t$ trong RMSprop.
- $m_t,v_t$: mômen bậc một và bậc hai trong Adam; $\hat m_t,\hat v_t$: các giá trị sau hiệu chỉnh độ chệch.
- $\lambda$: hệ số điều chuẩn trong công thức L1/L2 đang xét; $0\le p<1$: xác suất bỏ đơn vị trong dropout.
- $X\in\mathbb R^{B\times D}$, $\mu_{\mathcal B},\sigma^2_{\mathcal B},\gamma,\beta\in\mathbb R^D$: các đại lượng trong chuẩn hóa theo lô.
- $L_{data}$: mất mát dữ liệu trên tập huấn luyện; $L_{\mathcal B_t}$ là ước lượng trên lô nhỏ tại bước $t$.
- $w^*$ và $H_{ii}$: điểm cực tiểu cục bộ cùng phần tử đường chéo Hessian trong xấp xỉ L1.
- $\theta$: tham số mô hình; $c\in\mathcal C$: một cấu hình trong miền cấu hình được so sánh.

Phân biệt bốn nhóm: tham số (được cập nhật bởi bộ tối ưu), trạng thái bộ tối ưu (vận tốc, trung bình trượt), siêu tham số (tốc độ học, hệ số mômen, hệ số điều chuẩn) và chế độ mô hình (huấn luyện hoặc suy luận). Quy ước phát rộng: mọi vector chiều $D$ được phát rộng theo hàng trong tensor $B\times D$.

## Khái niệm trọng tâm

### 1. Chẩn đoán trước khi chọn kỹ thuật

Một giá trị mất mát cuối không đủ để ra quyết định. Đường cong huấn luyện/xác thực chỉ tạo giả thuyết; cần một phép kiểm tra nhỏ để xác nhận hoặc loại bỏ giả thuyết đó. Bảng dưới tóm tắt bốn dấu hiệu thường gặp, nguyên nhân hợp lý và phép kiểm tra tương ứng.

| Dấu hiệu | Nguyên nhân hợp lý | Phép kiểm tra nhỏ |
|---|---|---|
| Mất mát không đổi từ sớm | Tốc độ học quá nhỏ; khởi tạo kém làm gradient rất nhỏ | Kiểm tra chuẩn gradient $\lVert g_t\rVert$ và độ chênh tham số $\lVert w_t-w_{t-1}\rVert$ sau vài bước |
| Mất mát tăng hoặc thành NaN | Tốc độ học quá lớn; lỗi số học (tràn số) trong tầng tính toán | Kiểm tra giá trị hữu hạn và độ lớn của kích hoạt/gradient theo từng tầng |
| Dao động theo chu kỳ | Thứ tự xáo trộn lô không ngẫu nhiên; phân bố dữ liệu giữa các lô không đều | Kiểm tra thứ tự và cách xáo trộn lô, so sánh với chạy trên lô ngẫu nhiên |
| Huấn luyện giảm nhưng xác thực tăng | Quá khớp; cách tách tập xác thực hoặc tiền xử lý lệch pha | Kiểm tra quy trình xác thực và tiền xử lý trên cả hai tập |

![Bốn dạng đường cong mất mát: không đổi, tăng, dao động chu kỳ và tách giữa huấn luyện với xác thực.](img/lec-03/curve-diagnostics.svg)

![Phân biệt chưa hội tụ và quá khớp qua khoảng cách giữa đường huấn luyện và xác thực.](img/lec-03/train-validation-gap.svg)

Chưa hội tụ nghĩa là bài toán tối ưu chưa đạt trạng thái mong muốn trên chính tập huấn luyện, nên mất mát huấn luyện còn cao. Quá khớp nghĩa là mô hình khớp tốt tập huấn luyện nhưng không khái quát sang dữ liệu chưa thấy, nên mất mát xác thực tăng. Hai trường hợp cần can thiệp khác nhau: chưa hội tụ thường điều chỉnh bộ tối ưu, tốc độ học hoặc khởi tạo; quá khớp thường thêm điều chuẩn hoặc giảm dung lượng mô hình.

::: exercise Câu hỏi kiểm tra
Trên hình, mất mát huấn luyện giảm đều nhưng mất mát xác thực giữ nguyên rồi tăng nhẹ từ giữa quá trình. Trước khi thay cấu hình, cần làm phép kiểm tra nào để xác nhận giả thuyết?
:::

::: hint
Xét độ lệch giữa hai tập đến từ dữ liệu hay từ quá trình huấn luyện. Đối chiếu quy trình tách tập xác thực và tiền xử lý.
:::

::: solution
Giả thuyết nghiêng về quá khớp. Kiểm tra quy trình tách tập xác thực: đối chiếu phân bố nhãn, thứ tự dữ liệu và tiền xử lý giữa huấn luyện với xác thực. Nếu tập xác thực được lấy từ cửa sổ dữ liệu khác biệt, độ chênh có thể do quy trình chứ không phải quá khớp. Sau khi khớp quy trình, so sánh lại đường cong.
:::

### 2. SGD, tốc độ học và ổn định

SGD duyệt từng lô nhỏ. Gradient trung bình trên lô và bước cập nhật:

$$
g_t=\frac1B\sum_{i\in\mathcal B_t}\nabla_w\ell_i(w_{t-1}),\qquad
w_t=w_{t-1}-\eta_t g_t.
$$

Tốc độ học quá lớn làm tham số rời khỏi vùng thuận lợi, mất mát có thể tăng hoặc thành NaN. Tốc độ học quá nhỏ làm hội tụ chậm, dễ nhầm với tình trạng mất mát không đổi. Lịch tốc độ học làm giảm $\eta_t$ theo bước $t$; các dạng phổ biến gồm giảm theo cấp số, tỉ lệ nghịch, tuyến tính, cosin $\eta_t=\frac{\eta_0}{2}(1+\cos(\pi t/T))$ với $0\le t\le T$, giảm sau mỗi $K$ bước với $K\in\mathbb N_{>0}$ và tăng ấm ở giai đoạn đầu. Không có lịch nào luôn vượt trội; việc chọn phụ thuộc bài toán và ngân sách.

![Ba chế độ tốc độ học: quá nhỏ, phù hợp và quá lớn.](img/lec-03/learning-rate-regimes.svg)

**Ổn định số học.** Gradient lan qua chuỗi Jacobian qua nhiều tầng: chuẩn của tích các ma trận Jacobian có thể co lại hoặc phóng đại theo số tầng. Đây là điều kiện dẫn tới gradient triệt tiêu hoặc bùng nổ, không phải kết luận rằng mọi mạng sâu đều gặp trường hợp đó.

![Chuỗi Jacobian cho thấy gradient có thể co hoặc phóng đại qua nhiều tầng.](img/lec-03/jacobian-chain.svg)

Về mặt ổn định số, không tính $\log(\operatorname{softmax}(z))$ qua xác suất đã làm tròn vì tầng số mũ dễ tràn. Cách ổn định là trừ $m=\max_j z_j$ trước phép lũy thừa: $\log\sum_j e^{z_j}=m+\log\sum_j e^{z_j-m}$.

::: exercise Câu hỏi kiểm tra
Vì sao viết $\log(\operatorname{softmax}(z)_i)=z_i-\log\sum_j e^{z_j}$ theo dạng log-sum-exp (có trừ đi $m=\max_j z_j$) lại ổn định về số hơn so với tính thương $e^{z_j}/\sum_j e^{z_j}$ rồi lấy log khi $z$ có phần tử rất lớn?
:::

::: hint
So sánh độ lớn của $e^{z_j}$ trước và sau khi trừ $m=\max_j z_j$.
:::

::: solution
Khi $z$ có phần tử rất lớn, $e^{z_j}$ có thể tràn số. Trừ $m=\max_j z_j$ khiến mọi số mũ thành $z_j-m\le0$, nên $e^{z_j-m}\le1$, tránh tràn. Đẳng thức $\log\sum_j e^{z_j}=m+\log\sum_j e^{z_j-m}$ thu hồi đúng kết quả, vì vậy thương và log sau đó tính ổn định hơn.
:::

::: exercise Câu hỏi kiểm tra
Giải thích vì sao chuỗi Jacobian qua chiều sâu có thể dẫn tới gradient triệt tiêu hoặc bùng nổ, và vì sao đó là điều kiện chứ không phải kết luận cho mọi kiến trúc.
:::

::: hint
Xét tác động tích lũy khi nhiều tầng liên tiếp co hoặc khuếch đại tín hiệu gradient.
:::

::: solution
Gradient lan ngược là tích các ma trận Jacobian qua từng tầng. Chuẩn của tích bị chặn trên bởi tích các chuẩn thành phần; tác động thực tế còn phụ thuộc hướng của gradient. Nếu nhiều tầng liên tiếp làm co tín hiệu, gradient có thể triệt tiêu; nếu nhiều tầng liên tiếp khuếch đại tín hiệu, gradient có thể bùng nổ. Đây là điều kiện tiềm năng chứ không phải tuyên bố chắc chắn cho mọi mạng.
:::

### 3. Khởi tạo

Khởi tạo toàn 0 giữ tính đối xứng: nếu các đơn vị trong cùng một tầng có cùng đường vào, cùng đường ra và cùng tín hiệu ngược, thì ở mọi bước chúng nhận gradient giống nhau và mãi giữ giá trị giống nhau, nên mạng không tách được các đơn vị. Với quy ước $W\in\mathbb R^{n_{out}\times n_{in}}$, phương sai của một phần tử khởi tạo:

$$
\operatorname{Var}(W_{ij})=\frac{2}{n_{in}+n_{out}}\quad\text{(Xavier/Glorot)},
$$

$$
\operatorname{Var}(W_{ij})=\frac{2}{n_{in}}\quad\text{(Kaiming cho ReLU)}.
$$

Xavier/Glorot phù hợp giả thuyết kích hoạt gần tuyến tính và yêu cầu cân bằng lượt xuôi/ngược. Kaiming dành cho ReLU vì ReLU chặn một phần tín hiệu, nên cần phương sai lớn hơn để bù. Đây là quy tắc khởi tạo, không phải bảo đảm hội tụ.

![So sánh phương sai khởi tạo Xavier và Kaiming theo số kết nối vào, ra.](img/lec-03/initialization-variance.svg)

::: exercise Câu hỏi kiểm tra
Một tầng dùng kích hoạt ReLU có $n_{in}=512,n_{out}=512$. Chọn khởi tạo nào hợp lý và phương sai của một trọng số là bao nhiêu? Nêu giả thiết về kích hoạt được dùng để kết luận.
:::

::: hint
Kích hoạt ReLU chặn một phần tín hiệu; đối chiếu công thức Kaiming.
:::

::: solution
Do dùng ReLU, chọn khởi tạo Kaiming với giả thiết ReLU chặn một phần tín hiệu; phương sai $\operatorname{Var}(W_{ij})=2/n_{in}=2/512=1/256$. Đây là quy tắc khởi tạo, không phải bảo đảm hội tụ.
:::

### 4. Bộ tối ưu theo cùng một ví dụ

Điều kiện kém tạo đường đi răng cưa vì gradient biến thiên mạnh theo trục. Điểm yên và vùng gradient gần bằng 0 khi chưa đạt cực tiểu mong muốn có thể làm bước cập nhật chậm lại. Đây là các cơ chế có thể xảy ra, không phải nguồn duy nhất trong mọi bài toán.

![Đường đồng mức minh họa điều kiện kém, điểm yên và cực tiểu cục bộ.](img/lec-03/optimization-landscape.svg)

![Bước Mômen là tổng của vận tốc cũ và bước theo gradient hiện tại.](img/lec-03/momentum-vectors.svg)

**Mômen.** Mômen tích lũy vận tốc cũ làm êm đường đi và giúp vượt qua điểm yên:

$$
u_t=\beta u_{t-1}-\eta g_t,\qquad w_t=w_{t-1}+u_t.
$$

Ví dụ tính tay: $w_0=(1,-1)$, $u_0=(0,0)$, $\beta=0.9$, $\eta=0.1$, $g_1=(2,0.5)$, $g_2=(2,-0.5)$.

- Bước 1: $u_1=0.9(0,0)-0.1(2,0.5)=(-0.2,-0.05)$; $w_1=(1,-1)+u_1=(0.8,-1.05)$.
- Bước 2: $u_2=0.9(-0.2,-0.05)-0.1(2,-0.5)=(-0.38,0.005)$; $w_2=(0.8,-1.05)+u_2=(0.42,-1.045)$.

Mômen giữ một trạng thái vận tốc trên mỗi tham số, tức $P$ giá trị cho vector $w\in\mathbb R^P$.

**RMSprop.** Chia gradient cho trung bình trượt của bình phương gradient, phép toán theo phần tử:

$$
s_t=\beta s_{t-1}+(1-\beta)g_t\odot g_t,\qquad w_t=w_{t-1}-\eta\frac{g_t}{\sqrt{s_t}+\varepsilon}.
$$

Ví dụ tính tay: $w_0=(1,-1)$, $g_1=(2,0.5)$, $s_0=0$, $\beta=0.9$, $\eta=0.1$. Tạm bỏ $\varepsilon$ trong phép tính nhẩm: $s_1=0.9(0,0)+0.1(4,0.25)=(0.4,0.025)$; $w_1=(1,-1)-0.1\cdot(2/\sqrt{0.4},\,0.5/\sqrt{0.025})\approx(1,-1)-(0.3162,0.3162)=(0.6838,-1.3162)$. Khi triển khai luôn dùng $\varepsilon>0$. Chia theo trục gradient lớn giúp làm giảm bước trên trục đó, xử lý đường đi răng cưa.

**Adam.** Kết hợp mômen bậc một (như Mômen) và trung bình trượt bình phương (như RMSprop), kèm hiệu chỉnh độ chệch vì $m_0=v_0=0$:

$$
m_t=\beta_1 m_{t-1}+(1-\beta_1)g_t,\qquad v_t=\beta_2 v_{t-1}+(1-\beta_2)g_t\odot g_t,
$$

$$
\hat m_t=\frac{m_t}{1-\beta_1^t},\qquad \hat v_t=\frac{v_t}{1-\beta_2^t},\qquad w_t=w_{t-1}-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\varepsilon}.
$$

Ví dụ tính tay: cùng $w_0=(1,-1)$, $g_1=(2,0.5)$, $\eta=0.1$, $m_0=v_0=0$, $\beta_1=0.9$, $\beta_2=0.999$, tạm bỏ $\varepsilon$. $m_1=(0.2,0.05)$, $v_1=(0.004,0.00025)$; $\hat m_1=(0.2,0.05)/(0.1)=(2,0.5)$, $\hat v_1=(0.004,0.00025)/(0.001)=(4,0.25)$; $w_1=(1,-1)-0.1\cdot(2/2,\,0.5/0.5)=(0.9,-1.1)$. Khi triển khai luôn dùng $\varepsilon>0$.

Trạng thái trên mỗi tham số: SGD $0$; Mômen $P$; RMSprop $P$; Adam $2P$ cộng bộ đếm bước $t$ (cần cho hiệu chỉnh độ chệch). Không kết luận bộ tối ưu nào luôn tốt hơn; việc chọn phụ thuộc bài toán và giao thức so sánh.

::: exercise Câu hỏi kiểm tra
So sánh cơ chế và trạng thái của Mômen với Adam trong một bước cập nhật. Nêu điều kiện giao thức cần thiết để so sánh chúng đúng cách.
:::

::: hint
Xét số trạng thái giữ trên mỗi tham số, bộ đếm bước, và yêu cầu giữ cố định dữ liệu, hạt giống ngẫu nhiên, ngân sách cập nhật và tiêu chí đánh giá.
:::

::: solution
Mômen giữ một trạng thái $u_t\in\mathbb R^P$, cập nhật $w_t=w_{t-1}+u_t$ với $u_t=\beta u_{t-1}-\eta g_t$. Adam giữ hai trạng thái $m_t,v_t\in\mathbb R^P$ cộng bộ đếm bước; sau hiệu chỉnh độ chệch cập nhật $w_t=w_{t-1}-\eta\hat m_t/(\sqrt{\hat v_t}+\varepsilon)$. Để so sánh đúng, giữ cùng mô hình, dữ liệu, tiền xử lý, ngân sách cập nhật, tiêu chí và hạt giống/số lần chạy; không kết luận bộ nào luôn hơn.
:::

### 5. Từ tối ưu sang tổng quát hóa và điều chuẩn

Mất mát huấn luyện thấp không bảo đảm mất mát xác thực thấp. Điều chuẩn thay đổi bài toán hoặc quá trình huấn luyện để giảm sai số tổng quát hóa, có thể làm mất mát huấn luyện tăng.

Gradient của mất mát dữ liệu được ký hiệu $g_{data}=\nabla L_{data}$.

**L2.**

$$
\widetilde J(w)=L_{data}(w)+\frac\lambda2\lVert w\rVert_2^2,
$$

$$
w_t=(1-\eta\lambda)w_{t-1}-\eta\nabla L_{data}(w_{t-1}).
$$

Với $0\le\eta\lambda\le1$, số hạng $(1-\eta\lambda)w_{t-1}$ được gọi là hiệu ứng *co trọng số*. Ví dụ: $\eta=0.1$, $\lambda=0.05$, $w=(2,-1)$, $g_{data}=(0.4,-0.2)$ cho $w^+=(1-0.005)(2,-1)-0.1(0.4,-0.2)=(1.95,-0.975)$.

Với SGD thuần, điều chuẩn L2 tạo đúng hệ số co trọng số trên. Với bộ tối ưu có trạng thái tích lũy hoặc điều chỉnh theo từng tọa độ, điều chuẩn L2 và suy giảm trọng số tách rời không còn là cùng một phép cập nhật; không được suy rộng đẳng thức của SGD sang mọi bộ tối ưu.

**L1.**

$$
\widetilde J(w)=L_{data}(w)+\lambda\lVert w\rVert_1,\qquad
\partial|w_i|=\begin{cases}\{1\},&w_i>0,\\[-2pt]\{-1\},&w_i<0,\\[-2pt][-1,1],&w_i=0.\end{cases}
$$

Với $w=(2,-0.5,0)$, $\lambda=0.1$, đóng góp dưới gradient của hạng phạt là $(0.1,-0.1,0.1s)$ với $s\in[-1,1]$. L1 có thể khuyến khích tham số thưa (nhiều phần tử về 0). Nghiệm ngưỡng mềm dưới đây chỉ đúng trong xấp xỉ bậc hai cục bộ quanh $w^*$ với Hessian chéo $H_{ii}>0$; ngưỡng là $\lambda/H_{ii}$. Với $\lambda=0.2$, $H_{ii}=0.5$ cho ngưỡng $0.4$: $0.3\mapsto0$, $-0.9\mapsto-0.5$. Đây không phải nghiệm đóng tổng quát cho mạng sâu.

**Dropout đảo tỷ lệ.**

$$
h^{tr}=\frac{m\odot h}{1-p},\qquad m_j\sim\operatorname{Bernoulli}(1-p),\qquad h^{eval}=h.
$$

Ta có $\mathbb E[m]=1-p$ nên $\mathbb E[h^{tr}]=h$; mặt nạ cùng kích thước với kích hoạt; mỗi bước huấn luyện dùng một mặt nạ mới; khi suy luận dùng ánh xạ đồng nhất. Ví dụ $h=(2,-1,4)$, $p=0.5$, $m=(1,0,1)$ cho $h^{tr}=(2/0.5,\,0,\,4/0.5)=(4,0,8)$.

![Dropout bỏ ngẫu nhiên đơn vị khi huấn luyện và dùng đủ đơn vị khi suy luận.](img/lec-03/dropout-network.svg)

::: exercise Câu hỏi kiểm tra
Vì sao đảo tỷ lệ (chia cho $1-p$) giữ $\mathbb E[h^{tr}]=h$, cho phép dùng kích hoạt ban đầu khi đánh giá?
:::

::: hint
Dùng $\mathbb E[m_j]=1-p$ và tính kỳ vọng theo từng phần tử.
:::

::: solution
Do $m_j\sim\operatorname{Bernoulli}(1-p)$, kỳ vọng $\mathbb E[m]=1-p$. Vậy $\mathbb E[m\odot h]/(1-p)=h$. Khi suy luận, dùng $h^{eval}=h$ cho kết quả tương ứng với kỳ vọng của phép dropout, không cần điều chỉnh tỷ lệ.
:::

### 6. Chuẩn hóa theo lô

Dropout tạo nhiễu có chủ đích trên kích hoạt. Qua quá trình huấn luyện, thang của kích hoạt cũng có thể thay đổi giữa các lô; chuẩn hóa theo lô kiểm soát thang này bằng thống kê theo từng đặc trưng.

Với $X\in\mathbb R^{B\times D}$, chuẩn hóa theo trục lô:

$$
\mu_{\mathcal B}=\frac1B\sum_i X_{i:},\qquad
\sigma^2_{\mathcal B}=\frac1B\sum_i (X_{i:}-\mu_{\mathcal B})^2,
$$

$$
\widehat X=\frac{X-\mu_{\mathcal B}}{\sqrt{\sigma^2_{\mathcal B}+\varepsilon}},\qquad Y=\gamma\odot\widehat X+\beta.
$$

Mọi vector chiều $D$ được phát rộng theo hàng. Ví dụ $X=[[1,3],[3,7]]$ với $\varepsilon=0$: $\mu=(2,5)$, $\sigma^2=(1,4)$, $\widehat X=[[-1,-1],[1,1]]$; với $\gamma=(2,0.5)$, $\beta=(1,-1)$ cho $Y=[[-1,-1.5],[3,-0.5]]$. Thực tế phải dùng $\varepsilon>0$ để tránh chia cho 0.

- Huấn luyện: dùng thống kê lô $\mu_{\mathcal B},\sigma^2_{\mathcal B}$ và đồng thời cập nhật thống kê chạy để dùng lúc suy luận.
- Suy luận: dùng thống kê cố định ước lượng từ huấn luyện, không dùng thống kê lô.
- $\gamma,\beta$ dùng ở cả hai chế độ. Công thức cập nhật thống kê chạy phụ thuộc thư viện; khi triển khai cần ghi rõ lựa chọn đang dùng.
- Trong MLP, thứ tự triển khai của ví dụ này là tầng afin → chuẩn hóa theo lô → hàm kích hoạt; $\gamma,\beta$ là tham số học được.

![Luồng chuẩn hóa theo lô từ thống kê từng đặc trưng đến phép tỷ lệ và dịch.](img/lec-03/batchnorm-flow.svg)

![Chuẩn hóa theo lô dùng thống kê lô khi huấn luyện và thống kê chạy khi suy luận.](img/lec-03/batchnorm-train-eval.svg)

Giải thích “dịch chuyển hiệp biến nội bộ” về nguồn gốc của chuẩn hóa theo lô chỉ là trực giác lịch sử, không phải kết luận chặt chẽ.

::: exercise Câu hỏi kiểm tra
Cho $X\in\mathbb R^{4\times 3}$ là một lô huấn luyện. Xác định kích thước của $\mu_{\mathcal B},\sigma^2_{\mathcal B},\gamma,\beta$ và phân biệt nguồn thống kê dùng trong huấn luyện với suy luận của chuẩn hóa theo lô.
:::

::: hint
Mỗi đặc trưng có một thống kê; trục lô chỉ là trục được rút gọn.
:::

::: solution
Các đại lượng $\mu_{\mathcal B},\sigma^2_{\mathcal B},\gamma,\beta\in\mathbb R^3$ (một giá trị cho mỗi đặc trưng) và được phát rộng theo hàng trên lô. Huấn luyện dùng thống kê lô và cập nhật thống kê chạy; suy luận dùng thống kê cố định ước lượng từ huấn luyện, không dùng lô; $\gamma,\beta$ dùng ở cả hai chế độ.
:::

### 7. Chọn siêu tham số

Giao thức gồm hai vòng và một bước khóa đánh giá:

1. **Vòng trong:** với mỗi cấu hình $c\in\mathcal C$, huấn luyện để được $\theta^*(c)$ trên tập huấn luyện.
2. **Vòng ngoài:** chọn $c^*$ có kết quả xác thực tốt nhất.
3. **Khóa đánh giá:** khóa quy trình, cấu hình và điểm lưu tại cấu hình đã chọn; đánh giá trên tập kiểm tra một lần duy nhất.

Phải giữ cùng mô hình, dữ liệu, tiền xử lý, ngân sách cập nhật (số bước/vòng huấn luyện), tiêu chí và hạt giống/số lần chạy khi nguồn có. Không dùng tập kiểm tra để tinh chỉnh; tập này chỉ dùng cho lần đánh giá cuối.

### 8. Mở rộng triển khai

Các điều kiện dưới đây bổ sung cho giao thức chọn cấu hình ở mục 7 và giúp phép so sánh có thể tái lập.

**Tăng cường dữ liệu.** Chỉ dùng phép biến đổi giữ nguyên nhãn của bài toán. Lật ảnh có thể hợp lệ với một số lớp vật thể nhưng sai với chữ viết hoặc biển báo; điều kiện giữ nhãn phải được kiểm tra trước khi đưa phép biến đổi vào quy trình.

![Ví dụ các phép biến đổi tăng cường dữ liệu và điều kiện giữ nhãn.](img/lec-03/augmentation-transformations.svg)

**Tiền xử lý.** Ước lượng mọi thống kê tiền xử lý trên tập huấn luyện, rồi dùng chính các thống kê đã cố định đó cho tập xác thực và kiểm tra. Ước lượng lại từ tập xác thực hoặc kiểm tra làm rò rỉ thông tin.

**Kiểm kê cấu hình.** Với mỗi $c\in\mathcal C$, ghi lại bộ tối ưu, lịch tốc độ học, khởi tạo, điều chuẩn, chế độ chuẩn hóa, ngân sách cập nhật và hạt giống. Một so sánh không truy nguyên được cấu hình không đủ để chọn siêu tham số.

**Chuẩn hóa theo lô và theo tầng.** Chuẩn hóa theo lô (BN) rút gọn theo chiều lô; chuẩn hóa theo tầng (LN) rút gọn theo chiều đặc trưng của từng mẫu. So sánh ở đây chỉ nói về trục chuẩn hóa, không suy ra phương pháp nào luôn tốt hơn.

![Các trục được rút gọn trong chuẩn hóa theo lô và chuẩn hóa theo tầng.](img/lec-03/normalization-axes.svg)

## Từ công thức đến triển khai

Với tensor $X\in\mathbb R^{B\times D}$, mọi vector chiều $D$ được phát rộng theo hàng. Các ví dụ bộ tối ưu, L2 và L1 áp dụng theo phần tử; dropout nhân mặt nạ cùng kích thước với kích hoạt rồi chia cho $1-p$; chuẩn hóa theo lô tính thống kê theo chiều lô rồi phát rộng. Chuỗi triển khai là: lan truyền xuôi → mất mát → lan truyền ngược → bộ tối ưu cập nhật tham số và trạng thái. Mômen lưu $u$; RMSprop lưu $s$; Adam lưu $m,v,t$; dropout và chuẩn hóa theo lô cần đúng chế độ huấn luyện hoặc suy luận; chuẩn hóa theo lô còn lưu thống kê chạy.

## Tự kiểm tra

- Kiểm tra kích thước: $W\in\mathbb R^{n_{out}\times n_{in}}$; với BN các đại lượng $\mu,\sigma^2,\gamma,\beta\in\mathbb R^D$.
- Trạng thái bộ tối ưu trên mỗi tham số: SGD $0$; Mômen $P$; RMSprop $P$; Adam $2P$ cộng bộ đếm bước.
- Phân biệt tham số, trạng thái bộ tối ưu, siêu tham số và chế độ mô hình.
- Nhắc lại ba bước giao thức: chẩn đoán → chọn cơ chế → xác thực rồi khóa tập kiểm tra.

## Kết luận

Quy trình gồm ba bước: **chẩn đoán → chọn đúng cơ chế → so sánh bằng xác thực và khóa tập kiểm tra.** Buổi 04 bắt đầu từ hạn chế của MLP với dữ liệu có cấu trúc không gian.

## Tài liệu tham khảo

- `lec10_training.pdf`, trang 3–9, 11–17, 19–33, 35–41;
- `lec05_multilayer.pdf`, trang 37–47;
- `lec02_linear_part1.pdf`, trang 55–68;
- `lec03_linear_part2.pdf`, trang 2–15;
- `lec04_multiclass.pdf`, trang 19;
- `hocsau_draft.pdf`, PDF 58–66, 96–105, 153–158;
- Goodfellow, Bengio, Courville, *Deep Learning*, §7.1.2, trang in 230–232, công thức (7.18)–(7.23), liên kết chính thức https://www.deeplearningbook.org/contents/regularization.html.

## Chuẩn bị cho bài tập trên lớp

Ôn bốn nhóm kỹ năng trước giờ bài tập: chẩn đoán đường cong, tính một bước cập nhật của từng bộ tối ưu, lựa chọn điều chuẩn và thiết kế giao thức so sánh bằng xác thực rồi khóa tập kiểm tra.
