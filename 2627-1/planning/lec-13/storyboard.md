# Storyboard Bài 13

## Bảy mạch: chức năng, kết nối vào và kết nối ra

| # | Mạch | Chức năng | Kết nối vào | Kết nối ra |
|---|---|---|---|---|
| 1 | BC và dữ liệu trình diễn (L13-00–07, 8 trang, 24 phút) | Đặt vấn đề học từ chuyên gia; dựng $\mathcal D_E$, loss BC, hợp đồng huấn luyện/đánh giá | Từ bài trước: hồi quy và entropy chéo | Giao $\mathcal D_E$ và loss BC cho mạch 2; câu hỏi "nếu không có nhãn hành động?" |
| 2 | Lệch phân phối và DAgger (L13-08–12, 5 trang, 15 phút) | Giải thích vì sao BC hỏng khi chính sách tự vận hành; giới thiệu DAgger | Nhận $\mathcal D_E$ và loss BC từ mạch 1 | Trả lời kiểm tra L13-12; nêu nhu cầu tín hiệu mới → mạch 3 |
| 3 | Từ BC sang RL: tương tác và MDP (L13-13–20, 8 trang, 19 phút) | Quyết định BC/RL; vòng tương tác; sáu thành phần LLO26; tuple MDP; Markov; lợi tức; cờ $D^{term}$ | Nhận câu hỏi thiếu nhãn từ mạch 2 | Chuyển giao lợi tức $G_t$ và $D^{term}$ cho mạch 4 |
| 4 | Lợi tức, giá trị và Bellman (L13-21–27, 7 trang, 14 phút) | Định nghĩa $V^\pi,Q^\pi$; phân biệt kỳ vọng/cực đại; MC/TD; Bellman chính sách và tối ưu | Nhận $G_t$ và $D^{term}$ từ mạch 3 | Đưa Bellman tối ưu và đích một bước $Y=.9$ cho mạch 5 |
| 5 | Q-learning ngoài chính sách (L13-28–31, 4 trang, 8 phút) | Thay kỳ vọng bằng mẫu quan sát; off-policy; epsilon-tham lam; cập nhật bảng | Nhận Bellman tối ưu từ mạch 4 | Cập nhật bảng $.4\to.5$; bảng không mở rộng → mạch 6 |
| 6 | DQN từ pipeline đến giả mã (L13-32–40, 9 trang, 18 phút) | Xấp xỉ hàm; pipeline; tensor lô; hai nhánh; mất mát; hai pha giả mã | Nhận nhu cầu xấp xỉ từ mạch 5 | Hàng hành lang qua $q=.4$, $Y=.9$, hạng tử $.25$; giả mã hai pha → mạch 7 |
| 7 | Tổng kết và phụ lục (L13-41; X01–X04, 5 trang, 2 phút lõi + 20 phút phụ) | Kiểm tra tổng hợp ba nguồn tín hiệu; phụ lục luyện sâu | Nhận BC/Q/DQN từ mạch 6 | Dừng lõi tại L13-41; nếu dạy phụ lục, đi xuống vào X01 rồi tiếp tục xuống X04 |

## Chu trình sáu bước theo từng cụm

Mỗi cụm đi đủ: vấn đề → trực giác → ví dụ → hình thức → triển khai → kiểm tra.

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính toán | Triển khai/ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|
| Mạch 1: BC | 00 | 02 | 03–04 | 05–06 | 07 | 06 |
| Mạch 2: lệch phân phối | 08 | 09 | 08 | 09–10 | 11 | 12 |
| Mạch 3: RL và MDP | 13 | 14 | 15–16 | 17–19 | 20 | 16, 20 |
| Mạch 4: giá trị và Bellman | 24 | 21–22 | 19, 23, 26 | 21–22, 25, 27 | 21 (hình thức) | 19, 23, 26 |
| Mạch 5: Q-learning | 28 | 29–30 | 31 | 28 | 29–30 | 31 |
| Mạch 6: DQN | 32 | 34 | 35–38 | 33, 36–38 | 39–40 | 38 |
| Mạch 7: tổng kết | 41 | — | — | — | — | 41 |

- L13-26 không thuộc mạch 5; nó là cầu vào mạch 5 (ví dụ đích một bước dẫn sang Q-learning), nằm trong stack mạch 4.
- L13-21 giữ vai trò hình thức (định nghĩa $V^\pi$) cho mạch 4; không mang ví dụ.

- L13-16 gộp ví dụ và kiểm tra chẩn đoán vì sinh viên phải gọi tên sáu thành phần trước khi thấy tuple MDP.
- L13-20 gộp triển khai và kiểm tra vì quyết định triệt giá trị tương lai phụ thuộc trực tiếp cờ vừa định nghĩa.
- L13-19, 23 và 26 gộp ví dụ với kiểm tra; đáp án dùng fragment để giữ thứ tự hoạt động → tính toán.
- L13-24 gộp vấn đề và trực giác: đối chiếu Monte Carlo với sai phân thời gian tạo nhu cầu cho đích Bellman một bước.
- X01–X04 là phụ lục luyện sâu, không mang dữ kiện bắt buộc trở lại lõi.

## Dấu vết xuyên suốt

`tau chuyên gia → D_E với M cặp → lô BC B×D_a → trạng thái lệch → (S_t,A_t,R_{t+1},S_{t+1}) → G=(.81,.9,1) → Q(s_1,phải) → Y=.9 → Q bảng .4→.5 → một hàng DQN 5 trường (S,A,R,S',D^{term}) = (s_1,phải,0,s_2,0) → q=.4 → Y=.9 → sai số bình phương .25`.

Cờ $D^{term}$ xuất hiện ở L13-20, được đóng gói ở L13-35, dùng trong đích L13-37 và vòng đặt lại môi trường L13-39. Chính sách hành vi $\mu$ xuất hiện ở L13-29; phép cực đại thuộc chính sách đích.

## Từng trang: vai trò, đầu vào, đầu ra và câu nối

Mỗi trang có một vai trò chính trong sáu bước. `N/A` chỉ dùng cho trang định hướng, kèm lý do. Mọi câu nối trong cột “Câu nối” là lời giảng viên nói miệng, không hiển thị trên slide.

| ID | Phút | Vai trò | Đầu vào → đầu ra kiểm chứng / dữ liệu mang theo | Câu nối |
|---|---:|---|---|---|
| L13-00 | 3 | Vấn đề | Trạng thái do chính sách tạo → nhu cầu học tuần tự | “Bắt đầu từ dữ liệu chuyên gia.” |
| L13-01 | 3 | N/A — định hướng LLO, không phải khái niệm | Tiên quyết → bốn sản phẩm: loss BC, đích, Q-update, lô DQN | “Một hành lang sẽ tạo cả bốn.” |
| L13-02 | 3 | Trực giác | Hành lang $s_0,s_1,s_2$ → vật thể xuyên bài | “Chuyên gia để lại quỹ đạo nào?” |
| L13-03 | 3 | Ví dụ | Hành lang → $\tau^E$ đúng chỉ số T bước | “Tách quỹ đạo thành cặp có nhãn.” |
| L13-04 | 3 | Ví dụ | $\tau^E$ → $\mathcal D_E$ gồm M cặp | “Dùng các cặp này để học phân phối hành động.” |
| L13-05 | 3 | Hình thức | $\mathcal D_E$ → loss BC; phân biệt M và B | “Một phân phối rời rạc trông thế nào?” |
| L13-06 | 3 | Kiểm tra | Xác suất hai hành động → xác định xác suất phải tăng | “Loss nhỏ chưa đủ để đánh giá vận hành.” |
| L13-07 | 3 | Triển khai | Mô hình BC → hợp đồng huấn luyện/đánh giá quỹ đạo | “Khi tự chạy, chính sách tạo đầu vào mới.” |
| L13-08 | 3 | Vấn đề + ví dụ | Hành lang → nhánh trạng thái chưa có nhãn | “Hai phân phối trạng thái nay khác nhau.” |
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
| L13-20 | 2 | Triển khai + kiểm tra | Chuyển tiếp → $D^{term}$ và quyết định triệt giá trị tương lai | “Định nghĩa giá trị kỳ vọng.” |
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
| L13-35 | 2 | Ví dụ | Hàng 5 trường $(S,A,R,S',D^{term})=(s_1,phải,0,s_2,0)$ → shapes tổng quát | “Nhánh hiện tại chọn đúng hành động.” |
| L13-36 | 2 | Hình thức + ví dụ | $Q_\theta(s_1)=[.1,.4]$ → $q_{sa}=.4$; lô B | “Nhánh đích tạo Y.” |
| L13-37 | 2 | Hình thức + ví dụ | Hàng hành lang → $Y=.9$, stop-gradient và terminal mask | “Hai nhánh gặp nhau ở mất mát.” |
| L13-38 | 2 | Hình thức + kiểm tra số | $q=.4,Y=.9$ → sai số bình phương .25; giới hạn hội tụ | “Đặt các phép tính vào vòng tuần tự.” |
| L13-39 | 2 | Triển khai | Khởi tạo, đóng băng, thu thập, lưu, reset khi terminal | “Sau làm ấm, cập nhật mạng.” |
| L13-40 | 2 | Triển khai | Lấy mẫu, target, zero-grad, backward, step, hard sync | “Tự rà nguồn tín hiệu và gradient.” |
| L13-41 | 2 | Kiểm tra | BC/Q/DQN → terminal, gradient và quyết định BC/RL | “Dừng lõi hoặc đi sang phụ lục.” |
| L13-X01 | 5 | Hình thức + kiểm tra mở rộng | Hành động liên tục → Gaussian đường chéo, $\sigma>0$, giới hạn một mode | “Tiếp tục với kiểm tra cờ kết thúc.” |
| L13-X02 | 5 | Ví dụ + kiểm tra mở rộng | Chuyển tiếp cuối có $D^{term}=1$ → đích chỉ còn $R_{t+1}$ | “Ngoài chính sách còn cần gì?” |
| L13-X03 | 5 | Vấn đề + kiểm tra mở rộng | Replay thiếu hành động → kết luận cần độ phủ | “Rà toàn bộ lô DQN.” |
| L13-X04 | 5 | Kiểm tra mở rộng | $B=32,D_a=4$ → shapes và đường gradient | Kết thúc phụ lục. |

## Thời lượng và điều hướng thật

- Mạch 1 (L13-00–07): 8 trang × 3 phút = 24 phút.
- Mạch 2 (L13-08–12): 5 trang × 3 phút = 15 phút.
- Mạch 3 (L13-13–20): 3 trang × 3 phút + 5 trang × 2 phút = 19 phút (L13-13–15 là 3 phút, L13-16–20 là 2 phút).
- Mạch 4 (L13-21–27): 7 trang × 2 phút = 14 phút.
- Mạch 5 (L13-28–31): 4 trang × 2 phút = 8 phút.
- Mạch 6 (L13-32–40): 9 trang × 2 phút = 18 phút.
- Mạch 7: L13-41 = 2 phút; X01–X04 = 4 trang × 5 phút = 20 phút.
- Lõi: 100 phút, 42 trang. Phụ lục: 20 phút. Bài tập: 50 phút riêng, không cộng vào lõi.
- DOM có bảy outer section (stack dọc): L13-00–07; L13-08–12; L13-13–20; L13-21–25→L13-27→L13-26; L13-28–31; L13-32–40; L13-41 + X01–X04. Biên: đi phải tại L13-07, L13-12, L13-20, L13-26, L13-31 và L13-40. Trong stack thứ tư, thứ tự DOM là 25→27→26 (L13-27 đứng trước L13-26 dù ID lớn hơn); trong stack thứ sáu, thứ tự DOM là 32→34→33 (L13-34 đứng trước L13-33). Dừng ở L13-41 cho tuyến 100 phút. L13-41 và X01–X04 nằm cùng một outer stack: nếu dạy phụ lục 20 phút, đi xuống từ L13-41 để vào X01, rồi tiếp tục xuống X04; không đi phải.
- Phụ lục là một tuyến cuối duy nhất, không còn mô tả sai rằng X01–X04 gắn sau các slide lõi khác nhau.
