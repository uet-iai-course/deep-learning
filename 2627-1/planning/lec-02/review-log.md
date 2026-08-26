# Nhật ký rà soát Bài 02

## Phạm vi và quyết định nguồn

- Giữ phạm vi đề cương: lan truyền xuôi, hàm mất mát, đồ thị tính toán, quy tắc chuỗi, lan truyền ngược và một cập nhật MLP.
- Giữ mạch chính của `lec06_backprop.pdf`, tr. 3–16, 18–35 và `lec07_backprop_part2.pdf`, tr. 8–31.
- Dùng `lec05_multilayer.pdf`, tr. 28–34 để nhắc MLP; `lec04_multiclass.pdf`, tr. 12–19 cho softmax/entropy chéo; giáo trình PDF tr. 31–32, 68–73, 90–96 để kiểm chứng.
- Bỏ hình ResNet/ResNeXt ở `lec06_backprop.pdf`, tr. 14 vì kéo bài sang kiến trúc ngoài phạm vi. Không bàn cực tiểu địa phương, bộ tối ưu nâng cao hoặc gradient triệt tiêu qua mạng sâu; các phần đó thuộc Bài 03.

## Ánh xạ chi tiết và quyết định chuyển

| Nguồn | Nội dung nguồn | Trang đích | Quyết định | Lý do |
|---|---|---|---|---|
| Đề cương III.2, Buổi 2 | Tên, LLO, phạm vi | L02-00–01, toàn deck | giữ | Khóa ranh giới bài và mục tiêu |
| `lec06_backprop.pdf`, tr. 3–5 | MLP, forward/backward, đồ thị | L02-02–05 | giữ + Việt hóa | Mạch mở đầu chính |
| `lec06_backprop.pdf`, tr. 6–8 | Quy tắc chuỗi | L02-07 | giữ, chuyển sau ví dụ forward | Chu trình học cần ví dụ trước hình thức |
| `lec06_backprop.pdf`, tr. 11–13 | Upstream × local | L02-08 | giữ + sửa ký hiệu | Dùng cộng-gán nhất quán |
| `lec06_backprop.pdf`, tr. 14–16 | Nhiều đường | L02-12, L02-14 | giữ ý, bỏ hình kiến trúc | Không đổi phạm vi sang ResNet |
| `lec06_backprop.pdf`, tr. 18–35 | Cổng vô hướng, sigmoid | L02-05–11, L02-X01 | gộp + thêm ví dụ số | Giảm lặp; tạo tuyến tính toán kiểm được |
| `lec07_backprop_part2.pdf`, tr. 8–9 | Ví dụ cổng | L02-13 | giữ như ví dụ độc lập | Không trộn dữ kiện với ví dụ L02-05–12; hình không lộ đáp án |
| `lec07_backprop_part2.pdf`, tr. 10–14 | Jacobian/VJP | L02-15–17 | sửa quy ước | Dùng covector hàng nhất quán trên hình và công thức |
| `lec07_backprop_part2.pdf`, tr. 15–17 | ReLU, sigmoid | L02-18, L02-X02 | giữ + khóa ranh giới | Chỉ nói đạo hàm cục bộ; phần mạng sâu để Bài 03 |
| `lec07_backprop_part2.pdf`, tr. 19–29 | Tầng afin backward | L02-19–24, L02-33–35 | tách + chuyển quy ước | Đưa phép suy theo chỉ số vào lõi trước công thức ma trận; dùng batch-first |
| `lec05_multilayer.pdf`, tr. 28–34 | MLP nhiều lớp | L02-25–27 | giữ ý + sửa tầng ra | Tầng ra phân loại tạo logits, không đặt ReLU |
| `lec04_multiclass.pdf`, tr. 12–19 | Softmax, entropy chéo | L02-28–32 | tách + bổ sung suy dẫn | Tính log-softmax/LSE trực tiếp từ logits và suy $G_Z$ bằng quy tắc chuỗi |
| Giáo trình PDF tr. 68–73 | Softmax/CE | L02-28–32 | kiểm chứng + sửa kích thước | Không chép kích thước xung đột; giữ $Z,P,Y\in\mathbb R^{B\times k}$ |
| Giáo trình PDF tr. 90–94 | Đồ thị, trạng thái | L02-04, L02-14, L02-37 | giữ ý + làm rõ | Tách chế độ mô hình khỏi ghi gradient; thêm zero-grad trước batch |
| Giáo trình PDF tr. 96 | Bộ nhớ, gradient check | L02-X04–X05 | mở rộng | Dùng $\theta\pm\varepsilon e_j$, sai số tương đối, tránh điểm gãy |

## Sai khác có chủ ý và quyết định chỉnh sửa

| Vị trí | Quyết định | Bằng chứng và lý do |
|---|---|---|
| L02-05–12 | Dùng $f=2(xy+\max(z,w))$, $x=3,y=-4,z=2,w=-1$; chạy forward trước quy tắc chuỗi | Giá trị forward $-20$; gradient $(-8,6,2,0)$. Sửa thứ tự theo vòng rà storyboard. |
| L02-13 | Giữ ví dụ nguồn như ví dụ độc lập; bỏ gradient khỏi SVG | Câu hỏi nay yêu cầu tự tính; đáp án chỉ nằm trong notes/note-for-author. |
| L02-15–17 | Covector hàng: $G_x^{row}=G_z^{row}J_f$ | Đồng bộ hình VJP và công thức; không đổi quy ước gradient tensor cùng shape biến. |
| L02-19–24 | Đưa $Z_{ic}=\sum_jX_{ij}W_{jc}+b_c$ vào lõi | Sửa lỗi đặt công thức ma trận trước phép suy; ba công thức theo sau trực tiếp. |
| L02-25 | Đổi “ba lớp” thành “ba lớp đích”; định nghĩa one-hot và trục lớp trên mặt trang | Sửa mơ hồ và tiên quyết chỉ có trong notes. |
| L02-28–32 | Tách softmax, log-softmax/LSE, Jacobian softmax, quy tắc chuỗi và $G_Z$ | Trừ cực đại trước exp chưa đủ nếu tiếp tục lấy log của xác suất đã làm tròn; công thức mới tính CE trực tiếp từ logits. |
| L02-33–35 | Tách gradient tầng ra, kéo qua ReLU, gradient tầng ẩn; bỏ `.micro`; làm tròn 4 chữ số | Bản cũ thu SVG còn khoảng 10 px và dồn nhiều ma trận sáu chữ số. Toán hạng $H,W_2,A,X$ nay hiện rõ. |
| L02-36 | Cập nhật chỉ sau khi đủ gradient | Giữ mọi gradient tại cùng bộ tham số cũ. |
| L02-37 | Tách chế độ mô hình, ghi gradient, zero-grad và cập nhật | Ba loại trạng thái không đồng nhất; zero-grad phải đứng trước mỗi batch. |
| L02-X02 | Ghi ranh giới Bài 03 trên mặt trang | Chỉ kết luận đạo hàm sigmoid cục bộ nhỏ, không suy rộng sang mạng sâu. |
| L02-X05 | Dùng $\theta\pm\varepsilon e_j$, sai số tương đối, thử nhiều $\varepsilon$, tránh điểm gãy | Sửa công thức chỉ đổi một tọa độ và bổ sung điều kiện dùng gradient check. |
| Toàn bộ MLP | Mặt trang làm tròn 3–4 chữ số; notes và mục kiểm chứng giữ số đầy đủ | Tăng khả năng đọc mà không mất bằng chứng tính toán. |

## Báo cáo kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | L02-05–08 | Công thức quy tắc chuỗi đứng trước ví dụ forward | Chu trình khái niệm bắt đầu hình thức trước dữ kiện | Đã chuyển forward lên L02-06, quy tắc chuỗi xuống L02-07–08 |
| nghiêm trọng | L02-28–32 | Thiếu suy dẫn $G_Z$ | Bản cũ nhảy từ CE sang $(P-Y)/B$ | Đã thêm L02-30–31 |
| trung bình | L02-13 | Ví dụ đổi đột ngột | Dữ kiện khác ví dụ chính nhưng không báo | Đã ghi rõ “độc lập” trên tiêu đề, alt và notes |
| trung bình | Toàn storyboard | Thiếu tiên quyết, sản phẩm, tensor truyền, bước gộp/không áp dụng | Bảng cũ chỉ có luận điểm và câu nối | Đã bổ sung đủ trường cho từng trang |
| trung bình | L02-25–35 | Timing sít | Nhiều phép tính số dồn trong hai trang | Đã tách thành L02-32–35; lõi vẫn đúng 100 phút |
| nhẹ | L02-08, L02-12 | Dễ trùng ý cộng gradient | Cả hai cùng dùng cộng-gán | Giữ: L02-08 nêu quy tắc nút, L02-12 giải thích nhiều đường; notes phân vai |
| nhẹ | Outline | Ánh xạ nguồn còn theo cụm rộng | Không truy được quyết định theo trang nguồn | Đã thêm bảng ánh xạ chi tiết ở nhật ký này |

## Bốn báo cáo rà soát độc lập

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | L02-30 cũ | SVG backward không đọc được | `.figure.micro` giới hạn 145 px, chữ ước khoảng 9.5–10.9 px | Đã bỏ `.micro`, hiển thị SVG 250 px tại L02-33 |
| nghiêm trọng | L02-30–31 cũ | Quá nhiều ma trận sáu chữ số, thiếu bước trung gian | Tầng ra, $G_H$, ReLU và tầng ẩn dồn trong hai trang | Đã tách L02-32–35, làm tròn 4 chữ số, giữ số đầy đủ trong notes |
| trung bình | L02-24–31 cũ | Không nói tensor nào phải giữ | Backward dùng $H,W_2,A,X$ nhưng mặt trang không nối | Đã ghi toán hạng cần giữ tại L02-26–27, 33–35 |
| trung bình | L02-13 | Hình lộ đáp án | SVG ghi bốn gradient đầu vào | Đã bỏ đáp án khỏi SVG |
| trung bình | L02-01,24,26–29 cũ | Tiên quyết, one-hot, trục lớp chỉ ở notes | Người tự học không thấy trên mặt trang | Đã đưa lên L02-01, L02-25, L02-27–29 |
| trung bình | L02-24 cũ | “Ba lớp” mơ hồ | Không rõ lớp ẩn hay lớp đích | Đã đổi thành “ba lớp đích” |
| trung bình | L02-X05 | Thiếu $J^+,J^-$ và sai số | Chỉ có công thức vô hướng theo $\theta_j$ | Đã dùng $\theta\pm\varepsilon e_j$ và sai số tương đối |

### Chuyên gia Học sâu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | L02-27–30 cũ | Thiếu suy softmax–CE từ quy tắc chuỗi | $G_Z$ xuất hiện như công thức ghi nhớ | Đã thêm Jacobian softmax và phép ghép chuỗi tại L02-30–31 |
| trung bình | L02-18, L02-X02 | Ranh giới ReLU/sigmoid với Bài 03 chưa rõ | Có thể mở sang gradient triệt tiêu mạng sâu | Đã khóa kết luận ở đạo hàm cục bộ và ghi ranh giới trên L02-X02 |
| trung bình | L02-33 cũ | Trộn suy luận với ghi gradient | Model mode và autograd là hai điều khiển khác nhau | Đã tách ba trạng thái tại L02-37 |
| trung bình | L02-24–32 cũ | Thiếu điểm dừng tính | Không biết khi nào đủ gradient để cập nhật | L02-35 chốt đủ gradient, L02-36 mới cập nhật |
| nhẹ | L02-03, L02-29 cũ | Liên hệ hồi quy softmax chưa rõ | Tầng ra afin và gradient CE đứng rời | Notes L02-31 nối trực tiếp với hồi quy softmax |

### Độ chính xác toán học, thuật toán và triển khai

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | L02-27–29 cũ | CE chưa ổn định số đầy đủ | Trừ max cho softmax nhưng vẫn lấy $\log P$ | Đã tính log-softmax/LSE trực tiếp từ logits tại L02-29 |
| trung bình | L02-33 cũ | Thiếu đặt gradient về 0 | Chu trình có batch mới nhưng không xóa gradient tích lũy | Đã thêm zero-grad trước mỗi batch tại L02-37 |
| trung bình | L02-33 cũ | Trộn model mode và ghi gradient | Hai trạng thái có thể thay đổi độc lập | Đã tách thành hai thẻ riêng tại L02-37 |
| trung bình | L02-X05 | Thiếu $e_j$, cảnh báo điểm không trơn | Công thức không nói chỉ đổi tọa độ $j$ | Đã bổ sung $e_j$, thử $\varepsilon$, tránh điểm gãy |
| nhẹ | L02-14, L02-X04 | Thiếu chi phí VJP | Chưa nói vì sao không dựng Jacobian | Notes L02-14 nêu tính VJP cục bộ và cùng bậc với forward; không thêm hệ số ngoài nguồn |

### Phản biện học thuật và giảng dạy Học sâu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | L02-19–23 cũ | Công thức afin đứng trước phép suy | Người học chỉ nhận ba công thức ma trận | Đã thêm L02-20 và chỉ số vào L02-21–23 |
| nghiêm trọng | L02-27–29 cũ | CE ổn định số chưa đúng | Có nguy cơ $\log 0$ sau làm tròn/underflow | Đã dùng log-sum-exp trực tiếp từ logits |
| nghiêm trọng | L02-28–30 cũ | Thiếu quy tắc chuỗi cho $G_Z$ | Công thức đúng nhưng đặt không có cầu nối | Đã thêm L02-30–31 trước số gradient |
| trung bình | L02-15–18 | Hướng VJP chưa khóa | Hình dùng vector hàng nhưng ký hiệu chung mơ hồ | Đã định nghĩa covector hàng tại L02-15–16 |
| trung bình | L02-33 cũ | Trộn mode và gradient | Khái niệm triển khai không cùng trục | Đã tách tại L02-37 |
| trung bình | L02-13 | Ví dụ mới xuất hiện không báo | Dữ kiện đổi khỏi tuyến chính | Đã ghi “đồ thị độc lập” và không lộ đáp án |
| trung bình | L02-X05 | Thiếu sai số tương đối và lựa chọn epsilon | Không có tiêu chí so sánh | Đã bổ sung công thức sai số và hướng dẫn thử epsilon |

Mọi lỗi `chặn bàn giao` hoặc `nghiêm trọng`: không có lỗi chặn; toàn bộ lỗi nghiêm trọng nêu trên đã được xử lý. Các lỗi trung bình và nhẹ cũng đã được xử lý hoặc ghi quyết định giữ có lý do.

## Kiểm chứng ví dụ MLP với số đầy đủ

$$
P=\begin{bmatrix}0.922860&0.075753&0.001387\\0.075389&0.918423&0.006188\end{bmatrix},\qquad J=0.082688.
$$

- $G_Z=[[-0.038570,0.037876,0.000694],[0.037694,-0.040789,0.003094]]$;
- $G_{W_2}=[[-0.115711,0.113629,0.002081],[0.074951,-0.083033,0.008082]]$;
- $G_{b_2}=[-0.000876,-0.002912,0.003788]$;
- $G_H=[[-0.039264,0.037183],[0.034600,-0.043883]]$;
- $G_A=[[-0.039264,0.037183],[0,-0.043883]]$;
- $G_{W_1}=[[-0.039264,0.124948],[-0.078528,0.030483]]$;
- $G_{b_1}=[-0.039264,-0.006700]$.

Với $\eta=0.1$, $(W_1)_{11}$ thành $1.003926$. Sai phân hữu hạn trung tâm với $\varepsilon=10^{-4}$ tại tọa độ này cho $g_j^{\mathrm{num}}=-0.03926392814990187$, còn đạo hàm giải tích là $g_j=-0.039263928093072796$. Dùng mẫu số $\max(\tau,|g_j^{\mathrm{num}}|+|g_j|)$ với $\tau$ rất nhỏ, sai số tương đối xấp xỉ $7.24\times10^{-10}$.

## Rà lại độ chính xác sau chỉnh sửa

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| trung bình | L02-X05 | Mẫu số $\max(1,|g_j^{\mathrm{num}}|,|g_j|)$ che sai lệch tương đối khi gradient nhỏ | Với $g_j=10^{-8}$ và $g_j^{\mathrm{num}}=0$, công thức cũ cho $10^{-8}$ dù sai lệch tương đối là 100% | Dùng $|g_j^{\mathrm{num}}-g_j|/\max(\tau,|g_j^{\mathrm{num}}|+|g_j|)$; kiểm thêm sai số tuyệt đối khi cả hai gần 0 | Đã sửa L02-X05 và tính lại từ số đầy đủ |

Vòng rà lại xác nhận các công thức VJP/Jacobian, suy tầng afin theo chỉ số, log-softmax, log-sum-exp, đạo hàm softmax–entropy chéo, mọi kích thước và ma trận gradient tại L02-19–36 đều đúng. Thứ tự cập nhật, phân biệt chế độ mô hình với ghi gradient và thao tác đặt gradient về 0 cũng đúng.

## Kiểm định cuối

- HTML có 43 `data-slide-id` duy nhất và 43 khối ghi chú diễn giả; cấu trúc gồm 39 trang lõi và 4 trang mở rộng.
- Storyboard cộng đúng 100 phút lõi, 20 phút mở rộng và 50 phút bài tập tách riêng.
- Đã dựng 131 công thức bằng KaTeX cục bộ với `throwOnError: true` và `strict: "error"`; không có lỗi.
- Mười một SVG đều là XML hợp lệ, có `role="img"`, `title`, `desc`; mọi đường dẫn HTML tồn tại. Không có tham chiếu raster hoặc tài nguyên mạng cốt lõi.
- Đã rà thủ công toàn bộ tiêu đề `h1`, `h2`, `h3`; chỉ giữ MLP, ReLU, softmax, sigmoid và Jacobian như tên hoặc thuật ngữ chuẩn. Các cụm `gradient`, `max`, `batch`, `forward`, `backward`, `training`, `inference`, `loss` đã được thay bằng cách diễn đạt tiếng Việt trong tiêu đề.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`. Bản thay thế `python3 -m http.server 8765` đã chạy tại thư mục gốc; URL deck trả HTTP 200.
- Dự án Codex Slides bền vững có mã `20260826073304-b-i-02-lan-truy-n-v-th-t-nh-to-n-81pf`; `generated/outline.md` đã được đồng bộ với `planning/lec-02/outline.md` và xác minh kích thước 5358 byte. Tải thêm HTML, planning và SVG vào Design Files thất bại với HTTP 500; dự án vẫn ở checkpoint `clarify`, 0 slide.
- Phiên hiện tại không cung cấp Browser nội bộ hoặc trình duyệt headless đã cài sẵn. Vì vậy chưa thể duyệt trực quan mọi trang ngang/dọc ở 16:9 và màn hình hẹp, và không tuyên bố đã rà trực quan bằng Codex Slides. Kiểm định tĩnh, KaTeX và HTTP cục bộ đã hoàn tất; đây là giới hạn công cụ còn lại.

## Hình, biên tập và giới hạn

- Có 11 SVG tại `2627-1/img/lec-02/`; mọi SVG có `role="img"`, `title`, `desc`. `toy-backward-check.svg` đã bỏ đáp án; `mlp-example-backward.svg` không còn bị thu nhỏ.
- Không có raster, tài nguyên mạng hay code demo.
- Đã rà trực tiếp theo `no-ai-slop/eval.md`: không thêm số liệu/nhận định ngoài nguồn, không có câu hỏi tu từ, khẩu hiệu, nhịp máy móc, metadiscourse hoặc từ cấm trong nội dung hiển thị/notes.
- Đã rà theo Quill về thứ tự khái niệm, ký hiệu, tensor truyền và chuyển ý; không có và không tạo `quill.json`.
- Chưa cập nhật `index.html`; bước đó chỉ thực hiện sau kiểm định cuối của điều phối viên.
