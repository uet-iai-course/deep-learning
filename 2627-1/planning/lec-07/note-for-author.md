# Ghi chú dành cho người soạn — Bài 07

## Tuyến và điều hướng

- Tuyến lõi: L07-00 đến L07-38, 98 phút; L07-39 thuộc tuyến lõi với 2 phút, tổng 100 phút. Theo quy ước trình bày, đi xuống trong cụm và nhấn phải ở cuối cụm.
- Từ L07-38: tuyến lõi phải dùng End tới L07-39; không dùng Phải vì Phải sẽ vào L07-X01. Tuyến đầy đủ dùng Phải vào L07-X01, đi Xuống qua X02–X04 rồi Xuống tới L07-39. Chờ 60 giây ở L07-38.
- HTML gắn riêng phím Phải tại sáu ranh giới L07-06→07, L07-13→14, L07-21→22, L07-29→30, L07-34→35 và L07-38→X01. RevealJS mặc định giữ chỉ số dọc khi sang mạch kế, nên binding lấy đúng chỉ số ngang–dọc của trang đích; ở mọi trang khác, nó gọi `Reveal.right()`. Phím End có binding riêng tới L07-39 cho toàn bộ bài, tránh rơi vào X01 trong phiên mới chưa có chỉ số dọc đã nhớ.
- Ranh giới bảy mạch: dùng Phải ở năm điểm đầu để sang mạch kế; tại L07-38 dùng End cho tuyến lõi hoặc Phải cho tuyến đầy đủ. Mạch 7 đi Xuống từ X01 đến X04 rồi tới L07-39.
- Có thể cắt toàn bộ X01–X04; khi cắt, L07-39 vẫn được giữ bằng phím End từ L07-38. Nếu cần rút thêm 5 phút, gộp L07-35 và L07-37 khi nói.
- Bài tập 50 phút tách khỏi 120 phút deck.

## Điểm chờ và đáp án

| Trang | Chờ | Đáp án |
|---|---:|---|
| L07-06 | 45 giây | $X_7$ có kích thước $32\times64$; chọn trục thời gian. |
| L07-13 | 45 giây | Chỉ một $W_h$; bốn bước dùng chung cùng ma trận. |
| L07-17 | 45 giây | Cảm xúc: nhiều–sang–một; từ loại: nhiều–sang–nhiều căn chỉnh. |
| L07-21 | 45 giây | Toàn bộ $h_1,h_2,h_3,o_3,L$ có thể đổi. |
| L07-29 | 45 giây | $W_h$ dùng ở mọi bước nên gradient là tổng các lần dùng. |
| L07-34 | 45 giây | $0.8^{20}\approx0.0115$. |
| L07-38 | 60 giây | $h_3$ vẫn đi tới bước 4; gradient từ bước 6 không qua ranh giới về bước 2. |
| L07-X04 | 45 giây | Không dùng được trực tuyến nếu tương lai chưa có; tăng số tầng không thay điều kiện nhân quả này. |

Đáp án và thời lượng chờ giữ nguyên sau khi đổi cấu trúc; L07-39 vẫn thuộc tuyến lõi với 2 phút dù đứng sau X04.

## Bài tập 50 phút

1. **Trải mạng và kích thước — 15 phút.** Cho $N=16,T=4,D_x=5,D_h=7,D_y=3$. Vẽ mạng bốn bước; ghi kích thước $X_t,H_t,O_t,W_x,W_h,W_y,H_0$. Đáp án lần lượt: $16\times5$, $16\times7$, $16\times3$, $5\times7$, $7\times7$, $7\times3$, $16\times7$.
2. **BPTT bằng tay — 20 phút.** Dùng ví dụ vô hướng ba bước; tính $h_t,o_3,L$, ba $\delta_t$ và gradient của $w_x,w_h,w_y$. Dùng bảng số trong review-log để chấm; cho phép sai khác do làm tròn ở chữ số thứ tư.
3. **Phân tích gradient — 10 phút.** So sánh $0.8^{20}$ và $1.2^{20}$. Đáp án: khoảng $0.0115$ và $38.3376$; giải thích đây là ví dụ vô hướng, không phải điều kiện đầy đủ cho ma trận RNN có tanh.
4. **Phân loại dạng ánh xạ — 5 phút.** Phân loại cảm xúc, chú thích ảnh, gán nhãn từ loại và dịch máy. Đáp án: nhiều–sang–một, một–sang–nhiều, nhiều–sang–nhiều căn chỉnh, nhiều–sang–nhiều không căn chỉnh.

## Lưu ý toán học

- Dùng quy ước mỗi mẫu là một hàng từ đầu đến cuối; không đổi sang công thức cột khi nói BPTT.
- Trên L07-16, softmax tính theo trục $D_y$. Entropy chéo từ logit dùng $-O_{t,Y_t}+\operatorname{logsumexp}(O_t)$ theo trục này hoặc hàm nhận trực tiếp logit; không tính softmax rồi lấy log thủ công. Mất mát bình phương chỉ dành cho đích liên tục trong ví dụ nêu trên trang.
- Trên L07-23–24, nối rõ $\bar o_3\to\delta_3\to\delta_2\to\delta_1$ và nhấn mạnh $\delta_t=G_t$ trong trường hợp vô hướng. Trên L07-25, $G_{t+1}W_h^\top$ là gradient từ tương lai; $\bar O_tW_y^\top$ là gradient trực tiếp từ đầu ra hiện tại.
- Vòng BPTT phải đi đúng $t=T,T-1,\ldots,1$ với $G_{T+1}=0$; độ lệch cộng theo cả mẫu và thời gian như L07-26.
- Trên L07-28, nhánh trực tiếp giữ $h_2$ cố định. Đạo hàm toàn phần dùng $D_t=(1-h_t^2)(h_{t-1}+w_hD_{t-1})$.
- Trên L07-30, $h_t,dh_t,\bar h_t$ đều là hàng $1\times D_h$; $\bar h_t$ là một hàng của $\bar H_t$. Vi phân xuôi nhân $J_t$, gradient ngược nhân $J_t^\top$. L07-31 là trường hợp $D_h=1$, với $J_t=w_h(1-h_t^2)$.
- Không nói trị kỳ dị lớn nhất của $W_h$ đơn độc quyết định triệt tiêu/bùng nổ; các đạo hàm tanh thay đổi theo trạng thái.
- BPTT cắt ngắn không bỏ trạng thái xuôi; nó chỉ ngắt đường đạo hàm.

## Giới hạn nội dung

- Không mở công thức LSTM/GRU; L07-39 chỉ đặt câu hỏi thiết kế cho Bài 08.
- Không thêm teacher forcing, padding, masking, bucketing, clipping, code hoặc huấn luyện thực nghiệm. Các công thức chỉ giả sử lô đang xét gồm các chuỗi hoặc đoạn đã chọn cùng $T$; không trình bày cắt đoạn như cách ghép lô tổng quát, nhất là với nhãn toàn chuỗi.
- Không dùng trang nguồn ngoài các dải được `source.md` khóa.
- Mã `LLO3` là bản chép đúng đề cương dù trùng Buổi 02; không “sửa” trên mặt slide hoặc planning.

## Kiểm kê SVG

Tất cả SVG trong `img/lec-07/` phải được HTML tham chiếu. Không để tài sản nháp không dùng và không thêm raster.
