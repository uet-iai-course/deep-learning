# Buổi 05: Các kiến trúc mạng tích chập hiện đại

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- mô tả LeNet, AlexNet, VGG, GoogLeNet và ResNet bằng kích thước tensor và các khối tính toán;
- phân tích nơi tập trung tham số, phép nhân–cộng và đường truyền đạo hàm;
- giải thích vai trò của nhân $3\times3$, nhánh Inception, chuẩn hóa theo lô và kết nối tắt;
- phân biệt đóng băng tham số với chế độ huấn luyện hoặc suy luận khi học chuyển giao.

Kiến thức tiên quyết từ Bài 02–03: tích chập, phép gộp, hàm kích hoạt, lan truyền ngược, thứ tự trục NCHW/OIHW và phép nhân ma trận đạo hàm chuyển vị với véc-tơ.

Bài này xem kiến trúc như cách phân bổ bốn đại lượng: kích thước tensor, tham số, MAC và đường truyền đạo hàm. Mỗi kiến trúc thay đổi một nút thắt của kiến trúc trước, đồng thời tạo ra giới hạn mới cho kiến trúc sau.

## Ký hiệu và quy ước

- $X\in\mathbb R^{N\times C\times H\times W}$ theo NCHW: lô, kênh, chiều cao, chiều rộng.
- $W\in\mathbb R^{C_{out}\times C_{in}\times K_h\times K_w}$ theo OIHW.
- $P$ là số tham số học được, gồm độ lệch khi đặc tả có độ lệch.
- MAC là một phép nhân–cộng tích lũy. Các phép đếm trong bài không tính phép cộng độ lệch. Chỉ khi nêu quy ước mới dùng $1\,\mathrm{MAC}\approx2\,\mathrm{FLOP}$.
- $F(x;W)$ là nhánh thặng dư; $P(x)$ là phép chiếu trên nhánh tắt.
- Sau khi véc-tơ hóa, $J_F,J_P\in\mathbb R^{d_{out}\times d_{in}}$. Gradient cột truyền theo $\bar x=J_s^\top\bar s$.

Mỗi kiến trúc được kiểm bằng bốn câu: kích thước tensor thay đổi thế nào, tham số tập trung ở đâu, MAC tập trung ở đâu và đạo hàm có những đường truyền nào.

## Khái niệm trọng tâm

### Cụm 1: LeNet làm mốc so sánh

LeNet ghép các phép toán của bài trước thành một mạng hoàn chỉnh. Biến thể trong giáo trình nhận ảnh $28\times28$, dùng hai khối tích chập $5\times5$ → sigmoid → gộp trung bình, rồi các tầng đầy đủ $120\to84\to10$.

Biến thể này có đệm ở tầng đầu. Không ghép dấu vết của nó với LeNet-5 nguyên bản nhận ảnh $32\times32$.

![Dấu vết kích thước của biến thể LeNet dùng trong bài](img/lec-05/lenet-trace.svg)

LeNet cho một mẫu khối rõ, nhưng ảnh và tập nhãn lớn hơn đòi hỏi thêm kênh, thêm tầng và kỹ thuật huấn luyện phù hợp. AlexNet là mốc tiếp theo để quan sát hai loại chi phí khác nhau: dung lượng tham số và số phép tính.

::: exercise Câu hỏi kiểm tra
Một tầng tích chập $5\times5$ nhận một kênh và tạo sáu kênh, có độ lệch. Tầng có bao nhiêu tham số?
:::

::: solution
$6(1\cdot5\cdot5+1)=156$ tham số.
:::

### Cụm 2: AlexNet tách dung lượng khỏi chi phí tính toán

Các phép tính dưới đây dùng duy nhất bản sửa đổi nhận ảnh $3\times227\times227$ và có 64 kênh ở tầng tích chập đầu. Không trộn số của bản này với cấu hình AlexNet gốc chia mạng trên hai GPU.

Dấu vết kích thước là

$$
3\times227^2\to64\times56^2\to64\times27^2
\to192\times27^2\to192\times13^2
\to384\times13^2\to256\times13^2\to256\times13^2
\to256\times6^2\to9216\to4096\to4096\to1000.
$$

![Dấu vết kích thước phần tích chập của AlexNet](img/lec-05/alexnet-shapes.svg)

Tầng tích chập đầu dùng nhân $11\times11$, bước trượt 4, vùng đệm 2 và 64 kênh ra. Số MAC của tầng là

$$
56^2\cdot64\cdot3\cdot11^2=72\,855\,552.
$$

Ngay trước FC6, tensor $256\times6\times6$ được làm phẳng thành 9216 phần tử. FC6 có

$$
|W_{\mathrm{FC6}}|=9216\cdot4096=37\,748\,736
$$

trọng số, hoặc 37.752.832 tham số khi cộng 4096 độ lệch. Toàn mạng có 61.100.840 tham số và 716.767.232 MAC theo quy ước của bài.

::: derivation Kiểm tổng số MAC
| Tầng | MAC |
|---|---:|
| Tích chập 1–5 | 72.855.552; 223.948.800; 112.140.288; 149.520.384; 99.680.256 |
| FC6–FC8 | 37.748.736; 16.777.216; 4.096.000 |
| Tổng | 716.767.232 |
:::

::: example Hai nơi tập trung chi phí
FC6 nối mọi cặp trong ma trận $9216\times4096$, nên giữ nhiều tham số. Tầng tích chập 2 dùng nhân $5\times5$ trên $27^2$ vị trí và nhiều kênh, nên giữ nhiều MAC nhất trong dấu vết này. Số tham số và số MAC không xếp hạng các tầng theo cùng một thứ tự.
:::

ReLU, gộp cực đại, bỏ nút ngẫu nhiên và GPU xử lý các nút thắt khác nhau. ReLU thay sigmoid ở các tầng ẩn; gộp giảm độ phân giải; bỏ nút ngẫu nhiên điều chuẩn các tầng đầy đủ khi huấn luyện; GPU cho phép thực thi mạng lớn. Không dùng một thay đổi để giải thích thay cho các thay đổi còn lại.

::: exercise Câu hỏi kiểm tra
Tính số tham số có độ lệch của tầng tích chập đầu và giải thích vì sao kết quả nhỏ hơn nhiều so với số MAC của chính tầng đó.
:::

::: hint
Tham số được dùng lại ở mọi vị trí đầu ra; MAC phải nhân thêm $56^2$.
:::

::: solution
$64(3\cdot11^2+1)=23\,296$ tham số; mỗi trọng số được dùng trên nhiều vị trí không gian.
:::

AlexNet chọn riêng từng tầng và dồn nhiều tham số vào đầu đầy đủ. VGG thay cách thiết kế đó bằng một quy tắc lặp thống nhất.

### Cụm 3: VGG chuẩn hóa kiến trúc thành khối lặp

VGG-16 dùng năm khối có lần lượt $2,2,3,3,3$ tầng tích chập $3\times3$. Trong mỗi tầng đang xét, bước trượt và độ giãn đều bằng 1; vùng đệm giữ nguyên chiều cao và chiều rộng.

Ba tầng $3\times3$ liên tiếp có trường tiếp nhận

$$
r_0=1,\qquad r_1=3,\qquad r_2=5,\qquad r_3=7.
$$

Nếu mỗi tầng có $C_{in}=C_{out}=K$ và bỏ độ lệch, một tầng $7\times7$ dùng $49K^2$ trọng số. Ba tầng $3\times3$ dùng $27K^2$ trọng số. Phần giảm là

$$
\frac{49K^2-27K^2}{49K^2}=\frac{22}{49}\approx44{,}9\%.
$$

Ba tầng còn đặt thêm hai hàm kích hoạt so với một tầng duy nhất. Kết luận này phụ thuộc giả thiết cùng số kênh, bước trượt 1 và độ giãn 1; nó không chứng minh MAC luôn giảm trong mọi cấu hình.

![Một khối VGG dùng các tầng tích chập 3 nhân 3](img/lec-05/vgg-block.svg)

![Dấu vết năm khối của VGG-16](img/lec-05/vgg16-trace.svg)

::: exercise Câu hỏi kiểm tra
Với $K=64$, tính số trọng số của một tầng $7\times7$ và ba tầng $3\times3$.
:::

::: solution
$200\,704$ so với $110\,592$ trọng số.
:::

VGG làm cấu trúc đều hơn, nhưng mỗi khối vẫn chọn một kích thước nhân cho mọi đặc trưng. Inception cho nhiều thang không gian cùng hoạt động trong một khối.

### Cụm 4: Inception phân bổ tính toán qua nhiều nhánh

Phần gốc của GoogLeNet dùng ba tầng tích chập, đưa $3\times224^2$ thành $192\times28^2$. Bỏ độ lệch, ba tầng có

$$
7^2\cdot3\cdot64+1^2\cdot64\cdot64+3^2\cdot64\cdot192
=124\,096
$$

trọng số.

![Phần gốc ba tầng tích chập của GoogLeNet](img/lec-05/googlenet-stem.svg)

Một khối Inception nhận 192 kênh và chạy bốn nhánh song song. Các nhánh tạo lần lượt 64, 128, 32 và 32 kênh. Vì chúng giữ cùng $N,H,W$, phép ghép theo trục kênh tạo đầu ra $N\times256\times H\times W$.

![Bốn nhánh của một khối Inception](img/lec-05/inception-branches.svg)

Các tầng $1\times1$ trước nhân $3\times3$ và $5\times5$ giảm số kênh trung gian. Phép đếm đầy đủ là


| Nhánh | Trọng số khi có giảm kênh |
|---|---:|
| $1\times1:192\to64$ | 12.288 |
| $1\times1:192\to96$, rồi $3\times3:96\to128$ | 129.024 |
| $1\times1:192\to16$, rồi $5\times5:16\to32$ | 15.872 |
| gộp, rồi $1\times1:192\to32$ | 6.144 |
| Tổng | 163.328 |

Đây là phép đếm cho khối Inception đầu tiên với $C_{in}=192$; các khối sau có số kênh và số trọng số khác. Nếu hai nhân lớn nhận trực tiếp 192 kênh, tổng là 393.216 trọng số. Tầng $1\times1$ giảm chi phí trước khi áp dụng nhân lớn.

Toàn GoogLeNet xếp các khối Inception theo nhóm $2$–$5$–$2$, giảm độ phân giải $28\to14\to7$. Gộp toàn cục biến $1024\times7^2$ thành $1024\times1^2$. Tầng phân loại 1000 lớp còn 1.024.000 trọng số, thay vì 102.760.448 trọng số của FC6 trong VGG-16; nếu có độ lệch, đầu GoogLeNet có 1.025.000 tham số.

![Gộp toàn cục trước tầng phân loại](img/lec-05/global-average-head.svg)

::: exercise Câu hỏi kiểm tra
Một nhánh tạo tensor $N\times32\times(H-2)\times W$, ba nhánh còn lại giữ $N\times C_i\times H\times W$. Có thể ghép bốn nhánh theo trục kênh không?
:::

::: solution
Không. Các nhánh phải có cùng $N,H,W$; cần sửa vùng đệm của nhánh thứ nhất.
:::

### Cụm 5: Chuẩn hóa theo lô có hai chế độ

::: example Trục giảm và phát rộng
Với $X:8\times64\times28\times28$, mỗi kênh dùng $8\cdot28\cdot28=6272$ giá trị để tính trung bình và phương sai. BN tạo 64 cặp tham số theo kênh; nó không gộp 64 kênh với nhau.
:::

Tổng quát, với $X\in\mathbb R^{N\times C\times H\times W}$, chuẩn hóa theo lô (BN) tính thống kê riêng cho từng kênh trên các trục $N,H,W$:

$$
\mu_c=\frac{1}{NHW}\sum_{n,h,w}X_{n,c,h,w},
$$

$$
\sigma_c^2=\frac{1}{NHW}\sum_{n,h,w}(X_{n,c,h,w}-\mu_c)^2,
$$

$$
\widehat X_{n,c,h,w}=\frac{X_{n,c,h,w}-\mu_c}{\sqrt{\sigma_c^2+\epsilon}},
\qquad
Y_{n,c,h,w}=\gamma_c\widehat X_{n,c,h,w}+\beta_c.
$$

$\epsilon>0$ giữ mẫu số khác 0. Hai véc-tơ $\gamma,\beta\in\mathbb R^C$ được phát rộng thành $1\times C\times1\times1$.

![Các trục dùng để tính thống kê BN](img/lec-05/bn-axes.svg)

Khi huấn luyện, lượt xuôi dùng thống kê của lô hiện tại; đổi thành phần lô có thể đổi đầu ra của một mẫu. Khi suy luận, mô-đun dùng thống kê cố định đã được ước lượng trong quá trình học. Cách cập nhật các thống kê cố định phụ thuộc khung phần mềm và cấu hình, nên phải kiểm tra thay vì suy ra từ ký hiệu.

![Thống kê BN trong huấn luyện và suy luận](img/lec-05/bn-train-eval.svg)

::: exercise Câu hỏi kiểm tra
Một tensor $16\times128\times14\times14$ dùng bao nhiêu giá trị cho thống kê của mỗi kênh? $\gamma$ và $\beta$ có kích thước nào?
:::

::: solution
$16\cdot14\cdot14=3136$ giá trị mỗi kênh; $\gamma,\beta\in\mathbb R^{128}$.
:::

BN kiểm soát thang kích hoạt và tách rõ hai chế độ. Khi mạng tiếp tục sâu hơn, một vấn đề khác xuất hiện: thêm tầng có thể làm lỗi huấn luyện tăng dù mô hình mới chứa nhiều khả năng biểu diễn hơn. ResNet xử lý trực tiếp trở ngại này.

### Cụm 6: ResNet thêm đường truyền trực tiếp

**Suy giảm** là hiện tượng lỗi huấn luyện tăng khi xếp thêm tầng. Nó khác quá khớp, vì quá khớp thường đi cùng lỗi huấn luyện thấp nhưng lỗi kiểm tra cao. Các nguồn trong phạm vi bài không đủ để quy suy giảm cho một cơ chế gradient duy nhất.

![Hiện tượng suy giảm khi tăng độ sâu](img/lec-05/degradation.svg)

Một khối thặng dư học $F(x;W)$ rồi cộng với nhánh tắt:

$$
s=x+F(x;W).
$$

Phép cộng đòi hỏi hai nhánh cùng $N,C,H,W$. Khi số kênh hoặc độ phân giải đổi, nhánh tắt dùng phép chiếu $1\times1$:

$$
s=P(x)+F(x;W).
$$

![Nhánh đồng nhất trong một khối thặng dư](img/lec-05/residual-block.svg)

![Phép chiếu làm hai nhánh cùng kích thước](img/lec-05/residual-projection.svg)

Sau khi véc-tơ hóa tensor, nhánh đồng nhất và nhánh chiếu có các ma trận đạo hàm

$$
J_s=I+J_F,
\qquad
J_s=J_P+J_F.
$$

Với gradient cột,

$$
\bar x=J_s^\top\bar s.
$$

Số hạng $I$ tạo một đường cộng trực tiếp cho tín hiệu và đạo hàm. Tổng $I+J_F$ vẫn có thể triệt tiêu theo một hướng, nên kết nối tắt không phải bảo đảm rằng mọi gradient đều được giữ nguyên.

::: derivation Một ánh xạ và một nhánh cổ chai
Một tầng $3\times3:256\to256$ có $9\cdot256^2=589\,824$ trọng số. Nhánh cổ chai $256\to64\to64\to256$ dùng

$$
256\cdot64+9\cdot64^2+64\cdot256=69\,632
$$

trọng số. Tỷ lệ $589\,824/69\,632\approx8{,}47$ chỉ so một tầng $3\times3$ với cả nhánh cổ chai; không phải tỷ lệ giữa hai khối hoàn chỉnh tương đương.
:::

![Khối cơ bản và khối cổ chai](img/lec-05/resnet-block-types.svg)

Sau phần gốc nhận ảnh $3\times224^2$, ResNet-18 có bốn giai đoạn, mỗi giai đoạn gồm hai khối cơ bản. Dấu vết đầu ra là

$$
64\times56^2\to128\times28^2\to256\times14^2\to512\times7^2.
$$

Khối đầu ở các giai đoạn 2–4 giảm nửa độ phân giải và tăng số kênh, nên nhánh tắt phải chiếu trước khi cộng.

![Dấu vết bốn giai đoạn của ResNet-18](img/lec-05/resnet18-trace.svg)

::: exercise Câu hỏi kiểm tra
Thiết kế khối $N\times64\times56\times56\to N\times128\times28\times28$. Nhánh tắt cần toán tử nào?
:::

::: solution
Nhánh tắt dùng tích chập $1\times1$, bước trượt 2 và 128 kênh ra để khớp nhánh chính.
:::

Thân ResNet đã học có thể được tái dùng cho nhiệm vụ mới. Khi đó, việc cập nhật gradient và việc chọn chế độ mô-đun là hai quyết định riêng.

### Cụm 7: Học chuyển giao tách gradient khỏi chế độ mô-đun

Một thân mạng đã học có thể tạo véc-tơ đặc trưng cho nhiệm vụ mới. Ba quyết định phải được tách riêng:

- tham số nào được tính gradient và cập nhật;
- mô-đun nào chạy ở chế độ huấn luyện hoặc suy luận;
- BN dùng thống kê lô hay thống kê cố định trong giai đoạn tinh chỉnh.

Đóng băng tham số ngăn bộ tối ưu cập nhật các tham số đó; nó không tự động đổi mô-đun sang chế độ suy luận. Khi suy luận cuối cùng, toàn bộ mô-đun phải ở chế độ suy luận.

::: example Hai tình huống
Với tập mới nhỏ và gần miền nguồn, có thể đóng băng phần lớn thân, đặt thân ở chế độ suy luận và học đầu mới. Với tập mới lớn nhưng khác miền, có thể tinh chỉnh nhiều tầng hơn; chính sách BN phải được chọn và ghi rõ.
:::

![Thân tích chập tạo véc-tơ cho nhiệm vụ kế tiếp](img/lec-05/captioning-vector.svg)

Bộ phân loại phụ của GoogLeNet, cách nhìn ResNet như nhiều đường tính, thứ tự hậu kích hoạt hoặc tiền kích hoạt và giao diện véc-tơ là các phần bổ sung. Mô hình chuỗi nhận véc-tơ đặc trưng thuộc Bài 07.

## Từ công thức đến triển khai

Khi đọc hoặc cấu hình một kiến trúc, lần theo cùng một thứ tự:

1. ghi kích thước $N,C,H,W$ sau mỗi tích chập, phép gộp, ghép hoặc cộng;
2. kiểm điều kiện ghép theo kênh và điều kiện cộng theo phần tử;
3. đếm tham số từ kích thước tensor trọng số, tách rõ độ lệch;
4. đếm MAC từ số vị trí đầu ra và số tích trong mỗi vị trí;
5. xác định đường truyền đạo hàm qua nhánh chính, nhánh tắt và phép ghép;
6. khóa chế độ huấn luyện hoặc suy luận cho BN, bỏ nút ngẫu nhiên và toàn mô hình.

## Tự kiểm tra

1. Vì sao FC6 của AlexNet giữ nhiều tham số nhưng tầng tích chập 2 giữ nhiều MAC? (Cụm 2.)
2. Ba tầng $3\times3$ đạt trường tiếp nhận nào, dùng bao nhiêu trọng số so với một tầng $7\times7$? (Cụm 3.)
3. Vì sao bốn nhánh Inception phải có cùng $N,H,W$ trước khi ghép? (Cụm 4.)
4. Với $X:8\times64\times28\times28$, BN giảm theo những trục nào và dùng bao nhiêu giá trị mỗi kênh? (Cụm 5.)
5. Viết $J_s$ cho nhánh đồng nhất và nhánh chiếu; nêu điều kiện kích thước của phép cộng. (Cụm 6.)
6. Khi đóng băng thân mạng, vì sao vẫn phải chọn riêng chế độ mô-đun và chính sách BN? (Cụm 7.)

## Tài liệu tham khảo

- Đề cương học phần, III.2, Buổi 5; `source.md`, Buổi 05.
- `source-materials/slides/lec09_cnn_architectures.pdf`, PDF 3–9, 11–23, 26–34 và 44–46.
- `source-materials/slides/lec10_training.pdf`, PDF 25–32.
- `source-materials/textbooks/hocsau_draft.pdf`, PDF 132–146 và 149–163.
