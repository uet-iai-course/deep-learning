# Ghi chú cho người soạn — Bài 04

## Tuyến giảng

- Lõi L04-00–L04-38: 100 phút.
- Mở rộng L04-X01–L04-X05: 20 phút; có thể bỏ nguyên cụm.
- Không đưa mã trang, thời lượng, tuyến cắt hoặc đáp án lên slide/notes.
- Các hiệu ứng xuất hiện cần dừng để người học trả lời trước khi hiện: L04-14, L04-22, L04-25 và L04-X04.
- L04-X04 chỉ là cầu nối dấu vết kích thước của một mạng tích chập nhỏ theo cấu hình LeNet trong giáo trình; không dạy lịch sử hoặc kết quả định lượng.

## Ranh giới và quy ước nội bộ

- Chỉ dùng dải nguồn đã duyệt; không dùng `lec08_cnn.pdf`, PDF 31–36.
- Không mở rộng sang độ giãn, tích chập theo nhóm hoặc tích chập riêng từng kênh.
- Phép trên slide là tương quan chéo, không lật nhân; $X$ theo NCHW, $W$ theo OIHW.
- $K$ dành cho ví dụ một kênh; khi chuyển sang nhiều kênh, nối rõ sang lát $W_{o,c,:,:}$.
- Điều kiện “đệm giữ nguyên kích thước” chỉ dùng khi $S_h=S_w=1$; không gắn nhãn tổng quát khác.
- Phép gộp chỉ thường giảm độ phân giải khi cấu hình cửa sổ, bước trượt và đệm làm số vị trí đầu ra ít hơn.

## Đáp án tương tác

- L04-14: cửa sổ mới $[[1,2],[4,5]]$; $K=[[0,1],[2,3]]$ không đổi.
- L04-22: không có hàng đầu ra nếu $H_{in}+P_t+P_b<K_h$; tương tự theo chiều rộng.
- L04-25: $Y_{0,0,:,:}=[[56,72],[104,120]]$; mỗi ô cộng $2·2·2=8$ tích.
- L04-X04: $16·5·5=400$; không gộp kích thước lô vào trục đặc trưng.

## Bài tập 50 phút

### Tương quan chéo — 15 phút

Dùng ví dụ một kênh trên slide nhưng thay nhân bằng $[[1,0],[-1,1]]$. Yêu cầu tính đủ đầu ra. Kiểm tra thứ tự phần tử và không lật nhân.

### Kích thước và tham số — 15 phút

Cho $X:8×16×32×35$, $C_{out}=24$, nhân $3×5$, vùng đệm $(1,1,2,2)$, bước trượt $(2,1)$. Đáp án: $H_{out}=16$, $W_{out}=35$, kích thước $8×24×16×35$, tham số $24(16·3·5+1)=5784$.

### Phép gộp — 10 phút

Dùng ma trận 4×4 của slide, đổi bước trượt thành 1. Yêu cầu kích thước và hai cửa sổ đầu. Nhắc phép gộp tách theo kênh.

### Trường tiếp nhận — 10 phút

Ba tầng: $(K,S)=(3,1),(3,2),(3,1)$. Từ $r_0=j_0=1$: tầng 1 $(r,j)=(3,1)$; tầng 2 $(5,2)$; tầng 3 $(9,2)$.

## Điểm cần kiểm chứng sau chỉnh sửa

- Mọi thay đổi công thức kích thước, ví dụ nhiều kênh, tham số, MAC hoặc trường tiếp nhận phải được rà lại toán học.
- Nếu đổi thứ tự hoặc số trang, rà trang bị ảnh hưởng và hai trang lân cận mỗi phía.
- LeNet chỉ minh họa dấu vết kích thước; không thêm lịch sử hoặc kết quả định lượng.
