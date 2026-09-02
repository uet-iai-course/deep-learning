# Bài 01: Giới thiệu Học sâu và mạng perceptron đa lớp

## Phạm vi và kết quả học tập

Bài học tuân theo đề cương tại `III.2 → Buổi 1`, phục vụ LLO1–LLO2. Sau buổi học, sinh viên có thể:

- phân biệt viết quy tắc với học ánh xạ từ dữ liệu;
- phân biệt dữ liệu, mô hình, tham số, tiêu chí, huấn luyện và suy luận;
- giải thích giới hạn hình học của bộ phân loại dùng biến đổi afin qua XOR;
- mô tả đầu vào, tầng ẩn, tầng ra và hàm kích hoạt của mạng perceptron đa lớp (MLP);
- thực hiện lượt lan truyền xuôi với lô dữ liệu theo hàng, kiểm tra kích thước tensor và tính số tham số;
- giải thích cách một tầng ẩn ReLU tạo biểu diễn để giải XOR.

Tiên quyết: vector, ma trận, phép nhân ma trận, hàm số, bài toán phân loại nhị phân. Lan truyền ngược, tối ưu và thiết kế thí nghiệm nằm ngoài phạm vi.

## Mạch khái niệm

1. Tác vụ khó viết quy tắc dẫn đến học từ dữ liệu.
2. Bốn mốc kỹ thuật nối đơn vị tính toán, quy tắc học, giới hạn perceptron và huấn luyện mạng sâu.
3. Dữ liệu, tham số và dự đoán có vai trò khác nhau; bài học thu hẹp sang phân loại nhị phân có giám sát.
4. Mô hình dùng biến đổi afin tạo biên phẳng; XOR cho thấy giới hạn.
5. Hợp thành các biến đổi afin không thay đổi giới hạn đó.
6. Hàm kích hoạt phi tuyến tạo khả năng vượt khỏi họ biến đổi afin; với các trường hợp suy biến, chuỗi vẫn có thể rút gọn trên miền đang xét.
7. MLP hiện đại dùng hàm kích hoạt ở đơn vị ẩn, tạo logit rồi đổi thành đầu ra phù hợp.
8. ReLU biến đổi hình học dữ liệu; tầng ra tách trong không gian ẩn.
9. Mạng ReLU 2–2–1 cho một lượt lan truyền xuôi kiểm chứng được trên XOR.
10. Tuyến mở rộng kiểm tra kích thước tensor qua ba tầng tham số rồi nối độ sâu, độ rộng, biên nhiều mảnh, xấp xỉ phổ dụng và biểu diễn phân tán.

Mạch này đã được rà theo Quill: **vấn đề → khung học → giới hạn của biến đổi afin → XOR → phi tuyến → MLP → sức biểu diễn và giới hạn**. Cầu nối vector cột của slide nguồn sang lô dữ liệu theo hàng được khóa bằng quy ước mỗi hàng $X$ là $x_i^\top$. Không khởi tạo `quill.json`.

## Phân bổ thời lượng

- Tuyến lõi: 34 trang, 100 phút.
- Tuyến mở rộng: 6 trang, 20 phút; có thể bỏ toàn bộ mà không đứt mạch lõi.
- Bài tập: 50 phút, tách khỏi thời lượng deck.

## Ánh xạ nguồn

| Cụm | Trang đích | Nguồn chính | Nguồn kiểm chứng hoặc bổ sung |
|---|---|---|---|
| Bối cảnh, lịch sử và khung học | L01-00–09 | `lec01_intro.pdf`, tr. 3–15; `lec02_linear_part1.pdf`, tr. 19 | Đề cương Buổi 1; giáo trình PDF tr. 25–45 |
| Biến đổi afin và XOR | L01-10–16 | `lec02_linear_part1.pdf`, tr. 15–21; `lec05_multilayer.pdf`, tr. 4–10 | Giáo trình PDF tr. 83–86 |
| MLP và hàm kích hoạt | L01-17–23 | `lec05_multilayer.pdf`, tr. 11–12, 28 | Giáo trình PDF tr. 83–90 và 66–73 |
| ReLU, XOR và mạng sâu hơn | L01-24–32 | `lec05_multilayer.pdf`, tr. 13–27, 35 | Đề cương Buổi 1; ví dụ XOR tự tính |
| Kiểm tra | L01-33 | Đề cương Buổi 1 | Giáo trình PDF tr. 85–86 |
| Mở rộng: sức biểu diễn và giới hạn | L01-X01–X06 | `lec05_multilayer.pdf`, tr. 29–35 | X01 kiểm tra kích thước tensor qua ba tầng; không lặp hình hoặc luận điểm cầu nối ở L01-32 |

Không dùng các dải nguồn bị loại trong `source.md`. Không dùng nguồn web, code demo hoặc ảnh raster.

## Bảng thuật ngữ và ký hiệu

| Thuật ngữ hoặc ký hiệu | Nghĩa và quy ước |
|---|---|
| MLP | Mạng perceptron đa lớp, mạng truyền thẳng kết nối đầy đủ; số tầng đếm tầng có tham số, không đếm tầng đầu vào |
| $B$ | Kích thước batch; trục đầu tiên của mọi tensor theo batch |
| $d,h,k$ | Số đặc trưng đầu vào, số đơn vị ẩn, số đầu ra; dùng $h$ cho kích thước tầng ẩn trên toàn bài |
| $X\in\mathbb R^{B\times d}$ | Ma trận đầu vào, batch-first; hàng thứ $i$ là $x_i^\top$ |
| $\mathbf x\in\mathbb R^d$ | Vector đơn mẫu, chữ đậm; tensor lô $X$ xếp các vector đơn mẫu theo hàng |
| $W_1\in\mathbb R^{d\times h}$, $b_1\in\mathbb R^h$ | Tham số tầng ẩn |
| $H=g(XW_1+b_1)\in\mathbb R^{B\times h}$ | Biểu diễn ẩn; độ lệch broadcasting theo batch |
| $W_2\in\mathbb R^{h\times k}$, $b_2\in\mathbb R^k$ | Tham số tầng ra |
| $Z=HW_2+b_2\in\mathbb R^{B\times k}$ | Điểm số hoặc logit, chưa mặc nhiên là xác suất |
| $g$ | Hàm kích hoạt theo phần tử, thường là ReLU trong bài này |
| $\hat y$ | Dự đoán; phân biệt với nhãn $y$ |

## Bài tập 50 phút

1. XOR và giới hạn tuyến tính, 10 phút.
2. Vẽ MLP và ghi kích thước tensor, 20 phút.
3. So sánh chuỗi biến đổi afin với MLP dùng ReLU, 15 phút.
4. Quiz kiểm tra thuật ngữ và số tham số, 5 phút.

Đề bài, cách tổ chức và đáp án chi tiết nằm trong `note-for-author.md`.

# Đầu ra lecture note — Buổi 01

Mục này giữ nguyên bằng chứng deck ở trên và bổ sung hợp đồng với tài liệu tự học.

## Mục tiêu lecture note

Tài liệu tự học tiếng Việt đọc độc lập, bám LLO1–LLO2, không mở rộng sang lan truyền ngược hay tối ưu. Sau khi đọc, sinh viên có thể:

- giải thích vì sao một số tác vụ khó viết quy tắc và cần học từ dữ liệu;
- phân biệt biến đổi tuyến tính $Wx$ với afin $Wx+b$, và logit với xác suất;
- chứng minh trực quan XOR không tách được bằng biên afin qua bao lồi;
- mô tả cấu trúc MLP, quy ước batch-first, kích thước tensor, broadcasting và số tham số;
- tính lan truyền xuôi cho mạng ReLU 2–2–1 giải XOR và kiểm chứng bằng tay;
- giải thích khái quát sức biểu diễn của mạng nhiều lớp cùng giới hạn giữa biểu diễn được và dễ huấn luyện.

Các mục tiêu này giữ đúng mạch slide và phép tính đã khóa tại checkpoint A1; softmax chỉ là cầu nối tầng ra, xấp xỉ phổ dụng chỉ trình bày ở mức nguồn.

## Bản đồ 9 chủ đề — hợp đồng note-topic-id ↔ data-slide-id

| note-topic-id | Nhãn | Vai trò trong lecture note | data-slide-id |
|---|---|---|---|
| NT01-van-de-va-boi-canh | cốt lõi | Tác vụ khó viết quy tắc; học từ dữ liệu | L01-00–05 |
| NT02-hoc-tu-du-lieu | cầu nối | Dữ liệu, mô hình, tham số, tiêu chí, huấn luyện, suy luận; khóa phân loại nhị phân | L01-06–09 |
| NT03-bien-doi-afin | cốt lõi | Perceptron/biên quyết định; phân biệt tuyến tính và afin | L01-10–12 |
| NT04-xor | cốt lõi | AND/OR đối chiếu; XOR không tách tuyến tính bằng bao lồi | L01-13, L01-25 |
| NT05-hop-thanh-va-phi-tuyen | cốt lõi | Rút gọn hai tầng afin; vai trò hàm kích hoạt phi tuyến | L01-14–16 |
| NT06-cau-truc-mlp | cốt lõi | Tầng vào/ẩn/ra, công thức batch-first, tensor, broadcasting, số tham số | L01-17–18, L01-31–32, L01-X01 |
| NT07-ham-kich-hoat-va-dau-ra | cốt lõi | ReLU, sigmoid, tanh; chọn tầng ra; softmax chỉ là phần nối | L01-19–23 |
| NT08-mlp-relu-giai-xor | cốt lõi | Tính $A,H,z,p,\hat y$ cho bốn mẫu bằng mạng 2–2–1; 9 tham số; biên từng đoạn | L01-24–30 |
| NT09-suc-bieu-dien-va-gioi-han | bổ sung | Sâu/rộng, xấp xỉ phổ dụng (khái quát), biểu diễn phân tán, giới hạn, nối Buổi 02 | L01-33, L01-X02–X06 |

Không có chủ đề `đọc thêm` trong thân bài; lecture note không nhắc lại timing, mã trang, trạng thái kiểm chứng hay hướng dẫn cho người viết/diễn giả.

## Nguồn của lecture note

- Slide: `lec01_intro.pdf` 3–15, 13–15; `lec02_linear_part1.pdf` 15–19; `lec05_multilayer.pdf` 4–12, 13–29, 28, 35, 29–35.
- Giáo trình PDF: tr. 29–35, 41–42, 55–56, 66–73, 83–90.
- DOCX Buổi 1 và hoạt động XOR; ví dụ tự tính được ghi trong `review-log.md`.
- Phép tính khóa: tham số dựng tay, bốn hàng XOR `(0,0),(0,1),(1,0),(1,1)`; ví dụ cuối $B=32,d=10,h=20,k=3$.
- Không dùng dải nguồn bị loại, nguồn web, code demo hay ảnh raster.

## Ký hiệu và quy ước dùng chung

| Ký hiệu | Nghĩa và quy ước |
|---|---|
| Batch-first | Mỗi hàng của $X\in\mathbb R^{B\times d}$ là một mẫu $x_i^\top$; $B$ trục đầu |
| $A=XW_1+b_1$ | Phép afin tầng ẩn theo chiều lô; $b_1$ broadcasting theo lô |
| $H=\operatorname{ReLU}(A)$ | Biểu diễn ẩn |
| $z=HW_2+b_2$ | Logit; chữ thường $z$ khi một đầu ra, hoa $Z=HW_2+b_2$ khi nhiều lớp |
| $p=\sigma(z)$ | Xác suất qua sigmoid |
| $\hat y=\mathbf 1[p\ge0.5]$ | Dự đoán theo ngưỡng 0.5 |

Mọi phép tính trong buổi là suy luận trên dữ liệu cho trước, không phải huấn luyện. Ký hiệu này thống nhất với deck và bảng thuật ngữ ở phần trên.

## SVG tái sử dụng trong lecture note

Hai SVG có sẵn được tham chiếu bằng đường dẫn viewer `img/lec-01/`, giúp lập luận trong bài và không tạo raster:

| Tệp | Vị trí dùng | Vai trò |
|---|---|---|
| `xor-points.svg` | Mục XOR không tách tuyến tính | Bốn điểm XOR với hai đoạn nối các điểm cùng lớp giao nhau tại tâm hình vuông; minh họa bao lồi giao nhau |
| `xor-mlp.svg` | Mục MLP ReLU 2–2–1 giải XOR | Sơ đồ mạng 2–2–1 với hai nơ-ron ReLU ẩn và một đầu ra sigmoid; minh họa lan truyền xuôi |

Các SVG khác trong danh sách ưu tiên tại checkpoint A1 không được dùng trong bài; nếu cần SVG mới, phải ghi đặc tả và kiểm tra khả năng tiếp cận trước khi đưa vào kho.
