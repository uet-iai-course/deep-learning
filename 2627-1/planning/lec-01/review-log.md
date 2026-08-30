# Nhật ký rà soát Bài 01

## Kiểm kê và chuyển nguồn

- Đã dùng đúng dải nguồn được `source.md` duyệt cho Buổi 01.
- Đã Việt hóa mạch chính của `lec05_multilayer.pdf` trước khi bổ sung từ giáo trình.
- Đã đối chiếu `lec01_intro.pdf` tr. 3–15, 17–24; `lec02_linear_part1.pdf` tr. 15–21; `lec05_multilayer.pdf` tr. 2–35.
- Giáo trình chỉ được dùng để khôi phục khung học, kiểm chứng kích thước tensor, thuật ngữ và điều kiện phát biểu.
- Không dùng code, benchmark hoặc tài liệu ngoài danh mục.

## Quyết định sai khác so với nguồn

| Quyết định | Bằng chứng | Cách xử lý | Lý do |
|---|---|---|---|
| Dùng “biến đổi afin” cho $Wx+b$ | `lec02_linear_part1.pdf`, tr. 15–17 và `lec05_multilayer.pdf`, tr. 7–8 thường gọi rộng là “linear” | Gọi $Wx$ là tuyến tính, $Wx+b$ là biến đổi afin | Chính xác về toán học, thuần Việt và làm rõ phép rút gọn hai tầng |
| Không khẳng định tầng ra luôn có hàm kích hoạt phi tuyến | `lec05_multilayer.pdf`, tr. 28 | L01-22 trình bày cách chọn tầng ra theo miền đích; L01-23 kiểm tra cách chọn hàm kích hoạt | Tránh mâu thuẫn với đầu ra hồi quy và logit |
| Giữ xấp xỉ phổ dụng ở mức nguồn | `lec05_multilayer.pdf`, tr. 29 chỉ nêu mệnh đề khái quát | Không thêm miền compact hoặc lớp hàm; nêu rõ mệnh đề không bảo đảm học hay khái quát | Tôn trọng slide nguồn là nguồn ưu tiên |
| Nêu ReLU không khả vi tại 0 | `lec05_multilayer.pdf`, tr. 11–12; giáo trình PDF tr. 87 | Ghi rõ khả vi gần như mọi nơi và hiện thực chọn quy ước tại 0 | Tránh tuyên bố ReLU khả vi mọi nơi |
| Chuyển toàn bộ ký hiệu sang batch-first | Nguồn slide dùng vector cột; giáo trình dùng ma trận dữ liệu | Dùng $X:B\times d$, $W:d\times h$, broadcasting độ lệch theo batch | Nhất quán với tiêu chuẩn học phần và ví dụ XOR |
| Diễn giải tầng ẩn là biểu diễn phân tán | `lec05_multilayer.pdf`, tr. 30–34 | Không gán một ý nghĩa bắt buộc cho từng đơn vị | Giữ đúng cảnh báo của nguồn về khả năng diễn giải |
| Dựng ví dụ XOR 2–2–1 | Đề cương yêu cầu MLP; `lec02_linear_part1.pdf`, tr. 19 nêu XOR | Dùng tham số đã tự tính và ghi rõ không phải kết quả huấn luyện | Tạo ví dụ kiểm tra được từ giới hạn sang giải pháp |
| Đưa cấu trúc MLP trước chuỗi hình ReLU | `lec05_multilayer.pdf`, tr. 28 định nghĩa mạng hai tầng; tr. 13–27 minh họa sức mạnh ReLU | Dạy cấu trúc và kích thước tensor ở L01-17–23 rồi mới dùng chuỗi hình ở L01-24–28 | Sinh viên cần biết tầng ẩn, hàm kích hoạt và tầng ra trước khi đọc chuỗi biến đổi; đây là đổi thứ tự nguồn có chủ ý |
| Thu hẹp L01-09 sang phân loại nhị phân | Đề cương Buổi 1 và ví dụ perceptron/XOR ở `lec02_linear_part1.pdf`, tr. 15–21 | Bỏ ba chế độ học khỏi mặt trang, khóa $x_i\in\mathbb R^d$, $y_i\in\{0,1\}$ | Giảm tải dẫn nhập và giữ một bài toán xuyên suốt |
| Tách chuỗi hình ReLU theo bước | `lec05_multilayer.pdf`, tr. 13–27 tăng dần thông tin | Tạo SVG đầu vào, sau biến đổi afin, sau ReLU và kết quả có biên | Không lộ kết quả trước khi sinh viên quan sát từng phép biến đổi |
| Rút phát biểu xấp xỉ phổ dụng | `lec05_multilayer.pdf`, tr. 29 chỉ nêu mệnh đề khái quát | Bỏ điều kiện compact và tham chiếu giáo trình; chỉ nêu giới hạn của kết luận | Không đưa chi tiết không có trong slide nguồn được ưu tiên |
| Vẽ lại toàn bộ hình kỹ thuật | Hình nguồn cần chuyển và chuỗi hình cần tách bước | Dùng SVG có `role="img"`, `title`, `desc` và nhãn Việt | Tuân thủ quy định không trích raster |
| Bỏ `lec02_linear_part1.pdf` tr. 20–21 | Hai trang này bàn huấn luyện perceptron | Không đưa vào deck | Huấn luyện thuộc buổi 02–03 theo ranh giới đề cương |
| Không dùng bài tập GT 3.1.4 | Giáo trình PDF tr. 90 gợi ý bài tập | Dùng bộ bài tập bám hoạt động đề cương Buổi 1 | Bộ bài tập bám hoạt động đề cương; GT chỉ để kiểm chứng |
| Đổi nhãn $\{-1,1\}$/sgn sang $\{0,1\}$/hàm chỉ thị | Slide nguồn dùng $\{-1,1\}$ với sgn | Deck dùng $y_i\in\{0,1\}$, dự đoán cứng lấy bằng ngưỡng xác suất; ghi chú ở L01-09 | Nhất quán với sigmoid, XOR và quy ước ngưỡng trong toàn học phần |
| Sửa dải nguồn lịch sử | Bản nháp trích giáo trình PDF tr. 41–42 | Mở thành PDF tr. 41–44 | Khớp dải trang được ánh xạ cho bối cảnh lịch sử |

## Tự kiểm ví dụ XOR

Quy ước:

$$
W_1=\begin{bmatrix}1&1\\1&1\end{bmatrix},\quad
b_1=[0,-1],\quad
W_2=\begin{bmatrix}1\\-2\end{bmatrix},\quad
b_2=-0.5.
$$

Với $X$ gồm bốn hàng $(0,0),(0,1),(1,0),(1,1)$:

- $H=\operatorname{ReLU}(XW_1+b_1)$ có các hàng $(0,0),(1,0),(1,0),(2,1)$;
- logit $HW_2+b_2$ là $(-0.5,0.5,0.5,-0.5)$;
- sigmoid cho xấp xỉ $(0.378,0.622,0.622,0.378)$;
- ngưỡng $0.5$ cho $(0,1,1,0)$;
- số tham số là $4+2+2+1=9$.

## Tài sản trực quan

| SVG | Nội dung | Quan hệ cần giữ |
|---|---|---|
| `task-family.svg` | Nhóm bài toán theo đầu ra | Chủ ý thu hẹp 6 kiểu nguồn thành 5 nhóm để giảm tải; một đầu vào, năm kiểu đầu ra |
| `rule-vs-learning.svg` | Quy tắc và học từ dữ liệu | Tách huấn luyện khỏi áp dụng mô hình |
| `history-timeline.svg` | Bốn mốc lịch sử | Mỗi mốc gắn với một thay đổi kỹ thuật |
| `train-vs-infer.svg` | Hai pha vận hành | Chỉ huấn luyện cập nhật $\theta$ |
| `linear-boundary.svg` | Biên của biến đổi afin | $w^Tx+b=0$ chia hai nửa không gian |
| `perceptron.svg` | Một perceptron | Tổng trọng số, bias, hàm ngưỡng |
| `and-or-separability.svg` | AND và OR | Không lộ XOR trước L01-13 |
| `xor-points.svg` | Bốn điểm XOR | Hai lớp nằm ở các góc đối diện |
| `linear-layer.svg` | Tầng kết nối đầy đủ | Ba đầu vào tới bốn đầu ra |
| `affine-collapse.svg` | Rút gọn hai biến đổi afin | Giữ cả thành phần độ lệch |
| `mlp-anatomy.svg` | Đầu vào, ẩn, đầu ra | Kết nối đầy đủ giữa tầng kề |
| `activation-curves.svg` | ReLU, sigmoid, tanh | Đúng miền giá trị và hình dạng định tính |
| `xor-input.svg` | Không gian $X$ | Chưa lộ phép biến đổi hay kết quả |
| `xor-affine.svg` | Sau biến đổi afin | Đúng $A=(0,-1),(1,0)\times2,(2,1)$; trục $a_2$ có miền âm |
| `xor-relu-points.svg` | Sau ReLU | Chưa lộ biên tầng ra |
| `xor-relu-final.svg` | Kết quả trong $H$ | Chỉ L01-27 mới hiện biên tách |
| `xor-mlp.svg` | MLP 2–2–1 | Đúng trọng số, độ lệch và hàm kích hoạt |
| `representation-stack.svg` | Biểu diễn nhiều tầng | Từ đầu vào đến biểu diễn phục vụ dự đoán |
| `width-boundaries.svg` | Độ rộng và số mảnh biên | Chỉ là sơ đồ khái niệm, không định lượng |

Không có ngoại lệ raster. Không có phụ thuộc mạng cốt lõi.

Các tệp `boolean-separability.svg` và `relu-feature-map.svg` đã được bỏ sau khi xác nhận chỉ thuộc `lec-01` và không còn được HTML tham chiếu. Chuỗi SVG theo bước thay thế hai tệp này.

## Báo cáo phản biện độc lập và quyết định

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | L01-00–09 | Dẫn nhập chiếm quá nhiều thời gian và đổi bài toán liên tục | Bản nháp dành 24 phút, đi qua nhiều dạng đầu ra và chế độ học | Nén còn 16 phút, thêm kiểm tra vai trò, khóa phân loại nhị phân | Đã sửa; timing mới đúng danh sách 34 trang và tổng 100 phút |
| nghiêm trọng | L01-24–27 | Một hình duy nhất lộ ngay đầu vào, biến đổi và biên cuối | Cùng `relu-feature-map.svg` xuất hiện trên bốn trang | Tách hình theo bước | Đã tạo bốn SVG và chỉ hiện kết quả ở L01-27 |
| trung bình | L01-07–08, L01-13, L01-18, L01-30 | Thiếu điểm dừng để sinh viên tự phân biệt hoặc tính | Bản nháp chủ yếu giải thích liên tục | Thêm khối **Câu hỏi:** và trì hoãn bảng XOR | Đã thêm câu hỏi hiển thị; bảng L01-30 là fragment |
| trung bình | toàn deck | Bảng chữ nhỏ và bố cục màn hẹp chưa có phương án | `table.compact` ở `.72em`, viewport khóa phóng to | Tăng bảng và cho grid xếp một cột trên màn hẹp | Đã tăng `.90em`, bỏ khóa viewport và thêm media query |

### Chuyên gia Học sâu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | L01-16–23 | Cầu nối từ perceptron ngưỡng cứng sang MLP hiện đại và vai trò tầng ra chưa rõ | Hàm kích hoạt bị tách rời, softmax không nêu trục | Nêu rõ MLP hiện đại, gộp sigmoid/tanh, tách L01-22 trình bày tầng ra và L01-23 kiểm tra | Đã sửa L01-16–23; softmax theo trục lớp từng hàng $Z$ |
| nghiêm trọng | L01-32, L01-X01–X06 | Nguồn trang 35 bị dùng cho độ rộng; tuyến mở rộng lặp lõi | Trang 35 nói mạng sâu hơn hai tầng | Chuyển L01-32/X01 sang mạng sâu hơn, tổ chức lại tuyến sức biểu diễn | Đã sửa và khóa vai trò nguồn từng trang |
| trung bình | L01-X04 | Phát biểu xấp xỉ phổ dụng vượt mức nguồn ưu tiên | Bản nháp thêm miền compact và giáo trình | Rút về mệnh đề khái quát, nêu điều không được bảo đảm | Đã sửa; bỏ compact và giáo trình khỏi nguồn trang này |

### Độ chính xác toán học, thuật toán và triển khai

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | L01-25 | Mệnh đề bảo toàn không tách tuyến tính phụ thuộc giả thiết khả nghịch không cần thiết | XOR có hai bao lồi giao nhau; ảnh qua biến đổi afin của giao điểm vẫn chung | Dùng lập luận bao lồi, bỏ yêu cầu khả nghịch | Đã sửa mặt trang và ghi chú |
| nghiêm trọng | L01-14–18, L01-28 | Quy ước vector cột của nguồn và batch-first trong deck chưa được khóa | Có công thức dùng $W^\top x$ xen với $XW$ | Quy định mỗi hàng X là $x_i^\top$, mọi ma trận nhân bên phải | Đã sửa công thức và ghi chú |
| nghiêm trọng | L01-16 | “Không thể” là phát biểu tuyệt đối quá mạnh | Hàm phi tuyến vẫn có thể suy biến trên một miền hoặc bộ tham số | Đặt tiêu đề “Hàm phi tuyến tạo khả năng vượt khỏi họ biến đổi afin”; giữ “nói chung” trong phần đối chiếu | Đã sửa |
| nghiêm trọng | L01-22, L01-29–30 | Thiếu trục softmax, lưu ý loss ổn định và quy tắc đổi xác suất thành nhãn | Bản nháp chỉ liệt kê tên hàm | Nêu $Z:B\times k$, trục lớp, logits và $\hat y=\mathbb I[p\ge0.5]$ | Đã sửa |
| trung bình | L01-30 | Bảng hiện trước khi sinh viên tự tính | Toàn bộ bốn hàng đã có sẵn | Cho tính một hàng rồi mới hiện bảng | Đã dùng fragment và ghi đáp án trong notes |

### Phản biện học thuật và giảng dạy Học sâu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | L01-04 | “Lịch sử” chỉ là ba nhãn khái niệm, không có mốc thật | Hình cũ không có năm, công trình hay thay đổi kỹ thuật | Dùng 3–4 mốc có nguồn và nối từng mốc với cơ chế | Đã dùng 1943, 1949, 1969, 2012 và ghi nguồn |
| nghiêm trọng | L01-12–13 | Trang AND/OR đã lộ XOR trước khi đặt vấn đề | Một SVG chứa cả ba hàm Boolean | Tách hình AND/OR và XOR | Đã tách SVG |
| trung bình | L01-33, L01-X06 | Kết bài chỉ kiểm kích thước, chưa kiểm lập luận trung tâm hoặc giới hạn | Kết bài không phân biệt tuyến 100 và 120 phút | L01-33 kiểm XOR + kích thước; X06 kiểm sâu/rộng + giới hạn UAT | Đã sửa hai khối kết bài |
| trung bình | storyboard | Chu trình sáu bước và thời lượng không khớp nội dung thực tế | Bản cũ gán hàm kích hoạt sai trang, tổng dẫn nhập 24 phút | Ánh xạ lại từng cụm và thời lượng chính xác | Đã sửa; tuyến lõi 100 phút, mở rộng 20 phút |

Mọi lỗi `chặn bàn giao`, `nghiêm trọng` và `trung bình` trong bốn báo cáo trên đã được xử lý. Không có đề xuất nào ở ba mức này bị từ chối.

## Rà lại sau chỉnh sửa

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | L01-25–29 | Hình biến đổi afin cũ không dùng cùng $W_1,b_1$ với mạng XOR | Tham số ở L01-29 cho $A=(0,-1),(1,0),(1,0),(2,1)$, khác tọa độ SVG cũ | Vẽ lại đúng các điểm, gồm miền $a_2<0$; nêu phép gập của ReLU | Đã vẽ lại và thêm ghi chú $(0,-1)\mapsto(0,0)$ |
| nghiêm trọng | L01-32, L01-X01 | Hai trang lặp cùng hình và luận điểm mạng nhiều tầng | Cùng `representation-stack.svg` và cùng phát biểu | Giữ L01-32 làm cầu nối; dùng X01 để kiểm kích thước qua ba tầng tham số | Đã sửa X01 thành bảng kích thước và câu hỏi, không dùng hình |
| trung bình | L01-22 | Ổn định số của softmax chưa nêu phép tính theo hàng | Mới chỉ nói loss thường nhận logits | Nêu $m_i=\max_r Z_{ir}$ và trừ trong từng hàng | Đã bổ sung trong ghi chú diễn giả và `note-for-author.md` |
| trung bình | storyboard, note | Vị trí nghỉ và ánh xạ chu trình chưa đúng bằng chứng | Nghỉ ghi sau L01-15; X05 bị gán là triển khai | Chuyển nghỉ sau L01-18; ghi chu trình rút gọn và `không áp dụng` có lý do | Đã sửa, không đổi timing |

## Vòng rà soát hiện tại

Vòng rà này gồm đủ năm vai: sinh viên, chuyên gia Học sâu, độ chính xác toán/thuật toán/triển khai, phản biện học thuật/giảng dạy, kết nối/mạch viết. Mỗi phát hiện dùng các trường mức độ, trang chiếu, vấn đề, bằng chứng, đề xuất sửa, quyết định.

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| trung bình | L01-01, L01-13, L01-30 | Lời mời sau nhãn Câu hỏi chưa phải câu hỏi thật | L01-01 phát biểu mệnh đề; L01-30 mời tính nhưng bảng kề | Viết thành câu hỏi thật | Đã sửa ba trang |
| trung bình | L01-04 | Dải nguồn lịch sử hẹp hơn dải được ánh xạ | Ghi nguồn PDF tr. 41–42 | Mở thành 41–44 | Đã sửa |
| trung bình | L01-09 | Thiếu ghi chú chuyển nhãn từ nguồn sang deck | Nguồn dùng $\{-1,1\}$/sgn | Ghi chú quy ước $\{0,1\}$/chỉ thị và ngưỡng xác suất | Đã sửa trong notes |
| trung bình | L01-11 | Thiếu quy ước gán nhãn tại $z=0$ | Công thức dùng $\ge 0$ | Ghi rõ $z=0$ gán nhãn 1 | Đã sửa trong notes |
| trung bình | L01-14 | Kích thước tầng ẩn dùng $m$ trong khi toàn bài dùng $h$ | Ba dòng liệt kê dùng $m$ | Thống nhất thành $h$ | Đã sửa |
| trung bình | L01-16 | $g$ chưa được định nghĩa khi xuất hiện | Công thức dùng $g$ không giải thích | Định nghĩa $g$ là hàm phi tuyến theo phần tử, trình bày sau | Đã sửa |
| trung bình | L01-18 | Chưa nói rõ quan hệ với L01-16 | Bảng kích thước trùng công thức cũ | Notes ghi đây là đọc lại công thức L01-16 theo kích thước | Đã sửa |
| nghiêm trọng | L01-24 | Chuỗi L01-25–28 không kiểm chứng được vì thiếu $W_1,b_1$ | L01-29 mới hiện tham số | Hiển thị $W_1,b_1$ cùng công thức $A,H$ ở L01-24 | Đã sửa |
| nghiêm trọng | L01-28 | Tiêu đề mâu thuẫn nội dung: biên là tuyến tính từng đoạn | Tiêu đề cũ nói "phi tuyến" | Đổi thành "tuyến tính từng đoạn ở không gian gốc" | Đã sửa |
| trung bình | L01-29 | Trích nguồn lec05 quá rộng | Ghi tr. 13–29 | Thu hẹp thành tr. 13–14, 23–29 | Đã sửa |
| trung bình | L01-30 | Giá trị $p$ làm tròn dễ đọc như giá trị đúng | Bảng ghi 0.378, 0.622 | Thêm dấu xấp xỉ và nhãn cột "xấp xỉ" | Đã sửa |
| trung bình | L01-31 | Thiếu kích thước $Z$ trước $p$ | Danh sách chỉ có $p:4\times1$ | Thêm $Z:4\times1$ | Đã sửa |
| nghiêm trọng | L01-32 | Lặp ảnh `representation-stack.svg` với L01-05 | Cùng hình, cùng luận điểm | Bỏ ảnh, lấy công thức truy hồi làm trung tâm, ghi rõ là khái quát hóa công thức | Đã sửa |
| trung bình | L01-33 | Câu box mang tính khẩu hiệu | "Kết thúc khi giải thích được giới hạn, cơ chế và phép tính" | Thay bằng tiêu chí quan sát được | Đã sửa |
| trung bình | L01-X04 | "Mạng hai tầng" dễ gây nhầm cách đếm tầng | Nguồn đếm tầng có tham số | Nêu rõ một tầng ẩn và một tầng ra theo quy ước | Đã sửa |
| nhẹ | L01-X05 | Cụm "bank of templates" chưa Việt hóa | Notes dùng nguyên văn tiếng Anh | Việt hóa thành "tập mẫu dựng sẵn" | Đã sửa |
| trung bình | L01-X06 | Thiếu câu kiểm tra thu hồi biểu diễn phân tán và câu hỏi mở đầu | Kết bài chỉ hỏi sâu/rộng và UAT | Thêm câu kiểm tra phân tán; notes thu hồi câu hỏi mở đầu cho tuyến 120 phút | Đã sửa |
| trung bình | outline | Thiếu quy ước phân biệt vector đơn mẫu và tensor lô | Bảng ký hiệu chỉ có $X$ | Thêm dòng $\mathbf x$ chữ đậm; đồng bộ $h$ | Đã sửa |
| trung bình | storyboard | Thiếu bảng mạch ngoài; một số mô tả lệch HTML | Bản cũ không có bảng 6 mạch | Thêm bảng mạch, sửa L01-16, L01-19, L01-24, L01-28, L01-32, L01-X06 | Đã sửa, không đổi timing |
| nhẹ | review-log | Phát hiện "thiếu tài nguyên" từ một lượt rà | Reviewer chỉ được cấp bản sao văn bản | Bác phát hiện: Codex đã xác minh kho thật; reviewer chỉ được cấp bản sao văn bản nên không thấy tài nguyên | Ghi quyết định, không sửa deck |
| nhẹ | vai kết nối | Phát hiện thiếu vai thứ năm trong vòng trước | Vòng trước chỉ có bốn báo cáo | Đã xử lý bằng báo cáo hiện tại có đủ năm vai | Đã xử lý |

Các sửa cấu trúc và câu chuyển ở L01-16, L01-24, L01-28, L01-32, L01-X06 cần được vai kết nối và mạch viết rà lại cùng hai trang lân cận mỗi phía trước bàn giao.

## Tự kiểm biên tập

- Đã rà toàn bộ tiêu đề `h1`, `h2`, `h3`; sửa L01-01, L01-10, L01-15, L01-16, L01-18, L01-23, L01-25, L01-30, L01-31 và L01-X01–X04 sang cách diễn đạt thuần Việt. Dùng nhất quán “biến đổi afin”, “lan truyền xuôi” và “kích thước tensor”. Không đổi mã trang, cấu trúc, thời lượng, công thức hoặc nguồn.
- Giữ MLP, ReLU, XOR, sigmoid, tanh và perceptron trong tiêu đề vì đây là tên mô hình, hàm hoặc viết tắt thông dụng thuộc nhóm ngoại lệ. Giữ “tensor” trong cụm “kích thước tensor” để phân biệt với kích thước ma trận tham số; không dùng các cụm tiếng Anh tương ứng với “kích thước”, “lan truyền xuôi” hoặc “hàm kích hoạt” trong tiêu đề.
- L01-10 bổ sung điều kiện $\mathbf w\ne\mathbf 0$ trong ghi chú; L01-22 ghi rõ miền giá trị của đầu ra hồi quy, nhị phân và nhiều lớp. Hai bổ sung này làm chặt phát biểu hiện có, không đổi phạm vi hay thời lượng.
- Đã rà trực tiếp theo `no-ai-slop/eval.md`: bỏ câu hỏi tu từ, lời ca tụng, kết luận phóng đại, nhịp câu máy móc và thuật ngữ xoay vòng.
- Đã rà mạch theo Quill mà không tạo `quill.json`: vấn đề → khung học → giới hạn của biến đổi afin → XOR → phi tuyến → MLP → sức biểu diễn và giới hạn.
- Nội dung mặt trang không chứa mã nội bộ ngoài thuộc tính HTML, thời lượng, nhãn tuyến hoặc chỉ dẫn dành cho người soạn.
- Mọi công thức Markdown dùng `$...$` hoặc `$$...$$`.
- Đã kiểm 40 `data-slide-id` duy nhất, 40 khối ghi chú; tuyến lõi có 34 trang và đúng 100 phút, tuyến mở rộng có 6 trang và đúng 20 phút.
- Đã dựng thử 141 biểu thức bằng KaTeX cục bộ với `throwOnError: true`, `strict: "error"`; không có lỗi.
- Đã phân tích cú pháp HTML; 19 SVG đều là XML hợp lệ, có `role="img"`, `title`, `desc`; mọi SVG đều được HTML tham chiếu.
- Không có tham chiếu raster, tài nguyên cốt lõi qua mạng, liên kết cục bộ hỏng hoặc `quill.json`.
- `python3 -m reloadserver 8765` chưa chạy được trong môi trường chỉnh sửa vì thiếu mô-đun `reloadserver`; điều phối viên cần chạy lại kiểm tra máy chủ và rà trực quan trong môi trường có mô-đun hoặc ghi giới hạn khi bàn giao.

## Đối chiếu năm vai

| Vai | Phát hiện chính | Quyết định tương ứng |
|---|---|---|
| Sinh viên | Dẫn nhập quá dài, thiếu điểm dừng tự tính, bảng chữ nhỏ trên màn hẹp | Nén L01-00–09 còn 16 phút; thêm khối Câu hỏi và fragment bảng L01-30; tăng bảng `.90em` và media query |
| Chuyên gia Học sâu | Cầu nối perceptron → MLP chưa rõ; nguồn tr. 35 bị dùng sai cho độ rộng; tuyến mở rộng lặp lõi | Sửa L01-16–23; chuyển L01-32/X01 sang mạng sâu hơn; khóa vai trò nguồn từng trang |
| Độ chính xác toán học, thuật toán và triển khai | Bảo toàn tách tuyến tính phụ thuộc khả nghịch; quy ước batch-first chưa khóa; thiếu trục softmax và quy tắc ngưỡng | Dùng lập luận bao lồi; khóa mỗi hàng $X$ là $x_i^\top$; nêu $Z:B\times k$, logits và $\hat y=\mathbb I[p\ge0.5]$ |
| Phản biện học thuật và giảng dạy | Lịch sử không có mốc thật; AND/OR lộ XOR; kết bài chỉ kiểm kích thước | Dùng 1943, 1949, 1969, 2012; tách SVG AND/OR và XOR; sửa hai khối kết bài L01-33 và L01-X06 |
| Kết nối và mạch viết | Thiếu bảng mạch ngoài; mô tả mạch lệch HTML; thiếu vai thứ năm trong vòng trước | Thêm bảng sáu mạch khớp 6 section ngoài; bổ sung báo cáo đủ năm vai |

## Vòng nối tiếp

Vòng nối tiếp đã sửa: bảng sáu mạch ngoài khớp đúng 6 section ngoài của HTML, bảng chu trình Markdown hợp lệ (đoạn vai trò kép chuyển xuống sau bảng), câu hỏi L01-30 thành câu hỏi thật, và Việt hóa mọi chữ còn hiển thị trên mặt trang thành "kích thước" (kèm tiêu đề cột "Kích thước đầu ra").

## Lượt sửa tối thiểu sau xác minh của Codex

Lượt sửa tối thiểu này đã: (1) viết lại bảng sáu mạch ngoài trong storyboard thành ánh xạ 1-1 chính xác sáu section ngoài của HTML — hàng 1 L01-00–01 Mở đầu; hàng 2 L01-02–09 Học từ dữ liệu; hàng 3 L01-10–16 Giới hạn afin; hàng 4 L01-17–23 MLP và hàm kích hoạt; hàng 5 L01-24–33 ReLU, XOR và kết luận lõi; hàng 6 L01-X01–X06 Mở rộng và kết luận 120 phút — mỗi hàng có chức năng, kết nối vào và đầu ra riêng; (2) đổi câu hỏi L01-13 thành "Có thể vẽ một đường thẳng tách hai lớp không?", thay hai chữ còn trong notes L01-18 và L01-X01 bằng "kích thước", và đổi các khối .check còn mệnh lệnh (L01-23, L01-33, L01-X05) thành câu hỏi thật mà không đổi nội dung, số slide hay timing.

## Trạng thái sau chỉnh sửa

Bản hiện tại đã hợp nhất đầy đủ năm báo cáo phản biện. Điều phối viên đã hoàn tất kiểm định tĩnh, KaTeX, SVG, tham chiếu và ảnh chụp, ngoại trừ reloadserver đã ghi ở mục Kiểm định cuối.

## Rà lại sau chỉnh sửa hiện tại

Reviewer toán xác nhận toàn bộ sửa đúng, không có lỗi chặn, nghiêm trọng hay trung bình. Reviewer mạch xác nhận sáu mạch ánh xạ 1-1, các ranh giới và kết luận đạt; ba tín hiệu chuyển ý nhẹ (L01-19, L01-33 và câu tuyên bố L01-24 trong log) được xử lý trong lượt này.

## Kiểm định cuối

- 6 section ngoài của HTML khớp bảng sáu mạch.
- 40 `data-slide-id` duy nhất; 40/40 slide có khối ghi chú.
- 19 SVG phân tích XML thành công; tất cả đều có `role="img"`, `title`, `desc`.
- Không thiếu tham chiếu cục bộ; không có raster hay tài nguyên mạng.
- 141 biểu thức KaTeX dựng thành công với `throwOnError: true` và `strict: "error"`.
- Đã chụp và rà 40 slide ở 1280x720 cùng 40 slide ở 960x720; phát hiện và sửa lỗi tràn tiêu đề L01-25. Đã chụp lại L01-25 ở 960x720; tiêu đề nằm trọn khung.
- `python3 -m reloadserver 8765` không chạy được vì thiếu mô-đun `reloadserver`; máy chủ HTTP thay thế cũng không dùng được ở cổng 8765 vì cổng đang bị chiếm. Đây là ngoại lệ môi trường, không tuyên bố reloadserver đạt.
