# Nhật ký rà soát Bài 10

## Quyết định nguồn và phạm vi

| Quyết định | Bằng chứng và lý do |
|---|---|
| Giữ mạch Bahdanau trong dịch máy | `lec15_attention.pdf` PDF 3–17 đi từ nút thắt seq2seq đến ngữ cảnh theo bước và căn chỉnh; đúng LLO19–LLO20 |
| Dùng PDF 19–27 ở tuyến mở rộng | Dải này mở rộng cùng cơ chế sang vùng ảnh; không cần cho chu trình lõi |
| Chỉ dùng PDF 30–41 làm cầu nối | Bài 11 mới khóa self-attention và Transformer; L10-32 chỉ phân biệt nguồn Q/K/V |
| Dùng GT PDF 239–245 | Khôi phục hợp đồng học theo đáp án, EOS và mặt nạ đích từ bộ mã hóa–giải mã |
| Dùng GT PDF 258–263 | Kiểm chứng công thức chú ý tổng quát, Bahdanau, ngữ cảnh và cảnh báo diễn giải |
| Dùng GT PDF 323–327 | Một ứng dụng mở rộng căn chỉnh hai chiều cho cặp văn bản |
| Không dùng PDF 15–17 về benchmark và GNMT | LLO yêu cầu cơ chế và phân tích. Đường cong theo độ dài câu và hệ GNMT cần giao thức dữ liệu, metric và triển khai để diễn giải; đưa vào sẽ lệch trọng tâm và không cần để đạt sản phẩm học tập. |
| Không có code demo | Nguồn và yêu cầu không giao chuyển code; bài tập dùng tính tay và phân tích |
| Dùng đúng bảy mạch ngoài | Các nhóm là L10-00–03, 04–07, 08–13, 14–18, 19–26, 27–31 và X01–X04 rồi 32; giữ nguyên 37 trang và toàn bộ ID. |
| Chuyển L10-32 thành trang cuối chung | Kết luận phải phục vụ cả tuyến lõi lẫn tuyến đầy đủ. Đặt L10-32 sau nhánh mở rộng cho phép End từ L10-31 bỏ qua X01–X04, còn tuyến đầy đủ đi qua bốn trang này rồi cùng kết thúc ở L10-32. |
| Định tuyến lại phím ở ranh giới mạch | Reveal có thể giữ chỉ số dọc khi đi ngang. Phím Phải được ánh xạ tại 03→04, 07→08, 13→14, 18→19, 26→27 và 31→X01; End luôn đến L10-32. |

## Sai khác có chủ ý

- Chuyển công thức Bahdanau từ quy ước vectơ cột của giáo trình sang vectơ hàng để khớp các deck trước: $sW_s+hW_h+b_a$, sau đó nhân $v_a$. Quan hệ toán học giữ nguyên sau chuyển vị tham số.
- Bổ sung kích thước theo lô, trục softmax, phát tự động, mặt nạ nguồn trước softmax và chéo entropy hợp nhất từ logit. Đây là chi tiết triển khai cần thiết nhưng slide nguồn không ghi đầy đủ.
- Tạo trace số $e=(1,2,0)$ và ba giá trị hai chiều để nối ví dụ → hình thức → mặt nạ → căn chỉnh → kiểm tra. Các số không phải kết quả thực nghiệm và được ghi là ví dụ tự tính.
- Ma trận căn chỉnh L10-24 dùng hai hàng điểm hoán vị ngoài hàng trace đầu để minh họa truy vấn thay đổi. Không trình bày nó như dữ liệu quan sát.
- Heatmap L10-24 là dữ liệu tự xây để minh họa cực đại đổi thứ tự giữa hai chuỗi; nhãn không được dùng để suy diễn một căn chỉnh ngôn ngữ học đúng.
- Thu hẹp mệnh đề “attention giải quyết nút thắt” thành “giảm nút thắt ngữ cảnh cố định”; không khẳng định loại bỏ mọi giới hạn của RNN hoặc bảo đảm dịch đúng.
- Không đồng nhất trọng số chú ý với giải thích nhân quả. L10-26 giữ đúng cảnh báo của `source.md` và giáo trình PDF 262–263.
- Ba báo cáo phản biện đọc L10-20 thành $O_t$, nhưng kiểm tra byte cục bộ xác nhận chuỗi thật là `O_{t'}` trong cả định nghĩa logit và đối số softmax: `$P_{t'}=\operatorname{softmax}_{V_{tgt}}(O_{t'})$`. Đây là dương tính giả; tuyệt đối không đổi ngược thành $O_t$.
- Đưa định nghĩa tổng quát $\operatorname{Attention}(q,\{(k_i,v_i)\})=\sum_i\alpha(q,k_i)v_i$ vào L10-06 để tuyến lõi đạt LLO20. L10-X02 giữ vai trò áp dụng định nghĩa sang nhiều miền, không còn là lần định nghĩa đầu tiên.
- Giáo trình dùng $e(y_{t'-1})$ cho phép nhúng token đích. Deck đổi thành $E_y(y_{t'-1})$ để không xung đột với $E$ là ma trận điểm; bổ sung $E_y,D_e,g,\phi,h^{enc},W_o,b_o$ vào bảng ký hiệu và ghi chú.

## Tự tính ví dụ

| Đại lượng | Giá trị đầy đủ | Hiển thị |
|---|---:|---:|
| $\exp(-1)$ | 0.3678794412 | 0.3679 |
| $\exp(-2)$ | 0.1353352832 | 0.1353 |
| $\alpha_1$ | 0.2447284711 | 0.2447 |
| $\alpha_2$ | 0.6652409558 | 0.6652 |
| $\alpha_3$ | 0.0900305732 | 0.0900 |
| $c_1=\alpha_1-\alpha_3$ | 0.1546978979 | 0.1547 |
| $c_2=2\alpha_2+\alpha_3$ | 1.4205124847 | 1.4205 |
| $\alpha$ khi vị trí 3 đệm | $(0.2689414214,0.7310585786,0)$ | $(.2689,.7311,0)$ |
| $c$ khi vị trí 3 đệm | $(0.2689414214,1.4621171573)$ | $(.2689,1.4621)$ |

## Rà mạch và biên tập

- no-ai-slop: mặt trang dùng câu trực tiếp, không khẩu hiệu, câu hỏi tu từ, benchmark không có giao thức hoặc lời dẫn về chính văn bản.
- Quill: ký hiệu xuất hiện theo thứ tự $H,S^-$ → $e$ → $\alpha$ → $c$ → $s_{t'}$ → logit; trace được dùng lại đến kiểm tra cuối. Không tạo `quill.json`.
- Chu trình sáu bước được khóa trong storyboard. Công thức softmax xuất hiện sau bộ số; công thức điểm xuất hiện sau sơ đồ trực giác.
- Chỉ dẫn tuyến, đáp án và điểm cần kiểm chứng nằm trong `note-for-author.md`, không đặt trong ghi chú diễn giả.

## Chỉnh sửa sau phản biện độc lập

| Vai rà soát | Mức cao nhất trong báo cáo | Vấn đề hợp nhất | Quyết định |
|---|---|---|---|
| Góc nhìn sinh viên | nghiêm trọng | Đọc sai byte $O_{t'}$; xung đột $e$; thiếu ký hiệu; câu X02 chưa trọn | Bác false positive bằng kiểm tra byte; dùng $\exp$; bổ sung ký hiệu; viết lại thẻ X02. |
| Chuyên gia Học sâu | trung bình | Đọc sai byte $O_{t'}$; thiếu thuật ngữ cross-attention; baseline L30 và nguồn bị bỏ chưa rõ | Giữ công thức đúng; thêm thuật ngữ trong notes; gọi L30 là biến thể cơ sở; ghi rõ bỏ PDF 15–17. |
| Toán học, thuật toán và triển khai | nhẹ | Công thức chưa đệm ở L09; đường truy vấn chưa nối BPTT; thiếu $E_y,D_e$ | Làm rõ phạm vi công thức; nối gradient về bước trước; bổ sung hợp đồng nhúng. |
| Học thuật và giảng dạy | nghiêm trọng | Đọc sai byte $O_{t'}$; định nghĩa tổng quát nằm ở tuyến cắt; ký hiệu và BPTT thiếu nối | Bác false positive; đưa định nghĩa vào L10-06; bổ sung ký hiệu và đường BPTT. |
| Kết nối và mạch viết | trung bình | Notes L10-31 sai vị trí nhánh; đầu ra mạch 5/6 lệch; L30 tranh vai trò kết luận | Sửa câu nối, đồng bộ outline/storyboard và định vị L30 là đối chiếu thiết kế. |

- Sửa ba byte carriage-return làm hỏng `\rightarrow` ở L10-04 và sửa `alpha_i` thành `\alpha_i` ở L10-10.
- Khóa quy ước vectơ hàng ở cả HTML và `bahdanau-score.svg`: $sW_s$, $hW_h$, rồi nhân $v_a$; dùng $t'$ nhất quán cho thời gian đích.
- Bổ sung $s_{n,0}=\phi(h^{enc}_{n,L_n})$ từ trạng thái cuối hợp lệ, shape của phép khởi tạo và lưu ý hidden/cell state của LSTM.
- Giữ $H$ là trạng thái nguồn/khóa và giá trị thô; đổi tên hai biểu diễn chiếu thành $R_q,R_h$ để không tái định nghĩa Q/K. Làm rõ broadcasting, phép co với $v_a$ và số tham số $D_a(D_s+D_h+2)$.
- Bổ sung điều kiện mỗi hàng masked softmax có ít nhất một vị trí hợp lệ, hành vi của $-\infty$, sentinel hữu hạn và hàng toàn mask.
- Đổi kích thước từ vựng thành $V_{tgt}$, bổ sung shape $W_o,b_o,O$ toàn chuỗi, reduction token hợp lệ và điều kiện mẫu số dương nhờ EOS.
- Tách gradient tới encoder thành đường giá trị và đường khóa/điểm, đồng thời nêu đường truy vấn; thêm active mask cho mẫu suy luận đã kết thúc.
- Gắn token nguồn/đích và nhãn “dữ liệu tự xây” cho heatmap; thu hẹp L10-25 thành ba hàng điểm cho sẵn, không suy ngược tham số Bahdanau.
- Định lượng thời gian và bộ nhớ của khối attention, gồm kích hoạt $U$ khi backward.
- Chia deck thành bảy mạch ngoài và thêm liên kết phím Phải tại sáu ranh giới. Tại L10-31, End đi thẳng đến kết luận; phím Phải vào nhánh mở rộng rồi đi xuống đến kết luận chung.
- Đổi ví dụ tuyến mở rộng thành “tra cứu bản ghi theo khóa” và đổi tiêu đề L10-32 để nói rõ Q/K/V cùng được tạo từ một chuỗi.
- Sửa L10-28 để mũi tên đi từ mất mát về các biến nhận gradient; đường qua $s_{t'-1}$ tiếp tục theo BPTT về các bước đích trước. L10-29 nối ba hạng chi phí với các phép ở L10-27 và chốt đánh đổi chi phí theo cặp lấy truy xuất động.
- Phân vai L10-30 là đối chiếu hai biến thể cơ sở, còn L10-32 là kết luận chung và cầu sang Bài 11. Ghi chú L10-31 không còn nói nhánh mở rộng nằm “trước đó”.
- Hậu kiểm đổi tổng trọng số hiển thị thành $\sum_i\alpha_i\approx1$ sau làm tròn; dùng dấu xấp xỉ khi nhân các hệ số hiển thị đã làm tròn ở L10-11 và L10-18, còn kết quả cuối vẫn được tính từ số đầy đủ. Ghi chú L10-28 nêu gradient tới $H$ tiếp tục qua BPTT của bộ mã hóa.
- Sửa `cross-attention.svg` để mỗi $h_i$ đi rõ hai nhánh: nhánh khóa vào hàm điểm rồi softmax tạo $\alpha_{t',i}$, và nhánh giá trị vào $\sum_i\alpha_{t',i}h_i$ để tạo $c_{t'}$. Dùng bus $H_{1:T_s}$ để giữ sơ đồ dễ đọc.

Đề xuất không áp dụng: không thêm code, scaled dot-product, causal mask, multi-head hoặc benchmark vì vượt phạm vi Bài 10; không đổi số trang hay timing vì sửa cục bộ đã đủ và tuyến lõi/mở rộng vẫn là 100/20 phút.

## Kiểm định tĩnh sau chỉnh sửa

- Kiểm tra tĩnh xác nhận 37 mã `data-slide-id` duy nhất, 37 khối ghi chú và bảy mạch ngoài có kích thước 4, 4, 6, 5, 8, 5, 5; L10-32 là trang cuối.
- Thứ tự timing trong storyboard khớp HTML; tổng lõi 100 phút, mở rộng 20 phút và bài tập riêng 50 phút.
- JavaScript nội tuyến phân tích cú pháp được; bảng điều hướng có đúng sáu ranh giới, End trỏ đến L10-32 và các trang khác dùng `Reveal.right()`.
- Bảy SVG đều được tham chiếu và tồn tại; không sửa SVG, CSS, template hoặc index.
- no-ai-slop được dùng để bỏ chỉ dẫn nội bộ, câu chuyển có mã slide và diễn đạt mơ hồ; Quill được dùng để rà đầu vào–đầu ra của bảy mạch. Không tạo `quill.json`.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`; điều phối viên dùng `python3 -m http.server 8765 --bind 127.0.0.1` và chỉ phục vụ thư mục `2627-1/`.
- Chromium headless duyệt đủ 37 trang ở khung $1280\times720$ và $960\times720$, tạo 74 ảnh kiểm tra. Không có tài nguyên hỏng, ảnh thiếu, công thức cắt hoặc chồng lấn; cảnh báo biên tại L10-00 là dương tính giả của bố cục trang bìa và đã được kiểm tra trực quan.
- KaTeX dựng 151 biểu thức, gồm 17 công thức khối, với `throwOnError: true` và `strict: "error"`; không có lỗi KaTeX. Cảnh báo HTTP duy nhất là `favicon.ico` trả 404, không phải tài nguyên cốt lõi.
- Sáu tuyến phím Phải qua ranh giới mạch, End từ L10-31 đến L10-32 và tuyến đầy đủ L10-31 → X01 → X02 → X03 → X04 → L10-32 đều đạt; X04 cần thêm một lần điều hướng để hiện fragment trước khi sang kết luận.
- Danh sách toàn bộ tiêu đề `h1`, `h2`, `h3` đã được rà thủ công; tiêu đề thuần Việt, chỉ giữ tên riêng Bahdanau và thuật ngữ chuẩn softmax.
- Codex Slides trong Browser không có công cụ gọi được trong môi trường này; kiểm định trực quan được thực hiện bằng Chromium cục bộ trên đúng tệp được máy chủ phục vụ.

## Quy trình ghi chú bài giảng và giới hạn tác tử

- Vai lập kế hoạch, ba vai phân tích nguồn, vai kiểm định cấu trúc và năm vai phản biện dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter. Mọi báo cáo được chấp nhận đều có `requested_model` và `observed_model` trùng khớp, `provider` là `OpenRouter`.
- Tám nhiệm vụ soạn mảnh dùng đúng `deepseek/deepseek-v4-flash-0731` qua OpenRouter. Điều phối viên chỉ hợp nhất phần khớp nguồn và tự kiểm lại công thức; loại toàn bộ đề xuất về scaled dot-product, nhiều đầu, self-attention chi tiết, benchmark, kích thước mô hình và bài tập ngoài phân bổ 10/20/15/5 phút của Buổi 10.
- Phạm vi DeepSeek được khóa bền vững cho các đợt sau: mỗi nhiệm vụ chỉ được tạo đúng một tệp mới trong staging riêng; `MCP_WRITE_POLICY=create-once`; `MCP_MAX_WRITE_CHARS=2500`; không có quyền đọc hay ghi toàn kho, sửa tệp đã tồn tại, gọi shell, tải mạng hoặc ghi trực tiếp vào sản phẩm. Mảnh 01 có lần ghi 3.393 byte bị từ chối toàn bộ trước khi chấp nhận bản 2.636 byte. Mảnh 08 có năm lần ghi 5.238, 3.532, 3.397, 3.384 và 3.240 byte bị từ chối toàn bộ trước khi chấp nhận bản 3.059 byte; giới hạn áp dụng theo số ký tự Unicode nên số byte có thể lớn hơn 2.500.
- Hồ sơ gửi cho OpenRouter chỉ gồm văn bản UTF-8 đã trích từ đúng dải nguồn, deck, planning, mẫu, CSS, index và bảy SVG của Buổi 10. `.env`, khóa API và bí mật không nằm trong hồ sơ; `OPENROUTER_ENV_FILE` chỉ được launcher đọc cục bộ.
- Năm báo cáo độc lập cùng phát hiện việc tái dùng $A$ cho hai shape. Ghi chú đã đổi ma trận căn chỉnh của một mẫu thành $\mathcal A$, bổ sung hợp đồng $y,g,W_o,b_o$, làm rõ dịch chỉ số token, phạm vi đếm tham số và phạm vi biểu thức chi phí của khối chú ý.
- Báo cáo góc nhìn sinh viên đề nghị đổi bộ số bài tập vì trùng vết minh họa; không áp dụng vì `source.md` đã khóa bài tập ma trận nhỏ và việc dùng lại cùng vết giúp kiểm tra xuyên suốt. Báo cáo cũng đề nghị đổi các số làm tròn bằng cách trừ số đã làm tròn; không áp dụng vì các giá trị hiển thị được làm tròn trực tiếp từ số đầy đủ và đã được hai vai khác tính lại.
- `$no-ai-slop` được dùng ở bản cuối để bỏ câu mô tả quyết định biên tập khỏi mục nguồn, sửa giọng dặn người soạn thành cảnh báo cho người học, thống nhất thuật ngữ và loại dấu vết quy trình. Nguyên tắc `$quill` được dùng để rà chuỗi nút thắt → truy xuất → vết số → hàm điểm → bộ giải mã → căn chỉnh → chi phí → mở rộng; không tạo `quill.json`.
- Lượt rà lại dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter; wrapper xác nhận `requested_model` và `observed_model` trùng khớp, `provider` là `OpenRouter`. Không còn lỗi mức chặn, nghiêm trọng hoặc trung bình ở các vùng đã sửa.
- Kiểm tra tĩnh của ghi chú xác nhận một H1, 28 dòng chỉ thị tạo 7 cặp câu hỏi–lời giải, 140 biểu thức KaTeX dựng được với `throwOnError: true` và `strict: "error"`, bảy SVG tồn tại và đủ `role="img"`, `title`, `desc`. Không có mã trang, metadata tác tử, ký tự thay thế hoặc ký tự Cyrillic trong nội dung công khai.
- Chromium headless duyệt viewer ở $1280\times720$ và $390\times844$: 140 biểu thức, bảy hình, bảy khối lời giải đóng mặc định, không lỗi console, lỗi trang, yêu cầu hỏng hay ảnh hỏng. Liên kết deck, bỏ qua điều hướng, mở lời giải bằng bàn phím, chế độ in, chặn vượt thư mục và chặn ghép nhầm bài đều đạt. Chênh 35 px của `body.scrollWidth` trên màn hình hẹp nằm trong khối cuộn công thức; cửa sổ không bị cuộn ngang.
- Codex Slides không có công cụ gọi được trong môi trường hiện tại. Kiểm định trực quan dùng Chromium trên viewer cục bộ tại cổng 8766; đây là phương án thay thế đã ghi, không thay đổi nội dung hay giao diện dùng chung.

## Đồng bộ bộ trang chiếu với ghi chú

- Ba vai đọc độc lập và năm vai phản biện cuối dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter. Mọi kết quả được chấp nhận đều có `requested_model` và `observed_model` trùng khớp, `provider` là `OpenRouter`.
- DeepSeek dùng đúng `deepseek/deepseek-v4-flash-0731` qua OpenRouter và chỉ tạo `suggestions.md` trong staging mới. `MCP_WRITE_POLICY=create-once` và `MCP_MAX_WRITE_CHARS=2500` tiếp tục khóa phạm vi. Lần ghi đầu 3.177 byte vượt giới hạn và bị từ chối toàn bộ; lần ghi 2.719 byte, tương ứng 2.239 ký tự Unicode, mới được chấp nhận. DeepSeek không sửa HTML, lecture note, SVG hoặc tệp dự án.
- Các delta được áp dụng cục bộ: tách tính chất softmax khỏi định nghĩa chú ý tổng quát; bỏ ký hiệu ngữ cảnh trung gian gây xung đột; dùng $\mathcal A$ cho ma trận căn chỉnh một mẫu; ghép nhúng token và ngữ cảnh ở đầu vào bộ giải mã; đồng bộ sáu bước; tách chi phí logit khỏi chi phí khối chú ý; thống nhất tiên quyết và ba đường gradient.
- `$no-ai-slop` được dùng trên cả mặt trang và `aside.notes`. Đã bỏ tham chiếu `source.md`, các câu điều phối tuyến, lời nhắc trang trước–sau, mô tả tự kiểm và hướng dẫn dành cho diễn giả/người viết; giữ lại giải thích chuyên môn, cảnh báo sai lầm và nguồn. Nguyên tắc `$quill` xác nhận bảy mạch và các ranh giới không đổi; không tạo `quill.json`.
- Nhiều vai tiếp tục đọc sai chuỗi $O_{t'}$ thành $O_t$. Kiểm tra chuỗi trực tiếp trong HTML và kết quả KaTeX xác nhận công thức thật là $P_{t'}=\operatorname{softmax}_{V_{tgt}}(O_{t'})$; đề xuất sửa bị bác là dương tính giả. Đề xuất đổi ngữ cảnh cố định thành $c=\phi(h^{enc}_{L_n})$ cũng không áp dụng: baseline giữ $c=h^{enc}_{L_n}$ rồi dùng $s_0=\phi(c)$, đúng với L10-03 và ghi chú bài giảng.
- Chromium headless dựng 37 trang, bảy mạch ngoài, 37 mã duy nhất, 37 khối ghi chú, 158 biểu thức KaTeX và bảy SVG ở cả $1280\times720$ lẫn $960\times720$. Không có lỗi KaTeX, ảnh hỏng, lỗi runtime, tràn hoặc chồng lấn. Sáu tuyến phím Phải và End từ L10-31 đến L10-32 đều đạt; 74 ảnh kiểm định đã được tạo trong `/tmp`.
- Toàn bộ tiêu đề `h1`, `h2`, `h3` đã được xuất và rà thủ công. Tiêu đề thuần Việt; chỉ giữ tên riêng Bahdanau, ký hiệu LLO và thuật ngữ chuẩn softmax theo ngoại lệ đã cho phép.
