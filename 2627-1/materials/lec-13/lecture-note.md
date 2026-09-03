# Buổi 13: Học tăng cường và học bắt chước

## Mục tiêu và kiến thức tiên quyết

Sau buổi này, người học có thể:

- trình bày tác tử, môi trường, trạng thái, hành động và phần thưởng;
- phân biệt học bắt chước với học tăng cường qua nguồn tín hiệu và cách thu thập dữ liệu;
- tính lợi tức, giá trị trạng thái, giá trị hành động và một đích Bellman;
- thực hiện một cập nhật Q-learning và truy vết lô dữ liệu của mạng Q sâu (Deep Q-Network, DQN).

Kiến thức tiên quyết: xác suất có điều kiện, kỳ vọng, đạo hàm, entropy chéo, hồi quy và tensor theo lô. Bài không giả định người học đã học học tăng cường.

## Ký hiệu và quy ước thời gian

| Ký hiệu | Nghĩa |
|---|---|
| $M,B$ | Số cặp trong toàn bộ tập trình diễn và kích thước một lô |
| $S_t,A_t,R_{t+1}$ | Trạng thái, hành động và phần thưởng sinh sau hành động |
| $\pi_E,\pi_\theta,\mu$ | Chính sách chuyên gia, chính sách đang học và chính sách hành vi |
| $G_t$ | Lợi tức từ thời điểm $t$ |
| $V^\pi,Q^\pi,Q^*$ | Giá trị trạng thái, giá trị hành động và giá trị tối ưu |
| $D^{term}$ | Cờ kết thúc thật của quá trình quyết định |
| $\theta,\bar\theta$ | Tham số mạng hiện tại và mạng đích |

Quy ước xuyên suốt: ở thời điểm $t$, hành động $A_t$ sinh phần thưởng $R_{t+1}$ và trạng thái $S_{t+1}$. Quỹ đạo có $T$ bước kết thúc ở $S_T$ và không có $A_T$.

## Cụm 1: Học bắt chước từ dữ liệu trình diễn

Xét một robot đi trong hành lang ba trạng thái $s_0,s_1,s_2$. Chuyên gia tạo quỹ đạo

$$
\tau^E=(S_0,A_0^E,R_1,S_1,\ldots,A_{T-1}^E,R_T,S_T).
$$

![Hành lang được dùng xuyên suốt từ học bắt chước đến DQN](img/lec-13/corridor.svg)

Quỹ đạo đầy đủ có cả phần thưởng, nhưng hàm mất mát BC chỉ dùng các cặp trạng thái–hành động có nhãn:

$$
\mathcal D_E=\{(s_i,a_i^E)\}_{i=1}^{M}.
$$

Với hành động rời rạc, mạng xuất điểm cho $D_a$ hành động và softmax tạo $\pi_\theta(a\mid s)$. Hàm mất mát là âm log-hợp lý của hành động chuyên gia:

$$
\mathcal L_{BC}(\theta)
=-\frac1M\sum_{i=1}^{M}\log\pi_\theta(a_i^E\mid s_i).
$$

$M$ là kích thước toàn bộ tập. Trong một bước huấn luyện, lô $B$ chỉ chứa một phần của $M$ cặp. Với hành động liên tục, chính sách có thể xuất tham số của một phân phối và tối đa hóa log-hợp lý của hành động chuyên gia.

Hàm mất mát nhỏ trên $\mathcal D_E$ chỉ đo khả năng khớp hành động trên trạng thái chuyên gia. Đánh giá vận hành phải cho chính sách tự tạo quỹ đạo rồi đo đại lượng của cả quỹ đạo.

::: exercise Câu hỏi kiểm tra
Tại $s_1$, chuyên gia chọn “phải”. Chính sách dự đoán xác suất $(0{,}05;0{,}95)$ cho (trái, phải). Thành phần nào phải tăng để hàm mất mát BC giảm?
:::

::: solution
Xác suất của hành động “phải” phải tăng. Hàm mất mát của mẫu là $-\log\pi_\theta(\text{phải}\mid s_1)$.
:::

## Cụm 2: Lệch phân phối và DAgger

BC học trên phân phối trạng thái $d_{\pi_E}$ do chuyên gia tạo. Khi tự vận hành, chính sách $\pi_\theta$ tạo phân phối $d_{\pi_\theta}$. Một hành động sai có thể đưa robot đến trạng thái không có trong dữ liệu trình diễn; lỗi tiếp theo lại được dự đoán trên vùng chưa thấy.

![Một lỗi đưa chính sách sang nhánh trạng thái không có trong dữ liệu chuyên gia](img/lec-13/bc-shift.svg)

Do đó,

$$
d_{\pi_E}\ne d_{\pi_\theta}.
$$

Đây là lý do hàm mất mát trên tập kiểm định gồm các cặp trạng thái–hành động của chuyên gia có thể giảm trong khi chất lượng quỹ đạo vẫn thấp. Nhận xét này mô tả cơ chế, không khẳng định một tốc độ tăng lỗi phổ quát.

DAgger (Dataset Aggregation) thu thập trạng thái mà $\pi_\theta$ thực sự ghé, yêu cầu chuyên gia gán hành động cho các trạng thái đó, gộp cặp mới vào tập dữ liệu rồi huấn luyện lại. Cách làm này đưa nhãn đến gần phân phối vận hành hơn, nhưng phải trả chi phí truy vấn chuyên gia.

::: exercise Câu hỏi kiểm tra
Vì sao hàm mất mát BC trên tập kiểm định từ $d_{\pi_E}$ có thể thấp nhưng robot vẫn thất bại khi tự chạy?
:::

::: solution
Tập kiểm định không bao phủ các trạng thái do lỗi của $\pi_\theta$ tạo ra. Chính sách phải dự đoán ngoài phân phối dữ liệu chuyên gia, và các sai lệch có thể nối tiếp nhau dọc quỹ đạo.
:::

## Cụm 3: Từ hành động chuyên gia đến phần thưởng

BC và học tăng cường đều có thể học một chính sách, nhưng nguồn tín hiệu khác nhau.

| Thuộc tính | BC | Học tăng cường |
|---|---|---|
| Tín hiệu | Hành động chuyên gia | Phần thưởng từ môi trường |
| Dữ liệu | Cặp $(s,a^E)$ trong tập trình diễn | Chuyển tiếp $(S_t,A_t,R_{t+1},S_{t+1})$ |
| Tương tác | Không bắt buộc trong BC thuần | Chính sách tạo dữ liệu qua tương tác |
| Mục tiêu | Khớp phân phối hành động chuyên gia | Tối đa hóa lợi tức kỳ vọng |

BC phù hợp khi có trình diễn đáng tin và tương tác thử–sai khó hoặc nguy hiểm. DAgger cần thêm khả năng truy vấn chuyên gia tại trạng thái mới. Học tăng cường dùng được khi có phần thưởng và một môi trường đủ an toàn hoặc mô phỏng được để thu dữ liệu.

![Vòng tương tác giữa tác tử và môi trường](img/lec-13/mdp-loop.svg)

Một quá trình quyết định Markov (Markov decision process, MDP) được mô tả bằng

$$
\mathcal M=(\mathcal S,\mathcal A,P,r,\gamma,\rho_0).
$$

$P(s'\mid s,a)$ là xác suất chuyển trạng thái, $r(s,a,s')$ là phần thưởng theo chuyển tiếp, $\gamma\in[0,1]$ là hệ số chiết khấu và $\rho_0$ là phân phối trạng thái đầu. Chính sách $\pi(a\mid s)$ thuộc tác tử và không nằm trong bộ thành phần mô tả môi trường.

Tính Markov yêu cầu trạng thái hiện tại chứa đủ thông tin để dự đoán chuyển tiếp:

$$
p(S_{t+1}\mid S_t,A_t)
=p(S_{t+1}\mid S_{0:t},A_{0:t}).
$$

Nếu vị trí của xe không đủ để dự đoán chuyển động, vận tốc có thể phải được thêm vào trạng thái.

Lợi tức là tổng phần thưởng chiết khấu:

$$
G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}.
$$

Trong một lượt hữu hạn, phần thưởng sau kết thúc được quy ước bằng 0. Với dãy phần thưởng $(0,0,1)$ và $\gamma=0{,}9$,

$$
(G_0,G_1,G_2)=(0{,}81;0{,}9;1).
$$

Cờ $D^{term}_{t+1}=1$ đánh dấu kết thúc thật của MDP. Cờ này sẽ triệt phần giá trị tương lai trong đích một bước.

## Cụm 4: Giá trị và phương trình Bellman

Giá trị trạng thái và giá trị hành động dưới chính sách $\pi$ là

$$
V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],
$$

$$
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a].
$$

Sau khi cố định hành động đầu tiên, $Q^\pi$ vẫn lấy kỳ vọng trên chuyển tiếp và các hành động sau theo $\pi$. Vì vậy,

$$
V^\pi(s)=\mathbb E_{a\sim\pi(\cdot\mid s)}[Q^\pi(s,a)].
$$

Nếu hai hành động có $Q^\pi(s,a_1)=0{,}2$ và $Q^\pi(s,a_2)=0{,}8$, còn $\pi$ chọn đều, thì $V^\pi(s)=0{,}5$. Phép cực đại cho $0{,}8$; kỳ vọng và cực đại trả lời hai câu hỏi khác nhau.

Monte Carlo dùng lợi tức đầy đủ sau khi lượt kết thúc. Sai phân thời gian (temporal difference, TD) dùng phần thưởng quan sát và một ước lượng ở bước kế tiếp. Quan hệ Bellman của chính sách là

$$
Q^\pi(s,a)
=\mathbb E\left[R_{t+1}
+\gamma\,\mathbb E_{a'\sim\pi(\cdot\mid S_{t+1})}
Q^\pi(S_{t+1},a')\mid S_t=s,A_t=a\right].
$$

Với tập hành động hữu hạn, Bellman tối ưu thay kỳ vọng theo hành động bằng cực đại:

$$
Q^*(s,a)
=\mathbb E\left[R_{t+1}
+\gamma\max_{a'\in\mathcal A}Q^*(S_{t+1},a')
\mid S_t=s,A_t=a\right].
$$

![Đích Bellman nối phần thưởng hiện tại với giá trị tốt nhất ở trạng thái kế](img/lec-13/bellman-backup.svg)

::: exercise Câu hỏi kiểm tra
Với chuyển tiếp $(s_1,\text{phải},0,s_2)$, $\gamma=0{,}9$, chuyển tiếp chưa kết thúc và $\max_{a'}Q(s_2,a')=1$, đích một bước bằng bao nhiêu?
:::

::: solution
$Y=0+0{,}9\cdot1=0{,}9$.
:::

## Cụm 5: Q-learning ngoài chính sách

Khi không biết $P$, Q-learning dùng một chuyển tiếp quan sát để tạo đích:

$$
Y_t=R_{t+1}
+\gamma(1-D^{term}_{t+1})
\max_{a'}Q(S_{t+1},a').
$$

Cập nhật bảng Q là

$$
Q(S_t,A_t)\leftarrow
Q(S_t,A_t)+\alpha\bigl(Y_t-Q(S_t,A_t)\bigr).
$$

Chính sách hành vi $\mu$ tạo dữ liệu, còn phép cực đại trong đích mô tả chính sách đích. Vì hai chính sách có thể khác nhau, đây là học ngoài chính sách. Tuy vậy, dữ liệu vẫn phải có độ phủ đủ trên các cặp trạng thái–hành động cần ước lượng.

Chính sách epsilon-tham lam chọn một hành động cực đại với xác suất $1-\varepsilon$ và chọn đều từ $\mathcal A$ với xác suất $\varepsilon$. Thăm dò tạo cơ hội quan sát những hành động chưa được đánh giá tốt.

Với $Q(s_1,\text{phải})=0{,}4$, $Y=0{,}9$ và $\alpha=0{,}2$,

$$
Q(s_1,\text{phải})
\leftarrow0{,}4+0{,}2(0{,}9-0{,}4)=0{,}5.
$$

Chỉ một ô của bảng thay đổi trong bước này. Bảng Q không phù hợp khi không gian trạng thái quá lớn hoặc liên tục.

## Cụm 6: Mạng Q sâu

DQN thay bảng bằng mạng $Q_\theta$. Với lô $B$ trạng thái,

$$
S,S'\in\mathbb R^{B\times D_s},\qquad
Q_{all}=Q_\theta(S)\in\mathbb R^{B\times D_a}.
$$

Chỉ số hành động $A\in\{0,\ldots,D_a-1\}^{B}$ chọn một cột trên mỗi hàng để tạo $q_{sa}\in\mathbb R^B$. Bộ nhớ phát lại lưu năm trường

$$
(S,A,R,S',D^{term}).
$$

![Quy trình DQN gồm thu thập, bộ nhớ phát lại, mạng hiện tại và mạng đích](img/lec-13/dqn-pipeline.svg)

Lấy mẫu ngẫu nhiên từ bộ nhớ phát lại làm giảm tương quan thời gian giữa các mẫu trong cùng lô và cho phép dùng lại chuyển tiếp. Điều này không biến dữ liệu thành mẫu độc lập cùng phân phối hoàn hảo.

Mạng hiện tại $Q_\theta$ tạo $q_{sa}$ và nhận gradient. Mạng đích $Q_{\bar\theta}$ tạo

$$
Y=R+\gamma(1-D^{term})
\max_{a'}Q_{\bar\theta}(S',a')
\in\mathbb R^B
$$

trong ngữ cảnh không gradient. Mất mát là

$$
\mathcal L(\theta)=\frac1B\sum_{i=1}^{B}(Y_i-q_{sa,i})^2.
$$

Với một hàng có $q_{sa}=0{,}4$ và $Y=0{,}9$, hạng tử bình phương là $0{,}25$; trong lô $B>1$, đóng góp của hàng này vào trung bình là $0{,}25/B$.

Một vòng DQN có hai pha:

1. Chính sách hành vi tương tác, lưu chuyển tiếp và đặt lại môi trường khi lượt kết thúc.
2. Sau giai đoạn làm ấm, lấy một lô, tính $q_{sa}$ và $Y$, đặt gradient về 0, lan truyền ngược qua $Q_\theta$, cập nhật bộ tối ưu và đồng bộ cứng $\bar\theta\leftarrow\theta$ theo chu kỳ $C$.

Chỉ $\theta$ thuộc bộ tối ưu. Khi đánh giá, tắt các thành phần phụ thuộc chế độ huấn luyện. DQN với xấp xỉ phi tuyến không có bảo đảm hội tụ tổng quát.

::: exercise Câu hỏi kiểm tra
Trong công thức mất mát DQN, gradient đi qua đại lượng nào? Khi $D^{term}=1$, đích còn lại gì?
:::

::: solution
Gradient chỉ đi qua $q_{sa}=Q_\theta(S)[A]$. Nhánh $Q_{\bar\theta}$ tạo đích trong ngữ cảnh không gradient. Khi $D^{term}=1$, đích chỉ còn $Y=R$.
:::

## Tổng hợp

BC dùng hành động chuyên gia làm nhãn. DAgger vẫn dùng nhãn chuyên gia nhưng thu chúng tại trạng thái mà chính sách đang học ghé. Học tăng cường dùng phần thưởng từ tương tác. Q-learning tạo đích Bellman ngoài chính sách; DQN chỉ thay bảng Q bằng một bộ xấp xỉ hàm cùng các cơ chế ổn định hóa.

| Phương pháp | Nguồn tín hiệu | Dữ liệu quyết định cập nhật |
|---|---|---|
| BC | Hành động chuyên gia | Cặp $(s,a^E)$ từ $d_{\pi_E}$ |
| DAgger | Hành động chuyên gia được truy vấn thêm | Cặp được gộp từ trạng thái $\pi_\theta$ ghé |
| Q-learning | Phần thưởng và chuyển tiếp | Đích Bellman từ một mẫu |
| DQN | Như Q-learning | Lô từ bộ nhớ phát lại; Q được xấp xỉ bằng mạng |

## Phần mở rộng

Với hành động liên tục $D_a$ chiều, chính sách Gaussian có thể xuất $\mu(s),\sigma(s)\in\mathbb R^{D_a}$ với $\sigma>0$. Trong lô, hai tensor có kích thước $B\times D_a$. Một Gaussian đơn chỉ có một đỉnh nên không biểu diễn tốt một phân phối hành động nhiều đỉnh.

Học ngoài chính sách không loại bỏ yêu cầu độ phủ. Nếu bộ nhớ phát lại không chứa một hành động tại vùng trạng thái quan trọng, mất mát trên dữ liệu hiện có không cung cấp bằng chứng trực tiếp cho giá trị của hành động bị thiếu.

## Bài tập 50 phút

1. Trong 10 phút, từ hai quỹ đạo chuyên gia, viết $\mathcal D_E$, xác định $M$, lô $B$, nhãn và hàm mất mát BC.
2. Trong 10 phút, vẽ một nhánh lỗi của hành lang và giải thích $d_{\pi_E}\ne d_{\pi_\theta}$.
3. Trong 10 phút, xác định tác tử, môi trường, trạng thái, hành động, phần thưởng và chính sách của hành lang.
4. Trong 15 phút, tính $G_t$, đích Bellman và một cập nhật Q cho một mẫu giữa lượt và một mẫu kết thúc.
5. Trong 5 phút, chỉ ra bộ nhớ phát lại, phép lấy theo hành động, ngắt gradient và mạng đích trong quy trình DQN.

## Nguồn

- Đề cương học phần UET.AI3056, `III.2 → Buổi 13`, LLO26–27.
- Berkeley CS285, *Behavioral Cloning*, PDF 8–39.
- Berkeley CS285, *Value-based Reinforcement Learning*, PDF 5–20.
- Berkeley CS285, *Q-learning Practice*, PDF 2–22.
- Illinois ECE598SG1, *Imitation Learning*, PDF 1–14.
- Illinois ECE598SG1, *Deep Reinforcement Learning*, PDF 1–8.
- `source-materials/textbooks/hocsau_draft.pdf`, PDF 335–344.
