# Ghi chú cho người soạn Bài 10

## Tuyến giảng

- Tuyến lõi đi từ L10-00 đến L10-31 trong 99 phút, rồi kết thúc bằng L10-32 trong 1 phút. Tại L10-31, dùng End để đến thẳng L10-32.
- Tuyến đầy đủ dùng phím Phải tại L10-31 để vào L10-X01, đi xuống qua X02, X03, X04 rồi đến L10-32. Bốn trang mở rộng kéo dài 20 phút và có thể bỏ nguyên cụm; L10-32 vẫn là kết luận cuối.
- Phím Phải được định tuyến lại tại sáu ranh giới L10-03→04, 07→08, 13→14, 18→19, 26→27 và 31→X01 vì Reveal có thể giữ chỉ số dọc của mạch kế tiếp. End luôn đến L10-32; các phím khác dùng hành vi mặc định.
- Giữ bộ số $H=[(1,0),(0,2),(-1,1)]$, $e=(1,2,0)$ trên L10-08–13, 18, 24–25 và 31. Không đổi số giữa chừng.
- Khi viết công thức điểm, nhắc quy ước vectơ hàng của deck. Giáo trình trình bày dạng vectơ cột; hai dạng chỉ khác chuyển vị tham số.
- Phân biệt ba phép chuẩn hóa: softmax chú ý theo nguồn $T_s$; softmax đầu ra theo từ vựng $V_{tgt}=|\mathcal V_{tgt}|$; trung bình mất mát theo số ký hiệu đích hợp lệ.
- Ở L10-06, nêu định nghĩa tổng quát trước khi gắn $q=s_{t'-1}$ và $k_i=v_i=h_i$. L10-X02 chỉ áp dụng lại định nghĩa này sang ảnh, bản ghi và cặp văn bản.
- Mặt nạ nguồn đi vào trước softmax chú ý. Mỗi hàng có ít nhất một ký hiệu hợp lệ do EOS; giá trị thay thế hữu hạn chỉ cho trọng số đệm xấp xỉ 0 và không được dùng để che một hàng rỗng. Mặt nạ đích chỉ cân entropy chéo và không thay mặt nạ nguồn.
- Khởi tạo $s_{n,0}=\phi(h^{enc}_{n,L_n})$ từ trạng thái nguồn cuối hợp lệ, không lấy vị trí đệm. Với LSTM, truy vấn lấy trạng thái ẩn, không lấy trạng thái ô.
- Trong suy luận theo lô, dùng mặt nạ hoạt động để giữ trạng thái mẫu đã EOS hoặc loại mẫu đó khỏi lô hoạt động.
- Dùng L10-32 để thu hồi nút thắt → truy xuất theo bước → Q/K/V rồi nối sang Bài 11. Không mở hệ số tỉ lệ, nhiều đầu, mặt nạ nhân quả hoặc khối Transformer trong bài này.
- Bảy mạch có đầu ra liên tiếp: nút thắt → chu trình truy xuất → vết số → hàm điểm và mặt nạ → giải mã và căn chỉnh → thuật toán đầy đủ → chuyển miền và kết luận. Không đổi thứ tự này khi cắt tuyến mở rộng.

## Đáp án và lỗi dễ mắc

- L10-06: truy vấn là $s_{t'-1}$; khóa và giá trị đều là $h_i$ trong mô hình Bahdanau đang xét.
- L10-13: $A$ rút gọn trục $T_s$, nên $C$ có kích thước $N\times D_h$.
- L10-18: khi vị trí ba là đệm, $\alpha=(0.268941,0.731059,0)$ và $c=(0.268941,1.462117)$. Không nhân trọng số cũ với mặt nạ mà bỏ bước chuẩn hóa lại.
- L10-16: phép co với $v_a$ rút gọn chiều $D_a$; kết quả $N\times T_s\times1$ được bỏ trục cuối để thành $E\in\mathbb R^{N\times T_s}$.
- L10-23: huấn luyện dùng ký hiệu đúng ở đầu vào giải mã; suy luận dùng ký hiệu dự đoán. Suy luận dừng từng mẫu tại EOS hoặc độ dài tối đa.
- L10-26: trọng số lớn mô tả đóng góp trong phép tổng hợp tại lần chạy đó. Nó không đủ để kết luận nhân quả về dự đoán. Đi xuống L10-27, không đi phải.
- L10-29: ba hạng chi phí lần lượt ứng với chiếu trạng thái nguồn, chiếu truy vấn theo bước đích, rồi tính điểm và tổng giá trị cho mọi cặp. Tăng gấp đôi $T'$ làm hạng theo cặp tăng gấp đôi nếu các kích thước khác giữ nguyên.
- L10-30: gọi đây là đối chiếu hai biến thể cơ sở và đánh đổi, không giảng như kết luận chung; L10-32 mới thu hồi toàn bài và nối Bài 11.
- L10-31: $\alpha=(0.244728,0.665241,0.090031)$; $c=(0.154698,1.420512)$; softmax chạy trên ba vị trí nguồn.
- L10-X04: trong mô tả ảnh, truy vấn là trạng thái giải mã trước; khóa và giá trị là đặc trưng theo vùng; softmax chạy trên vùng hợp lệ.

## Bài tập 50 phút và đáp án

1. **Phân tích nút thắt, 10 phút.** Cho hai thiết kế: $c=h_{L_n}$ dùng cho mọi bước và $c_{t'}=\sum_i\alpha_{t',i}h_i$. Yêu cầu nêu hai hạn chế của thiết kế đầu và cơ chế cụ thể của thiết kế sau. Đáp án: một vectơ phải giữ mọi chi tiết nguồn và mọi bước không thể truy xuất vị trí khác nhau; chú ý tính điểm theo truy vấn bước đích rồi tổng hợp lại các trạng thái nguồn.
2. **Tính chú ý, 20 phút.** Dùng $H=[(1,0),(0,2),(-1,1)]$, $e=(1,2,0)$. Phần a không mặt nạ; phần b đặt vị trí ba là đệm. Yêu cầu dùng softmax ổn định, ghi trục và tính $\alpha,c$. Đáp án phần a: $\alpha=(0.244728,0.665241,0.090031)$, $c=(0.154698,1.420512)$. Phần b: $\alpha=(0.268941,0.731059,0)$, $c=(0.268941,1.462117)$.
3. **Đọc căn chỉnh, 15 phút.** Dùng ma trận ở L10-24. Yêu cầu nêu vị trí lớn nhất mỗi hàng, xác nhận tổng hàng và phân biệt căn chỉnh mềm với ghép cặp cứng. Đáp án: các cực đại lần lượt ở cột 2, 3, 1; mỗi hàng cộng 1; các ô còn lại vẫn có trọng số dương.
4. **Giới hạn diễn giải, 5 phút.** Phản biện mệnh đề “ô chú ý lớn nhất là nguyên nhân của ký hiệu dự đoán”. Đáp án: trọng số chỉ thuộc phép tổng hợp; cần can thiệp vào ký hiệu hoặc trạng thái, hay dùng phép đo bổ sung để đánh giá quan hệ nhân quả.

## Điểm cần kiểm chứng khi sửa

- Nếu đổi trace, phải sửa đồng thời L10-08–13, 18, 24–25, 31, outline, storyboard, review-log và đáp án bài tập.
- Nếu đổi quy ước trục, phải sửa L10-07, 09, 13, 15–18, 20, 24, 28–29 và 31.
- Nếu thêm nội dung Transformer, phải đối chiếu ranh giới Bài 11; mặc định không mở rộng ngoài cầu nối L10-32.
- Nếu thay mô hình giải mã, phải giữ thứ tự truy vấn $s_{t'-1}$ → ngữ cảnh $c_{t'}$ → trạng thái $s_{t'}$ nhất quán với công thức đang dạy.
- Nếu thay bản đồ chú ý, phải giữ nhãn ký hiệu ở cả hai trục và ghi rõ dữ liệu tự xây; không biến các hàng điểm cho sẵn thành kết quả của tham số chưa được cung cấp.

## Giới hạn công cụ

- Kiểm tra tự động không thay thế duyệt trực quan. Nếu Browser hoặc Codex Slides không khả dụng, chỉ báo kết quả kiểm định tĩnh và để điều phối viên chạy HTTP/visual.
