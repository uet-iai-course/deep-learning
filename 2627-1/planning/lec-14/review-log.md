# Nhật ký rà soát Bài 14

## Quyết định sửa sau phản biện

| Vấn đề | Quyết định và bằng chứng |
|---|---|
| Ba phương pháp dùng ví dụ khác nhau | Khóa episode G tại L14-08 và dùng trực tiếp ở L14-11–15, L14-19–25, L14-28–41. G là cùng bài toán 2-way 2-shot, không phải ba ví dụ tương tự. |
| Ví dụ I lấn vai trò so sánh | Chuyển I xuống X03, ghi rõ chỉ là vi-trace exact/FO/HVP. Mọi bảng và kiểm tra cuối dùng G. |
| Công thức trước hợp đồng | Đưa tình huống nguồn 5-way 1-shot lên L14-02; support/query, N/K/R/B, shape và split xuất hiện trước objective L14-09. |
| MAML quá tải Hessian | Lõi dạy $\theta\to\phi(\theta)\to L_Q$ và exact/FO ở mức khái niệm. Số học Hessian/HVP chuyển X03; HVP bị loại khỏi tiên quyết. |
| Thứ tự MAML | Khóa L14-27 trực giác → L14-28–31 G → L14-32 objective → L14-33–34 thuật toán/graph → L14-35–36 meta-gradient → L14-37 meta-test. |
| Shape và ký hiệu | Dùng R cho số query mỗi lớp, giữ $Q_i$ là tập. Ghi đủ $X^S,X^Q,Y^S,Y^Q$, nhãn cục bộ, flatten và broadcasting; log-softmax theo trục lớp. |
| Siamese bị hiểu như classifier N-way | Đưa cặp G trước BCE; khóa $z=1$ cùng lớp, mean trên $B_p$; nêu pair accuracy không suy ra N-way nếu thiếu aggregation. |
| MAML thiếu giả mã triển khai | L14-33 ghi zero-grad, phi riêng từng task, support/query means, task mean, backward và optimizer step; cấm sửa theta tại chỗ. |
| Hậu kiểm toán sau sửa | Ghi $S_i\cap Q_i=\varnothing$ và kỳ vọng qua episode; L14-33 đặt $\phi_i^0=\theta$ trước cập nhật; bảng L14-39 không còn gọi bộ xác minh Siamese là đầu ra $A_\theta(S)$. |
| FO diễn đạt sai | Viết Jacobian $\partial\phi/\partial\theta\approx I$, tương đương bỏ hạng Hessian; không viết “bỏ Jacobian”. |
| Split bị tuyệt đối hóa | L14-07 ghi tách theo lớp/miền/task instance tùy giao thức; vẫn giữ train/validation/test task split. |
| Phụ lục sai phạm vi | Khóa X01 prompting distinction, X02 variable-K, X03 I/exact/FO/HVP, X04 land-cover PDF26–31. |
| Bài tập lệch nguồn | Trả bài tập về hợp đồng episode, ProtoNet và inner update + outer objective MAML; exact/FO chỉ ở phụ lục, không bắt buộc bài tập. |

## Sai khác có chủ ý và phần bỏ

- Episode G, bộ phân loại logistic trên G và vi-trace I là ví dụ số tự dựng để kiểm tra công thức; không được trình bày như benchmark hoặc dẫn chứng thực nghiệm.
- Thay ký hiệu số truy vấn mỗi lớp từ Q thành R để không xung đột với tập $Q_i$; đây là sửa ký hiệu, không đổi thuật toán nguồn.
- Tách chi tiết exact/FO/HVP từ CS330 optimization PDF19–24 xuống X03 để bảo toàn tải nhận thức lõi.
- Land-cover từ PDF26–31 chỉ giữ cách đóng khung task/support/query; bỏ mọi kết quả so sánh và claim hiệu năng.
- CS330 metric PDF35–37: bỏ claim rộng về sức biểu đạt, nhất quán và bất định; L14-40 chỉ nói lựa chọn phụ thuộc cấu trúc tác vụ và ngân sách.
- Berkeley PDF18–23: bỏ mở rộng meta-RL vì ngoài LLO và thời lượng.
- Homework PDF3–9: bỏ code, cấu hình chạy và benchmark; giữ công thức, shape, variable-K và cấu trúc bài tập.
- Giáo trình PDF288–293 chỉ dùng X01 để phân biệt prompting; không đổi mạch chính từ slide nguồn.

## Phép tính đã kiểm

- ProtoNet G: $c_A=1,c_B=5$; query A có khoảng cách $(2.25,6.25)$ và $p_A=.98201379$; query B có khoảng cách $(12.25,.25)$ và $p_B=.99999386$; NLL trung bình $\approx.009078$.
- MAML G: tại $\theta=(w,b)=(0,0)$, BCE trung bình bốn hỗ trợ cho gradient $(-1,0)$; $\alpha=1$ cho $\phi=(1,0)$. Query A đúng với $P(A)=\sigma(.5)=.622459$; query B đúng với $P(B)=\sigma(1.5)=.817574$; NLL trung bình $\approx.3377$.
- I ở X03: với mất mát nửa bình phương, gradient support -2, Hessian 1, $\alpha=.5$, $\phi=1$, gradient query theo phi -4; exact -2, FO -4.

## Tài sản và khả năng đọc

- `episode-contract.svg`, `siamese.svg`, `protonet.svg`, `maml-loop.svg` được vẽ lại, có `title`, `desc`, nhãn tiếng Việt từ 30 px; riêng sơ đồ MAML dùng 34 px để giữ khả năng đọc khi chiếu. Không dùng Unicode subscript glyph.
- Không dùng raster, ảnh sinh hoặc tài nguyên mạng. Công thức và bảng vẫn là HTML/KaTeX.

## Rà thứ tự và lân cận

- Sau khi đổi thứ tự, đã rà ±2 tại L14-02–10, L14-11–16, L14-24–36, L14-37–41 và X01–X04.
- Biên stack thực tế giữ câu nối: L14-15→16, L14-26→27, L14-41→X01. Tuyến lõi dừng được ở L14-41.
- Timing giữ 42 trang lõi = 100 phút, 4 trang phụ lục = 20 phút, bài tập = 50 phút riêng.

## Biên tập

- `no-ai-slop`: bỏ khẩu hiệu, câu hỏi tu từ và claim quảng bá; giữ động từ tính, chọn, so sánh, truy vết. Mặt trang và notes dùng tiếng Việt làm ngôn ngữ chính.
- `quill`: rà trật tự tình huống→hợp đồng→G→ba phương pháp→so sánh; ký hiệu G, N/K/R/B, $S_i/Q_i$, $\theta/\phi$ không đứt. Không tạo `quill.json`.
- Các chỉ dẫn tuyến cắt, đáp án và trạng thái kiểm chứng chỉ nằm trong planning, không đưa lên mặt trang hoặc notes.

## Trạng thái

Đã xử lý toàn bộ lỗi chặn, nghiêm trọng và trung bình hợp lệ trong phạm vi sửa B14. Hậu kiểm toán học cuối đạt PASS sau ba vá về hợp đồng $S_i/Q_i$, thứ tự giả mã MAML và vai trò tập tham chiếu Siamese.

## Kiểm định cuối

- 46 `data-slide-id` duy nhất, 46 khối ghi chú; 42 trang lõi và 4 trang mở rộng khớp storyboard.
- KaTeX strict dựng thành công 114/114 biểu thức với `throwOnError: true`.
- Trình phân tích HTML không còn thẻ chưa đóng; 13 tài nguyên cục bộ đều tồn tại. Bốn SVG phân tích XML thành công, có `title` và `desc`.
- Không có ảnh raster, tài nguyên cốt lõi qua mạng hoặc byte điều khiển lạ. Danh sách tiêu đề `h1`, `h2`, `h3` đã được rà thủ công; tiếng Anh còn lại chỉ là tên phương pháp, viết tắt hoặc phép toán chuẩn.
- Đã tăng nhãn sơ đồ MAML lên 34 px sau rà trực quan ảnh tổng hợp; không phát hiện nhãn tràn khung SVG.
- `python3 -m reloadserver 8765` không chạy được vì môi trường thiếu mô-đun `reloadserver`. Máy chủ HTTP cục bộ hiện có tại cổng 8765 trả HTTP 200 cho 9/9 mục: HTML bài giảng, trang chỉ mục, CSS, RevealJS, KaTeX và bốn SVG.
- Môi trường không có trình duyệt đồ họa hoặc Codex Slides. Vì vậy chưa thể tuyên bố đã duyệt từng trang ở khung 16:9 và màn hình hẹp; đây là giới hạn còn lại của kiểm định trực quan.
