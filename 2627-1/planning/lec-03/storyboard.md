# Storyboard Bài 03

## Bản đồ hành trình

Đường cong học → chẩn đoán → SGD/tốc độ học → ổn định số và gradient → khởi tạo → bộ tối ưu → tổng quát hóa → L2/L1/dropout → chuẩn hóa theo lô → chọn siêu tham số → kết luận và khóa tập kiểm tra.

Ví dụ xuyên suốt truyền các đại lượng sau: $w_t,g_t,\eta_t$ từ SGD sang Mômen/RMSprop/Adam; $X\in\mathbb R^{B\times D}$ từ kích hoạt sang chuẩn hóa theo lô; mất mát huấn luyện và xác thực từ chẩn đoán sang chọn siêu tham số. Chu trình học tập của mỗi cụm được ghi trong bảng dưới.

## Tuyến lõi — 100 phút

| Mã | Phút | Bước | Luận điểm, đầu vào → sản phẩm | Nguồn |
|---|---:|---|---|---|
| L03-00 | 1 | Vấn đề | Huấn luyện có thể thất bại dù công thức lan truyền ngược đúng → ba nhóm quyết định | Đề cương, Buổi 3 |
| L03-01 | 1 | Kiểm tra | Tiên quyết Bài 02 → mục tiêu quan sát được | Đề cương; `source.md` |
| L03-02 | 3 | Trực giác | Mất mát theo thời gian → đọc tín hiệu thay vì nhìn một số cuối | lec10:4–7 |
| L03-03 | 3 | Ví dụ | Bốn dạng lỗi rõ → giả thuyết kiểm tra đầu tiên | lec10:6 |
| L03-04 | 3 | Ví dụ | Chậm hội tụ và quá khớp → tách tối ưu với tổng quát hóa | lec10:7 |
| L03-05 | 3 | Kiểm tra | Đường cong → thứ tự chẩn đoán có thể kiểm chứng | lec10:6–7 |
| L03-06 | 3 | Vấn đề + trực giác + hình thức | Hướng nhất quán/đổi dấu → gradient lô nhỏ và cập nhật SGD | lec10:3 |
| L03-07 | 2 | Trực giác | $\eta$ quá lớn/quá nhỏ → ba chế độ đường cong | lec10:4–5 |
| L03-08 | 2 | Triển khai + kiểm tra | $K,T\in\mathbb N_{>0}$, $t\in\{0,\ldots,T\}$ → lịch là một phần cấu hình | lec10:8 |
| L03-09 | 3 | Vấn đề | Mũ, tích Jacobian, thang kích hoạt → ba nguồn bất ổn | GT:96–100; lec10:23–24 |
| L03-10 | 3 | Trực giác + tính toán + kiểm tra | $z=(1000,999)$ → trừ cực đại, log-sum-exp ổn định trên trục lớp | lec04:19 |
| L03-11 | 3 | Hình thức | Chuỗi Jacobian → gradient triệt tiêu/bùng nổ | GT:96–100 |
| L03-12 | 3 | Ví dụ | Đường vào và đường ra cùng đối xứng → kích hoạt và tín hiệu ngược bằng nhau | lec10:23; GT:100 |
| L03-13 | 3 | Triển khai | $n_{in},n_{out}$ và kích hoạt → Xavier/Kaiming | lec10:24; GT:98–100 |
| L03-14 | 1 | Kiểm tra | Tầng $256\to128$ → tính phương sai khởi tạo | lec10:24 |
| L03-15 | 2 | Vấn đề | Độ cong khác nhau → SGD dao động ở hướng dốc | lec10:11–12 |
| L03-16 | 2 | Ví dụ | Gradient tức thời → đường đi răng cưa | lec10:12 |
| L03-17 | 3 | Hình thức | $g_t,u_{t-1}$ → vận tốc Mômen | lec10:13 |
| L03-18 | 3 | Tính toán | Hai gradient → $u_1,w_1,u_2,w_2$ | lec10:13; tính lại |
| L03-19 | 3 | Hình thức | Lịch sử bình phương gradient → RMSprop | lec10:14 |
| L03-20 | 2 | Tính toán | $s_0=0,w_0,g_1$ → $s_1$ và bước RMSprop đầy đủ | lec10:14; tính lại |
| L03-21 | 3 | Hình thức | Mômen bậc một và hai → cập nhật Adam | lec10:15 |
| L03-22 | 2 | Tính toán | $t=1,m_0=v_0=0$ → $m_1,v_1,\hat m_1,\hat v_1,w_1$ | lec10:15; tính lại |
| L03-23 | 1 | So sánh + kiểm tra | Trạng thái $0/P/P/2P$, cơ chế và điểm cần thử → không xếp hạng phổ quát | lec10:11–17 |
| L03-24 | 2 | Vấn đề | Mất mát huấn luyện giảm, xác thực tăng → quá khớp | lec10:35–36 |
| L03-25 | 1 | Trực giác + hình thức | Trọng số lớn trả thêm chi phí → $\mathcal W$ chịu L2; dropout là nhiễu | lec10:35–41; GT:64–66,103–105 |
| L03-26 | 2 | Tính toán | L2 + SGD → hệ số co khi $0\le\eta\lambda\le1$ và bước theo gradient dữ liệu | lec10:37; GT:64–66 |
| L03-27 | 1 | Ví dụ | $w,g,\eta,\lambda$ → cập nhật số | lec10:37; tính lại |
| L03-28 | 1 | Triển khai | SGD-L2 và suy giảm trọng số tách rời → không đồng nhất với mọi bộ tối ưu | lec10:37 |
| L03-29 | 3 | Ví dụ + trực giác → hình thức + kiểm tra | $w=(2,-.5,0)$ và lực theo dấu → mục tiêu L1, đạo hàm dưới; tại 0 nhận một khoảng | Goodfellow et al. §7.1.2: (7.18)–(7.20) |
| L03-30 | 3 | Ví dụ + vấn đề → hình thức + kiểm tra | Hai tọa độ và ngưỡng $0.4$ → độ cong $H_{ii}$, xấp xỉ tách và điều kiện về 0 | Goodfellow et al. §7.1.2: (7.21)–(7.23); tính lại |
| L03-31 | 1 | Trực giác | Phụ thuộc đồng thích nghi → che ngẫu nhiên đơn vị | lec10:39–40; GT:103–105 |
| L03-32 | 3 | Hình thức | $0\le p<1$; kỳ vọng ở huấn luyện và ánh xạ đồng nhất khi suy luận | GT:103–105 |
| L03-33 | 2 | Tính toán | $h=(2,-1,4)$, $p=0.5$ → $(4,0,8)$ | GT:103–105; tính lại |
| L03-34 | 1 | Kiểm tra | Chế độ mô hình → xác định hành vi dropout | lec10:39–41; GT:105 |
| L03-35 | 2 | Vấn đề | Kích hoạt trôi thang → chuẩn hóa trong từng lô | lec10:25–26; GT:153–154 |
| L03-36 | 3 | Hình thức | $X:B\times D$ → $\mu,\sigma^2,\hat X,Y$ đúng kích thước | GT:153–155 |
| L03-37 | 3 | Ví dụ/tính toán | $X:2\times2$, tính tay $\varepsilon=0$ → $\mu,\sigma^2,\hat X,Y$; triển khai $\varepsilon>0$ | GT:153–155; tính lại |
| L03-38 | 2 | Triển khai | Afin → BN → kích hoạt; $\gamma,\beta$ học được | lec10:27,31–32; GT:155 |
| L03-39 | 3 | Hình thức | Huấn luyện dùng thống kê lô; suy luận dùng thống kê cố định ước lượng từ huấn luyện | lec10:28; GT:156–157 |
| L03-40 | 2 | Kiểm tra | Dùng lại $X:2\times2$ ở L03-37 → phát hiện rút gọn sai trục | lec10:30,33; GT:155–158 |
| L03-41 | 3 | Trực giác + hình thức + triển khai | Thẻ hai vòng → $\theta^*(c)$ và $c^*=\arg\min_{c\in\mathcal C}L_{val}$ | lec05:42–46; GT:62 |
| L03-42 | 2 | Kiểm tra | Khóa ngân sách, tiêu chí, cấu hình trước khi mở tập kiểm tra | lec05:42–46; GT:62 |

Tổng tuyến lõi L03-00–42 trước kết luận: **98 phút**.

### Kết luận lõi — 2 phút

| Mã | Phút | Bước | Luận điểm | Nguồn |
|---|---:|---|---|---|
| L03-X05 | 2 | Kiểm tra | Kết luận toàn bài: chẩn đoán → chọn cơ chế → so sánh bằng xác thực và khóa tập kiểm tra | lec10:16–17; lec05:42–46; GT:62 |

Tổng tuyến lõi gồm L03-00–42 và L03-X05: **100 phút**. Mã X05 được giữ ổn định dù trang đã chuyển vào tuyến lõi.

## Tuyến mở rộng/có thể cắt — 20 phút

| Mã | Phút | Bước | Luận điểm | Nguồn |
|---|---:|---|---|---|
| L03-X01 | 5 | Triển khai | Tăng cường dữ liệu chỉ dùng biến đổi giữ nhãn | lec10:19–21 |
| L03-X02 | 5 | Triển khai | Tiền xử lý dùng thống kê huấn luyện cho xác thực/kiểm tra | lec10:22 |
| L03-X03 | 5 | Triển khai | Kiểm kê nhóm siêu tham số và ghi lại mỗi cấu hình $c\in\mathcal C$ | lec05:42–46; lec10:23–24,39–41 |
| L03-X04 | 5 | Hình thức | So sánh trục của BN và LN trên tensor $B\times D$ | lec10:33; GT:155–157 |

Tổng tuyến mở rộng: **20 phút** (X01–X04 mỗi trang 5 phút). Điều hướng tuyến lõi: tại L03-42 bấm **End** để tới trang cuối L03-X05, bỏ qua X01–X04. Điều hướng tuyến đầy đủ: từ L03-42 nhấn phải tới L03-X01, nhấn xuống qua L03-X02, L03-X03 và L03-X04, rồi nhấn phải tới L03-X05. Bỏ toàn bộ phần mở rộng để giữ tuyến 100 phút.

## Chu trình học tập theo cụm

| Cụm | Vấn đề | Trực giác/ví dụ | Hình thức/tính toán | Triển khai | Kiểm tra |
|---|---|---|---|---|---|
| Chẩn đoán | 00 | 02 | không áp dụng: cụm đọc tín hiệu | 03–05 | 05 |
| SGD và tốc độ học | 06 | 06–07 | 06,08 | 08 | Gộp trực giác hướng nhiễu vào 06; câu hỏi 08 nối lịch với cấu hình rồi sang bất ổn ở 09 |
| Ổn định và khởi tạo | 09 | 10,12 | 10–11,13 | 13 | 10,14; L03-10 gộp ví dụ logit với công thức và câu kiểm tra để tránh hình thức đứng trước ví dụ |
| Bộ tối ưu | 15 | 16,18 | 17–22 | 23 | 20,23; 14→15 nối khởi tạo với đường đi cập nhật, 23→24 nối tối ưu với tổng quát hóa |
| Điều chuẩn | 24 | 25,27,29–31; L03-29–30 đặt ví dụ trước công thức ngay trên mặt trang | 25–30,32–33 | 28,34 | 27,29–30,34 |
| Chuẩn hóa theo lô | 35 | 35,37 | 36–39 | 37–39 | 40 dùng lại tensor L03-37; 34→35 nối nhiễu dropout với thống kê kích hoạt |
| Siêu tham số | 41 | 41 | 41 | 41–42, X03 | 42; L03-41 gộp vấn đề + trực giác + hình thức + triển khai, 40→41 nối vòng huấn luyện đúng với vòng ngoài chọn cấu hình |
| Kết luận (X05) | — | — | — | — | X05 chốt ba bước chẩn đoán → chọn cơ chế → so sánh bằng xác thực và khóa tập kiểm tra; nối từ 42 hoặc từ X04 |

Các bước được gộp đều có lý do: L03-06 đặt tình huống trước rồi gộp trực giác với công thức vì cùng dùng $g_t$; L03-25 gộp trực giác “trọng số lớn trả thêm chi phí” với hạng phạt L2; L03-29 đặt vectơ và lực theo dấu trước định nghĩa tổng quát; L03-30 đặt hai tọa độ cùng ngưỡng trước độ cong, giả thiết Hessian chéo và nghiệm ngưỡng mềm; L03-35 nêu vấn đề thang kích hoạt, L03-37 gộp ví dụ và tính toán, L03-40 dùng lại tensor để kiểm tra trục; L03-41 đặt thẻ hai vòng trước công thức rồi gộp hình thức với triển khai vì ký hiệu đặc tả trực tiếp quy trình. Dấu vết: $w_0,g_1,\eta$ dùng lại ở L03-18,20,22; $\lambda$ nối L2 ở L03-25–28 với L1 ở L03-29–30; $X:B\times D$ đi từ L03-36 qua ví dụ L03-37 đến kiểm tra L03-40.

## Bài tập 50 phút riêng

1. Chẩn đoán đường cong học: 15 phút.
2. So sánh cập nhật của các bộ tối ưu: 15 phút.
3. Phân biệt huấn luyện/suy luận với chuẩn hóa theo lô và dropout: 10 phút.
4. Chọn điều chuẩn cho một tình huống: 10 phút.

Đề bài, đáp án và cách tổ chức nằm trong `note-for-author.md`, không xuất hiện trong timing 120 phút của deck.

## Hợp đồng ngữ nghĩa ghi chú ↔ deck

- Ghi chú là bản tự học đầy đủ; deck là tuyến trình chiếu 100 phút lõi cộng 20 phút mở rộng. Hai sản phẩm dùng cùng ký hiệu, ví dụ số, kết luận và nguồn.
- Mỗi chủ đề `note-l03-t01`–`note-l03-t15` trong `outline.md` ánh xạ tới một dải `data-slide-id`; không buộc mỗi đề mục ghi chú tương ứng một trang.
- Các phép tính Mômen, RMSprop, Adam, L2, L1, dropout và chuẩn hóa theo lô phải giữ nguyên dữ kiện và kết quả giữa hai sản phẩm.
- Ghi chú có thể diễn giải dài hơn, nhưng không được thêm kết luận, nguồn hoặc chủ đề vượt phạm vi deck đã khóa. Nội dung mở rộng của ghi chú tương ứng đúng L03-X01–X04.
- Mọi hướng dẫn cắt tuyến, điều hướng, đáp án chi tiết và quyết định kiểm chứng chỉ ở `note-for-author.md`; chúng không xuất hiện trong ghi chú công khai hoặc ghi chú diễn giả.
