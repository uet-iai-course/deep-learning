# Dàn ý Bài 08: Các kiến trúc mạng nơ-ron truy hồi hiện đại

## Phạm vi và kết quả học tập

- Đối tượng: sinh viên đại học đã học mạng nơ-ron truy hồi (RNN) cơ bản, lan truyền ngược theo thời gian (BPTT), quy tắc chuỗi, sigmoid, tanh và phép toán tensor theo lô.
- LLO15: trình bày cấu trúc và cơ chế hoạt động của bộ nhớ ngắn dài hạn (LSTM) và đơn vị truy hồi có cổng (GRU).
- LLO16: phân tích ưu điểm và giới hạn của LSTM/GRU so với RNN cơ bản khi xử lý phụ thuộc dài hạn.
- Tuyến lõi: 100 phút. Tuyến mở rộng/có thể cắt: 20 phút. Bài tập riêng: 50 phút.
- Không tạo demo phân tích cảm xúc: phần nguồn đã ánh xạ chỉ mô tả kiến trúc và ví dụ, không có code để chuyển; người dùng cũng không yêu cầu demo.

## Cấu trúc bảy mạch

| Mạch | Trang | Chức năng |
|---|---|---|
| 1 | L08-00–06 | Mở bài, cầu nối gradient và hợp đồng tensor |
| 2 | L08-07–17 | Xây ô LSTM, ví dụ số và phương trình ma trận |
| 3 | L08-18–21 | Phân tích nhánh gradient của LSTM |
| 4 | L08-22–29 | Cơ chế, ví dụ, quy ước và nhánh giữ trực tiếp của GRU |
| 5 | L08-30–33 | RNN sâu và RNN hai chiều |
| 6 | L08-34–38 | Bộ mã hóa–giải mã và mất mát có mặt nạ |
| 7 | L08-X01–X04, L08-39 | Bốn trạm đối chiếu mở rộng rồi kết luận bắt buộc |

L08-39 là trang cuối và thuộc tuyến lõi 3 phút. Tại L08-38, phím End đi thẳng đến L08-39; phím Phải đi vào L08-X01, rồi đi xuống qua L08-X04 đến L08-39. Liên kết phím Phải được khóa tại sáu ranh giới L08-06→07, 17→18, 21→22, 29→30, 33→34 và 38→X01; phím End luôn đến L08-39.

## Mạch khái niệm

1. Từ tích Jacobian của RNN cơ bản đến nhu cầu có đường lưu giữ có điều kiện.
2. Phân biệt trạng thái ô $C_t$ và trạng thái ẩn $H_t$; khóa quy ước tensor, độ dài thật, trạng thái đầu và mặt nạ trạng thái nguồn.
3. Xây LSTM theo thứ tự tăng dần của slide nguồn: ứng viên, cổng vào, cổng ra, cổng quên, ô hoàn chỉnh. Giữ cổng ra trước cổng quên vì nguồn giới thiệu từng thành phần theo thứ tự đó; sơ đồ ô hoàn chỉnh sau cùng vẫn thể hiện đúng luồng cập nhật trạng thái ô.
4. Tính một bước LSTM vô hướng, rồi khái quát sang phương trình ma trận và bảng kích thước.
5. Tách nhánh gradient trực tiếp qua $C_t$ khỏi đạo hàm toàn phần; giới hạn mệnh đề về gradient triệt tiêu.
6. Khóa dữ kiện một bước GRU trước khi khái quát phương trình; đổi quy ước cổng bằng cả biến cổng và tiền kích hoạt.
7. Đếm tham số theo phương trình bài, rồi kiểm tra hệ số nhánh giữ trực tiếp của GRU và phân biệt nó với đạo hàm toàn phần.
8. Mở rộng bằng trạng thái tổng quát $S$: $S=H$ cho RNN/GRU và $S=(H,C)$ cho LSTM; sau đó xét mạng hai chiều.
9. Dùng một mô hình cơ sở GRU mã hóa–giải mã: token được ánh xạ thành vector nhúng, trạng thái nguồn cuối hợp lệ khởi tạo bộ giải mã, logit đi vào chéo entropy ổn định và mặt nạ đích chỉ chọn token mất mát.
10. Tổ chức tuyến mở rộng thành bốn trạm đối chiếu: biểu diễn phân loại → chi phí tham số của ô → sinh tự hồi quy → chọn kiến trúc; sau đó quay về kết luận chung về cơ chế và giới hạn gradient.

## Ánh xạ nguồn

| Nguồn | Phạm vi dùng | Vai trò |
|---|---|---|
| DOCX đề cương, III.2 → Buổi 8 | Tên buổi, LLO15–LLO16, LSTM/GRU, RNN sâu, hai chiều, dịch máy | Khóa phạm vi và ranh giới buổi |
| `source-materials/slides/lec14_rnn.pdf`, PDF 25–33 | LSTM được xây từng bước; GRU và quy ước cổng cập nhật | Nguồn chính, giữ mạch |
| Cùng tệp, PDF 35–40 | RNN nhiều tầng và hai chiều | Nguồn phụ |
| Cùng tệp, PDF 58–62 | Bộ mã hóa–giải mã và bối cảnh dịch máy | Nguồn phụ; không dùng benchmark GNMT |
| Bài 07 và `source-materials/slides/lec14_rnn.pdf`, PDF 25 | Đường đạo hàm dài có thể co hoặc giãn; động cơ đường cập nhật có cổng | Cầu nối tiên quyết, không dùng trực tiếp PDF 23 |
| `source-materials/textbooks/hocsau_draft.pdf`, PDF 226–245 | Kích thước, phát tự động, GRU, RNN mở rộng, học theo đáp án, mặt nạ | Kiểm chứng và bổ sung phần slide thiếu |
| Cùng tệp, PDF 315–317 | Phân tích cảm xúc bằng RNN hai chiều | Ví dụ mở rộng |

## Tài sản trực quan

| Tệp SVG | Nội dung | Nguồn để vẽ lại |
|---|---|---|
| `bridge-gradient.svg` | So sánh đường trạng thái RNN cơ bản và LSTM | Bài 07; lec14_rnn 25; GT 226 |
| `lstm-build.svg` | Bốn tín hiệu của LSTM | lec14_rnn 26–31 |
| `lstm-cell.svg` | Ô LSTM hoàn chỉnh | lec14_rnn 31–32 |
| `gradient-paths.svg` | Nhánh trực tiếp và các nhánh toàn phần | Suy ra từ đồ thị ô LSTM |
| `gru-cell.svg` | Cổng đặt lại và cập nhật của GRU | lec14_rnn 33 |
| `stacked-rnn.svg` | RNN ba tầng | lec14_rnn 35–38; GT 232–234 |
| `bidirectional.svg` | Hai hướng trên cùng chuỗi | lec14_rnn 39–40; GT 234–236 |
| `encoder-decoder.svg` | Mã hóa nguồn và giải mã đích | lec14_rnn 58–59; GT 239–242 |
| `sentiment.svg` | Ghép $\overrightarrow H_{L_n}$ và $\overleftarrow H_1$ để phân loại cảm xúc | GT 315–317 |

## Thuật ngữ và ký hiệu

| Ký hiệu/thuật ngữ | Nghĩa và quy ước |
|---|---|
| $N,T,L_n,D_x,D_h$ | Kích thước lô, số bước tối đa sau đệm, độ dài thật mẫu $n$, chiều đầu vào, chiều ẩn |
| $D_e,V$ | Chiều vector nhúng token đích; kích thước từ vựng |
| $X_t$ | Lát cắt tại thời điểm $t$, kích thước $N\times D_x$ |
| $H_t$ | Trạng thái ẩn, kích thước $N\times D_h$ |
| $C_t$ | Trạng thái ô của LSTM, kích thước $N\times D_h$ |
| $I_t,F_t,O_t,G_t$ | Cổng vào, cổng quên, cổng ra, ứng viên của LSTM |
| $R_t,Z_t,\widetilde H_t$ | Cổng đặt lại, cổng cập nhật, trạng thái ứng viên của GRU |
| $\odot$ | Tích Hadamard theo từng phần tử |
| $S_t$ | Trạng thái tổng quát: $H_t$ cho RNN/GRU, $(H_t,C_t)$ cho LSTM |
| $M^{src},M^{tgt}$ | Mặt nạ giữ trạng thái nguồn; mặt nạ chọn token đích trong mất mát |
| $Q$ | Ngữ cảnh từ trạng thái GRU mã hóa cuối hợp lệ, $N\times D_h$ |
| $u_n^{cls},U^{cls}$ | Biểu diễn phân loại của mẫu $n$, $1\times2D_h$; lô biểu diễn, $N\times2D_h$ |
| $A_{t'},P_{t'}$ | Logit và xác suất theo từ vựng, $N\times V$ |
| $\langle bos\rangle,\langle eos\rangle$ | Token bắt đầu và kết thúc chuỗi |

Quy ước GRU của bài là quy ước slide chính:

$$H_t=(1-Z_t)\odot H_{t-1}+Z_t\odot\widetilde H_t.$$

Giáo trình dùng ký hiệu phần bù cho cổng cập nhật. Ánh xạ là $Z_{\text{slide}}=1-Z_{\text{GT}}$; nếu hai cổng đều do sigmoid tạo ra thì $a_{\text{slide}}=-a_{\text{GT}}$, nên trọng số và độ lệch tạo tiền kích hoạt cũng đổi dấu.
