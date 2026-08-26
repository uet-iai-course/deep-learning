# Storyboard Bài 13

## Chu trình sáu bước

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính toán | Triển khai/ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|
| BC và lệch phân phối | 00 | 02 | 03–04, 08 | 05–06, 09–10 | 07, 11 | 06, 12 |
| MDP | 13 | 14 | 15–16 | 17–19 | 20 | 16, 20 |
| Giá trị và Bellman | 19 | 21–22, 24 | 19, 23, 26 | 21–22, 25, 27 | 24, 26 | 19, 23, 26 |
| Q-learning | 28 | 29–30 | 26, 31 | 27–28 | 29–31 | 31 |
| DQN | 32 | 34 | 35–38 | 33, 36–38 | 39–40 | 41 |

- L13-16 gộp ví dụ và kiểm tra chẩn đoán vì sinh viên phải gọi tên sáu thành phần trước khi thấy tuple MDP.
- L13-20 gộp triển khai và kiểm tra vì quyết định bootstrap phụ thuộc trực tiếp hai cờ vừa định nghĩa.
- L13-19, 23 và 26 gộp ví dụ với kiểm tra; đáp án dùng fragment để giữ thứ tự hoạt động → tính toán.
- L13-24 gộp vấn đề và trực giác: đối chiếu Monte Carlo với sai phân thời gian tạo nhu cầu cho đích Bellman một bước.
- X01–X04 là phụ lục luyện sâu, không mang dữ kiện bắt buộc trở lại lõi.

## Dấu vết xuyên suốt

`tau chuyên gia → D_E với M cặp → lô BC B×D_a → trạng thái lệch → (S_t,A_t,R_{t+1},S_{t+1}) → G=(.81,.9,1) → Q(s_1,phải) → Y=.9 → Q bảng .4→.5 → một hàng DQN (s_1,phải,0,s_2,0,0) → q=.4 → Y=.9 → hạng tử bình phương .25`.

Hai cờ xuất hiện ở L13-20, được đóng gói ở L13-35, dùng trong đích L13-37 và vòng đặt lại môi trường L13-39. Chính sách hành vi $\mu$ xuất hiện ở L13-29; phép cực đại thuộc chính sách đích.

## Từng trang: vai trò, đầu vào, đầu ra và câu nối

Mỗi trang có một vai trò chính trong sáu bước. `N/A` chỉ dùng cho trang định hướng, kèm lý do.

| ID | Phút | Vai trò | Đầu vào → đầu ra kiểm chứng / dữ liệu mang theo | Câu nối |
|---|---:|---|---|---|
| L13-00 | 3 | Vấn đề | Trạng thái do chính sách tạo → nhu cầu học tuần tự | “Bắt đầu từ dữ liệu chuyên gia.” |
| L13-01 | 3 | N/A — định hướng LLO, không phải khái niệm | Tiên quyết → bốn sản phẩm: loss BC, đích, Q-update, lô DQN | “Một hành lang sẽ tạo cả bốn.” |
| L13-02 | 3 | Trực giác | Hành lang $s_0,s_1,s_2$ → vật thể xuyên bài | “Chuyên gia để lại quỹ đạo nào?” |
| L13-03 | 3 | Ví dụ | Hành lang → $\tau^E$ đúng chỉ số T bước | “Tách quỹ đạo thành cặp có nhãn.” |
| L13-04 | 3 | Ví dụ | $\tau^E$ → $\mathcal D_E$ gồm M cặp | “Dùng các cặp này để học phân phối hành động.” |
| L13-05 | 3 | Hình thức | $\mathcal D_E$ → loss BC; phân biệt M và B | “Một phân phối rời rạc trông thế nào?” |
| L13-06 | 3 | Kiểm tra | Xác suất ba hành động → xác định xác suất phải tăng | “Loss nhỏ chưa đủ để đánh giá vận hành.” |
| L13-07 | 3 | Triển khai | Mô hình BC → hợp đồng huấn luyện/đánh giá quỹ đạo | “Khi tự chạy, chính sách tạo đầu vào mới.” |
| L13-08 | 3 | Ví dụ | Hành lang → nhánh trạng thái chưa có nhãn | “Hai phân phối trạng thái nay khác nhau.” |
| L13-09 | 3 | Hình thức | Nhánh lỗi → $d_{\pi_E}$ và $d_{\pi_\theta}$ | “Sai một bước có thể kéo dài.” |
| L13-10 | 3 | Hình thức | Hai phân phối → cơ chế tích lũy lỗi, không claim định lượng | “Có thể lấy nhãn ở trạng thái mới không?” |
| L13-11 | 3 | Triển khai | Trạng thái chính sách ghé → chu trình DAgger có truy vấn expert | “Kiểm tra vì sao loss và lợi tức lệch nhau.” |
| L13-12 | 3 | Kiểm tra | $d_{\pi_E},d_{\pi_\theta}$ → giải thích loss giảm nhưng lợi tức thấp | “Nếu không có nhãn hành động thì dùng tín hiệu nào?” |
| L13-13 | 3 | Vấn đề | BC → quyết định BC hay RL theo nguồn tín hiệu | “RL cần vòng tương tác.” |
| L13-14 | 3 | Trực giác | Tác tử/môi trường → vòng $S_t,A_t,R_{t+1},S_{t+1}$ | “Viết vòng này thành dữ liệu hành lang.” |
| L13-15 | 3 | Ví dụ | Vòng tương tác → ba chuyển tiếp cụ thể | “Gọi tên sáu thành phần trước khi ký hiệu hóa.” |
| L13-16 | 2 | Ví dụ + kiểm tra chẩn đoán | Chuyển tiếp → sáu thành phần LLO26 | “Bây giờ đóng gói môi trường thành MDP.” |
| L13-17 | 2 | Hình thức | Sáu thành phần → $\mathcal M=(S,A,P,r,\gamma,\rho_0)$; policy tách riêng | “Trạng thái phải đủ thông tin gì?” |
| L13-18 | 2 | Hình thức | MDP → điều kiện Markov và ví dụ thêm vận tốc | “Phần thưởng xa được cộng thế nào?” |
| L13-19 | 2 | Ví dụ + kiểm tra | $(0,0,1),\gamma=.9$ → $G_2=1,G_1=.9,G_0=.81$ | “Trước khi bootstrap, phân biệt hai kiểu kết thúc.” |
| L13-20 | 2 | Triển khai + kiểm tra | Chuyển tiếp → $D^{term},D^{trunc}$ và quyết định giữ giá trị tương lai | “Định nghĩa giá trị kỳ vọng.” |
| L13-21 | 2 | Hình thức | $G_t$ → $V^\pi(s)$ | “Giữ cố định hành động đầu tiên.” |
| L13-22 | 2 | Trực giác + hình thức | $V^\pi$ → $Q^\pi(s,a)$ | “Kỳ vọng và cực đại có giống nhau không?” |
| L13-23 | 2 | Ví dụ + kiểm tra | Hai Q-value → kỳ vọng .5 và max .8 | “Đích một bước khác lợi tức đầy đủ ra sao?” |
| L13-24 | 2 | Vấn đề + trực giác | Monte Carlo → sai phân thời gian | “Viết quan hệ dưới chính sách đang xét.” |
| L13-25 | 2 | Hình thức | Đích TD → Bellman của policy | “Thử một chuyển tiếp cụ thể.” |
| L13-27 | 2 | Hình thức | Bellman chính sách → Bellman tối ưu với $a'\in\mathcal A$ hữu hạn | “Thử trên một chuyển tiếp hành lang.” |
| L13-26 | 2 | Ví dụ + kiểm tra | $(s_1,phải,0,s_2)$ → $Y=.9$ | “Không biết P thì dùng mẫu quan sát.” |
| L13-28 | 2 | Vấn đề + hình thức | Bellman → cập nhật Q-learning một mẫu, terminal mask | “Dữ liệu và chính sách đích có thể khác.” |
| L13-29 | 2 | Trực giác | $\mu$ và max-target → học ngoài chính sách, vẫn cần độ phủ | “Chính sách hành vi tạo độ phủ thế nào?” |
| L13-30 | 2 | Triển khai | Q hiện tại → epsilon-tham lam thu thập dữ liệu | “Tính một cập nhật bảng.” |
| L13-31 | 2 | Ví dụ + kiểm tra | $Q=.4,Y=.9,\alpha=.2$ → $.5$ và chỉ một ô đổi | “Bảng Q không mở rộng tốt.” |
| L13-32 | 2 | Vấn đề | Bảng Q → nhu cầu xấp xỉ hàm | “Mạng phải xuất tensor nào?” |
| L13-34 | 2 | Trực giác | Thu thập→lưu→lấy mẫu→hai nhánh→mất mát | “Khóa tensor của từng nhánh.” |
| L13-33 | 2 | Hình thức | $S:B\times D_s$ → $Q_{all}:B\times D_a$; mở rộng DQN | “Đóng gói hàng hành lang vào lô.” |
| L13-35 | 2 | Ví dụ | $(s_1,phải,0,s_2,0,0)$ → shapes tổng quát | “Nhánh hiện tại chọn đúng hành động.” |
| L13-36 | 2 | Hình thức + ví dụ | $Q_\theta(s_1)=[.1,.4]$ → $q_{sa}=.4$; lô B | “Nhánh đích tạo Y.” |
| L13-37 | 2 | Hình thức + ví dụ | Hàng hành lang → $Y=.9$, stop-gradient và terminal mask | “Hai nhánh gặp nhau ở mất mát.” |
| L13-38 | 2 | Hình thức + kiểm tra số | $q=.4,Y=.9$ → hạng tử bình phương .25; giới hạn hội tụ | “Đặt các phép tính vào vòng tuần tự.” |
| L13-39 | 2 | Triển khai | Khởi tạo, đóng băng, thu thập, lưu, reset hai cờ | “Sau làm ấm, cập nhật mạng.” |
| L13-40 | 2 | Triển khai | Lấy mẫu, target, zero-grad, backward, step, hard sync | “Tự rà nguồn tín hiệu và gradient.” |
| L13-41 | 2 | Kiểm tra | BC/Q/DQN → terminal, gradient và quyết định BC/RL | “Dừng lõi hoặc đi sang phụ lục.” |
| L13-X01 | 5 | Hình thức + kiểm tra mở rộng | Hành động liên tục → Gaussian đường chéo, $\sigma>0$, giới hạn một mode | “Tiếp tục với cờ cắt thời gian.” |
| L13-X02 | 5 | Ví dụ + kiểm tra mở rộng | $(S_{99},A_{99},R_{100},S_{100})$ → giữ bootstrap khi truncated | “Ngoài chính sách còn cần gì?” |
| L13-X03 | 5 | Vấn đề + kiểm tra mở rộng | Replay thiếu hành động → kết luận cần độ phủ | “Rà toàn bộ lô DQN.” |
| L13-X04 | 5 | Kiểm tra mở rộng | $B=32,D_a=4$ → shapes và đường gradient | Kết thúc phụ lục. |

## Thời lượng và điều hướng thật

- L13-00–15: 16 trang × 3 phút = 48 phút.
- L13-16–41: 26 trang × 2 phút = 52 phút.
- Lõi: 100 phút, 42 trang.
- Phụ lục X01–X04: 4 trang × 5 phút = 20 phút.
- Bài tập: 50 phút riêng, không cộng vào 120 phút.
- DOM có bốn stack dọc: L13-00–12; L13-13–25→L13-27→L13-26; L13-28–41; và X01–X04. Đi phải tại L13-12, rồi đi xuống đến L13-26 trước khi đi phải sang L13-28. Dừng ở L13-41 cho tuyến 100 phút. Chỉ đi phải từ L13-41 nếu dạy phụ lục 20 phút, rồi đi xuống X01→X04.
- Phụ lục là một tuyến cuối duy nhất, không còn mô tả sai rằng X01–X04 gắn sau các slide lõi khác nhau.
