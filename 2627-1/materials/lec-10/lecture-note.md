# Buổi 10: Cơ chế chú ý

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- giải thích nút thắt của bộ mã hóa–giải mã khi mọi bước đích cùng phụ thuộc vào một vectơ ngữ cảnh cố định;
- mô tả vai trò của truy vấn, khóa và giá trị trong chú ý chéo;
- tính điểm, trọng số chú ý và vectơ ngữ cảnh trên một ví dụ nhỏ;
- kiểm tra kích thước tensor, trục softmax và mặt nạ nguồn trong chú ý cộng Bahdanau;
- nối cơ chế chú ý với cập nhật bộ giải mã, hàm mất mát và quá trình sinh tự hồi quy;
- đọc ma trận căn chỉnh mềm mà không đồng nhất trọng số chú ý với giải thích nhân quả.

Kiến thức tiên quyết: mạng nơ-ron truy hồi, bộ mã hóa–giải mã, softmax, chéo entropy, phép nhân ma trận theo lô, phát tự động và lan truyền ngược theo thời gian.

## Ký hiệu và hợp đồng tensor

Mỗi mẫu là một hàng. Chuỗi nguồn được đệm đến $T_s$ bước, chuỗi đích được đệm đến $T'$ bước và lô có $N$ mẫu.

| Đại lượng | Kích thước | Nghĩa |
|---|---|---|
| $H$ | $N\times T_s\times D_h$ | Các trạng thái bộ mã hóa |
| $S^-$ | $N\times D_s$ | Trạng thái bộ giải mã trước bước đang xét |
| $E$ | $N\times T_s$ | Điểm tương thích tại một bước đích |
| $A$ | $N\times T_s$ | Trọng số chú ý tại một bước đích |
| $C$ | $N\times D_h$ | Ngữ cảnh riêng cho bước đích |
| $L_n$ | vô hướng nguyên | Độ dài nguồn thật của mẫu $n$, gồm EOS |
| $M^{src}$ | $N\times T_s$ | Mặt nạ vị trí nguồn hợp lệ |
| $M^{tgt}$ | $N\times T'$ | Mặt nạ token đích tham gia hàm mất mát |
| $D_a$ | vô hướng nguyên | Chiều ẩn của mạng tính điểm cộng |
| $R_q,R_h$ | $N\times D_a$ và $N\times T_s\times D_a$ | Truy vấn và trạng thái nguồn sau phép chiếu trong mạng điểm |
| $E_y$ | $V_{tgt}\times D_e$ | Ma trận nhúng từ vựng đích |
| $y_{n,t'}$ | token rời rạc | Token đích đúng của mẫu $n$ tại bước $t'$ |
| $g$ | hàm | Ô truy hồi của bộ giải mã, như RNN hoặc GRU |
| $W_o,b_o$ | $(D_s+D_h)\times V_{tgt}$ và $V_{tgt}$ | Tham số chiếu trạng thái và ngữ cảnh thành logit |
| $O$ | $N\times T'\times V_{tgt}$ | Logit đầu ra của toàn chuỗi đích |
| $\mathcal A$ | $T'\times T_s$ | Ma trận căn chỉnh của một mẫu |

Ở một mẫu và một bước đích, đặt

$$
q=s_{t'-1},\qquad k_i=v_i=h_i.
$$

Truy vấn đến từ trạng thái bộ giải mã trước đó. Khóa và giá trị cùng lấy từ trạng thái bộ mã hóa, nhưng tham gia hai nhánh khác nhau: khóa dùng để tính điểm, còn giá trị dùng để tạo ngữ cảnh.

## Khái niệm trọng tâm

### Cụm 1: Nút thắt của một ngữ cảnh cố định

Trong bộ mã hóa–giải mã cơ sở, toàn bộ chuỗi nguồn được nén vào một vectơ. Bài này dùng biến thể trong đó trạng thái mã hóa cuối hợp lệ khởi tạo bộ giải mã:

$$
s_{n,0}=\phi\!\left(h^{enc}_{n,L_n}\right)\in\mathbb R^{D_s}.
$$

$\phi$ là phép đồng nhất khi hai chiều trạng thái bằng nhau, hoặc một phép chiếu học được. Không lấy trạng thái ở vị trí đệm. Với LSTM, cần phân biệt trạng thái ẩn dùng làm truy vấn với trạng thái ô nội bộ.

![Một vectơ ngữ cảnh cố định phục vụ mọi bước đích](img/lec-10/bottleneck.svg)

Thiết kế này buộc một biểu diễn hữu hạn phục vụ mọi quyết định ở phía đích. Khi chuỗi dài, trật tự từ giữa hai ngôn ngữ khác nhau hoặc một bước đích cần một phần nguồn cụ thể, việc truy xuất thông tin trở nên khó hơn. Chú ý làm giảm nút thắt này bằng cách tạo một ngữ cảnh mới ở từng bước đích; nó không bảo đảm loại bỏ mọi giới hạn của mạng truy hồi.

::: exercise Câu hỏi kiểm tra
Một câu nguồn có độ dài thật 7, gồm EOS, rồi được đệm lên 10. Trạng thái nào được dùng để khởi tạo bộ giải mã trong biến thể cơ sở của bài?
:::

::: solution
Dùng trạng thái mã hóa ở vị trí hợp lệ cuối cùng, tức $h^{enc}_{n,L_n}$ với $L_n=7$, không dùng trạng thái ở vị trí đệm thứ 10.
:::

### Cụm 2: Truy xuất nguồn theo từng bước đích

Ở mỗi bước $t'$, chú ý thực hiện ba phép tính:

1. so sánh truy vấn $s_{t'-1}$ với từng khóa $h_i$ để tạo điểm $e_{t',i}$;
2. chuẩn hóa các điểm trên trục vị trí nguồn để tạo trọng số $\alpha_{t',i}$;
3. lấy tổng có trọng số của các giá trị $h_i$ để tạo $c_{t'}$.

![Luồng chú ý chéo từ truy vấn và trạng thái nguồn đến ngữ cảnh](img/lec-10/cross-attention.svg)

Dạng tổng quát là

$$
\operatorname{Attention}\!\left(q,\{(k_i,v_i)\}_{i=1}^{T_s}\right)
=\sum_{i=1}^{T_s}\alpha(q,k_i)v_i.
$$

Khái niệm chú ý tổng quát không buộc mọi cách đặt $\alpha$ phải là một phân phối xác suất. Hàm $\alpha$ cụ thể sẽ được xây ở Cụm 4; Cụm 3 dùng điểm cho sẵn để tách riêng phép chuẩn hóa và tổng hợp. Trong cơ chế Bahdanau của bài này, $\alpha$ được tạo bởi softmax nên không âm và có tổng bằng 1 trên các vị trí nguồn hợp lệ. Vì vậy $c_{t'}$ là một tổ hợp lồi của các giá trị hợp lệ.

::: exercise Câu hỏi kiểm tra
Trong chú ý chéo Bahdanau cho dịch máy, đại lượng nào thay đổi theo bước đích dù các trạng thái mã hóa đã được tính xong?
:::

::: solution
Truy vấn $s_{t'-1}$ thay đổi, nên điểm $e_{t',i}$, trọng số $\alpha_{t',i}$ và ngữ cảnh $c_{t'}$ cũng thay đổi theo bước đích.
:::

### Cụm 3: Một vết tính hoàn chỉnh

Xét một mẫu có ba trạng thái nguồn hai chiều và ba điểm đã cho:

$$
H=[(1,0),(0,2),(-1,1)],\qquad e=(1,2,0).
$$

Softmax ổn định trừ điểm lớn nhất trước khi lấy hàm mũ:

$$
\alpha_i=\frac{\exp(e_i-m)}{\sum_j\exp(e_j-m)},
\qquad m=\max_j e_j.
$$

Với $m=2$,

$$
(\exp(-1),\exp(0),\exp(-2))
\approx(0{,}3679,1,0{,}1353).
$$

Do đó

$$
\alpha\approx(0{,}244728,0{,}665241,0{,}090031).
$$

Ngữ cảnh là

$$
c=\sum_{i=1}^{3}\alpha_i h_i
\approx(0{,}154698,1{,}420512).
$$

![Vết tính từ điểm qua softmax đến vectơ ngữ cảnh](img/lec-10/trace-attention.svg)

Trục nguồn bị rút gọn khi tính tổng: $A$ có kích thước $N\times T_s$, $H$ có kích thước $N\times T_s\times D_h$, còn $C$ có kích thước $N\times D_h$. Mỗi trọng số được phát trên $D_h$ thành phần của giá trị tương ứng.

::: exercise Câu hỏi kiểm tra
Tự tính $\alpha$ và $c$ từ $H,e$. Kiểm tra ba điều: $\alpha_i\ge0$, $\sum_i\alpha_i=1$ và $c$ có hai thành phần.
:::

::: solution
$\alpha\approx(0{,}244728,0{,}665241,0{,}090031)$ và $c\approx(0{,}154698,1{,}420512)$. Các hệ số không âm, tổng bằng 1 nếu dùng số đầy đủ, và tổng trên ba vị trí nguồn để lại chiều giá trị $D_h=2$.
:::

### Cụm 4: Hàm điểm cộng Bahdanau và mặt nạ

Điểm phải phụ thuộc đồng thời vào truy vấn và từng vị trí nguồn; nó không được cho sẵn trong mô hình. Với quy ước vectơ hàng, mạng điểm cộng dùng

$$
u_{n,t',i}=\tanh\!\left(
s_{n,t'-1}W_s+h_{n,i}W_h+b_a
\right)\in\mathbb R^{1\times D_a},
$$

$$
e_{n,t',i}=u_{n,t',i}v_a\in\mathbb R.
$$

Ba điểm $e=(1,2,0)$ ở Cụm 3 có thể được xem là đầu ra của mạng này tại một bước đích.

Trong đó

$$
W_s\in\mathbb R^{D_s\times D_a},\quad
W_h\in\mathbb R^{D_h\times D_a},\quad
b_a\in\mathbb R^{1\times D_a},\quad
v_a\in\mathbb R^{D_a\times1}.
$$

![Mạng tính điểm cộng Bahdanau](img/lec-10/bahdanau-score.svg)

Số tham số của mạng điểm cộng là

$$
D_sD_a+D_hD_a+D_a+D_a
=D_a(D_s+D_h+2).
$$

Con số này không gồm tham số của phép chiếu khởi tạo $\phi$ hay tầng đầu ra $W_o,b_o$.

Khi tính theo lô, $S^-W_s$ có kích thước $N\times D_a$ và được thêm một trục nguồn; $HW_h$ có kích thước $N\times T_s\times D_a$. Phép phát tự động dùng lại từng hàng truy vấn trên $T_s$ vị trí nguồn. Sau $\tanh$, phép nhân với $v_a$ co chiều $D_a$ để tạo $E\in\mathbb R^{N\times T_s}$.

Vị trí đệm phải bị loại trước softmax:

$$
\widetilde e_{n,i}=
\begin{cases}
e_{n,i}, & M^{src}_{n,i}=1,\\
-\infty, & M^{src}_{n,i}=0,
\end{cases}
\qquad
A=\operatorname{softmax}_{T_s}(\widetilde E).
$$

Mỗi hàng phải có ít nhất một vị trí hợp lệ; EOS bảo đảm điều kiện này trong dữ liệu đã chuẩn hóa. Nếu thư viện không hỗ trợ $-\infty$ ổn định, có thể dùng một số âm rất lớn, nhưng khi đó trọng số đệm chỉ xấp xỉ 0 và hàng bị che toàn bộ vẫn cần xử lý riêng.

Trong vết số trên, nếu vị trí thứ ba là đệm thì

$$
\alpha\approx(0{,}268941,0{,}731059,0),
\qquad
c\approx(0{,}268941,1{,}462117).
$$

::: exercise Câu hỏi kiểm tra
Vì sao đặt trọng số đệm về 0 sau softmax rồi giữ nguyên các trọng số còn lại là sai?
:::

::: solution
Các trọng số hợp lệ khi đó không còn tổng bằng 1. Mặt nạ phải được áp dụng trước softmax, hoặc phải chuẩn hóa lại đúng trên tập vị trí hợp lệ.
:::

### Cụm 5: Nối ngữ cảnh vào bộ giải mã

Một bước giải mã nhận token đích trước đó, trạng thái trước đó và ngữ cảnh vừa tính:

$$
s_{t'}=g\!\left(s_{t'-1},[E_y(y_{t'-1});c_{t'}]\right).
$$

Bài dùng quy ước token đầu vào là $y_{t'-1}$. Các tài liệu khác có thể dịch chỉ số thời gian; vì vậy phải kiểm tra định nghĩa bước khi đối chiếu công thức.

Logit và xác suất đầu ra theo quy ước vectơ hàng là

$$
O_{t'}=[s_{t'};c_{t'}]W_o+b_o,
\qquad
P_{t'}=\operatorname{softmax}_{V_{tgt}}(O_{t'}).
$$

Đầu vào $[E_y(y_{t'-1});c_{t'}]$ của $g$ có chiều $D_e+D_h$; cấu hình ô truy hồi phải nhận đúng chiều này. Softmax chú ý chạy trên $T_s$ vị trí nguồn; softmax đầu ra chạy trên $V_{tgt}$ mục từ vựng. Hai phép chuẩn hóa không dùng chung trục.

![Đầu vào bộ giải mã khi huấn luyện và khi suy luận](img/lec-10/train-infer.svg)

Khi huấn luyện bằng học theo đáp án, bước $t'$ nhận token đúng $y_{t'-1}$. Khi suy luận, nó nhận token vừa dự đoán ở bước trước và dừng khi sinh EOS hoặc đạt giới hạn độ dài. Trong suy luận theo lô, mẫu đã sinh EOS phải giữ nguyên trạng thái bằng mặt nạ hoạt động hoặc được loại khỏi lô đang chạy.

Trong hàm mất mát, $y_{n,t'}$ là token đúng cần dự đoán tại bước $t'$; cùng chuỗi đích được dịch một bước để $y_{t'-1}$ làm đầu vào bộ giải mã. Hàm mất mát trung bình trên các token đích hợp lệ là

$$
\mathcal L=
\frac{
-\sum_{n=1}^{N}\sum_{t'=1}^{T'}
M^{tgt}_{n,t'}\log P_{n,t',y_{n,t'}}
}{
\sum_{n=1}^{N}\sum_{t'=1}^{T'}M^{tgt}_{n,t'}
}.
$$

Mặt nạ nguồn điều khiển vị trí được chú ý; mặt nạ đích điều khiển token tham gia mất mát. Đó là hai chức năng khác nhau.

Trong triển khai, dùng chéo entropy hợp nhất từ logit hoặc log-softmax ổn định. Công thức qua $P$ ở trên chỉ làm rõ vị trí của mặt nạ đích.

::: exercise Câu hỏi kiểm tra
Một tensor logit có kích thước $8\times12\times5000$. Nêu trục softmax đầu ra và đại lượng bị rút gọn khi tính chéo entropy trung bình có mặt nạ.
:::

::: solution
Softmax đầu ra chạy trên trục từ vựng kích thước 5000. Chéo entropy chọn logit của nhãn đúng, dùng $M^{tgt}$ để lấy tổng trên các mẫu và trục $T'=12$ bước đích hợp lệ, rồi chia cho số token hợp lệ.
:::

### Cụm 6: Căn chỉnh mềm và giới hạn diễn giải

Với một mẫu, xếp các hàng $\alpha_{t',:}$ theo thời gian đích tạo ma trận căn chỉnh

$$
\mathcal A\in\mathbb R^{T'\times T_s},
\qquad \mathcal A_{t',:}=\alpha_{t',:}.
$$

Mỗi hàng cho biết phân bố trọng số trên các vị trí nguồn tại một bước đích. Hình dùng $T'=T_s=3$; các điểm được cho để minh họa cách cực đại có thể đổi vị trí giữa các bước.

![Ba hàng trọng số chú ý tạo một ma trận căn chỉnh mềm](img/lec-10/alignment.svg)

Ô lớn chỉ cho biết vị trí nguồn nhận trọng số lớn trong phép tính đang xét. Nó không tự chứng minh quan hệ ngôn ngữ học, không cho biết một token là nguyên nhân của dự đoán và không bảo đảm mô hình dùng thông tin theo cách con người diễn giải. Muốn lập luận nhân quả cần một kiểm tra can thiệp, chẳng hạn thay đổi hoặc che một phần đầu vào rồi đo tác động lên đầu ra trong một giao thức rõ ràng.

::: exercise Câu hỏi kiểm tra
Phản biện mệnh đề: “Ô lớn nhất trong mỗi hàng chứng minh từ nguồn tương ứng gây ra token đích.”
:::

::: solution
Trọng số chỉ là hệ số trong một phép tổng của mô hình. Các đường tính khác, biểu diễn đã trộn ngữ cảnh và tính phụ thuộc giữa các biến khiến trọng số không đủ làm bằng chứng nhân quả. Cần kiểm tra can thiệp và đo thay đổi đầu ra.
:::

### Cụm 7: Thuật toán, gradient và chi phí

Một bước giải mã có chú ý gồm sáu việc:

1. áp dụng $W_s$ cho truy vấn và $W_h$ cho trạng thái nguồn trong mạng điểm;
2. tạo điểm Bahdanau cho từng cặp bước đích–vị trí nguồn;
3. áp dụng mặt nạ nguồn rồi softmax trên $T_s$;
4. lấy tổng giá trị có trọng số để tạo $c_{t'}$;
5. cập nhật trạng thái giải mã từ $y_{t'-1}$ và $c_{t'}$;
6. tạo logit, xác suất và phần mất mát của token hợp lệ.

Có ba đường đạo hàm cần phân biệt: đường giá trị qua tổng có trọng số, đường khóa qua điểm rồi softmax và đường truy vấn về trạng thái giải mã trước. Đường truy vấn tiếp tục qua các bước đích trước bằng lan truyền ngược theo thời gian; hai đường đầu tiếp tục về bộ mã hóa.

Nếu chiếu trạng thái nguồn một lần, chi phí của riêng khối chú ý là

$$
\Theta\!\left(
NT_sD_hD_a
+NT'D_sD_a
+NT'T_s(D_a+D_h)
\right).
$$

Hai ma trận điểm và trọng số cần $\Theta(NT'T_s)$ ô nhớ. Nếu lưu toàn bộ kích hoạt ẩn của mạng điểm để lan truyền ngược, phần này có thể cần $\Theta(NT'T_sD_a)$ ô nhớ.

Phép chiếu logit ở bộ giải mã có chi phí riêng $\Theta(NT'(D_s+D_h)V_{tgt})$ và không nằm trong biểu thức của khối chú ý trên.

So với một ngữ cảnh cố định, chú ý trả thêm chi phí theo từng cặp bước đích–vị trí nguồn để đổi lấy khả năng truy xuất nguồn động. Đây là đánh đổi về biểu diễn và tính toán, không phải bảo đảm chất lượng đầu ra.

::: exercise Câu hỏi kiểm tra
Trong biểu thức chi phí, hạng nào tăng đồng thời theo $T'$ và $T_s$? Hai thành phần trong hạng đó phản ánh những phép tính nào?
:::

::: solution
Hạng $NT'T_s(D_a+D_h)$ tăng theo cả hai độ dài. Thành phần $D_a$ gắn với việc thu gọn kích hoạt mạng điểm bằng $v_a$; thành phần $D_h$ gắn với tổng các giá trị theo trọng số.
:::

## Mở rộng: Giữ cơ chế, đổi nguồn của khóa và giá trị

Khung truy vấn–khóa–giá trị không phụ thuộc riêng vào dịch máy.

![Ánh xạ truy vấn, khóa và giá trị trong ba miền](img/lec-10/applications.svg)

- Trong mô tả ảnh, trạng thái bộ giải mã là truy vấn; đặc trưng của các vùng ảnh cung cấp khóa và giá trị.
- Trong tra cứu trên một tập, truy vấn so khớp với khóa của từng phần tử rồi tổng hợp các giá trị.
- Với một cặp văn bản, token của một câu có thể truy xuất biểu diễn token của câu kia; làm theo hai chiều tạo hai ma trận căn chỉnh mềm.

Trục softmax luôn phải được nêu theo tập phần tử đang được truy xuất. Ở Buổi 11, truy vấn, khóa và giá trị có thể cùng được tạo từ một chuỗi. Cầu nối này chỉ đổi nguồn của ba vai trò; công thức tự chú ý được phát triển ở buổi sau.

## Tổng kết

- Ngữ cảnh cố định nén toàn bộ nguồn vào một vectơ dùng chung; chú ý tạo ngữ cảnh riêng theo bước đích.
- Bahdanau dùng trạng thái giải mã trước làm truy vấn và trạng thái mã hóa làm cả khóa lẫn giá trị.
- Mặt nạ nguồn được áp dụng trước softmax trên trục $T_s$; softmax đầu ra chạy trên trục từ vựng.
- Ngữ cảnh, cập nhật bộ giải mã, logit và mất mát phải giữ cùng quy ước chỉ số và kích thước.
- Ma trận chú ý hỗ trợ quan sát căn chỉnh mềm nhưng không phải bằng chứng nhân quả.
- Ở Buổi 11, cả ba vai trò truy vấn, khóa và giá trị sẽ cùng được tạo từ một chuỗi.

## Bài tập 50 phút

1. **Phân tích nút thắt — 10 phút.** So sánh bộ mã hóa–giải mã dùng một ngữ cảnh cố định với biến thể tạo ngữ cảnh theo bước. Nêu hai hạn chế cụ thể của thiết kế cố định và cơ chế mà chú ý dùng để giảm mỗi hạn chế.
2. **Tính chú ý trên ma trận nhỏ — 20 phút.** Dùng $H=[(1,0),(0,2),(-1,1)]$ và $e=(1,2,0)$ để tính softmax ổn định, $\alpha$ và $c$. Lặp lại khi vị trí thứ ba là đệm. Ghi rõ trục chuẩn hóa và kiểm tra tổng trọng số.
3. **Đọc căn chỉnh — 15 phút.** Chọn ba hàng trong ma trận căn chỉnh của hình. Với mỗi hàng, nêu vị trí có trọng số lớn nhất và một nhận xét chỉ dựa trên dữ liệu nhìn thấy. Không gán quan hệ ngôn ngữ học nếu chưa có bằng chứng.
4. **Giới hạn diễn giải — 5 phút.** Viết một phản biện ngắn cho mệnh đề “trọng số lớn nhất là nguyên nhân của dự đoán”, rồi đề xuất một phép can thiệp có thể kiểm tra mệnh đề đó.

## Nguồn

- Đề cương học phần, mục III.2, Buổi 10: tên buổi, LLO19–LLO20 và phạm vi cơ chế chú ý.
- `source-materials/slides/lec15_attention.pdf`, trang PDF 3–14: nút thắt bộ mã hóa–giải mã, ngữ cảnh theo bước và căn chỉnh.
- `source-materials/slides/lec15_attention.pdf`, trang PDF 19–27: mở rộng sang mô tả ảnh.
- `source-materials/slides/lec15_attention.pdf`, trang PDF 30–41: vai trò truy vấn, khóa, giá trị và cầu nối tối thiểu sang tự chú ý.
- `source-materials/textbooks/hocsau_draft.pdf`, trang PDF 239–245: bộ mã hóa–giải mã, học theo đáp án và mặt nạ đích.
- `source-materials/textbooks/hocsau_draft.pdf`, trang PDF 258–263: chú ý tổng quát, Bahdanau, căn chỉnh và giới hạn diễn giải.
- `source-materials/textbooks/hocsau_draft.pdf`, trang PDF 323–327: căn chỉnh chú ý cho cặp văn bản.
