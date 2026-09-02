# Buổi 01 — Từ biến đổi afin đến MLP ReLU giải XOR

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, bạn có thể:

- Giải thích vì sao một số tác vụ khó viết quy tắc tay và cần học từ dữ liệu.
- Phân biệt biến đổi tuyến tính $Wx$ với biến đổi afin $Wx+b$, và phân biệt logit với xác suất.
- Chứng minh trực quan rằng XOR không tách được bằng một biên afin, dùng bao lồi.
- Mô tả cấu trúc MLP (tầng vào, tầng ẩn, tầng ra), quy ước ưu tiên chiều lô, kích thước tensor, quảng bá kích thước và số tham số.
- Tính lan truyền xuôi cho mạng ReLU 2–2–1 giải XOR và kiểm tra kết quả bằng tay.
- Giải thích khái quát sức biểu diễn của mạng nhiều lớp, cùng giới hạn giữa biểu diễn được và dễ huấn luyện.

Kiến thức tiên quyết: đại số ma trận cơ bản (nhân ma trận, cộng vector), khái niệm hàm số và đồ thị, và ý tưởng sơ khai về phân loại nhị phân.

## Ký hiệu và quy ước

- **Ưu tiên chiều lô (batch-first):** mỗi hàng của $X\in\mathbb R^{B\times d}$ là một mẫu $x_i^\top$; $B$ là số mẫu trong lô, $d$ là số đặc trưng.
- Tầng ẩn có $h$ nơ-ron, tầng ra có $k$ nơ-ron. Ma trận trọng số $W_1\in\mathbb R^{d\times h}$, $W_2\in\mathbb R^{h\times k}$; độ chệch (bias) $b_1\in\mathbb R^{h}$, $b_2\in\mathbb R^{k}$.
- **Quảng bá kích thước (broadcasting):** khi cộng $b_1$ vào $XW_1\in\mathbb R^{B\times h}$, cùng một vector độ chệch được cộng vào từng hàng.
- **Chuỗi ký hiệu:**
  $$
  A = XW_1+b_1, \qquad H = \operatorname{ReLU}(A), \qquad z = H W_2+b_2, \qquad p = \sigma(z), \qquad \hat y = \mathbf 1[p\ge 0.5].
  $$
  Với tầng ra nhiều lớp, ma trận logit dùng ký hiệu hoa $Z$; riêng mạng XOR chỉ có một đầu ra nên logit dùng chữ thường $z$.
- Mọi phép tính trong buổi này là suy luận (inference) trên dữ liệu đã cho, không phải huấn luyện.

## Khái niệm trọng tâm

### Vấn đề và bối cảnh: tác vụ khó viết quy tắc

Nhiều tác vụ nhận dạng khó diễn đạt bằng một danh sách quy tắc đủ để bao quát mọi trường hợp, chẳng hạn phân biệt ảnh mèo và ảnh chó. Thay vì viết quy tắc, ta để mô hình **học từ dữ liệu**: cho trước các cặp (đầu vào, nhãn), mô hình tự điều chỉnh tham số để khớp dữ liệu. Khung này gồm ba thành phần: dữ liệu, mô hình và tiêu chí khớp; tham số là đại lượng được điều chỉnh bên trong mô hình.

::: example Ví dụ tính được
Cho bốn mẫu nhị phân $(0,0),(0,1),(1,0),(1,1)$ với nhãn XOR $(0,1,1,0)$. Đây là dữ liệu; mô hình là một hàm có tham số; tham số được chọn để khớp nhãn; tiêu chí khớp đo độ sai lệch giữa dự đoán và nhãn. Trong buổi này ta dùng chính bốn mẫu này xuyên suốt.
:::

### Học từ dữ liệu: phân biệt các khái niệm

- **Dữ liệu:** các mẫu đầu vào và nhãn tương ứng.
- **Mô hình:** họ hàm số có tham số, ví dụ một biến đổi afin.
- **Tham số:** các giá trị số trong mô hình được điều chỉnh khi học.
- **Huấn luyện:** quá trình điều chỉnh tham số để giảm sai lệch so với nhãn.
- **Suy luận:** dùng mô hình đã có tham số để dự đoán trên mẫu mới.

Bài toán ở đây là **phân loại nhị phân có giám sát**: nhãn có sẵn và chỉ có hai lớp, mô hình được điều chỉnh theo đúng nhãn đó. Trong buổi này, các tham số của mạng XOR được **dựng tay** để minh họa lan truyền xuôi, không phải là kết quả của một quá trình huấn luyện.

*Tự kiểm tra:* xác định dữ liệu, nhãn và thành phần được điều chỉnh khi huấn luyện mô hình XOR.

### Biến đổi afin và biên quyết định

Một perceptron đơn tính $z = w^\top x + b$. Đây là biến đổi **afin**: phần tuyến tính $w^\top x$ cộng thêm độ chệch $b$. Nếu không có $b$, mọi biên đều đi qua gốc tọa độ; độ chệch cho phép dịch biên. Biên quyết định là tập các điểm thỏa $w^\top x + b = 0$, một siêu phẳng.

::: derivation Suy diễn chi tiết
Phân biệt tuyến tính và afin: biến đổi tuyến tính $f(x)=Wx$ thỏa $f(0)=0$; biến đổi afin $f(x)=Wx+b$ nói chung có $f(0)=b\neq 0$. Vì vậy một biên afin có dạng $Wx+b=0$, còn biên tuyến tính thuần túy là trường hợp riêng $b=0$.
:::

*Tự kiểm tra:* với $w=(1,-1)$ và $b=-0.5$, xác định giao điểm của biên quyết định với hai trục và phía chứa lớp dương.

### XOR không tách tuyến tính: chứng minh bằng bao lồi

Đối chiếu với AND và OR: cả hai đều tách được bằng một đường thẳng. XOR thì không. Bao lồi của một tập điểm là tập lồi nhỏ nhất chứa mọi điểm đó; với hai điểm, bao lồi chính là đoạn thẳng nối chúng.

![Bốn điểm XOR; hai đoạn nối các điểm cùng lớp giao nhau tại tâm hình vuông.](img/lec-01/xor-points.svg)

::: proof Chứng minh
**Mục tiêu:** chứng minh không tồn tại biên afin tách hai lớp của XOR.

**Ý tưởng:** hai tập điểm tách được bằng một siêu phẳng khi và chỉ khi bao lồi của chúng rời nhau.

**Các bước then chốt:**
1. Lớp nhãn $0$ gồm $(0,0)$ và $(1,1)$; bao lồi của chúng là đoạn thẳng nối hai điểm, chứa điểm $(0.5,0.5)$.
2. Lớp nhãn $1$ gồm $(0,1)$ và $(1,0)$; bao lồi của chúng là đoạn thẳng nối hai điểm, cũng chứa điểm $(0.5,0.5)$.
3. Hai bao lồi cùng chứa $(0.5,0.5)$ nên chúng giao nhau, tức không rời nhau.

**Kết luận:** hai lớp không tách được bằng một biên afin. Đây là lý do cần nhiều hơn một biến đổi afin.
:::

*Tự kiểm tra:* chỉ ra hai cặp điểm cùng lớp tạo nên hai đoạn thẳng cắt nhau tại tâm hình vuông.

### Hợp thành và vai trò của phi tuyến

Hợp thành hai biến đổi afin vẫn là một biến đổi afin: $W_2(W_1x+b_1)+b_2 = (W_2W_1)x + (W_2b_1+b_2)$. Vì vậy, nếu chỉ xếp chồng các tầng afin, mạng không học được gì hơn một biến đổi afin duy nhất. Hàm kích hoạt **phi tuyến** phá vỡ tính afin của phép hợp thành; tác dụng cụ thể còn phụ thuộc vào hàm và bài toán.

*Tự kiểm tra:* rút gọn hợp thành của hai phép afin về dạng một phép afin duy nhất.

### Cấu trúc MLP

MLP gồm tầng vào (dữ liệu $X$), một hoặc nhiều tầng ẩn, và tầng ra. Với một tầng ẩn, lan truyền xuôi là chuỗi $A = XW_1+b_1$, $H = \operatorname{ReLU}(A)$, $Z = H W_2+b_2$:

$$
A = XW_1 + b_1, \qquad H = \operatorname{ReLU}(A), \qquad Z = H W_2 + b_2.
$$

Ở đây $XW_1+b_1$ là phép afin theo chiều lô, với $b_1$ được quảng bá kích thước theo chiều lô như đã nêu ở phần ký hiệu.

::: example Ví dụ tính được
Với $B=32$, $d=10$, $h=20$, $k=3$: $X$ có kích thước $32\times10$, $H$ có kích thước $32\times20$, $Z$ có kích thước $32\times3$. Số tham số là $10\cdot20+20+20\cdot3+3=283$.
:::

*Tự kiểm tra:* xác định kích thước $Z$ và số tham số khi tăng $h$ lên gấp đôi.

### Hàm kích hoạt và tầng ra

- **ReLU:** $\operatorname{ReLU}(u)=\max(0,u)$. Không khả vi tại $0$ và khả vi gần như mọi nơi. Mạng ReLU tạo ánh xạ tuyến tính từng đoạn: trên mỗi vùng của không gian đầu vào, mạng rút gọn thành một biến đổi afin khác nhau.
- **Sigmoid:** $\sigma(u)=1/(1+e^{-u})$, nén về $(0,1)$, dùng cho xác suất nhị phân.
- **tanh:** nén về $(-1,1)$.

Tầng ra được chọn theo bài toán. Với phân loại nhị phân, ta dùng một nơ-ron ra với sigmoid để biến logit thành xác suất. **Logit** là giá trị $z$ trước khi qua sigmoid; **xác suất** là $\sigma(z)$. Với phân loại nhiều lớp, softmax được tính theo trục lớp; trừ logit lớn nhất trước khi lũy thừa giúp tránh tràn số mà không đổi kết quả.

*Tự kiểm tra:* với logit $z=0.5$, tính $\sigma(0.5)$ và xác định $\hat y$ theo ngưỡng $0.5$.

### MLP ReLU 2–2–1 giải XOR

Ta dựng tay mạng 2–2–1 với các tham số:

$$
W_1=\begin{bmatrix}1&1\\1&1\end{bmatrix},\quad
b_1=(0,\,-1),\quad
W_2=\begin{bmatrix}1\\-2\end{bmatrix},\quad b_2=-0.5.
$$

![Mạng MLP 2–2–1 với hai nơ-ron ReLU ẩn và một đầu ra sigmoid dùng để giải XOR.](img/lec-01/xor-mlp.svg)

::: derivation Suy diễn chi tiết
Tính $XW_1$ cho từng hàng $(a,b)$: mỗi hàng cho $(a+b,\ a+b)$. Cộng $b_1=(0,-1)$ — một **vector hàng được quảng bá theo chiều lô**, tức cùng giá trị này được cộng vào mỗi hàng — ta được $A=XW_1+b_1$, rồi áp ReLU:

- $(0,0)$: $(0,-1)\to(0,0)$.
- $(0,1)$: $(1,0)\to(1,0)$.
- $(1,0)$: $(1,0)\to(1,0)$.
- $(1,1)$: $(2,1)\to(2,1)$.

Vậy $H=\operatorname{ReLU}(A)$ có các hàng $(0,0),(1,0),(1,0),(2,1)$. Hình học: trong không gian ẩn, biểu diễn $(1,0)$ của lớp $1$ tách khỏi $(0,0)$ và $(2,1)$ của lớp $0$, nên tầng ra chỉ cần một biên afin để tách các biểu diễn đó. Tiếp theo $z = H W_2 + b_2$:

- $(0,0)$: $0\cdot1+0\cdot(-2)-0.5=-0.5$.
- $(1,0)$: $1\cdot1+0\cdot(-2)-0.5=0.5$.
- $(1,0)$: $0.5$.
- $(2,1)$: $2\cdot1+1\cdot(-2)-0.5=-0.5$.

Logit là $(-0.5,0.5,0.5,-0.5)^\top$. Qua sigmoid: $\sigma(-0.5)\approx0.378$, $\sigma(0.5)\approx0.622$, nên xác suất xấp xỉ $(0.378,0.622,0.622,0.378)^\top$. Ngưỡng $p\ge0.5$ cho dự đoán $\hat y = (0,1,1,0)^\top$, đúng XOR.
:::

Số tham số của mạng này là $2\cdot2+2+2\cdot1+1=9$.

::: exercise Câu hỏi kiểm tra
Vì sao hai tầng afin xếp chồng không giải được XOR, nhưng mạng ReLU 2–2–1 ở trên lại giải được?
:::

::: hint
Xét phép hợp thành hai biến đổi afin có còn là afin không, và ReLU đã phá vỡ tính afin đó như thế nào.
:::

::: solution
Đối chiếu: hợp thành hai phép afin vẫn là afin; ReLU phá vỡ tính afin của phép hợp thành.
:::

::: exercise Tính tay một mẫu
Dùng chuỗi ký hiệu $A\to H\to z\to p\to\hat y$ để tính lan truyền xuôi cho mẫu $(0,1)$.
:::

::: hint
Áp lần lượt $A=XW_1+b_1$, $H=\operatorname{ReLU}(A)$, $z=HW_2+b_2$, $p=\sigma(z)$, rồi so $p$ với ngưỡng $0.5$.
:::

::: solution
Với $(0,1)$: $A=(1,0)$, $H=(1,0)$, $z=0.5$, $p\approx0.622$, $\hat y=1$.
:::

### Sức biểu diễn và giới hạn

XOR cho thấy một tầng afin không đủ. Có thể tăng **độ sâu** bằng cách thêm tầng ẩn hoặc tăng **độ rộng** bằng cách thêm nơ-ron trong mỗi tầng. Ở mức khái quát, kết quả xấp xỉ phổ dụng cho biết một mạng có đủ nơ-ron có thể xấp xỉ một lớp hàm rộng. Kết quả này chỉ nói về khả năng biểu diễn; nó không bảo đảm quá trình huấn luyện sẽ tìm được tham số phù hợp hoặc mô hình sẽ khái quát tốt trên dữ liệu mới. Trong **biểu diễn phân tán**, một đặc trưng được mã hóa bởi sự phối hợp của nhiều nơ-ron thay vì gắn với một nơ-ron riêng. Buổi 02 chuyển sang cách tìm tham số bằng lan truyền ngược và tối ưu.

*Tự kiểm tra:* phân biệt khả năng biểu diễn XOR với khả năng tìm tham số và khái quát trên dữ liệu mới.

## Từ công thức đến triển khai

Lan truyền xuôi của MLP là chuỗi phép afin và kích hoạt: $A=XW_1+b_1$, $H=\operatorname{ReLU}(A)$, $z=HW_2+b_2$, rồi $p=\sigma(z)$ ở tầng ra. Độ chệch được quảng bá theo chiều lô. Với mạng XOR, chuỗi kích thước là $X:4\times2 \to A:4\times2 \to H:4\times2 \to z:4\times1 \to p:4\times1$; với ví dụ nhiều lớp là $X:32\times10 \to A:32\times20 \to H:32\times20 \to Z:32\times3$. Buổi này dừng ở lan truyền xuôi và suy luận.

## Tự kiểm tra

- Kiểm tra kích thước tensor: $X:4\times2$, $H:4\times2$, $z:4\times1$; với ví dụ cuối $H:32\times20$, $Z:32\times3$.
- Kiểm tra số tham số: mạng XOR có $9$ tham số; ví dụ cuối có $283$ tham số.
- Phân biệt dữ liệu, nhãn, tham số, huấn luyện và suy luận; phân biệt logit với xác suất; phân biệt biến đổi tuyến tính với afin.
- Giải thích vì sao mạng ReLU tạo ánh xạ tuyến tính từng đoạn.
- Phân biệt biểu diễn được với dễ huấn luyện và khái quát tốt.

## Tài liệu tham khảo

- `lec01_intro.pdf`, trang chiếu 3–15 (vấn đề, bối cảnh và học từ dữ liệu).
- `lec02_linear_part1.pdf`, trang chiếu 15–21 (biến đổi afin, biên quyết định và XOR).
- `lec05_multilayer.pdf`, trang chiếu 2–35 (MLP, hợp thành, hàm kích hoạt, XOR, cấu trúc và sức biểu diễn).
- GT PDF, trang 29–35, 41–42, 55–56, 66–73, 83–90.
- DOCX Buổi 1 và hoạt động XOR.

### Đọc trước

Theo DOCX đề cương, tài liệu đọc trước gồm Goodfellow Chương 6 và D2L Chương 5 về mạng nơ-ron sâu.
