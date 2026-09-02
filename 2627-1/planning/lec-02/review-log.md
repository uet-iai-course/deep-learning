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
| `lec06_backprop.pdf`, tr. 3–5 | MLP, lan truyền xuôi/ngược, đồ thị | L02-02–05 | giữ + Việt hóa | Mạch mở đầu chính |
| `lec06_backprop.pdf`, tr. 6–8 | Quy tắc chuỗi | L02-07 | giữ, chuyển sau ví dụ lan truyền xuôi | Chu trình học cần ví dụ trước hình thức |
| `lec06_backprop.pdf`, tr. 11–13 | Thượng nguồn × cục bộ | L02-08 | giữ + sửa ký hiệu | Dùng cộng-gán nhất quán |
| `lec06_backprop.pdf`, tr. 14–16 | Nhiều đường | L02-12, L02-14 | giữ ý, bỏ hình kiến trúc | Không đổi phạm vi sang ResNet |
| `lec06_backprop.pdf`, tr. 18–35 | Cổng vô hướng, sigmoid | L02-05–11, L02-X01 | gộp + thêm ví dụ số | Giảm lặp; tạo tuyến tính toán kiểm được |
| `lec07_backprop_part2.pdf`, tr. 8–9 | Ví dụ cổng | L02-13 | giữ như ví dụ độc lập | Không trộn dữ kiện với ví dụ L02-05–12; hình không lộ đáp án |
| `lec07_backprop_part2.pdf`, tr. 10–14 | Jacobian/VJP | L02-15–17 | sửa quy ước | Dùng covector hàng nhất quán trên hình và công thức |
| `lec07_backprop_part2.pdf`, tr. 15–17 | ReLU, sigmoid | L02-18, L02-X02 | giữ + khóa ranh giới | Chỉ nói đạo hàm cục bộ; phần mạng sâu để Bài 03 |
| `lec07_backprop.pdf`, tr. 19–29 | Tầng afin lượt ngược | L02-19–24, L02-33–35 | tách + chuyển quy ước | Đưa phép suy theo chỉ số vào lõi trước công thức ma trận; dùng lô theo hàng |
| `lec05_multilayer.pdf`, tr. 28–34 | MLP nhiều lớp | L02-25–27 | giữ ý + sửa tầng ra | Tầng ra phân loại tạo điểm số, không đặt ReLU |
| `lec04_multiclass.pdf`, tr. 12–19 | Softmax, entropy chéo | L02-28–32 | tách + bổ sung suy dẫn | Tính log-softmax/LSE trực tiếp từ điểm số và suy $G_Z$ bằng quy tắc chuỗi |
| Giáo trình PDF tr. 68–73 | Softmax/CE | L02-28–32 | kiểm chứng + sửa kích thước | Không chép kích thước xung đột; giữ $Z,P,Y\in\mathbb R^{B\times k}$ |
| Giáo trình PDF tr. 90–94 | Đồ thị, trạng thái | L02-04, L02-14, L02-37 | giữ ý + làm rõ | Tách chế độ mô hình khỏi ghi gradient; thêm đặt gradient về 0 trước lô |
| Giáo trình PDF tr. 96 | Bộ nhớ, kiểm tra đạo hàm | L02-X04–X05 | mở rộng | Dùng $\theta\pm\varepsilon e_j$, sai số tương đối, tránh điểm gãy |

## Sai khác có chủ ý và quyết định chỉnh sửa

| Vị trí | Quyết định | Bằng chứng và lý do |
|---|---|---|
| L02-05–12 | Dùng $f=2(xy+\max(z,w))$, $x=3,y=-4,z=2,w=-1$; chạy lan truyền xuôi trước quy tắc chuỗi | Giá trị xuôi $-20$; gradient $(-8,6,2,0)$. Sửa thứ tự theo vòng rà storyboard. |
| L02-13 | Giữ ví dụ nguồn như ví dụ độc lập; bỏ gradient khỏi SVG | Câu hỏi nay yêu cầu tự tính; đáp án chỉ nằm trong notes/note-for-author. |
| L02-15–17 | Covector hàng: $G_x^{row}=G_z^{row}J_f$ | Đồng bộ hình VJP và công thức; không đổi quy ước gradient tensor cùng kích thước biến. |
| L02-19–24 | Đưa $Z_{ic}=\sum_jX_{ij}W_{jc}+b_c$ vào lõi | Sửa lỗi đặt công thức ma trận trước phép suy; ba công thức theo sau trực tiếp. |
| L02-25 | Đổi “ba lớp” thành “ba lớp đích”; định nghĩa nhãn nhất vị và trục lớp trên mặt trang | Sửa mơ hồ và tiên quyết chỉ có trong notes. |
| L02-28–32 | Tách softmax, log-softmax/LSE, Jacobian softmax, quy tắc chuỗi và $G_Z$ | Trừ cực đại trước exp chưa đủ nếu tiếp tục lấy log của xác suất đã làm tròn; công thức mới tính mất mát trực tiếp từ điểm số. |
| L02-33–35 | Tách gradient tầng ra, kéo qua ReLU, gradient tầng ẩn; bỏ `.micro`; làm tròn 4 chữ số | Bản cũ thu SVG còn khoảng 10 px và dồn nhiều ma trận sáu chữ số. Toán hạng $H,W_2,A,X$ nay hiện rõ. |
| L02-36 | Cập nhật chỉ sau khi đủ gradient | Giữ mọi gradient tại cùng bộ tham số cũ. |
| L02-37 | Tách chế độ mô hình, ghi gradient, đặt gradient về 0 và cập nhật | Ba loại trạng thái không đồng nhất; đặt gradient về 0 phải đứng trước mỗi lô. |
| L02-X02 | Ghi ranh giới Bài 03 trên mặt trang | Chỉ kết luận đạo hàm sigmoid cục bộ nhỏ, không suy rộng sang mạng sâu. |
| L02-X05 | Dùng $\theta\pm\varepsilon e_j$, sai số tương đối, thử nhiều $\varepsilon$, tránh điểm gãy | Sửa công thức chỉ đổi một tọa độ và bổ sung điều kiện dùng kiểm tra đạo hàm. |
| L02-06 | Ví dụ $f=2(xy+\max(z,w))$ là ví dụ tự dựng theo mạch cổng nguồn, không phải ví dụ nguyên văn `lec06` tr. 18–31 | Ghi rõ trong notes và nguồn của trang để không gán sai cho nguồn. |
| L02-14 | Bỏ mệnh đề "lượt ngược cùng bậc chi phí với lượt xuôi" vì nguồn không chứng minh | Giữ nguyên thuật toán lan truyền ngược; notes chỉ nối triển khai ở mức nguồn cho phép. |
| L02-18 | Đưa quy ước đạo hàm ReLU tại $A=0$ bằng 0 lên mặt trang; notes ghi hệ quả đơn vị ReLU chết | Quy ước cần thấy được; nguyên nhân và cách xử lý để Bài 03. |
| L02-27–32 | Đồng bộ cách gọi "điểm số" lần đầu, sau đó ưu tiên "điểm số" | Giảm pha ngôn ngữ; thuật ngữ nhất quán trên mặt trang. |
| L02-31 | Thêm bước trung gian $\partial\ell_i/\partial Z_{ic}=P_{ic}-Y_{ic}$ rồi $G_Z=(P-Y)/B$ | Bước suy thấy được; không đổi dữ kiện số hay công thức đã xác nhận. |
| L02-37 | Đổi nhãn thẻ "Đạo hàm" thành "Ghi gradient"; thêm thứ tự một bước trên mặt trang | Nhãn đúng bản chất; thứ tự lô mới → xóa gradient cũ → xuôi → mất mát → ngược → cập nhật. |
| L02-39 | Thêm trang kết ngoài kết luận chung, thu hồi chuỗi và ba tiêu chí kiểm | Sửa lỗi chặn mạch: thiếu section kết ngoài; cả hai tuyến kết thúc ở đây. |
| L02-31, L02-33, L02-38, L02-39 | L02-31 là 5 phút, L02-33 là 4 phút, L02-38 là 2 phút, L02-39 là 2 phút | Giữ tổng lõi đúng 100 phút; L02-38 nhường 1 phút và phần bù còn lại lấy từ dồn trang cho L02-39 |
| L02-X03 | Giữ mã trống, không dùng | Không đổi mã các trang còn lại; mã ổn định. |
| Toàn bộ MLP | Mặt trang làm tròn 3–4 chữ số; notes và mục kiểm chứng giữ số đầy đủ | Tăng khả năng đọc mà không mất bằng chứng tính toán. |

## Báo cáo kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | L02-05–08 | Công thức quy tắc chuỗi đứng trước ví dụ lan truyền xuôi | Chu trình khái niệm bắt đầu hình thức trước dữ kiện | Đã chuyển lan truyền xuôi lên L02-06, quy tắc chuỗi xuống L02-07–08 |
| nghiêm trọng | L02-28–32 | Thiếu suy dẫn $G_Z$ | Bản cũ nhảy từ CE sang $(P-Y)/B$ | Đã thêm L02-30–31 |
| trung bình | L02-13 | Ví dụ đổi đột ngột | Dữ kiện khác ví dụ chính nhưng không báo | Đã ghi rõ “độc lập” trên tiêu đề, alt và notes |
| trung bình | Toàn storyboard | Thiếu tiên quyết, sản phẩm, tensor truyền, bước gộp/không áp dụng | Bảng cũ chỉ có luận điểm và câu nối | Đã bổ sung đủ trường cho từng trang |
| trung bình | L02-25–35 | Timing sít | Nhiều phép tính số dồn trong hai trang | Đã tách thành L02-32–35; lõi vẫn đúng 100 phút |
| nhẹ | L02-08, L02-12 | Dễ trùng ý cộng gradient | Cả hai cùng dùng cộng-gán | Giữ: L02-08 nêu quy tắc nút, L02-12 giải thích nhiều đường; notes phân vai |
| nhẹ | Outline | Ánh xạ nguồn còn theo cụm rộng | Không truy được quyết định theo trang nguồn | Đã thêm bảng ánh xạ chi tiết ở nhật ký này |

## Năm báo cáo rà soát độc lập

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | L02-30 cũ | SVG lan truyền ngược không đọc được | `.figure.micro` giới hạn 145 px, chữ ước khoảng 9.5–10.9 px | Đã bỏ `.micro`, hiển thị SVG 250 px tại L02-33 |
| nghiêm trọng | L02-30–31 cũ | Quá nhiều ma trận sáu chữ số, thiếu bước trung gian | Tầng ra, $G_H$, ReLU và tầng ẩn dồn trong hai trang | Đã tách L02-32–35, làm tròn 4 chữ số, giữ số đầy đủ trong notes |
| trung bình | L02-24–31 cũ | Không nói tensor nào phải giữ | Backward dùng $H,W_2,A,X$ nhưng mặt trang không nối | Đã ghi toán hạng cần giữ tại L02-26–27, 33–35 |
| trung bình | L02-13 | Hình lộ đáp án | SVG ghi bốn gradient đầu vào | Đã bỏ đáp án khỏi SVG |
| trung bình | L02-01,24,26–29 cũ | Tiên quyết, nhãn nhất vị, trục lớp chỉ ở ghi chú | Người tự học không thấy trên mặt trang | Đã đưa lên L02-01, L02-25, L02-27–29 |
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
| nghiêm trọng | L02-27–29 cũ | CE chưa ổn định số đầy đủ | Trừ cực đại cho softmax nhưng vẫn lấy $\log P$ | Đã tính log-softmax/LSE trực tiếp từ điểm số tại L02-29 |
| trung bình | L02-33 cũ | Thiếu đặt gradient về 0 | Chu trình có lô mới nhưng không xóa gradient tích lũy | Đã thêm đặt gradient về 0 trước mỗi lô tại L02-37 |
| trung bình | L02-33 cũ | Trộn chế độ mô hình và ghi gradient | Hai trạng thái có thể thay đổi độc lập | Đã tách thành hai thẻ riêng tại L02-37 |
| trung bình | L02-X05 | Thiếu $e_j$, cảnh báo điểm không trơn | Công thức không nói chỉ đổi tọa độ $j$ | Đã bổ sung $e_j$, thử $\varepsilon$, tránh điểm gãy |
| nhẹ | L02-14, L02-X04 | Thiếu chi phí VJP | Chưa nói vì sao không dựng Jacobian | Bác mệnh đề chi phí "cùng bậc lan truyền xuôi" vì nguồn không chứng minh; chỉ giữ VJP cục bộ và duyệt tô-pô ngược |

### Phản biện học thuật và giảng dạy Học sâu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | L02-19–23 cũ | Công thức afin đứng trước phép suy | Người học chỉ nhận ba công thức ma trận | Đã thêm L02-20 và chỉ số vào L02-21–23 |
| nghiêm trọng | L02-27–29 cũ | CE ổn định số chưa đúng | Có nguy cơ $\log 0$ sau làm tròn hoặc tràn dưới | Đã dùng log-sum-exp trực tiếp từ điểm số |
| nghiêm trọng | L02-28–30 cũ | Thiếu quy tắc chuỗi cho $G_Z$ | Công thức đúng nhưng đặt không có cầu nối | Đã thêm L02-30–31 trước số gradient |
| trung bình | L02-15–18 | Hướng VJP chưa khóa | Hình dùng vector hàng nhưng ký hiệu chung mơ hồ | Đã định nghĩa covector hàng tại L02-15–16 |
| trung bình | L02-33 cũ | Trộn mode và gradient | Khái niệm triển khai không cùng trục | Đã tách tại L02-37 |
| trung bình | L02-13 | Ví dụ mới xuất hiện không báo | Dữ kiện đổi khỏi tuyến chính | Đã ghi “đồ thị độc lập” và không lộ đáp án |
| trung bình | L02-X05 | Thiếu sai số tương đối và lựa chọn epsilon | Không có tiêu chí so sánh | Đã bổ sung công thức sai số và hướng dẫn thử epsilon |

### Kết nối và mạch viết

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | review-log | Thiếu vai kết nối và mạch viết trong bộ năm báo cáo | Mục "Năm báo cáo" cũ chỉ liệt kê bốn vai; vai kết nối vào mạch viết chưa có bảng riêng | Thêm chính mục này làm báo cáo vai thứ năm, với bảng đủ cột Mức độ, Trang chiếu, Vấn đề, Bằng chứng, Đề xuất sửa, Quyết định | Đã sửa bằng chính báo cáo này |
| trung bình | storyboard, bảng sáu mạch | Bảng sáu mạch lệch hai mạch đầu so với ranh giới trang thực tế | Mạch "Mở đầu" ghi L02-00–05 nhưng L02-06–07 thuộc mạch cổng theo bảng ánh xạ; mạch "Cổng vô hướng" ghi L02-06–14 trong khi vai trò kết nối vào từ L02-06 | Căn lại ranh giới hai mạch đầu theo bảng ánh xạ chi tiết | Đã sửa thành L02-00–05 và L02-06–14 |
| trung bình | note-for-author, tuyến mở rộng | Chỉ dẫn bỏ mở rộng chưa cụ thể về thao tác điều hướng | Câu "bỏ qua section mở rộng" không nói thao tác phím; người trình chiếu có thể đi lạc vào L02-X01 | Ghi rõ thao tác: từ L02-38 nhấn mũi tên phải hai lần để đến L02-39 | Đã sửa bằng thao tác mũi tên phải hai lần |
| chặn bàn giao | L02-39, hai tuyến | Thiếu kết bài: cả hai tuyến kết thúc mà không có trang kết | Trước khi thêm L02-39, tuyến lõi dừng ở L02-38 và tuyến đầy đủ dừng ở L02-X05; không có thu hồi chuỗi | Thêm trang kết L02-39 và rà lại cả hai tuyến | Đã sửa bằng L02-39; rà lại xác nhận hết lỗi |

Vai trò trong mạch của từng điểm: báo cáo này là vai kết nối vào mạch viết (kết nối vào: bộ bốn báo cáo trước; kết nối ra: vòng sửa sau năm báo cáo và kiểm định cuối). Bảng sáu mạch là kết nối vào từ bảng ánh xạ chi tiết và kết nối ra sang storyboard. Chỉ dẫn điều hướng kết nối vào tuyến lõi L02-38 và kết nối ra sang L02-39. Trang kết L02-39 kết nối vào toàn bộ tuyến lõi và kết nối ra sang Bài 03.

Mọi lỗi `chặn bàn giao` hoặc `nghiêm trọng`: không có lỗi chặn; toàn bộ lỗi nghiêm trọng nêu trên đã được xử lý. Các lỗi trung bình và nhẹ cũng đã được xử lý hoặc ghi quyết định giữ có lý do.

## Vòng sửa sau năm báo cáo (bản hiện tại)

Năm báo cáo hiện tại gồm đúng năm vai: góc nhìn sinh viên; chuyên gia Học sâu; độ chính xác toán học, thuật toán và triển khai; phản biện học thuật và giảng dạy; kết nối và mạch viết. Kiểm định storyboard được ghi là một bước riêng, không tính vào năm báo cáo. Mỗi báo cáo theo đúng vai với các trường mức độ/trang/vấn đề/bằng chứng/đề xuất như các bảng trên.

Quyết định điều phối viên chấp nhận:

- Ví dụ $f=2(xy+\max(z,w))$ là ví dụ tự dựng theo mạch cổng nguồn; ghi rõ ở L02-05–06, không phải ví dụ nguyên văn `lec06` tr. 18–31.
- Tầng ra afin → softmax cho phân loại; không đặt ReLU ở tầng ra.
- Hệ số $1/B$ trong $G_Z=(P-Y)/B$ đến từ trung bình lô.

Đề xuất được sửa hoặc bác:

| Đề xuất | Quyết định |
|---|---|
| Thêm mạch kết ngoài (L02-39) | Đã sửa: thêm trang kết, đúng 6 mạch ngoài |
| Giảm thời lượng để giữ tổng 100+20 | Đã sửa: L02-31 là 5 phút, L02-33 là 4 phút, L02-38 là 2 phút, L02-39 là 2 phút; tổng lõi 100 |
| L02-01 thêm softmax/logarit vào tiên quyết | Đã sửa; Jacobian không thành tiên quyết, được giới thiệu ở L02-15–16 |
| L02-06 nâng cỡ bảng | Đã sửa bằng style cục bộ `font-size:.80em` |
| L02-14 bỏ mệnh đề chi phí cùng bậc | Đã sửa; giữ thuật toán |
| L02-18 quy ước ReLU tại 0 lên mặt trang | Đã sửa; notes thêm đơn vị ReLU chết, xử lý để Bài 03 |
| L02-27–32 đồng bộ "điểm số (logit)" | Đã sửa |
| L02-31 thêm bước trung gian thấy được | Đã sửa bằng các khối căn giữa; không thêm ví dụ số Jacobian riêng |
| L02-37 đổi nhãn thẻ và thêm thứ tự | Đã sửa; không nêu tên framework/API |
| Ghi chú L02-13 nói rõ ReLU nhận 6>0 | Đã sửa; không đổi cấu trúc hay số |
| Ghi chú L02-28 cảnh báo $\log(P)$ bị tràn dưới | Đã sửa; ghi chú L02-32 thêm trực giác bất biến khi cộng hằng số, theo mẹo ổn định softmax trong nguồn |
| L02-X05 định nghĩa sai phân trung tâm | Đã sửa; ghi chú nối sang L02-39 |
| Ghi chú L02-X01 báo tuyến có thể cắt | Đã sửa |
| Bác: thêm cơ chế tham chiếu của đạo hàm tự động ở L02-X04 | Bác vì ngoài nguồn |
| Bác: tính mất mát mới sau cập nhật ở L02-36 | Bác vì ngoài phạm vi một bước cập nhật |
| Bác: thêm mã trình diễn, sổ tay tính toán, nguồn web | Bác vì phạm vi nguồn khóa |

Lỗi kết bài (thiếu mạch kết ngoài) đã xử lý bằng L02-39. Lý do bỏ `lec06` tr. 9–10: nội dung hai trang đó trùng mạch cổng đã gộp ở L02-05–11 và không mang dữ kiện số riêng. Lý do giữ X03 trống: không đổi mã các trang còn lại, giữ mã ổn định giữa các vòng sửa.

Kiểm định cuối đã được chạy lại sau các sửa; kết quả hiện hành nằm trong mục **Kiểm định cuối** bên dưới.

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

Vòng rà lại xác nhận các công thức VJP/Jacobian, suy tầng afin theo chỉ số, log-softmax, log-sum-exp, đạo hàm softmax–entropy chéo, mọi kích thước và ma trận gradient tại L02-19–36 đều đúng. Thứ tự cập nhật, phân biệt chế độ mô hình với ghi gradient và thao tác đặt gradient về 0 cũng đúng. Lượt rà toán sau sửa không còn lỗi chặn, nghiêm trọng hay trung bình. Lượt rà kết nối xác nhận kết bài hết lỗi sau khi các điểm trên được sửa: L02-39 có mặt ở cả hai tuyến, bảng sáu mạch đã căn lại, và chỉ dẫn bỏ mở rộng đã cụ thể bằng thao tác mũi tên phải hai lần.

## Kiểm định cuối

- Trạng thái bản hiện tại: **ĐẠT**, với ngoại lệ công cụ được ghi riêng dưới đây.
- HTML có 44 `data-slide-id` duy nhất, 44 ghi chú diễn giả và 6 mạch ngoài; số trang theo từng mạch là `[6, 9, 10, 14, 4, 1]`.
- Storyboard cộng đúng 100 phút lõi, 20 phút mở rộng và 50 phút bài tập tách riêng.
- Đã dựng 140 công thức bằng KaTeX cục bộ với `throwOnError: true` và `strict: "error"`; không có lỗi.
- Mười một SVG đều là XML hợp lệ, có `role="img"`, `title`, `desc`; mọi đường dẫn HTML tồn tại. Không có tham chiếu ảnh raster hoặc tài nguyên mạng cốt lõi.
- Đã rà thủ công toàn bộ tiêu đề `h1`, `h2`, `h3`; chỉ giữ MLP, ReLU, softmax, sigmoid và Jacobian như tên hoặc thuật ngữ chuẩn.
- Đã chụp và rà toàn bộ 44 trang bằng Chromium ở 1280 × 720 và 960 × 720, tổng cộng 88 ảnh. L02-39 từng bị cắt công thức ở mép phải; đã tách công thức thành ba dòng, chừa khoảng cho nút điều hướng và chụp lại ở cả hai khung. Không còn tràn chữ, chồng lấn hoặc công thức bị cắt.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`. Dùng `python3 -m http.server 8765` chỉ trên thư mục `2627-1/` để phục vụ kiểm tra, tránh làm lộ `.env` hoặc nguồn nội bộ.
- Dự án Codex Slides bền vững có mã `20260826073304-b-i-02-lan-truy-n-v-th-t-nh-to-n-81pf`; `generated/outline.md` đã được đồng bộ với `planning/lec-02/outline.md`. Tải thêm HTML, planning và SVG vào Design Files từng thất bại với HTTP 500; phiên này không có trình duyệt nội bộ Codex Slides, nên kiểm định trực quan được thực hiện bằng Chromium cục bộ.

## Hình, biên tập và giới hạn

- Có 11 SVG tại `2627-1/img/lec-02/`; mọi SVG có `role="img"`, `title`, `desc`. `toy-backward-check.svg` đã bỏ đáp án; `mlp-example-backward.svg` không còn bị thu nhỏ.
- Không có ảnh raster, tài nguyên mạng hay mã trình diễn.
- Đã rà trực tiếp theo `no-ai-slop/eval.md`: không thêm số liệu hoặc nhận định ngoài nguồn, không có câu hỏi tu từ, khẩu hiệu, nhịp máy móc, lời dẫn về quá trình viết hoặc từ cấm trong nội dung hiển thị và ghi chú.
- Đã rà theo Quill về thứ tự khái niệm, ký hiệu, tensor truyền và chuyển ý; không có và không tạo `quill.json`.
- `index.html` đã có liên kết đúng đến deck Bài 02; không cần sửa mục chỉ mục trong vòng này.

## Quy trình và kiểm định lecture note

### Dossier và worker

- Codex trích cục bộ đúng các dải nguồn đã duyệt thành UTF-8: `lec06` tr. 3–16, 18–35; `lec07` tr. 8–31; `lec05` tr. 28–34; `lec04` tr. 12–19; giáo trình PDF tr. 31–32, 68–73, 90–96; mục DOCX `III.2 → Buổi 2`. Không gửi PDF, DOCX, `.env` hoặc bí mật lên OpenRouter.
- Reader lập kế hoạch và reader bản đồ chủ đề dùng `z-ai/glm-5.3-flash` qua OpenRouter, metadata quan sát khớp model yêu cầu. Lượt reader nguồn đầu tiên vượt giới hạn 10 tool-call nên toàn bộ đầu ra bị loại; chạy lại cùng model bằng hai dossier nửa phạm vi và hợp nhất tại checkpoint.
- Writer dùng `deepseek/deepseek-v4-flash-0731` qua OpenRouter. Lượt soạn chỉ nhận `approved-spec.md` và mẫu lecture note, chỉ tạo `lecture-note.md`. Lượt tự kiểm dùng staging mới, chỉ nhận bản nháp và checklist, rồi chỉ ghi một bản sửa. Cả hai lượt có `requested_model` và `observed_model` trùng nhau, provider là OpenRouter.
- Điều phối viên phát hiện đặc tả tạm từng ghi sai đáp án của bài kiểm tra độc lập. Bài và đáp án được khóa lại theo cùng hàm $f=2(xy+\max(z,w))$: tại $x=4,y=-6,z=-1,w=2.5$, gradient theo $x,y,z,w$ là $-12,8,0,2$.

### Năm phản biện và vòng sửa

| Vai | Kết quả | Quyết định |
|---|---|---|
| Góc nhìn sinh viên | Đạt; hai câu diễn đạt nhẹ chưa tự nhiên | Đã sửa câu về gradient độ chệch và nhận xét sigmoid cục bộ |
| Chuyên gia Học sâu | Toán của note đúng; báo sai khác với đặc tả tạm và cho rằng SVG thiếu trong staging | Sửa đặc tả tạm; bác nhận định SVG vì bốn tài sản thật trong kho đã được kiểm tra |
| Toán–thuật toán–triển khai | Đạt; reviewer dùng một quy ước sai số tương đối khác | Giữ định nghĩa đã công bố và tính trực tiếp từ số đầy đủ |
| Phản biện học thuật–giảng dạy | Mạch đạt; phép tính lại sai độ lớn hiệu hai gradient | Bác bằng hiệu trực tiếp $5.68\times10^{-11}$ |
| Kết nối và mạch viết | Lượt đầu vượt tool-call nên bị loại; lượt lại với một tệp đầu vào đạt | Sửa chuỗi tensor thành $X\to A\to H\to Z\to P\to J$ và rút gọn số thập phân |

Hai tái kiểm định cuối đều dùng `z-ai/glm-5.3-flash` qua OpenRouter với metadata khớp. Vai toán xác nhận toàn bộ ví dụ vô hướng, gradient trung bình theo lô, ReLU tại 0 và kiểm gradient; vai mạch xác nhận tuyến vô hướng → tensor → MLP, kết luận và không có chỉ dẫn nội bộ. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.

### Giới hạn phạm vi ổn định cho DeepSeek

- Một task dùng một staging vật lý, danh sách đầu vào đóng và đúng một đầu ra.
- Bản nháp lecture note dùng mẫu hai đầu vào/một đầu ra; tự kiểm dùng staging mới và cũng chỉ một đầu ra.
- Writer không đọc lại nguồn thô sau checkpoint; mọi mốc nguồn, phép tính và ranh giới phải nằm trong đặc tả đã duyệt.
- Planning, index, SVG và báo cáo tách khỏi task soạn note. Mảnh bổ sung dài tối đa 1.500 từ hoặc 6.000 ký tự; ghi chú diễn giả tối đa năm khối mỗi task.
- Mọi `length`, timeout, tool-limit, JSON không hợp lệ hoặc thiếu tệp đều bị loại; không đổi model/provider và không tăng ngân sách trước khi chia nhỏ phạm vi.
- Các quy tắc này đã được ghi vào `prompt_lecture_note_deck.md` để áp dụng cho các buổi sau.

### Biên tập và QA lecture note

- Lượt `$no-ai-slop` loại câu máy móc, số thập phân gây nhiễu và siêu bình luận; tự kiểm theo `no-ai-slop/eval.md` không thấy dấu vết AI, nhãn quy trình, mã nội bộ hay chỉ dẫn dành cho người viết/diễn giả trong tài liệu công khai.
- Lượt `$quill` xác nhận thứ tự nhu cầu gradient → đồ thị → cổng vô hướng → tensor/VJP → tầng afin → softmax/entropy chéo → MLP → trạng thái → kiểm gradient; ký hiệu và dữ kiện không đổi giữa các phần. Không tạo `quill.json`.
- Note có đúng một H1 và 14 dòng directive tạo bảy khối cân bằng, không lồng nhau; các loại `exercise`, `solution`, `derivation` đều thuộc allowlist của viewer. Hai khối lời giải dùng `<details>` và gập mặc định theo `material-viewer.js`.
- Đã dựng 125 biểu thức bằng KaTeX cục bộ với `throwOnError: true`, `strict: "error"`; không có lỗi.
- Note dùng bốn SVG hiện có, đều có `role="img"`, `title`, `desc`; mọi đường dẫn tồn tại và không có raster.
- `index.html` trỏ đúng `material-viewer.html?doc=materials/lec-02/lecture-note.md&deck=lecture-02-lan-truyen-va-do-thi-tinh-toan.html`. HTTP cục bộ tại cổng 8766 trả 200 cho index, viewer, Markdown và deck.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Phiên này không có Browser/Codex Slides nên không tuyên bố đã kiểm trực quan bằng công cụ đó; QA tĩnh, KaTeX và HTTP đã hoàn tất.

## Đồng bộ deck sau lecture note

### Fan-out delta và writer

- Ba lượt chỉ đọc dùng `z-ai/glm-5.3-flash` qua OpenRouter; metadata model/provider đều khớp. Vai độ phủ xác nhận deck bao phủ toàn bộ tuyến lõi và mở rộng của note; vai toán xác nhận mọi công thức, shape và số; vai storyboard xác nhận 6 mạch ngoài cùng timing 100+20 phút.
- Delta duy nhất được duyệt là bổ sung vào ghi chú L02-31: nếu mất mát lấy tổng theo lô thì công thức không có hệ số $1/B$. Mặt slide không đổi nên không tăng tải hay gây tràn.
- DeepSeek writer dùng `deepseek/deepseek-v4-flash-0731` qua OpenRouter với đúng hai đầu vào và một đầu ra: `approved-delta.md`, một section L02-31, và `replacement.html`. `requested_model` khớp `observed_model`; provider là OpenRouter. Codex kiểm rồi áp dụng đúng một thay thế.
- Đề xuất đổi thao tác từ hai lần thành năm lần bị bác. Trong RevealJS, `<section>` ngoài nằm trên trục ngang, bốn trang mở rộng là `<section>` trong trên trục dọc. Từ L02-38, lần nhấn phải thứ nhất sang đầu stack mở rộng; lần thứ hai sang section kết luận. Hướng dẫn này được giữ trong storyboard và `note-for-author.md`, đồng thời xóa khỏi ghi chú diễn giả.

### Năm phản biện độc lập sau delta

| Vai | Kết quả | Quyết định |
|---|---|---|
| Góc nhìn sinh viên | PASS; báo nhẹ xác suất $0.075753$ và thao tác điều hướng | Bác: tính trực tiếp cho $0.0757529296$; hai lần nhấn đúng với stack RevealJS. Nhận góp ý alt text. |
| Chuyên gia Học sâu | Lượt đầu timeout nên bị loại; lượt lại dossier hẹp PASS | Không đổi model hay tăng ngân sách; ghi nhận deck đủ độ phủ và chiều sâu. |
| Toán–thuật toán–triển khai | PASS | Xác nhận $1/B$, chuỗi MLP, cập nhật và gradient check. |
| Phản biện học thuật–giảng dạy | Lượt đầu báo sai $G_{W_1}$ vì dùng $G_{A,21}=0.0346$ | Bác bằng mặt nạ ReLU: $A_{21}=-1$ nên $G_{A,21}=0$. Tái kiểm phạm vi hẹp xác nhận L02-34–36 và L02-X05 đúng, kết luận PASS. |
| Kết nối và mạch viết | Nhận hai góp ý thật: alt L02-13 chứa chú giải biên tập; dòng trạng thái trong storyboard chồng L02-33–36. Tái kiểm toàn tệp timeout. | Đã sửa alt theo nghĩa, gán vấn đề trạng thái cho L02-37 và bỏ chỉ dẫn khỏi notes. Chạy lại trên dossier ba section + hai đoạn storyboard, PASS. |

Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`. Mã X03 vẫn để trống có chủ ý nhằm giữ ổn định `data-slide-id` và đã được giải thích trong planning.

### `$no-ai-slop`, `$quill` và QA cuối

- Lượt `$no-ai-slop` đọc toàn bộ nội dung hiển thị và 44 ghi chú: bỏ chú giải biên tập trong alt L02-13; bỏ chỉ dẫn điều hướng khỏi L02-38/L02-39; đổi các câu chỉ dẫn ở L02-15, L02-28, L02-37, L02-X01, L02-X02, L02-X04, L02-39 thành giải thích kỹ thuật trực tiếp. Không còn dấu vết AI, nhãn quy trình hay hướng dẫn cho diễn giả/người viết trong HTML.
- Lượt `$quill` xác nhận xương sống vô hướng → tensor → MLP → trạng thái → kết luận, ranh giới các mạch và ký hiệu không đổi. Không tạo `quill.json`.
- QA tĩnh: 6 section ngoài, 44 `data-slide-id` duy nhất, 44 ghi chú, 140 biểu thức KaTeX ở `throwOnError: true`, `strict: "error"`, 11 SVG có `role="img"`, `title`, `desc`; cấu hình RevealJS bắt buộc và toàn bộ đường dẫn đều đạt.
- Rà thủ công toàn bộ `h1`, `h2`, `h3`: chỉ giữ MLP, ReLU, softmax, sigmoid và Jacobian theo nhóm thuật ngữ chuẩn được phép. Delta không thay đổi nội dung nhìn thấy hay bố cục; kiểm định hình ảnh 88 ảnh ở 1280×720 và 960×720 của bản deck trước delta vẫn áp dụng.
- HTTP cục bộ tại cổng 8766 trả 200. `python3 -m reloadserver 8765` vẫn lỗi vì thiếu mô-đun; Browser/Codex Slides không khả dụng trong phiên này, nên không tuyên bố đã dùng chúng.
