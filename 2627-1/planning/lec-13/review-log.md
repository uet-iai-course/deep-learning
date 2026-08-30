# Nhật ký rà soát Bài 13

## Quyết định nguồn và ký hiệu

| Quyết định | Lý do |
|---|---|
| Dùng một hành lang tự dựng | Nối BC, lệch phân phối, MDP, Bellman, Q-learning và DQN bằng cùng dữ kiện; mọi số được tự tính |
| Giữ BC trước RL | Khớp `source.md` và nguồn chính CS285 L02 |
| Dùng $R_{t+1}$ sau $A_t$ | Tránh lẫn chỉ số giữa quỹ đạo, vòng tương tác và đích Bellman |
| MDP dùng $(S,A,P,r,\gamma,\rho_0)$ với $P(s'\mid s,a)$ và $r(s,a,s')$ | Loại mâu thuẫn giữa phân phối chung $p(s',r\mid s,a)$ và hàm thưởng tách riêng |
| Tách policy khỏi tuple MDP | Policy mô tả tác tử; MDP ở deck mô tả môi trường |
| Chỉ giữ $D^{term}$ | Truncation không có trong dải nguồn khóa; loại mọi $D^{trunc}$ và mọi nhắc đến cắt thời gian |
| Bellman tối ưu giả sử tập hành động hữu hạn | Phép cực đại được duyệt trực tiếp; không suy rộng sang hành động liên tục |
| DQN dùng MSE, target network đóng băng và đồng bộ cứng | Khớp CS285 L08; không thêm Huber mặc định hoặc soft update |
| Không claim hội tụ DQN phi tuyến | Nguồn không cung cấp bảo đảm hội tụ tổng quát |
| Không code demo hoặc benchmark | Không được yêu cầu; không có nguồn code được khóa cho sản phẩm này |

## Bổ sung và làm rõ so với nguồn

| Nội dung | Trạng thái | Lý do |
|---|---|---|
| $\rho_0$ trong tuple MDP | Bổ sung | Nguồn khóa nêu trạng thái đầu nhưng không dùng ký hiệu riêng; cần $\rho_0$ để tuple đủ sáu thành phần và nối với reset môi trường |
| $r(s,a,s')$ hàm thưởng xác định theo chuyển tiếp | Làm rõ | Nguồn khóa có phần thưởng theo chuyển tiếp; ký hiệu hàm xác định giúp tránh lẫn với kỳ vọng và khớp bảng chuyển tiếp L13-15 |
| Quy ước $R_{t+1}$ sinh sau $A_t$ | Làm rõ | Nguồn khóa dùng cả hai quy ước; chọn một quy ước duy nhất để quỹ đạo, vòng tương tác và đích cùng chỉ số |
| Dạng joint Markov $\Pr(S_{t+1},R_{t+1}\mid S_{0:t},A_{0:t})=\Pr(S_{t+1},R_{t+1}\mid S_t,A_t)$ | Làm rõ | Nguồn khóa nêu điều kiện Markov bằng lời; viết dạng joint để phân biệt với kernel $P(s'\mid s,a)$ |
| Monte Carlo đối chiếu sai phân thời gian (L13-24) | Bổ sung | Nguồn khóa có hai kiểu đích nhưng không đặt cạnh nhau; cần cầu này để Bellman một bước xuất hiện tự nhiên |
| Tách quỹ đạo huấn luyện/kiểm định/kiểm tra (L13-07) | Bổ sung | Giao thức dữ liệu của môn học; nguồn khóa không nói riêng cho BC |
| BC loss có bằng chứng gián tiếp | Ghi nhận | Loss BC là entropy chéo âm log-khả năng, tức maximum likelihood trên dữ liệu chuyên gia; nguồn khóa trình bày loss mà không gọi tên maximum likelihood, nên bài chỉ nêu liên hệ này như bằng chứng gián tiếp |

## Hợp nhất phản biện và thay đổi

| Vấn đề đã nhận | Xử lý |
|---|---|
| Tên L13-13 khiến reward giống nhãn thay thế | Đổi thành RL học từ phần thưởng và tương tác; thêm cầu quyết định BC/RL; nguồn của L13-13 sửa về DOCX, Buổi 13 |
| Gaussian làm đứt tuyến rời rạc | L13-06 giữ phân phối rời rạc; Gaussian chuyển sang X01, khóa covariance đường chéo và $\sigma>0$ |
| MDP dùng thành phần không nhất quán | Sắp lại interaction→transitions→kiểm tra sáu thành phần→tuple MDP→Markov |
| Thiếu kiểm tra LLO26 | L13-16 yêu cầu nhận diện tác tử, môi trường, trạng thái, hành động, reward và policy |
| Lợi tức và Bellman xuất hiện dày | Thêm cầu Monte Carlo/sai phân thời gian, fragment trước đáp án ở L13-19, 23, 26 |
| Dấu vết hành lang dừng trước DQN | L13-35–38 truyền hàng $(s_1,phải,0,s_2,0)$ qua $q=.4$, $Y=.9$, hạng tử bình phương $.25$ |
| Pipeline DQN xuất hiện sau chi tiết | Đưa pipeline lên L13-34, trước shapes, gather, target và loss |
| Thiếu thuật toán tuần tự | L13-39–40 chứa khởi tạo, freeze, collect no-grad, warmup, sample, target, zero-grad, backward, step, hard sync, reset khi terminal |
| Tuyến X được mô tả như bốn nhánh nhưng DOM là stack cuối | Khóa một phụ lục cuối 20 phút; planning ghi điều hướng thật |
| M/B, quỹ đạo, cờ và X02 lệch chỉ số | Khóa M là dataset, B là minibatch; quỹ đạo T bước; X02 đổi thành kiểm tra cờ kết thúc thật trong đích, không còn truncated |
| Thuật ngữ Anh và SVG DQN nhỏ | Việt hóa mặt slide; mở rộng BC/RL/MDP/DQN lần đầu; SVG DQN dùng nhãn Việt từ 28 px |
| Cấu trúc 4 section không khớp 7 mạch | Đổi sang 7 section: mạch 1 (L13-00–07), mạch 2 (L13-08–12), mạch 3 (L13-13–20), mạch 4 (L13-21–27), mạch 5 (L13-28–31), mạch 6 (L13-32–40), mạch 7 (L13-41 + X01–X04) |

## Rà trang lân cận sau đổi thứ tự/nội dung

- L13-03–08: quỹ đạo không có $A_T$; M/B nhất quán; L13-06 nối trực tiếp sang đánh giá BC.
- L13-11–20: cầu BC/RL, interaction, transitions, kiểm tra sáu thành phần, MDP và Markov không dùng tiên quyết về sau.
- L13-17–29: lợi tức → cờ terminal → V/Q → Monte Carlo/sai phân thời gian → Bellman chính sách → Bellman tối ưu → ví dụ → Q-learning.
- L13-30–41: thăm dò → cập nhật bảng → nhu cầu mạng → sơ đồ DQN → kích thước tensor → hàng số → đích/mất mát → hai pha giả mã → kiểm tra.
- X01–X04 và L13-39–41: phụ lục không mang dữ kiện bắt buộc trở lại lõi; L13-41 và X01–X04 cùng một outer stack, đi xuống từ L13-41 vào X01 rồi xuống X04.

## Tài sản

Năm SVG được tham chiếu trong HTML: `corridor.svg`, `bc-shift.svg`, `mdp-loop.svg`, `bellman-backup.svg`, `dqn-pipeline.svg`; trong đó ba SVG khác bản đầu và đã sửa trong quy trình này: `corridor.svg` (thêm nút đích nhánh lệch), `mdp-loop.svg` (thêm nhãn $S_t$) và `bellman-backup.svg` (đổi thuật ngữ, làm hình trung tính, bỏ 0.9/đáp án khỏi hình). `bc-shift.svg` và `dqn-pipeline.svg` không sửa lần này. Không có raster hoặc tài nguyên mạng.

## Tự rà toán và triển khai

- Hành lang: $G_2=1,G_1=.9,G_0=.81$ với $\gamma=.9$.
- Đích: $0+.9\times1=.9$; cập nhật bảng $.4+.2(.9-.4)=.5$.
- Hàng DQN: dự đoán $.4$, đích $.9$, sai số bình phương $(.4-.9)^2=.25$; đóng góp vào mất mát trung bình là $.25/B$.

## Quyết định của lượt chỉnh sửa riêng

| Sửa | Quyết định |
|---|---|
| L13-06 | Dùng đúng 2 hành động xuyên ví dụ hành lang: phân phối $[.05,.95]$ theo thứ tự (trái, phải); đáp án nêu thành phần thứ hai |
| L13-16, L13-36 | Giữ nguyên 2 hành động; không đổi |
| X04 | Ghi rõ trong notes và planning: bài kiểm tra tổng quát hợp đồng tensor, $D_a=4$ tùy ý, không phải ví dụ hành lang |
| L13-20 | Bỏ Q/đích Bellman trước định nghĩa; hỏi–đáp ý nghĩa kết thúc thật: phần lợi tức còn lại/giá trị tương lai bằng 0; nguồn giữ GT 12.24/Illinois Algorithm 1 |
| L13-26 | Sửa alt hình; SVG bellman-backup làm trung tính (chỉ mô tả chuyển tiếp và dữ kiện, bỏ 0.9/max Q=1); đáp án chỉ nằm trong fragment |
| L13-39–40 | Giảm tải mặt slide: giữ 10 bước cốt lõi; chuyển warmup/reset chi tiết/mode/no-grad/zero-grad/$n_{update}$ vào notes; giữ số trang, ID, thứ tự và tổng 100 phút |
| L13-17 | Slide nêu $\gamma\in[0,1]$; $\gamma=1$ chỉ khi lợi tức hữu hạn; notes giải thích chân trời vô hạn thường $\gamma<1$ |
| L13-41 | Thêm một câu thu hồi luận đề mở đầu về trạng thái do chính sách tạo ra |
| X03 | Hai vế độ phủ dùng cùng trạng thái $s_2$ |
| L13-38 | Đổi “hạng tử trong tổng” thành “sai số bình phương” để không lẫn với trung bình |
| Timing mạch 3 | Sửa thành 3 trang×3 + 5 trang×2 = 19 phút |
| DQN 5 trường | Chuẩn hóa hàng $(S,A,R,S',D^{term})$ trong storyboard/outline/note-for-author |
| Điều hướng | Ghi đúng 7 outer section, counts [8,5,8,7,4,9,5], biên đi phải, thứ tự DOM 25→27→26 và 32→34→33 |
| Bảng chu trình | Mạch 1 chỉ 00–07; mạch 2 08–12; mạch 4 vai trò L13-21 là hình thức; mạch 5 không nhận L13-26 (chỉ là cầu vào) |
| Timing mạch 5 | Đề xuất điều chỉnh không áp dụng vì tổng 100 phút và nhịp đã khóa; lưu ý linh hoạt trong note-for-author |
- Batch: $Q_{all}:B\times D_a$; chỉ số lấy hành động $B\times1$; $q_{sa},Y:B$; loss vô hướng.
- Gradient chỉ qua $Q_\theta(S,A)$; $\bar\theta$ đóng băng, không thuộc optimizer; đồng bộ cứng mỗi C bước.
- Môi trường reset khi lượt kết thúc thật; chỉ $D^{term}$ triệt giá trị tương lai trong target.

## Tự biên tập

- `no-ai-slop`: bỏ khẩu hiệu, câu hỏi tu từ và cụm dẫn rỗng; giữ câu ngắn, động từ tính/nhận diện/chọn/truy vết; không thêm claim.
- `quill`: rà liên tục ký hiệu $M/B$, $R_{t+1}$, $S_T$, cờ terminal, $\theta/\bar\theta$ và câu nối giữa bảy mạch; không tạo `quill.json`.

## Trạng thái

Vòng chỉnh sửa riêng đã hoàn tất trong phạm vi B13. Cần kiểm định cuối bằng trình duyệt/Codex Slides trước bàn giao chính thức; lượt này chỉ chạy kiểm tra tĩnh và KaTeX nếu công cụ cục bộ cho phép.

## Hậu kiểm điều phối viên

- Đưa Bellman tối ưu L13-27 trước ví dụ cực đại L13-26; rà lại L13-24–29.
- Đưa sơ đồ DQN L13-34 trước kích thước tensor L13-33; rà lại L13-32–36.
- Sửa điều hướng sau đổi thứ tự: stack thứ tư kết thúc ở L13-26; chỉ đi phải sang L13-28 sau trang này.
- Tách rõ $P(s'\mid s,a)$, hàm thưởng xác định và xác suất điều kiện $\Pr$.
- Sửa $.25$ thành hạng tử bình phương; mất mát trung bình nhận đóng góp $.25/B$.
- Bổ sung bộ tối ưu, cập nhật trạng thái, bộ đếm bước cập nhật và hợp đồng Gaussian theo lô.
- KaTeX strict dựng 162 biểu thức, không lỗi; 46 ID và 46 ghi chú, không trùng hoặc thiếu.
- Dựng montage của các SVG; thay glyph chỉ số dưới Unicode bằng `s0`, `A(t)`, `S(t+1)` để nhãn không mất trong renderer.
- `python3 -m reloadserver 8765` không khả dụng; máy chủ HTTP đang có trên cổng 8765 trả 200 cho HTML, SVG, CSS, RevealJS và KaTeX.
- Không có trình duyệt/Codex Slides trong môi trường; không tuyên bố đã duyệt từng viewport.

## Kiểm kê nguồn không dùng

- `lec01_intro.pdf` PDF 45–46: đã kiểm kê nội dung; không đưa vào bài vì chỉ có liên hệ benchmark, ngoài phạm vi đã khóa.
