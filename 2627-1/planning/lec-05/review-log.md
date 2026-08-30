# Nhật ký rà soát Bài 05

## Quyết định nguồn và phạm vi

- Giữ thứ tự nguồn: LeNet → AlexNet → VGG → GoogLeNet/Inception → chuẩn hóa theo lô → ResNet → học chuyển giao.
- Bỏ `lec09_cnn_architectures.pdf` PDF 36–43, NiN, DenseNet, ResNeXt, meme và ảnh chụp vì ngoài phạm vi hoặc không đáp ứng yêu cầu SVG.
- Không dùng bảng lỗi hoặc bảng xếp hạng để suy ra ưu thế tuyệt đối khi thiếu giao thức tiền xử lý, dữ liệu bổ sung, số lần chạy và ngân sách tính toán.
- Dùng GT chỉ để kiểm chứng kích thước, công thức, trạng thái BN và nối mạch; không thay mạch chính của slide nguồn.

## Sai khác và sửa số

| Bằng chứng nguồn | Quyết định trong bộ trang | Lý do |
|---|---|---|
| GT dùng biến thể LeNet với ảnh MNIST 28×28, đệm ở tầng đầu | Ghi rõ đây là biến thể GT, không đồng nhất LeNet-5 nguyên bản 32×32 | Tránh trộn hai dấu vết kích thước |
| `lec09` PDF 5–7 nói AlexNet gốc chia hai GPU; PDF 8 là bản sửa đổi | Mọi số dùng duy nhất bản sửa đổi 227×227, tích chập 1 có 64 kênh; hai GPU chỉ là bối cảnh | Tránh ghép số giữa hai kiến trúc |
| Bảng PDF 8 ghi “flop” theo quy ước không khóa rõ | Tính lại và gọi 716.767.232 MAC; chỉ nói $1$ MAC xấp xỉ $2$ FLOP khi nêu quy ước | Không đồng nhất MAC với FLOP |
| PDF 17 ghi 418M và so sánh 17,8× | Chỉ báo 124.096 trọng số không độ lệch cho đúng ba tầng tích chập trong phần gốc | Hai tầng gộp không có trọng số; quy ước 418M không được khóa cho bộ trang |
| Nguồn mô tả Inception bằng hình | Vẽ lại bốn nhánh; khóa bước trượt/đệm; tính 163.328 so với 393.216 trọng số | Hai số cũng là MAC tích chập trên mỗi vị trí khi giữ cùng $H,W$; không gọi là tổng chi phí khối |
| GT PDF 149–152 mô tả toàn GoogLeNet | Thay bảng nhánh lặp ở L05-21 bằng dấu vết phần gốc → 2–5–2 khối Inception có gộp xen kẽ → gộp toàn cục → lớp | Đáp ứng LLO9 về kiến trúc toàn mạng, không chỉ khối |
| Nguồn dùng gộp trung bình toàn cục và đầu 1000 lớp | Nêu GAP loại bỏ chuỗi tầng đầy đủ lớn nhưng vẫn giữ tầng tuyến tính $1024\rightarrow1000$; so 1.024.000 trọng số với 102.760.448 trọng số riêng FC6 VGG | Trọng số so với trọng số; ghi rõ hai tầng không cùng chức năng đầu ra |
| `lec10` trình bày trực giác “dịch chuyển đồng biến nội bộ” | Không dùng làm giải thích duy nhất; mô tả phép biến đổi, trục và trạng thái | GT PDF 157–158 nêu giới hạn của trực giác này |
| GT PDF 157 nói thống kê “toàn cục” sau huấn luyện | Dùng cụm “thống kê cố định được ước lượng trong huấn luyện”; không khóa trung bình trượt lũy thừa | Cách cập nhật, tham số quán tính và hiệu chỉnh phương sai phụ thuộc khung phần mềm |
| Nguồn ResNet đôi chỗ gắn suy giảm với đạo hàm khó truyền | Tách “lỗi huấn luyện tăng khi thêm tầng” khỏi quá khớp và khỏi khẳng định đạo hàm triệt tiêu | Định nghĩa đúng hiện tượng suy giảm |
| PDF 30 gọi 589.824 và 69.632 là “phép toán” | Gọi đúng phép so một ánh xạ 3×3 256→256 với toàn nhánh cổ chai 256→64→64→256 | Cùng đơn vị trọng số và MAC tích chập trên mỗi vị trí; chưa nhân $H×W$ |
| PDF 32 diễn giải ResNet như nhiều đường | Đưa sang mở rộng và ghi là diễn giải nghiên cứu, không phải chứng minh một tổ hợp mô hình | Giữ đúng mức độ bằng chứng |

## Các phép tính đã kiểm tra

- AlexNet sửa đổi: chuỗi kích thước $3×227^2→64×56^2→64×27^2→192×27^2→192×13^2→384×13^2→256×13^2→256×13^2→256×6^2→9216→4096→4096→1000$.
- FC6 có 37.748.736 trọng số; tổng có độ lệch 61.100.840 tham số; tổng 716.767.232 MAC.
- Ba nhân 3×3, bước trượt 1, độ giãn 1 cho trường tiếp nhận 7; $49K^2$ so với $27K^2$, giảm $22/49≈44,9\%$ và thêm hai ReLU.
- Phần gốc GoogLeNet có 124.096 trọng số không độ lệch theo các tầng 7×7, 1×1, 3×3 đã khóa.
- Inception: $64+128+32+32=256$ kênh; có giảm kênh 163.328, không giảm 393.216 trọng số, tỷ lệ khoảng 2,41.
- Toàn GoogLeNet: phần gốc $192×28^2$ → hai Inception $480×28^2$ → gộp → năm Inception $832×14^2$ → gộp → hai Inception $1024×7^2$ → gộp toàn cục → 1000 lớp.
- Đầu gộp toàn cục: $1024×7^2→1024×1^2→1000$; tầng phân loại có 1.024.000 trọng số hoặc 1.025.000 tham số nếu có độ lệch.
- BN CNN giảm theo N,H,W cho từng C; ví dụ $8×64×28×28$ dùng 6272 giá trị mỗi kênh; $\gamma,\beta$ phát rộng thành $1×64×1×1$.
- Một ánh xạ trực tiếp 256→256 bằng nhân 3×3 có 589.824 trọng số; toàn nhánh cổ chai 256→64→64→256 có 69.632, giảm 8,47 lần. Đây không phải tỷ lệ giữa hai khối hoàn chỉnh.
- Phép cộng thặng dư chỉ hợp lệ khi hai nhánh cùng N,C,H,W; phép chiếu 1×1 xử lý đổi kênh và giảm mẫu.
- Sau khi vectơ hóa, $J_F,J_P\in\mathbb R^{d_{out}\times d_{in}}$ và có thể là ma trận chữ nhật khi kích thước đổi. Ma trận đạo hàm: nhánh đồng nhất $I+J_F$; nhánh chiếu $J_P+J_F$; hậu kích hoạt nhân trái bởi $D_{\mathrm{ReLU}}(s)$. Với gradient cột, tích Jacobian chuyển vị–vectơ là $\bar x=J_s^\top\bar s$.
- ResNet-18: phần gốc $64×56^2$; bốn giai đoạn có 2–2–2–2 khối và đầu ra $64×56^2$, $128×28^2$, $256×14^2$, $512×7^2$; sau đó gộp toàn cục và tầng đầy đủ.

## Quyết định sau phản biện

- Tăng cỡ chữ nền từ `.78em` lên `.9em`; `.small` và bảng cho cỡ hiệu dụng `.774em`. Bỏ giới hạn thấp 215 px và tăng kích thước các SVG có nhiều nhãn.
- L05-02 hiện cấu trúc LeNet 5×5–sigmoid–gộp trung bình; L05-11/14 hiện số tầng VGG 2–2–3–3–3 và dấu mốc đầu đầy đủ.
- L05-04–08 khóa đầy đủ đặc tả AlexNet và hiện phép tính đại diện cho tham số/MAC của hai tầng đầu trước khi cộng tổng.
- L05-24–28 trở thành cụm BN khép kín. Thứ tự hậu/tiền kích hoạt được chuyển hoàn toàn sang L05-X04 sau cụm ResNet.
- L05-30–33 dùng $s$ cho giá trị trước kích hoạt, định nghĩa $J_F,J_P$ và tách ba trường hợp nhánh đồng nhất, phép chiếu, hậu kích hoạt.
- L05-35 chỉ so khối cơ bản với cổ chai; L05-36 thay trang quy tắc tên bằng dấu vết ResNet-18 và câu hỏi kích thước/phép chiếu.
- L05-37 giữ cầu nối ngắn nhưng thêm tình huống cụ thể, hai quyết định độc lập về gradient/chế độ mô-đun và chính sách BN.
- L05-10, L05-23, L05-31 và L05-36 dùng hiệu ứng xuất hiện; thời gian chờ được tính trong storyboard.
- Chuyển chỉ dẫn tuyến cắt, phạm vi và quyết định nguồn khỏi ghi chú diễn giả sang `note-for-author.md` và nhật ký này.

## Đề xuất không áp dụng

- Không thêm bảng kết quả hoặc tuyên bố hội tụ: nguồn không khóa giao thức đủ để suy ra quan hệ nhân quả hay bảo đảm tối ưu.
- Không mở rộng sang NiN, DenseNet, ResNeXt hoặc trang nguồn 36–43: ngoài phạm vi đã duyệt.
- Không biến L05-X05 thành bài mô tả ảnh: chỉ giữ giao diện vectơ; mô hình chuỗi thuộc Bài 07.
- Không khóa một công thức cập nhật thống kê BN theo tên thuật toán cụ thể: nguồn chỉ đủ để khẳng định thống kê cố định được ước lượng khi huấn luyện.
- Không dùng bảng FLOP giữa các họ mạng: quy ước phép đếm và triển khai chưa đồng nhất.

## Rà biên tập

- Đã áp dụng `no-ai-slop`: bỏ khẩu hiệu, câu hỏi tu từ, nhận định hơn kém thiếu giao thức và câu kết khoa trương; giữ câu ngắn, số cụ thể và động từ trực tiếp.
- Đã rà theo nguyên tắc Quill: khóa NCHW/MAC trước phép đếm; mỗi kiến trúc có dấu vết toàn mạng hoặc lý do rút gọn; dữ kiện từ ví dụ được truyền sang tham số/MAC/ma trận đạo hàm; BN khép kín trước ResNet. Không tạo `quill.json`.
- Tiêu đề chỉ giữ tên kiến trúc, CNN, BN, ReLU, NCHW, MAC/FLOP và ký hiệu chuẩn bằng tiếng Anh.

## Hai vòng hậu kiểm cuối

### Vòng 1

- Khóa lại ba tầng tích chập ở phần gốc GoogLeNet, toàn mạng 2–5–2 Inception và dấu vết ResNet-18.
- Sửa phép so Inception thành trọng số và MAC tích chập trên mỗi vị trí; sửa GAP thành phép loại bỏ đầu đầy đủ lớn nhưng vẫn giữ tầng tuyến tính $1024\rightarrow1000$.
- Khép cụm chuẩn hóa theo lô trước ResNet; tách thống kê huấn luyện/suy luận; không khóa trung bình trượt lũy thừa.
- Tăng chữ hiệu dụng và nhãn SVG, thêm fragment, đồng bộ timing 100+20 phút và tuyến bài tập 50 phút.

### Vòng 2

- Sửa L05-X05 sang Bài 07; đồng bộ outline, storyboard và ghi chú nội bộ.
- Vectơ hóa tensor ở L05-33, thêm kích thước Jacobian và tích Jacobian chuyển vị–vectơ cho gradient cột; đổi nhãn đầu ra khối thặng dư từ $y$ sang $s$.
- Đưa điều kiện $K$ lên mặt L05-13; khóa rõ tỷ lệ 8,47 không phải phép so hai khối hoàn chỉnh.
- Sửa chu trình VGG, BN và ResNet theo đúng thứ tự; sửa điều hướng xuống trong cụm và phải ở cuối cụm; khóa AlexNet 20 phút, ResNet 22 phút và L05-37 là 3 phút mà tổng lõi vẫn 100 phút.
- Chuyển toàn bộ chỉ dẫn thời gian chờ và tuyến trình chiếu khỏi ghi chú diễn giả sang `note-for-author.md` và storyboard.
- Xóa ba SVG không được dùng; kiểm kê cuối còn 18 SVG và cả 18 đều được HTML tham chiếu.

## Vòng chỉnh sửa theo kiểm định storyboard và báo cáo nguồn

- **Cấu trúc mạch:** gộp từ 8 xuống đúng 7 `<section>` ngoài: [L05-00..03], [04..10], [11..15], [16..23], [24..28], [29..37], [X01..X05 rồi L05-38]. L05-38 được chuyển xuống cuối chồng mở rộng, sau L05-X05, và là trang cuối toàn deck. Điều hướng: tuyến lõi tại L05-37 nhấn End tới L05-38; tuyến mở rộng tại L05-37 nhấn phải sang L05-X01, xuống qua L05-X05 rồi xuống tới L05-38. Thứ tự X01–X05 không đổi. Đã đồng bộ storyboard.md và note-for-author.md; không đưa chỉ dẫn tuyến lên mặt slide hoặc ghi chú diễn giả.
- **Học chuyển giao (L05-37):** phần này có nguồn slide `lec09_cnn_architectures.pdf` PDF 44–46 nhưng không nằm trong danh mục "Bài giảng" Buổi 5 của DOCX (chỉ gián tiếp ở Buổi 6). Giữ ở tuyến lõi với vai trò cầu nối ngắn phục vụ LLO10; ghi rõ đây là mở rộng phạm vi so với văn bản đề cương.
- **Suy giảm độ chính xác huấn luyện:** tách hiện tượng "lỗi huấn luyện tăng khi thêm tầng" (định nghĩa suy giảm) khỏi diễn giải "suy giảm gradient" của DOCX dòng 368 và GT `hocsau-p149-163.txt` 662–670. Lý do: hiện tượng quan sát được trên đồ thị lỗi huấn luyện là dữ kiện; khẳng định về đạo hàm triệt tiêu là một diễn giải cơ chế mà nguồn không chứng minh trong phạm vi bài. Bộ trang giữ dữ kiện, ghi trực giác ở ghi chú, không tuyên bố cơ chế.
- **L05-36:** thêm câu nối trong ghi chú diễn giả từ ResNet-18 sang học chuyển giao (thân đã học có thể tái dùng → hai quyết định gradient/chế độ), khớp câu nối cụm trong storyboard.
- **L05-33:** giảm tải mặt trang: chuyển thẻ hậu kích hoạt $J_z=D_{\mathrm{ReLU}}(s)J_s$ xuống ghi chú; thêm một dòng nhắc quy ước gradient cột và tiên quyết Jacobian Bài 02–03 ở cỡ chữ thường, không thu nhỏ chữ thêm.
- **L05-20:** loại xung đột ký hiệu $W$: công thức MAC dùng $W_s$ cho bề rộng không gian và chú thích rõ $|W|$ là số trọng số; đồng bộ storyboard.
- **L05-26:** bỏ lặp đầy đủ ví dụ 6272; tham chiếu ví dụ trang trước và tập trung trục giảm, phát rộng $\gamma,\beta$.
- **Storyboard:** sửa bảng chu trình cụm GoogLeNet thành "ví dụ phần gốc L05-17 → trực giác/ví dụ khối L05-18" cho khớp thứ tự trang.
- Timing giữ nguyên: mạch 1=8, 2=20, 3=11, 4=20, 5=14, 6=25 (L05-29..37), 7=20 mở rộng + 2 kết luận (L05-38); lõi 100, mở rộng 20; bài tập 50 phút tách riêng.

## Hợp nhất năm phản biện

Các sửa đã áp dụng:
- Sửa notes L05-20 thành bốn nhánh đúng: $192·64=12.288$; $192·96+96·128·9=129.024$; $192·16+16·32·25=15.872$; $192·32=6.144$; tổng $163.328$; bỏ phép phân rã sai 73.728+108.544.
- Storyboard L05-20 dùng $H_s·W_s·|W|$ với điều kiện các tích chập cùng kích thước đầu ra; chu trình GoogLeNet sửa thành "tính L05-20 → triển khai L05-21 → tính/so L05-22 → kiểm tra L05-23".
- Thay mọi "Bài 03–04" còn lại thành "Bài 02–03" trong storyboard, review-log, note-for-author.
- Outline: mạch 1 đổi tên "Mở đầu + LeNet"; ranh giới hậu/tiền kích hoạt ghi "chỉ xuất hiện trên mặt trang ở L05-X04; ghi chú L05-30/33 được phép nhắc ở mức điều kiện".
- Note-for-author L05-20 đổi sang $H_s,W_s$ và ghi điều kiện cùng kích thước đầu ra.
- L05-12: rút gọn câu điều kiện thành "ba tầng đang xét đều có bước trượt 1 và độ giãn 1; bước trượt hoặc độ giãn ở tầng trước làm đổi công thức tích lũy".

Năm quyết định không áp dụng:
- a) Giữ 163.328 vì gồm đủ hai tầng giảm kênh; 141.824 đã bỏ sót $192·96$ và $192·16$.
- b) Giữ 716.767.232 vì conv5=99.680.256; 99.681.024 sai 768.
- c) Giữ timing vì L16–23=20 (L17=2), L29–37=25 (22+3), L38=2 riêng.
- d) Giữ thứ tự X01..X05 theo cấu trúc đã khóa.
- e) Giữ học chuyển giao vì nguồn đã được ánh xạ/duyệt và là cầu nối, đồng thời vẫn ghi rõ ngoài danh mục DOCX.

## Tái kiểm sau chỉnh sửa

- Rà toán học xác nhận lại AlexNet, Inception, chuẩn hóa theo lô, Jacobian, ResNet và timing; không còn lỗi nghiêm trọng hoặc chặn bàn giao.
- Rà mạch xác nhận đúng 7 mạch, kết luận ở cuối, hai tuyến điều hướng và các ranh giới phần. Sửa câu nối L05-X01 để phản ánh đúng GoogLeNet rồi ResNet; bổ sung câu nối L05-X03→L05-X04 và L05-X04→L05-X05. Không đổi thứ tự trang mở rộng.
- Không thêm câu chỉ dẫn rẽ tuyến vào ghi chú L05-37: vai trò và thao tác điều hướng đã ghi trong storyboard và `note-for-author.md`; đưa nhãn tuyến vào ghi chú diễn giả sẽ vi phạm quy tắc không hiển thị chỉ dẫn nội bộ. Đây là đề xuất mức nhẹ và không chặn bàn giao.
- Rà trình chiếu ở 1280×720 và 960×720 cho thấy công thức L05-32 sát mép phải; đổi riêng khối công thức sang lớp `small` (cỡ hiệu dụng vẫn trên ngưỡng đọc) để tạo lề an toàn, không đổi nội dung toán học.

## Giới hạn kiểm định trực quan

- `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`; cổng 8765 đồng thời đang phục vụ một kho khác nên không dừng tiến trình ngoài phạm vi. Máy chủ dự phòng chỉ phục vụ `2627-1/` tại cổng 8766; HTML, CSS, RevealJS, KaTeX và SVG kiểm tra đều trả HTTP 200, tệp HTML phục vụ khớp hàm băm với tệp trong kho.
- Chromium headless dựng đủ 88 lượt: 44 trang ở 1280×720 và 44 trang ở 960×720. Sau khi tắt chuyển cảnh để chụp ổn định, không có tràn nội dung, lỗi console, yêu cầu tài nguyên thất bại hoặc phần tử `katex-error`.
- Kiểm tra trực quan toàn bộ hai bảng ảnh liên hệ và các trang dày L05-07, L05-20, L05-25, L05-32, L05-33, L05-36, L05-37, L05-X04, L05-38: chữ, bảng, công thức, SVG, fragment và chân trang đều đọc được; L05-32 đã được tạo thêm lề an toàn như ghi ở mục tái kiểm.
- Kiểm định tĩnh: đúng 7 `<section>` ngoài với số trang `[4,7,5,8,5,9,6]`; 44 ID duy nhất, 44 ghi chú, 44 nguồn; 18/18 tham chiếu ảnh là SVG cục bộ, không raster hoặc phụ thuộc mạng cốt lõi; 18 SVG phân tích XML và có `role="img"`, `title`, `desc`.
- Rà thủ công toàn bộ `h1`, `h2`, `h3`: chỉ giữ tiếng Anh cho tên kiến trúc, API/ký hiệu và viết tắt được phép. `index.html` đã có liên kết đúng tới bài 05.
