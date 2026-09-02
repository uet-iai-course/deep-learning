# Bài 11 — Kiến trúc Transformer

## Phạm vi và trạng thái

- 41 trang lõi L11-00–40, 100 phút.
- 4 trang mở rộng L11-X01–X04 trong một stack dọc, 20 phút.
- Bài tập 50 phút tách riêng: 40 phút tính toán và 10 phút phòng máy với API chính thức của PyTorch 2.13.
- Khoảng trống nguồn cho phần phòng máy đã được xử lý bằng hai tài liệu PyTorch được người dùng duyệt ngày 27-08-2026.

## Kết quả học tập

- LLO21: trình bày luồng bộ mã hóa và bộ giải mã Transformer.
- LLO22: giải thích tự chú ý, chú ý nhiều đầu và mã hóa vị trí bằng kích thước và phép tính cụ thể.
- Sản phẩm kiểm chứng: truy vết $Q,K,V\to QK^\top/\sqrt{d_k}\to$ mặt nạ $\to$ softmax theo khóa $\to AV$; truy vết $H^{src}_0\to H^{enc}$; xác định đầu vào và nguồn Q/K/V của ba nhánh trong một tầng giải mã.

## Mạch nội dung

1. Giới hạn xử lý tuần tự và cầu nối từ chú ý chéo sang tự chú ý.
2. Trace tự dựng $B=1,T=3,D=4,d_k=d_v=2$ cho đầu 1.
3. Mặt nạ nhân quả, mặt nạ khóa đệm, hàng bị chặn hoàn toàn và ba loại chú ý.
4. Đầu 2, ghép đầu, chiếu ra và số tham số.
5. Mã hóa vị trí, FFN, đường dư, dropout, LN và khối chuẩn hóa sau.
6. Truy hồi từng tầng của bộ mã hóa/bộ giải mã, đầu ra sau $L_{enc}/L_{dec}$ tầng, dịch chuỗi đích, điểm từ vựng, sai số và huấn luyện–suy luận.
7. Bốn phép kiểm mở rộng về đối xứng hoán vị, chi phí theo $T^2$, số tham số và cấu trúc vị trí tương đối; toàn bộ mạch có thể cắt.

## Ánh xạ nguồn

| Nguồn | Dải | Quyết định | Trang đích |
|---|---:|---|---|
| DOCX, Buổi 11 | tên buổi, LLO21–22 | giữ | L11-00–01 khóa phạm vi. |
| `lec15_attention.pdf` | PDF 28–30 | giữ, gộp | L11-02: vấn đề chuỗi và động cơ thay đường xử lý tuần tự. |
| `lec15_attention.pdf` | PDF 31–35 | giữ, tách, sửa | L11-03–14: cầu nối sang tự chú ý, QKV, tích vô hướng, scale, softmax và $AV$; sửa trục softmax thành trục khóa. |
| `lec15_attention.pdf` | PDF 36 | giữ, gộp | L11-X01: dùng tính tương đương hoán vị để làm rõ động cơ thêm vị trí; liên hệ phát biểu mở ở L11-30. |
| `lec15_attention.pdf` | PDF 37–39 | giữ, tách | L11-15–18: tự chú ý nhân quả và ví dụ số. |
| `lec15_attention.pdf` | PDF 40 | giữ, gộp | L11-19–24: tổng kết ba loại chú ý. |
| `lec15_attention.pdf` | PDF 41 | bỏ | Hình minh họa và liên kết ngoài không cần cho LLO. |
| `lec15_attention.pdf` | PDF 42 | giữ, vẽ lại | L11-36–37: kiến trúc encoder–decoder tổng thể. |
| `lec15_attention.pdf` | PDF 43 | giữ, bổ sung số | L11-30–31: mã hóa vị trí sin–cos, nối với $D=4$. |
| `lec15_attention.pdf` | PDF 44 | giữ, tách | L11-25–29: chú ý nhiều đầu, đầu 2, ghép và chiếu. |
| `lec15_attention.pdf` | PDF 45 | giữ, sửa | L11-32–35: FFN, đường dư, LayerNorm và chuẩn hóa sau. |
| `lec15_attention.pdf` | PDF 46 | giữ, vẽ lại | L11-36–37: kiến trúc Transformer đầy đủ. |
| `lec15_attention.pdf` | PDF 47 | bỏ | Kết quả thực nghiệm không cần cho LLO21–22 và thiếu giao thức để phân tích trong thời lượng. |
| `lec15_attention.pdf` | PDF 48 | giữ, giới hạn | L11-02 và X02: song song hóa, đường truyền và chi phí bậc hai; không suy thành ưu thế tuyệt đối. |
| `lec16_transformer.pdf` | PDF 4–17 | giữ, gộp | L11-03 và L11-15–24: cầu nối, ba loại chú ý, công thức và mặt nạ; PDF 17 dùng cho giới hạn chi phí. |
| `lec16_transformer.pdf` | PDF 22 | giữ, khai triển | L11-30–31 về mã hóa vị trí; X04 về phép quay theo độ lệch vị trí. |
| `lec16_transformer.pdf` | PDF 26 | giữ | L11-25–29 về chú ý nhiều đầu. |
| `lec16_transformer.pdf` | PDF 28 | giữ | L11-32 về FFN. |
| `lec16_transformer.pdf` | PDF 33 | giữ, sửa | L11-34: thêm căn phương sai và $\varepsilon>0$. |
| `lec16_transformer.pdf` | PDF 36 | giữ, vẽ lại | L11-36–37: kiến trúc Transformer đầy đủ. |
| `hocsau_draft.pdf` | PDF 263–270 | giữ, kiểm chứng | QKV, scale, trục khóa, đầu ra chú ý, chi phí, mã hóa vị trí, quan hệ vị trí tương đối và chú ý nhiều đầu. |
| `hocsau_draft.pdf` | PDF 271–276 | giữ, kiểm chứng | FFN, đường dư, LayerNorm, encoder/decoder, dịch nhãn và mục tiêu chuỗi. |
| `pytorch-scaled-dot-product-attention.html` | chữ ký API, quy ước kích thước, mặt nạ Boolean, `dropout_p` | thêm, giới hạn | BT11-04: tính thủ công điểm/scale/mask/softmax/$AV$ trên $Q,K,V:B\times H_a\times T\times d_h$, rồi kiểm bằng SDPA và `assert_close`; `True` cho phép vị trí tham gia; đặt `dropout_p=0.0` khi đánh giá. |
| `pytorch-multihead-attention.html` | `batch_first`, mặt nạ Boolean, kích thước đầu ra | thêm, giới hạn | BT11-04: đối chiếu MHA với đầu vào $B\times T\times D$; `True` chặn vị trí; kiểm tra đầu ra và trọng số theo từng đầu. |

Không dùng `lec16_transformer.pdf` PDF 18–20, 23–25, 27, 29–32, 34–35, 38–48. Hai bản HTML PyTorch cục bộ chỉ dùng cho phòng máy; không dùng phần kernel tối ưu, benchmark hoặc GQA và không dùng nguồn web khác.

## Ký hiệu và trace

| Ký hiệu | Nghĩa |
|---|---|
| $B$ | cỡ lô; $B=1$ trong trace, còn $n$ chỉ là chỉ số một mẫu |
| $T,T_q,T_k,T_s,T_t$ | độ dài chung, truy vấn, khóa, nguồn và đích |
| $D,d_k,d_v,D_{ff},H_a$ | chiều mô hình, khóa, giá trị, FFN và số đầu |
| $Q,K,V,S,A,O,O_{MHA}$ | truy vấn, khóa, giá trị, điểm đã scale, trọng số, đầu ra chú ý và đầu ra sau chiếu nhiều đầu |
| $B_M$ | mặt nạ cộng $0/-\infty$; trước L11-25 có shape $B\times T_q\times T_k$, sau đó thêm trục đầu đơn vị |
| $X$ | trace $3\times4$ với ba hàng $[1,0,1,0]$, $[0,1,0,1]$, $[1,1,0,0]$ |
| $H_0^{src},H_0^{tgt},H^{enc},H^{dec}$ | đầu vào đầy đủ và trạng thái cuối của bộ mã hóa/bộ giải mã |
| $H^{src}_\ell,G_\ell,L_{enc},L_{dec}$ | trạng thái sau tầng mã hóa/giải mã thứ $\ell$ và số tầng của hai bộ |
| $Z,W_{vocab},b_{vocab},|V_{tgt}|$ | điểm từ vựng, tham số chiếu và kích thước từ vựng đích |

## Bài tập 50 phút

1. BT11-01: tính đầy đủ phép chú ý cho trace $B=1,T=2,D=d_k=d_v=2$, với $X$ và các ma trận chiếu được cho — 20 phút, có đề, sản phẩm và rubric trong `note-for-author.md`.
2. BT11-02: dựng mặt nạ nhân quả kết hợp khóa đệm cho hai chuỗi có độ dài hợp lệ 3 và 2 — 10 phút, có đề, sản phẩm và rubric.
3. BT11-03: truy vết kích thước hai đầu với $B=2,T=5,D=8,H_a=2$ tới phép ghép và chiếu ra — 10 phút, có đề, sản phẩm và rubric.
4. BT11-04: kiểm chứng phép chú ý thủ công bằng `scaled_dot_product_attention`, rồi khảo sát `MultiheadAttention` — 10 phút: dự đoán, đọc hợp đồng API, chạy mã, `assert_close`, rồi đối chiếu kích thước, mặt nạ Boolean và chế độ đánh giá. Không so đầu ra SDPA với đầu ra MHA vì dữ kiện và phép chiếu khác nhau. Thử thay đổi `batch_first` là phần tùy chọn có điểm thưởng. Đề, mã, đầu ra dự kiến, sản phẩm, đáp án và rubric nằm trong `note-for-author.md`.

BT11-01 → BT11-04 tạo một tuyến tái áp dụng hợp đồng và kỹ năng: tính Q/K/V và softmax → dựng mặt nạ nhân quả → truy vết kích thước nhiều đầu → kiểm chứng bằng hai API. Mỗi bài dùng dữ kiện riêng, không truyền cùng tensor sang bài sau.

Bài tập về nhà theo DOCX: giải thích bộ mã hóa xử lý một câu từ nhúng và vị trí đến trạng thái đầu ra; đề và rubric nằm trong `note-for-author.md`.
