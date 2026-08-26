# Bài 14 — Siêu học tập

## Mục tiêu, phạm vi và thời lượng

- Đối tượng: sinh viên đã biết phân phối xác suất, gradient, quy tắc chuỗi, entropy chéo, softmax ổn định và chia huấn luyện–kiểm định–kiểm tra.
- LLO28: giải thích động lực, phân phối tác vụ, episode và mục tiêu đánh giá sau thích nghi.
- LLO29: mô tả và so sánh Siamese, ProtoNet, MAML theo dữ liệu, trạng thái thích nghi, dự đoán và gradient.
- Tuyến lõi L14-00–41: 100 phút. Phụ lục L14-X01–X04: 20 phút. Tiết bài tập: 50 phút riêng.
- Không mở rộng sang meta-RL, benchmark, mã triển khai hoặc kết luận một phương pháp luôn tốt hơn.

## Mạch khái niệm

Tình huống 5-way 1-shot → phân phối tác vụ → hợp đồng support/query và N/K/R/B → episode G 2-way 2-shot → mục tiêu sau thích nghi → Siamese trên G → ProtoNet trên G → trạng thái thích nghi metric/optimization → MAML trên G → thuật toán hai vòng → meta-gradient → meta-test và rò rỉ → so sánh ba họ trên G → kiểm tra quyết định.

## Dấu vết dữ liệu và ký hiệu

- Episode G: lớp A có hỗ trợ 0, 2 và truy vấn 2.5; lớp B có hỗ trợ 4, 6 và truy vấn 4.5. Đây là biểu diễn một chiều tự dựng, không phải số liệu thực nghiệm.
- Hợp đồng: $X^S:[B,N,K,D_x]$, $X^Q:[B,N,R,D_x]$, $Y^S:[B,N,K]$, $Y^Q:[B,N,R]$; nhãn cục bộ $0,\ldots,N-1$.
- ProtoNet: $Z^S:[B,N,K,D]$ → $C:[B,N,D]$ → điểm chưa chuẩn hóa $[B,NR,N]$ → log-softmax theo trục lớp → NLL trung bình truy vấn rồi tác vụ.
- MAML trên G: bộ phân loại $P_\phi(B\mid h)=\sigma(w(h-3)+b)$; $\theta=(0,0)$ → gradient hỗ trợ $(-1,0)$ → $\phi=(1,0)$ → mất mát truy vấn $.3377$.
- Ví dụ I chỉ là vi-trace toán ở X03 để phân biệt exact/FO/HVP; không thay thế G trong so sánh ba phương pháp.

## Ánh xạ nguồn đã duyệt

| Nguồn | Dải PDF | Quyết định | Trang đích và lý do |
|---|---:|---|---|
| CS330 optimization-based meta-learning | 4–8 | Giữ, tách | L14-00, L14-02–09: đặt tình huống 5-way 1-shot trước phân phối tác vụ và mục tiêu. |
| Cùng tệp | 9–11 | Gộp, sửa | L14-26–28: cầu nối thích nghi metric/optimization và trực giác khởi tạo MAML; dùng G thay ví dụ rời. |
| Cùng tệp | 12–18 | Giữ, tách | L14-29–34: inner update, query loss, outer objective và thuật toán hai vòng. |
| Cùng tệp | 19–24 | Tách | L14-35–36 chỉ giữ dependency và FO ở mức khái niệm; exact/FO/HVP cùng ví dụ I chuyển X03 để giảm tải lõi. |
| Cùng tệp | 26–31 | Gộp, giữ ở phụ lục | L14-X04: vùng địa lý là tác vụ; bỏ kết quả benchmark và không suy diễn ưu thế. |
| CS330 metric-based meta-learning | 4–7 | Gộp, sửa | L14-03–09: episode, support/query và mục tiêu sau thích nghi. |
| Cùng tệp | 8–12 | Giữ, tách | L14-11–15: cặp G, Siamese dùng chung tham số, BCE trung bình và giới hạn bộ xác minh. |
| Cùng tệp | 13–17 | Giữ, tách | L14-16–25: prototype, khoảng cách, xác suất, NLL và rò rỉ. |
| Cùng tệp | 34 | Gộp | L14-26, L14-39–40: cùng khung dữ liệu/trạng thái thích nghi/dự đoán để đối chiếu. |
| Cùng tệp | 35–37 | Bỏ phần claim rộng | Chỉ giữ nhận định có điều kiện ở L14-40; bỏ khẳng định phổ quát về sức biểu đạt, nhất quán hoặc độ bất định. |
| Berkeley meta-learning | 4–5 | Giữ, gộp | L14-02–03: bài toán ít mẫu và phân phối tác vụ. |
| Cùng tệp | 18–23 | Giữ, gộp | L14-27, L14-35–37: MAML, đường meta-gradient và meta-test; bỏ nhánh meta-RL. |
| Homework ProtoNet/MAML | 1–3 | Giữ, sửa ký hiệu | L14-04–10: support/query, N/K/R/B và shape; đổi số truy vấn mỗi lớp thành R để dành $Q_i$ cho tập truy vấn. |
| Cùng tệp | 3–5 | Giữ, tách | L14-17–25: công thức ProtoNet; bỏ mã và benchmark. |
| Cùng tệp | 5–7 | Giữ, tách | L14-27–34: MAML inner update và outer objective; bỏ cấu hình triển khai không cần thiết. |
| Cùng tệp | 8–9 | Giữ ở phụ lục, bỏ benchmark | L14-X02: thay đổi K cần đánh giá riêng; không trình bày số liệu kết quả. |
| Giáo trình `hocsau_draft.pdf` | 288–293 | Chỉ dùng phân biệt | L14-X01: phân biệt siêu học tập ít mẫu và gợi ý ít mẫu; không đưa prompting vào lõi. |

## Chu trình học tập

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính | Triển khai/ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|
| Episode | 02–03 | 03–04 | 02, 08 | 05–06, 09 | 07 | 10 |
| Siamese | 11 | 12 | 11 | 13 | 14 | 15 |
| ProtoNet | 16 | 17–18 | 19, 21, 23 | 18, 20, 22–23 | 24 | 25 |
| MAML | 26–27 | 27–28 | 28–31 | 30, 32, 35–36 | 33–34, 37 | 38, 41 |
| So sánh | 26 | 39 | G xuyên suốt | 39–40 | 37, 40 | 41 |

## Bài tập 50 phút

1. 10 phút: xác định N/K/R/B, support/query và split hợp lệ.
2. 15 phút: tính prototype, điểm, log-softmax và NLL trên episode G.
3. 15 phút: thực hiện một inner update và viết outer objective MAML; không yêu cầu exact/FO.
4. 10 phút: so sánh ProtoNet và MAML theo trạng thái thích nghi, gradient và chi phí meta-test.
