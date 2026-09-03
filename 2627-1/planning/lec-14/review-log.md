# Nhật ký rà soát Bài 14

## Phạm vi DeepSeek bắt buộc cho các đợt sau

- DeepSeek chỉ nhận một thư mục staging mới dưới `/tmp` cho từng tác vụ; không được cấp quyền ghi vào kho dự án.
- Mỗi tác vụ chỉ được tạo đúng một tệp mảnh. Luôn đặt `MCP_WRITE_POLICY=create-once` và `MCP_MAX_WRITE_CHARS=2500`; không tăng trần theo một lần chạy thành công.
- Tệp đích phải chưa tồn tại. Lần ghi vượt 2.500 ký tự bị từ chối nguyên khối trước khi tạo tệp; staging đã lỗi không được dùng lại.
- Chỉ giao một hoặc hai mục đã khóa, kèm danh sách tệp đầu vào tối thiểu. Không giao toàn bộ ghi chú hoặc deck trong một lượt và không cho phép sửa nối tiếp trên mảnh đã tạo.
- Chỉ nhận kết quả có metadata runtime `requested_model=observed_model=deepseek/deepseek-v4-flash-0731`, `provider=OpenRouter`. Lượt sai model, thiếu metadata, dở dang hoặc vượt giới hạn bị loại toàn bộ.
- Trước khi hợp nhất, Codex kiểm UTF-8, ký tự thay thế, ký tự Cyrillic lẫn vào tiếng Việt, KaTeX, đường dẫn, phạm vi nguồn và dấu vết chỉ dẫn cho người viết hoặc diễn giả. Chỉ Codex dùng `apply_patch` để đưa phần đã duyệt vào kho.
- Không đọc hoặc gửi `.env`, biến môi trường hay bí mật. Worker chỉ nhận hồ sơ nguồn UTF-8 đã lọc; PDF và DOCX được trích xuất cục bộ trước khi giao.

## Hồ sơ đa tác tử cho bản ghi chú

- Hồ sơ nguồn đã lọc nằm tại `/tmp/deep-learning-lec14-dossier.v8FBcu`; chỉ gồm văn bản UTF-8 và tệp dự án cần thiết, không có `.env`, PDF, DOCX hoặc bí mật.
- Vai lập kế hoạch, ánh xạ nguồn và kiểm toán toán học dùng `z-ai/glm-5.3-flash`; các kết quả được nhận đều có `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- DeepSeek chạy trong các staging mới `/tmp/lec14-writer-01` đến `/tmp/lec14-writer-09b` với chính sách trên. Các mảnh 01–06, 08 và 09b hợp lệ. Mảnh 07, 07b và 09 bị loại vì vượt trần hoặc hết giới hạn gọi công cụ; không có tệp một phần được dùng.
- Mảnh 01 bịa một số định danh; mảnh 02 tuyệt đối hóa tính độc lập của tác vụ; mảnh 03 dùng cụm từ sai nghĩa; mảnh 08 khái quát sai về cập nhật tham số; mảnh 09b pha tiếng Anh quá mức. Các câu này bị loại hoặc viết lại từ đặc tả và nguồn, không được hợp nhất nguyên văn.

## Hợp nhất năm báo cáo độc lập cho ghi chú

Năm vai góc nhìn sinh viên, chuyên gia Học sâu, toán học–triển khai, phản biện giảng dạy và kết nối–mạch viết chạy song song bằng `z-ai/glm-5.3-flash`. Mọi báo cáo được dùng đều có `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.

| Mức độ | Mục | Vấn đề và bằng chứng | Quyết định |
|---|---|---|---|
| trung bình | sau Ví dụ G | Ghi chú thiếu mục tiêu chung đo chất lượng sau thích nghi, trong khi outline và deck dùng nó làm điểm vào cho ba họ phương pháp. | Thêm mục tiêu kỳ vọng và nói rõ Siamese chỉ cho điểm cặp nếu chưa có quy tắc tổng hợp. |
| trung bình | Phần mở rộng | Storyboard có vi-trace I cho exact/FO/HVP nhưng ghi chú chưa có. | Thêm ví dụ I với exact $-2$, FO $-4$ và giới hạn về tích Hessian–vector. |
| trung bình | Bài tập 50 phút | Hai bài tính lặp nguyên ví dụ G đã giải. | Đổi truy vấn của bài ProtoNet và đổi $\alpha$ của bài MAML; giữ đúng phân bổ 10+15+15+10 phút. |
| nhẹ | ProtoNet | $Y^Q$ khai báo $[B,N,R]$ nhưng công thức lấy nhãn theo chỉ số phẳng $q$. | Nêu phép làm phẳng nhãn thành $[B,NR]$ theo cùng thứ tự với truy vấn. |
| nhẹ | tiên quyết và thuật ngữ | Thiếu sigmoid/BCE, shape/broadcast và ánh xạ thuật ngữ `episode`, `$N$-way $K$-shot`. | Bổ sung tại lần xuất hiện đầu; tiếng Việt vẫn là ngôn ngữ chính. |
| nhẹ | FO-MAML | Câu “không bỏ toàn bộ Jacobian” chưa chỉ rõ phần được xấp xỉ. | Viết $\partial\phi/\partial\theta=I-\alpha H$, FO thay bằng $I$ nhưng vẫn giữ gradient truy vấn. |
| nhẹ | mạch và ký hiệu | Thiếu câu nối vào bảng so sánh; $D_x\to D$ chưa được giải thích. | Thêm câu nối và định nghĩa $D$ là kích thước biểu diễn nhúng. |

- Phát hiện “thiếu bốn SVG” bị loại: cả bốn tệp tồn tại, phân tích XML được và Chromium tải thành công; worker chỉ không liệt kê được chúng qua mẫu đường dẫn đã dùng.
- Đề xuất đưa phân bổ phút theo cụm vào ghi chú bị loại: đây là hướng dẫn vận hành, đã nằm trong storyboard và `note-for-author.md`, không thuộc nội dung công khai.

## Kiểm định ghi chú sau chỉnh sửa

- `no-ai-slop`: đã rà trực tiếp theo `eval.md`; không còn câu quảng bá, diễn giải tự tán dương, dấu vết worker hay chỉ dẫn cho người viết/diễn giả. Nội dung giữ câu ngắn, số liệu cụ thể và thuật ngữ nhất quán.
- `quill`: rà xương sống tình huống ít mẫu → phân phối tác vụ → hợp đồng hỗ trợ/truy vấn → ví dụ G → Siamese → ProtoNet → MAML → so sánh → mở rộng; các ký hiệu G, $N/K/R/B$, $S_i/Q_i$ và $\theta/\phi$ được truyền liên tục. Không tạo `quill.json`.
- Kiểm tra tĩnh: tệp UTF-8, 4 khối câu hỏi và 4 lời giải, 4 SVG hợp lệ, không có ký tự thay thế hoặc Cyrillic lẫn vào tiếng Việt. Hai lỗi `$mathcal T$` trong bản đầu đã sửa thành `$\mathcal T$`.
- Trình xem cục bộ tại cổng 8766 dựng 153 cụm KaTeX, không có `.katex-error`; cả bốn SVG tải đủ, có văn bản thay thế. Chromium chụp toàn trang và xuất PDF 10 trang, không ghi nhận lỗi console, lỗi trang hoặc yêu cầu thất bại.
- `python3 -m reloadserver 8765` không khả dụng vì thiếu mô-đun; kiểm định dùng máy chủ tĩnh cục bộ trên cổng 8766. Codex Slides không có bề mặt gọi được trong phiên này, nên không tuyên bố đã dùng plugin.
- Lượt tái kiểm đầu vượt giới hạn gọi công cụ nên không có báo cáo và bị loại. Lượt thu hẹp sau đó gán sai logit ban đầu thành $h-3$ thay vì $w(h-3)+b=0$ tại $w=b=0$, rồi kết luận nhầm gradient bằng 0. Lượt tái kiểm tranh chấp đã đặt đúng logit bằng 0 nhưng lại dùng $p-y=+0{,}5$ cho hai mẫu có $y=1$ thay vì $-0{,}5$. Cả hai kết luận bị loại. Bốn vai trước và phép tính xác định cục bộ đều cho $\nabla_w\mathcal L_S=(-1{,}5-0{,}5-0{,}5-1{,}5)/4=-1$, $\nabla_b\mathcal L_S=0$.

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

## Ranh giới stack và lý do đổi từ 4 sang 6

- HTML chia sáu stack outer với counts [11,5,10,6,7,7]: L14-00–10, L14-11–15, L14-16–25, L14-26–31, L14-32–38, L14-39–41 + X01–X04.
- Lý do đổi từ 4 sang 6: hai stack cũ (L14-16–26, L14-27–41) cắt ngang biên cụm ProtoNet/MAML; tách theo biên cụm thực tế (25/26, 31/32, 38/39) cho mỗi stack một mạch khái niệm và điều hướng ngắn hơn.
- Biên stack giữ câu nối: L14-10→11, L14-15→16, L14-25→26, L14-31→32, L14-38→39, L14-41→X01.

## Rà thứ tự và lân cận

- Sau khi tách stack, đã rà hai trang mỗi phía tại các biên L14-10, L14-15, L14-25, L14-31, L14-38 và X01; câu nối và ký hiệu G không bị đứt.
- Timing giữ 42 trang lõi = 100 phút, 4 trang phụ lục = 20 phút, bài tập = 50 phút riêng.

## Hợp nhất năm báo cáo độc lập

| Vai rà soát | Mức độ | Trang | Vấn đề | Bằng chứng | Đề xuất | Quyết định |
|---|---|---|---|---|---|---|
| Góc nhìn sinh viên | trung bình | L14-03, L14-16, L14-38 | Phân biệt học chuyển giao/siêu học tập còn nằm trong notes; động cơ chuyển từ cặp sang prototype chưa hiện; cụm MAML thiếu câu kiểm tra đóng. | Mặt trang L14-03 chỉ nói “nhiều tác vụ”; L14-16 vào định nghĩa ngay; L14-38 chỉ có bảng rò rỉ. | Đưa tiêu chí objective sau thích nghi lên mặt trang; thêm một câu động cơ; thêm câu hỏi và fragment về rò rỉ trong tác vụ. | Đã áp dụng bằng câu ngắn, không thêm trang hoặc claim định lượng. |
| Chuyên gia Học sâu | trung bình | L14-09, L14-12–13 | Objective chung dễ ép Siamese vào $A_\theta$; quan hệ chia sẻ $f_\theta$ và $p_b=\sigma(s_b)$ chưa hiện đủ. | Siamese chỉ cho điểm cặp nếu thiếu luật tổng hợp N-way; slide BCE nhảy thẳng tới $p_b$. | Giới hạn phạm vi objective, thêm caption chia sẻ bộ mã hóa và nối logits với xác suất. | Đã áp dụng; giữ Siamese là bộ xác minh cặp và không tự dựng luật tổng hợp. |
| Toán học, thuật toán và triển khai | không có lỗi | L14-19–23, L14-28–31, L14-X03 | Các phép ProtoNet G, MAML G và exact/FO I cần được tính độc lập. | Hậu kiểm thu được $\mathcal L_G=0.00907804$, $\nabla L_S=(-1,0)$, $\mathcal L_Q=0.337745$, exact $=-2$, FO $=-4$; shape và broadcasting đúng. | Giữ số liệu; nối lưu ý ổn định số với $p_b=\sigma(s_b)$. | PASS; chỉ bổ sung định nghĩa logits ở L14-13, không đổi kết quả số. |
| Phản biện học thuật và giảng dạy | trung bình | L14-26–37, L14-39–41 | G bị mô tả như giữ xuyên cả phần tổng quát hóa; chức năng kiểm tra MAML và kiểm tra tổng hợp chưa tách rõ. | L14-32–36 đã chuyển từ số G sang objective/thuật toán tổng quát; L14-41 so cả ba họ. | Tách tuyến G 26–31, tổng quát hóa 32–36, meta-test 37; giao L38 đóng MAML và L41 tổng hợp. | Đã đồng bộ note-for-author và storyboard; không đổi thứ tự trang. |
| Kết nối và mạch viết | nghiêm trọng | L14-41→X01, L14-39 | Chỉ dẫn đi phải mâu thuẫn DOM vì X01 nằm ngay dưới L14-41 trong cùng outer section; phần so sánh thiếu trang nêu vấn đề. | Outer cuối chứa L14-39–41 và X01–X04; đi phải sẽ rời stack thay vì tới X01. | Sửa mọi chỉ dẫn thành đi xuống; giao L14-39 nêu vấn đề so sánh, L14-41 kiểm tra tổng hợp. | Đã sửa lỗi điều hướng nghiêm trọng trong storyboard và note-for-author; outer structure giữ nguyên. |

## Đề xuất không áp dụng

- Không thêm slide bài tập: tiết bài tập đã được tách riêng trong planning; deck giữ 46 trang và timing 100+20 phút.
- Không sửa `viewport`: cấu hình theo template dùng chung và nằm ngoài phạm vi chỉnh sửa Bài 14.
- Không thêm episode accuracy hoặc khoảng tin cậy: các nguồn đã khóa không cung cấp giao thức hay số liệu tương ứng.

## Hậu kiểm sau chỉnh sửa

- Tác tử toán học đọc trực tiếp HTML và tính lại độc lập: ProtoNet G có $c_A=1$, $c_B=5$, xác suất đúng $0.98201379$ và $0.99999386$, NLL $0.00907804$; MAML G có gradient $(-1,0)$, $\phi=(1,0)$, NLL $0.337745$; ví dụ I cho exact $=-2$, FO $=-4$. Kết quả PASS.
- Một lượt GLM trên bản trích tối thiểu đã tính sai trung bình $(0,2)$ thành $0.2$ và dùng sai $\sigma(-0.5)$; báo cáo đó bị loại vì mâu thuẫn trực tiếp với dữ kiện. Phép tính cục bộ và tác tử đọc trực tiếp HTML đều xác nhận các số trên.
- Tác tử kết nối đọc trực tiếp HTML và planning xác nhận 46 ID, 46 notes, sáu stack `[11,5,10,6,7,7]`; mọi biên phần đạt. L14-41 và X01 cùng stack nên đi xuống; lỗi điều hướng nghiêm trọng đã được xử lý.

## Biên tập

- `no-ai-slop`: bỏ khẩu hiệu, câu hỏi tu từ và claim quảng bá; giữ động từ tính, chọn, so sánh, truy vết. Mặt trang và notes dùng tiếng Việt làm ngôn ngữ chính.
- `quill`: rà trật tự tình huống→hợp đồng→G→ba phương pháp→so sánh; ký hiệu G, N/K/R/B, $S_i/Q_i$, $\theta/\phi$ không đứt. Không tạo `quill.json`.
- Các chỉ dẫn tuyến cắt, đáp án và trạng thái kiểm chứng chỉ nằm trong planning, không đưa lên mặt trang hoặc notes.

## Trạng thái

Đã xử lý các lỗi nghiêm trọng và trung bình hợp lệ từ năm vai phản biện. Lỗi nghiêm trọng về điều hướng L14-41→X01 đã được sửa thành đi xuống trong cùng stack. Hai hậu kiểm sau chỉnh sửa đều đạt.

## Kiểm định cuối

- 46 `data-slide-id` duy nhất, 46 khối ghi chú; 42 trang lõi và 4 trang mở rộng khớp storyboard.
- Cấu trúc stack sau tách: sáu stack outer với counts [11,5,10,6,7,7]; độ sâu lồng 0 (mỗi slide là section con trực tiếp của một stack).
- Chromium dựng 119 biểu thức KaTeX, không có `.katex-error`; cấu hình giữ `throwOnError: true` và `strict: "error"`.
- Trình phân tích HTML không còn thẻ chưa đóng; 13 tài nguyên cục bộ đều tồn tại. Bốn SVG phân tích XML thành công, có `title` và `desc`.
- Không có ảnh raster, tài nguyên cốt lõi qua mạng hoặc byte điều khiển lạ. Danh sách tiêu đề `h1`, `h2`, `h3` đã được rà thủ công; tiếng Anh còn lại chỉ là tên phương pháp, viết tắt hoặc phép toán chuẩn.
- `python3 -m reloadserver 8765` không chạy được vì môi trường thiếu mô-đun `reloadserver`; máy chủ HTTP cục bộ tại cổng 8765 trả HTTP 200 cho 18/18 mục cốt lõi được kiểm: deck, index, CSS, RevealJS, bốn plugin, ba tài nguyên KaTeX và bốn SVG.
- Chromium headless đã duyệt đủ 46 trang ở 1280×720 và 900×720 với mọi fragment hiện: không tràn, không chữ dưới 18 px, không lỗi trang, không phản hồi tài nguyên hỏng. Phím xuống từ trang đầu đến `(h=0,v=1)` và phím phải đến `(h=1,v=0)`.
- Đã xem trực quan các trang L14-03, 09, 12, 13, 16, 33, 38, 39, 40 và X03; xem lại L14-33, 38, 39, 40 ở màn hình hẹp. Bố cục, bảng, công thức và fragment đọc được.
- Console có một 404 favicon ở lượt mở đầu; favicon không phải tài nguyên cốt lõi và không ảnh hưởng deck. Codex Slides không có bề mặt khả dụng trong phiên này, nên kiểm định trực quan dùng Chromium cục bộ.
