# Nhật ký rà soát Bài 08

## Quyết định nguồn và phạm vi

| Quyết định | Bằng chứng và lý do |
|---|---|
| Giữ mạch xây LSTM từng thành phần | `lec14_rnn.pdf` 25–32 lần lượt đưa ứng viên, trạng thái ô, cổng vào, cổng ra và cổng quên; bản deck giữ trình tự này trước khi khái quát. |
| Cầu nối gradient dùng Bài 07 và PDF 25 | Bỏ tham chiếu trực tiếp `lec14_rnn.pdf` PDF 23; Bài 07 đã thiết lập tích Jacobian co/giãn, còn PDF 25 mở động cơ LSTM. |
| Dùng GT để bổ sung GRU | Slide chính chỉ có PDF 33; GT PDF 229–232 cung cấp kích thước, phát tự động và phương trình ma trận đầy đủ. |
| Dùng 35–40 cho nhiều tầng và hai chiều | Đúng dải phụ được `source.md` khóa; không lấy phần kiến trúc ngoài dải. |
| Dùng 58–59 và GT 239–243 cho dịch máy | Đủ để giới thiệu bộ mã hóa–giải mã, học theo đáp án và mặt nạ; không dùng số liệu GNMT ở 60–62 vì không cần cho LLO. |
| Dùng GT 315–317 cho phân tích cảm xúc | Nguồn đã ánh xạ vai trò ví dụ ứng dụng; đặt trong tuyến mở rộng. |
| Không có code demo | Nguồn và yêu cầu không giao chuyển code; bài tập 50 phút dùng tính tay và phân tích. |

## Sai khác và mâu thuẫn đã xử lý

- Slide chính dùng $H_t=(1-Z_t)\odot H_{t-1}+Z_t\odot\widetilde H_t$, nên $Z_t$ gần 1 ghi ứng viên mới.
- GT PDF 231 dùng $H_t=Z_t\odot H_{t-1}+(1-Z_t)\odot\widetilde H_t$, nên $Z_t$ gần 1 giữ trạng thái cũ.
- Bản deck giữ quy ước slide chính vì slide quyết định mạch và ký hiệu trong phạm vi buổi. L08-27 ghi hai phương trình và ánh xạ $Z_{slide}=1-Z_{GT}$. Vì $\sigma(-a)=1-\sigma(a)$, cùng một hàm cổng còn đòi hỏi đổi dấu tiền kích hoạt, trọng số và độ lệch; không giữ nguyên $Z$/weights rồi đổi nghĩa.
- Mệnh đề của slide PDF 25 về “tránh gradient suy giảm” được thu hẹp thành “thêm nhánh trực tiếp có hệ số cổng quên”. L08-18–21 phân biệt đạo hàm nhánh với đạo hàm toàn phần và không tuyên bố LSTM loại bỏ gradient triệt tiêu.
- Bổ sung trạng thái đầu, thiết bị, phát tự động và mặt nạ từ GT vì thiếu chúng sẽ làm công thức theo lô hoặc triển khai mơ hồ. Mặt nạ nguồn giữ trạng thái; mặt nạ đích chỉ chọn token trong mất mát.
- Chọn mô hình cơ sở GRU cho cả bộ mã hóa và bộ giải mã. $Q_n=H_{L_n}^{enc,(n)}$ chỉ khởi tạo $S_0$; không chèn lại $Q$ ở mỗi bước.
- Phép đếm tham số giả sử đúng phương trình của bài với một độ lệch cho mỗi phép affine/cổng; không khẳng định mọi API đóng gói độ lệch giống nhau.

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

## Hợp nhất storyboard và bốn phản biện

| Góc rà soát | Mức độ | Trang | Vấn đề | Quyết định sửa |
|---|---|---|---|---|
| Sinh viên | nghiêm trọng | L08-04,07,12–17,24–27 | Công thức/cổng xuất hiện trước định nghĩa; ví dụ chứa dữ kiện không dùng; thiếu kiểm tra kích thước | Bỏ công thức sớm ở L04, biến L07 thành bản đồ, khóa tiền kích hoạt LSTM, đặt ví dụ GRU trước phương trình và thêm kiểm tra L17. |
| Chuyên gia Học sâu | nghiêm trọng | L08-05–06,30–39 | Trạng thái LSTM nhiều tầng và mặt nạ chưa có hợp đồng; bộ mã hóa–giải mã trộn nhiều mô hình cơ sở | Dùng $S=H$ hoặc $(H,C)$, tách $M^{src}/M^{tgt}$, khóa GRU mã hóa/giải mã và trạng thái nguồn cuối hợp lệ. |
| Toán học, thuật toán và triển khai | nghiêm trọng | L08-18–29,35–39,X02 | Nhánh gradient chưa khóa biến; ánh xạ $Z$ thiếu đổi dấu tiền kích hoạt; mất mát chưa khóa ổn định số; phép đếm độ lệch dễ bị hiểu là API | Ghi các đại lượng giữ cố định, thêm tích $.4788$, ánh xạ $a_s=-a_g$, dùng chéo entropy hợp nhất từ logit và giới hạn phép đếm theo phương trình bài. |
| Học thuật và giảng dạy | trung bình | L08-00–08,31,39,X01–X03 | Thuật ngữ lần đầu, chu trình kiểm tra và ứng dụng mở rộng chưa tạo bước tiến | Mở đầy đủ viết tắt, thêm kiểm tra L31/L39, định nghĩa gộp cảm xúc theo độ dài thật và thay bảng lặp bằng vết sinh tự hồi quy. |

- Đã rà vùng bị ảnh hưởng và hai trang lân cận: L08-00–08, L08-12–31 và L08-33–X04.
- Thứ tự chu trình sau sửa: L08-15 là hoạt động trong ví dụ LSTM, L08-17 là kiểm tra cuối; GRU dùng dữ kiện L08-24 trước hình thức L08-25; L08-31 và L08-39 có câu hỏi cùng fragment.
- Timing được cân lại mà không đổi tổng: L08-04 và L08-07 mỗi trang giảm 1 phút; L08-20 và L08-39 mỗi trang tăng 1 phút. Lõi giữ 100 phút, mở rộng 20 phút, bài tập 50 phút.
- Để tránh quá tải L08-36, chuyển sơ đồ mã hóa–giải mã sang L08-35; L08-36 chỉ giữ cập nhật GRU, toàn bộ kích thước logit/đầu ra và quy ước $Q$ chỉ khởi tạo $S_0$. Không thêm trang hoặc đổi timing.
- Dọn biên tập cuối: ghi chú L04/L07 chỉ mô tả cơ chế, Việt hóa “gradient”, “bias” và “pad” trên mặt trang; không đổi toán hoặc timing.

## Biên tập và tài sản

- Nội dung hiển thị và ghi chú đã được biên tập theo no-ai-slop: câu trực tiếp, không khẩu hiệu, không câu hỏi tu từ, không kết luận thực nghiệm thiếu giao thức.
- Quill được dùng để rà chuỗi vấn đề → trực giác cổng → ví dụ số → phương trình → gradient → kiến trúc → ứng dụng; không tạo `quill.json`.
- Chín SVG được vẽ lại; không dùng ảnh raster, screenshot hoặc tài sản mạng.
- Tất cả quyết định về tuyến cắt, đáp án và điểm cần kiểm chứng nằm trong `note-for-author.md`, không đặt trong ghi chú diễn giả.

## Kiểm định tĩnh của bản nháp

- 44 trang, 44 mã `data-slide-id` duy nhất, 44 khối ghi chú và 44 dòng timing trong storyboard; thứ tự mã HTML khớp storyboard.
- KaTeX strict: 189 biểu thức, 0 lỗi với `throwOnError: true` và `strict: "error"`.
- Cấu trúc HTML: thẻ đóng/mở cân bằng; trang chỉ dùng section ngoài cho cụm và section trong cho trang.
- Tài nguyên cục bộ: 19 đường dẫn, 0 đường dẫn thiếu; không có phụ thuộc mạng cốt lõi.
- SVG: 9/9 tệp được tham chiếu đúng một tập, 0 tài sản thừa; tất cả phân tích XML được và có `role="img"`, `title`, `desc`; cỡ chữ nhỏ nhất 22 px.
- 9 thẻ `img` có mô tả `alt`; không có tham chiếu PNG, JPEG, GIF hoặc WebP.
- Timing: lõi 100 phút, mở rộng 20 phút, bài tập riêng 50 phút.
- 9 lời mời tương tác đều dùng nhãn `Câu hỏi:` và có phản hồi dạng fragment.
- Tiêu đề `h1`, `h2`, `h3` được rà thủ công; tiếng Anh chỉ còn tên kiến trúc hoặc viết tắt được phép như RNN, LSTM, GRU và LLO.
- Cấu hình RevealJS giữ khung 1280 × 720, điều khiển ở cạnh, số trang, hash một gốc, KaTeX, ghi chú và tô sáng mã.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy được vì môi trường thiếu mô-đun `reloadserver`.
- Máy chủ HTTP cục bộ đang có tại cổng 8765 trả mã 200; SHA-256 của bản phục vụ trùng tệp HTML trong kho.
- Browser và Codex Slides không khả dụng trong lượt hậu kiểm, nên chưa thể xác nhận trực quan từng trang ở hai kích thước màn hình; kiểm tra SVG bằng montage cục bộ không phát hiện lỗi cắt hoặc chồng lấn rõ ràng.
