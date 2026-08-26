# Ghi chú cho người soạn — Bài 03

## Tuyến giảng

- Tuyến lõi L03-00 đến L03-42: 100 phút.
- Tuyến mở rộng L03-X01 đến L03-X05: 20 phút. Có thể bỏ nguyên phần mà không làm đứt mạch; từ L03-42 kết thúc buổi lõi.
- Khi thiếu thời gian trong tuyến lõi, rút phần tính tay L03-18 xuống việc kiểm tra dấu và hướng, nhưng không bỏ trạng thái RMSprop/Adam hoặc phân biệt huấn luyện/suy luận.
- Cụm điều chuẩn dùng 1 phút ở L03-25, 2 phút ở L03-26 và 3 phút cho mỗi trang L03-29–30; không kéo dài phần mở đầu L2 làm mất thời gian định nghĩa L1.

## Các điểm cần nhấn khi giảng

1. Đường cong học chỉ tạo giả thuyết. Xác nhận bằng phép kiểm tra nhỏ: dữ liệu, gradient, cập nhật, xáo trộn và chế độ mô hình.
2. Tách ba lỗi: số học ở phép toán; gradient qua chuỗi tầng; tổng quát hóa trên dữ liệu chưa thấy.
3. Trạng thái của bộ tối ưu có cùng kích thước với tham số và phải được lưu qua các bước.
4. So sánh bộ tối ưu phải giữ cùng mô hình, dữ liệu, tiền xử lý, ngân sách cập nhật và quy tắc chọn điểm lưu.
5. Với BN cho MLP lô theo hàng, rút gọn trục $B$ và kiểm tra phát rộng trên $D$. So sánh BN/LN chỉ nằm ở X04.
6. Với L1, phân biệt đạo hàm dưới tại 0 với đạo hàm thông thường; chỉ kết luận L1 khuyến khích tham số thưa.
7. Với L2, chỉ gọi $(1-\eta\lambda)w$ là thành phần co khi $0\le\eta\lambda\le1$; ví dụ số có $\eta\lambda=.005$.

## Bài tập 50 phút và đáp án

### 1. Chẩn đoán đường cong học — 15 phút

Cho bốn đường cong: mất mát không đổi; mất mát thành NaN sau 300 bước; huấn luyện giảm nhưng xác thực tăng; mất mát dao động theo chu kỳ. Yêu cầu nhóm nêu hai giả thuyết và một phép kiểm tra cho mỗi trường hợp.

Đáp án định hướng:

- Không đổi: tham số không cập nhật, gradient bằng 0 hoặc tốc độ học quá nhỏ; kiểm tra norm gradient và độ chênh tham số sau một bước.
- NaN: mũ/log/chia không ổn định hoặc gradient bùng nổ; kiểm tra giá trị hữu hạn theo từng tầng và dùng công thức log-sum-exp.
- Khoảng cách tăng: quá khớp hoặc tiền xử lý lệch; kiểm tra quy trình xác thực, sau đó thử điều chuẩn/tăng cường dữ liệu.
- Chu kỳ: dữ liệu không xáo trộn hoặc lịch tốc độ học; kiểm tra thứ tự lô và vẽ theo vòng huấn luyện.

### 2. So sánh cập nhật — 15 phút

Dùng ví dụ Mômen trong review-log. Yêu cầu tính hai bước SGD và Mômen, sau đó chỉ ra tọa độ nào được làm trơn. Với RMSprop và Adam, yêu cầu tính từ trạng thái 0 theo đúng ví dụ trên slide.

### 3. Huấn luyện/suy luận — 10 phút

Cho $X\in\mathbb R^{4\times3}$ và dropout $p=.25$. Hỏi nguồn ngẫu nhiên và thống kê nào được dùng khi huấn luyện/suy luận. Đáp án: dropout lấy mặt nạ mới khi huấn luyện, đồng nhất khi suy luận; BN dùng thống kê lô khi huấn luyện và thống kê cố định ước lượng từ huấn luyện khi suy luận; $\gamma,\beta$ dùng ở cả hai.

### 4. Chọn điều chuẩn — 10 phút

Tình huống: mất mát huấn luyện thấp, mất mát xác thực cao, tập ảnh nhỏ và có phép lật giữ nhãn. Nhóm đề xuất tối đa hai thay đổi và giao thức so sánh. Đáp án hợp lệ: tăng cường dữ liệu đã kiểm tra giữ nhãn và L2/dropout; mỗi lần chỉ đổi một nhóm yếu tố, chọn bằng xác thực, đánh giá kiểm tra một lần sau khi khóa cấu hình.

## Giới hạn và đáp án cụm L1

- L03-29: với $w=(2,-.5,0)$ và $\lambda=.1$, đóng góp đạo hàm dưới của hạng phạt là $(.1,-.1,.1s)$, $s\in[-1,1]$; tại tọa độ 0, khoảng đáp án là $[-.1,.1]$.
- L03-30: giả thiết bắt buộc là xấp xỉ bậc hai cục bộ quanh $w^*$, Hessian chéo và $H_{ii}>0$. $H_{ii}=\partial^2L_{data}/\partial w_i^2$ là độ cong theo tọa độ; Hessian chéo làm xấp xỉ tách theo từng tọa độ. Tọa độ về 0 khi $|w_i^*|\le\lambda/H_{ii}$. Với $\lambda=.2,H_{ii}=.5$, ngưỡng $.4$ cho $.3\mapsto0$ và $-.9\mapsto-.5$.
- Nguồn dùng $\alpha$; deck dùng $\lambda$ để thống nhất với cụm L2. Không đổi ý nghĩa hệ số khi chuyển ký hiệu.
- Nguồn phân tích hồi quy tuyến tính không bias; deck thay tên mục tiêu dữ liệu bằng $L_{data}$ để minh họa cục bộ. Không trình bày công thức ngưỡng mềm như nghiệm tổng quát của mạng sâu. Không mở API, code, Bayes/Laplace hoặc thuật toán proximal.

## Điểm cần kiểm chứng sau chỉnh sửa

- Mọi thay đổi công thức Momentum, RMSprop, Adam, L2, L1, dropout hoặc BN phải được tác tử độ chính xác rà lại.
- Nếu thay số slide hoặc thứ tự, rà lại trang bị ảnh hưởng và hai trang lân cận mỗi phía.
- Không đưa nội dung của tệp này lên mặt slide hoặc ghi chú diễn giả.
