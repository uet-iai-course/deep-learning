# Nhật ký rà soát Bài 04

## Quyết định nguồn

- Giữ mạch chính của `lec08_cnn.pdf`: ảnh → tích chập → nhiều kênh → phép gộp → trường tiếp nhận → đầu phân loại.
- Dùng GT PDF 110–135 để kiểm chứng ký hiệu, nhiều kênh, kích thước, phép gộp và LeNet.
- Không dùng slide PDF 31–36. Trang mở rộng 1×1 chỉ dùng giáo trình PDF 126–127, nằm trong dải đã duyệt.
- Không dùng lịch sử hoặc kết quả định lượng LeNet.

## Sửa và làm rõ

| Vấn đề nguồn | Quyết định |
|---|---|
| Nguồn thường gọi phép trượt là tích chập | Nêu rõ thư viện học sâu thực hiện tương quan chéo, không lật nhân |
| GT dùng bố cục kênh cuối ở một số minh họa | Khóa toàn deck theo NCHW cho tensor kích hoạt và OIHW cho trọng số; giải nghĩa bốn chữ trên mặt trang |
| Nguồn dùng “bất biến dịch chuyển” cho bản đồ đặc trưng | Dùng “tương đương dịch chuyển”; nêu biên, vùng đệm và bước trượt có thể phá quan hệ chính xác |
| Công thức nguồn thường dùng vùng đệm đối xứng | Dùng $P_t,P_b,P_l,P_r$ để xử lý nhân chẵn và đệm bất đối xứng |
| Nguồn có biến thể độ giãn/group/tích chập riêng từng kênh | Bỏ vì ngoài phạm vi đã khóa |
| Nguồn ghi số phép toán nhưng thiếu quy ước đếm | Dùng MAC và không quy đổi thành FLOPs |
| Phép gộp được mô tả tăng bất biến | Chỉ nói giảm nhạy với dịch chuyển nhỏ trong điều kiện cụ thể; không bất biến tuyệt đối |
| Công thức tham số đôi khi bỏ độ lệch | Dùng $C_{out}(C_{in}K_hK_w+1)$ |

## Quyết định sau phản biện

| Mức | Vấn đề | Quyết định và lý do |
|---|---|---|
| Chặn bàn giao | L04-22 có ký tự `<` thô trong HTML | Đổi thành `\lt` để HTML hợp lệ và KaTeX xử lý nhất quán; đáp án dùng hiệu ứng xuất hiện |
| Nghiêm trọng | Cỡ chữ nền `.78em` làm chữ, bảng và công thức nhỏ | Tăng section lên `.9em`; khóa `.tiny=.84em`, bảng `.86em`, `.math-mid=.9em`, đều cho cỡ hiệu dụng ít nhất `.756em`; tăng chiều cao hình `.medium` và chữ trong các SVG trọng yếu |
| Nghiêm trọng | L04-02 nói làm phẳng “xóa” quan hệ lân cận | Sửa thành giữ giá trị nhưng không mã hóa hoặc khai thác tường minh quan hệ cục bộ |
| Nghiêm trọng | Ví dụ kích thước dùng ký hiệu $P=1,S=2$ mơ hồ | Ghi đủ $P_t=P_b=P_l=P_r=1$ và $S_h=S_w=2$; khóa $S_h,S_w\in\mathbb Z_{>0}$ |
| Nghiêm trọng | Công thức nhiều kênh dùng chỉ số có thể âm | Định nghĩa $\widetilde X$ là tensor đệm 0 và chỉ đánh chỉ số không âm trên tensor này |
| Nghiêm trọng | Ví dụ 56 thiếu dữ kiện để tái lập | Hiển thị đủ $X_0,X_1,W_{0,0},W_{0,1},b_0=0$, phép tính 56; trang sau hiện ma trận kết quả và tám tích sau câu hỏi |
| Nghiêm trọng | Định nghĩa trường tiếp nhận nói “tầng trước” nhưng truy hồi đo trên đầu vào | Định nghĩa lại là vùng trên đầu vào hoặc tầng tham chiếu; $r_l,j_l$ cùng đo trên tầng đó |
| Trung bình | Câu hỏi hiển thị sẵn đáp án | Dùng hiệu ứng xuất hiện ở L04-14, L04-22, L04-25 và L04-X04 |
| Trung bình | $K$ và $W$ đổi ký hiệu không có cầu nối | Thêm chú giải: $K$ là nhân ví dụ một kênh; $W$ là tensor trọng số đầy đủ, $W_{o,c,:,:}$ là lát nhân |
| Trung bình | Dễ hiểu tích chập chồng nhau vẫn tạo phi tuyến | Bổ sung cầu nối ở L04-26 và phát biểu tường minh ở L04-37 rằng tích chập thường đi với hàm kích hoạt |
| Trung bình | Phát biểu đệm giữ kích thước và phép gộp quá rộng | Khóa đệm giữ kích thước ở $S=1$; nói phép gộp “thường” giảm độ phân giải khi hình học làm giảm số vị trí |
| Trung bình | Ghi chú diễn giả chứa chỉ dẫn phạm vi nội bộ | Chuyển ranh giới độ giãn và dải nguồn sang `note-for-author.md`; notes chỉ giữ mạch giảng và nguồn |
| Trung bình | Nhãn SVG pha tiếng Anh | Việt hóa toàn bộ thành nhân, vùng đệm, bước trượt và độ lệch trong nhãn lẫn mô tả |
| Trung bình | Ví dụ nhiều kênh chỉ ghi vùng đệm và bước trượt trong ghi chú | Đưa $P_t=P_b=P_l=P_r=0$ và $S_h=S_w=1$ lên mặt L04-24 để ví dụ tự đủ dữ kiện |

## Thay đổi mạch cục bộ

- L04-08–15: vấn đề cửa sổ → trực giác không lật → ví dụ $X,K$ → tính 19 và đủ $Y$ → công thức → kiểm tra và đối chiếu API.
- L04-23–28: nhu cầu gom kênh và $\widetilde X$ → ví dụ đủ dữ kiện → kiểm tra kết quả → tensor $W$ nhiều kênh ra → tham số và MAC.
- L04-33–37: định nghĩa theo tầng tham chiếu → truy hồi → ví dụ bước trượt 1 → kiểm tra bước trượt 2 → triển khai thân mạng có kích hoạt.
- Không đổi số trang hoặc mã trang; đã rà hai trang lân cận ở mỗi biên cụm và bổ sung câu chuyển tại L04-07, L04-15, L04-28, L04-32.

## Đề xuất không áp dụng

- Không thêm trang riêng cho độ giãn, tích chập theo nhóm hoặc tích chập riêng từng kênh: ngoài phạm vi và nguồn đã khóa.
- Không thêm mã API: nguồn không có mã và đề bài không yêu cầu trình diễn.
- Không dạy lịch sử hoặc kết quả định lượng LeNet: L04-X04 chỉ dùng cấu hình trong giáo trình để luyện kích thước.
- Không đổi MAC thành FLOPs: thiếu quy ước một MAC được tính là một hay hai phép toán.
- Không thêm nhãn “SAME” tổng quát: phát biểu hiện tại chỉ chứng minh điều kiện giữ kích thước khi bước trượt bằng 1.

## Ví dụ đã tính lại

- Một kênh: $X=[[0,1,2],[3,4,5],[6,7,8]]$, $K=[[0,1],[2,3]]$ cho $Y=[[19,25],[37,43]]$.
- Nhiều kênh theo GT PDF 125: $Y_{0,0,:,:}=[[56,72],[104,120]]$.
- Kích thước: $X:2×3×6×7$, $C_{out}=4$, $K=3$, đệm 1, bước trượt 2 cho $Y:2×4×3×4$.
- Nhiều kênh: hai đóng góp ở ô trên trái là 37 và 19, cộng $b_0=0$ cho 56; các ô còn lại là 72, 104, 120.
- Tham số: $4(3·3·3+1)=112$.
- MAC: mỗi mẫu $3·4·4·3·3·3=1296$; cả lô $2592$.
- Phép gộp: max $[[6,8],[3,4]]$; trung bình $[[3.25,5.25],[2,2]]$.

## Biên tập

- Đã áp dụng no-ai-slop/eval: bỏ khẩu hiệu, câu hỏi tu từ, nhận định quảng bá và kết luận vượt nguồn.
- Đã rà mạch theo nguyên tắc Quill: mỗi cụm có vấn đề, trực giác, ví dụ, hình thức, triển khai và kiểm tra; dữ kiện được truyền từ ví dụ kích thước sang tham số và MAC. Không tạo `quill.json`.
- Các báo cáo phản biện độc lập do điều phối viên quản lý; nhật ký này ghi các quyết định hợp nhất được giao cho vòng chỉnh sửa.

## Kiểm định cuối

- 44 mã trang duy nhất, 44 khối ghi chú và 4 hiệu ứng xuất hiện; cấu trúc section cân bằng.
- 127 biểu thức dựng bằng KaTeX với `throwOnError: true`, `strict: "error"`; không có lỗi.
- 14 SVG phân tích XML thành công, có `role="img"`, `title`, `desc`; không có raster, tài nguyên từ xa hoặc đường dẫn thiếu.
- URL `http://localhost:8765/2627-1/lecture-04-mang-no-ron-tich-chap.html` trả HTTP 200 và nội dung khớp tệp trong kho.
- Môi trường không có mô-đun `reloadserver`, Chromium, Playwright hoặc Codex Browser. Đã dùng máy chủ HTTP đang chạy ở cổng 8765 để kiểm tra phục vụ tệp; chưa thể rà trực quan từng trang, tràn chữ hoặc màn hình hẹp bằng trình duyệt và không tuyên bố đã làm bước đó.
