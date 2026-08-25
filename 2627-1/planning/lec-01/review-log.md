# Nhật ký rà soát Bài 01

## Kiểm kê và chuyển nguồn

- Đã dùng đúng dải nguồn được `source.md` duyệt cho Buổi 01.
- Đã Việt hóa mạch chính của `lec05_multilayer.pdf` trước khi bổ sung từ giáo trình.
- Đã đối chiếu `lec01_intro.pdf` tr. 3–15, 17–24; `lec02_linear_part1.pdf` tr. 15–21; `lec05_multilayer.pdf` tr. 2–35.
- Giáo trình chỉ được dùng để khôi phục khung học, kiểm chứng shape, thuật ngữ và điều kiện phát biểu.
- Không dùng code, benchmark hoặc tài liệu ngoài danh mục.

## Quyết định sai khác so với nguồn

| Quyết định | Bằng chứng | Cách xử lý | Lý do |
|---|---|---|---|
| Dùng “affine” cho $Wx+b$ | `lec02_linear_part1.pdf`, tr. 15–17 và `lec05_multilayer.pdf`, tr. 7–8 thường gọi rộng là linear | Gọi $Wx$ là tuyến tính, $Wx+b$ là affine | Chính xác về toán học và làm rõ phép rút gọn hai tầng |
| Không khẳng định tầng ra luôn có activation phi tuyến | `lec05_multilayer.pdf`, tr. 28 | L01-23 chọn activation theo miền đích; hồi quy có thể dùng đồng nhất | Tránh mâu thuẫn với đầu ra hồi quy và logit |
| Giữ xấp xỉ phổ dụng ở mức nguồn | `lec05_multilayer.pdf`, tr. 29 chỉ nêu mệnh đề khái quát | Không thêm miền compact hoặc lớp hàm; nêu rõ mệnh đề không bảo đảm học hay khái quát | Tôn trọng slide nguồn là nguồn ưu tiên |
| Nêu ReLU không khả vi tại 0 | `lec05_multilayer.pdf`, tr. 11–12; giáo trình PDF tr. 87 | Ghi rõ khả vi gần như mọi nơi và hiện thực chọn quy ước tại 0 | Tránh tuyên bố ReLU khả vi mọi nơi |
| Chuyển toàn bộ ký hiệu sang batch-first | Nguồn slide dùng vector cột; giáo trình dùng ma trận dữ liệu | Dùng $X:B\times d$, $W:d\times h$, broadcasting độ lệch theo batch | Nhất quán với tiêu chuẩn học phần và ví dụ XOR |
| Diễn giải tầng ẩn là biểu diễn phân tán | `lec05_multilayer.pdf`, tr. 30–34 | Không gán một ý nghĩa bắt buộc cho từng đơn vị | Giữ đúng cảnh báo của nguồn về khả năng diễn giải |
| Dựng ví dụ XOR 2–2–1 | Đề cương yêu cầu MLP; `lec02_linear_part1.pdf`, tr. 19 nêu XOR | Dùng tham số đã tự tính và ghi rõ không phải kết quả huấn luyện | Tạo ví dụ kiểm tra được từ giới hạn sang giải pháp |
| Đưa cấu trúc MLP trước chuỗi hình ReLU | `lec05_multilayer.pdf`, tr. 28 định nghĩa mạng hai tầng; tr. 13–27 minh họa sức mạnh ReLU | Dạy cấu trúc và shape ở L01-17–23 rồi mới dùng chuỗi hình ở L01-24–28 | Sinh viên cần biết tầng ẩn, activation và tầng ra trước khi đọc chuỗi biến đổi; đây là đổi thứ tự nguồn có chủ ý |
| Thu hẹp L01-09 sang phân loại nhị phân | Đề cương Buổi 1 và ví dụ perceptron/XOR ở `lec02_linear_part1.pdf`, tr. 15–21 | Bỏ ba chế độ học khỏi mặt trang, khóa $x_i\in\mathbb R^d$, $y_i\in\{0,1\}$ | Giảm tải dẫn nhập và giữ một bài toán xuyên suốt |
| Tách chuỗi hình ReLU theo bước | `lec05_multilayer.pdf`, tr. 13–27 tăng dần thông tin | Tạo SVG đầu vào, sau affine, sau ReLU và kết quả có biên | Không lộ kết quả trước khi sinh viên quan sát từng phép biến đổi |
| Rút phát biểu xấp xỉ phổ dụng | `lec05_multilayer.pdf`, tr. 29 chỉ nêu mệnh đề khái quát | Bỏ điều kiện compact và tham chiếu giáo trình; chỉ nêu giới hạn của kết luận | Không đưa chi tiết không có trong slide nguồn được ưu tiên |
| Vẽ lại toàn bộ hình kỹ thuật | Hình nguồn cần chuyển và chuỗi hình cần tách bước | Dùng SVG có `role="img"`, `title`, `desc` và nhãn Việt | Tuân thủ quy định không trích raster |

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
| `task-family.svg` | Nhóm bài toán theo đầu ra | Một đầu vào, năm kiểu đầu ra |
| `rule-vs-learning.svg` | Quy tắc và học từ dữ liệu | Tách huấn luyện khỏi áp dụng mô hình |
| `history-timeline.svg` | Bốn mốc lịch sử | Mỗi mốc gắn với một thay đổi kỹ thuật |
| `train-vs-infer.svg` | Hai pha vận hành | Chỉ huấn luyện cập nhật $\theta$ |
| `linear-boundary.svg` | Biên affine | $w^Tx+b=0$ chia hai nửa không gian |
| `perceptron.svg` | Một perceptron | Tổng trọng số, bias, hàm ngưỡng |
| `and-or-separability.svg` | AND và OR | Không lộ XOR trước L01-13 |
| `xor-points.svg` | Bốn điểm XOR | Hai lớp nằm ở các góc đối diện |
| `linear-layer.svg` | Tầng kết nối đầy đủ | Ba đầu vào tới bốn đầu ra |
| `affine-collapse.svg` | Rút gọn hai tầng affine | Giữ cả thành phần độ lệch |
| `mlp-anatomy.svg` | Đầu vào, ẩn, đầu ra | Kết nối đầy đủ giữa tầng kề |
| `activation-curves.svg` | ReLU, sigmoid, tanh | Đúng miền giá trị và hình dạng định tính |
| `xor-input.svg` | Không gian $X$ | Chưa lộ phép biến đổi hay kết quả |
| `xor-affine.svg` | Sau phép affine | Đúng $A=(0,-1),(1,0)\times2,(2,1)$; trục $a_2$ có miền âm |
| `xor-relu-points.svg` | Sau ReLU | Chưa lộ biên tầng ra |
| `xor-relu-final.svg` | Kết quả trong $H$ | Chỉ L01-27 mới hiện biên tách |
| `xor-mlp.svg` | MLP 2–2–1 | Đúng trọng số, bias và activation |
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
| nghiêm trọng | L01-16–23 | Cầu nối từ perceptron ngưỡng cứng sang MLP hiện đại và vai trò tầng ra chưa rõ | Activation bị tách rời, softmax không nêu trục | Nêu rõ MLP hiện đại, gộp sigmoid/tanh, tách chọn tầng ra và kiểm tra | Đã sửa L01-16–23; softmax theo trục lớp từng hàng $Z$ |
| nghiêm trọng | L01-32, L01-X01–X06 | Nguồn trang 35 bị dùng cho độ rộng; tuyến mở rộng lặp lõi | Trang 35 nói mạng sâu hơn hai tầng | Chuyển L01-32/X01 sang mạng sâu hơn, tổ chức lại tuyến sức biểu diễn | Đã sửa và khóa vai trò nguồn từng trang |
| trung bình | L01-X04 | Phát biểu xấp xỉ phổ dụng vượt mức nguồn ưu tiên | Bản nháp thêm miền compact và giáo trình | Rút về mệnh đề khái quát, nêu điều không được bảo đảm | Đã sửa; bỏ compact và giáo trình khỏi nguồn trang này |

### Độ chính xác toán học, thuật toán và triển khai

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | L01-25 | Mệnh đề bảo toàn không tách tuyến tính phụ thuộc giả thiết khả nghịch không cần thiết | XOR có hai bao lồi giao nhau; ảnh affine của giao điểm vẫn chung | Dùng lập luận bao lồi, bỏ yêu cầu khả nghịch | Đã sửa mặt trang và ghi chú |
| nghiêm trọng | L01-14–18, L01-28 | Quy ước vector cột của nguồn và batch-first trong deck chưa được khóa | Có công thức dùng $W^\top x$ xen với $XW$ | Quy định mỗi hàng X là $x_i^\top$, mọi ma trận nhân bên phải | Đã sửa công thức và ghi chú |
| nghiêm trọng | L01-16 | “Không thể” là phát biểu tuyệt đối quá mạnh | g phi tuyến vẫn có thể suy biến trên một miền hoặc bộ tham số | Dùng “g không affine cho phép; nói chung không rút” | Đã sửa |
| nghiêm trọng | L01-22, L01-29–30 | Thiếu trục softmax, lưu ý loss ổn định và quy tắc đổi xác suất thành nhãn | Bản nháp chỉ liệt kê tên hàm | Nêu $Z:B\times k$, trục lớp, logits và $\hat y=\mathbb I[p\ge0.5]$ | Đã sửa |
| trung bình | L01-30 | Bảng hiện trước khi sinh viên tự tính | Toàn bộ bốn hàng đã có sẵn | Cho tính một hàng rồi mới hiện bảng | Đã dùng fragment và ghi đáp án trong notes |

### Phản biện học thuật và giảng dạy Học sâu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | L01-04 | “Lịch sử” chỉ là ba nhãn khái niệm, không có mốc thật | Hình cũ không có năm, công trình hay thay đổi kỹ thuật | Dùng 3–4 mốc có nguồn và nối từng mốc với cơ chế | Đã dùng 1943, 1949, 1969, 2012 và ghi nguồn |
| nghiêm trọng | L01-12–13 | Trang AND/OR đã lộ XOR trước khi đặt vấn đề | Một SVG chứa cả ba hàm Boolean | Tách hình AND/OR và XOR | Đã tách SVG |
| trung bình | L01-33, L01-X06 | Kết bài chỉ kiểm shape, chưa kiểm lập luận trung tâm hoặc giới hạn | Closure không phân biệt tuyến 100 và 120 phút | L01-33 kiểm XOR + shape; X06 kiểm sâu/rộng + giới hạn UAT | Đã sửa hai closure |
| trung bình | storyboard | Chu trình sáu bước và timing không khớp nội dung thực tế | Bản cũ gán activation sai trang, tổng dẫn nhập 24 phút | Ánh xạ lại từng cụm và timing chính xác | Đã sửa; tuyến lõi 100 phút, mở rộng 20 phút |

Mọi lỗi `chặn bàn giao`, `nghiêm trọng` và `trung bình` trong bốn báo cáo trên đã được xử lý. Không có đề xuất nào ở ba mức này bị từ chối.

## Rà lại sau chỉnh sửa

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | L01-25–29 | Hình affine cũ không dùng cùng $W_1,b_1$ với mạng XOR | Tham số ở L01-29 cho $A=(0,-1),(1,0),(1,0),(2,1)$, khác tọa độ SVG cũ | Vẽ lại đúng các điểm, gồm miền $a_2<0$; nêu phép gập của ReLU | Đã vẽ lại và thêm ghi chú $(0,-1)\mapsto(0,0)$ |
| nghiêm trọng | L01-32, L01-X01 | Hai trang lặp cùng hình và luận điểm mạng nhiều tầng | Cùng `representation-stack.svg` và cùng phát biểu | Giữ L01-32 làm cầu nối; dùng X01 để kiểm shape qua ba tầng tham số | Đã sửa X01 thành bảng shape và câu hỏi, không dùng hình |
| trung bình | L01-22 | Ổn định số của softmax chưa nêu phép tính theo hàng | Mới chỉ nói loss thường nhận logits | Nêu $m_i=\max_r Z_{ir}$ và trừ trong từng hàng | Đã bổ sung trong ghi chú diễn giả và `note-for-author.md` |
| trung bình | storyboard, note | Vị trí nghỉ và ánh xạ chu trình chưa đúng bằng chứng | Nghỉ ghi sau L01-15; X05 bị gán là triển khai | Chuyển nghỉ sau L01-18; ghi chu trình rút gọn và `không áp dụng` có lý do | Đã sửa, không đổi timing |

## Tự kiểm biên tập

- Đã rà trực tiếp theo `no-ai-slop/eval.md`: bỏ câu hỏi tu từ, lời ca tụng, kết luận phóng đại, nhịp câu máy móc và thuật ngữ xoay vòng.
- Đã rà mạch theo Quill mà không tạo `quill.json`: vấn đề → khung học → giới hạn affine → XOR → phi tuyến → MLP → sức biểu diễn và giới hạn.
- Nội dung mặt trang không chứa mã nội bộ ngoài thuộc tính HTML, thời lượng, nhãn tuyến hoặc chỉ dẫn dành cho người soạn.
- Mọi công thức Markdown dùng `$...$` hoặc `$$...$$`.
- Đã kiểm 40 `data-slide-id` duy nhất, 40 khối ghi chú; tuyến lõi có 34 trang và đúng 100 phút, tuyến mở rộng có 6 trang và đúng 20 phút.
- Đã dựng thử 128 biểu thức bằng KaTeX cục bộ với `throwOnError: true`, `strict: "error"`; không có lỗi.
- Đã phân tích cú pháp HTML; 19 SVG đều là XML hợp lệ, có `role="img"`, `title`, `desc`; mọi SVG đều được HTML tham chiếu.
- Không có tham chiếu raster, tài nguyên cốt lõi qua mạng, liên kết cục bộ hỏng hoặc `quill.json`.
- `python3 -m reloadserver 8765` chưa chạy được trong môi trường chỉnh sửa vì thiếu mô-đun `reloadserver`; điều phối viên cần chạy lại kiểm tra máy chủ và rà trực quan trong môi trường có mô-đun hoặc ghi giới hạn khi bàn giao.

## Trạng thái sau chỉnh sửa

Bản hiện tại đã hợp nhất bốn báo cáo phản biện. Điều phối viên cần chạy kiểm định HTML, KaTeX, SVG, tham chiếu cục bộ và rà trực quan trước khi bàn giao.
