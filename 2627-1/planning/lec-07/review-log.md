# Nhật ký rà soát Bài 07

## Quyết định nguồn và phạm vi

| Quyết định | Bằng chứng và lý do |
|---|---|
| Giữ nguyên `LLO3` của BPTT | DOCX Buổi 7 dùng `LLO3`, trùng mã Buổi 02. Đây là lỗi đánh số đã được `source.md` yêu cầu giữ dấu vết; không đổi mã. |
| Giữ trục nội dung của `lec14_rnn.pdf` 3–23 | Đi từ bài toán chuỗi đến ô RNN, quan hệ truy hồi, lan truyền xuôi, BPTT và gradient dài; khớp phạm vi DOCX. |
| Chỉ dùng 35–40 và 42 trong dải phụ | 35–40 hỗ trợ dạng ánh xạ, nhiều tầng, hai chiều; 42 kiểm chứng mô hình ngôn ngữ. 43–49 không cần cho LLO. |
| Không dùng 25–33 hoặc 51–62 | `source.md` dành 25–33 cho Buổi 08 và cấm 51–62. |
| LSTM/GRU chỉ là cầu nối | DOCX nhắc đọc trước, `source.md` yêu cầu kết thúc ở giới hạn phụ thuộc dài. Không đưa công thức hoặc so sánh kiến trúc. |
| Không có lab/code demo | DOCX có lab NumPy nhưng chỉ dẫn cụ thể của người dùng khóa không code demo; thay bằng bài tập tính tay đúng 50 phút. |
| Không thêm teacher forcing, padding/masking, bucketing hoặc clipping | Không cần cho phép tính RNN cơ bản trong dải nguồn được chọn; thêm chúng sẽ mở rộng phạm vi triển khai. Không dùng cắt đoạn như lời giải mặc định vì có thể làm sai nghĩa nhãn toàn chuỗi. |

## Quyết định toán học và triển khai

- Chọn quy ước lô theo hàng và khóa $X\in\mathbb R^{N\times T\times D_x}$ cho lô đang xét: các chuỗi hoặc đoạn đã chọn có cùng $T$ và mọi bước hợp lệ. Padding/masking và bucketing cho chuỗi khác độ dài không thuộc phạm vi; không khẳng định chuỗi gốc phải được cắt đoạn.
- Nêu $H_0$ như điều kiện biên với đúng kích thước, kiểu dữ liệu và thiết bị.
- Tách tiền kích hoạt $A_t$, trạng thái $H_t$ và đầu ra $O_t$ để BPTT có biến lấy đạo hàm rõ.
- Với nhiều–sang–một, mất mát chỉ ở $O_T$ nhưng gradient vẫn truyền qua mọi trạng thái trước.
- Với nhiều–sang–nhiều căn chỉnh, khóa mẫu số $NT$; phân biệt đích chỉ số lớp $N\times T$ với đích vectơ $N\times T\times D_y$. Trường hợp không căn chỉnh được nêu nhưng không mở cơ chế giải mã hoặc teacher forcing.
- Gradient trạng thái gồm hai nhánh: đầu ra hiện tại và trạng thái tương lai. BPTT khởi tạo $G_{T+1}=0$, lặp $t=T,\ldots,1$; gradient trọng số và độ lệch cộng qua mẫu và thời gian.
- Tách đạo hàm trực tiếp $\partial h_3/\partial w_h$ khi giữ $h_2$ cố định khỏi đạo hàm toàn phần có đường qua $h_2$.
- Phát biểu triệt tiêu/bùng nổ theo tích Jacobian. Không dùng mệnh đề quá mạnh rằng chỉ giá trị kỳ dị của $W_h$ quyết định; đạo hàm tanh và hướng vectơ cũng tham gia.
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

## Biên tập và tài sản

- Mặt trang và ghi chú được rà theo no-ai-slop: câu trực tiếp, không câu hỏi tu từ, không khẩu hiệu, không kết luận chung thiếu cơ chế.
- Quill được dùng để rà chuỗi vấn đề → ví dụ vô hướng → quan hệ truy hồi → trải mạng → BPTT → tích Jacobian; không tạo `quill.json`.
- Mọi hướng dẫn về timing, tuyến, đáp án và phạm vi nằm trong `note-for-author.md`, không nằm trong ghi chú diễn giả.
- Mười bốn hình được vẽ lại bằng SVG; không dùng raster hoặc màu làm tín hiệu duy nhất.

## Đề xuất không áp dụng

- Không đưa mẫu văn bản sinh ở `lec14_rnn.pdf` 43–49: không cần cho LLO và thiếu giao thức để dùng như bằng chứng.
- Không triển khai mô hình ngôn ngữ ký tự: nguồn có hình minh họa nhưng người dùng khóa không code demo.
- Không dạy cơ chế sinh chú thích hoặc dịch máy; chỉ dùng chúng để phân loại dạng ánh xạ chuỗi.
- Không tuyên bố BPTT cắt ngắn giải quyết gradient triệt tiêu/bùng nổ; nó giới hạn đường gradient và đổi bài toán tối ưu.

## Hợp nhất báo cáo độc lập và chỉnh sửa

| Góc rà soát | Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Quyết định sửa |
|---|---|---|---|---|---|
| Sinh viên | nghiêm trọng | L07-07–13, L07-22–27 | Hai cụm công thức tổng quát xuất hiện trước ví dụ | Ví dụ vô hướng nằm sau công thức ô; ký hiệu BPTT đến trước đồ thị delta | Đưa dữ kiện và phép tính vô hướng lên L07-07–08; đưa đồ thị/delta lên L07-23–24 rồi mới khái quát. |
| Chuyên gia Học sâu | nghiêm trọng | L07-02–16 | Phạm vi chuỗi biến độ dài, padding và kiểu đích chưa khóa | $X[:,t,:]$ giống cú pháp Python; $Y$ bị đồng nhất với $O$ | Khóa lô đang xét có các mẫu cùng $T$ và mọi bước hợp lệ; để cách ghép lô chuỗi khác độ dài ngoài phạm vi; định nghĩa lát cắt toán học và hai kiểu đích. |
| Tái rà toán học | nghiêm trọng | L07-02, L07-05, L07-15 | Cắt mọi chuỗi gốc thành đoạn cùng $T$ có thể làm hỏng nhãn toàn chuỗi trong nhiều–sang–một | Nhãn $Y^{(n)}$ gắn với toàn chuỗi, không tự động gắn đúng với từng đoạn cắt | Thay bằng giả thiết cục bộ cho lô đang xét; nêu padding/masking/bucketing ngoài phạm vi và cảnh báo không tự cắt chuỗi có nhãn toàn chuỗi. |
| Tái rà storyboard | trung bình | L07-07–21, X01–X04 | L07-08 bị ghi như kiểm tra kết thúc; L18/L20 đảo vai trò; phần mở rộng bị ép thành một chu trình | Kiểm tra phải đến sau hình thức; L18 là thuật toán, L20 là phép tính số; hai cặp mở rộng dùng dữ kiện khác nhau | Giữ L07-08 là hoạt động trong ví dụ, thêm kiểm tra chia sẻ tham số ở L07-13; phân loại lại L18/L20; tách hai nhánh mở rộng rút gọn và nêu lý do. |
| Hậu kiểm chu trình | nhẹ | L07-07–21 | Hàng lan truyền xuôi chưa phản ánh rõ ví dụ đã mở trước thuật toán | L07-07–08 cung cấp trực giác và bộ số; L07-18 mới hình thức hóa vòng lặp | Khóa thứ tự L07-07–08 → L07-18 → L07-19–20 → L07-21 trong storyboard; không đổi HTML. |
| Toán học, thuật toán và triển khai | nghiêm trọng | L07-25–31 | BPTT thiếu vòng lặp, đạo hàm độ lệch và quan hệ Jacobian xuôi/ngược | $\bar H_t$ chưa định nghĩa trên mặt trang; chưa có $G_{T+1}=0$ trong thuật toán | Thêm vòng $T\to1$, $\bar O_t$, $\bar H_t$, $G_t$, tổng độ lệch, vectơ hàng $dh$ và gradient nhân $J_t^\top$. |
| Học thuật và giảng dạy | trung bình | L07-01, L07-39, X03–X04 | Tiên quyết và cầu nối còn là chỉ dẫn biên tập; mở rộng thiếu kiểm tra | Notes ghi lý do giữ mã LLO; X03 thiếu kích thước; X04 không kiểm tra nhân quả | Chuyển dấu vết LLO sang planning; bổ sung tiên quyết Jacobian/VJP; thêm kích thước tầng và câu hỏi hai chiều. |

Rà lại sau thay đổi đã bao phủ các trang bị tác động và hai trang lân cận: L07-00–19, L07-20–33, L07-37–X04. Bản vá cuối rà riêng L07-00–07, L07-06–15, L07-13–22 và L07-37–X04. Không đổi 44 trang; lõi vẫn 100 phút, mở rộng vẫn 20 phút.

## Kiểm định cuối

- 44 trang, 44 mã `data-slide-id` duy nhất, 44 khối ghi chú có nguồn và 9 đáp án dạng fragment.
- KaTeX strict: 178 biểu thức, 0 lỗi với `throwOnError: true`, `strict: "error"`.
- DOM/tài nguyên: 0 đường dẫn thiếu; 14/14 SVG được tham chiếu, không có tài sản thừa.
- SVG XML: 14/14 tệp phân tích được; mỗi tệp có `role="img"`, `title`, `desc`; nhãn nhỏ nhất 22 px.
- Timing: 44 dòng storyboard; lõi 100 phút, mở rộng 20 phút, bài tập riêng 50 phút.
- Kiểm tra tiêu đề không còn từ tiếng Anh ngoài tên/viết tắt/ký hiệu chuẩn; không có teacher forcing, masking, clipping, code demo hoặc raster.
- `LSTM|GRU` chỉ xuất hiện trên một dòng/trang cầu nối L07-39.
- `reloadserver` không có trong môi trường. Máy chủ đang có ở cổng 8765 trả HTTP 200 cho HTML và SVG; hash HTML được phục vụ khớp tệp trong kho.
- Không có Browser/Chromium/Playwright hoặc công cụ Codex Slides khả dụng trong phiên này; chưa thể tuyên bố đã rà trực quan từng trang ở hai kích thước màn hình.
