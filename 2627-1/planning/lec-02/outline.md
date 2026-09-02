# Bài 02: Lan truyền và đồ thị tính toán

## Phạm vi và kết quả học tập

Bài học tuân theo đề cương tại `III.2 → Buổi 2`, phục vụ LLO3–LLO4. Sau buổi học, sinh viên có thể:

- mô tả lan truyền xuôi, hàm mất mát, lan truyền ngược và cập nhật tham số trong MLP;
- tách một biểu thức thành đồ thị tính toán có hướng không chu trình;
- áp dụng quy tắc chuỗi theo dạng gradient thượng nguồn nhân đạo hàm cục bộ;
- cộng gradient từ nhiều nhánh và kiểm tra gradient theo đúng biến;
- suy và kiểm tra kích thước các gradient của ReLU và tầng afin theo lô dữ liệu;
- thực hiện một bước lan truyền xuôi, entropy chéo trung bình, lan truyền ngược và cập nhật trên MLP nhỏ.

Tiên quyết: đạo hàm một biến, quy tắc chuỗi, phép nhân ma trận, MLP, ReLU, softmax và logarit ở mức nhập môn. Jacobian không phải tiên quyết; nó được giới thiệu tại L02-15–16. Bộ tối ưu nâng cao, cực tiểu địa phương, gradient triệt tiêu qua mạng sâu và kỹ thuật tiết kiệm bộ nhớ chi tiết nằm ngoài phạm vi.

## Mạch khái niệm

1. MLP là chuỗi biến đổi; huấn luyện cần gradient theo mọi tham số.
2. Đồ thị tính toán ghi quan hệ phụ thuộc và thứ tự tính.
3. Biểu thức vô hướng được tách thành cổng, chạy xuôi và lưu toán hạng trước khi nêu quy tắc chuỗi.
4. Quy tắc chuỗi trở thành `gradient thượng nguồn × đạo hàm cục bộ`; nhiều nhánh dùng phép cộng gradient.
5. Quy tắc vô hướng mở rộng sang tensor qua tích vector–Jacobian, nhưng triển khai không dựng Jacobian dày đặc.
6. Với quy ước lô theo hàng, phép suy theo chỉ số dẫn đến $G_X=G_ZW^\top$, $G_W=X^\top G_Z$, $G_b=\sum_iG_{Z,i:}$.
7. Một MLP 2–2–3 theo dõi cùng $X,Y,W_1,b_1,W_2,b_2$ qua ReLU, điểm số, log-softmax, entropy chéo và suy $G_Z=(P-Y)/B$ bằng quy tắc chuỗi.
8. Pha huấn luyện tách chế độ mô hình, ghi gradient, đặt gradient về 0 và cập nhật tham số.
9. Trang kết L02-39 thu hồi chuỗi $X\to H\to Z\to J\to$ gradient $\to$ cập nhật cùng ba tiêu chí kiểm được, rồi nối sang Bài 03.
10. Tuyến mở rộng gộp sigmoid thành cổng, khóa ranh giới với Bài 03, nêu đánh đổi bộ nhớ và kiểm tra gradient bằng sai phân hữu hạn.

Mạch đã được rà theo Quill: **nhu cầu gradient → đồ thị phụ thuộc → quy tắc cục bộ → tensor và kích thước → MLP xuyên suốt → cập nhật và trạng thái**. Ký hiệu không đổi giữa ví dụ, công thức và câu hỏi. Không tạo `quill.json`.

## Phân bổ thời lượng

- Tuyến lõi: 40 trang (L02-00–39), 100 phút; L02-39 là trang kết thu hồi toàn bộ mạch.
- Tuyến mở rộng: 4 trang, 20 phút; có thể bỏ toàn bộ sau L02-38, khi đó đi thẳng từ L02-38 sang L02-39.
- Bài tập: 50 phút, tách khỏi thời lượng deck.

## Ánh xạ nguồn

| Cụm | Trang đích | Nguồn chính | Nguồn kiểm chứng hoặc bổ sung |
|---|---|---|---|
| MLP, nhu cầu gradient và đồ thị | L02-00–05 | `lec06_backprop.pdf`, tr. 3–5 | `lec05_multilayer.pdf`, tr. 28–34; giáo trình PDF tr. 31–32, 90–92 |
| Quy tắc chuỗi và cổng vô hướng | L02-06–14 | `lec06_backprop.pdf`, tr. 6–16, 18–35; `lec07_backprop_part2.pdf`, tr. 8–9 | Hai ví dụ số đã tính lại; L02-13 là ví dụ độc lập |
| Vector, Jacobian, ReLU và tầng afin | L02-15–24 | `lec07_backprop_part2.pdf`, tr. 10–29 | Giáo trình PDF tr. 91–93; suy theo chỉ số ở L02-20–23 |
| MLP theo lô hàng xuyên suốt | L02-25–38 | `lec07_backprop_part2.pdf`, tr. 15–29; `lec04_multiclass.pdf`, tr. 12–19 | `lec05_multilayer.pdf`, tr. 28–34; giáo trình PDF tr. 68–73, 94, 96 |
| Kết luận một bước huấn luyện | L02-39 | tổng hợp từ `lec06_backprop.pdf`, tr. 3–5; `lec07_backprop_part2.pdf`, tr. 19–29 | giáo trình PDF tr. 31–32 |
| Mở rộng | L02-X01, L02-X02, L02-X04, L02-X05 | `lec06_backprop.pdf`, tr. 18–31; `lec07_backprop_part2.pdf`, tr. 17 | Giáo trình PDF tr. 94, 96 |

Không dùng hình ResNet/ResNeXt ở `lec06_backprop.pdf` tr. 14, nội dung cực tiểu địa phương hay khảo sát bộ tối ưu. Không dùng nguồn web, mã trình diễn hoặc ảnh raster.

## Bảng thuật ngữ và ký hiệu

| Ký hiệu | Nghĩa và quy ước |
|---|---|
| $B,d,h,k$ | Kích thước lô, số đặc trưng, số đơn vị ẩn, số lớp |
| $X\in\mathbb R^{B\times d}$ | Lô dữ liệu theo hàng; hàng $i$ là một mẫu |
| $A=XW_1+b_1$ | Tiền kích hoạt; $b_1$ phát rộng theo hàng |
| $H=\operatorname{ReLU}(A)$ | Biểu diễn ẩn |
| $Z=HW_2+b_2$ | Logits, chưa phải xác suất |
| $P=\operatorname{softmax}(Z)$ | Xác suất, chuẩn hóa theo trục lớp trong từng hàng |
| $Y\in\{0,1\}^{B\times k}$ | Nhãn nhất vị |
| $\operatorname{LSE}(Z_{i:})$ | Log-sum-exp ổn định trên trục lớp của mẫu $i$ |
| $J$ | Mất mát vô hướng, lấy trung bình theo lô; phân biệt với $J_f$ là Jacobian của một phép biến đổi $f$ |
| $G_U=\partial J/\partial U$ | Gradient của $J$ theo tensor $U$, cùng kích thước với $U$ |
| $\bar u$ | Ký hiệu tương đương cho $\partial J/\partial u$ trong đồ thị vô hướng |
| $\eta$ | Tốc độ học |

## Bài tập 50 phút

1. Dựng đồ thị tính toán, 10 phút.
2. Tính lan truyền ngược bằng tay, 15 phút.
3. Kiểm tra kích thước tensor và gradient qua ReLU/tầng afin, 15 phút.
4. Tìm và sửa lỗi đạo hàm, 10 phút.

Đề bài, cách tổ chức và đáp án chi tiết nằm trong `note-for-author.md`.

## Bản đồ chủ đề của ghi chú bài giảng

| Mã nội bộ | Nhãn | Chủ đề | Phần ghi chú | Trang chiếu liên quan |
|---|---|---|---|---|
| T02-N01 | cốt lõi | Nhu cầu gradient và đồ thị phụ thuộc | Từ MLP đến nhu cầu gradient | L02-02–05 |
| T02-N02 | cốt lõi | Cổng vô hướng, quy tắc chuỗi và cộng gradient | Ví dụ vô hướng; thuật toán lan truyền ngược | L02-06–14 |
| T02-N03 | cầu nối | Từ đạo hàm vô hướng sang tích vector–Jacobian | Từ số vô hướng sang tensor | L02-15–18 |
| T02-N04 | cốt lõi | Lan truyền ngược qua tầng afin theo lô | Tầng afin theo lô | L02-19–24 |
| T02-N05 | cốt lõi | Softmax, log-sum-exp và entropy chéo | Softmax, log-softmax và entropy chéo | L02-25–32 |
| T02-N06 | cốt lõi | MLP 2–2–3 xuyên suốt | Ví dụ MLP 2–2–3 xuyên suốt | L02-25–36 |
| T02-N07 | bổ sung | Trạng thái của một bước huấn luyện | Một bước huấn luyện và trạng thái | L02-37–38 |
| T02-N08 | bổ sung | Bộ nhớ và kiểm tra gradient số | Đi sâu thêm | L02-X04–X05 |
| T02-N09 | đọc thêm | Tài liệu đọc trước cho Buổi 03 | Tài liệu tham khảo | Không đưa lên deck Bài 02 |

Các mã trên chỉ dùng để truy nguyên trong planning. Tài liệu công khai dùng tiêu đề theo nghĩa, không hiển thị mã nội bộ. Bốn SVG được dùng lại từ deck vì chúng khớp trực tiếp các chủ đề T02-N02, T02-N04 và T02-N06; ghi chú không tạo ảnh raster hay tài sản mới.
