# Nhật ký rà soát Bài 07

## Quyết định nguồn và phạm vi

| Quyết định | Bằng chứng và lý do |
|---|---|
| Giữ nguyên `LLO3` của BPTT | DOCX Buổi 7 dùng `LLO3`, trùng mã Buổi 02. Đây là lỗi đánh số đã được `source.md` yêu cầu giữ dấu vết; không đổi mã. |
| Chuyển LLO về nguyên văn DOCX trên L07-01 | Ba card dùng đúng nguyên văn: LLO13 “Trình bày được cấu trúc và nguyên lý hoạt động của một mạng RNN đơn giản.”; LLO14 “Giải thích được khái niệm trạng thái ẩn (hidden state) và cách nó lưu trữ thông tin quá khứ.”; LLO3 “Mô tả được thuật toán Lan truyền ngược theo thời gian (BPTT).” Nội dung bài giảng mở rộng (dạng ánh xạ chuỗi, mạng trải theo thời gian, gradient triệt tiêu/bùng nổ) được tách rõ trong `outline.md` và không ghi vào nguyên văn LLO. |
| Gộp 9 mạch thành 7 mạch và chuyển L07-39 xuống cuối | Bản trước có 9 `<section>` ngoài, vượt dải 5–7 của quy trình. Gộp thành 7 mạch: [00–06], [07–13], [14–21], [22–29], [30–34], [35–38], [X01–X04 rồi 39]. L07-39 chuyển xuống sau X04 làm slide cuối toàn deck để bài luôn khép bằng câu hỏi cho Bài 08; tuyến lõi tại L07-38 dùng End tới 39, tuyến đầy đủ đi Phải qua X01–X04 rồi Down tới 39. Timing từng trang giữ nguyên; tiểu tổng lõi 15+17+20+21+14+11+2=100, mở rộng 20, bài tập 50. |
| Gộp 9 mạch thành 7 mạch và chuyển L07-39 xuống cuối | Bản trước có 9 `<section>` ngoài, vượt dải 5–7 của quy trình. Gộp thành 7 mạch: [00–06], [07–13], [14–21], [22–29], [30–34], [35–38], [X01–X04 rồi 39]. L07-39 chuyển xuống sau X04 làm slide cuối toàn deck để bài luôn khép bằng câu hỏi cho Bài 08; tuyến lõi tại L07-38 dùng End tới 39, tuyến đầy đủ đi Phải qua X01–X04 rồi Down tới 39. Timing từng trang giữ nguyên; tiểu tổng lõi 15+17+20+21+14+11+2=100, mở rộng 20, bài tập 50. |
| Gắn riêng phím Phải tại sáu ranh giới mạch | RevealJS giữ chỉ số dọc khi chuyển sang `<section>` ngang kế tiếp, nên thao tác Phải có thể vào sai trang. Bảng ánh xạ khóa L07-06→07, L07-13→14, L07-21→22, L07-29→30, L07-34→35 và L07-38→X01; binding lấy `Reveal.getIndices` rồi gọi `Reveal.slide(h,v)`. Ở trang khác gọi `Reveal.right()`. |
| Gắn phím End tới L07-39 | Trong phiên mới, End mặc định có thể vào X01 vì RevealJS chưa nhớ chỉ số dọc 4 của mạch cuối. Binding End áp dụng cho toàn bộ bài, tìm L07-39, lấy `Reveal.getIndices` rồi gọi `Reveal.slide(h,v)`; đúng nghĩa đi tới trang cuối. |
| Giữ trục nội dung của `lec14_rnn.pdf` 3–23 | Đi từ bài toán chuỗi đến ô RNN, quan hệ truy hồi, lan truyền xuôi, BPTT và gradient dài; khớp phạm vi DOCX. |
| Chỉ dùng 35–40 và 42 trong dải phụ | 35–40 hỗ trợ dạng ánh xạ, nhiều tầng, hai chiều; 42 kiểm chứng mô hình ngôn ngữ. 43–49 nằm trong dải phụ được duyệt (35–40 và 42–49) nhưng bị bỏ vì không cần cho LLO; đây là quyết định trong dải được duyệt, không phải nguồn cấm. |
| Không dùng 25–33 hoặc 51–62 | `source.md` dành 25–33 cho Buổi 08 và cấm 51–62. |
| LSTM/GRU chỉ là cầu nối | DOCX nhắc đọc trước, `source.md` yêu cầu kết thúc ở giới hạn phụ thuộc dài. Không đưa công thức hoặc so sánh kiến trúc. |
| Không có lab/code demo | Quy trình chỉ tạo code demo khi nguồn có nội dung code tương ứng hoặc người dùng yêu cầu. Phần nguồn được ánh xạ cho buổi này không cung cấp triển khai cần chuyển và người dùng không yêu cầu demo; thay bằng bài tập tính tay đúng 50 phút. |
| Không thêm teacher forcing, padding/masking, bucketing hoặc cắt giới hạn gradient | Dải chính 3–23 trình bày triệt tiêu/bùng nổ và BPTT cắt ngắn nhưng không trình bày cắt giới hạn gradient; các nội dung còn lại cũng không cần cho phép tính RNN cơ bản. Không dùng cắt đoạn như lời giải mặc định vì có thể làm sai nghĩa nhãn toàn chuỗi. |

## Quyết định toán học và triển khai

- Chọn quy ước lô theo hàng và khóa $X\in\mathbb R^{N\times T\times D_x}$ cho lô đang xét: các chuỗi hoặc đoạn đã chọn có cùng $T$ và mọi bước hợp lệ. Padding/masking và bucketing cho chuỗi khác độ dài không thuộc phạm vi; không khẳng định chuỗi gốc phải được cắt đoạn.
- Nêu $H_0$ như điều kiện biên với đúng kích thước, kiểu dữ liệu và thiết bị.
- Tách tiền kích hoạt $A_t$, trạng thái $H_t$ và đầu ra $O_t$ để BPTT có biến lấy đạo hàm rõ.
- Với nhiều–sang–một, khóa đích chỉ số lớp $N$ hoặc đích vectơ $N\times D_y$; mất mát chỉ ở $O_T$ nhưng gradient vẫn truyền qua mọi trạng thái trước.
- Với nhiều–sang–nhiều căn chỉnh, khóa mẫu số $NT$; phân lớp dùng softmax theo trục $D_y$. Entropy chéo được tính trực tiếp từ logit bằng $-O_{t,Y_t}+\operatorname{logsumexp}(O_t)$ theo trục này hoặc hàm nhận trực tiếp logit, không qua phép softmax rồi log thủ công. Đích liên tục có thể dùng mất mát bình phương. Trường hợp không căn chỉnh được nêu nhưng không mở cơ chế giải mã hoặc teacher forcing.
- Gradient trạng thái gồm hai nhánh: đầu ra hiện tại và trạng thái tương lai. Ví dụ hiện rõ $\bar o_3\to\delta_3\to\delta_2\to\delta_1$ trước khi khái quát. BPTT khởi tạo $G_{T+1}=0$, lặp $t=T,\ldots,1$; gradient trọng số và độ lệch cộng qua mẫu và thời gian.
- Tách đạo hàm trực tiếp $\partial h_3/\partial w_h$ khi giữ $h_2$ cố định khỏi đạo hàm toàn phần có đường qua $h_2$.
- Phát biểu triệt tiêu/bùng nổ theo tích Jacobian. Nhãn mũi tên gradient trong `gradient-product.svg` dùng $J_t^\top$ theo quy ước vectơ hàng. Không dùng mệnh đề quá mạnh rằng chỉ giá trị kỳ dị của $W_h$ quyết định; đạo hàm tanh và hướng vectơ cũng tham gia.
- BPTT cắt ngắn chuyển trạng thái về phía trước nhưng ngắt gradient ở ranh giới; gradient là xấp xỉ của toàn chuỗi.

## Tự tính ví dụ số

| Đại lượng | Giá trị |
|---|---:|
| $(a_1,h_1)$ | $(0.500000,0.462117)$ |
| $(a_2,h_2)$ | $(0.369694,0.353724)$ |
| $(a_3,h_3)$ | $(-0.217021,-0.213677)$ |
| $(o_3,\mathcal L)$ | $(-0.256412,0.215439)$ |
| $(\delta_1,\delta_2,\delta_3)$ | $(-0.331024,-0.526139,-0.751730)$ |
| $(\partial L/\partial w_x,\partial L/\partial w_h,\partial L/\partial w_y)$ | $(0.420706,-0.509043,0.140260)$ |
| $dh_3/dw_h$ toàn phần | $0.646244$ |
| gradient $w_h$ chỉ từ nhánh trực tiếp bước 3 | $-0.265905$ |
| $\partial h_3/\partial h_0$ | $0.336196$ |
| $0.8^{20}$ | $0.011529$ |

## Dấu vết hai lỗi lịch giữa kỳ

Giữ nguyên cả hai bằng chứng lỗi lịch của đề cương, không hòa giải:

1. **Bảng đánh giá đặt giữa kỳ ở tuần 8** trong khi tiến độ chi tiết xếp ôn tập và kiểm tra giữa kỳ ở buổi 09. Hai mốc này mâu thuẫn nhau trong DOCX; deck không tự chọn một phía.
2. **Nội dung chi tiết buổi 09** là “Ôn tập và kiểm tra giữa kỳ”, trong khi bảng đánh giá đã đặt giữa kỳ ở tuần 8. Deck 09 không được xây dựng theo quy trình, nên mâu thuẫn được ghi lại nguyên trạng.

## Sơ đồ bốn dạng ánh xạ ở L07-14

Sơ đồ `architectures.svg` là tổng hợp từ DOCX Buổi 7 (yêu cầu các dạng ánh xạ chuỗi) và `lec14_rnn.pdf` trang 35 (đối chiếu nhiều–sang–nhiều); không sao chép nguyên một hình duy nhất từ nguồn.

## Trạng thái kiểm định sau chỉnh sửa

- Bản hiện tại giữ 44 trang, 44 mã `data-slide-id` duy nhất, 7 `<section>` ngoài có kích thước `[7,7,8,8,5,4,5]`, và L07-39 ở cuối. Các con số này được kiểm tra tĩnh sau lượt chỉnh sửa năm báo cáo.
- Kiểm định cuối bên dưới được chạy lại trên chính bản hiện tại; không kế thừa các tuyên bố trình duyệt của bản trước.

## Biên tập và tài sản

- Mặt trang và ghi chú được rà theo no-ai-slop: câu trực tiếp, không câu hỏi tu từ, không khẩu hiệu, không kết luận chung thiếu cơ chế.
- Quill được dùng để rà chuỗi vấn đề → ví dụ vô hướng → quan hệ truy hồi → trải mạng → BPTT → tích Jacobian; không tạo `quill.json`.
- Mọi hướng dẫn về timing, tuyến, đáp án và phạm vi nằm trong `note-for-author.md`, không nằm trong ghi chú diễn giả.
- Mười bốn hình được vẽ lại bằng SVG; không dùng raster hoặc màu làm tín hiệu duy nhất.

## Đề xuất không áp dụng

- Không đưa mẫu văn bản sinh ở `lec14_rnn.pdf` 43–49: không cần cho LLO và thiếu giao thức để dùng như bằng chứng.
- Không triển khai mô hình ngôn ngữ ký tự: quy trình chỉ tạo code demo khi nguồn có nội dung code tương ứng hoặc người dùng yêu cầu; nguồn chỉ có hình minh họa, không có triển khai cần chuyển, và người dùng không yêu cầu demo.
- Không dạy cơ chế sinh chú thích hoặc dịch máy; chỉ dùng chúng để phân loại dạng ánh xạ chuỗi.
- Không tuyên bố BPTT cắt ngắn giải quyết gradient triệt tiêu/bùng nổ; nó giới hạn đường gradient và đổi bài toán tối ưu.
- Không tách L07-26 thành trang mới và không thêm SVG vòng BPTT: giữ 44 trang, chuyển công thức độ lệch vào ghi chú và giữ ba gradient trọng số trên mặt trang để giảm tải.
- Không bỏ L07-X02: trang được định vị lại thành đối chiếu hai đồ thị giám sát, tạo bước tiến từ mất mát căn chỉnh sang trục đầu ra riêng.
- Không đưa chỉ dẫn phím hoặc thời lượng vào mặt trang hay ghi chú diễn giả. Cảnh báo đặc biệt tại L07-38 chỉ nằm trong `note-for-author.md`.

## Hợp nhất năm báo cáo độc lập và chỉnh sửa

| Góc rà soát | Mức độ cao nhất | Trang chiếu | Vấn đề | Bằng chứng | Quyết định sửa |
|---|---|---|---|---|---|
| Sinh viên | trung bình | L07-23–26, L07-30 | Thiếu bước nối delta, L07-26 quá tải, ký hiệu Jacobian đến đột ngột | $\bar o_3$ đứng tách khỏi $\delta_3$; năm công thức trên một trang | Hiện phép tính $\delta_3,\delta_2,\delta_1$; chuyển gradient độ lệch vào ghi chú; nối $\bar h_t$ với $\bar H_t$. |
| Chuyên gia Học sâu | trung bình | L07-00, L07-15–16, planning | Thiếu giới thiệu RNN, hợp đồng đích toàn chuỗi và trạng thái kiểm định nhất quán | RNN xuất hiện trước dạng đầy đủ; $Y$ chỉ có dạng theo thời gian | Giới thiệu “mạng nơ-ron hồi quy (RNN)” ở L07-00; bổ sung hai kiểu $Y$ nhiều–sang–một; tách kiểm tĩnh hiện tại khỏi kiểm định trình duyệt đang chờ. |
| Toán học, thuật toán và triển khai | trung bình | L07-15, L07-30 | Hợp đồng đích nhiều–sang–một thiếu; nhãn cạnh gradient thiếu chuyển vị | Công thức dùng $Y^{(n)}$ chưa khai báo; mũi tên đỏ ghi $J_t$ | Bổ sung $Y\in\{1,\ldots,D_y\}^{N}$ hoặc $\mathbb R^{N\times D_y}$; sửa SVG thành $J_t^\top$. |
| Học thuật và giảng dạy | nghiêm trọng | L07-15–16, L07-23–25 | Mất mát phân lớp chưa định nghĩa; chuỗi phép tính delta bị đứt | Nguồn 14–17 có softmax và entropy chéo; ví dụ nhảy từ $\bar o_3$ tới ba delta | Thêm softmax theo $D_y$, entropy chéo/log-sum-exp ổn định và mất mát cho đích liên tục; hiện đầy đủ chuỗi delta trước công thức ma trận. |
| Kết nối và mạch viết | trung bình | L07-38, X01–X04, L07-39 | Điểm vào/ra nhánh mở rộng mờ; storyboard gọi X04 là kết thúc; mạch 7 có chức năng kép chưa ghi | X01 mở phân rã xác suất không có câu nối; kết luận chỉ thu hồi tuyến lõi | Thêm câu nối trong notes; X04 dẫn tới L07-39; ghi rõ mạch 7 gồm bốn trang có thể cắt và một trang kết luận bắt buộc. |

Các thay đổi không thêm, bỏ hoặc đổi thứ tự trang. Phạm vi rà lại kết nối gồm L07-13–18, L07-21–32 và L07-34–39 cùng X01–X04; các công thức đổi đáng kể ở L07-15–16, L07-23–26 và `gradient-product.svg` cần được tái rà toán học ở bước sau.

## Kiểm định cuối

- Kiểm tĩnh: 44 trang; 44 mã duy nhất; 44 ghi chú có nguồn; 7 mạch ngoài có kích thước `[7,7,8,8,5,4,5]`; thứ tự kết thúc `X01, X02, X03, X04, 39`; lõi 100 phút, mở rộng 20 phút, bài tập 50 phút. Sau khi bỏ thuộc tính `data-slide-id`, không còn mã nội bộ trên mặt trang hoặc ghi chú.
- Tài sản: HTML tham chiếu đủ 14 SVG, không dùng raster hoặc tài nguyên mạng; cả 14 SVG phân tích được như XML và có `role`, `title`, `desc`; không có đường dẫn cục bộ bị thiếu.
- KaTeX với `throwOnError: true`, `strict: "error"`: 195 phần tử `.katex`, 22 công thức khối, 0 lỗi. Công thức L07-X01 được tách thành hai dòng để không tràn ngang.
- Trình duyệt: đã duyệt và chụp 88 ảnh cho toàn bộ 44 trang ở 1280×720 và 960×720. Không có `scrollWidth` hoặc `scrollHeight` vượt khung; cỡ chữ nhỏ nhất đo được khoảng 31.8 px. Cờ hình học tự động ở L07-33 được đối chiếu trực tiếp ở cả hai kích thước: nội dung vẫn nằm trong khung và không bị cắt.
- Điều hướng: sáu ranh giới Phải đạt `06→07`, `13→14`, `21→22`, `29→30`, `34→35`, `38→X01`; tuyến lõi `L07-38 → End → L07-39`; tuyến đầy đủ `L07-38 → X01 → X02 → X03 → X04 → L07-39`. X04 có một fragment nên cần thêm một lần nhấn Xuống trước khi tới L07-39.
- HTTP: mọi HTML, CSS, JavaScript, phông KaTeX và SVG cốt lõi trả 200 hoặc 304. Chỉ `favicon.ico` không tồn tại và trả 404; không ảnh hưởng deck. `reloadserver` không có trong môi trường, nên dùng `python3 -m http.server 8766` tại `2627-1/` để kiểm định cục bộ.
