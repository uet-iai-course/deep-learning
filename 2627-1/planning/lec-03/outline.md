# Bài 03 — Tối ưu hóa mạng nơ-ron đa lớp

## Phạm vi và mục tiêu

- Đối tượng: sinh viên đại học đã học đại số tuyến tính, giải tích, xác suất, Python, học máy nhập môn và hai bài đầu của học phần.
- Phạm vi đề cương: LLO5–LLO6; mất ổn định số, gradient triệt tiêu hoặc bùng nổ, quá khớp, bộ tối ưu, khởi tạo, điều chuẩn, dropout, chuẩn hóa theo lô và tinh chỉnh siêu tham số.
- Tuyến trình chiếu: 100 phút lõi và 20 phút mở rộng/có thể cắt.
- Bài tập: 50 phút riêng, không tính vào thời lượng trình chiếu.
- Sản phẩm học tập: chẩn đoán đường cong học; tính đầy đủ trạng thái và một bước Mômen, RMSprop, Adam và L2; tính đạo hàm dưới và ngưỡng mềm L1 trong giả thiết đã nêu; chọn khởi tạo có điều kiện; phân biệt huấn luyện/suy luận của dropout và chuẩn hóa theo lô; thiết kế hai vòng chọn siêu tham số bằng tập xác thực.

## Nguồn đã chọn

1. Chuẩn phạm vi: `source-materials/resources/UET_Đề cương học phần_UET.AI3056_Học sâu_7460108.01.24.2506.docx`, III.2 → Buổi 3.
2. Nguồn chính: `source-materials/slides/lec10_training.pdf`, PDF 3–9, 11–17, 19–33, 35–41.
3. Nguồn phụ: `lec05_multilayer.pdf`, PDF 37–47; `lec02_linear_part1.pdf`, PDF 55–68; `lec03_linear_part2.pdf`, PDF 2–15; `lec04_multiclass.pdf`, PDF 19.
4. Giáo trình kiểm chứng: `source-materials/textbooks/hocsau_draft.pdf`, PDF 58–66, 96–105, 153–158.
5. Nguồn bổ sung đã duyệt cho L1: Goodfellow, Bengio và Courville, *Deep Learning*, §7.1.2, trang in 230–232, (7.18)–(7.23), `https://www.deeplearningbook.org/contents/regularization.html`.
6. Không dùng `lec10_training.pdf`, PDF 43–47 vì vượt phạm vi; không dùng PDF 29 và 47 làm bằng chứng định lượng.

## Hành trình khái niệm

1. Đọc dấu hiệu từ đường cong huấn luyện và xác thực.
2. Tách lỗi triển khai, vấn đề tối ưu và vấn đề tổng quát hóa.
3. Kiểm soát bước cập nhật bằng tốc độ học và lịch tốc độ học.
4. Theo dõi thang kích hoạt và gradient; chọn khởi tạo phù hợp.
5. So sánh SGD, Momentum, RMSprop và Adam bằng cùng giao thức.
6. Kiểm soát khoảng cách huấn luyện–xác thực bằng L2, L1 và dropout.
7. Chuẩn hóa theo lô đúng trục, đúng shape và đúng chế độ mô hình.
8. Chọn siêu tham số chỉ bằng tập xác thực; khóa cấu hình trước khi đánh giá trên tập kiểm tra.

## Ánh xạ nguồn sang cụm đích

| Cụm đích | Nguồn | Quyết định |
|---|---|---|
| Đường cong học | `lec10_training.pdf`, PDF 4–7, 9 | Giữ mạch; vẽ lại các dạng đường cong bằng SVG, không sao chép ảnh |
| SGD và tốc độ học | `lec10_training.pdf`, PDF 3, 8 | Giữ; Việt hóa và thống nhất ký hiệu $g_t,\eta_t$ |
| Ổn định số và gradient | `lec04_multiclass.pdf`, PDF 19; GT PDF 96–100 | Nối log-sum-exp với chuỗi Jacobian; không dùng GT 58–63 cho L03-10 |
| Khởi tạo | `lec10_training.pdf`, PDF 23–24; `lec05_multilayer.pdf`, PDF 37–47; GT PDF 96–102 | Tách vấn đề đối xứng và bảo toàn phương sai |
| Bộ tối ưu | `lec10_training.pdf`, PDF 11–17 | Giữ thứ tự; sửa nhãn PDF 14 thành RMSprop; viết Adam đủ hiệu chỉnh mômen |
| Điều chuẩn | `lec10_training.pdf`, PDF 35–41; GT PDF 64–66, 103–105; Goodfellow et al. §7.1.2, trang in 230–232, (7.18)–(7.23) | Giữ L2 và dropout; thêm L1 với định nghĩa cục bộ của đạo hàm dưới và nghiệm ngưỡng mềm. Nguồn phân tích hồi quy tuyến tính không bias; deck chỉ dùng $L_{data}$ như minh họa xấp xỉ cục bộ, không suy rộng. Sửa dropout sang quy ước đảo tỷ lệ |
| Chuẩn hóa theo lô | `lec10_training.pdf`, PDF 25–28, 30–33; GT PDF 153–158 | Làm rõ shape; thêm ví dụ số MLP; suy luận dùng thống kê cố định ước lượng từ huấn luyện, không khóa EMA |
| Chọn siêu tham số | `lec05_multilayer.pdf`, PDF 42–46; GT PDF 62 | Hai vòng huấn luyện–lựa chọn; khóa ngân sách, tiêu chí và cấu hình trước tập kiểm tra |
| Mở rộng | `lec10_training.pdf`, PDF 19–22, 33; `lec05_multilayer.pdf`, PDF 42–46; GT PDF 155–157 | Có thể cắt; tăng cường dữ liệu, tiền xử lý, kiểm kê cấu hình, BN/LN và giới hạn so sánh |

## Thuật ngữ và ký hiệu

| Ký hiệu/thuật ngữ | Nghĩa và quy ước |
|---|---|
| $B$ | Kích thước lô nhỏ; trục đầu của tensor MLP |
| $D$ | Số đặc trưng hoặc số đơn vị của một tầng |
| $w_t$ | Vector tham số tại bước $t$ |
| $g_t=\nabla_w L_{\mathcal B_t}(w_{t-1})$ | Gradient trung bình trên lô nhỏ ở bước $t$ |
| $\eta_t$ | Tốc độ học; có thể thay đổi theo bước hoặc vòng huấn luyện |
| $K,T,t$ | Chu kỳ giảm, tổng số bước của lịch và chỉ số bước; $K,T>0$, $0\le t\le T$ |
| $u_t$ | Vận tốc của Mômen, cùng kích thước với $w_t$ |
| $s_t$ | Trung bình trượt của $g_t\odot g_t$ trong RMSprop |
| $m_t,v_t$ | Mômen bậc một và bậc hai trong Adam |
| $\hat m_t,\hat v_t$ | Mômen đã hiệu chỉnh độ chệch |
| $\lambda$ | Hệ số điều chuẩn L2 hoặc L1 theo công thức đang xét; nguồn L1 dùng $\alpha$, deck đổi sang $\lambda$ để thống nhất |
| $w^*$ | Điểm cực tiểu của mất mát dữ liệu trong xấp xỉ bậc hai cục bộ dùng cho L1 |
| $H_{ii}$ | Phần tử đường chéo dương của Hessian trong xấp xỉ L1; ngưỡng là $\lambda/H_{ii}$ |
| $p$ | Xác suất bỏ một đơn vị trong dropout; xác suất giữ là $1-p$ |
| $X\in\mathbb R^{B\times D}$ | Kích hoạt MLP, hàng là mẫu, cột là đặc trưng |
| $\mu_{\mathcal B},\sigma^2_{\mathcal B}\in\mathbb R^D$ | Trung bình và phương sai theo trục lô |
| $\gamma,\beta\in\mathbb R^D$ | Tham số tỷ lệ và dịch của chuẩn hóa theo lô |
| $\theta,c,\mathcal C,N$ | Tham số mô hình, một cấu hình siêu tham số, tập cấu hình thử và ngân sách |
| huấn luyện / xác thực / kiểm tra | Ba vai trò dữ liệu không hoán đổi |

## Ranh giới đã khóa

- Không tạo code demo.
- Không đưa số liệu đối sánh hoặc kết luận một bộ tối ưu luôn tốt hơn.
- L1 dùng đúng nguồn Goodfellow et al. §7.1.2 đã duyệt. Nghiệm ngưỡng mềm chỉ áp dụng cho xấp xỉ bậc hai cục bộ với Hessian chéo $H_{ii}>0$; không suy rộng thành nghiệm đóng cho mọi mạng sâu.
- Diễn giải $(1-\eta\lambda)w$ là co trọng số chỉ khi $0\le\eta\lambda\le1$; bước SGD đầy đủ còn có $-\eta g_{data}$.
- Không mở API, code, diễn giải Bayes/Laplace hoặc thuật toán proximal trong cụm L1.
- Các chỉ dẫn cắt, đáp án chi tiết và trạng thái kiểm chứng chỉ nằm trong `note-for-author.md`.
