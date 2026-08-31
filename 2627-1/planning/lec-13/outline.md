# Bài 13 — Học tăng cường và học bắt chước

## Mục tiêu, đối tượng và thời lượng

- LLO26 (DOCX, Buổi 13): trình bày tác tử, môi trường, trạng thái, hành động và phần thưởng.
- LLO27 (DOCX, Buổi 13): phân biệt học tăng cường với học bắt chước.
- Giá trị Q, Q-learning và mạng Q sâu (Deep Q-Network, DQN) là nội dung kỹ thuật bắt buộc trong mục Bài giảng của DOCX; không gán chúng vào LLO27.
- Chính sách là nội dung bài giảng: thuộc tác tử, nằm ngoài tuple MDP; xuất hiện ở L13-16 và L13-17.
- Đối tượng đã học xác suất có điều kiện, kỳ vọng, đạo hàm, entropy chéo, hồi quy và tensor theo lô; không giả định đã học RL.
- Tuyến lõi L13-00–41: 100 phút. Phụ lục X01–X04: 20 phút. Bài tập: 50 phút riêng.

## Bảy mạch, counts và thời lượng

| # | Mạch | Trang | Count | Phút |
|---|---|---|---:|---:|
| 1 | BC và dữ liệu trình diễn | L13-00–07 | 8 | 24 |
| 2 | Lệch phân phối và DAgger | L13-08–12 | 5 | 15 |
| 3 | Từ BC sang RL: tương tác và MDP | L13-13–20 | 8 | 19 |
| 4 | Lợi tức, giá trị và Bellman | L13-21–27 | 7 | 14 |
| 5 | Q-learning ngoài chính sách | L13-28–31 | 4 | 8 |
| 6 | DQN từ pipeline đến giả mã | L13-32–40 | 9 | 18 |
| 7 | Tổng kết và phụ lục | L13-41; X01–X04 | 5 | 2 (+20) |

Lõi: $24+15+19+14+8+18+2=100$ phút. Phụ lục: $4\times5=20$ phút. Bài tập riêng: $10+10+10+15+5=50$ phút.

## Thứ tự DOM thực tế

Bảy outer section (stack dọc), đi xuống rồi đi phải:

1. L13-00–07: mạch 1.
2. L13-08–12: mạch 2.
3. L13-13–20: mạch 3.
4. L13-21–25 → L13-27 → L13-26: mạch 4; thứ tự DOM cục bộ là 25→27→26 (L13-27 đứng trước L13-26 dù ID lớn hơn).
5. L13-28–31: mạch 5.
6. L13-32–34→33–40: mạch 6; thứ tự DOM cục bộ là 32→34→33 (L13-34 đứng trước L13-33 dù ID lớn hơn).
7. L13-41 + X01–X04: mạch 7 và phụ lục, cùng một outer stack; từ L13-41 đi xuống vào X01 rồi tiếp tục xuống X04.

## Mạch và dấu vết dữ liệu

Một hành lang được truyền xuyên suốt:

`quỹ đạo chuyên gia → cặp (s,a) → phân phối BC → trạng thái lệch → vòng tương tác → chuyển tiếp (S,A,R,S') → lợi tức → V/Q → đích Bellman → cập nhật bảng Q → một hàng DQN 5 trường (S,A,R,S',D^{term}) → q=.4, Y=.9, sai số bình phương=.25`.

Quy ước duy nhất: hành động $A_t$ sinh $R_{t+1}$ và $S_{t+1}$. Quỹ đạo T bước kết thúc ở $S_T$ và không có $A_T$. Cờ $D^{term}$ đánh dấu kết thúc thật của MDP và triệt giá trị tương lai trong đích.

## Nguồn

| Nguồn | Dải | Vai trò |
|---|---|---|
| DOCX, Buổi 13 | — | LLO26/27, nội dung kỹ thuật bắt buộc; nguồn của L13-01, L13-13, L13-16 |
| CS285 L02 Behavioral Cloning | PDF 8–39 | Trình diễn, BC, phân phối hành động, lệch phân phối, DAgger |
| CS285 L07 Value-based RL | PDF 5–20 | Giá trị, học ngoài chính sách, thăm dò, bộ nhớ phát lại |
| CS285 L08 Q-learning Practice | PDF 2–22 | DQN, ngắt gradient, mạng đích và ổn định |
| Illinois L12 Imitation Learning | PDF 1–14 | Lệch phân phối tuần tự và DAgger |
| Illinois L10 Deep RL | PDF 1–8 | Cầu nối Q-learning với mạng Q |
| `hocsau_draft.pdf` | PDF 335–344 | MDP, lợi tức, V/Q, Bellman, Q-learning và thăm dò |
| `lec01_intro.pdf` | PDF 45–46 | Đã kiểm kê; không dùng trong bài |

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
| $D^{term}$ | cờ kết thúc thật; triệt giá trị tương lai trong đích |
| $\theta,\bar\theta$ | tham số mạng hiện tại và mạng đích |

Lô DQN: $S,S'\in\mathbb R^{B\times D_s}$; $A\in\{0,\ldots,D_a-1\}^{B}$; $R\in\mathbb R^B$; $D^{term}\in\{0,1\}^{B}$; $Q_{all}\in\mathbb R^{B\times D_a}$; $q_{sa},Y\in\mathbb R^B$; mất mát vô hướng.

## Bài tập 50 phút

1. Xác định dữ liệu, chính sách và phân phối hành động trong BC — 10 phút.
2. Phân tích lệch phân phối trên quỹ đạo hành lang — 10 phút.
3. Nhận diện năm thành phần theo LLO26 và chính sách thuộc tác tử — 10 phút.
4. Tính lợi tức, đích Bellman và một cập nhật Q — 15 phút.
5. Chỉ ra bộ nhớ phát lại, phép lấy theo hành động, ngắt gradient và mạng đích — 5 phút.
