# Nhật ký rà soát Bài 03

## Trạng thái nguồn và chặn bàn giao

- Phạm vi DOCX của Buổi 3 được giữ nguyên. Nguồn chính là `lec10_training.pdf`, các dải đã khóa trong `source.md`; giáo trình chỉ kiểm chứng các mục được ánh xạ.
- Chặn L1 đã đóng bằng nguồn bổ sung được người dùng duyệt: Goodfellow, Bengio và Courville, §7.1.2, trang in 230–232, (7.18)–(7.23), bản chính thức tại `https://www.deeplearningbook.org/contents/regularization.html`.
- Không dùng raster hoặc code demo. Nguồn web duy nhất là bản sách chính thức đã duyệt cho L1. Dự án Codex Slides `20260826084351-b-i-03-t-i-u-h-a-m-ng-n-ron-a-l-p-liye` đã lưu bền vững `generated/outline.md`, nhưng vẫn ở checkpoint làm rõ với 0 trang; phiên này không có Browser để rà hiển thị nên không tuyên bố đã kiểm tra trực quan bằng Codex Slides.

## Sai khác và quyết định nguồn

| Nguồn/vị trí | Sai khác hoặc rủi ro | Quyết định |
|---|---|---|
| `lec10_training.pdf`, PDF 14 | Nhãn nguồn không khớp công thức trung bình trượt bình phương gradient | Gọi đúng RMSprop; thêm $s_0=0$ để ví dụ xác định duy nhất |
| `lec10_training.pdf`, PDF 15 | Adam dễ bị học như công thức không có trạng thái số | Thêm ví dụ $t=1$ với $m_0=v_0=0$, $\beta_1=.9,\beta_2=.999$ và cùng $w_0,g_1,\eta$ |
| `lec10_training.pdf`, PDF 16–17 | Nhận xét thực hành có thể thành xếp hạng phổ quát | So cơ chế, trạng thái $0/P/P/2P$, độ nhạy và giao thức; không xếp hạng |
| `lec10_training.pdf`, PDF 23; GT PDF 100 | $h_1=h_2$ riêng lẻ không đủ suy gradient bằng nhau | Yêu cầu đối xứng cả kết nối vào và kết nối ra/tín hiệu ngược |
| `lec10_training.pdf`, PDF 24; GT 100–102 | Xavier/Kaiming có giả thiết | Ghi giới hạn về độc lập, trung bình gần 0, loại kích hoạt và kiến trúc |
| `lec04_multiclass.pdf`, PDF 19 | L03-10 từng dẫn GT 58–63 không hỗ trợ trực tiếp | Bỏ GT 58–63; giữ nguồn softmax đúng dải |
| GT PDF 96–100 | Chuỗi Jacobian | L03-11 chỉ dùng dải này, bỏ nguồn phụ không cần thiết |
| `lec10_training.pdf`, PDF 35–41; GT 64–66,103–105 | L2 và dropout khác loại điều chuẩn | L2 là phạt trên $\mathcal W$; dropout là nhiễu ngẫu nhiên; bias và $\gamma,\beta$ thường cấu hình riêng, không thành quy tắc tuyệt đối |
| Goodfellow et al. §7.1.2, (7.18)–(7.23) | Nguồn dùng $\alpha$ và phân tích hồi quy tuyến tính không bias | Đổi $\alpha$ thành $\lambda$ để thống nhất deck; dùng $L_{data}$ như minh họa xấp xỉ cục bộ; ghi rõ Hessian chéo $H_{ii}>0$ và không suy rộng nghiệm cho mọi mạng sâu |
| `lec10_training.pdf`, PDF 39; GT 103–105 | Hai quy ước dropout dễ lẫn | Dùng dropout đảo tỷ lệ, $0\le p<1$; tách kỳ vọng huấn luyện và ánh xạ đồng nhất suy luận |
| GT PDF 153–155 | Công thức BN trừu tượng | Thêm ví dụ MLP $2\times2$ tính $\mu,\sigma^2,\hat X,Y$; không đưa CNN vào lõi |
| `lec10_training.pdf`, PDF 28; GT 156–157 | Nguồn không khóa công thức cập nhật thống kê suy luận | Viết trung tính: thống kê cố định được ước lượng trong huấn luyện; không khẳng định EMA/hệ số chạy |
| `lec10_training.pdf`, PDF 33; GT 155–157 | Nguồn hỗ trợ BN/LN, không đủ cho InstanceNorm/GroupNorm | X04 chỉ so BN và LN; vẽ lại SVG |
| `lec05_multilayer.pdf`, PDF 42–46; GT 62 | Tinh chỉnh cần hai vòng và khóa tập kiểm tra | L03-41–42 dùng $c\in\mathcal C$, $\theta^*(c)$ và $c^*$; giữ $\lambda$ cho hệ số điều chuẩn, không dùng làm ký hiệu cấu hình |
| `lec05_multilayer.pdf`, PDF 42–46 | X03 cũ vượt nguồn khi áp đặt tìm kiếm nhiều giai đoạn | Thay bằng kiểm kê nhóm siêu tham số và vòng ghi cấu hình |

## Ví dụ số đã kiểm lại

- Mômen: $u_1=(-.2,-.05)$, $w_1=(.8,-1.05)$, $u_2=(-.38,.005)$, $w_2=(.42,-1.045)$.
- RMSprop: $w_0=(1,-1)$, $g_1=(2,.5)$, $s_0=0$, $\beta=.9$, $\eta=.1$. Khi bỏ $\varepsilon$ để tính nhẩm, $s_1=(.4,.025)$ và $w_1\approx(.6838,-1.3162)$.
- Adam: cùng $w_0,g_1,\eta$, $\beta_1=.9,\beta_2=.999$, $m_0=v_0=0$. $m_1=(.2,.05)$, $v_1=(.004,.00025)$, $\hat m_1=(2,.5)$, $\hat v_1=(4,.25)$, $w_1=(.9,-1.1)$ khi bỏ $\varepsilon$ để tính nhẩm.
- L2: $(1-.1\cdot.05)(2,-1)-.1(.4,-.2)=(1.95,-.975)$.
- L1 tại $w=(2,-.5,0)$, $\lambda=.1$: đóng góp đạo hàm dưới là $(.1,-.1,.1s)$ với $s\in[-1,1]$; tọa độ 0 nhận khoảng $[-.1,.1]$.
- Ngưỡng mềm: $\lambda=.2$, $H_{ii}=.5$ cho ngưỡng $.4$; $.3\mapsto0$ và $-.9\mapsto-.5$.
- Dropout: $h=(2,-1,4)$, $p=.5$, $m=(1,0,1)$ cho $h^{tr}=(4,0,8)$ khi huấn luyện; kỳ vọng theo mặt nạ bằng $h$; suy luận dùng $h$.
- BN: $X=[[1,3],[3,7]]$, $\mu=(2,5)$, $\sigma^2=(1,4)$, $\hat X=[[-1,-1],[1,1]]$ khi tính nhẩm với $\varepsilon=0$; $\gamma=(2,.5),\beta=(1,-1)$ cho $Y=[[-1,-1.5],[3,-.5]]$.

## Kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Trạng thái/đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | Toàn tuyến lõi | Tổng timing thực là 102 phút | Hai trang mở đầu cùng 2 phút | Đã sửa L03-00 và L03-01 còn 1 phút; lõi đúng 100 |
| trung bình | L03-06–08 | Công thức SGD đứng trước trực giác/kiểm tra | Cụm thiếu tình huống về hướng nhiễu | Đã gộp trực giác vào L03-06 và câu hỏi miền lịch vào L03-08; ghi lý do gộp |
| trung bình | Các điểm nối | Thiếu câu chuyển 14→15, 23→24, 32→33, 38→39 | Notes kết thúc rời cụm | Đã thêm đủ bốn câu chuyển |
| trung bình | L03-37, X04 | Tensor trace BN lẫn MLP/CNN | Lõi đổi loại tensor giữa hai trang | L03-37 giữ $B\times D$; so trục BN/LN chuyển X04 |
| nhẹ | L03-42 | Hướng điều hướng sai | Storyboard ghi phím xuống dù phần kế là ngang | Đã sửa thành phím phải |

## Bốn báo cáo rà soát độc lập

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Trạng thái/đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | L03-20,22 | Mục tiêu “tính cập nhật” nhưng slide không tính trạng thái | RMSprop chỉ hỏi tỷ số; Adam chỉ có công thức | Đã thêm phép tính đầy đủ từ trạng thái 0 |
| nghiêm trọng | L03-37 | CNN xuất hiện trong lõi khi tensor trace là MLP | Người học đổi trục và ký hiệu đột ngột | Đã thay bằng ví dụ BN MLP số |
| trung bình | L03-14,27 | Câu hỏi lộ đáp án ngay | Đáp án hiện cùng khung hình | Đã dùng fragment để hiện sau thao tác tiến |
| trung bình | Toàn deck/SVG | Chữ nhỏ và đồ thị dựa vào màu | `.tiny` hiệu dụng .567em; nét curve giống nhau | Đã nâng `.tiny`/table, thêm nét đứt/chấm-gạch và nhãn trục cho đồ thị chính |
| trung bình | Thuật ngữ | Pha Anh–Việt làm tăng tải | kích hoạt, bộ tối ưu và chế độ mô hình từng dùng không nhất quán | Đã Việt hóa nội dung giảng; chỉ giữ tên chuẩn/API khi cần |

### Chuyên gia Học sâu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Trạng thái/đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | Phạm vi L1 | DOCX có L1 nhưng nguồn ban đầu chưa đủ | Chỉ có công thức GT 66 | Đã đóng sau khi người dùng duyệt Goodfellow et al. §7.1.2; thêm L03-29–30 với giới hạn giả thiết rõ |
| nghiêm trọng | L03-23 | So sánh bộ tối ưu thiếu điều kiện | Bản cũ chỉ nói giao thức, không chỉ trạng thái/cơ chế | Đã thêm bảng $0/P/P/2P$, cơ chế và miền cần thử; không xếp hạng |
| nghiêm trọng | L03-41–42 | Thiếu vòng trong/vòng ngoài | Bản cũ chỉ nói chia tập và bảng chẩn đoán | Đã thay bằng ký hiệu cấu hình, ngân sách, xác thực và khóa tập kiểm tra |
| trung bình | L03-25–34 | Phân loại điều chuẩn chưa rõ | L2, L1, suy giảm trọng số và dropout nằm liên tiếp nhưng khác cơ chế | Đã tách hạng phạt L2/L1, suy giảm tách rời và nhiễu dropout; tập trọng số chịu phạt rõ ràng |
| trung bình | L03-13,24 | Phát biểu dễ quá rộng | Khởi tạo/tổng quát hóa thiếu điều kiện | Đã thêm giới hạn Xavier/Kaiming và caveat thích nghi xác thực |

### Độ chính xác toán học, thuật toán và triển khai

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Trạng thái/đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | L03-12 | Suy gradient từ $h_1=h_2$ không hợp lệ | Gradient còn phụ thuộc kết nối ra | Đã yêu cầu đối xứng đường vào, đường ra và tín hiệu ngược |
| nghiêm trọng | L03-20,22 | Ví dụ thiếu trạng thái ban đầu và bước cập nhật | Kết quả không xác định duy nhất/không kiểm được | Đã ghi $s_0,m_0,v_0=0$ và tính đủ kết quả |
| nghiêm trọng | L03-39 | Khẳng định cập nhật thống kê chạy/EMA vượt nguồn | Dải nguồn chỉ khóa thống kê suy luận cố định | Đã viết trung tính và sửa SVG |
| trung bình | L03-08 | Thiếu miền $K,T,t$ | Lịch cosin/bước không khóa chỉ số | Đã thêm $K,T>0$, $0\le t\le T$ |
| trung bình | L03-32 | Thiếu miền p và trộn kỳ vọng với suy luận | $p=1$ làm chia 0; hai đẳng thức không cùng chế độ | Đã thêm $0\le p<1$, ký hiệu huấn luyện/suy luận riêng |
| trung bình | L03-37 | Ví dụ BN thiếu shape/broadcasting | Bản cũ chỉ so trục | Đã tính số và ghi mọi shape |

### Phản biện học thuật và giảng dạy

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Trạng thái/đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | L1 | Không đủ bằng chứng để dạy đúng phạm vi trong bản nguồn ban đầu | Thiếu nguồn tác dụng và đạo hàm dưới | Đã đóng bằng nguồn chính thức được duyệt; không mở API/code/Bayes/Laplace/prox ngoài đặc tả |
| nghiêm trọng | L03-X03 | Truy nguyên dừng sớm/K-fold sai | GT 64–66 không hỗ trợ nội dung | Đã thay bằng kiểm kê cấu hình từ lec05 PDF 42–46 và các dải lec10 đã ánh xạ |
| nghiêm trọng | L03-X04 | InstanceNorm/GroupNorm vượt bằng chứng | Nguồn chỉ đủ BN/LN | Đã bỏ hai loại và vẽ lại SVG chỉ BN/LN |
| trung bình | L03-10–12,41 | Dẫn nguồn không khớp | GT58–63 ở L03-10; nguồn quá rộng ở L03-41 | Đã sửa L03-10, L03-11, L03-12, L03-41 theo dải yêu cầu |
| trung bình | L03-37–42 | Mạch từ BN sang tinh chỉnh thiếu cầu nối | Bản cũ kết thúc BN rồi nhảy sang chia tập | Đã nối kiểm tra BN ở L03-40 với hai vòng lựa chọn L03-41–42 |

Mọi lỗi chặn, nghiêm trọng và trung bình có căn cứ đã được xử lý. Chặn L1 đã đóng bằng nguồn bổ sung được duyệt.

## Hậu kiểm vòng hai

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Trạng thái xử lý |
|---|---|---|---|---|
| trung bình | L03-41–42, X03 | Dùng $\lambda$ cho cả cấu hình làm lẫn với hệ số điều chuẩn | $\lambda$ đã có nghĩa ở L03-25–30 | Đã đổi cấu hình thành $c\in\mathcal C$; $\lambda$ chỉ dùng cho hệ số L2/L1 theo công thức đang xét |
| nghiêm trọng | L03-X03 | Chiến lược rộng–hẹp vượt nguồn | lec05 PDF 42–46 chỉ hỗ trợ nhóm siêu tham số và vòng thử | Đã thay bằng kiểm kê cấu hình |
| trung bình | L03-06,25,41 | Hình thức đứng trước trực giác | Công thức xuất hiện trước tình huống/thẻ quy trình | Đã đặt trực giác trước công thức và ghi lý do gộp |
| trung bình | L03-12 | Chưa định nghĩa $\bar h_j$ | Ký hiệu xuất hiện trong điều kiện đối xứng | Đã thêm $\bar h_j=\partial L/\partial h_j$ |
| trung bình | L03-20,22,37 | Điều kiện bỏ $\varepsilon$ chỉ nằm trong notes | Kết quả số trông như triển khai chính xác | Đã ghi tính tay $\varepsilon=0$, triển khai $\varepsilon>0$ |
| trung bình | L03-40 | Cụm BN thiếu kiểm tra dùng lại tensor | Không kiểm trục bằng ví dụ L03-37 | Đã thêm câu hỏi với $X:2\times2$ |
| nhẹ | L03-09,13 | Dải GT chưa đúng hậu kiểm | Cần GT96–100 và GT98–100 | Đã sửa HTML và storyboard |
| trung bình | L03-40 | Câu hỏi hậu kiểm mô tả sai đối tượng bị trộn | Rút gọn qua $D$ trộn đặc trưng trong mỗi mẫu, không trộn mẫu | Đã sửa câu hỏi và đáp án notes |
| trung bình | L03-X03 | Nguồn lec05 chưa đủ cho khởi tạo/dropout | Hai nhóm này đến từ dải lec10 đã ánh xạ | Đã bổ sung lec10 PDF 23–24, 39–41 |
| trung bình | Chu trình ổn định/điều chuẩn/siêu tham số | Nhãn bước và thứ tự ví dụ chưa đồng bộ | L03-10 thiếu ví dụ; L03-25 và L03-41 gộp nhiều bước | Đã thêm ví dụ logit/câu kiểm tra và sửa bảng chu trình cùng lý do gộp |
| trung bình | Toàn deck/planning | Thuật ngữ và chữ phụ còn khó đọc | Planning còn Anh–Việt; `.81×.82=.664em` dưới khuyến nghị | Đã Việt hóa thuật ngữ, sửa SVG và nâng `.compact`, `.tiny`, bảng lên `.93em` (hiệu dụng `.753em`) |

## Kiểm tra biên tập và giới hạn

### Bản vá L1 theo nguồn bổ sung đã duyệt

- Chèn L03-29–30 sau L03-28; đổi ID các trang dropout, chuẩn hóa theo lô và tinh chỉnh cũ từ L03-29–40 thành L03-31–42. Giữ nguyên L03-X01–X05.
- L03-29 đặt ví dụ $w=(2,-.5,0)$, $\lambda=.1$ và trực giác lực theo dấu trước mục tiêu $\widetilde J=L_{data}+\lambda\lVert w\rVert_1$ cùng đạo hàm dưới tại 0. L03-30 đặt hai tọa độ và ngưỡng trước định nghĩa độ cong, giả thiết Hessian chéo và nghiệm ngưỡng mềm.
- Đổi ký hiệu $\alpha$ của nguồn thành $\lambda$ để nối với cụm điều chuẩn hiện có. Không mở API, code, Bayes/Laplace hoặc thuật toán proximal; chỉ kết luận L1 khuyến khích tham số thưa.
- Rà lại vùng bị ảnh hưởng và hai trang lân cận mỗi phía: L03-23–33. Hai câu nối L03-28→29 và L03-30→31 nằm trong mạch nói, không phải chỉ dẫn điều hướng.
- Timing cuối: L03-25 giảm 2→1 phút; L03-26 giảm 3→2; L03-29 và L03-30 tăng 2→3. Chọn rút L03-25 vì đây là cầu nối một trực giác và một công thức; nội dung vẫn đọc được trong 1 phút. Tuyến lõi giữ 100 phút, mở rộng 20 phút, bài tập riêng 50 phút.

### Hợp nhất bốn phản biện sau bản vá L1

| Góc rà soát | Mức độ | Trang chiếu | Vấn đề | Quyết định sửa |
|---|---|---|---|---|
| Sinh viên | nghiêm trọng | L03-29–30 | Công thức xuất hiện trước tình huống; đạo hàm dưới và Hessian bị giả định là tiên quyết | Đặt vectơ/lực theo dấu và hai tọa độ/ngưỡng lên trước; định nghĩa đạo hàm dưới trong notes và $H_{ii}$ trên mặt trang. |
| Chuyên gia Học sâu | trung bình | L03-28–31 | Thiếu cầu nối giữa L2, L1 và dropout; phạm vi nghiệm L1 dễ bị hiểu rộng | Thêm hai câu nối cơ chế; khóa kết luận ở tác dụng khuyến khích độ thưa và xấp xỉ cục bộ. |
| Toán học, thuật toán và triển khai | trung bình | L03-26,28 | Diễn giải co thiếu điều kiện $0\le\eta\lambda\le1$ | Thêm điều kiện co và ví dụ $\eta\lambda=.005$. |
| Học thuật và giảng dạy | trung bình | L03-25–30, X03 | Hai slide L1 thiếu thời gian; kiểm kê chỉ nêu L2 | Phân bổ 3 phút cho mỗi slide L1, rút L03-25 và L03-26 mỗi trang 1 phút; đổi X03 thành hệ số L1/L2. |

- Đã rà theo `no-ai-slop/eval.md`: giữ mệnh đề nguồn, bỏ lời khẳng định phổ quát, câu hỏi tu từ và lời dẫn giải về chính văn bản; không thêm số liệu đối sánh.
- Đã rà theo Quill: ký hiệu xuất hiện trước khi dùng; $w_0,g_1,\eta$ truyền qua ví dụ bộ tối ưu; $X:B\times D$ truyền qua BN; hai vòng tinh chỉnh nối xác thực với khóa tập kiểm tra. Không có và không tạo `quill.json`.
- Chưa cập nhật `index.html`; chưa commit/push.
- Kiểm định RevealJS cục bộ: 48 mã trang duy nhất, 48 ghi chú, 13 SVG được HTML tham chiếu và đều phân tích XML/a11y hợp lệ; mọi tài nguyên tương đối đều tồn tại; không có raster hoặc phụ thuộc mạng cốt lõi. KaTeX dựng 131 biểu thức với `throwOnError: true`, `strict: "error"`, không lỗi.
- Phiên này không có trình duyệt đồ họa hoặc headless để duyệt tràn chữ ở khung 16:9 và màn hình hẹp; kết quả trên là kiểm định tĩnh của RevealJS, KaTeX và tài nguyên cục bộ.

## Kết quả nguồn và storyboard hiện hành (bản cuối)

Các mục dưới đây là trạng thái hiện hành sau vòng chỉnh cuối; các báo cáo phía trên giữ nguyên như lịch sử của các vòng rà trước.

- Nguồn: `qquad` đã sửa (không còn ký hiệu lỗi trong HTML).
- Cấu trúc: 9 mạch cũ hợp nhất thành 7 mạch; HTML giữ đúng 7 section ngoài [00–05], [06–14], [15–23], [24–34], [35–42], [X01–X04], [X05]; đủ 48 ID và 48 notes.
- L03-08: lược về dạng lịch, giữ $K,T\in\mathbb N_{>0}$, $0\le t\le T$.
- L03-13: chỉ giữ hai công thức Xavier/Kaiming.
- Thuật ngữ: "Momentum" Việt hóa thành "Mômen" thống nhất toàn deck và planning.
- L03-10: ghi chú nguồn log-sum-exp đúng dải lec04:19.
- L03-42: đổi "lịch học" thành "lịch tốc độ học"; L03-03 đổi tương tự.
- L03-X05: viết lại thành kết luận toàn bài ba bước (chẩn đoán → chọn cơ chế → so sánh bằng xác thực và khóa tập kiểm tra); timing X05 là 2 phút, X01–X04 mỗi trang 5 phút, lõi đúng 100 phút, mở rộng đúng 20 phút, bài tập 50 phút tách riêng.
- Routes: lõi bấm End tại L03-42 để tới X05; đầy đủ L03-42 → phải tới X01 → xuống qua X02–X04 → phải tới X05.
- `index.html` đã có mục Bài 3.
- Năm vai độc lập mới (sinh viên, chuyên gia Học sâu, toán học–thuật toán–triển khai, phản biện học thuật–giảng dạy, kết nối–mạch viết) đã chạy trên bản trước lượt chỉnh sửa hợp nhất này. Kiểm định kỹ thuật, KaTeX, trực quan và HTTP sau chỉnh sửa vẫn CHƯA CHẠY.

## Báo cáo năm vai độc lập trên bản hiện hành

Bảng dưới là báo cáo của năm vai rà soát độc lập chạy trên bản hiện hành (sau bản vá L1, hợp nhất 7 mạch và chỉnh timing). Các báo cáo phía trên giữ nguyên như lịch sử của các vòng rà trước.

### Vai 1 — Sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất | Quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | L03-42 → X05 | Chỉ dẫn cũ không thể bỏ qua bốn trang mở rộng | Cấu trúc RevealJS và planning | Dùng phím tắt tới trang cuối; ghi đúng thao tác tuyến đầy đủ | Đã xử lý: lõi bấm End tại L03-42; đầy đủ đi phải tới X01, xuống qua X02–X04 rồi phải tới X05 |
| trung bình | L03-37 | Kết quả $\hat X$ và $Y$ hiện cùng lúc làm lộ đáp án tính toán | HTML L03-37 | Thêm fragment | Đã xử lý: hai khối công thức thành fragment |
| trung bình | L03-14, 27, 30 | Câu hỏi lộ đáp án | HTML các trang này | Fragment cho đáp án | Đã có fragment sẵn trên HTML hiện hành |
| trung bình | Toàn deck | Chữ phụ nhỏ | CSS `.tiny`/bảng .93em, hiệu dụng .753em | Nâng lên ≥ .75em ngưỡng | Bác ở mức chặn: .753em đạt ngưỡng .75; chờ kết quả visual trước khi đổi thêm |

### Vai 2 — Chuyên gia Học sâu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | L03-12 | Điều kiện "cùng tầng, cùng đầu vào x" chỉ nằm trong notes | HTML L03-12 | Đưa điều kiện lên mặt trang | Đã xử lý: box trên mặt L03-12 ghi điều kiện áp dụng |
| nghiêm trọng | Mạch↔section | Bảy mạch planning phải ánh xạ 1:1 với section HTML | outline.md vs HTML | Định nghĩa lại vai trò theo đúng wrapper hiện hành | Đã xử lý: 00–05; 06–14; 15–23; 24–34; 35–42; X01–X04; X05 |
| trung bình | L03-28 | AdamW cần giải thích rõ | HTML L03-28 notes | Giải thích suy giảm tách rời | Đã có: notes giải thích AdamW là biến thể Adam với hệ số co tác động trực tiếp lên tham số |
| trung bình | L03-29 | Tiêu đề/định nghĩa L1 | HTML L03-29 | Định nghĩa đạo hàm dưới trên mặt | Đã có: box trên mặt định nghĩa $\partial|w_i|$ |

### Vai 3 — Độ chính xác toán học, thuật toán và triển khai

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | L03-10 | Notes còn câu sai "log không nhận đối số âm quá lớn" | HTML L03-10 notes | Bỏ hẳn câu sai, thay bằng phát biểu đúng | Đã xử lý: thay bằng "tổng mũ hữu hạn và log chỉ nhận đối số dương" |
| nghiêm trọng | Timing | Lõi 102 phút sau bản vá L1 | storyboard.md | Giảm L03-07 3→2 và L03-15 3→2 | Đã xử lý: lõi L03-00–42 = 98 phút + X05 2 phút = 100 |
| trung bình | L03-13 | "Lần đầu Glorot/Xavier" chưa ghi rõ | HTML L03-13 | Ghi Xavier (Glorot) lần đầu xuất hiện | Đã có: thẻ "Xavier (Glorot)" trên mặt L03-13 |
| trung bình | L03-24 | Dừng sớm cần nêu đúng vai trò | HTML L03-24 notes | Ghi dừng sớm là quyết định siêu tham số | Đã có trong notes hiện hành |
| trung bình | L03-25 | Chuẩn Frobenius cần định nghĩa | HTML L03-25 notes | Định nghĩa $\lVert W\rVert_F^2$ | Đã có: notes định nghĩa tổng bình phương mọi phần tử |
| trung bình | L03-36 | Phương sai chia B | HTML L03-36 notes | Ghi ước lượng chệch | Đã có trong notes hiện hành |
| trung bình | L03-16 | Thiếu phát biểu "không có trạng thái phụ" | HTML L03-16 | Ghi rõ trên notes | Đã có: "SGD không giữ trạng thái phụ" |

### Vai 4 — Phản biện học thuật và giảng dạy

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | Câu nối | Thiếu câu chuyển 14→15, 32→33, 38→39 | HTML notes | Thêm ba câu nối | Đã xử lý: 14→15 (mạch kế bộ tối ưu), 32→33 (mạch kế thống kê lô), 38→39 (hai chế độ thống kê) |
| trung bình | L03-42/X05 | Vai trò X05 trong timing chưa rõ | outline.md, storyboard.md | Tách X05 khỏi mạch 7 lõi | Đã xử lý: mạch 7 ghi 5+2 phút; tổng 98+2=100 |
| trung bình | Bài tập | Bài tập 50 phút phải tách khỏi timing deck | note-for-author.md | Ghi rõ tách riêng | Đã có: 50 phút riêng, không tính vào 120 phút |

### Vai 5 — Kết nối và mạch viết

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | KaTeX | Báo cáo cũ nêu thiếu KaTeX | vendor/katex | Kiểm tra thư mục vendor | Bác: `vendor/katex` tồn tại trong dự án; cấu hình `katex:{local:"vendor/katex"}` hợp lệ |
| trung bình | Điều hướng | Chỉ dẫn cũ không khớp cấu trúc ngang–dọc | storyboard.md, note-for-author.md | Ghi thao tác theo đúng cấu trúc RevealJS | Đã xử lý bằng End cho tuyến lõi; tuyến đầy đủ đi phải, xuống, rồi phải |
| trung bình | Planning | Timing tổng phải 100+20, bài tập 50 | outline.md, storyboard.md | Đồng bộ ba tệp | Đã xử lý: lõi 98+X05 2=100; X01–X04=20; toàn tuyến 120; bài tập 50 |

## Trạng thái xác minh cuối

- Hậu kiểm toán học–thuật toán–triển khai sau chỉnh sửa: không còn lỗi chặn hoặc nghiêm trọng; các công thức và timing 98+2 đã được tính lại. Ba góp ý diễn đạt nhẹ ở L03-10, L03-12 và L03-37 đã xử lý cục bộ.
- Hậu kiểm kết nối–mạch viết sau chỉnh sửa: bảy section ánh xạ một-một, timing 100+20 và điều hướng End/phải–xuống–phải đạt; ba góp ý nhẹ ở L03-16, L03-32 và L03-33 đã xử lý cục bộ.
- Cấu trúc: đạt 7 section ngoài theo đúng dải `[00–05]`, `[06–14]`, `[15–23]`, `[24–34]`, `[35–42]`, `[X01–X04]`, `[X05]`; 48 `data-slide-id` duy nhất và 48 khối notes.
- Tài nguyên: mọi `src`/`href` cục bộ tồn tại; không có tham chiếu mạng cốt lõi hoặc raster; 13 SVG phân tích XML thành công và đều có `role="img"`, `title`, `desc`.
- KaTeX: Chromium dựng deck với `throwOnError: true`, `strict: "error"`; DOM có phần tử KaTeX và không có `katex-error`.
- HTTP: `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`; dùng máy chủ dự phòng `python3 -m http.server 8765` chỉ tại `2627-1/`, deck trả HTTP 200.
- Trực quan: đã chụp và duyệt đủ 48 trang ở 1280×720 và 960×720; không thấy tràn chữ, chồng lấn, công thức hoặc SVG bị cắt. Cỡ chữ `.compact`/`.tiny` hiệu dụng khoảng `.753em` vẫn đọc được ở hai khung, nên giữ nguyên CSS cục bộ.
- Tiêu đề: đã xuất toàn bộ `h1`, `h2`, `h3` và rà thủ công; chỉ giữ tiếng Anh ở tên/viết tắt kỹ thuật như SGD, MLP, ReLU, Glorot/Xavier, Kaiming, RMSprop, Adam, dropout, BN và LN.
- Timing và điều hướng: lõi 98+2=100 phút, mở rộng 20 phút, toàn tuyến 120 phút, bài tập 50 phút riêng; phím End và tuyến phải–xuống–phải đã được kiểm tra theo cấu trúc RevealJS.
- Storyboard giữ mã ổn định L03-X05 nhưng đặt trang này trong mục kết luận lõi riêng; bảng mở rộng chỉ còn X01–X04, tránh cộng nhầm thành 22 phút.
- Kết quả kiểm định cuối: **ĐẠT**.
- Các báo cáo "Bốn báo cáo rà soát độc lập" và "Hậu kiểm vòng hai" phía trên là báo cáo lịch sử của các vòng rà trước, không phải kết quả trên bản hiện hành.

## Pha A — ghi chú bài giảng, đợt hiện hành

### Dossier và tác tử đọc nguồn

- Dossier chỉ đọc được tạo từ đúng các dải trong `source.md`: `lec10_training.pdf` 3–9, 11–17, 19–33, 35–41; `lec05_multilayer.pdf` 37–47; `lec02_linear_part1.pdf` 55–68; `lec03_linear_part2.pdf` 2–15; `lec04_multiclass.pdf` 19; giáo trình 58–66, 96–105, 153–158; DOCX III.2 → Buổi 3; Goodfellow §7.1.2 đã duyệt.
- Ba tác tử đọc nguồn GLM chạy song song trên các dossier tách biệt. Cả ba đều báo đúng model `z-ai/glm-5.3-flash`, provider OpenRouter và không mở tệp ngoài allowlist.
- Tác tử lập bản đồ chủ đề đề xuất 15 chủ đề. Điều phối viên hợp nhất thành `note-l03-t01`–`note-l03-t15` trong `outline.md`; mã chỉ dùng nội bộ.

### Giới hạn DeepSeek và checkpoint

| Công đoạn | Phạm vi cấp cho writer | Kết quả | Quyết định |
|---|---|---|---|
| Soạn bản nháp | Chỉ `approved-spec.md`, mẫu ghi chú và một đầu ra `lecture-note.md` | Đúng model `deepseek/deepseek-v4-flash-0731`, provider OpenRouter; nội dung tốt nhưng writer ghi lại toàn tệp ba lần | Giữ bản hợp lệ cuối; từ các buổi sau chỉ cho phép đúng một thao tác ghi toàn tệp rồi dừng |
| Tự kiểm | Chỉ bản nháp và checklist trong staging mới | Đúng metadata nhưng bản sửa làm hỏng Unicode, KaTeX và đổi đuôi đường dẫn `.svg` | Loại toàn bộ đầu ra; quay về checkpoint bản nháp tốt, không vá trên bản hỏng |

Quy tắc bền vững đã ghi vào `prompt_lecture_note_deck.md`: lượt soạn chỉ ghi toàn tệp đúng một lần; lượt tự kiểm mặc định chỉ tạo báo cáo; task sửa chỉ được trả tối đa ba thay thế ngắn có điểm neo; mọi đầu ra hỏng công thức, Unicode, đường dẫn hoặc sai danh sách tệp phải bị loại và quay về checkpoint hợp lệ gần nhất.

### Năm vai rà độc lập cho lecture note

Năm vai dùng cùng checkpoint đóng băng, chỉ đọc `lecture-note.md`, `outline.md`, `storyboard.md`; model yêu cầu và quan sát đều là `z-ai/glm-5.3-flash`, provider OpenRouter.

| Vai | Phát hiện chính | Xử lý |
|---|---|---|
| Sinh viên | Lượt đầu báo thiếu planning do glob ngoặc nhọn không được công cụ hỗ trợ; lượt tái kiểm đọc đúng ba tệp. Đề nghị thêm gợi ý cho bài log-sum-exp | Báo thiếu tệp bị bác bằng kiểm kê staging; đã thêm gợi ý cho log-sum-exp, Jacobian, dropout và BN |
| Chuyên gia Học sâu | Thiếu phân biệt L2 với suy giảm trọng số tách rời; thiếu nội dung X01–X03; thiếu $P,\varepsilon$ | Đã bổ sung có giới hạn, khôi phục đủ bốn chủ đề mở rộng, khai báo ký hiệu |
| Toán học, thuật toán và triển khai | Các phép tính đều đúng; đề nghị làm rõ $\varepsilon$ chỉ bị bỏ trong tính nhẩm và sửa diễn giải chuẩn tích Jacobian | Đã sửa; hậu kiểm tính lại toàn bộ và PASS |
| Phản biện học thuật và giảng dạy | Chỉ số bước L2 lệch quy ước; mục nối triển khai mỏng; câu về thống kê chạy mang giọng biên soạn | Đã thống nhất $w_{t-1}\to w_t$, bổ sung trạng thái triển khai và viết lại câu kỹ thuật |
| Kết nối và mạch viết | Ký hiệu $L_{data}$ xuất hiện đột ngột; thiếu nối dropout→BN; kết luận nằm trong mục mở rộng; còn cụm “Đã kiểm”, “bắt buộc nêu”, “nguồn không khóa” | Đã khai báo ký hiệu, thêm câu nối, tách mục kết luận và xóa dấu vết biên soạn; hậu kiểm mạch PASS |

Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`. Các cảnh báo thiếu SVG ở lượt sinh viên là hệ quả của staging reviewer không chứa tài sản; kiểm định cục bộ trên kho thật xác nhận mọi SVG được tham chiếu đều tồn tại.

### Biên tập và kiểm định ghi chú

- `$no-ai-slop`: đã đọc toàn văn và loại trạng thái kiểm chứng, chỉ dẫn người viết, siêu bình luận, cụm kết luận máy móc và thuật ngữ Anh–Việt không cần thiết. Không có mục tự kể “đã thay đổi gì” trong sản phẩm công khai.
- `$quill`: đã rà tuyến chẩn đoán → bước cập nhật/ổn định → khởi tạo → bộ tối ưu → điều chuẩn → chuẩn hóa → chọn siêu tham số → mở rộng → kết luận; ký hiệu và dữ kiện được truyền nhất quán. Không tạo `quill.json`.
- Hậu kiểm mạch cuối sau khi chuyển Kết luận xuống sau phần triển khai và tự kiểm: GLM đọc đủ ba tệp, metadata đúng, xác nhận kết nối vào từ mục 7 hoặc 8 và kết nối ra Buổi 04; kết quả PASS.
- Kiểm định tĩnh hiện hành: một H1; 42 chỉ thị mở/đóng hợp lệ; 183 biểu thức KaTeX dựng với `throwOnError: true`, `strict: "error"`; 12 SVG được tham chiếu và đều có `role="img"`, `title`, `desc`; không có nhãn OpenRouter/DeepSeek/GLM/checkpoint/mã trang/chỉ dẫn người soạn trong tài liệu công khai.
- Liên kết index chỉ được cập nhật sau khi các kiểm tra trên đạt. `python3 -m reloadserver 8765` chưa dùng được vì môi trường thiếu mô-đun; dùng máy chủ HTTP cục bộ làm phương án kiểm tra đường dẫn. Phiên hiện tại không có Browser/Codex Slides để xác nhận trực quan viewer ở hai khung màn hình; giới hạn này phải được giữ trong báo cáo bàn giao.
