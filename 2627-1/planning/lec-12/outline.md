# Bài 12 — Transformer nâng cao

## Trạng thái phạm vi

- Đối tượng: sinh viên đã học cơ chế chú ý và Transformer cơ sở ở Bài 10–11.
- Bản hiện tại có 38 trang lõi, 100 phút.
- Phụ lục có 4 trang, 20 phút.
- Bài tập 50 phút được thiết kế riêng, không cộng vào thời lượng trình chiếu.

## Kết quả học tập và mức đáp ứng

- LLO23: phân biệt mô hình chỉ bộ mã hóa và chỉ bộ giải mã qua luồng thông tin, mặt nạ và mục tiêu — đã có nội dung.
- LLO24: trình bày mô hình ngôn ngữ lớn và mô hình đa phương thức ở mức khái niệm — đã có nội dung; CLIP được dùng làm trường hợp hai bộ mã hóa ảnh–văn bản.
- LLO25: truy vết Vision Transformer từ ảnh NCHW đến dự đoán — đã có nội dung.

## Mạch nội dung

1. Một chuỗi ký hiệu, ba họ kiến trúc và ba cách tạo tín hiệu học.
2. Chỉ bộ mã hóa: ngữ cảnh hai chiều, MLM, vị trí chịu giám sát và tinh chỉnh.
3. Chỉ bộ giải mã: mặt nạ nhân quả, nhãn kế tiếp và sinh tự hồi quy.
4. Mã hóa–giải mã: dịch chuỗi đích, ba mặt nạ, kích thước, sai số và khác biệt huấn luyện–suy luận.
5. Huấn luyện trước qua ví dụ MLM/CLM và định nghĩa làm việc về mô hình ngôn ngữ lớn.
6. Mô hình đa phương thức và CLIP như một trường hợp ảnh–văn bản hai bộ mã hóa.
7. CLIP: biểu diễn chung, ma trận tương đồng, sai số đối xứng và phân loại zero-shot.
8. ViT: NCHW → ví dụ mảnh → công thức tổng quát → chiếu → CLS/vị trí → bộ mã hóa chuẩn hóa trước → phân loại hoặc biểu diễn ảnh CLIP.
9. Tình huống đạo đức và bảng tổng hợp năm cấu hình theo luồng thông tin.

## Ánh xạ nguồn và quyết định

| Nguồn | Dải | Quyết định | Trang đích và lý do |
|---|---:|---|---|
| DOCX đề cương, Buổi 12 | tên buổi, LLO23–25 | giữ | L12-00–01 khóa phạm vi; L12-18–23 đáp ứng LLO24 ở mức khái niệm. |
| `lec16_transformer.pdf` | PDF 38–48 | giữ, tách | L12-02–20: tách ba họ, MLM, CLM, tinh chỉnh và huấn luyện trước để giảm tải nhận thức. |
| `lec17_vision_transformers.pdf` | PDF 5–17 | gộp, lược | Chỉ giữ động cơ chuyển ảnh thành chuỗi tại L12-24–25. Lược các hướng CNN+kết hợp chú ý và ImageGPT vì không cần cho chuỗi ViT cơ sở. |
| `lec17_vision_transformers.pdf` | PDF 18–24 | giữ, tách, thêm ví dụ | L12-24–35 và X04: tách mảnh, chiếu, CLS/vị trí, chuẩn hóa trước và đánh đổi chi phí; ví dụ $N=2,C=3,H=W=32,P=8,D=64$ là phép tính tự dựng, không phải kết quả thực nghiệm. |
| `lec17_vision_transformers.pdf` | PDF 25–26 | bỏ | Biến thể/quy mô hệ thống nằm ngoài mục tiêu truy vết ViT cơ sở và không cần cho LLO25. |
| `lec01_intro.pdf` | PDF 24 | bỏ khỏi nội dung kỹ thuật | Trang giới thiệu ứng dụng không cung cấp cơ chế đa phương thức hay bằng chứng để đáp ứng LLO24. |
| `hocsau_draft.pdf` | PDF 277–293 | giữ, sửa cục bộ | Kiểm chứng ViT, BERT, mã hóa–giải mã, GPT và LLM; L12-14–17 được viết lại trực tiếp từ PDF 284–288. |
| `hocsau_draft.pdf` | PDF 327–333 | giữ | L12-07 và X01 về tinh chỉnh bộ mã hóa. |
| `hocsau_draft.pdf` | PDF 352–359 | giữ, đổi thành tình huống | L12-36 đặt tình huống trợ lý tuyển sinh để sinh viên chọn rủi ro, phép kiểm và hành động; đáp án mẫu chỉ nằm trong `note-for-author.md`. |
| `hocsau_draft.pdf` | PDF 312–314 | không dùng | Dải này không hỗ trợ các khẳng định đa phương thức đã có trong bản cũ; mọi dẫn chiếu tương ứng đã bị xóa. |
| Radford và cộng sự (2021), CLIP | PDF 1–3, Hình 1 và Hình 3 | giữ, tách, vẽ lại | L12-21 định nghĩa mô hình đa phương thức rồi dùng CLIP làm trường hợp cụ thể; L12-22–23 tách hai bộ mã hóa, loss đối xứng và phân loại zero-shot; L12-26 nối ViT như một lựa chọn nhánh ảnh; X03 dùng phép tính $N=2$ tự dựng. Không dùng benchmark, quy mô dữ liệu hoặc mô tả CLIP như mô hình sinh. |

Không dùng `lec17_vision_transformers.pdf` PDF 29–77, slide detection, diffusion hoặc nguồn web. Ba sơ đồ CLIP được vẽ lại thành SVG; không trích ảnh raster từ bài báo.

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $N,T_s,T_t,V,D$ | cỡ lô, độ dài nguồn, độ dài đích, kích thước từ vựng, chiều mô hình |
| $Y^{in},Y^{out}$ | chuỗi đích dịch một vị trí, cùng kích thước $N\times T_t$ |
| $H^{enc},H^{dec}$ | biểu diễn nguồn và biểu diễn đích |
| $Z^{CLM},Z^{tgt},Z^{cls}$ | điểm chưa chuẩn hóa cho dự đoán kế tiếp, chuỗi đích và phân loại ảnh |
| $E_I,E_T\in\mathbb R^{N\times D}$ | biểu diễn ảnh và văn bản đã chuẩn hóa theo hàng trong CLIP |
| $S=E_IE_T^\top/\tau$ | ma trận điểm tương đồng ảnh–văn bản, $\tau>0$; hàng là ảnh, cột là văn bản |
| $\mathcal L_{I\to T},\mathcal L_{T\to I}$ | trung bình log-softmax theo hàng của $S$ và $S^\top$; $\mathcal L_{CLIP}$ là trung bình hai hướng |
| $E_T^{cls}\in\mathbb R^{K\times D},\ Z\in\mathbb R^{N\times K}$ | biểu diễn câu nhắc lớp và điểm lớp zero-shot; ký hiệu $Z$ được giữ riêng cho điểm lớp |
| $\Omega$ | tập vị trí MLM hợp lệ và được phép chọn, $|\Omega|>0$ |
| $M^{valid},M^{causal},M^{tgt}$ | mặt nạ hợp lệ, nhân quả và vị trí đích chịu giám sát |
| $X\in\mathbb R^{N\times C\times H\times W}$ | ảnh theo thứ tự NCHW |
| $P,T_p$ | cạnh mảnh và số mảnh $(H/P)(W/P)$ |
| $H_a$ | số đầu chú ý; tỷ số chi phí ở L12-33 chỉ xét phần tự chú ý theo chiều chuỗi |
| $Z_0,Z_\ell$ | chuỗi ViT trước và sau khối thứ $\ell$; CLS cuối đi vào đầu lớp độc lập hoặc phép chiếu–chuẩn hóa tạo $E_I$ cho CLIP |

## Bài tập 50 phút

1. So sánh ba họ theo luồng thông tin, mặt nạ và mục tiêu — 10 phút.
2. Dựng mặt nạ Boolean và dạng cộng cho nguồn/đích, tách mặt nạ chú ý khỏi mặt nạ giám sát — 10 phút.
3. Tính kích thước ViT từ NCHW đến điểm phân loại và kiểm tra trục softmax — 10 phút.
4. Động não dự án cuối kỳ dùng kiến trúc Transformer hoặc LLM có sẵn; đánh giá tính khả thi và sáng tạo — 20 phút.

Hoạt động thứ tư thực hiện yêu cầu trong DOCX Buổi 12. Sản phẩm, tiến trình và thang chấm được ghi riêng trong `note-for-author.md`; không đưa chỉ dẫn nội bộ lên trang chiếu hoặc ghi chú diễn giả.
