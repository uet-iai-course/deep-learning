# Nhật ký rà soát Bài 13

## Phạm vi worker OpenRouter cho ghi chú bài giảng — 2026-09-03

- Hồ sơ nguồn lọc: `/tmp/deep-learning-lec13-dossier.RzO1O6`; mọi PDF được trích xuất cục bộ thành văn bản UTF-8 đúng dải. Không gửi PDF, `.env`, khóa hoặc bí mật cho worker.
- Planner, tác tử ánh xạ nguồn và tác tử kiểm toán dùng `z-ai/glm-5.3-flash`; metadata runtime của các báo cáo được chấp nhận xác nhận `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Tác tử ánh xạ gọi `search_text` hai lần với đường dẫn tệp thay vì thư mục; server từ chối và worker tự sửa bằng `path=source`. Không có mở rộng quyền hay dữ liệu ngoài hồ sơ lọc.
- Mười tác vụ DeepSeek dùng staging riêng `/tmp/lec13-writer-01` đến `/tmp/lec13-writer-10`, `MCP_WRITE_POLICY=create-once`, `MCP_MAX_WRITE_CHARS=2500`; metadata xác nhận đúng `deepseek/deepseek-v4-flash-0731` qua OpenRouter. Writer không có quyền ghi vào kho.
- Nội dung được biên tập trước khi hợp nhất. Đã loại phép tính kỳ vọng sai $0{,}65$ do worker dùng nhầm cặp $0{,}5/0{,}8$ thay cho ví dụ đã khóa $0{,}2/0{,}8$; bỏ tuyên bố RL có thể vượt chuyên gia; làm yếu các khẳng định quá mức rằng DAgger “cắt” lỗi hoặc replay tạo dữ liệu i.i.d.; không khóa Adam vì nguồn chỉ yêu cầu bộ tối ưu.
- Giới hạn bền vững: không tăng ngưỡng 2.500 ký tự; khi vượt phải dùng staging mới và nhiệm vụ hẹp hơn. DeepSeek chỉ tạo mảnh đề xuất, không sửa trực tiếp HTML/Markdown/SVG của dự án. Mọi số, chỉ số thời gian, terminal mask, gradient và phạm vi nguồn phải được kiểm lại cục bộ.

## Năm phản biện độc lập cho ghi chú bài giảng — 2026-09-03

- Năm vai góc nhìn sinh viên, chuyên gia Học sâu, chính xác toán–triển khai, phản biện giảng dạy và kết nối mạch viết đều chạy bằng `z-ai/glm-5.3-flash` qua OpenRouter. Mọi báo cáo được chấp nhận có `requested_model=observed_model=z-ai/glm-5.3-flash` và `provider=OpenRouter`.
- Lượt chuyên gia đầu tiên vượt giới hạn tám lượt gọi công cụ và bị loại toàn bộ. Lượt thay thế dùng đúng năm tệp đã chỉ định, cấm tìm kiếm thêm và hoàn tất sau hai vòng; không tăng quyền hoặc mở rộng hồ sơ.
- Không báo cáo nào phát hiện lỗi `chặn bàn giao` hay `nghiêm trọng`. Kiểm toán độc lập xác nhận $G=(0{,}81;0{,}9;1)$, $V^\pi=0{,}5$, cực đại $0{,}8$, đích $0{,}9$, cập nhật $0{,}4\to0{,}5$, sai số $0{,}25$, cờ kết thúc, học ngoài chính sách, kích thước tensor và hướng gradient.
- Đã đồng bộ ví dụ BC của ghi chú với deck thành $(0{,}05;0{,}95)$; đổi quỹ đạo thành dạng đầy đủ có phần thưởng và nói rõ BC chỉ chiếu xuống cặp trạng thái–hành động; Việt hóa các từ `loss`, `pipeline`, `tuple`; bỏ dòng giới hạn biên soạn khỏi bề mặt ghi chú công khai.
- Đã sửa bảng chu trình: L13-06 chỉ là bước kiểm tra; mạch giá trị bắt đầu vấn đề ở L13-21, dùng L13-24 làm cầu mục tiêu một bước và ghi `không áp dụng` cho triển khai vì phần đó bắt đầu ở Q-learning.
- Các góp ý chỉ liên quan deck — cỡ chữ hiệu dụng, định nghĩa lợi tức trước L13-13, nhịp mạch 5/6, điều kiện $\gamma=1$, đáp án L13-41, ký hiệu $Q^+$, API `gather`, Huber và dòng tương tác trong bảng — được chuyển sang pha cập nhật deck, không sửa lẫn vào commit ghi chú.
- Không thêm dòng số của hành lang vào kết luận ghi chú: bảng tổng hợp đã thu hồi đúng BC→DAgger→Q-learning→DQN; dữ kiện số vẫn được nối đầy đủ ở các cụm 4–6. Không đưa chỉ dẫn giảng viên vào ghi chú công khai; điều phối thời lượng vẫn ở `note-for-author.md`.

### Tái kiểm và dựng bản ghi chú

- Tác tử GLM tái kiểm đúng hai tệp đã sửa và trả `PASS`; metadata xác nhận đúng model/provider. Quỹ đạo $T$ bước, ví dụ BC, bảng chu trình, chỉ số thời gian, các số Q-learning/DQN và hướng gradient đều nhất quán.
- `material-viewer.html` dựng đúng ghi chú từ liên kết trong `index.html`; Chromium xuất ảnh toàn trang và PDF 12 trang, không có công thức lỗi, tài nguyên thiếu hoặc văn bản quy trình trên bề mặt công khai.
- Kiểm tra `$no-ai-slop`: bỏ tiếng Anh có cách diễn đạt Việt ổn định, câu giới hạn biên soạn và mọi lời hướng dẫn người viết; giữ tên riêng, ký hiệu và viết tắt cần thiết. Kiểm tra theo nguyên tắc `$quill`: chuỗi BC → lệch phân phối → MDP/lợi tức → giá trị/Bellman → Q-learning → DQN → tổng hợp giữ một ví dụ và một hệ ký hiệu xuyên suốt; không tạo `quill.json`.

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

Vòng chỉnh sửa riêng và vòng hoàn tất sau phản biện đã kết thúc trong phạm vi Bài 13. Kiểm định tĩnh, KaTeX và Chromium ở hai khung nhìn đã chạy trên chính bản hiện tại; kết quả được ghi ở mục “Vòng hoàn tất sau kiểm toán toàn khóa”.

## Hậu kiểm điều phối viên

- Đưa Bellman tối ưu L13-27 trước ví dụ cực đại L13-26; rà lại L13-24–29.
- Đưa sơ đồ DQN L13-34 trước kích thước tensor L13-33; rà lại L13-32–36.
- Sửa điều hướng sau đổi thứ tự: stack thứ tư kết thúc ở L13-26; chỉ đi phải sang L13-28 sau trang này.
- Tách rõ $P(s'\mid s,a)$, hàm thưởng xác định và xác suất điều kiện $\Pr$.
- Sửa $.25$ thành hạng tử bình phương; mất mát trung bình nhận đóng góp $.25/B$.
- Bổ sung bộ tối ưu, cập nhật trạng thái, bộ đếm bước cập nhật và hợp đồng Gaussian theo lô.
- KaTeX strict dựng 162 biểu thức, không lỗi; 46 ID và 46 ghi chú, không trùng hoặc thiếu.
- Dựng montage của các SVG; thay glyph chỉ số dưới Unicode bằng `s0`, `A(t)`, `S(t+1)` để nhãn không mất trong renderer.
- `python3 -m reloadserver 8765` không khả dụng; máy chủ HTTP cục bộ trên cổng 8765 trả 200 cho HTML, SVG, CSS, RevealJS và KaTeX.
- Lượt hậu kiểm cũ chưa có trình duyệt. Trạng thái này đã được thay thế bởi kiểm định Chromium ở hai khung nhìn trong vòng hoàn tất bên dưới.

## Kiểm kê nguồn không dùng

- `lec01_intro.pdf` PDF 45–46: đã kiểm kê nội dung; không đưa vào bài vì chỉ có liên hệ benchmark, ngoài phạm vi đã khóa.

## Vòng hoàn tất sau kiểm toán toàn khóa

### Năm báo cáo phản biện độc lập

Năm worker chỉ đọc chạy song song qua OpenRouter. Metadata do cầu nối ghi nhận cho cả năm: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`; hồ sơ `review`, timeout tuyệt đối 300 giây. Không worker nào có công cụ ghi.

| Vai | Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|---|
| Góc nhìn sinh viên | trung bình | L13-13, L13-16 | Nhãn tương tác không thống nhất; câu kiểm tra gộp LLO26 với chính sách | L13-13 dùng “Quyết định”; LLO26 chỉ nêu năm thành phần, còn chính sách là nội dung bài | Dùng nhãn “Câu hỏi”; tách năm thành phần LLO26 khỏi chính sách | Đã sửa HTML và planning |
| Chuyên gia Học sâu | trung bình | L13-19, L13-28, L13-41 | Cận vô hạn thiếu quy ước sau kết thúc; đích bảng chưa nói dùng Q hiện tại; kết luận gọi DQN là nguồn tín hiệu thứ ba | L13-41 đặt BC, Q-learning và DQN trên cùng trục “nguồn tín hiệu” dù DQN chỉ đổi bộ xấp xỉ | Khóa phần thưởng sau kết thúc bằng 0; nêu Q hiện tại; tách hai nguồn tín hiệu khỏi cơ chế DQN | Đã sửa HTML, storyboard và ghi chú người soạn |
| Độ chính xác toán học, thuật toán và triển khai | nhẹ | L13-01, L13-24, L13-30, L13-37 | DQN chưa mở rộng ở lần đầu; mục tiêu TD còn mơ hồ; thăm dò chưa nêu phân phối; số 1 trong đích chưa ghi giả thiết | Các số $.81,.9,.5,.25$ và tensor đều đúng; vấn đề chỉ nằm ở hợp đồng diễn đạt | Mở rộng DQN; gọi hai kiểu mục tiêu hồi quy; chọn đều trên $\mathcal A$; ghi giả sử $\max Q_{\bar\theta}=1$ | Đã sửa; không đổi công thức hoặc số |
| Phản biện học thuật và giảng dạy | trung bình | L13-20, L13-41 | “Giá trị tương lai” xuất hiện trước khi định nghĩa V/Q; kết luận gán việc bổ sung nhãn trên $d_{\pi_\theta}$ cho BC thuần | V/Q chỉ được định nghĩa ở L13-21–22; thuật toán truy vấn chuyên gia trên trạng thái mới là DAgger ở L13-11 | Chỉ nói phần lợi tức còn lại ở L13-20; phân biệt BC thuần, DAgger và RL ở kết luận | Đã sửa HTML và planning |
| Kết nối và mạch viết | trung bình | L13-32→34→33, L13-41 | Mạng đích xuất hiện ở pipeline trước khi được giới thiệu; kết luận trộn trục tín hiệu và cơ chế | L13-34 đứng trước hợp đồng tensor L13-33 theo chủ ý; L13-41 là điểm thu hồi toàn bài | Giữ thứ tự nhưng giới thiệu $Q_\theta,Q_{\bar\theta}$ trong notes; đổi luận điểm kết luận | Đã sửa; giữ 7 mạch và thứ tự DOM |

Không báo cáo nào phát hiện lỗi `chặn bàn giao` hoặc `nghiêm trọng`. Các góp ý trung bình đều đã xử lý. Những góp ý nhẹ hợp lệ về chỉ số hành động từ 0, chu kỳ đồng bộ $C$, shape Gaussian một mẫu/theo lô và quan hệ $V^\pi=\mathbb E_{a\sim\pi}Q^\pi$ cũng đã được áp dụng.

Các đề xuất không áp dụng:

- Không bỏ mã LLO26/27 ở L13-01: đây là kết quả học tập lấy trực tiếp từ đề cương, không phải mã quy trình nội bộ.
- Không đổi thứ tự ID 25→27→26 hoặc 32→34→33: thứ tự DOM đã được phê duyệt vì Bellman tối ưu phải đứng trước ví dụ cực đại, còn pipeline DQN phải đứng trước hợp đồng tensor; đã bổ sung cầu ký hiệu thay vì đảo trang.
- Không thêm tuyên bố hội tụ Q-learning hoặc DQN: nguồn và phạm vi bài không đủ để khóa giả thiết hội tụ.

### Tác tử chỉnh sửa và xử lý lỗi worker

Hai lượt writer GLM trên staging tối thiểu đều dừng ở giới hạn công cụ với lỗi nguyên văn lần lượt `model exceeded the tool-call limit (16)` và `model exceeded the tool-call limit (12)`. Không có thay đổi worker nào được ghi trực tiếp vào kho. Điều phối viên đã đọc diff staging, chỉ hợp nhất các thay đổi có căn cứ bằng bản vá cục bộ và đồng bộ lại HTML, storyboard, outline, note-for-author và nhật ký này.

### Hậu kiểm sau chỉnh sửa

- Cấu trúc tĩnh: 46 trang, 46 `data-slide-id` duy nhất, 46 khối ghi chú; 7 section ngoài với kích thước `[8,5,8,7,4,9,5]`; đúng tuyến lõi 100 phút, phụ lục 20 phút và bài tập 50 phút riêng.
- Tài nguyên: không thiếu đường dẫn cục bộ, không dùng raster hoặc tài nguyên mạng cốt lõi; năm SVG Bài 13 có mô tả tiếp cận.
- Chromium dựng toàn bộ 46 trang ở 1280×720 và 900×720, hiện mọi fragment: không tràn ngang/dọc, không `katex-error`, không lỗi trang và không phản hồi cốt lõi từ 400 trở lên. Một 404 console ở lượt 1280×720 là `favicon.ico`, không thuộc deck.
- Điều hướng bàn phím từ trang đầu: Xuống đến `{h:0,v:1}`; Phải đến `{h:1,v:0}`. Các biên đặc biệt 25→27→26, 32→34→33 và L13-41→X01 giữ đúng như storyboard.
- Đã rà trực quan các trang thay đổi L13-01, 13, 16, 20, 24, 37, 40, 41 và X01 ở cả hai khung; chữ, công thức, bảng, fragment và chân trang đều đọc được.
- Hậu kiểm toán giữ nguyên các giá trị đã tính lại: $G=(.81,.9,1)$, đích $.9$, cập nhật $.4\to.5$, sai số bình phương $.25$, gradient chỉ qua mạng hiện tại và shape DQN theo lô.
- `no-ai-slop`: bỏ nhãn dẫn không nhất quán, câu kết phân loại sai và cụm tiếng Anh không cần thiết; không thêm khẩu hiệu hoặc claim. Quill: rà lại chuỗi BC → DAgger → MDP → lợi tức → V/Q → Bellman → Q-learning → DQN → kết luận; không tạo `quill.json`.
- Bề mặt Codex Slides trong trình duyệt không được cung cấp trong môi trường hiện tại; kiểm định trực quan được thực hiện bằng Chromium cục bộ trên đúng RevealJS hiện hành.

### Ba tái kiểm độc lập sau hợp nhất

Ba worker GLM 5.3 Flash chỉ đọc chạy trên bản đã hợp nhất: kiểm định storyboard (`storyboard`, timeout 180 giây), tái kiểm toán–thuật toán (`recheck`, 180 giây) và tái kiểm kết nối (`recheck`, 180 giây). Cả ba đều trả `PASS`, metadata runtime tiếp tục xác nhận provider OpenRouter và model quan sát đúng `z-ai/glm-5.3-flash`.

- Kiểm định storyboard xác nhận 100+20 phút, bài tập 50 phút, 7 mạch, 46 trang, các ranh giới và dấu vết số. Ba góp ý nhẹ được xử lý: bỏ L13-19 khỏi hàng mạch 4; ghi rõ vai trò gộp L13-28 và L13-29–30; thống nhất diễn đạt không gradient ở L13-37.
- Tái kiểm toán xác nhận toàn bộ số, Bellman, cập nhật Q, cờ kết thúc, tensor, gradient, hai mạng, vòng huấn luyện và vai trò DQN đều đúng; không có phát hiện mới.
- Tái kiểm mạch xác nhận các biên 12→13, 20→21, 26→28, 31→32, 32→34→33, 40→41 và 41→X01; kết luận thu hồi mở bài. Góp ý nhẹ ở L13-41 được áp dụng bằng cách tách “Nguồn: phần thưởng” khỏi “Cơ chế: đích Bellman”. Không đưa $V(S_{t+1})$ lên L13-24 vì trang này chủ ý đối chiếu hai họ mục tiêu trước khi chọn Bellman cho $V$ hay $Q$ ở trang kế tiếp.
- Tái kiểm mạch cuối sau sửa nhẹ trả `PASS`: L13-41 tách đúng nguồn/cơ chế và thu hồi L13-00; L13-36→38 giữ chuỗi $.4\to.9\to.25$; L13-40→41→X01 liền mạch; storyboard không còn gán L13-19 cho mạch 4 và đã khai báo vai trò gộp L13-28/29–30. Không có lỗi chặn hoặc nghiêm trọng.
