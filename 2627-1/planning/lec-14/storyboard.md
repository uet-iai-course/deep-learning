# Storyboard Bài 14

## Chu trình và tuyến dữ liệu

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/tính | Triển khai/ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|
| Episode | L14-02–03 | L14-03–04 | L14-02,08 | L14-05–06,09 | L14-07 | L14-10 |
| Siamese | L14-11 | L14-12 | L14-11 | L14-13 | L14-14 | L14-15 |
| ProtoNet | L14-16 | L14-17–18 | L14-19,21,23 | L14-18,20,22–23 | L14-24 | L14-25 |
| MAML | L14-26–27 | L14-27–28 | L14-28–31 | L14-30,32,35–36 | L14-33–34,37 | L14-38 |
| So sánh | L14-39 | L14-39 | G xuyên ba họ | L14-39–40 | L14-40 | L14-41 |

G được khóa ở L14-08 và truyền sang cặp Siamese, prototype/khoảng cách/NLL, rồi bộ phân loại MAML. I chỉ xuất hiện tại X03 như vi-trace exact/FO/HVP, không phải bài toán so sánh chính.

## Từng trang lõi

Mỗi hàng ghi sáu vai trò theo thứ tự `vấn đề; trực giác; ví dụ; hình thức/tính; triển khai/ứng dụng; kiểm tra`. `N/A` có lý do vì một trang chỉ làm một bước trung tâm; các bước còn lại do trang trong cùng cụm đảm nhiệm.

| ID | Phút | Sáu vai trò | Đầu vào → đầu ra; dữ liệu truyền; câu nối |
|---|---:|---|---|
| L14-00 | 3 | Vấn đề: định nghĩa nhu cầu học qua tác vụ; các bước khác N/A vì là mở bài. | Ít nhãn → câu hỏi thích nghi nhanh; nối LLO. |
| L14-01 | 3 | Triển khai: khóa sản phẩm LLO; các bước khác N/A vì là định hướng. | Tiên quyết → ba sản phẩm episode/loss/update; nối tình huống. |
| L14-02 | 3 | Vấn đề + ví dụ: 5-way 1-shot; kiểm tra bằng câu hỏi; các bước khác N/A vì chưa ký hiệu hóa. | Tình huống nguồn → nhu cầu dùng nhiều tác vụ; nối phân phối tác vụ. |
| L14-03 | 3 | Trực giác: phân biệt điều kiện ít mẫu, học chuyển giao và siêu học tập bằng việc chất lượng sau thích nghi có nằm trong mục tiêu huấn luyện hay không; hình thức sơ bộ bằng hai phân phối; còn lại N/A. | $p_\mathcal T(x,y)$ → $p(\mathcal T)$; nối episode. |
| L14-04 | 3 | Trực giác: hỗ trợ thích nghi/truy vấn đánh giá; triển khai bằng sơ đồ; còn lại N/A. | Một tác vụ → $S_i\cap Q_i=\varnothing$, cùng lấy từ $\mathcal T_i$; nối đếm mẫu. |
| L14-05 | 3 | Hình thức: N/K/R, nhãn cục bộ; còn lại N/A vì hợp đồng ký hiệu. | $S_i,Q_i$ → $NK,NR$; nối shape. |
| L14-06 | 3 | Hình thức/tính: hợp đồng tensor và quy tắc flatten; còn lại N/A. | N/K/R/B → $X^S,X^Q,Y^S,Y^Q$; nối split. |
| L14-07 | 3 | Triển khai: giao thức split theo câu hỏi đánh giá; kiểm tra ngầm bằng ba trường hợp; còn lại N/A. | Trục task/class/domain → split không rò rỉ; nối G cụ thể. |
| L14-08 | 3 | Ví dụ: khóa episode G 2-way 2-shot; còn lại N/A vì dữ liệu sẽ dùng ở ba cụm. | Hợp đồng → G với A/B, support/query; nối mục tiêu chung. |
| L14-09 | 3 | Hình thức: kỳ vọng qua tác vụ và episode sau thích nghi; ProtoNet tạo prototype, MAML tạo tham số thích nghi; Siamese giữ vai trò xác minh cặp nếu chưa có luật tổng hợp N-way. | $(\mathcal T,S,Q)$ → $\mathcal L^Q(A_\theta(S))$ cho các phương pháp có trạng thái sau hỗ trợ; không ép Siamese vào $A_\theta$; nối kiểm tra hợp đồng. |
| L14-10 | 3 | Kiểm tra: tính số mẫu; các bước khác N/A vì đóng cụm. | B/N/K/R → 12 support, 6 query; nối cách tạo cặp từ G. |
| L14-11 | 3 | Vấn đề + ví dụ: G tạo cặp cùng/khác lớp; còn lại N/A. | G → $(2.5,2,z=1)$ và $(2.5,4,z=0)$; nối kiến trúc dùng chung. |
| L14-12 | 3 | Trực giác + triển khai: hai nhánh dùng chung bộ mã hóa $f_\theta$; còn lại N/A. | Hai mẫu qua cùng $f_\theta$ → hai embedding so sánh được; nối mất mát cặp. |
| L14-13 | 3 | Hình thức/tính: $p_b=\sigma(s_b)$ và BCE trung bình trên $B_p$ từ logits ổn định; còn lại N/A. | $s,z\to p$ → $\mathcal L_{pair}$; nối giới hạn dự đoán. |
| L14-14 | 3 | Triển khai: bộ xác minh cặp và caveat lấy mẫu; còn lại N/A. | Điểm cặp → chưa có quy tắc N-way; nối kiểm tra G. |
| L14-15 | 3 | Kiểm tra: nhãn cặp và chiều mất mát; còn lại N/A vì đóng cụm. | G + BCE → loss giảm; nối đại diện theo lớp. |
| L14-16 | 2 | Vấn đề: bộ xác minh phải so truy vấn với nhiều mẫu tham chiếu; trực giác dùng prototype để rút gọn thành một đại diện mỗi lớp; còn lại N/A. | Nhiều so sánh cặp → một prototype/lớp; nối embedding. |
| L14-17 | 2 | Trực giác + hình thức shape: bộ mã hóa tạo không gian so sánh; còn lại N/A. | $X^S,X^Q$ → $Z^S,Z^Q$; G có D=1; nối trung bình K. |
| L14-18 | 2 | Hình thức/tính: mean đúng trục K; kiểm tra âm bằng cấm query; còn lại N/A. | $Z^S[B,N,K,D]$ → $C[B,N,D]$; nối G. |
| L14-19 | 2 | Ví dụ + kiểm tra: tính prototype G; còn lại N/A. | A(0,2), B(4,6) → (1,5); nối broadcasting. |
| L14-20 | 2 | Hình thức/tính: broadcast và rút gọn D; còn lại N/A. | query/prototype → $d,\ell:[B,NR,N]$; nối tính G. |
| L14-21 | 2 | Ví dụ + kiểm tra: tính khoảng cách query A; còn lại N/A. | 2.5 và (1,5) → (2.25,6.25); nối chuẩn hóa. |
| L14-22 | 2 | Hình thức/triển khai: log-softmax ổn định theo trục lớp; còn lại N/A. | $\ell[B,NR,N]$ → $\log P[B,NR,N]$; nối NLL. |
| L14-23 | 2 | Ví dụ + hình thức/tính: gather nhãn, mean query rồi task; kiểm tra bằng fragment. | G → xác suất và $\mathcal L_G\approx.00908$; nối gradient. |
| L14-24 | 2 | Triển khai: computational graph và gradient hai nhánh; còn lại N/A. | NLL → cập nhật bộ mã hóa chung; nối leakage. |
| L14-25 | 2 | Kiểm tra: phát hiện query vào prototype; còn lại N/A vì đóng cụm. | G → vi phạm support/query; nối trạng thái thích nghi MAML. |
| L14-26 | 2 | Vấn đề + trực giác: hai họ khác ở $A_\theta(S)$; còn lại N/A. | G/ProtoNet → prototype; MAML → tham số $\phi$; nối động lực. |
| L14-27 | 2 | Vấn đề + trực giác: học khởi tạo dễ thích nghi; điều kiện khả vi; còn lại N/A. | Objective chung → MAML; nối classifier G. |
| L14-28 | 2 | Ví dụ: cùng G với classifier khả vi; hình thức sơ bộ; còn lại N/A. | G → $P_\phi(B\mid h)$, $\theta=(0,0)$; nối gradient hỗ trợ. |
| L14-29 | 2 | Ví dụ + tính toán + kiểm tra: gradient support G; còn lại N/A. | Bốn support → $(-1,0)$; nối inner update. |
| L14-30 | 2 | Hình thức/tính: inner update, fragment số; còn lại N/A. | $\theta,\alpha,\nabla L_S$ → $\phi=(1,0)$; nối query. |
| L14-31 | 2 | Ví dụ + kiểm tra: dự đoán và loss query G; còn lại N/A. | $\phi$ + hai query → $.3377$; nối outer objective. |
| L14-32 | 2 | Hình thức: mean query trong task rồi mean B task; còn lại N/A. | $\phi_i$ → $\mathcal L_{meta}$; nối thuật toán. |
| L14-33 | 2 | Triển khai: lấy lô tác vụ, đặt $\phi_i^0=\theta$, cập nhật khả vi và tối ưu vòng ngoài; còn lại N/A. | L32 → đặt gradient 0/phi riêng/mean truy vấn/mean tác vụ/lan truyền ngược/cập nhật; nối sơ đồ. |
| L14-34 | 2 | Triển khai + trực giác: lô tác vụ thành một cập nhật chung; còn lại N/A. | Thuật toán → graph nhiều nhánh; nối đường meta-gradient. |
| L14-35 | 2 | Trực giác + hình thức: dependency $\theta\to\phi(\theta)\to L_Q$; còn lại N/A. | Graph → quy tắc chuỗi; nối exact/FO khái niệm. |
| L14-36 | 2 | Hình thức: exact giữ đạo hàm, FO xấp xỉ Jacobian bằng I; còn lại N/A. | Dependency → hai đường gradient; số học chuyển X03; nối meta-test. |
| L14-37 | 2 | Triển khai/ứng dụng: meta-test và caveat mode; còn lại N/A. | $\theta$ + support mới → $\phi_{test}$ → query; nối leakage. |
| L14-38 | 2 | Kiểm tra đóng cụm MAML: phân biệt rò rỉ trong tác vụ và qua tác vụ; fragment xác nhận dùng nhãn truy vấn để cập nhật $\phi$ là rò rỉ trong tác vụ. | Support/query + task split → lỗi trong/qua task; nối vấn đề cần so sánh ba cách dùng hỗ trợ. |
| L14-39 | 2 | Vấn đề so sánh + trực giác + ví dụ: cùng G nhưng ba phương pháp tạo trạng thái sau hỗ trợ và kiểu dự đoán khác nhau. | G → tham chiếu cặp với $\theta$ không đổi/prototype/$\phi$; nối gradient/chi phí. |
| L14-40 | 2 | Triển khai + so sánh: tham số, gradient, test compute; còn lại N/A. | Ba trạng thái G → trade-off có điều kiện; nối quyết định. |
| L14-41 | 2 | Kiểm tra tổng hợp: nhận diện prototype, cập nhật tham số và bộ xác minh cặp trên G; còn lại N/A vì kết thúc lõi. | G → gọi đúng Siamese/ProtoNet/MAML; đi xuống X01 nếu mở phụ lục. |
| **Lõi** | **100** | **42 trang** | **16 trang × 3 phút + 26 trang × 2 phút.** |

## Phụ lục và bài tập

| ID | Phút | Vai trò | Đầu vào → đầu ra; câu nối |
|---|---:|---|---|
| L14-X01 | 5 | Đối chiếu/kiểm tra; chu trình rút gọn vì chỉ khóa ranh giới. | Siêu học tập ít mẫu ↔ gợi ý ít mẫu; nối variable-K. |
| L14-X02 | 5 | Vấn đề + kiểm tra; rút gọn vì không có benchmark được duyệt. | K huấn luyện → K kiểm tra đổi; yêu cầu đánh giá riêng; nối chi tiết gradient. |
| L14-X03 | 5 | Ví dụ + hình thức/tính + kiểm tra; triển khai bằng caveat graph/HVP. | I: exact -2, FO -4; làm rõ HVP không cần ma trận Hessian; nối ứng dụng. |
| L14-X04 | 5 | Ứng dụng + kiểm tra; rút gọn vì nguồn chỉ dùng làm case. | Vùng địa lý → task/support/query; không nêu benchmark; kết thúc. |
| **Mở rộng** | **20** | **4 trang** | **Đi xuống từ L14-41 đến X01, rồi tiếp tục xuống X04 trong cùng stack.** |

Tiết bài tập 50 phút tách timing: 10 phút hợp đồng episode; 15 phút ProtoNet G; 15 phút inner update và outer objective MAML; 10 phút so ProtoNet/MAML. Exact/FO không phải yêu cầu bài tập.

## Điều hướng thực tế

DOM có sáu stack dọc với counts [11,5,10,6,7,7]: L14-00–10, L14-11–15, L14-16–25, L14-26–31, L14-32–38 và L14-39–41 + X01–X04. Đi xuống trong stack; đi phải tại các biên L14-10, L14-15, L14-25, L14-31 và L14-38. Stack cuối chứa tuyến so sánh L14-39–41 rồi phụ lục X01–X04 đi xuống; không có nhánh phụ lục thứ hai.

Sau lần tách từ 4 sang 6 stack đã rà hai trang mỗi phía tại các biên L14-10, L14-15, L14-25, L14-31, L14-38 và X01; câu nối và ký hiệu G không bị đứt.
