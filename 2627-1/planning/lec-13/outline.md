# Bài 13 — Học tăng cường và học bắt chước

## Mục tiêu, đối tượng và thời lượng

- LLO26: trình bày tác tử, môi trường, trạng thái, hành động, phần thưởng và chính sách.
- LLO27: phân biệt học tăng cường với học bắt chước; truy vết giá trị hành động, Q-learning và mạng Q sâu (Deep Q-Network, DQN).
- Đối tượng đã học xác suất có điều kiện, kỳ vọng, đạo hàm, entropy chéo, hồi quy và tensor theo lô; không giả định đã học RL.
- Tuyến lõi L13-00–41: 100 phút. Phụ lục X01–X04: 20 phút. Bài tập: 50 phút riêng.

## Mạch và dấu vết dữ liệu

Một hành lang được truyền xuyên suốt:

`quỹ đạo chuyên gia → cặp (s,a) → phân phối BC → trạng thái lệch → vòng tương tác → chuyển tiếp (S,A,R,S') → lợi tức → V/Q → đích Bellman → cập nhật bảng Q → một hàng trong lô DQN → q=.4, Y=.9, hạng tử bình phương=.25`.

Quy ước duy nhất: hành động $A_t$ sinh $R_{t+1}$ và $S_{t+1}$. Quỹ đạo T bước kết thúc ở $S_T$ và không có $A_T$.

## Nguồn

| Nguồn | Dải | Vai trò |
|---|---|---|
| CS285 L02 Behavioral Cloning | PDF 8–39 | Trình diễn, BC, phân phối hành động, lệch phân phối, DAgger |
| CS285 L07 Value-based RL | PDF 5–20 | Giá trị, học ngoài chính sách, thăm dò, bộ nhớ phát lại |
| CS285 L08 Q-learning Practice | PDF 2–22 | DQN, ngắt gradient, mạng đích và ổn định |
| Illinois L12 Imitation Learning | PDF 1–14 | Lệch phân phối tuần tự và DAgger |
| Illinois L10 Deep RL | PDF 1–8 | Cầu nối Q-learning với mạng Q |
| `hocsau_draft.pdf` | PDF 335–344 | MDP, lợi tức, V/Q, Bellman, Q-learning và thăm dò |
| `lec01_intro.pdf` | PDF 45–46 | Liên hệ ngắn, không dùng benchmark |

Không dùng GT PDF 345–351, trang ngoài dải, nguồn web, benchmark, policy gradient, actor–critic, RLHF hoặc code demo.

## Ký hiệu và hợp đồng tensor

| Ký hiệu | Nghĩa |
|---|---|
| $M$ | số cặp trong toàn bộ tập BC |
| $B$ | kích thước một lô BC hoặc DQN |
| $S_t,A_t,R_{t+1}$ | trạng thái, hành động, phần thưởng sinh sau hành động |
| $\pi,\mu$ | chính sách đang xét/đích và chính sách hành vi |
| $G_t$ | lợi tức từ thời điểm t |
| $V^\pi,Q^\pi,Q^*$ | giá trị trạng thái, giá trị hành động và giá trị tối ưu |
| $D^{term},D^{trunc}$ | cờ kết thúc thật và cờ cắt ngoài MDP |
| $\theta,\bar\theta$ | tham số mạng hiện tại và mạng đích |

Lô DQN: $S,S'\in\mathbb R^{B\times D_s}$; $A\in\{0,\ldots,D_a-1\}^{B}$; $R\in\mathbb R^B$; $D^{term},D^{trunc}\in\{0,1\}^{B}$; $Q_{all}\in\mathbb R^{B\times D_a}$; $q_{sa},Y\in\mathbb R^B$; mất mát vô hướng.

## Tuyến nội dung

1. BC và lệch phân phối: L13-00–12.
2. Quyết định BC/RL, tương tác, chuyển tiếp, kiểm tra sáu thành phần và MDP: L13-13–20.
3. Lợi tức, giá trị, Monte Carlo, sai phân thời gian và Bellman: L13-19–27.
4. Q-learning ngoài chính sách và thăm dò: L13-28–31.
5. DQN từ pipeline đến hàng số, công thức, giả mã và kiểm tra: L13-32–41.
6. Phụ lục cuối 20 phút: X01 hành động liên tục; X02 cắt thời gian; X03 độ phủ; X04 tự rà lô DQN.

## Bài tập 50 phút

1. Xác định dữ liệu, chính sách và phân phối hành động trong BC — 10 phút.
2. Phân tích lệch phân phối trên quỹ đạo hành lang — 10 phút.
3. Nhận diện sáu thành phần theo LLO26 — 10 phút.
4. Tính lợi tức, đích Bellman và một cập nhật Q — 15 phút.
5. Chỉ ra bộ nhớ phát lại, phép lấy theo hành động, ngắt gradient và mạng đích — 5 phút.
