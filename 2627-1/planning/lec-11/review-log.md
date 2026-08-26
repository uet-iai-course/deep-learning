# Nhật ký rà soát — Bài 11

## Trạng thái

- Deck trình chiếu: 41 trang lõi/100 phút + 4 trang mở rộng/20 phút.
- Bài tập: đủ 50 phút, gồm 40 phút tính toán và 10 phút phòng máy có nguồn PyTorch 2.13 được duyệt.
- Lỗi chặn về nguồn phòng máy đã được xử lý; kiểm định RevealJS, PyTorch và bốn lượt phản biện cuối đều đạt. Bài đủ điều kiện cập nhật index, commit và push; giới hạn Codex Slides được ghi riêng trong nhật ký.

## Quyết định học thuật và sửa lỗi nguồn

| Vùng | Vấn đề nguồn | Quyết định |
|---|---|---|
| L11-10 | Slide ghi `softmax(..., dim=1)` theo bố cục minh họa, mơ hồ khi chuyển sang tensor. | Khóa trục cuối là khóa $T_k$; hàng là truy vấn, cột là khóa. |
| L11-34 | Slide LN dùng ký hiệu độ lệch chuẩn/phương sai không nhất quán và thiếu căn, epsilon. | Dùng $\sqrt{\sigma^2+\varepsilon}$, $\varepsilon>0$, chuẩn hóa theo $D$ cho từng mẫu/vị trí. |
| L11-36 | Slide nguồn có một cấu hình số nhưng nguồn duyệt không đủ để sửa hoặc chuẩn hóa cấu hình đó. | Bỏ hoàn toàn claim cấu hình khỏi deck; chỉ giữ phát biểu số tầng và số đầu là siêu tham số. |
| L11-35 | Nguồn chính dùng Add & Norm sau mỗi nhánh. | Giữ chuẩn hóa sau xuyên B11; xóa nội dung pre-norm ngoài nguồn khỏi X04. |
| L11-09–11,23 | Bản trước đưa trục đầu vào mặt nạ trước khi giới thiệu MHA, khiến phép cộng giữa tensor ba và bốn chiều không nhất quán. | Trước L11-25 dùng $S,B_M,A:B\times T_q\times T_k$ và $(B_M)_{n,i,j}$; từ L11-25 mới mở mặt nạ thành $B\times1\times T_q\times T_k$ để phát qua $H_a$ đầu. |
| L11-38–39 | Ký hiệu $A,V$ cho điểm từ vựng xung đột với trọng số chú ý và tensor giá trị. | Dùng $Z$, $W_{vocab}$, $b_{vocab}$, $|V_{tgt}|$; thêm log-sum-exp ổn định và CE có mặt nạ với mẫu số dương. |
| L11-23–38 | Trích dẫn trang nguồn bị lệch giữa positional/MHA/FFN/LN/kiến trúc đầy đủ. | Đối chiếu lại trang thật: `lec15` PDF 43–47 và `lec16` PDF 22, 26, 28, 33, 36; PDF 47 của `lec15` là kết quả và không dùng. |
| L11-25–31 | Mạch deck đặt chú ý nhiều đầu trước mã hóa vị trí, khác thứ tự nguồn. | Giữ thứ tự này để hoàn tất phép tính hai đầu trên $X$ thô trước; sau đó mới tạo đầu vào đầy đủ $H_0=X+PE$. Cách cô lập này tránh đổi số giữa trace MHA và trace vị trí. |
| L11-X04 | So sánh pre-norm/post-norm không có nguồn duyệt trong phạm vi B11. | Xóa và thay bằng quan hệ độ lệch của mã hóa sin–cos từ `lec16` PDF 22 và GT PDF 268. |
| L11-X04 | Ma trận quay in tại GT PDF 268 có dấu không khớp quy ước $[\sin(p\omega),\cos(p\omega)]$ ngay trước đó. | Giữ kết luận có nguồn rằng phép biến đổi chỉ phụ thuộc độ lệch; sửa dấu bằng cách tự kiểm hai công thức cộng góc và ghi ma trận đúng trong deck. |
| L11-28,31,36–37 | Hậu kiểm phát hiện va ký hiệu, thiếu trục lô trong chỉ số và đường dư chưa hiện rõ trên SVG. | Đổi đầu ra nhiều đầu thành $O_{MHA}$; dùng $H_0[0,0,:]$; thêm Dropout vào mọi nhánh và vẽ hai/ba mũi tên dư tới đúng hộp Cộng+LN. |
| BT11-04 | DOCX yêu cầu khảo sát mã cài đặt tự chú ý nhưng các slide và giáo trình ban đầu không có mã hoặc hợp đồng API. | Người dùng duyệt hai tài liệu PyTorch 2.13 ngày 27-08-2026. Dùng SDPA và MHA để kiểm tra kích thước, `batch_first`, mặt nạ Boolean đối nghịch và dropout khi đánh giá. |
| BT11-04 | SDPA và MHA diễn giải `True` khác nhau trên mặt nạ Boolean. | Dùng `keep_mask` cho SDPA và `block_mask = ~keep_mask` cho MHA; yêu cầu sinh viên giải thích phép phủ định thay vì chỉ chạy mã. |
| BT11-04 | SDPA luôn áp dụng dropout theo `dropout_p`, không tự đọc trạng thái `eval()` của mô-đun gọi. | Đặt `dropout_p=0.0` cho SDPA trong lần chạy đánh giá; cấu hình dropout của MHA là `0.1` nhưng gọi `eval()` để tắt khi đánh giá. |
| BT11-01–04 | Bản lab chưa chỉ rõ dữ kiện nào được truyền từ ba bài tính toán sang bài chạy API. | Khóa tuyến sản phẩm: phép tính Q/K/V và softmax → mặt nạ → kích thước nhiều đầu → bản ghi chạy SDPA/MHA. |
| BT11-04 | Bốn yêu cầu ban đầu khó hoàn tất trong 10 phút nếu vừa cài môi trường vừa thử đổi `batch_first`. | Chốt nhịp 1–2–4–3 phút; chuyển thử `batch_first=False` thành tùy chọn và yêu cầu chuẩn bị sẵn PyTorch 2.13 trên CPU trước lớp. |
| L11-27 | $O^{(2)}$ được tính từ trọng số đầy đủ nhưng hiển thị $.751/.496$, không khớp làm tròn ba chữ số. | Sửa thành $.752/.497$ và ghi rõ chỉ làm tròn sau phép nhân. |
| L11-36–37 | Công thức cũ chỉ mô tả một khối từ $H_0$ tới đầu ra nên chưa cho thấy truy hồi qua nhiều tầng hoặc đầu ra sau $L_{enc}/L_{dec}$. | Dùng $H^{src}_{\ell-1}\to H^{src}_\ell$, $G_{\ell-1}\to G_\ell$; định nghĩa $H^{enc}=H^{src}_{L_{enc}}$, $H^{dec}=G_{L_{dec}}$. SVG ghi lặp tầng và Bỏ ngẫu nhiên trên từng nhánh. |
| L11-38 | Công thức LSE chiếm chỗ nhưng cặp chuỗi dịch nhãn vẫn trừu tượng. | Thêm `[BOS,tôi,học]`/`[tôi,học,EOS]`; giữ loss log-softmax có mặt nạ trên slide và chuyển khai triển LSE ổn định vào notes. |
| BT11-04 | Lab cũ chỉ đối chiếu hai API nên chưa kiểm chứng phép tính tay với SDPA trên cùng dữ kiện; MHA có phép chiếu riêng nên đầu ra không thể so trực tiếp với SDPA. | Thêm nhánh thủ công điểm→scale→mask→softmax→$AV$, dùng cùng Q/K/V/mặt nạ với SDPA và `torch.testing.assert_close`. Giữ MHA để khảo sát giao diện/mặt nạ, dùng `inference_mode`, cấm so hai đầu ra; `batch_first` là điểm thưởng. |

## Xử lý bốn báo cáo độc lập

- Sửa ký hiệu đầu ra từ vựng, hàm mất mát ổn định và mặt nạ ký hiệu tại L11-38.
- Mở rộng L11-36–37 thành trace đầy đủ của bộ mã hóa và bộ giải mã; hai SVG ghi rõ từng lần Cộng+LN.
- Tổng quát hóa MHA tại L11-25 và nối trực tiếp nguồn Q/K/V của chú ý chéo tại L11-37.
- Chuyển công thức sin–cos sang L11-30; L11-31 giữ ví dụ số, sửa chỉ số thành $H_0[0,0,:]$, nối $H_0$ với Q/K/V và thêm câu hỏi kích thước.
- Thống nhất ký hiệu mặt nạ trước/sau khi có trục đầu; thêm giả thiết cho lập luận phương sai và shape của $\gamma,\beta$.
- Tăng `.small` từ `.84em` lên `.88em`, tương đương khoảng `.757em` so với cỡ Reveal gốc khi slide dùng `.86em`.
- Viết đủ đề, dữ kiện, sản phẩm, rubric và đáp án cho 40 phút bài tập có nguồn; thêm bài tập về nhà theo DOCX.
- Bản rà trước giữ nguyên lỗi chặn phòng máy 10 phút vì khi đó chưa có nguồn code/API được duyệt.

## Sai khác có chủ ý

- Trace $B=1,T=3,D=4,d_k=d_v=2$, hai bộ ma trận chiếu và mọi kết quả số đều do deck tự dựng để minh họa công thức; không phải bằng chứng thực nghiệm.
- Chọn $W_O=I_4,b_O=0$ để trace ghép đầu có thể kiểm tay.
- Vẽ lại 12 sơ đồ kỹ thuật bằng SVG; không sao chép raster hoặc hình phụ thuộc mạng.
- Bỏ trang kết quả nguồn và các trang ngoài dải đã duyệt.
- Trước ngày 27-08-2026, không tạo mã hoặc giả mã cho phòng máy vì nguồn chưa đủ. Sau khi người dùng duyệt nguồn PyTorch, bổ sung mã tối thiểu theo đúng hợp đồng API và giữ quyết định cũ làm dấu vết.
- Mã lab tự dựng tensor đầu vào nhỏ để kiểm tra API; không trình bày kết quả như bằng chứng thực nghiệm.
- Phạm vi nguồn PyTorch chỉ gồm chữ ký API, kích thước, mặt nạ, `batch_first`, `is_causal`, `dropout_p` và đầu ra. Lab không dùng kernel tối ưu, benchmark hoặc GQA.
- Ví dụ MHA dùng $X$ để cô lập cơ chế; tầng Transformer đầy đủ bắt đầu bằng $H_0=X+PE$. Lý do này được nêu trên L11-31 và trong storyboard.
- Đầu ra sau chiếu nhiều đầu dùng $O_{MHA}$ để không va với $Y^{in},Y^{out}$ của chuỗi đích.
- Không áp đặt cách triệt truy vấn đệm theo tầng vì nguồn duyệt chỉ đủ cho mặt nạ khóa và loại ký hiệu đệm khỏi sai số.

## Rà no-ai-slop và Quill

- Mỗi trang giữ một luận điểm; thuật ngữ truy vấn/khóa/giá trị, điểm/trọng số/đầu ra được dùng nhất quán; $A$ chỉ là trọng số chú ý và $Z$ chỉ là điểm từ vựng.
- Các chu trình đi từ vấn đề và trace số đến công thức, triển khai và kiểm tra.
- BT11-04 nối trực tiếp hợp đồng tensor ở L11-20/23/25 với hai API; thuật ngữ `keep_mask` và `block_mask` giữ nguyên từ đề đến mã, đầu ra và rubric.
- Bốn bài tập dùng một tuyến sản phẩm liên tục; BT11-04 kiểm tra bằng API các phép tính, mặt nạ và kích thước đã tạo ở BT11-01–03.
- Không có chỉ dẫn người soạn, timing, tuyến cắt hoặc đáp án trong mặt slide/notes.
- Không tạo `quill.json`.

## Kiểm định tĩnh

- HTML có 45 ID duy nhất, 45 ghi chú nguồn và cấu trúc section cân bằng.
- Storyboard có đúng 45 hàng theo cùng thứ tự ID; timing tính lại là lõi 100 phút và mở rộng 20 phút.
- KaTeX strict dựng thành công 160 biểu thức với `throwOnError: true`, `strict: "error"`.
- Mọi CSS/JS/SVG được tham chiếu đều là tài nguyên cục bộ và tồn tại; không có raster hoặc phụ thuộc mạng.
- 12/12 SVG hợp lệ XML, có `role="img"`, `title`, `desc`; cỡ chữ khai báo nhỏ nhất 24 px.
- `convert` và `montage` dựng lại thành công hai SVG encoder/decoder sau sửa; đã xem montage, sửa nhãn encoder bị đè đường dư. Hai tệp vẫn hợp lệ XML và giữ nhãn chính 34 px/32 px; nhãn Bỏ ngẫu nhiên nhỏ nhất 25 px trong SVG decoder.
- Không có control byte, tiêu đề chứa thuật ngữ nội bộ bị cấm hoặc `quill.json`.
- Runtime BT11-04 mới: **PASS** bằng PyTorch 2.13.0+cpu trên CPU. `torch.testing.assert_close` xác nhận phép tính thủ công khớp SDPA; bốn kích thước và hai ma trận mặt nạ khớp đầu ra dự kiến. Cảnh báo thiếu NumPy trong môi trường kiểm thử tối giản không ảnh hưởng đoạn mã hoặc kết quả.
- Bản in Reveal phát hiện L11-31 tràn sang một trang PDF riêng cho hộp Câu hỏi, làm tổng PDF thành 46 trang. Giữ nguyên cỡ chữ, ID và timing; giới hạn hình `positional-encoding.svg` ở chiều cao 210 px để nội dung nằm lại trên một trang chiếu.
- Môi trường phòng máy vẫn phải qua preflight PyTorch 2.13 trên CPU trước giờ học; thời gian cài đặt không tính vào 10 phút lab.
- Chromium in Reveal ở khung 1280×720 cho đúng 45 trang sau vá L11-31; đã rà toàn bộ contact sheet, không có tràn, chồng lấn hoặc cắt nội dung. Ảnh chụp khung hẹp 900×720 của L11-31, L11-36, L11-37 và L11-38 đều đọc được, không bị cắt.
- Đã tạo Codex Slides project shell `20260826234600-b-i-11-ki-n-tr-c-transformer-8nca`, nhưng mọi lần tải Design File đều lỗi HTTP 500; log ghi `ReferenceError: File is not defined` tại files route. Đây là lỗi runtime/plugin Node, nên chưa có bằng chứng kiểm định hiển thị trong Codex Browser.

## Hậu kiểm chỉnh sửa storyboard

- Đã đối chiếu lại citation trong L11-23–38 và hai trang lân cận: `lec15` PDF 43 positional, 44 MHA, 45 khối Transformer, 46 kiến trúc đầy đủ, 47 kết quả không dùng; `lec16` PDF 22 positional, 26 MHA, 28 FFN, 33 LayerNorm, 36 kiến trúc đầy đủ.
- Đã chuẩn hóa $B$ là ký hiệu cỡ lô trong HTML, SVG và planning; $n$ chỉ còn là chỉ số mẫu, còn $L$ là số tầng trong sơ đồ encoder.
- Bộ phân tích XML chuẩn của Python đọc thành công 12/12 SVG; môi trường không có `xmllint`.

## Lịch sử xử lý nguồn phòng máy

- Bản nháp đầu ghi trạng thái **CHƯA ĐẠT** và không tự chọn thư viện, vì nguồn được duyệt khi đó không có code/API.
- Ngày 27-08-2026, người dùng duyệt tài liệu chính thức PyTorch 2.13 về `scaled_dot_product_attention` và `MultiheadAttention`; hai bản HTML được lưu cục bộ trong `source-materials/resources/` và ánh xạ trong `source.md`.
- Sau phê duyệt, BT11-04 được bổ sung vào bốn tệp planning. Khoảng trống nguồn 10 phút đã đóng; HTML/SVG/index không thuộc lượt sửa này.

## Xử lý vòng bốn báo cáo mới

- Chuyên gia/storyboard: làm rõ truy hồi và đầu ra cuối của $L_{enc}/L_{dec}$ tầng tại L11-36–37; giữ nguyên ID và 4+4 phút.
- Toán học/triển khai: sửa làm tròn L11-27; đổi BT11-04 thành kiểm chứng thủ công≈SDPA trên cùng dữ kiện và tách MHA khỏi phép so sánh đầu ra.
- Góc nhìn sinh viên: thêm cặp chuỗi cụ thể ở L11-38, chuyển khai triển LSE vào notes và biến `batch_first=False` thành điểm thưởng.
- Học thuật/giảng dạy: giữ mạch chuẩn hóa sau của Transformer gốc, bổ sung nhãn lặp tầng và Bỏ ngẫu nhiên trong hai SVG thay vì thêm trang.
- QA sau sửa: runtime BT11-04 đã PASS; montage hai SVG đã rà; Chromium print 1280×720 cho đúng 45 trang và contact sheet không có lỗi hiển thị; L11-31/L11-36–38 ở 900×720 đọc được, không bị cắt. Kiểm định Codex Browser chưa hoàn tất do lỗi HTTP 500 của tuyến tải Design File, không phải lỗi deck.
