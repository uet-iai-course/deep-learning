# Nhật ký rà soát — Bài 12

## Trạng thái bàn giao

Bản hoàn chỉnh có 38 trang lõi/100 phút và 4 trang mở rộng/20 phút. LLO24 có định nghĩa mô hình đa phương thức và trường hợp CLIP dựa trên nguồn được duyệt. Bốn lượt review độc lập, kiểm định storyboard, hậu kiểm toán/học thuật và rà trực quan cuối đều đã hoàn tất.

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

- Bốn lượt review độc lập và báo cáo storyboard sau bổ sung CLIP đã được hợp nhất; các quyết định sửa tương ứng được ghi trong bảng trên.
- Hậu kiểm toán xác nhận PASS cho loss CLIP, trục, hệ số $1/N$, ổn định số, shape ViT, cầu nối ViT→$E_I$, hai vị trí bỏ ngẫu nhiên và kết quả X03.
- Hậu kiểm học thuật xác nhận PASS cho hoạt động thảo luận L36, mạch L18–26, sơ đồ L29–30, so sánh L35 và bảng tổng hợp L37.
