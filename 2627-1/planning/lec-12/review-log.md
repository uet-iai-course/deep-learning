# Nhật ký rà soát — Bài 12

## Phạm vi worker OpenRouter cho ghi chú bài giảng — 2026-09-03

- Hồ sơ nguồn lọc: `/tmp/deep-learning-lec12-dossier.Xvp2nS`. PDF được trích xuất cục bộ thành UTF-8 theo đúng dải đã duyệt; không gửi PDF, `.env`, khóa hoặc tệp bí mật cho worker.
- Tác tử lập kế hoạch và đọc nguồn yêu cầu `z-ai/glm-5.3-flash`; lượt lập kế hoạch được chấp nhận sau khi metadata runtime xác nhận `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Ba lượt phân tích nguồn/toán/sư phạm tiếp tục gọi công cụ nhưng không trả JSON kết quả hoàn chỉnh; không dùng các lượt này làm bằng chứng. Đây là lỗi đầu ra worker, không phải xác nhận nội dung.
- Tác tử soạn yêu cầu `deepseek/deepseek-v4-flash-0731`. Mỗi mảnh dùng staging riêng `/tmp/lec12-writer-01b`, `/tmp/lec12-writer-02` đến `/tmp/lec12-writer-10`, `MCP_WRITE_POLICY=create-once` và `MCP_MAX_WRITE_CHARS=2500`. Tệp đích không tồn tại trước lần ghi; writer không có quyền ghi vào kho dự án.
- Lượt 01 ban đầu tại `/tmp/lec12-writer-01` hai lần vượt 2.500 ký tự. Cầu nối từ chối toàn bộ trước khi tạo tệp; lượt này bị dừng và thay bằng nhiệm vụ hẹp hơn tại staging mới `01b`.
- DeepSeek ở mảnh 01b ghi `fragment.md` ở gốc staging thay vì `output/fragment.md`. Nội dung vẫn nằm trong gốc được cấp và chỉ ghi một lần; đường dẫn sai được ghi nhận, không sao chép tự động vào kho.
- Mọi mảnh được biên tập lại bằng tay trước khi hợp nhất. Ba lỗi nội dung bị loại: chia nhiệt độ hai lần và đảo dấu loss CLIP; ghi tỷ số tiệm cận của chi phí chú ý là 4 thay vì 16; mô tả nhầm hai vị trí là đệm trong ví dụ mặt nạ.
- Giới hạn bền vững cho các đợt sau: không tăng `MCP_MAX_WRITE_CHARS`; khi vượt giới hạn phải tách hoặc thu hẹp nhiệm vụ trong staging mới. Không cho DeepSeek sửa trực tiếp HTML, Markdown hay SVG của dự án; chỉ nhận mảnh đề xuất. Không gửi `.env`, bí mật hoặc tệp nhị phân. Mọi công thức, shape, số liệu và phạm vi nguồn phải được kiểm lại cục bộ trước khi hợp nhất.

## Rà soát ghi chú bài giảng — 2026-09-03

- Năm vai reviewer độc lập chạy bằng `z-ai/glm-5.3-flash`; mọi lượt được dùng đều có metadata runtime `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Các lỗi đã sửa: ba macro `\qquad`; thiếu câu hỏi kiểm tra ở cụm mã hóa–giải mã và CLIP; dùng lại `objective-trace.svg` sai ngữ cảnh; ví dụ MLM không khớp vị trí 4/5; ký hiệu mặt nạ bộ mã hóa không thống nhất.
- Cảnh báo thiếu RevealJS, plugin và KaTeX bị bác bỏ vì hồ sơ nguồn lọc không sao chép thư viện. Kiểm tra trên kho thật xác nhận `revealjs/dist/reveal.js`, `plugin/math/math.js` và `vendor/katex/` tồn tại.
- Hậu kiểm GLM theo hồ sơ `recheck` xác nhận PASS cho năm vùng sửa và tính lại đúng $\ln(4/3)\approx0{,}287682$, $65^2/17^2\approx14{,}62$ và giới hạn tiệm cận 16.
- Kiểm định trình xem: HTTP 200 trên cổng cục bộ 8766; Chromium kết xuất ảnh 1280×720 và PDF 14 trang. Văn bản trích từ PDF không có `qquad`, lỗi KaTeX, `undefined`, `NaN`, tên worker hoặc chỉ dẫn nội bộ.
- Rà `$no-ai-slop`: không còn nhãn “mảnh”, lời dẫn chung chung, tự khen, câu hỏi tu từ, dấu vết worker, chú giải quy trình hay chỉ dẫn cho người viết/diễn giả. Các câu hỏi còn lại đều là hoạt động học tập có nhiệm vụ cụ thể.
- Rà theo nguyên tắc `$quill`: thứ tự ba họ → huấn luyện trước/LLM → CLIP → ViT → giới hạn triển khai giữ được quan hệ tiên quyết; ký hiệu và bộ số được truyền liên tục từ ví dụ sang công thức và bài kiểm tra. Không tạo `quill.json`.

## Lượt phân tích nguồn mới và sửa cục bộ theo đặc tả

| Mức độ | Vùng | Vấn đề | Quyết định |
|---|---|---|---|
| Trung bình | L12-37 | Ghi chú nguồn dùng cụm chung "tổng hợp từ các nguồn của Buổi 12", không truy nguyên được. | Thay bằng trích cụ thể: giáo trình PDF 280–293 và 327–333; Radford và cộng sự (2021), PDF 1–3; `lec17_vision_transformers.pdf`, PDF 18–24. Không đổi nội dung bảng. |
| Nhẹ | `clip-zero-shot.svg` | `desc` chưa nhắc hệ số nhiệt độ $\tau$ dù $Z=E_I(E_T^{cls})^\top/\tau$ ở L12-23. | Bổ sung vào `desc` câu nhắc chia điểm cho hệ số nhiệt độ $\tau$ (dạng $1/\tau$) trước softmax theo trục lớp. |
| Nhẹ | `mask-families.svg` | `desc` dùng "cặp hợp lệ" mơ hồ, chưa nói rõ hợp lệ nghĩa là khóa không phải đệm. | Viết lại `desc`: ô được phép nghĩa là khóa không phải vị trí đệm. |
| Không áp dụng | L12-02 | Nguồn đã sắp đúng thứ tự nguồn chính trước (`lec16_transformer.pdf`, PDF 38–48) rồi giáo trình (PDF 280–288); không đổi nội dung. | Giữ nguyên. |

## Bằng chứng tính lại độc lập

- Shape ViT: ảnh $2\times3\times32\times32$, $P=8$ cho $T_p=(32/8)^2=16$ mảnh, $CP^2=3\cdot64=192$; sau chiếu $2\times16\times64$; thêm CLS và nhúng vị trí cho $2\times17\times64$; mỗi khối giữ nguyên kích thước. Khớp L12-28, L12-31, L12-34.
- CLIP X03: $E_I=E_T=I_2$, $1/\tau=\ln3$ cho $S=\operatorname{diag}(\ln3,\ln3)$; mỗi hàng và cột cho xác suất $3/4$ cho cặp đúng, nên $\mathcal L_{I\to T}=\mathcal L_{T\to I}=\mathcal L_{CLIP}=\ln(4/3)\approx0{,}287682$.
- Tỷ số chi phí chú ý: $65^2/17^2=4225/289\approx14{,}62$; 16 chỉ là tỷ số tiệm cận khi bỏ qua CLS. Khớp L12-33 và X04.

## Lượt chỉnh sửa riêng sau giới hạn lượt trước

Kiểm định storyboard phát hiện trùng nội dung giữa L12-13 và L12-17 (cùng chạm hợp đồng suy luận của bộ giải mã). Rà soát lại bằng 5 vai reviewer độc lập: sinh viên, chuyên gia Học sâu, toán/thuật toán/triển khai, phản biện học thuật/giảng dạy, và kết nối/mạch. Mỗi vai tóm tắt theo trường: mức độ / trang / vấn đề / bằng chứng / đề xuất, rồi tổng hợp quyết định sửa.

| Mức độ | Trang | Vấn đề | Bằng chứng | Đề xuất | Quyết định |
|---|---|---|---|---|---|
| Nghiêm trọng | L12-13, L12-17 | Đáp án L12-13 nói EOS "trở thành khóa hợp lệ khi dự đoán các vị trí sau nó" dễ đọc thành EOS được dùng ngay; trùng mạch hợp đồng suy luận ở L12-17. | HTML L12-13 fragment; storyboard dòng L12-13/L12-17. | Viết chính xác: không, vì mặt nạ chặn mọi khóa $j>i$; EOS bên phải chưa nằm trong tiền tố được phép đọc tại vị trí 2. | Đã sửa HTML và note-for-author; đóng lỗi. |
| Trung bình | L12-04 | Mặt nạ khóa hợp lệ cần tách bạch khỏi mặt nạ chú ý. | HTML L12-04. | Nêu rõ $M^{valid}$ chặn đệm trước softmax. | Đã sửa. |
| Trung bình | L12-22 | Trục log-softmax và hệ số $1/N$ từng mơ hồ. | HTML L12-22. | Khóa hàng=ảnh, cột=văn bản, hai loss trên $S$ và $S^\top$. | Đã sửa; giữ font `.82`, không thêm tải văn bản. |
| Trung bình | L12-24 | Ví dụ trước tổng quát hóa. | HTML L12-24–25. | Giữ ví dụ $32\times32,P=8$ trước công thức. | Đã sửa. |
| Trung bình | L12-29 | Thiếu trục LN, epsilon, chế độ dropout. | HTML L12-29. | LN theo $D$, $\varepsilon>0$, dropout trước cộng đường dư, train/eval. | Đã sửa. |
| Trung bình | L12-33 | Tỷ số 16 từng bị dùng như số đúng. | HTML L12-33, X04. | Ghi $14{,}62$ cho ví dụ, 16 chỉ tiệm cận. | Đã sửa; khôi phục bullet X04 trong note-for-author. |
| Trung bình | L12-35–36 | Câu chuyển giữa tuyến kỹ thuật và thảo luận từng đứt. | HTML L12-35–36. | Thêm câu nối ở ghi chú L12-35. | Đã sửa; giữ bullet riêng L12-35→36 trong note-for-author. |
| Nhẹ | SVG (4 tệp) | Thuật ngữ pha Anh–Việt, KaTeX thô. | `img/lec-12/*.svg`. | Việt hóa và thay nhãn. | Đã sửa. |
| Nhẹ | L12-37 | Nguồn ghi chung chung. | HTML L12-37. | Trích nguồn cụ thể. | Đã sửa. |
| Nhẹ | L12-16 | Công thức loss cần nhấn cross-entropy hợp nhất. | HTML L12-16. | Thêm câu chỉ dẫn ổn định số. | Đã sửa. |

Quyết định không đổi:
- Không đổi timing L12-36: thời lượng đã khớp storyboard và tổng 100 phút; đổi sẽ lệch tuyến lõi.
- Không tách fragment X03: phép tính hai cặp gọn, tách làm mất tính liền mạch của ví dụ kiểm chứng đối xứng.
- Không đảo L12-29–30: thứ tự công thức rồi sơ đồ khớp mạch "định nghĩa → trực giác hóa" đã dùng xuyên bài.

Không tuyên bố QA trình duyệt mới; không đồng bộ Codex Slides. Kiểm tĩnh: 42 ID slide duy nhất, 42 ghi chú diễn giả, sáu stack ngang cho tuyến lõi và một stack dọc cho phụ lục.

## Hậu kiểm sau chỉnh sửa riêng

- Vai toán học, thuật toán và triển khai xác nhận mask, các hàm mất mát, trục log-softmax, $\tau$, ví dụ $\ln(4/3)$, chuỗi kích thước ViT, $H_a$, $W_o$ và tỷ số $14{,}62$ đều đạt. Điều phối viên phát hiện thêm một lỗi triển khai ở L12-17: đầu ra chú ý chéo không cố định vì truy vấn đích thay đổi. Bản cuối chỉ giữ $H^{enc}$ cố định và nêu khóa/giá trị nguồn đã chiếu là phần có thể lưu khi triển khai hỗ trợ.
- Vai kết nối và mạch viết xác nhận lỗi nghiêm trọng L12-13/L12-17 đã đóng: L12-13 chỉ kiểm tra nhân quả; L12-17 kiểm tra phần nguồn được tái dùng và tiền tố đích tăng dần. Ranh giới L12-35→36→37, mạch CLIP→ViT, 7 mạch ngoài và thời lượng 100+20+50 đều đạt.
- Sau hậu kiểm, làm rõ câu trục ở L12-22 và đồng bộ cách gọi sáu stack ngang cùng một stack dọc trong `note-for-author.md`; hai sửa này không đổi công thức, thứ tự, ID hoặc thời lượng.

## Kiểm định cuối của checkpoint hiện hành

- Lệnh bắt buộc `python3 -m reloadserver 8765` vẫn không chạy vì môi trường thiếu mô-đun `reloadserver`. Máy chủ dự phòng chỉ phục vụ thư mục `2627-1` trên `127.0.0.1:8765`; không phục vụ gốc kho hoặc `.env`.
- Chromium chụp đủ 42 trang ở $1280\times720$ và 42 trang ở $900\times720$. Sau khi tắt hiệu ứng chuyển trang để tránh ảnh trung gian, không phát hiện phần tử vượt khung, tràn chữ, chồng lấn hoặc nội dung bị cắt.
- KaTeX không có phần tử lỗi ở cả hai kích thước. Toàn bộ tài nguyên cốt lõi tải thành công; lỗi 404 duy nhất là favicon không cốt lõi.
- Điều hướng bàn phím đã đổi được cả chỉ số ngang và dọc. Kiểm tĩnh xác nhận 42 ID duy nhất, 42 ghi chú, 42 hàng storyboard đúng thứ tự, 7 `<section>` ngoài, không có raster và 7/7 SVG có `role="img"`, `title`, `desc`.
- Rà thủ công toàn bộ tiêu đề `h1`, `h2`, `h3`: không có tiêu đề pha tiếng Anh ngoài tên kiến trúc, mô hình và viết tắt được phép như Transformer, CLIP, ViT, CNN, LLM, CLS và LLO.
- Codex Slides không có bề mặt gọi được trong phiên công cụ hiện tại; không tuyên bố đã rà bằng Codex Slides. Giới hạn này không thay đổi bằng chứng kiểm định Chromium cục bộ ở trên.

## Trạng thái bàn giao

Bản hoàn chỉnh có 38 trang lõi/100 phút và 4 trang mở rộng/20 phút. LLO24 có định nghĩa mô hình đa phương thức và trường hợp CLIP dựa trên nguồn được duyệt. Năm lượt review độc lập, kiểm định storyboard và hai hậu kiểm toán/mạch đều đã hoàn tất.

## Phát hiện đã ghi nhận và quyết định sửa

| Mức độ | Vùng | Vấn đề | Quyết định |
|---|---|---|---|
| Chặn bàn giao | L12-21–23, X03 cũ | Nội dung đa phương thức và phép kiểm ảnh không có bằng chứng trong dải nguồn đã duyệt; dẫn PDF 312–314 sai. | Xóa hoàn toàn bốn trang khỏi HTML; xóa ánh xạ sai; ghi khoảng trống nguồn và thiếu 7+5 phút. |
| Đã xử lý | L12-21–23, X03 | Người dùng duyệt Radford và cộng sự (2021), PDF 1–3, làm nguồn bổ sung cho mô hình đa phương thức. | Soạn lại từ đầu: hai bộ mã hóa, ma trận tương đồng và sai số đối xứng, phân loại zero-shot; thêm phép tính $N=2$ ở X03. Không khôi phục nội dung cũ không truy nguyên được. |
| Nghiêm trọng | L12-21–23 | Có nguy cơ mô tả CLIP như mô hình sinh hoặc như kiến trúc chú ý chéo. | Ghi rõ hai nhánh mã hóa độc lập, mỗi đầu vào cho một vectơ; chỉ tương tác qua ma trận tương đồng. Không dùng sinh chú thích hoặc cross-attention. |
| Nghiêm trọng | L12-22–23, X03 | Ký hiệu và trục có thể mơ hồ giữa điểm ghép cặp và điểm lớp. | Dùng $E_I,E_T$ cho biểu diễn đã chuẩn hóa, $S\in\mathbb R^{N\times N}$ cho điểm cặp, $Z\in\mathbb R^{N\times K}$ cho điểm lớp; nêu hàng=ảnh, cột=văn bản, softmax lớp theo $K$. |
| Nghiêm trọng | L12-14–17 | Thiếu dịch nhãn, kích thước biểu diễn/điểm, trục từ vựng, trung bình theo ký hiệu hợp lệ và khác biệt huấn luyện–suy luận. | Viết lại từ giáo trình PDF 284–288; giữ chu trình ví dụ → mặt nạ → tính toán → kiểm tra. |
| Nghiêm trọng | L12-04,10,15 | Chưa khóa trục truy vấn/khóa, phát mặt nạ, dạng Boolean/cộng và quan hệ giữa đệm với hàm mất mát. | Bổ sung kích thước $N\times1\times T_q\times T_k$, hàng truy vấn/cột khóa, phát theo đầu; chỉ bắt buộc chặn khóa đệm và loại vị trí đệm khỏi loss. Không áp đặt quy tắc đưa đầu ra truy vấn đệm về không. |
| Trung bình | L12-11,16,32 | Ký hiệu $A$ cho điểm lớp va với $A$ của trọng số chú ý ở Bài 10–11. | Đổi điểm chưa chuẩn hóa thành $Z^{CLM}$, $Z^{tgt}$ và $Z^{cls}$; giữ $A$ riêng cho trọng số chú ý. |
| Trung bình | Bài tập 50 phút | Bản trước chỉ có bài kỹ thuật, chưa thực hiện hoạt động động não dự án cuối kỳ và tiêu chí đánh giá trong DOCX Buổi 12. | Phân bổ 30 phút bài kỹ thuật + 20 phút động não; đặt sản phẩm và thang chấm khả thi/sáng tạo trong `note-for-author.md`, không đưa chỉ dẫn nội bộ lên mặt trang chiếu hoặc ghi chú diễn giả. |
| Trung bình | L12-06,11 | Miền tập MLM và mẫu số CLM chưa đủ chặt. | Loại đệm/ký hiệu đặc biệt theo giao thức, yêu cầu $|\Omega|>0$ và $\sum M^{tgt}>0$; EOS là nhãn hợp lệ. |
| Trung bình | L12-18–20 | Kiểm định quy mô lặp lại cấu trúc rủi ro ở L12-36. | Đổi L12-20 thành kiểm tra giới hạn suy luận từ tên gọi LLM. |
| Nghiêm trọng | L12-29–33, X04 | Thiếu trục LN, epsilon, chế độ dropout; tỷ lệ 16 lần bị dùng như số đúng của ví dụ. | Khóa LN theo $D$, $\varepsilon>0$, dropout trước phép cộng đường dư và train/eval; ghi $65^2/17^2\approx14{,}62$, chỉ gọi 16 lần là tiệm cận. |
| Trung bình | 4 SVG dùng thực tế | Thuật ngữ pha Anh–Việt; SVG ViT hiển thị chuỗi KaTeX thô. | Việt hóa bốn SVG, thay chuỗi KaTeX thô bằng nhãn SVG, thêm hàng=truy vấn/cột=khóa. |
| Trung bình | Toàn bộ trang chiếu và tệp quy trình | Thuật ngữ và storyboard chưa đủ kiểm chứng; trạng thái thời lượng bị trình bày như hoàn thành. | Rà no-ai-slop/Quill, Việt hóa tiêu đề và ghi chú; viết lại storyboard mọi ID; công khai trạng thái chưa đạt. |
| Trung bình, storyboard | L12-18–26, X03 | Chu trình LLM thiếu ví dụ; kiểm tra CLIP chỉ nằm ở tuyến cắt; trace $E_I,E_T,S,Z$ đứt trước ViT; công thức mảnh đi trước ví dụ; X03 thiếu kết quả mảnh. | Thêm ví dụ MLM/CLM ở L18; thêm kiểm tra shape/trục ở L23; nối CLS cuối→chiếu→chuẩn hóa→$E_I$ tại L26; đổi L24 thành ví dụ và L25 thành tổng quát; thêm fragment X03. |
| Trung bình, góc nhìn sinh viên | L12-19–20,26,35–37 | Định nghĩa/câu hỏi LLM có nhiều cách hiểu; hai tiêu đề không khớp nội dung; đạo đức là bảng đáp án sẵn; trang tổng hợp bỏ CLIP và encoder–decoder. | Khóa định nghĩa làm việc và câu hỏi có/không; đổi tiêu đề L26/L35; chuyển L36 thành tình huống thảo luận; L37 dùng bảng năm cấu hình. |
| Trung bình, chuyên gia Học sâu | L12-21,23–26 | “Đa phương thức” chưa được định nghĩa trước CLIP và quan hệ CLIP–ViT dễ bị hiểu là đồng nhất. | L21 định nghĩa mô hình đa phương thức rồi giới hạn CLIP là trường hợp ảnh–văn bản; L23/L26 nói rõ ViT chỉ là một lựa chọn bộ mã hóa ảnh. |
| Trung bình, toán học/triển khai | L12-22, X03 | $\mathcal L_{I\to T},\mathcal L_{T\to I}$ thiếu $1/N$, trục log-softmax và chỉ dẫn ổn định số; X03 không hiện kết quả. | Viết đủ hai phép trung bình trên $S$ và $S^\top$, dùng cross-entropy hợp nhất/log-softmax ổn định; fragment X03 hiện $S$ và $\ln(4/3)$. |
| Trung bình, học thuật/giảng dạy | L12-18–23,36–37 | Ví dụ chưa dẫn vào định nghĩa, câu hỏi chưa tạo quyết định và tổng kết chưa đối chiếu đủ các họ. | Dùng lại MLM/CLM trước định nghĩa LLM; kiểm tra CLIP trong lõi; L36 yêu cầu bằng chứng+hành động; L37 đối chiếu encoder, decoder, encoder–decoder, CLIP và ViT. |
| Chặn hiển thị, kiểm định cuối | L12-22 | Hai công thức sai số đặt chung một dòng làm tràn ngang và đẩy toàn bộ bố cục `print-pdf` khỏi khung. | Tách phần biểu diễn, ma trận điểm và hai sai số thành các dòng riêng; giữ cỡ công thức trung tâm từ `0.75em`; rà lại ở 1280×720 và 900×720. Không đổi nội dung toán học. |

## Sai khác có chủ ý so với nguồn

- Ví dụ văn bản và ví dụ ViT dùng số tự dựng để kiểm tra kích thước; không được trình bày như kết quả thực nghiệm.
- `lec17` PDF 5–17 được gộp thành động cơ ở L12-24–25; các hướng lai CNN và ImageGPT bị lược để giữ mạch ViT cơ sở.
- `lec17` PDF 25–26 bị bỏ vì vượt mức truy vết ViT cơ sở.
- Công thức mặt nạ, điều kiện mẫu số, quy tắc chặn khóa đệm, loại đệm khỏi loss và cross-entropy hợp nhất là phần làm rõ triển khai dựa trên công thức nguồn/Bài 11. Không bắt buộc triệt đầu ra tại truy vấn đệm.
- Các trang đa phương thức cũ bị xóa thay vì giữ nội dung không có nguồn; sau khi nguồn CLIP được duyệt, L12-21–23 và X03 được soạn mới từ PDF 1–3.
- Hình 1 và Hình 3 của CLIP được vẽ lại thành ba SVG theo quan hệ khái niệm, không chép ảnh mẫu, bố cục hoặc giả mã nguyên văn.
- Công thức $S=E_IE_T^\top/\tau$ dùng $\tau>0$ thay cho tham số log-temperature trong giả mã nguồn; hai cách tương đương qua $1/\tau=\exp(t)$.
- Ví dụ X03 là phép tính tự dựng với hai cặp trực chuẩn; không phải số liệu hay kết quả thực nghiệm từ bài báo.
- Hoạt động động não và thang chấm dự án được thêm từ DOCX Buổi 12. Đây là hoạt động của tiết bài tập và không tính vào thời lượng trình chiếu.

## Rà vùng ảnh hưởng ±2

- L12-12–20: kiểm tra lại đường chuyển từ sinh tự hồi quy sang mã hóa–giải mã, rồi huấn luyện trước và LLM; dữ kiện $Y^{in}/Y^{out}$ và các mặt nạ được giữ xuyên L12-14–17.
- L12-18–26 và hai trang mỗi phía: L16–17 giữ nguyên trace mã hóa–giải mã; L18 dùng MLM/CLM làm ví dụ trước định nghĩa L19 và kiểm tra L20; L21 định nghĩa đa phương thức; L22–23 khóa loss và kiểm tra CLIP; L24–25 đi ví dụ→tổng quát; L26 nối ViT với $E_I$ trước L27–28. Không đồng nhất CLIP với ViT.
- L12-27–37 và hai trang mỗi phía: L27–34 giữ trace shape; L29 và SVG thống nhất hai vị trí bỏ ngẫu nhiên; L35 chỉ so thiên kiến; L36 là tình huống không lộ đáp án; L37 tổng hợp đủ năm cấu hình.
- X01–X04: một stack phụ lục dọc; X03 nối phép sinh ở X02 với đánh đổi ViT ở X04 bằng một phép tính riêng cho CLIP, không phụ thuộc ví dụ ViT.

## Kiểm định tĩnh sau sửa

- HTML: 42 ID duy nhất, 42 ghi chú; storyboard có đúng 42 hàng và cùng thứ tự ID.
- Thời lượng theo storyboard: lõi 38 trang/100 phút; mở rộng 4 trang/20 phút; bài tập 50 phút riêng.
- KaTeX: 129 biểu thức dựng thành công với `throwOnError: true`, `strict: "error"` sau khi giải mã thực thể HTML trước khi kiểm.
- Tài nguyên: 17 đường dẫn cục bộ đều tồn tại; không có tài nguyên mạng cốt lõi hoặc ảnh raster.
- SVG: 7/7 tệp được HTML tham chiếu, đọc được bằng trình phân tích XML, có `role="img"`, `title` và `desc`.
- Ví dụ X03 được tính độc lập: xác suất cặp đúng là $3/4$ và sai số đối xứng là $\ln(4/3)\approx0{,}287682$.
- Ba SVG CLIP đã được kết xuất bằng ImageMagick và rà ở kích thước gốc; không thấy nhãn bị cắt hoặc quan hệ sai. `vit-prenorm.svg` sau sửa cũng kết xuất thành công; hai nút Bỏ ngẫu nhiên nằm trước đúng hai phép cộng đường dư và không chồng nhãn.
- Không có `quill.json`.
- Rà `no-ai-slop`: phần bổ sung không có mở bài rỗng, phóng đại, câu hỏi tu từ hoặc kết luận không có nguồn. Tiêu đề mới viết bằng tiếng Việt; tên CLIP chỉ xuất hiện sau khi giới thiệu đầy đủ.
- Rà liên tục theo Quill: L18–20 chuẩn bị huấn luyện trước và giới hạn kết luận; L21–23 nối dữ liệu ghép cặp với mục tiêu đối sánh; L24–26 cụ thể hóa nhánh ảnh bằng ViT. X01–X04 giữ bốn bài mở rộng độc lập và có câu chuyển rõ.
- HTTP cục bộ: trang và toàn bộ 17 tài nguyên trả mã 200 tại cổng 8765.
- Rà trực quan: đã chụp đủ 42/42 trang ở 1280×720; rà hai bảng tiếp xúc; không thấy tràn, chồng lấn, công thức hoặc hình bị cắt. L12-21–23 và L12-36–37 được rà thêm ở 900×720 và không bị cắt.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy được vì môi trường thiếu mô-đun `reloadserver`; dùng máy chủ HTTP cục bộ đang chạy trên đúng cổng 8765 để tiếp tục kiểm định.
- Chromium tải và chụp trang RevealJS bình thường. Chức năng `--print-to-pdf` của Chromium trong phiên này sinh PDF trắng một trang cho cả Bài 11 đối chứng và Bài 12, nên không dùng PDF đó làm bằng chứng; thay bằng ảnh chụp từng trang.
- Codex Slides đã mở dự án `20260827003236-b-i-12-transformer-n-ng-cao-vgii`. Tải Design File bằng đường dẫn tuyệt đối thất bại với HTTP 500; đây là giới hạn runtime của plugin, trùng lớp lỗi `File is not defined` đã quan sát ở Bài 11. Không tuyên bố đã đồng bộ hoặc rà deck trong Codex Slides.

## Trạng thái review độc lập

- Năm lượt review độc lập và báo cáo storyboard sau bổ sung CLIP đã được hợp nhất; các quyết định sửa tương ứng được ghi trong bảng trên.
- Hậu kiểm toán xác nhận PASS cho loss CLIP, trục, hệ số $1/N$, ổn định số, shape ViT, cầu nối ViT→$E_I$, hai vị trí bỏ ngẫu nhiên và kết quả X03.
- Hậu kiểm học thuật xác nhận PASS cho hoạt động thảo luận L36, mạch L18–26, sơ đồ L29–30, so sánh L35 và bảng tổng hợp L37.
