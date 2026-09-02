# Buổi 06: Học biểu diễn và mạng tự mã hóa

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- mô tả bộ mã hóa, không gian ẩn và bộ giải mã của mạng tự mã hóa (autoencoder, AE);
- tính kích thước tensor, số tham số và mất mát tái tạo trên một ví dụ nhỏ;
- phân biệt mã thấp chiều, mã thưa và mạng tự mã hóa khử nhiễu;
- nối tiền huấn luyện không nhãn với đóng băng hoặc tinh chỉnh trên tác vụ đích;
- giải thích vì sao AE thường không tự cung cấp một quy tắc lấy mẫu trong không gian ẩn.

Kiến thức tiên quyết: MLP, lan truyền ngược, phép nhân ma trận, chia dữ liệu huấn luyện–kiểm định–kiểm tra, quy ước NCHW và chế độ huấn luyện–suy luận của mô-đun.

Tuyến lõi đi từ ảnh → biểu diễn → tái tạo → ràng buộc biểu diễn → tái sử dụng. Phần bổ sung xét hình học của không gian biểu diễn. Chất lượng tái tạo và chất lượng biểu diễn là hai đại lượng liên quan nhưng không đồng nhất.

## Ký hiệu và hợp đồng tensor

- $X_{\mathrm{img}}\in[0,1]^{N\times1\times28\times28}$ là lô ảnh MNIST theo NCHW.
- $X\in[0,1]^{N\times784}$ là lô ảnh sau khi làm phẳng từng mẫu.
- $H_e,H_d\in\mathbb R^{N\times256}$ là hoạt hóa ẩn của bộ mã hóa và bộ giải mã.
- $Z=f_\theta(X)\in\mathbb R^{N\times d}$ là lô mã tiềm ẩn.
- $\hat X=g_\phi(Z)\in(0,1)^{N\times784}$ là lô tái tạo qua đầu ra sigmoid.
- $\widetilde X\in\mathbb R^{N\times784}$ là đầu vào bị nhiễu; đích khử nhiễu vẫn là $X$ sạch.

Kiến trúc xuyên suốt là $784\to256\to d\to256\to784$.

## Khái niệm trọng tâm

### Cụm 1: Biểu diễn thay đổi độ khó của tác vụ

Một biểu diễn là cách mã hóa dữ liệu để phép toán hoặc tác vụ phía sau dễ thực hiện hơn. Cùng một giá trị có thể khó chia ở dạng ký hiệu này nhưng dễ chia ở dạng ký hiệu khác; cùng một ảnh có thể khó phân loại từ từng điểm ảnh nhưng dễ phân loại hơn từ một véc-tơ đặc trưng phù hợp.

![Tuyến từ dữ liệu đến biểu diễn và tác vụ](img/lec-06/representation-route.svg)

Học tự giám sát tạo tín hiệu học từ chính dữ liệu. Với AE, đầu vào sạch đóng vai trò đích tái tạo; không cần nhãn lớp để huấn luyện bộ mã hóa và bộ giải mã.

![Hai cách biểu diễn cùng một chữ số](img/lec-06/numeral-representation.svg)

Mất mát tái tạo thấp chỉ xác nhận khả năng khôi phục đầu vào theo hàm mất mát đã chọn. Nó chưa xác nhận mã hữu ích cho phân loại, tìm kiếm hoặc một tác vụ đích khác.

::: exercise Câu hỏi kiểm tra
Một AE huấn luyện trên ảnh không có nhãn lớp có phải là mô hình học có giám sát phân loại không?
:::

::: solution
Không. Đích học là chính dữ liệu đầu vào, không phải nhãn lớp. Đây là mục tiêu tự giám sát.
:::

Đánh giá một mã đòi hỏi mô tả rõ cách tạo mã và cách tái tạo dữ liệu từ mã đó.

### Cụm 2: Bộ mã hóa, mã tiềm ẩn và bộ giải mã

Bộ mã hóa $f_\theta$ biến $X$ thành $Z$. Bộ giải mã $g_\phi$ biến $Z$ thành $\hat X$. Toàn mô hình thực hiện

$$
X\xrightarrow{f_\theta}Z\xrightarrow{g_\phi}\hat X.
$$

![Ba phần của một mạng tự mã hóa](img/lec-06/ae-overview.svg)

Với MNIST, dấu vết kích thước là

$$
N\times1\times28\times28\to N\times784\to N\times256
\to N\times d\to N\times256\to N\times784.
$$

![Dấu vết kích thước tensor trên MNIST](img/lec-06/mnist-shapes.svg)

Một MLP minh họa dùng ReLU ở các lớp ẩn và sigmoid ở đầu ra để đưa mỗi phần tử của $\hat X$ vào $(0,1)$.

![Kiến trúc MLP của mạng tự mã hóa](img/lec-06/ae-mlp.svg)

::: derivation Số tham số khi $d=32$

| Lớp | Tham số có độ lệch |
|---|---:|
| $784\to256$ | $784\cdot256+256=200.960$ |
| $256\to32$ | $256\cdot32+32=8.224$ |
| $32\to256$ | $32\cdot256+256=8.448$ |
| $256\to784$ | $256\cdot784+784=201.488$ |
| Tổng | $419.120$ |

:::

::: exercise Câu hỏi kiểm tra
Với $N=16$ và $d=32$, kích thước của $Z$ và $\hat X$ là gì?
:::

::: solution
$Z\in\mathbb R^{16\times32}$ và $\hat X\in(0,1)^{16\times784}$.
:::

Kích thước đầu ra khớp đầu vào cho phép so từng phần tử trong mất mát tái tạo.

### Cụm 3: Mất mát tái tạo phải khóa quy ước lấy trung bình

Với một mẫu $x\in\mathbb R^D$, tổng bình phương sai số là

$$
\mathrm{SSE}(x,\hat x)=\sum_{j=1}^{D}(x_j-\hat x_j)^2.
$$

Với một lô $X\in\mathbb R^{N\times D}$, bài này dùng trung bình bình phương sai số

$$
\mathrm{MSE}(X,\hat X)=\frac{1}{ND}\lVert X-\hat X\rVert_F^2.
$$

Hai đại lượng khác nhau ở mẫu số. Một thư viện có thể dùng phép tổng hoặc một quy ước giảm khác; vì vậy báo cáo mất mát phải ghi rõ trục và phép giảm.

::: example Ví dụ bốn chiều
Với $x=(0{,}2,0{,}4,0{,}8,0{,}3)$ và $\hat x=(0{,}1,0{,}6,0{,}5,0{,}5)$,

$$
\mathrm{SSE}=0{,}01+0{,}04+0{,}09+0{,}04=0{,}18,
\qquad
\mathrm{MSE}=\frac{0{,}18}{4}=0{,}045.
$$
:::

Huấn luyện giảm mất mát trên tập huấn luyện. Kích thước mã, cường độ phạt và mức nhiễu được chọn trên tập kiểm định. Tập kiểm tra chỉ dùng sau khi các lựa chọn đã chốt.

::: exercise Câu hỏi kiểm tra
Một lô có $N=2$, $D=4$ và tổng bình phương sai số trên cả lô bằng $0{,}40$. MSE theo quy ước của bài bằng bao nhiêu?
:::

::: solution
$0{,}40/(2\cdot4)=0{,}05$.
:::

Mất mát tái tạo thấp vẫn có thể xuất hiện cùng một đường sao chép không hữu ích.

### Cụm 4: Nút thắt hạn chế đường sao chép

Nếu mô hình đủ năng lực, nghiệm đồng nhất $\hat X=X$ cho mất mát tái tạo bằng 0 mà không tạo ra biểu diễn hữu ích cho tác vụ khác.

![Đường sao chép đồng nhất](img/lec-06/identity-copy.svg)

Mã có $d<784$ tạo một nút thắt kiến trúc. Mô hình phải đưa thông tin qua ít tọa độ hơn đầu vào, nên ràng buộc này khuyến khích nén.

![Nút thắt trong không gian mã](img/lec-06/bottleneck.svg)

Nút thắt không bảo đảm chống ghi nhớ. Một mạng có năng lực lớn vẫn có thể gán mã riêng cho các mẫu huấn luyện. Vì vậy $d$ phải được đánh giá bằng dữ liệu chưa thấy và bằng tác vụ đích, không chỉ bằng mất mát huấn luyện.

::: exercise Câu hỏi kiểm tra
Một mô hình có MSE huấn luyện gần 0 nhưng MSE kiểm định cao. Có thể kết luận mã đã học cấu trúc tổng quát không?
:::

::: solution
Không. Khoảng cách huấn luyện–kiểm định là dấu hiệu mô hình có thể ghi nhớ dữ liệu huấn luyện.
:::

Ngoài việc giảm $d$, ràng buộc có thể tác động trực tiếp lên mã hoặc lên dữ liệu đầu vào.

### Cụm 5: Ba cách đặt ràng buộc

Mã thấp chiều đặt ràng buộc bằng $d$. Mã thưa đặt ràng buộc trên số hoặc độ lớn của các phần tử hoạt động. Khử nhiễu đặt ràng buộc bằng cách thay đổi đầu vào nhưng giữ đích sạch.

Với phạt thưa mềm,

$$
\mathcal L=\mathrm{MSE}(X,\hat X)+\lambda\Omega(Z).
$$

$\lambda$ cân bằng tái tạo và độ thưa. Top-$k$ là ràng buộc cứng: với từng mẫu, chỉ giữ $k$ phần tử mã theo tiêu chí đã chọn và đặt phần còn lại bằng 0. Hai cơ chế không đồng nhất.

Một lựa chọn cụ thể là $\Omega(Z)=\lVert Z\rVert_1/(Nd)$. Đây là ví dụ về phạt mềm, không phải định nghĩa duy nhất của $\Omega$.

![Mã thưa theo từng mẫu](img/lec-06/sparse-code.svg)

AE khử nhiễu nhận $\widetilde X$ nhưng tối ưu tái tạo $X$ sạch:

$$
Z=f_\theta(\widetilde X),\qquad
\hat X=g_\phi(Z),\qquad
\mathcal L=\frac{1}{ND}\lVert X-\hat X\rVert_F^2.
$$

![Luồng đầu vào nhiễu và đích sạch](img/lec-06/denoising-flow.svg)

::: exercise Câu hỏi kiểm tra
Với $d=32$, top-$k$ dùng $k=8$. Mỗi mẫu có tối đa bao nhiêu phần tử mã khác 0, và đích của AE khử nhiễu là tensor nào?
:::

::: solution
Mỗi mẫu có tối đa 8 phần tử được giữ. Đích khử nhiễu là $X$ sạch, không phải $\widetilde X$.
:::

Giá trị của mã được kiểm tiếp bằng hiệu năng trên một tác vụ đích và dữ liệu chưa thấy.

### Cụm 6: Tái sử dụng bộ mã hóa

Sau tiền huấn luyện, bộ giải mã có thể được bỏ và $Z$ được đưa vào một đầu phân loại có tham số $\psi$.

![Tái sử dụng bộ mã hóa cho tác vụ đích](img/lec-06/downstream-reuse.svg)

Đóng băng dùng stop-gradient qua bộ mã hóa:

$$
Z=\operatorname{stopgrad}(f_{\theta^\star}(X)),\qquad \Delta\theta=0.
$$

Chỉ $\psi$ thuộc bộ tối ưu. Tinh chỉnh cho phép cập nhật một phần hoặc toàn bộ $\theta$ cùng với $\psi$.

![Đóng băng và tinh chỉnh](img/lec-06/freeze-finetune.svg)

Việc có gradient và chế độ mô-đun là hai quyết định riêng. `eval()` có thể đổi hành vi của bỏ nút ngẫu nhiên hoặc chuẩn hóa theo lô; stop-gradient chỉ chặn cập nhật tham số. Khi suy luận cuối, toàn mô hình chạy ở chế độ suy luận.

Tiền huấn luyện chỉ dùng phần huấn luyện. Chọn $d$, $\lambda$, mức nhiễu và chính sách tinh chỉnh trên kiểm định. Đánh giá kiểm tra một lần sau khi chốt cấu hình.

::: exercise Câu hỏi kiểm tra
Khi đóng băng bộ mã hóa, tham số nào thuộc bộ tối ưu? `eval()` khác stop-gradient ở điểm nào?
:::

::: solution
Chỉ tham số đầu tác vụ $\psi$ thuộc bộ tối ưu. `eval()` đổi hành vi lượt xuôi của các mô-đun có trạng thái; stop-gradient chặn cập nhật $\theta$.
:::

Một mã hữu ích cho tác vụ đích vẫn chưa cung cấp quy tắc lấy mẫu cho bộ giải mã.

### Cụm 7: Mã tùy ý không có bảo đảm tái tạo

Mất mát AE thường chỉ ràng buộc bộ giải mã tại các mã do bộ mã hóa tạo:

$$
z^{(n)}=f_\theta(x^{(n)}).
$$

![Mã quan sát và mã lấy tùy ý](img/lec-06/sampling-latent.svg)

Một mã tùy ý có thể nằm ngoài vùng mã đã được quan sát. Khi đó $g_\phi(z)$ là ngoại suy của bộ giải mã và không có bảo đảm tạo ảnh hợp lệ.

![Vùng mã được bộ giải mã hỗ trợ](img/lec-06/decoder-support.svg)

AE thông thường không định nghĩa một phân phối lấy mẫu cho $Z$. Không được tự giả sử $z\sim\mathcal N(0,I)$. Mạng tự mã hóa biến phân (variational autoencoder, VAE) bổ sung một mô hình xác suất cho mã, nhưng nằm ngoài phạm vi bài.

::: exercise Câu hỏi kiểm tra
Vì sao không thể lấy $z\sim\mathcal N(0,I)$ rồi xem $g_\phi(z)$ là một mẫu hợp lệ của AE thông thường?
:::

::: solution
Mất mát chỉ huấn luyện bộ giải mã tại các mã do bộ mã hóa tạo; AE thường không khóa phân phối chuẩn cho $Z$. Mã lấy tùy ý có thể nằm ngoài vùng đã được ràng buộc.
:::

Giới hạn lấy mẫu làm nổi bật hai câu hỏi riêng: dữ liệu được biểu diễn trên cấu trúc nào và biểu diễn đó hữu ích cho tác vụ nào.

## Phần bổ sung: cấu trúc của không gian biểu diễn

Biểu diễn có thể làm một phép toán đơn giản hoặc phức tạp hơn. Chẳng hạn, $210/6=35$ dễ tính trong hệ thập phân; cùng phép chia với số La Mã $\mathrm{CCX}/\mathrm{VI}=\mathrm{XXXV}$ đòi hỏi thêm bước chuyển biểu diễn. Ví dụ này minh họa chi phí thao tác, không xếp hạng mọi hệ biểu diễn.

Trong trường hợp tuyến tính với mất mát bình phương và các điều kiện phù hợp, không gian con mà AE học có quan hệ với không gian con thành phần chính của PCA. Đây là kết quả có điều kiện, không áp dụng trực tiếp cho mọi AE phi tuyến.

![Không gian con tuyến tính của PCA](img/lec-06/pca-subspace.svg)

AE phi tuyến có thể biểu diễn dữ liệu tập trung gần một cấu trúc cong chiều thấp. Hình học của mã vẫn phải được kiểm bằng dữ liệu và tác vụ; hình đa tạp không tự chứng minh rằng nội suy hay lấy mẫu tùy ý là hợp lệ.

![Một đa tạp phi tuyến chiều thấp](img/lec-06/nonlinear-manifold.svg)

Ba ký hiệu kiểm soát ba cơ chế khác nhau: $d$ là chiều mã, $k$ là số phần tử được giữ bởi ràng buộc cứng và $\Omega$ là hàm phạt mềm. Không thay một ký hiệu cho ký hiệu khác khi so sánh các biến thể.

Độ hữu ích của biểu diễn phụ thuộc tác vụ. Cùng một mã có thể phù hợp cho phân loại nhưng không phù hợp cho tái tạo chi tiết. Giao thức đánh giá phải nêu tác vụ đích, tập dữ liệu chưa thấy và chính sách đóng băng hoặc tinh chỉnh.

## Từ công thức đến triển khai

1. khóa miền và kích thước từ $X_{\mathrm{img}}$ đến $\hat X$;
2. ghi rõ phép giảm của mất mát và mẫu số $ND$;
3. xác định ràng buộc nằm ở $d$, $\Omega$, top-$k$ hay quá trình tạo $\widetilde X$;
4. tách tham số có gradient khỏi chế độ mô-đun;
5. tách tập huấn luyện, kiểm định và kiểm tra ở cả tiền huấn luyện lẫn tác vụ đích;
6. chỉ lấy mẫu ở nơi có giả thiết hoặc dữ liệu hỗ trợ.

## Tự kiểm tra

1. Chuỗi kích thước của AE MNIST thay đổi thế nào? (Cụm 2.)
2. Vì sao SSE $0{,}18$ cho $D=4$ tương ứng MSE $0{,}045$? (Cụm 3.)
3. Vì sao $d<784$ không bảo đảm chống ghi nhớ? (Cụm 4.)
4. Phạt thưa mềm khác top-$k$ cứng ở đâu? (Cụm 5.)
5. Đóng băng tham số khác chế độ suy luận thế nào? (Cụm 6.)
6. Vì sao không được tự lấy $z\sim\mathcal N(0,I)$ cho AE thường? (Cụm 7.)

## Tài liệu tham khảo

- Đề cương học phần, III.2, Buổi 6; `source.md`, Buổi 06.
- `stanford-cs231n-2025-lecture13-generative-models.pdf`, PDF 63–70.
- `illinois-ece417-fa2023-lecture20-autoencoders.pdf`, PDF 4–14.
- `cmu-11785-s2021-representation-learning.pdf`, PDF 1–17.
- `cmu-11785-s2021-autoencoders.pdf`, PDF 2–7.
- `lec01_intro.pdf`, PDF 26–37; `lec09_cnn_architectures.pdf`, PDF 44–46; `lec11_dense.pdf`, PDF 3–10.
- `hocsau_draft.pdf`, PDF 38–40, 105–107 và 168–171.
