# Storyboard Bài 01

## Bản đồ hành trình

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức hoặc tính toán | Triển khai hoặc ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|
| Học từ dữ liệu | L01-02 | L01-03–05 | L01-02–03 | L01-06 | L01-07–09 | L01-07–08 |
| Giới hạn của biến đổi afin | L01-10 | L01-11–12 | L01-13 | L01-14–16 | Không áp dụng: bài chưa chuyển sang lượt lan truyền xuôi của MLP | L01-13 |
| MLP và kích hoạt | L01-15 | L01-16–17 | L01-18, L01-20–22 | L01-18, L01-20–22 | L01-18 và L01-22 nối công thức với lượt lan truyền xuôi, tầng ra | L01-18, L01-20, L01-23 |
| ReLU và XOR | L01-24–25 | L01-26–28 | L01-29–30 | L01-29–31 | Lượt lan truyền xuôi cho toàn bộ lô ở L01-30 | L01-30–31, L01-33 |
| Sức biểu diễn và giới hạn | L01-X01 | L01-X02–X03 | L01-X01 và minh họa định tính L01-X03 | L01-X04 | Không áp dụng: nguồn bàn sức biểu diễn, không có triển khai | L01-X06 |

Các cụm học từ dữ liệu, MLP–kích hoạt và ReLU–XOR dùng chu trình đầy đủ hoặc gần đầy đủ. Cụm giới hạn của biến đổi afin dùng chu trình rút gọn vì chưa có triển khai MLP. Cụm mở rộng cũng rút gọn: L01-X05 minh họa biểu diễn phân tán, không được gán là bước triển khai.

Kiến thức đầu vào là phép nhân ma trận và phân loại nhị phân. Sản phẩm học tập cuối là lời giải thích kiểm chứng được về việc MLP giải XOR, kèm kích thước tensor và số tham số. Bốn điểm XOR giữ nguyên từ L01-13 đến L01-31. Mỗi hàng của $X$ là $x_i^\top$; các ký hiệu $X,W_1,b_1,H,W_2,b_2,Z$ giữ nguyên từ công thức tổng quát sang ví dụ số.

## Trang lõi, tổng 100 phút

| Trang | Phút | Luận điểm và sản phẩm học tập | Đầu vào → đầu ra | Câu nối |
|---|---:|---|---|---|
| L01-00 | 1 | Khóa chủ đề và câu hỏi dẫn nhập | Đề cương → vấn đề của bài | Bắt đầu từ tác vụ khó viết quy tắc |
| L01-01 | 2 | Nêu hai nhóm năng lực cần đạt | Tiên quyết → kết quả quan sát được | Xét một tác vụ cụ thể |
| L01-02 | 2 | Có tác vụ rõ đầu vào và đầu ra nhưng thiếu quy tắc | Ảnh, tiếng nói, cảm biến → nhãn hoặc hành động | Thay quy tắc bằng dữ liệu |
| L01-03 | 2 | Phân biệt chương trình quy tắc và mô hình học | Dữ liệu có nhãn → mô hình tham số | Đặt thay đổi này vào lịch sử kỹ thuật |
| L01-04 | 1 | Bốn mốc nối với bốn thay đổi kỹ thuật | 1943, 1949, 1969, 2012 → đơn vị, học, giới hạn, quy mô | Học sâu khác ở chuỗi biểu diễn |
| L01-05 | 2 | Học sâu hợp thành nhiều tầng biểu diễn | $x$ → biểu diễn tầng sâu | Đặt chuỗi tầng vào khung học thống kê |
| L01-06 | 2 | Dữ liệu, mô hình và tiêu chí có vai trò khác nhau | $(x_i,y_i),f_\theta,\ell$ → bài toán ước lượng | Tách huấn luyện và suy luận |
| L01-07 | 2 | Chỉ huấn luyện cập nhật tham số | Dữ liệu huấn luyện và mẫu mới → $\theta,\hat y$ | Kiểm tra ba vai trò |
| L01-08 | 1 | Phân biệt dữ liệu, tham số, dự đoán | $x,\theta,\hat y$ → vai trò đúng | Khóa bài toán cụ thể |
| L01-09 | 1 | Thu hẹp sang phân loại nhị phân có giám sát | $x_i\in\mathbb R^d,y_i\in\{0,1\}$ → phạm vi tiếp theo | Xét biên quyết định |
| L01-10 | 4 | Biên của biến đổi afin là một siêu phẳng khi $\mathbf w\ne\mathbf 0$ | $\mathbf x,\mathbf w,b$ → $z=0$ | Một đơn vị tính biên này như thế nào |
| L01-11 | 3 | Perceptron là tổng trọng số, độ lệch và ngưỡng | $\mathbf x$ → $z$ → $\hat y$ | Kiểm tra các hàm Boolean đơn giản |
| L01-12 | 3 | AND và OR tách tuyến tính, chưa lộ XOR | Bốn đỉnh Boolean → một đường tách | Chuyển sang cấu hình xen kẽ |
| L01-13 | 5 | XOR không có một đường tách | Bảng XOR, bao lồi → giới hạn perceptron | Thử tăng số đơn vị |
| L01-14 | 3 | Nhiều đơn vị tạo một tầng ma trận | Hàng $x_i^\top$, $X,W,b$ → $Y$ và kích thước tensor | Thử xếp hai tầng |
| L01-15 | 5 | Hợp thành nhiều biến đổi afin vẫn là một biến đổi afin | $X,W_1,b_1,W_2,b_2$ → biến đổi afin tương đương | Thêm hàm phi tuyến |
| L01-16 | 3 | Hàm phi tuyến tạo khả năng vượt khỏi họ biến đổi afin | Tiền kích hoạt → biểu diễn phi tuyến | Đặt cơ chế vào cấu trúc MLP |
| L01-17 | 4 | MLP có đầu vào, tầng ẩn và tầng ra | Các đơn vị → kiến trúc 2 tầng | Theo dõi tensor qua mạng |
| L01-18 | 5 | Lan truyền xuôi phải giữ đúng kích thước tensor | $B,d,h,k$ → kích thước từng tensor | Nghỉ ngắn rồi chọn hàm kích hoạt |
| L01-19 | 2 | Tổng quan vai trò và miền ra của hàm kích hoạt | Tiền kích hoạt → ba họ hàm | Xét ReLU |
| L01-20 | 3 | ReLU giữ dương và chặn âm | Vector nhỏ → vector sau ReLU | So với hàm bị chặn |
| L01-21 | 3 | Sigmoid và tanh đều bị chặn | Logit → $(0,1)$ hoặc $(-1,1)$ | Chọn tầng ra |
| L01-22 | 3 | Trình bày cách chọn tầng ra theo miền đích | $Z:B\times k$ → sigmoid hoặc softmax theo lớp | Kiểm tra lựa chọn |
| L01-23 | 2 | Kiểm tra cách chọn hàm kích hoạt | Ba tình huống → ReLU, sigmoid, softmax | Quay lại tác động hình học của ReLU |
| L01-24 | 3 | Đặt bài toán biến đổi XOR sang không gian ẩn | Bốn điểm ở X → biến đổi afin rồi ReLU | Xét riêng biến đổi afin |
| L01-25 | 3 | Biến đổi afin không làm XOR tách tuyến tính | $A=(0,-1),(1,0)\times2,(2,1)$; điểm lớp 1 nằm trên bao lồi lớp 0 | Thêm ReLU |
| L01-26 | 5 | ReLU ép miền âm lên biên tọa độ | $a_j$ → $h_j$ và các điểm H, chưa có biên | Quan sát khả năng tách |
| L01-27 | 3 | Tầng ra dùng biên của biến đổi afin trong không gian ẩn | $H$ → biên xuất hiện | Kéo biên về không gian gốc |
| L01-28 | 3 | Biên trở thành tuyến tính từng đoạn trong X | $Z=\operatorname{ReLU}(XW_1+b_1)W_2+b_2$ | Dựng mạng giải XOR |
| L01-29 | 5 | Mạng 2–2–1 có tham số dựng tay cho XOR | Bảng XOR → $W_1,b_1,W_2,b_2$ và quy tắc $\hat y$ | Tính một hàng |
| L01-30 | 6 | Bốn đầu vào đi qua cùng một lượt lan truyền xuôi | $X:4\times2$ → $H$, logit, $p$, $\hat y$ | Kiểm tra kích thước tensor và độ lớn mô hình |
| L01-31 | 3 | Kích thước tensor và số tham số của mạng XOR | Kích thước tensor → 9 tham số | Mở sang mạng sâu hơn |
| L01-32 | 2 | Mạng sâu hơn hợp thành nhiều biểu diễn | $H_{\ell-1}$ → $H_\ell$ | Chốt tuyến lõi |
| L01-33 | 3 | Kiểm cả lý do XOR cần phi tuyến và kích thước tensor | XOR, $32\times10$, $h=20$, $k=3$ → lời giải thích và phép tính | Kết thúc tuyến 100 phút |

## Trang mở rộng, tổng 20 phút

Các trang này nằm trong một phần riêng sau tuyến lõi. Có thể bỏ cả phần khi hết giờ; không cần đổi thứ tự trang lõi.

| Trang | Phút | Luận điểm | Nguồn | Câu nối |
|---|---:|---|---|---|
| L01-X01 | 3 | Kiểm tra kích thước tensor qua ba tầng tham số | `lec05_multilayer.pdf` tr. 35 | Phân biệt hai trục kiến trúc |
| L01-X02 | 4 | Độ sâu và độ rộng thay đổi cấu trúc theo hai cách | `lec05_multilayer.pdf` tr. 29, 35 | Xem minh họa biên nhiều mảnh |
| L01-X03 | 3 | Biên quyết định nhiều mảnh là minh họa định tính | `lec05_multilayer.pdf` tr. 29 | Đặt giới hạn cho kết luận biểu diễn |
| L01-X04 | 3 | Xấp xỉ phổ dụng chỉ là mệnh đề về sức biểu diễn | `lec05_multilayer.pdf` tr. 29 | Sức biểu diễn không đồng nghĩa dễ học |
| L01-X05 | 3 | Biểu diễn thường phân tán | `lec05_multilayer.pdf` tr. 30–34 | Kiểm tra sức biểu diễn và giới hạn |
| L01-X06 | 4 | Kiểm tra độ sâu, độ rộng và giới hạn của UAT | `lec05_multilayer.pdf` tr. 29–35 | Kết thúc tuyến đầy đủ 120 phút |

## Bài tập 50 phút, tách khỏi deck

| Hoạt động | Phút | Sản phẩm |
|---|---:|---|
| Chứng minh trực quan XOR không tách tuyến tính | 10 | Lập luận dựa trên bốn đỉnh hình vuông |
| Vẽ MLP và ghi kích thước tensor | 20 | Sơ đồ lô theo hàng cùng kích thước mọi tham số và tensor |
| So sánh các biến đổi afin với MLP ReLU | 15 | Phép rút gọn đại số và một phản ví dụ phi tuyến |
| Quiz | 5 | Bốn câu ngắn về thuật ngữ, hàm kích hoạt và số tham số |

Đáp án và cách điều phối nằm trong `note-for-author.md`, không đưa vào trang chiếu.
