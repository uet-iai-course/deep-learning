# Nhật ký rà soát Bài 10

## Quyết định nguồn và phạm vi

| Quyết định | Bằng chứng và lý do |
|---|---|
| Giữ mạch Bahdanau trong dịch máy | `lec15_attention.pdf` PDF 3–17 đi từ nút thắt seq2seq đến ngữ cảnh theo bước và căn chỉnh; đúng LLO19–LLO20 |
| Dùng PDF 19–27 ở tuyến mở rộng | Dải này mở rộng cùng cơ chế sang vùng ảnh; không cần cho chu trình lõi |
| Chỉ dùng PDF 30–41 làm cầu nối | Bài 11 mới khóa self-attention và Transformer; L10-32 chỉ phân biệt nguồn Q/K/V |
| Dùng GT PDF 239–245 | Khôi phục hợp đồng học theo đáp án, EOS và mặt nạ đích từ bộ mã hóa–giải mã |
| Dùng GT PDF 258–263 | Kiểm chứng công thức chú ý tổng quát, Bahdanau, ngữ cảnh và cảnh báo diễn giải |
| Dùng GT PDF 323–327 | Một ứng dụng mở rộng căn chỉnh hai chiều cho cặp văn bản |
| Không dùng benchmark | LLO yêu cầu cơ chế và phân tích; giao thức benchmark không cần để đạt sản phẩm học tập |
| Không có code demo | Nguồn và yêu cầu không giao chuyển code; bài tập dùng tính tay và phân tích |

## Sai khác có chủ ý

- Chuyển công thức Bahdanau từ quy ước vectơ cột của giáo trình sang vectơ hàng để khớp các deck trước: $sW_s+hW_h+b_a$, sau đó nhân $v_a$. Quan hệ toán học giữ nguyên sau chuyển vị tham số.
- Bổ sung kích thước theo lô, trục softmax, phát tự động, mặt nạ nguồn trước softmax và chéo entropy hợp nhất từ logit. Đây là chi tiết triển khai cần thiết nhưng slide nguồn không ghi đầy đủ.
- Tạo trace số $e=(1,2,0)$ và ba giá trị hai chiều để nối ví dụ → hình thức → mặt nạ → căn chỉnh → kiểm tra. Các số không phải kết quả thực nghiệm và được ghi là ví dụ tự tính.
- Ma trận căn chỉnh L10-24 dùng hai hàng điểm hoán vị ngoài hàng trace đầu để minh họa truy vấn thay đổi. Không trình bày nó như dữ liệu quan sát.
- Thu hẹp mệnh đề “attention giải quyết nút thắt” thành “giảm nút thắt ngữ cảnh cố định”; không khẳng định loại bỏ mọi giới hạn của RNN hoặc bảo đảm dịch đúng.
- Không đồng nhất trọng số chú ý với giải thích nhân quả. L10-26 giữ đúng cảnh báo của `source.md` và giáo trình PDF 262–263.

## Tự tính ví dụ

| Đại lượng | Giá trị đầy đủ | Hiển thị |
|---|---:|---:|
| $\exp(-1)$ | 0.3678794412 | 0.3679 |
| $\exp(-2)$ | 0.1353352832 | 0.1353 |
| $\alpha_1$ | 0.2447284711 | 0.2447 |
| $\alpha_2$ | 0.6652409558 | 0.6652 |
| $\alpha_3$ | 0.0900305732 | 0.0900 |
| $c_1=\alpha_1-\alpha_3$ | 0.1546978979 | 0.1547 |
| $c_2=2\alpha_2+\alpha_3$ | 1.4205124847 | 1.4205 |
| $\alpha$ khi vị trí 3 đệm | $(0.2689414214,0.7310585786,0)$ | $(.2689,.7311,0)$ |
| $c$ khi vị trí 3 đệm | $(0.2689414214,1.4621171573)$ | $(.2689,1.4621)$ |

## Rà mạch và biên tập

- no-ai-slop: mặt trang dùng câu trực tiếp, không khẩu hiệu, câu hỏi tu từ, benchmark không có giao thức hoặc lời dẫn về chính văn bản.
- Quill: ký hiệu xuất hiện theo thứ tự $H,S^-$ → $e$ → $\alpha$ → $c$ → $s_{t'}$ → logit; trace được dùng lại đến kiểm tra cuối. Không tạo `quill.json`.
- Chu trình sáu bước được khóa trong storyboard. Công thức softmax xuất hiện sau bộ số; công thức điểm xuất hiện sau sơ đồ trực giác.
- Chỉ dẫn tuyến, đáp án và điểm cần kiểm chứng nằm trong `note-for-author.md`, không đặt trong ghi chú diễn giả.

## Chỉnh sửa sau phản biện độc lập

- Sửa ba byte carriage-return làm hỏng `\rightarrow` ở L10-04 và sửa `alpha_i` thành `\alpha_i` ở L10-10.
- Khóa quy ước vectơ hàng ở cả HTML và `bahdanau-score.svg`: $sW_s$, $hW_h$, rồi nhân $v_a$; dùng $t'$ nhất quán cho thời gian đích.
- Bổ sung $s_{n,0}=\phi(h^{enc}_{n,L_n})$ từ trạng thái cuối hợp lệ, shape của phép khởi tạo và lưu ý hidden/cell state của LSTM.
- Giữ $H$ là trạng thái nguồn/khóa và giá trị thô; đổi tên hai biểu diễn chiếu thành $R_q,R_h$ để không tái định nghĩa Q/K. Làm rõ broadcasting, phép co với $v_a$ và số tham số $D_a(D_s+D_h+2)$.
- Bổ sung điều kiện mỗi hàng masked softmax có ít nhất một vị trí hợp lệ, hành vi của $-\infty$, sentinel hữu hạn và hàng toàn mask.
- Đổi kích thước từ vựng thành $V_{tgt}$, bổ sung shape $W_o,b_o,O$ toàn chuỗi, reduction token hợp lệ và điều kiện mẫu số dương nhờ EOS.
- Tách gradient tới encoder thành đường giá trị và đường khóa/điểm, đồng thời nêu đường truy vấn; thêm active mask cho mẫu suy luận đã kết thúc.
- Gắn token nguồn/đích và nhãn “dữ liệu tự xây” cho heatmap; thu hẹp L10-25 thành ba hàng điểm cho sẵn, không suy ngược tham số Bahdanau.
- Định lượng thời gian và bộ nhớ của khối attention, gồm kích hoạt $U$ khi backward.
- Sửa điều hướng: đi xuống xuyên suốt tuyến lõi và chỉ đi phải tại L10-32; bổ sung câu chuyển ở các ranh giới khái niệm và bảng lý do/đầu ra kiểm chứng trong storyboard.
- Đổi ví dụ tuyến mở rộng thành “tra cứu bản ghi theo khóa” và đổi tiêu đề L10-32 để nói rõ Q/K/V cùng được tạo từ một chuỗi.
- Sửa `cross-attention.svg` để mỗi $h_i$ đi rõ hai nhánh: nhánh khóa vào hàm điểm rồi softmax tạo $\alpha_{t',i}$, và nhánh giá trị vào $\sum_i\alpha_{t',i}h_i$ để tạo $c_{t'}$. Dùng bus $H_{1:T_s}$ để giữ sơ đồ dễ đọc.

Đề xuất không áp dụng: không thêm code, scaled dot-product, causal mask, multi-head hoặc benchmark vì vượt phạm vi Bài 10; không đổi số trang hay timing vì sửa cục bộ đã đủ và tuyến lõi/mở rộng vẫn là 100/20 phút.

## Kiểm định tĩnh

- 37 trang, 37 mã `data-slide-id` duy nhất, 37 khối ghi chú và 37 dòng timing; thứ tự HTML khớp storyboard.
- KaTeX strict dựng 134 biểu thức với `throwOnError: true`, `strict: "error"`, không lỗi sau chỉnh sửa.
- Timing: lõi 100 phút, mở rộng 20 phút, bài tập riêng 50 phút.
- 8 câu hỏi đều có nhãn `Câu hỏi:` và phản hồi dạng fragment.
- 17 tài nguyên tương đối, 0 đường dẫn thiếu; không có ảnh raster hoặc phụ thuộc mạng cốt lõi.
- 7 SVG đều được tham chiếu; tất cả phân tích XML được, có `role="img"`, `title`, `desc` và cỡ chữ nhỏ nhất 22 px.
- Cấu trúc `section`, `div`, `aside`, `table` cân bằng; tiêu đề đã rà thuần Việt, chỉ giữ tên riêng và ký hiệu chuẩn.
- Không có chỉ dẫn nội bộ trong ghi chú diễn giả; không có và không tạo `quill.json`.
- Không chạy HTTP, Browser hoặc Codex Slides trong lượt soạn; điều phối viên thực hiện kiểm định trực quan sau cùng.
- Không sửa `index.html`; không commit/push.

Hậu kiểm lượt chỉnh sửa: không còn byte điều khiển ngoài tab/newline; 37 ID duy nhất, 37 ghi chú, 2 cột RevealJS (lõi và mở rộng), cấu trúc section/div/aside cân bằng; timing vẫn 100/20 phút; 17 tham chiếu tài nguyên đều tồn tại; 7 SVG phân tích XML thành công. Không có project ID hoặc phiên Codex Browser trong tác vụ này, nên xác minh hiển thị trực quan vẫn do điều phối viên thực hiện.

Hậu kiểm montage cục bộ cho thấy bộ dựng raster không hiển thị ổn chỉ số Unicode trong SVG. Nhãn kỹ thuật được đổi sang dạng ngoặc như `h(1)`, `s(t′−1)` và `α(t′,i)` để đọc ổn định hơn; quan hệ toán học và dữ liệu không đổi. Montage sau sửa không còn nhãn mất chỉ số hoặc chồng lấn rõ ràng.

Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy được vì môi trường thiếu mô-đun `reloadserver`. Máy chủ HTTP cục bộ đang có tại cổng 8765 trả mã 200; SHA-256 của bản phục vụ trùng tệp HTML trong kho. Browser và Codex Slides không khả dụng, nên chưa thể xác nhận trực quan từng trang ở hai kích thước màn hình; không tuyên bố đã thực hiện bước này.
