# Dàn ý Bài 10: Cơ chế chú ý

## Phạm vi và kết quả học tập

- Đối tượng: sinh viên đại học đã học mạng nơ-ron truy hồi (RNN), bộ mã hóa–giải mã, softmax, quy tắc chuỗi và tensor theo lô.
- LLO19: giải thích giới hạn của bộ mã hóa–giải mã dùng một vectơ ngữ cảnh.
- LLO20: trình bày truy vấn, khóa, giá trị, hàm điểm và trọng số chú ý trong dịch máy.
- Tuyến lõi: 33 trang, 100 phút. Tuyến mở rộng: 4 trang, 20 phút. Bài tập riêng: 50 phút.
- Trọng tâm là chú ý chéo Bahdanau. Tự chú ý chỉ là cầu nối sang Bài 11; không mở scaled dot-product hoặc nhiều đầu.
- Không có code demo hoặc benchmark; nguồn khóa cơ chế, công thức, căn chỉnh và ứng dụng.

## Cấu trúc bảy mạch

| Mạch | Trang | Chức năng | Kết nối vào | Kết nối ra |
|---|---|---|---|---|
| 1 | L10-00–03 | Mở bài và xác lập nút thắt của ngữ cảnh cố định | Tiên quyết bộ mã hóa–giải mã từ Bài 08 | Nhu cầu truy xuất nguồn theo từng bước đích |
| 2 | L10-04–07 | Giới thiệu chu trình điểm–softmax–tổng và vai trò Q/K/V | Nhu cầu truy xuất theo bước | Hợp đồng tensor cho vết số |
| 3 | L10-08–13 | Tính trọn vết điểm, trọng số và ngữ cảnh | $H,E,A,C$ đã khóa kích thước | Nhu cầu học hàm điểm thay vì cho sẵn điểm |
| 4 | L10-14–18 | Xây hàm điểm Bahdanau, phát tự động và mặt nạ nguồn | Vết số có điểm cho sẵn | Ngữ cảnh hợp lệ để cập nhật bộ giải mã |
| 5 | L10-19–26 | Nối ngữ cảnh với đầu ra, huấn luyện, suy luận và căn chỉnh | $c_{t'}$ từ chú ý có mặt nạ | Sáu phép tính riêng lẻ của một bước giải mã |
| 6 | L10-27–31 | Khép thuật toán, gradient, chi phí và kiểm tra toàn vết | Các phép tính riêng lẻ đã hoàn chỉnh | Nhánh ứng dụng mở rộng hoặc kết luận chung |
| 7 | L10-X01–X04, L10-32 | Chuyển cơ chế sang miền khác rồi kết luận và nối Bài 11 | Q/K/V trong dịch máy | Q/K/V là khung chung; Bài 11 tạo ba vai trò từ cùng chuỗi |

L10-32 là trang cuối chung và vẫn thuộc tuyến lõi 1 phút. Tại L10-31, End đi thẳng đến L10-32; phím Phải đi vào L10-X01, rồi đi xuống qua L10-X04 đến L10-32. Phím Phải được định tuyến lại tại sáu ranh giới 03→04, 07→08, 13→14, 18→19, 26→27 và 31→X01; End luôn đến L10-32.

## Mạch khái niệm

1. Nút thắt của một vectơ ngữ cảnh cố định trong bộ mã hóa–giải mã.
2. Ngữ cảnh riêng theo bước đích: điểm tương thích → softmax nguồn → tổng có trọng số.
3. Định nghĩa tổng quát $\operatorname{Attention}(q,\{(k_i,v_i)\})=\sum_i\alpha(q,k_i)v_i$; trong Bahdanau, truy vấn từ bộ giải mã còn khóa và giá trị từ các trạng thái bộ mã hóa.
4. Vết số xuyên suốt $e=(1,2,0)$ và $H=[(1,0),(0,2),(-1,1)]$.
5. Hàm điểm cộng Bahdanau theo vectơ hàng, kích thước và số tham số, phát tự động và mặt nạ nguồn.
6. Cập nhật bộ giải mã, logit, chéo entropy ổn định, học theo đáp án và suy luận tự hồi quy.
7. Ma trận căn chỉnh mềm và giới hạn của việc diễn giải trọng số chú ý.
8. Thuật toán một bước, đường đạo hàm, chi phí và so sánh với ngữ cảnh cố định.
9. Ứng dụng ảnh và cặp văn bản ở tuyến mở rộng; kết luận chung thu hồi nút thắt → truy xuất theo bước → Q/K/V rồi nối sang Bài 11 mà không triển khai tự chú ý.

## Ánh xạ nguồn

| Nguồn | Phạm vi dùng | Vai trò |
|---|---|---|
| DOCX đề cương, III.2 → Buổi 10 | Tên buổi, LLO19–LLO20, phạm vi chú ý | Khóa ranh giới bài |
| `source-materials/slides/lec15_attention.pdf`, PDF 3–17 | Nút thắt seq2seq, ngữ cảnh theo bước, điểm, softmax, tổng giá trị, căn chỉnh | Dùng PDF 3–14 cho mạch lõi; bỏ PDF 15–17 về benchmark theo độ dài và GNMT vì ngoài LLO và thiếu giao thức cần để diễn giải kết quả |
| Cùng tệp, PDF 19–27 | Tổng quát hóa chú ý và mô tả ảnh | Tuyến mở rộng; không dùng benchmark |
| Cùng tệp, PDF 30–41 | Truy vấn–khóa–giá trị và cầu nối Transformer | Chỉ dùng vai trò Q/K/V và một trang cầu nối tự chú ý |
| `source-materials/textbooks/hocsau_draft.pdf`, PDF 239–245 | Bộ mã hóa–giải mã, học theo đáp án, mặt nạ đích | Khôi phục tiên quyết triển khai |
| Cùng tệp, PDF 258–263 | Chú ý tổng quát, Bahdanau, công thức, căn chỉnh, giới hạn diễn giải | Kiểm chứng toán và ký hiệu |
| Cùng tệp, PDF 323–327 | Chú ý có thể phân rã cho cặp văn bản | Ứng dụng mở rộng |

## Tài sản trực quan

| Tệp SVG | Nội dung | Nguồn |
|---|---|---|
| `bottleneck.svg` | Một ngữ cảnh cố định cho mọi bước đích | lec15 PDF 5–8 |
| `cross-attention.svg` | Luồng truy vấn → điểm → trọng số → ngữ cảnh | lec15 PDF 9–13 |
| `trace-attention.svg` | Vết số $H,e,\alpha,c$ | Công thức nguồn; số tự tính |
| `bahdanau-score.svg` | Mạng tính điểm cộng | GT PDF 260–261 |
| `alignment.svg` | Ma trận căn chỉnh mềm $3\times3$ | lec15 PDF 12–14; số tự tính |
| `train-infer.svg` | Token đầu vào khi huấn luyện và suy luận | GT PDF 242–245 |
| `applications.svg` | Ánh xạ Q/K/V trong ba ứng dụng | lec15 PDF 19–24; GT PDF 323–327 |

## Ký hiệu

| Ký hiệu | Nghĩa và kích thước |
|---|---|
| $N,T_s,T'$ | Kích thước lô, số bước nguồn tối đa, số bước đích |
| $L_n$ | Độ dài nguồn thật của mẫu $n$, gồm EOS và $1\le L_n\le T_s$ |
| $H$ | Trạng thái mã hóa, $N\times T_s\times D_h$ |
| $h^{enc}_{n,L_n},\phi$ | Trạng thái mã hóa cuối hợp lệ của mẫu $n$; phép đồng nhất hoặc phép chiếu học được để khởi tạo bộ giải mã |
| $S^-,s_{n,t'-1}$ | Trạng thái giải mã trước, $N\times D_s$ hoặc một hàng $1\times D_s$ |
| $s_{n,0}$ | Trạng thái giải mã đầu, $s_{n,0}=\phi(h^{enc}_{n,L_n})\in\mathbb R^{D_s}$; không lấy vị trí đệm |
| $R_q,R_h$ | Biểu diễn truy vấn và trạng thái nguồn sau phép chiếu, $N\times D_a$ và $N\times T_s\times D_a$ |
| $E,A$ | Điểm và trọng số ở một bước đích, $N\times T_s$ |
| $\mathcal A$ | Ma trận căn chỉnh của một mẫu, $T'\times T_s$ |
| $C$ | Ngữ cảnh ở một bước đích, $N\times D_h$ |
| $E_y,D_e$ | Ma trận nhúng token đích, $V_{tgt}\times D_e$; chiều vector nhúng |
| $g$ | Ô truy hồi của bộ giải mã, như RNN hoặc GRU |
| $W_o,b_o$ | Trọng số và độ lệch chiếu $[s_{t'};c_{t'}]$ thành logit từ vựng; $(D_s+D_h)\times V_{tgt}$ và $V_{tgt}$ |
| $O_{t'},P_{t'}$ | Logit và xác suất đầu ra, $N\times V_{tgt}$; toàn chuỗi $O$ có shape $N\times T'\times V_{tgt}$ |
| $D_a$ | Chiều ẩn của mạng tính điểm cộng |
| $M^{src},M^{tgt}$ | Mặt nạ vị trí nguồn hợp lệ; mặt nạ token đích trong mất mát |
| $V_{tgt}=|\mathcal V_{tgt}|$ | Kích thước từ vựng đích; không nhầm với tensor giá trị attention |
| $q,k_i,v_i$ | Truy vấn, khóa và giá trị; trong Bahdanau: $q=s_{t'-1}$, $k_i=v_i=h_i$ |

## Vết số khóa

$$H=[(1,0),(0,2),(-1,1)],\qquad e=(1,2,0).$$

$$\alpha=(0.244728,0.665241,0.090031),\qquad c=(0.154698,1.420512).$$

Nếu vị trí ba là đệm: $\alpha=(0.268941,0.731059,0)$ và $c=(0.268941,1.462117)$.

Các điểm trong vết được cho sẵn sau mạng score; hai hàng mở rộng của heatmap là dữ liệu tự xây để minh họa cực đại đổi thứ tự, không phải căn chỉnh ngôn ngữ học và không được suy ngược từ một bộ tham số Bahdanau cụ thể.

## Hợp đồng triển khai bổ sung

- Mỗi hàng masked softmax có ít nhất một vị trí nguồn hợp lệ nhờ EOS. Dùng $-\infty$ khi phép toán hỗ trợ; sentinel hữu hạn chỉ làm trọng số đệm xấp xỉ 0 và hàng toàn mask phải được xử lý riêng.
- Với LSTM, truy vấn dùng trạng thái ẩn của decoder, không dùng trạng thái ô.
- Suy luận theo lô dùng mặt nạ hoạt động hoặc thu gọn lô để giữ nguyên trạng thái của mẫu đã sinh EOS.
- Mạng điểm có $D_a(D_s+D_h+2)$ tham số. Chi phí chú ý là $\Theta(NT_sD_hD_a+NT'D_sD_a+NT'T_s(D_a+D_h))$; lưu kích hoạt $U$ cho lan truyền ngược có thể cần $\Theta(NT'T_sD_a)$ bộ nhớ.
