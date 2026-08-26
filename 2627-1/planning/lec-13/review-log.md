# Nhật ký rà soát Bài 13

## Quyết định nguồn và ký hiệu

| Quyết định | Lý do |
|---|---|
| Dùng một hành lang tự dựng | Nối BC, lệch phân phối, MDP, Bellman, Q-learning và DQN bằng cùng dữ kiện; mọi số được tự tính |
| Giữ BC trước RL | Khớp `source.md` và nguồn chính CS285 L02 |
| Dùng $R_{t+1}$ sau $A_t$ | Tránh lẫn chỉ số giữa quỹ đạo, vòng tương tác và đích Bellman |
| MDP dùng $(S,A,P,r,\gamma,\rho_0)$ với $P(s'|s,a)$ và $r(s,a,s')$ | Loại mâu thuẫn giữa phân phối chung $p(s',r|s,a)$ và hàm thưởng tách riêng |
| Tách policy khỏi tuple MDP | Policy mô tả tác tử; MDP ở deck mô tả môi trường |
| Tách $D^{term}$ và $D^{trunc}$ | Kết thúc thật triệt giá trị tương lai; cắt thời gian không tự triệt nếu $S'$ hợp lệ |
| Bellman tối ưu giả sử tập hành động hữu hạn | Phép cực đại được duyệt trực tiếp; không suy rộng sang hành động liên tục |
| DQN dùng MSE, target network đóng băng và đồng bộ cứng | Khớp CS285 L08; không thêm Huber mặc định hoặc soft update |
| Không claim hội tụ DQN phi tuyến | Nguồn không cung cấp bảo đảm hội tụ tổng quát |
| Không code demo hoặc benchmark | Không được yêu cầu; không có nguồn code được khóa cho sản phẩm này |

## Hợp nhất phản biện và thay đổi

| Vấn đề đã nhận | Xử lý |
|---|---|
| Tên L13-13 khiến reward giống nhãn thay thế | Đổi thành RL học từ phần thưởng và tương tác; thêm cầu quyết định BC/RL |
| Gaussian làm đứt tuyến rời rạc | L13-06 giữ phân phối rời rạc; Gaussian chuyển sang X01, khóa covariance đường chéo và $\sigma>0$ |
| MDP dùng thành phần không nhất quán | Sắp lại interaction→transitions→kiểm tra sáu thành phần→tuple MDP→Markov |
| Thiếu kiểm tra LLO26 | L13-16 yêu cầu nhận diện tác tử, môi trường, trạng thái, hành động, reward và policy |
| Lợi tức và Bellman xuất hiện dày | Thêm cầu Monte Carlo/sai phân thời gian, fragment trước đáp án ở L13-19, 23, 26 |
| Dấu vết hành lang dừng trước DQN | L13-35–38 truyền hàng $(s_1,phải,0,s_2,0,0)$ qua $q=.4$, $Y=.9$, hạng tử bình phương $.25$ |
| Pipeline DQN xuất hiện sau chi tiết | Đưa pipeline lên L13-34, trước shapes, gather, target và loss |
| Thiếu thuật toán tuần tự | L13-39–40 chứa khởi tạo, freeze, collect no-grad, warmup, sample, target, zero-grad, backward, step, hard sync, reset hai cờ |
| Tuyến X được mô tả như bốn nhánh nhưng DOM là stack cuối | Khóa một phụ lục cuối 20 phút; planning ghi điều hướng thật |
| M/B, quỹ đạo, cờ và X02 lệch chỉ số | Khóa M là dataset, B là minibatch; quỹ đạo T bước; X02 dùng $R_{100},S_{100}$ |
| Thuật ngữ Anh và SVG DQN nhỏ | Việt hóa mặt slide; mở rộng BC/RL/MDP/DQN lần đầu; SVG DQN dùng nhãn Việt từ 28 px |

## Rà trang lân cận sau đổi thứ tự/nội dung

- L13-03–08: quỹ đạo không có $A_T$; M/B nhất quán; L13-06 nối trực tiếp sang đánh giá BC.
- L13-11–20: cầu BC/RL, interaction, transitions, kiểm tra sáu thành phần, MDP và Markov không dùng tiên quyết về sau.
- L13-17–29: lợi tức → hai cờ → V/Q → Monte Carlo/sai phân thời gian → Bellman chính sách → Bellman tối ưu → ví dụ → Q-learning.
- L13-30–41: thăm dò → cập nhật bảng → nhu cầu mạng → sơ đồ DQN → kích thước tensor → hàng số → đích/mất mát → hai pha giả mã → kiểm tra.
- X01–X04 và L13-39–41: phụ lục không mang dữ kiện bắt buộc trở lại lõi; chỉ đi phải sau L13-41.

## Tài sản

Năm SVG được HTML tham chiếu: `corridor.svg`, `bc-shift.svg`, `mdp-loop.svg`, `bellman-backup.svg`, `dqn-pipeline.svg`. `dqn-pipeline.svg` được vẽ lại bằng nhãn tiếng Việt từ 28 px, có `title`, `desc`, các bước thu thập/lưu/lấy mẫu và hai nhánh hiện tại/đích. Không có raster hoặc tài nguyên mạng.

## Tự rà toán và triển khai

- Hành lang: $G_2=1,G_1=.9,G_0=.81$ với $\gamma=.9$.
- Đích: $0+.9\times1=.9$; cập nhật bảng $.4+.2(.9-.4)=.5$.
- Hàng DQN: dự đoán $.4$, đích $.9$, hạng tử bình phương $(.4-.9)^2=.25$; đóng góp vào mất mát trung bình là $.25/B$.
- Batch: $Q_{all}:B\times D_a$; chỉ số lấy hành động $B\times1$; $q_{sa},Y:B$; loss vô hướng.
- Gradient chỉ qua $Q_\theta(S,A)$; $\bar\theta$ đóng băng, không thuộc optimizer; đồng bộ cứng mỗi C bước.
- Môi trường reset khi $D^{term}\lor D^{trunc}$; chỉ $D^{term}$ triệt giá trị tương lai trong target.

## Tự biên tập

- `no-ai-slop`: bỏ khẩu hiệu, câu hỏi tu từ và cụm dẫn rỗng; giữ câu ngắn, động từ tính/nhận diện/chọn/truy vết; không thêm claim.
- `quill`: rà liên tục ký hiệu $M/B$, $R_{t+1}$, $S_T$, hai cờ, $\theta/\bar\theta$ và câu nối giữa năm cụm; không tạo `quill.json`.

## Trạng thái

Vòng chỉnh sửa riêng đã hoàn tất trong phạm vi B13. Cần kiểm định cuối bằng trình duyệt/Codex Slides trước bàn giao chính thức; lượt này chỉ chạy kiểm tra tĩnh và KaTeX nếu công cụ cục bộ cho phép.

## Hậu kiểm điều phối viên

- Đưa Bellman tối ưu L13-27 trước ví dụ cực đại L13-26; rà lại L13-24–29.
- Đưa sơ đồ DQN L13-34 trước kích thước tensor L13-33; rà lại L13-32–36.
- Sửa điều hướng sau đổi thứ tự: stack thứ hai kết thúc ở L13-26; chỉ đi phải sang L13-28 sau trang này.
- Tách rõ $P(s'\mid s,a)$, hàm thưởng xác định và xác suất điều kiện $\Pr$.
- Sửa $.25$ thành hạng tử bình phương; mất mát trung bình nhận đóng góp $.25/B$.
- Bổ sung bộ tối ưu, cập nhật trạng thái, bộ đếm bước cập nhật và hợp đồng Gaussian theo lô.
- KaTeX strict dựng 162 biểu thức, không lỗi; 46 ID và 46 ghi chú, không trùng hoặc thiếu.
- Dựng montage của cả năm SVG; thay glyph chỉ số dưới Unicode bằng `s0`, `A(t)`, `S(t+1)` để nhãn không mất trong renderer.
- `python3 -m reloadserver 8765` không khả dụng; máy chủ HTTP đang có trên cổng 8765 trả 200 cho HTML, SVG, CSS, RevealJS và KaTeX.
- Không có trình duyệt/Codex Slides trong môi trường; không tuyên bố đã duyệt từng viewport.
