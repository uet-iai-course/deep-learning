# Nhật ký rà soát Bài 08

## Quyết định nguồn và phạm vi

| Quyết định | Bằng chứng và lý do |
|---|---|
| Giữ mạch xây LSTM từng thành phần | `lec14_rnn.pdf` 25–32 xây ô theo từng bước và giới thiệu cổng ra trước cổng quên. Bản deck giữ thứ tự này để bám mạch nguồn; sơ đồ ô hoàn chỉnh sau cùng được sửa để thể hiện đúng $C_{t-1}\odot F_t+G_t\odot I_t\to C_t\to\tanh\to H_t$. |
| Cầu nối gradient dùng Bài 07 và PDF 25 | Bỏ tham chiếu trực tiếp `lec14_rnn.pdf` PDF 23; Bài 07 đã thiết lập tích Jacobian co/giãn, còn PDF 25 mở động cơ LSTM. |
| Dùng GT để bổ sung GRU | Slide chính chỉ có PDF 33; GT PDF 229–232 cung cấp kích thước, phát tự động và phương trình ma trận đầy đủ. |
| Dùng 35–40 cho nhiều tầng và hai chiều | Đúng dải phụ được `source.md` khóa; không lấy phần kiến trúc ngoài dải. |
| Dùng 58–59 và GT 239–243 cho dịch máy | Đủ để giới thiệu bộ mã hóa–giải mã, học theo đáp án và mặt nạ; không dùng số liệu GNMT ở 60–62 vì không cần cho LLO. |
| Dùng GT 315–317 cho phân tích cảm xúc | Nguồn đã ánh xạ vai trò ví dụ ứng dụng; đặt trong tuyến mở rộng. |
| Không tạo demo phân tích cảm xúc | GT 315–317 mô tả kiến trúc và ví dụ nhưng không có code để chuyển; người dùng không yêu cầu demo. Bài tập 50 phút dùng tính tay và phân tích. |
| Chia deck thành bảy mạch ngoài | Giữ đúng các nhóm L08-00–06, 07–17, 18–21, 22–29, 30–33, 34–38 và X01–X04 rồi 39. Mạch cuối có nhánh mở rộng và kết luận chung, không đổi 44 trang. |
| Khóa tuyến lõi và tuyến đầy đủ bằng bàn phím | Reveal có thể giữ chỉ số dọc khi đi ngang giữa các mạch. Vì vậy, phím Phải được ánh xạ tại sáu ranh giới 06→07, 17→18, 21→22, 29→30, 33→34, 38→X01; phím End luôn đến L08-39. Tuyến lõi dùng End tại L08-38, tuyến đầy đủ đi Phải rồi xuống X01–X04–39. |

## Sai khác và mâu thuẫn đã xử lý

- Slide chính dùng $H_t=(1-Z_t)\odot H_{t-1}+Z_t\odot\widetilde H_t$, nên $Z_t$ gần 1 ghi ứng viên mới.
- GT PDF 231 dùng $H_t=Z_t\odot H_{t-1}+(1-Z_t)\odot\widetilde H_t$, nên $Z_t$ gần 1 giữ trạng thái cũ.
- Bản deck giữ quy ước slide chính vì slide quyết định mạch và ký hiệu trong phạm vi buổi. L08-27 ghi hai phương trình và ánh xạ $Z_{slide}=1-Z_{GT}$. Vì $\sigma(-a)=1-\sigma(a)$, cùng một hàm cổng còn đòi hỏi đổi dấu tiền kích hoạt, trọng số và độ lệch; không giữ nguyên $Z$/weights rồi đổi nghĩa.
- Mệnh đề của slide PDF 25 về “tránh gradient suy giảm” được thu hẹp thành “thêm nhánh trực tiếp có hệ số cổng quên”. L08-18–21 phân biệt đạo hàm nhánh với đạo hàm toàn phần và không tuyên bố LSTM loại bỏ gradient triệt tiêu.
- Bổ sung trạng thái đầu, thiết bị, phát tự động và mặt nạ từ GT vì thiếu chúng sẽ làm công thức theo lô hoặc triển khai mơ hồ. Mặt nạ nguồn giữ trạng thái; mặt nạ đích chỉ chọn token trong mất mát.
- Chọn mô hình cơ sở GRU cho cả bộ mã hóa và bộ giải mã. $Q_n=H_{L_n}^{enc,(n)}$ chỉ khởi tạo $S_0$; không chèn lại $Q$ ở mỗi bước.
- Phép đếm tham số giả sử đúng phương trình của bài với một độ lệch cho mỗi phép affine/cổng; không khẳng định mọi API đóng gói độ lệch giống nhau.
- `lstm-cell.svg` được sửa luồng dữ liệu: $C_{t-1}$ nhân $F_t$, $G_t$ nhân $I_t$, hai nhánh cộng thành $C_t$, rồi $\tanh(C_t)$ nhân $O_t$ để tạo $H_t$.
- Năm báo cáo đều nhắc hoặc đánh dấu L08-36 dùng $P_{t'}=\operatorname{softmax}_V(A_t)$, nhưng bản HTML tại thời điểm chỉnh sửa đã dùng đúng $P_{t'}=\operatorname{softmax}_V(A_{t'})$. Đây là false positive do báo cáo không phản ánh bản hiện tại; giữ công thức đúng và không đổi ngược.
- Rút $D_s=D_h$ khỏi L08-36 vì $D_s$ không được dùng ở nơi khác. Giữ các kích thước cần cho phép cập nhật và đầu ra; định nghĩa $D_e$ là chiều vector nhúng token đích, độc lập với $D_h$.
- Không sửa liên kết phím Phải hoặc End dựa trên suy đoán về xử lý sự kiện. Kiểm chứng sáu ranh giới và đích End ở bước runtime; chỉ sửa nếu trình duyệt cho thấy điều hướng kép hoặc sai đích.

## Tự tính ví dụ

### LSTM

| Đại lượng | Giá trị đầy đủ | Hiển thị |
|---|---:|---:|
| $I_t=\sigma(0.2)$ | 0.5498339973 | 0.5498 |
| $F_t=\sigma(1.0)$ | 0.7310585786 | 0.7311 |
| $O_t=\sigma(-0.4)$ | 0.4013123399 | 0.4013 |
| $G_t=\tanh(0.6)$ | 0.5370495670 | 0.5370 |
| $C_t=F_t(0.3)+I_tG_t$ | 0.5146056838 | 0.5146 |
| $\tanh(C_t)$ | 0.4735259488 | 0.4735 |
| $H_t=O_t\tanh(C_t)$ | 0.1900318065 | 0.1900 |

### GRU theo quy ước slide

| Đại lượng | Giá trị đầy đủ | Hiển thị |
|---|---:|---:|
| $R_t=\sigma(0.3)$ | 0.5744425168 | 0.5744 |
| $Z_t=\sigma(0.7)$ | 0.6681877722 | 0.6682 |
| $x_t+R_th_{t-1}$ | 0.3851114966 | 0.3851 |
| $\widetilde h_t$ | 0.3671382594 | 0.3671 |
| $h_t=(1-Z_t)h_{t-1}+Z_t\widetilde h_t$ | 0.1789548500 | 0.1790 |

Tích cổng quên ở L08-20: $0.95\cdot0.8\cdot0.9\cdot1\cdot0.7=0.4788$. Đây là hệ số của nhánh trực tiếp, không phải đạo hàm toàn phần.

Với $D_x=3,D_h=4$, cơ sở affine là $3\cdot4+4^2+4=32$; GRU có 96 và LSTM có 128 tham số trong ô theo quy ước một bias cho mỗi phép affine/cổng.

## Hợp nhất storyboard và năm phản biện

| Góc rà soát | Mức độ | Trang | Vấn đề | Quyết định sửa |
|---|---|---|---|---|
| Sinh viên | nghiêm trọng | L08-18,28–29,36,X02 | Báo lỗi chỉ số softmax; L36 quá tải và thiếu $D_e$; L29/X02 lặp kiểm tra số tham số | Xác nhận softmax là false positive; bỏ $D_s$, định nghĩa $D_e$; đổi L29 sang kiểm tra hệ số nhánh giữ; định vị X02 là bài áp dụng chi phí. Rủi ro phím chỉ được ghi để kiểm runtime. |
| Chuyên gia Học sâu | trung bình | L08-36,X01 | $D_e$ chưa định nghĩa; $Q$ bị dùng cho hai biểu diễn khác kích thước; báo lỗi chỉ số softmax | Định nghĩa $D_e$; đổi biểu diễn phân loại thành $u_n^{cls},U^{cls}$; giữ $P_{t'}=\operatorname{softmax}_V(A_{t'})$. |
| Toán học, thuật toán và triển khai | trung bình | L08-06,18,36 | $\widehat S_t$ chỉ có trong notes; chữ thường ở gradient chưa giải thích; báo lỗi chỉ số softmax | Định nghĩa $\widehat S_t$ trên mặt trang; giải thích chữ thường là hàng/mẫu; xác nhận công thức softmax hiện có đúng. |
| Học thuật và giảng dạy | nghiêm trọng | L08-06,20,27,34,36,X01 | Báo lỗi chỉ số softmax; ký hiệu $Q$, $D_e$, $H_-$ và $x_t/X_t$ chưa nhất quán; thiếu cầu sang BPTT | Giữ softmax đúng; đổi ký hiệu phân loại; định nghĩa $D_e$, $\widehat S_t$, $x_t\to X_t$; dùng $H_{t-1}$; nối tích cổng quên với BPTT. |
| Kết nối và mạch viết | trung bình | L08-17–20, X01–X04,39 | Kết luận chưa thu hồi rõ giới hạn gradient; nhánh mở rộng chuyển cấp đột ngột và X02 dễ lặp L08-28 | Nối kích thước sang nhánh gradient trong notes; tổ chức X01–X04 thành bốn trạm đối chiếu, xác định X02 là bước áp dụng công thức thành chi phí cụ thể; L39 khép cơ chế và giới hạn LLO16. |

- Đã rà vùng bị ảnh hưởng và hai trang lân cận: L08-04–08, L08-15–21, L08-22–31 và L08-33–39 cùng X01–X04.
- Thứ tự chu trình sau sửa: L08-15 là hoạt động trong ví dụ LSTM, L08-17 là kiểm tra cuối rồi nối sang nhánh gradient; GRU dùng dữ kiện L08-24 trước hình thức L08-25 và L08-29 kiểm tra hệ số nhánh giữ; L08-31, L08-37 và L08-39 có câu hỏi cùng fragment.
- Timing được cân lại mà không đổi tổng: L08-04 và L08-07 mỗi trang giảm 1 phút; L08-20 và L08-39 mỗi trang tăng 1 phút. Lõi giữ 100 phút, mở rộng 20 phút, bài tập 50 phút.
- Để tránh quá tải L08-36, giữ sơ đồ mã hóa–giải mã ở L08-35; bỏ $D_s$, giữ cập nhật GRU cùng các kích thước thiết yếu của nhúng, trạng thái, trọng số đầu ra và logit. $P_{t'}$ tiếp tục dùng đúng $A_{t'}$. Không thêm trang hoặc đổi timing.
- L08-X01 đổi ký hiệu biểu diễn phân loại từ $q_n,Q$ sang $u_n^{cls},U^{cls}$ để không xung đột với ngữ cảnh $Q$ của bộ mã hóa–giải mã. Bốn trang mở rộng có câu chuyển liên tiếp; X02 là phép áp dụng công thức L08-28 vào kích thước cụ thể, không lặp chức năng hình thức hóa.
- Dọn biên tập cuối: định nghĩa $\widehat S_t$ trên mặt L08-06; thay $H_-$ bằng $H_{t-1}$; phân biệt token $x_t$ với vector nhúng theo lô $X_t$; giải thích chữ thường trong công thức gradient là một hàng/mẫu; nối L08-17→18 và tích cổng quên với BPTT trong notes.
- L08-39 thu hồi LLO15–LLO16: cổng tạo nhánh lưu giữ có điều kiện, giúp giảm nhẹ nhưng không loại bỏ gradient triệt tiêu. Câu nối nhận được cả bài toán dịch máy của tuyến lõi và trạm chọn kiến trúc của tuyến đầy đủ.

## Đề xuất không áp dụng

- Không đổi công thức softmax ở L08-36 vì bản được chỉnh sửa đã dùng đúng $A_{t'}$; đổi thành $A_t$ sẽ tạo lỗi.
- Không đổi số hoặc thứ tự X01–X04. Câu chuyển và vai trò áp dụng của X02 đủ sửa bước nhảy mà không phá cấu trúc hoặc timing đã khóa.
- Không thêm ma trận nhúng đầy đủ hoặc trạng thái “tham số được học” lên L08-36. Trang chỉ cần hợp đồng đầu vào của GRU; định nghĩa $D_e$ và kích thước $E(y_{t'-1})$ đã đủ cho phép nhân, còn thêm chi tiết sẽ đi ngược mục tiêu giảm tải.
- Không thêm lại câu hỏi số tham số hay hiệu năng ở L08-29. L08-28 và X02 đã đảm nhiệm hai mức hình thức–áp dụng; L08-29 dành riêng cho hệ số nhánh giữ và giới hạn của đạo hàm trực tiếp.
- Không sửa liên kết phím trước khi có bằng chứng runtime. Giả thuyết điều hướng kép được chuyển thành mục kiểm chứng trình duyệt trong `note-for-author.md`.
- Không thêm chú giải $\odot$ trên mặt L08-09 hoặc thuật ngữ tiếng Anh “candidate” vào notes. Tích Hadamard đã được khóa là tiên quyết ở L08-01; ký hiệu và thuật ngữ “ứng viên” nhất quán trong deck và bảng ký hiệu.

## Biên tập và tài sản

- Nội dung hiển thị và ghi chú đã được biên tập theo no-ai-slop: câu trực tiếp, không khẩu hiệu, không câu hỏi tu từ, không kết luận thực nghiệm thiếu giao thức.
- Quill được dùng để rà chuỗi vấn đề → trực giác cổng → ví dụ số → phương trình → gradient → kiến trúc → ứng dụng; không tạo `quill.json`.
- Chín SVG được vẽ lại; không dùng ảnh raster, screenshot hoặc tài sản mạng.
- Rà trực quan `lstm-cell.svg` cho thấy nhãn đầu vào chung sát mép và chưa thể hiện rõ nhánh tới bốn tín hiệu. Đã dịch nhãn vào trong khung và thêm bus đầu vào tới $F_t,I_t,G_t,O_t$; luồng chính vẫn là $C_{t-1}\odot F_t+I_t\odot G_t\to C_t\to\tanh\to H_t$.
- Tất cả quyết định về tuyến cắt, đáp án và điểm cần kiểm chứng nằm trong `note-for-author.md`, không đặt trong ghi chú diễn giả.

## Trạng thái kiểm định sau chỉnh sửa

- Kiểm định tĩnh xác nhận 44 mã `data-slide-id` duy nhất và bảy mạch ngoài có kích thước 7, 11, 4, 8, 4, 5, 5; L08-39 là trang cuối.
- Thứ tự timing trong storyboard khớp tuyến đầy đủ X01–X04→39; tổng lõi 100 phút, mở rộng 20 phút và bài tập riêng 50 phút.
- Cú pháp JavaScript của khối điều hướng, tham chiếu SVG, cấu trúc XML và thuộc tính tiếp cận được kiểm tra cục bộ sau khi sửa.
- `python3 -m reloadserver 8765` không khả dụng trong môi trường (`No module named reloadserver`). Kiểm định cuối dùng máy chủ tĩnh chỉ bind `127.0.0.1` và chỉ phục vụ thư mục `2627-1/`.
- Chromium dựng đủ 44 trang ở cả $1280\times720$ và $960\times720$, tạo 88 ảnh kiểm tra; không phát hiện tràn, chồng lấn, tài nguyên hỏng hoặc hình thiếu.
- KaTeX dựng 204 công thức, gồm 26 công thức khối, không có lỗi phân tích. Chín SVG tải thành công; lỗi HTTP duy nhất là `favicon.ico` không thuộc nội dung deck.
- Kiểm thử bàn phím xác nhận sáu ranh giới Phải 06→07, 17→18, 21→22, 29→30, 33→34, 38→X01; phím End từ L08-38 tới L08-39. Tuyến đầy đủ đi qua X01, X02, X03, X04, fragment của X04 rồi kết thúc ở L08-39.
- Danh sách toàn bộ tiêu đề `h1`, `h2`, `h3` đã được xuất và rà thủ công; không có tiêu đề pha tiếng Anh ngoài các tên kiến trúc, viết tắt và mã LLO được phép.

## Pipeline lecture note

- Hồ sơ nguồn riêng đặt trong thư mục tạm chỉ chứa các đoạn UTF-8 cần thiết từ đề cương, slide, giáo trình, deck, planning và chín SVG. Không gửi `.env`, khóa API hoặc bí mật cho worker; `.env` chỉ được cầu nối cục bộ dùng để nạp khóa.
- Vai lập kế hoạch, ba vai phân tích nguồn, vai kiểm định storyboard, năm vai phản biện và hai lượt rà lại dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter. Mọi kết quả được chấp nhận đều có `requested_model` và `observed_model` trùng khớp, `provider` là `OpenRouter`.
- Mười nhiệm vụ soạn mảnh dùng đúng `deepseek/deepseek-v4-flash-0731` qua OpenRouter. Điều phối viên chỉ hợp nhất nội dung đã đối chiếu với nguồn và tự tính lại; loại toàn bộ mảnh 02 vì hỏng Unicode và tuyên bố quá mức, đồng thời loại các chi tiết không có trong nguồn hoặc sai phép tính ở các mảnh khác.
- Phạm vi DeepSeek được khóa để các đợt sau không thể tự mở rộng: mỗi nhiệm vụ chỉ được tạo đúng một tệp mới trong staging riêng; `MCP_WRITE_POLICY=create-once`; `MCP_MAX_WRITE_CHARS=2500`; không có quyền đọc hay ghi toàn kho, không được sửa tệp đã tồn tại, không được gọi shell, không được tải mạng và không được ghi trực tiếp vào sản phẩm. Lần ghi đầu của các mảnh 07, 09 và 10 vượt 2.500 ký tự đã bị từ chối toàn bộ trước khi tạo tệp; chỉ lượt thử lại ngắn hơn mới được chấp nhận.
- Lượt rà mạch sau chỉnh sửa phát hiện xung đột ký hiệu tầng đầu ra với cổng ra LSTM và thiếu định nghĩa $D_e$; lecture note đổi tầng chiếu sang $W_y,b_y$, bổ sung hợp đồng nhúng và làm rõ miền của mặt nạ. Một lượt rà toán hết thời gian được ghi nhận nhưng không dùng làm bằng chứng. Lượt rà toán thay thế xác nhận LSTM, shape và đếm tham số; đề xuất đổi $0{,}1790$ thành $0{,}1789$ bị bác vì phép tính bằng số đầy đủ cho $0{,}1789548500$, làm tròn đúng là $0{,}1790$.
- `$no-ai-slop` được dùng để rà toàn bộ văn bản công khai: không còn dấu vết worker, nhãn quy trình, chỉ dẫn diễn giả/người viết hoặc câu quảng bá. Nguyên tắc `$quill` được dùng để rà tuyến vấn đề → cơ chế cổng → ví dụ số → hình thức → kiến trúc → ứng dụng; không tạo `quill.json`.
- Kiểm định tĩnh lecture note: một `h1`, 40 chỉ thị bài tập/đáp án, 174 biểu thức KaTeX, chín ảnh và không có lỗi cấu trúc. Chromium dựng thành công ở $1280\times720$ và $390\times844$: 174 công thức, chín SVG, mười khối đáp án đóng mặc định, không lỗi runtime, không tràn ngang; bàn phím, chế độ in, chặn đường dẫn vượt thư mục và chặn ghép sai buổi đều đạt.
- Codex Slides không có runtime khả dụng trong môi trường hiện tại. Kiểm định trực quan dùng Chromium headless và giới hạn này được giữ trong nhật ký thay vì tuyên bố đã dùng Codex Slides.
