# Bài 07 — Mạng nơ-ron hồi quy

## Phạm vi và kết quả học tập

- Đối tượng: sinh viên đã học quy tắc chuỗi, Jacobian, tích vectơ–Jacobian, chuẩn vectơ–ma trận, lan truyền ngược, MLP và phép nhân ma trận theo lô.
- LLO13: “Trình bày được cấu trúc và nguyên lý hoạt động của một mạng RNN đơn giản.”
- LLO14: “Giải thích được khái niệm trạng thái ẩn (hidden state) và cách nó lưu trữ thông tin quá khứ.”
- LLO3: “Mô tả được thuật toán Lan truyền ngược theo thời gian (BPTT).”
- **Dấu vết đề cương:** mã `LLO3` ở Buổi 07 trùng `LLO3` của Buổi 02. Deck và planning giữ nguyên mã, không tự sửa thành mã khác.
- **Nội dung bài giảng tách khỏi nguyên văn LLO:** phần phân tích gradient triệt tiêu hoặc bùng nổ, các dạng ánh xạ chuỗi (một–sang–một, một–sang–nhiều, nhiều–sang–một, nhiều–sang–nhiều) và mô hình trải mạng theo thời gian là nội dung bài giảng mở rộng theo mạch của `source.md` Buổi 07, không nằm trong nguyên văn ba LLO trên; chúng phục vụ LLO13–LLO14 và LLO3 (BPTT) nhưng được trình bày như nội dung giảng thêm.
- Tuyến lõi 100 phút, tuyến mở rộng có thể cắt 20 phút, bài tập riêng 50 phút.
- Không có code demo hoặc raster. LSTM/GRU chỉ xuất hiện ở trang cầu nối, không có công thức cổng.
- Các công thức xét một lô gồm các chuỗi hoặc đoạn đã chọn có cùng $T$ và mọi bước hợp lệ. Cách ghép lô chuỗi khác độ dài bằng padding, masking hoặc bucketing nằm ngoài phạm vi; không tự coi cắt đoạn là giải pháp tổng quát.

## Cấu trúc bảy mạch

Deck gồm 7 `<section>` ngoài (44 trang, 44 mã `data-slide-id` duy nhất):

1. **Mở đầu** (L07-00–06): vấn đề chuỗi, trạng thái, hợp đồng tensor, kiểm tra.
2. **Ô RNN và ví dụ vô hướng** (L07-07–13): bộ số, quan hệ truy hồi, kích thước, trải mạng.
3. **Dạng ánh xạ và lan truyền xuôi** (L07-14–21): bốn dạng, mất mát, thuật toán, ví dụ số, kiểm tra.
4. **BPTT** (L07-22–29): đồ thị gradient, vòng $T\to1$, gradient tham số, kiểm tra.
5. **Ổn định gradient** (L07-30–34): tích Jacobian, triệt tiêu/bùng nổ, kiểm tra.
6. **BPTT cắt ngắn** (L07-35–38): chi phí, so sánh $T$ và $K$, kiểm tra.
7. **Mở rộng và kết luận** (L07-X01–X04, rồi L07-39): tuyến mở rộng có thể cắt, kết thúc bằng trang cầu nối L07-39 sang Bài 08.

L07-39 là trang cuối toàn bộ bài: tuyến lõi tại L07-38 nhấn End để tới L07-39; tuyến đầy đủ từ L07-38 nhấn Phải vào L07-X01, đi Xuống qua X02–X04 rồi tới L07-39. Phím Phải có binding riêng tại sáu ranh giới L07-06, L07-13, L07-21, L07-29, L07-34 và L07-38 vì RevealJS giữ chỉ số dọc khi chuyển sang mạch kế; ở các trang khác, binding gọi lại `Reveal.right()`. Phím End có binding riêng tìm L07-39 và gọi `Reveal.slide(h,v)`, nên luôn tới đúng trang cuối kể cả trong phiên mới.

## Mạch nội dung

1. Dữ liệu chuỗi, thứ tự và nhu cầu giữ ngữ cảnh.
2. Trạng thái ẩn; hợp đồng tensor theo quy ước lô ở hàng.
3. Ví dụ vô hướng trước; sau đó khái quát quan hệ truy hồi, kích thước, trạng thái đầu và mạng được trải.
4. Một–sang–một, một–sang–nhiều, nhiều–sang–một và nhiều–sang–nhiều.
5. Lan truyền xuôi qua một ví dụ vô hướng ba bước.
6. BPTT: gradient đầu ra, gradient trạng thái, tổng gradient tham số.
7. Đạo hàm trực tiếp và đạo hàm toàn phần trong ví dụ ba bước.
8. Tích Jacobian, gradient triệt tiêu và bùng nổ.
9. BPTT toàn phần so với BPTT cắt ngắn; cầu nối sang kiến trúc có cổng.
10. Mở rộng: mô hình ngôn ngữ, căn chỉnh chuỗi, RNN nhiều tầng và hai chiều.

## Hợp đồng tensor

| Đại lượng | Kích thước | Nghĩa |
|---|---|---|
| $X$ | $N\times T\times D_x$ | Lô đang xét gồm các chuỗi hoặc đoạn đã chọn cùng $T$, mọi bước hợp lệ |
| $X_t$ | $N\times D_x$ | Ma trận hàng của toàn bộ lô tại $t=1,\ldots,T$ |
| $H_t,A_t$ | $N\times D_h$ | Trạng thái và tiền kích hoạt |
| $O_t$ | $N\times D_y$ | Đầu ra tại bước $t$ |
| $W_x$ | $D_x\times D_h$ | Trọng số đầu vào–trạng thái |
| $W_h$ | $D_h\times D_h$ | Trọng số truy hồi dùng chung theo thời gian |
| $W_y$ | $D_h\times D_y$ | Trọng số trạng thái–đầu ra |
| $b_h,b_y$ | $D_h,D_y$ | Độ lệch phát theo trục lô |
| $H_0$ | $N\times D_h$ | Trạng thái đầu, bằng 0 hoặc được cung cấp rõ |
| $Y$ cho nhiều–sang–một | $N$ hoặc $N\times D_y$ | Chỉ số lớp toàn chuỗi, hoặc đích vectơ/liên tục của toàn chuỗi |
| $Y$ cho nhiều–sang–nhiều căn chỉnh | $N\times T$ hoặc $N\times T\times D_y$ | Chỉ số lớp, hoặc đích vectơ one-hot/liên tục tại từng bước |

## Ví dụ số xuyên suốt

RNN vô hướng, ba bước, nhiều–sang–một:

$$x=(1,0,-1),\quad h_0=0,\quad w_x=0.5,\quad w_h=0.8,\quad w_y=1.2,$$

$$h_t=\tanh(w_xx_t+w_hh_{t-1}),\quad o_3=w_yh_3,\quad y=0.4,\quad \mathcal L=\tfrac12(o_3-y)^2.$$

Kết quả đã tự tính: $h=(0.462117,0.353724,-0.213677)$, $o_3=-0.256412$, $\mathcal L=0.215439$; $\delta=(-0.331024,-0.526139,-0.751730)$; $\partial\mathcal L/\partial w_x=0.420706$, $\partial\mathcal L/\partial w_h=-0.509043$, $\partial\mathcal L/\partial w_y=0.140260$. Đạo hàm trực tiếp tại bước 3 cho gradient $-0.265905$; đạo hàm toàn phần cho $-0.509043$.

## Ánh xạ nguồn

| Nguồn | Dải trang PDF | Quyết định và trang đích |
|---|---:|---|
| `lec14_rnn.pdf` | 3–4 | Giữ mô hình ngôn ngữ làm động cơ và mở rộng: L07-02, L07-X01. |
| cùng tệp | 5–6 | Gộp chú thích ảnh thành ví dụ một–sang–nhiều: L07-14. Không đi vào cơ chế sinh. |
| cùng tệp | 7–9 | Giữ dịch máy/chuỗi–sang–chuỗi ở mức phân loại dạng ánh xạ: L07-14, L07-X02. |
| cùng tệp | 10–13 | Việt hóa ô RNN, rồi đặt ví dụ vô hướng trước công thức ma trận và kích thước: L07-04, L07-07–13. |
| cùng tệp | 14–17 | Giữ lan truyền xuôi, mất mát và đồ thị tính toán: L07-14–25; nêu cả nhiều–sang–nhiều không căn chỉnh nhưng không triển khai bộ giải mã. |
| cùng tệp | 18 | Giữ cảnh báo bộ nhớ BPTT: L07-35, L07-37. |
| cùng tệp | 19–20 | Giữ BPTT cắt ngắn, trạng thái đi tiếp nhưng gradient bị ngắt: L07-36–38. |
| cùng tệp | 21 | Đưa ví dụ gradient vô hướng trước, rồi sửa công thức theo quy ước lô ở hàng và vòng lặp $T\to1$: L07-22–29. |
| cùng tệp | 22–23 | Giữ tích Jacobian và giới hạn phụ thuộc dài; dùng trang 23 chỉ làm cầu nối: L07-30–34, L07-39. |
| cùng tệp | 35 | Dùng làm đối chiếu ánh xạ nhiều–sang–nhiều: L07-14. |
| cùng tệp | 36–38 | Gộp ba trang lặp thành một công thức RNN nhiều tầng: L07-X03. |
| cùng tệp | 39–40 | Gộp thành RNN hai chiều và khóa điều kiện có toàn chuỗi: L07-X04. |
| cùng tệp | 42 | Dùng sơ đồ RNN ký tự để kiểm chứng phân rã mô hình ngôn ngữ: L07-X01. |
| cùng tệp | 43–49 | Bỏ khỏi deck: quyết định trong dải nguồn phụ được duyệt (dải phụ là 35–40 và 42–49); mẫu sinh và đơn vị có thể diễn giải không cần cho LLO, không dùng số liệu hoặc kết luận thực nghiệm. Không phải nguồn cấm. |
| `hocsau_draft.pdf` | 199–205 | Kiểm chứng dữ liệu chuỗi, các dạng ánh xạ, trạng thái và mô hình ngôn ngữ: L07-02–06, L07-14–17, L07-X01–X02. |
| cùng tệp | 209–213 | Khôi phục ký hiệu mô hình RNN cơ bản và trạng thái: L07-07–13. |
| cùng tệp | 213–218 | Kiểm chứng quan hệ truy hồi, đầu ra, tham số và lan truyền xuôi: L07-07–21. |
| cùng tệp | 218–224 | Kiểm chứng BPTT, đạo hàm toàn phần, cắt ngắn và tích lũy gradient: L07-22–39. |

## Tài sản

Mười bốn SVG tại `2627-1/img/lec-07/`: ngữ cảnh chuỗi, mạng được trải, kích thước ô, dạng ánh xạ, ví dụ lan truyền xuôi, ví dụ BPTT, đạo hàm trực tiếp/toàn phần, tích Jacobian, triệt tiêu/bùng nổ, BPTT toàn phần/cắt ngắn, chia sẻ tham số, bộ nhớ BPTT, phụ thuộc dài và cầu nối kiến trúc có cổng.
