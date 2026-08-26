# Ghi chú cho người soạn — Bài 11

## Tuyến giảng và điều hướng

- Dùng mũi tên xuống trong sáu stack lõi. Dùng mũi tên phải tại L11-03, 14, 24, 29, 35 và 40.
- Phụ lục là một stack dọc duy nhất X01 → X02 → X03 → X04.
- Giữ trace $B=1,T=3,D=4,d_k=d_v=2$ từ L11-04 đến L11-29. Trace này cô lập cơ chế chú ý trên $X$.
- Tại L11-31, chuyển sang đầu vào đầy đủ $H_0=X+PE$. Không tính lại toàn bộ phép chú ý; chỉ giữ kích thước $1\times3\times4$.
- Tại L11-09–10, giữ $S,B_M,A$ ở dạng $B\times T_q\times T_k$. Trục đầu $h$ chỉ xuất hiện từ L11-25; khi đó mở mặt nạ thành $B\times1\times T_q\times T_k$.
- L11-22 giữ cảnh báo hàng toàn chặn. L11-23 chỉ dạy hai hợp đồng có nguồn: chặn khóa đệm trước softmax và loại ký hiệu đệm khỏi sai số.
- L11-36–37 dành đủ thời gian truy vết $H^{src}_{\ell-1}\to H^{src}_\ell$ và $G_{\ell-1}\to G_\ell$, từng nhánh Bỏ ngẫu nhiên và mỗi đường dư tới Cộng+LN. Chốt $H^{enc}=H^{src}_{L_{enc}}$ và $H^{dec}=G_{L_{dec}}$.
- Số tầng và số đầu là siêu tham số. Không chuyển cấu hình số trên slide nguồn thành cấu hình bắt buộc.

## Tuyến cắt

- Cắt toàn bộ X01–X04 vẫn giữ đúng 100 phút lõi.
- Nếu chỉ có 110 phút, ưu tiên X02 về chi phí và X04 về quan hệ vị trí tương đối.
- Không cắt L11-10, L11-22–23, L11-31, L11-34–38 hoặc L11-40.

## Đáp án kiểm tra trên lớp

- L11-02: bộ mã hóa không nhân quả cho một truy vấn đọc mọi khóa nguồn hợp lệ; khóa đệm bị chặn.
- L11-14: điểm $1\times3\times3$; softmax theo trục khóa cuối; $AV$ trả $1\times3\times2$.
- L11-18: truy vấn 3 được đọc cả ba khóa nên hàng không đổi; truy vấn 1 chỉ có khóa 1 nên trọng số là $[1,0,0]$.
- L11-24: $A$ có kích thước $B\times H_a\times3\times5$; mặt nạ nguồn có thể là $B\times1\times1\times5$ hoặc mở rộng thành $B\times1\times3\times5$, rồi phát qua đầu.
- L11-29: không tính độ lệch có $64$ tham số; độ lệch Q/K/V tổng $12$ và độ lệch ra $4$, nên tổng là $80$.
- L11-31: $PE$ có kích thước $3\times4$ và được phát qua trục lô; $H_0[0,0,:]=X[0,0,:]+PE[0,:]$. Kết quả giữ shape $1\times3\times4$.
- L11-40:
  1. $QK^\top:B\times H_a\times T_q\times T_k$; $A$ cùng kích thước; $AV:B\times H_a\times T_q\times d_v$.
  2. $PE$ cung cấp vị trí và được cộng theo phần tử, nên đầu vào vẫn là $B\times T\times D$.
  3. Softmax chạy theo khóa $T_k$; LayerNorm chạy theo chiều đặc trưng $D$.
  4. Mặt nạ khóa chặn vị trí không được đọc; mặt nạ sai số loại đệm khỏi tổng và mẫu số; dịch nhãn tạo cặp đầu vào–đích kế tiếp.
- X01: đầu ra hoán vị theo cùng phép hoán vị; mã hóa vị trí hoặc mặt nạ phụ thuộc vị trí phá đối xứng.
- X02: $(512/128)^2=16$ lần cho hạng bậc hai.
- X03: $d_k,d_v$ giảm một nửa; tổng tham số chiếu vẫn $4D^2$ nếu giữ tổng chiều bằng $D$.
- X04: ma trận quay chỉ phụ thuộc $k\omega_i$, không phụ thuộc vị trí tuyệt đối $p$.

## Bài tập 50 phút

### BT11-01 — Tính một phép tự chú ý, 20 phút

**Dữ kiện**

Xét một mẫu với $B=1,T=2,D=d_k=d_v=2$:

$$
X=\begin{bmatrix}1&0\\0&1\end{bmatrix},\qquad
W_Q=W_K=W_V=I_2,\qquad B_M=0.
$$

**Yêu cầu**

1. Tính $Q,K,V$ và ghi kích thước khi khôi phục trục lô.
2. Tính $S=QK^\top/\sqrt2$.
3. Tính softmax theo khóa để được $A$, làm tròn ba chữ số thập phân.
4. Tính $O=AV$ và giải thích vì sao $O=A$ trong dữ kiện này.

**Sản phẩm nộp**

- Một bảng gồm $Q,K,V,S,A,O$ và kích thước từng tensor.
- Một câu xác nhận trục softmax.

**Đáp án**

$$Q=K=V=X,$$

$$
S=\begin{bmatrix}1/\sqrt2&0\\0&1/\sqrt2\end{bmatrix}
\approx\begin{bmatrix}.707&0\\0&.707\end{bmatrix}.
$$

Vì $\exp(.707)\approx2.028$:

$$
A\approx\begin{bmatrix}.670&.330\\.330&.670\end{bmatrix},\qquad O=AV=A.
$$

Khi khôi phục trục lô: $Q,K,V,O$ có kích thước $1\times2\times2$; $S,A$ có kích thước $1\times2\times2$.

**Rubric, 10 điểm**

- Q/K/V và kích thước đúng: 2 điểm.
- $S$ và hệ số $\sqrt2$ đúng: 2 điểm.
- Softmax đúng trục và số đúng: 3 điểm.
- $O$ đúng: 2 điểm.
- Giải thích $O=A$ vì $V=I_2$: 1 điểm.

### BT11-02 — Mặt nạ nhân quả và khóa đệm, 10 phút

**Dữ kiện**

Một lô có $B=2$, độ dài đệm chung $T=3$. Mẫu 1 có ba ký hiệu hợp lệ; mẫu 2 có hai ký hiệu hợp lệ và vị trí 3 là đệm. Cả hai dùng tự chú ý nhân quả.

**Yêu cầu**

1. Viết ma trận giữ/chặn $3\times3$ cho từng mẫu; dùng 1 cho khóa được phép đọc và 0 cho khóa bị chặn.
2. Chuyển sang mặt nạ cộng $0/-\infty$ có kích thước $B\times1\times3\times3$.
3. Ghi vị trí nào bị loại khỏi hàm mất mát của mẫu 2.

**Sản phẩm nộp**

- Hai ma trận giữ/chặn và một câu mô tả mặt nạ sai số.

**Đáp án**

Mẫu 1:

$$
M^{(1)}=\begin{bmatrix}1&0&0\\1&1&0\\1&1&1\end{bmatrix}.
$$

Mẫu 2, khóa thứ ba luôn bị chặn:

$$
M^{(2)}=\begin{bmatrix}1&0&0\\1&1&0\\1&1&0\end{bmatrix}.
$$

Đổi phần tử 1 thành 0 và phần tử 0 thành $-\infty$ để được mặt nạ cộng. Ký hiệu thứ ba của mẫu 2 có mặt nạ sai số bằng 0. Không yêu cầu một quy tắc triệt truy vấn đệm ở từng tầng.

**Rubric, 10 điểm**

- Mặt nạ nhân quả mẫu 1 đúng: 3 điểm.
- Kết hợp khóa đệm ở mẫu 2 đúng: 3 điểm.
- Kích thước bốn chiều và quy tắc phát qua đầu đúng: 2 điểm.
- Mặt nạ sai số đúng: 2 điểm.

### BT11-03 — Truy vết hai đầu, 10 phút

**Dữ kiện**

$B=2,T=5,D=8,H_a=2,d_k=d_v=4$. Mỗi đầu có ma trận chiếu riêng; tổng chiều sau khi ghép là 8. Phép chiếu ra dùng $W_O\in\mathbb R^{8\times8}$.

**Yêu cầu**

Ghi kích thước của Q/K/V theo đầu, ma trận điểm, trọng số, đầu ra từng đầu, tensor sau ghép và đầu ra sau $W_O$. Tính số tham số chiếu khi không dùng độ lệch.

**Sản phẩm nộp**

- Một chuỗi shape hoàn chỉnh từ đầu vào tới đầu ra.
- Một phép đếm tham số.

**Đáp án**

- Q/K/V theo đầu: $2\times2\times5\times4$.
- Điểm và trọng số: $2\times2\times5\times5$.
- Đầu ra theo đầu: $2\times2\times5\times4$.
- Sau ghép: $2\times5\times8$.
- Sau $W_O$: $2\times5\times8$.
- Tham số: $3D^2+D^2=4D^2=256$.

**Rubric, 10 điểm**

- Q/K/V và trục đầu đúng: 3 điểm.
- Điểm/trọng số đúng: 2 điểm.
- Đầu ra, ghép và chiếu ra đúng: 3 điểm.
- Số tham số đúng: 2 điểm.

## BT11-04 — Kiểm chứng phép chú ý thủ công bằng SDPA, 10 phút

**Chuẩn bị trước lớp**

- Máy phòng thực hành phải có PyTorch 2.13 chạy được trên CPU.
- Giảng viên chạy thử lệnh `python3 -c "import torch; assert torch.__version__.startswith('2.13.'); print(torch.__version__, torch.rand(1).device)"` trước giờ học; đầu ra phải cho biết phiên bản 2.13 và thiết bị `cpu`.
- Không tính thời gian cài PyTorch vào 10 phút lab. Nếu preflight không đạt, dùng bản ghi đầu ra dự phòng và yêu cầu sinh viên đối chiếu tĩnh.

**Câu nối sản phẩm**

BT11-01 tạo phép tính Q/K/V, softmax và đầu ra chú ý. BT11-02 tạo mặt nạ nhân quả. BT11-03 khóa các kích thước có trục đầu. BT11-04 chuyển ba sản phẩm đó thành dự đoán trước khi chạy hai API.

**Nhịp thực hiện**

- Phút 0–1: dự đoán kích thước đầu ra và hai ma trận mặt nạ.
- Phút 1–3: đọc chữ ký API, `batch_first`, quy ước `True` và cảnh báo `dropout_p`.
- Phút 3–7: chạy phép tính thủ công và SDPA trên cùng Q/K/V/mặt nạ; xác nhận bằng `assert_close`.
- Phút 7–10: khảo sát giao diện MHA; đối chiếu kích thước, phép phủ định mặt nạ và chế độ đánh giá.

**Mục tiêu**

Tính chú ý bằng các phép tensor cơ bản, kiểm chứng kết quả bằng SDPA trên cùng dữ kiện, rồi khảo sát giao diện MHA. Bài này dùng PyTorch 2.13 trên CPU; không yêu cầu GPU.

**Đề bài**

1. Chỉ ra năm bước của phép tính thủ công: điểm, scale, chặn, softmax và nhân với V.
2. Chạy mã; xác nhận `torch.testing.assert_close` không báo lỗi và ghi các kích thước cùng hai mặt nạ.
3. Giải thích vì sao `block_mask = ~keep_mask`, vì sao không so sánh `y_sdpa` với `y_mha`, và các chỗ khóa chế độ đánh giá.

**Nếu còn thời gian**

Đổi `batch_first=True` thành `False` nhưng giữ nguyên `x` có kích thước $B\times T\times D$. Dự đoán lỗi diễn giải trục trước khi chạy; không cần sửa mã.

```python
import torch
import math
import torch.nn.functional as F
from torch import nn

torch.manual_seed(7)
device = torch.device("cpu")
B, H_a, T, d_h = 1, 2, 3, 2
D = H_a * d_h

# SDPA: Q, K, V có thứ tự trục (lô, đầu, truy vấn/khóa, đặc trưng).
q = torch.randn(B, H_a, T, d_h, device=device)
k = torch.randn(B, H_a, T, d_h, device=device)
v = torch.randn(B, H_a, T, d_h, device=device)
keep_mask = torch.ones(T, T, dtype=torch.bool, device=device).tril()

with torch.inference_mode():
    scores = q @ k.transpose(-2, -1)
    scores = scores / math.sqrt(d_h)
    masked_scores = scores.masked_fill(~keep_mask, float("-inf"))
    weights_manual = torch.softmax(masked_scores, dim=-1)
    y_manual = weights_manual @ v

    y_sdpa = F.scaled_dot_product_attention(
        q, k, v, attn_mask=keep_mask, dropout_p=0.0
    )
    torch.testing.assert_close(y_manual, y_sdpa, rtol=1e-5, atol=1e-6)

# MHA: batch_first=True nên X có thứ tự trục (lô, chuỗi, đặc trưng).
x = torch.randn(B, T, D, device=device)
mha = nn.MultiheadAttention(
    embed_dim=D, num_heads=H_a, dropout=0.1, batch_first=True
).to(device)
mha.eval()
block_mask = ~keep_mask

with torch.inference_mode():
    y_mha, weights_mha = mha(
        x, x, x,
        attn_mask=block_mask,
        need_weights=True,
        average_attn_weights=False,
    )

assert y_manual.shape == (B, H_a, T, d_h)
assert y_sdpa.shape == (B, H_a, T, d_h)
assert y_mha.shape == (B, T, D)
assert weights_mha.shape == (B, H_a, T, T)

print("Thủ công:", tuple(y_manual.shape))
print("SDPA:", tuple(y_sdpa.shape))
print("MHA:", tuple(y_mha.shape))
print("Trọng số MHA:", tuple(weights_mha.shape))
print("Thủ công và SDPA: khớp")
print("Mặt nạ giữ của SDPA:\n", keep_mask.int())
print("Mặt nạ chặn của MHA:\n", block_mask.int())
```

**Sản phẩm nộp**

- Một bản ghi gồm bốn kích thước, hai ma trận mặt nạ và xác nhận phép tính thủ công khớp SDPA.
- Ba câu giải thích phép tính thủ công, `block_mask = ~keep_mask`, và lý do không so sánh đầu ra SDPA với đầu ra MHA.
- Một câu chỉ ra `dropout_p=0.0`, `mha.eval()` và `torch.inference_mode()` trong lần chạy đánh giá.
- Nếu làm phần tùy chọn, thêm một câu về cách `batch_first` đổi nghĩa hai trục đầu.

**Đầu ra dự kiến**

```text
Thủ công: (1, 2, 3, 2)
SDPA: (1, 2, 3, 2)
MHA: (1, 3, 4)
Trọng số MHA: (1, 2, 3, 3)
Thủ công và SDPA: khớp
Mặt nạ giữ của SDPA:
 tensor([[1, 0, 0],
        [1, 1, 0],
        [1, 1, 1]], dtype=torch.int32)
Mặt nạ chặn của MHA:
 tensor([[0, 1, 1],
        [0, 0, 1],
        [0, 0, 0]], dtype=torch.int32)
```

**Đáp án**

- Nhánh thủ công thực hiện $QK^\top$, chia $\sqrt{d_h}$, `masked_fill`, softmax theo trục khóa và nhân với V. SDPA nhận cùng Q/K/V/mặt nạ và trả tensor cùng kích thước $1\times2\times3\times2$; `assert_close` kiểm hai kết quả.
- MHA nhận $X$ có kích thước $1\times3\times4$ vì `batch_first=True`; đầu ra giữ kích thước này. Khi không lấy trung bình theo đầu, trọng số có kích thước $1\times2\times3\times3$.
- Trong `scaled_dot_product_attention`, `True` cho phép vị trí tham gia chú ý. Trong `MultiheadAttention`, `True` ở mặt nạ Boolean chặn vị trí. Vì vậy MHA phải nhận `~keep_mask`.
- Không so sánh `y_sdpa` với `y_mha`: MHA nhận tensor $X$ khác Q/K/V thủ công và còn có các phép chiếu tham số được khởi tạo ngẫu nhiên.
- SDPA luôn dùng xác suất truyền qua `dropout_p`, kể cả khi mô-đun gọi đang ở chế độ đánh giá. Lần chạy này đặt `dropout_p=0.0`. MHA được cấu hình `dropout=0.1` nhưng `mha.eval()` tắt dropout; `torch.inference_mode()` tắt ghi đồ thị gradient cho cả hai lần gọi.
- Nếu đặt `batch_first=False` mà không chuyển vị `x`, MHA diễn giải hai trục đầu là $(T,B)$ thay vì $(B,T)$. Với $x$ hiện tại, nó đọc độ dài chuỗi là 1 và cỡ lô là 3; mặt nạ $3\times3$ không còn khớp độ dài truy vấn 1.

**Rubric, 10 điểm**

- Viết đúng năm bước thủ công và `assert_close` đạt: 4 điểm.
- Ghi đúng bốn kích thước: 2 điểm.
- Ghi đúng hai mặt nạ và giải thích phép phủ định: 2 điểm.
- Giải thích đúng dropout, `inference_mode` và lý do không so sánh SDPA với MHA: 2 điểm.
- Điểm thưởng: giải thích đúng tác động của `batch_first=False`: 1 điểm, không dùng để bù lỗi ở phần bắt buộc.

**Nguồn và giới hạn**

- PyTorch 2.13, `torch.nn.functional.scaled_dot_product_attention`: chữ ký API, kích thước, quy ước mặt nạ Boolean và cảnh báo về `dropout_p`.
- PyTorch 2.13, `torch.nn.MultiheadAttention`: `batch_first`, kích thước đầu ra, trọng số theo đầu và quy ước mặt nạ Boolean.
- Không mở rộng sang lựa chọn kernel, benchmark, GQA hoặc hiệu năng phần cứng.

## Bài tập về nhà theo DOCX

**Đề bài**

Cho một câu nguồn đã được tách thành $T_s$ ký hiệu và nhúng thành $X^{src}\in\mathbb R^{B\times T_s\times D}$. Hãy giải thích bằng 180–250 từ cách bộ mã hóa Transformer biến câu này thành $H^{enc}$ để bộ giải mã dùng làm khóa và giá trị. Bài viết phải nêu:

1. cách tạo $H_0^{src}$ từ nhúng và mã hóa vị trí;
2. nguồn Q/K/V trong tự chú ý bộ mã hóa;
3. vị trí của hai lần Cộng+LN và FFN trong một tầng, rồi cách lặp đến $H^{enc}=H^{src}_{L_{enc}}$;
4. shape được giữ qua tầng và vai trò của mặt nạ khóa đệm;
5. ý nghĩa của $H^{enc}$ đối với chú ý chéo.

**Rubric, 10 điểm**

- Luồng $X^{src}\to H_0^{src}\to H^{src}_1\to\cdots\to H^{enc}$ đúng và đủ: 3 điểm.
- Q/K/V, mặt nạ và trục được mô tả đúng: 2 điểm.
- Hai nhánh Cộng+LN và FFN đúng thứ tự: 2 điểm.
- Shape $B\times T_s\times D$ nhất quán: 2 điểm.
- Diễn đạt rõ, đúng giới hạn từ: 1 điểm.

## Điểm cần kiểm định cuối

- Chromium in Reveal ở 1280×720 đã cho đúng 45 trang; toàn bộ contact sheet không có tràn, chồng lấn hoặc cắt nội dung. L11-31, L11-36, L11-37 và L11-38 cũng đọc được, không bị cắt ở khung 900×720.
- Codex Slides project shell `20260826234600-b-i-11-ki-n-tr-c-transformer-8nca` đã được tạo, nhưng tải Design File thất bại với HTTP 500 và `ReferenceError: File is not defined` tại files route. Chưa có kiểm định hiển thị Codex Browser; đây là giới hạn runtime/plugin Node, không phải bằng chứng lỗi deck.
- Khối mã BT11-04 mới đã chạy đạt bằng PyTorch 2.13.0+cpu trên CPU: phép tính thủ công khớp SDPA qua `torch.testing.assert_close`; bốn kích thước và hai ma trận mặt nạ khớp đầu ra dự kiến. Cảnh báo thiếu NumPy trong môi trường kiểm thử tối giản không ảnh hưởng đoạn mã hoặc kết quả.
- Trước mỗi buổi học, vẫn chạy preflight trên máy phòng thực hành. Nếu dùng phiên bản khác, chỉ xác nhận hợp đồng kích thước và mặt nạ, không suy rộng về triển khai nội bộ.
