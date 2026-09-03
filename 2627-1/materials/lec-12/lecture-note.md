# Buổi 12: Transformer nâng cao

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- phân biệt mô hình chỉ bộ mã hóa, chỉ bộ giải mã và mã hóa–giải mã qua luồng thông tin, mặt nạ và mục tiêu học;
- trình bày mô hình ngôn ngữ lớn và mô hình đa phương thức ở mức khái niệm;
- giải thích cách CLIP học không gian biểu diễn chung cho ảnh và văn bản;
- truy vết kích thước tensor của Vision Transformer (ViT) từ ảnh đến dự đoán.

Kiến thức tiên quyết: cơ chế chú ý và kiến trúc Transformer của Buổi 10–11, phép nhân ma trận, softmax, chéo entropy và tensor theo quy ước NCHW.

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $N,T_s,T_t,V,D$ | Cỡ lô, độ dài nguồn, độ dài đích, kích thước từ vựng và chiều mô hình |
| $M^{valid},M^{causal},M^{tgt}$ | Mặt nạ hợp lệ, mặt nạ nhân quả và mặt nạ vị trí chịu sai số |
| $Y^{in},Y^{out}$ | Đầu vào và nhãn của bộ giải mã, lệch nhau một vị trí |
| $y_{n,t}$ | Ký hiệu gốc hoặc nhãn kế tiếp tại vị trí $(n,t)$ |
| $E_I,E_T\in\mathbb R^{N\times D}$ | Biểu diễn ảnh và văn bản đã chuẩn hóa trong CLIP |
| $X\in\mathbb R^{N\times C\times H\times W}$ | Lô ảnh theo thứ tự NCHW |
| $P,T_p$ | Cạnh mảnh ảnh và số mảnh $(H/P)(W/P)$ |

## Cụm 1: Một chuỗi, ba họ Transformer

Giữ cố định chuỗi “mạng nơ-ron học”. Ba họ kiến trúc tạo tín hiệu học khác nhau bằng cách thay đổi tập vị trí được đọc và vị trí phải dự đoán.

![Ba họ Transformer khác nhau ở luồng thông tin, mặt nạ và mục tiêu](img/lec-12/mask-families.svg)

| Họ | Luồng thông tin | Mặt nạ chính | Mục tiêu điển hình |
|---|---|---|---|
| Chỉ bộ mã hóa | Hai chiều | Chặn khóa đệm | Khôi phục ký hiệu bị che |
| Chỉ bộ giải mã | Một chiều | Chặn khóa tương lai và khóa đệm | Dự đoán ký hiệu kế tiếp |
| Mã hóa–giải mã | Nguồn hai chiều, đích một chiều, chú ý chéo sang nguồn | Nguồn hợp lệ, đích nhân quả, khóa nguồn hợp lệ | Dự đoán chuỗi đích |

Mặt nạ chú ý quyết định vị trí nào được đọc. Mặt nạ giám sát quyết định vị trí nào góp vào hàm mất mát. Hai quyết định này không thay thế nhau.

## Cụm 2: Mô hình chỉ bộ mã hóa

Bộ mã hóa dùng ngữ cảnh hai chiều. Với lô có $T_q$ truy vấn và $T_k$ khóa, mặt nạ hợp lệ có thể phát thành kích thước $N\times1\times T_q\times T_k$. Mặt nạ chặn cột khóa đệm trước softmax; softmax vẫn chạy trên trục khóa.

Trong mô hình ngôn ngữ có che (masked language modeling, MLM), đầu vào $\widetilde X$ được thay đổi tại một tập vị trí hợp lệ $\Omega$. Mô hình khôi phục ký hiệu gốc tại các vị trí đó. Với $Z\in\mathbb R^{N\times T\times V}$,

$$
\mathcal L_{MLM}=
\frac{1}{|\Omega|}
\sum_{(n,t)\in\Omega}
\operatorname{CE}(Z_{n,t,:},y_{n,t}),
\qquad |\Omega|>0.
$$

Chéo entropy chuẩn hóa theo trục từ vựng $V$. Các vị trí không thuộc $\Omega$ vẫn có thể cung cấp ngữ cảnh nhưng không góp trực tiếp vào tổng sai số MLM.

Biểu diễn của bộ mã hóa có thể được dùng lại cho phân loại toàn chuỗi qua vị trí tổng hợp, hoặc cho gán nhãn từng vị trí. Khi đó một đầu tác vụ được thêm vào và mô hình được tinh chỉnh bằng dữ liệu có nhãn.

::: exercise Câu hỏi kiểm tra
Một chuỗi có năm vị trí; vị trí 4 bị che và vị trí 5 vẫn hợp lệ. Vị trí 4 được đọc những khóa nào, và vị trí nào góp trực tiếp vào sai số MLM?
:::

::: solution
Vị trí 4 được đọc các khóa hợp lệ 1–5 ở cả hai phía. Nếu $\Omega=\{4\}$ thì chỉ vị trí 4 góp trực tiếp vào sai số.
:::

## Cụm 3: Mô hình chỉ bộ giải mã

Khi sinh chuỗi, tương lai chưa tồn tại. Xác suất chuỗi được phân rã thành các dự đoán từ tiền tố:

$$
p(x_{1:T})=\prod_{t=1}^{T}p(x_t\mid x_{<t}).
$$

Mặt nạ nhân quả chỉ cho truy vấn $i$ đọc khóa $j\le i$. Ở dạng cộng, các vị trí $j>i$ nhận $-\infty$ trước softmax. Nếu lô có đệm, mặt nạ này còn phải kết hợp với mặt nạ khóa hợp lệ.

Trong mô hình ngôn ngữ nhân quả (causal language modeling, CLM), điểm $Z^{CLM}\in\mathbb R^{N\times T\times V}$ được so với nhãn kế tiếp. Mặt nạ $M^{tgt}\in\{0,1\}^{N\times T}$ loại vị trí đệm khỏi cả tổng và mẫu số:

$$
\mathcal L_{CLM}=
\frac{
\sum_{n,t}M^{tgt}_{n,t}\operatorname{CE}(Z^{CLM}_{n,t,:},y_{n,t})
}{
\sum_{n,t}M^{tgt}_{n,t}
}.
$$

Khi huấn luyện, toàn bộ chuỗi đích đã biết nên các vị trí được tính song song, nhưng mặt nạ vẫn ngăn rò thông tin tương lai. Khi suy luận, mô hình bắt đầu bằng BOS, đưa dự đoán trở lại tiền tố và dừng ở EOS hoặc giới hạn độ dài.

::: exercise Câu hỏi kiểm tra
Ở truy vấn $i=2$, một EOS nằm tại vị trí $j=4$ có được đọc không?
:::

::: solution
Không. Mặt nạ nhân quả chặn mọi khóa $j>i$. Việc EOS có phải nhãn hợp lệ hay không thuộc về mặt nạ giám sát, không làm thay đổi quan hệ nhân quả.
:::

## Cụm 4: Mô hình mã hóa–giải mã

Chuỗi đích được dịch một vị trí thành hai tensor cùng kích thước $N\times T_t$:

- $Y^{in}$ bắt đầu bằng BOS và đi vào bộ giải mã;
- $Y^{out}$ kết thúc bằng EOS và đóng vai trò nhãn.

![Luồng từ chuỗi nguồn và chuỗi đích đến hàm mất mát](img/lec-12/objective-trace.svg)

Ba luồng cần ba hợp đồng riêng:

| Luồng | Kích thước mặt nạ | Quy tắc |
|---|---|---|
| Tự chú ý nguồn | $N\times1\times T_s\times T_s$ | Chặn khóa nguồn đệm |
| Tự chú ý đích | $N\times1\times T_t\times T_t$ | Chặn khóa tương lai và khóa đích đệm |
| Chú ý chéo | $N\times1\times T_t\times T_s$ | Truy vấn đích đọc khóa nguồn hợp lệ |

Chú ý chéo lấy truy vấn từ trạng thái bộ giải mã, còn khóa và giá trị từ đầu ra bộ mã hóa. Điểm đích $Z^{tgt}\in\mathbb R^{N\times T_t\times V}$ dùng chéo entropy theo trục $V$ và chỉ trung bình trên vị trí đích hợp lệ.

Khi huấn luyện, bộ giải mã nhận toàn bộ $Y^{in}$ theo cơ chế học theo đáp án. Khi suy luận, biểu diễn nguồn được tính một lần, còn tiền tố đích tăng thêm một ký hiệu sau mỗi bước.

::: exercise Câu hỏi kiểm tra
Với $T_t=4$ và $T_s=6$, mặt nạ chú ý chéo có kích thước nào? Trục nào chứa các khóa nguồn?
:::

::: solution
Mặt nạ phát theo đầu có kích thước $N\times1\times4\times6$. Trục cuối dài 6 chứa các khóa nguồn; softmax của chú ý chéo chạy trên trục này.
:::

## Cụm 5: Huấn luyện trước và mô hình ngôn ngữ lớn

MLM và CLM đều tạo nhãn từ dữ liệu chưa gán nhãn thủ công. Huấn luyện trước học một bộ tham số có thể được dùng lại; tinh chỉnh hoặc nhắc lệnh điều chỉnh cách dùng bộ tham số đó cho tác vụ cụ thể.

Trong bài này, mô hình ngôn ngữ lớn (large language model, LLM) là mô hình ngôn ngữ nơ-ron được huấn luyện trước ở quy mô lớn và có thể thích nghi cho nhiều nhiệm vụ. Không có một ngưỡng “lớn” phổ quát. Tên gọi LLM không tự chứng minh mô hình đúng, an toàn hay phù hợp miền; mỗi kết luận cần giao thức đánh giá riêng.

## Cụm 6: CLIP và biểu diễn ảnh–văn bản

Mô hình đa phương thức xử lý từ hai loại dữ liệu trở lên. CLIP là trường hợp ảnh–văn bản với hai bộ mã hóa độc lập: một bộ nhận ảnh, bộ còn lại nhận văn bản. Mỗi nhánh được chiếu về cùng chiều $D$ rồi chuẩn hóa L2 theo hàng.

![Hai bộ mã hóa CLIP đưa ảnh và văn bản vào cùng không gian biểu diễn](img/lec-12/clip-dual-encoder.svg)

Với $N$ cặp đúng trong một lô,

$$
E_I,E_T\in\mathbb R^{N\times D},\qquad
S=\frac{E_IE_T^\top}{\tau}\in\mathbb R^{N\times N},\qquad \tau>0.
$$

Hàng $i$ của $S$ so ảnh $i$ với mọi văn bản; hàng $i$ của $S^\top$ so văn bản $i$ với mọi ảnh. Nhãn đúng nằm trên đường chéo.

![Đường chéo của ma trận tương đồng chứa các cặp ảnh–văn bản đúng](img/lec-12/clip-similarity-matrix.svg)

$$
\mathcal L_{I\to T}
=-\frac1N\sum_{i=1}^{N}
\log\frac{e^{S_{ii}}}{\sum_{j=1}^{N}e^{S_{ij}}},
$$

$$
\mathcal L_{T\to I}
=-\frac1N\sum_{i=1}^{N}
\log\frac{e^{S_{ii}}}{\sum_{j=1}^{N}e^{S_{ji}}},
\qquad
\mathcal L_{CLIP}=\frac{\mathcal L_{I\to T}+\mathcal L_{T\to I}}2.
$$

Trong chương trình, hai đại lượng này nên được tính bằng chéo entropy hợp nhất hoặc log-softmax ổn định số.

Nếu $E_I=E_T=I_2$ và $1/\tau=\ln3$ thì

$$
S=\begin{bmatrix}\ln3&0\\0&\ln3\end{bmatrix}.
$$

Xác suất của cặp đúng ở mỗi hàng và cột là $3/(3+1)=3/4$. Vì vậy,

$$
\mathcal L_{I\to T}=\mathcal L_{T\to I}
=-\ln\frac34=\ln\frac43\approx0{,}287682.
$$

Để phân loại không mẫu huấn luyện theo lớp đích, mỗi tên lớp được đặt vào một câu nhắc và mã hóa thành $E_T^{cls}\in\mathbb R^{K\times D}$. Điểm lớp là

$$
Z=\frac{E_I(E_T^{cls})^\top}{\tau}\in\mathbb R^{N\times K},
$$

và softmax chạy trên trục $K$. Cách dùng này vẫn cần được đánh giá trên dữ liệu đích; “zero-shot” không phải bảo chứng về chất lượng.

![Các câu nhắc lớp tạo bộ phân loại zero-shot trong không gian chung](img/lec-12/clip-zero-shot.svg)

::: exercise Câu hỏi kiểm tra
Với $N=8$, $D=512$ và $K=5$, hãy nêu kích thước của $S$, $E_T^{cls}$ và $Z$, rồi xác định trục softmax của $Z$.
:::

::: solution
$S$ có kích thước $8\times8$, $E_T^{cls}$ có kích thước $5\times512$, và $Z$ có kích thước $8\times5$. Softmax của $Z$ chạy trên trục lớp $K=5$.
:::

## Cụm 7: Vision Transformer

Transformer nhận chuỗi, còn ảnh là lưới. ViT chuyển ảnh thành chuỗi mảnh trước khi dùng bộ mã hóa Transformer.

Xét $X\in\mathbb R^{2\times3\times32\times32}$, cạnh mảnh $P=8$ và chiều mô hình $D=64$. Mỗi ảnh có

$$
T_p=(32/8)(32/8)=16
$$

mảnh. Mỗi mảnh chứa $CP^2=3\cdot8^2=192$ số. Sau khi làm phẳng theo thứ tự quét hàng,

$$
X_{patch}\in\mathbb R^{2\times16\times192}.
$$

Tổng quát, với $P\mid H$ và $P\mid W$,

$$
T_p=\frac HP\frac WP,\qquad
X_{patch}\in\mathbb R^{N\times T_p\times CP^2}.
$$

Một phép chiếu dùng chung cho mọi mảnh đưa chiều $CP^2$ về $D$:

$$
E_{patch}=X_{patch}W_E+b_E,\qquad
W_E\in\mathbb R^{CP^2\times D}.
$$

Trong ví dụ, kích thước chuyển từ $2\times16\times192$ thành $2\times16\times64$.

![Vết kích thước từ ảnh NCHW đến đầu ra ViT](img/lec-12/vit-trace.svg)

ViT chèn một vectơ CLS học được vào đầu chuỗi và cộng mã vị trí:

$$
Z_0=[E_{cls};E_{patch}]+E_{pos}
\in\mathbb R^{N\times(T_p+1)\times D}.
$$

Ví dụ trên cho $Z_0\in\mathbb R^{2\times17\times64}$. Một khối chuẩn hóa trước bảo toàn kích thước:

$$
U_\ell=Z_{\ell-1}+\operatorname{Drop}
\bigl(\operatorname{MSA}(\operatorname{LN}(Z_{\ell-1}))\bigr),
$$

$$
Z_\ell=U_\ell+\operatorname{Drop}
\bigl(\operatorname{MLP}(\operatorname{LN}(U_\ell))\bigr).
$$

![Khối ViT chuẩn hóa trước với hai đường dư](img/lec-12/vit-prenorm.svg)

Chuẩn hóa lớp chạy trên chiều $D$. Bỏ ngẫu nhiên hoạt động khi huấn luyện và tắt khi đánh giá. Sau $L$ khối, vị trí CLS có thể đi vào đầu phân loại độc lập, hoặc được chiếu và chuẩn hóa để tạo một hàng của $E_I$ trong CLIP.

Kích thước mảnh quyết định độ dài chuỗi. Với ảnh $32\times32$, đổi từ $P=8$ sang $P=4$ làm số mảnh tăng từ 16 lên 64 và độ dài kể cả CLS tăng từ 17 lên 65. Riêng phần tự chú ý theo chiều chuỗi có tỷ số chi phí

$$
\frac{65^2}{17^2}=\frac{4225}{289}\approx14{,}62.
$$

Nếu bỏ qua CLS trong giới hạn chuỗi dài, số mảnh tăng bốn lần nên chi phí chú ý tiến tới tăng 16 lần.

::: exercise Câu hỏi kiểm tra
Với $X\in\mathbb R^{2\times3\times32\times32}$, $P=4$ và $D=64$, hãy tính kích thước $Z_0$.
:::

::: solution
Có $(32/4)^2=64$ mảnh. Sau khi thêm CLS, $Z_0\in\mathbb R^{2\times65\times64}$.
:::

## Đạo đức và giới hạn triển khai

Một trường đại học dùng trợ lý dựa trên LLM để đọc hồ sơ, trả lời thí sinh và đề xuất xếp hạng.

::: exercise Câu hỏi thảo luận
Chọn một rủi ro: chênh lệch chất lượng giữa các nhóm thí sinh, lộ thông tin cá nhân, hoặc thông tin tuyển sinh sai. Hãy nêu bằng chứng cần thu, phép kiểm có thể thực hiện và hành động nếu phép kiểm thất bại. Trợ lý nên tự ra quyết định hay chỉ hỗ trợ con người? Giải thích bằng hậu quả và khả năng kiểm soát.
:::

Một tên kiến trúc không quyết định mức an toàn. Phạm vi dùng, dữ liệu, quyền truy cập, người chịu trách nhiệm và giao thức đánh giá phải được xác định trước triển khai.

## Tổng hợp

| Cấu hình | Dữ liệu vào và luồng thông tin | Tín hiệu học hoặc đầu ra |
|---|---|---|
| Chỉ bộ mã hóa | Một chuỗi, ngữ cảnh hai chiều | MLM hoặc biểu diễn cho tác vụ |
| Chỉ bộ giải mã | Một chuỗi, ngữ cảnh nhân quả | CLM và sinh tự hồi quy |
| Mã hóa–giải mã | Chuỗi nguồn và tiền tố đích | Dự đoán chuỗi đích |
| CLIP | Cặp ảnh–văn bản, hai bộ mã hóa độc lập | Sai số đối sánh đối xứng; điểm lớp zero-shot |
| ViT | Ảnh được đổi thành chuỗi mảnh | Phân loại ảnh hoặc biểu diễn nhánh ảnh |

Khi kiểm tra một mô hình Transformer, hãy lần theo bốn câu hỏi: tensor nào đi vào; vị trí nào được đọc; điểm nào được so với nhãn; giao thức nào đủ để đánh giá kết luận.

## Bài tập 50 phút

1. Trong 10 phút, điền bảng so sánh ba họ Transformer theo luồng thông tin, mặt nạ và mục tiêu.
2. Trong 10 phút, dựng mặt nạ luận lý và mặt nạ cộng cho hai chuỗi dài 4 và 2 trong cùng lô; tách mặt nạ chú ý khỏi mặt nạ giám sát.
3. Trong 10 phút, với $N=4,C=3,H=W=64,P=16,D=128,K=10$, tính kích thước từ ảnh đến điểm phân loại và xác định trục softmax.
4. Trong 20 phút, đề xuất một dự án cuối kỳ dùng Transformer hoặc LLM có sẵn. Nêu bài toán, dữ liệu có thể tiếp cận, đầu ra, cách đánh giá, nguồn lực và rủi ro chính; đánh giá riêng tính khả thi và tính sáng tạo.

## Nguồn

- Đề cương học phần UET.AI3056, `III.2 → Buổi 12`, LLO23–25.
- `source-materials/slides/lec16_transformer.pdf`, PDF 38–48.
- `source-materials/slides/lec17_vision_transformers.pdf`, PDF 5–24.
- `source-materials/textbooks/hocsau_draft.pdf`, PDF 277–293, 327–333 và 352–359.
- Radford và cộng sự (2021), *Learning Transferable Visual Models From Natural Language Supervision*, PDF 1–3, Hình 1 và Hình 3.
