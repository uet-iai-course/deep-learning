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

## Báo cáo lịch sử và vòng hiện hành

Các mục “Sửa và làm rõ” và “Quyết định sau phản biện” ở trên là báo cáo lịch sử của các vòng rà trước, giữ nguyên để truy vết. Vòng hiện hành là mục “Tái cấu trúc bảy mạch” dưới đây.

## Tái cấu trúc bảy mạch (vòng hiện hành)

- Số mạch ngoài đổi từ 9 thành 7 theo yêu cầu cấu trúc: [L04-00–07], [08–15], [16–28], [29–32], [33–37], [X01–X05], [38]. Không đổi ID, giữ đủ 44 mã trang và 44 ghi chú; tuyến lõi 100 phút, mở rộng 20 phút, bài tập 50 phút riêng.
- L04-38 tách thành mạch kết luận độc lập, là trang cuối deck; mạch mở rộng X01–X05 đặt trước kết luận.
- Câu nối đã sửa cho cấu trúc mới: ranh giới 03→04 nay trong mạch 1; 15→16 giữa mạch 2–3; 22→23 trong mạch 3; 28→29 giữa mạch 3–4; 32→33 giữa mạch 4–5. L04-37 nối trường tiếp nhận sang thân–đầu mạng; X01–X05 nối các biến thể mở rộng; L04-38 thu hồi vấn đề mở đầu và bốn phép kiểm. Đã rà hai trang lân cận mỗi biên; luận điểm nguồn không đổi vì câu nối cục bộ đủ.
- Điều hướng: tuyến lõi tại L04-37 bấm End tới L04-38; tuyến đầy đủ từ L04-37 nhấn phải tới X01, nhấn xuống qua X02–X05, rồi nhấn phải tới L04-38. Chỉ dẫn điều hướng và timing chỉ nằm trong planning, không lên mặt slide hay notes.

## Năm báo cáo độc lập trên bản bảy mạch (vòng hiện hành)

Năm vai rà soát độc lập đã chạy trên bản bảy mạch. Phát hiện trùng được hợp nhất nhưng mỗi vai vẫn được nêu riêng.

| Vai | Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|---|
| Góc nhìn sinh viên | Trung bình | L04-02, L04-23, L04-24, L04-31 | Thiếu phản hồi cho một câu hỏi; hai trang nhiều kênh dày; kết quả gộp trung bình xuất hiện trước câu hỏi | L04-02 chưa có đáp án; L04-23 có hình và hai công thức; L04-24 có bốn ma trận; L04-31 đặt kết quả trước câu hỏi | Thêm fragment L04-02; giảm tải L04-23–24; đặt câu hỏi trước fragment L04-31 |
| Chuyên gia Học sâu | Trung bình | Bài tập 50 phút, L04-13, L04-27, L04-X05, L04-38 | Báo cáo nghi ngờ shape bài tập; một số nhãn/ghi chú mơ hồ; kết luận quá ngắn | Báo cáo đọc $X$ không theo NCHW; nhãn $b$ và câu bỏ độ lệch chưa rõ; L04-38 chỉ 1 phút | Bác phép tính sai; làm rõ $b$, độ lệch và bộ tối ưu; nâng kết luận lên 3 phút |
| Độ chính xác toán học, thuật toán và triển khai | Nghiêm trọng | Bài tập 50 phút | Báo cáo đề xuất đổi đáp án do đọc nhầm trục NCHW | Với $X:8×16×32×35$, báo cáo dùng $H_{in}=16$ thay vì 32 | Bác đề xuất; giữ $H_{out}=16$, $W_{out}=35$ và ghi phép tính đầy đủ |
| Phản biện học thuật và giảng dạy | Trung bình | L04-09, L04-16, L04-23–24, L04-27–28, storyboard | Công thức xuất hiện sớm; cụm kích thước thiếu câu vấn đề; trang nhiều kênh dày; nhãn chu trình lệch vai trò | L04-09 có công thức trước ví dụ; L04-16 chỉ khóa trục; L04-23 có hình và hai công thức; planning gán sai vai một số trang | Đưa trực giác lên L04-09, thêm vấn đề L04-16, giảm tải L04-23–24, sửa nhãn storyboard |
| Kết nối và mạch viết | Trung bình | L04-37–38, L04-X01–X05, storyboard | Notes chứa nhãn nội bộ/đáp án; mạch mở rộng thiếu câu nối; vai trò planning chưa khớp | L04-37 nhắc tuyến; L04-38 chứa đáp án bốn phép kiểm; X01–X05 nối như danh mục | Chuyển nội bộ/đáp án sang note-for-author; thêm câu nối; đồng bộ vai trò và kết nối |

### Quyết định đã áp dụng

- L04-23: thêm câu trực giác $\\widetilde X$ trên mặt trang; giữ cases chi tiết trong notes.
- L04-X01: khôi phục note-source giáo trình PDF 116–119; X01–X05 đều có câu nối và note-source.
- Timing: L04-38 = 3 phút; L04-17 và L04-21 mỗi trang rút còn 2 phút; mạch 3 = 34 phút; lõi 100, mở rộng 20, đầy đủ 120.
- Nhãn storyboard: L04-01 mục tiêu/quy ước; chu trình kích thước L04-16→17–18→19→20→21→22; L04-14 kiểm tra cơ chế; L04-20 ví dụ/tính toán; L04-27–28 tính toán/ứng dụng chi phí; L04-37 cầu nối ứng dụng thân–đầu; cụm nhiều kênh ghi rõ L04-25 kiểm tra ví dụ trước L04-26.
- note-for-author: thêm đáp án L04-02 và bốn phép kiểm L04-38.

### Quyết định bác hai đề xuất tính sai do đọc nhầm NCHW

- Hai đề xuất đổi đáp án bài tập kích thước bị bác vì đọc nhầm trục. Theo NCHW, $X:8×16×32×35$ nghĩa là $N=8$, $C_{in}=16$, $H_{in}=32$, $W_{in}=35$. Do đó $H_{out}=\\lfloor(32+1+1-3)/2\\rfloor+1=16$, $W_{out}=\\lfloor(35+2+2-5)/1\\rfloor+1=35$, $Y=8×24×16×35$, tham số $24(16·3·5+1)=5784$. Đáp án trong note-for-author giữ nguyên.
- Đề xuất nghi ngờ avg pool bị bác: tính lại từ ma trận slide cho $[[3.25,5.25],[2,2]]$ đúng; giữ nguyên L04-30/L04-31.

### Trạng thái sau chỉnh sửa

- Đã áp dụng các sửa, hoàn tất tái kiểm toán học và mạch viết; bằng chứng trình duyệt và kiểm định cuối nằm ở mục cuối tệp.

## Dấu vết nguồn bổ sung (vòng hiện hành)

- Ví dụ tương quan chéo S8–16 của slide được thay bằng ví dụ một kênh từ GT PDF 116–119 vì nhỏ, đủ dữ kiện và kiểm tra được.
- Công thức trường tiếp nhận stride-2 ở slide PDF 50 sai/không tổng quát; thay bằng truy hồi $r,j$ đã kiểm chứng.
- Slide S29 dùng ký hiệu $K,L$; deck đổi sang $C_{in},C_{out}$ và dùng MAC, không quy đổi FLOPs.
- Không dùng ví dụ học nhân GT 4.2.3 vì nguồn chính đã đủ trực giác và không cần mở thí nghiệm học nhân.

## Quyết định bác đề xuất sai về gộp trung bình (vòng hiện hành)

- Báo cáo phân tích nguồn đã nhầm cách chia cửa sổ khi tính avg pool. Tính lại từ ma trận hiển thị $X=[[1,1,2,4],[5,6,7,8],[3,2,1,0],[1,2,3,4]]$ với cửa sổ $2\times2$, bước trượt 2: hai cửa sổ dưới là $\{3,2,1,2\}$ và $\{1,0,3,4\}$, cho trung bình $2$ và $2$. Kết quả đúng là $[[3.25,5.25],[2,2]]$; đề xuất sửa khác bị bác. Giữ nguyên max pool $[[6,8],[3,4]]$ và giữ nguyên L04-30/L04-31.

## Thay đổi mạch cục bộ

- L04-08–15: vấn đề cửa sổ → trực giác không lật → ví dụ $X,K$ → tính 19 và đủ $Y$ → công thức → kiểm tra và đối chiếu API.
- L04-23–28: nhu cầu gom kênh và $\widetilde X$ → ví dụ đủ dữ kiện → kiểm tra kết quả → tensor $W$ nhiều kênh ra → tham số và MAC.
- L04-33–37: định nghĩa theo tầng tham chiếu → truy hồi → ví dụ bước trượt 1 → kiểm tra bước trượt 2 → triển khai thân mạng có kích hoạt.
- Đã rà hai trang lân cận ở mỗi biên cụm và bổ sung câu chuyển tại L04-07, L04-15, L04-28, L04-32.

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
- Phép gộp: max $[[6,8],[3,4]]$; trung bình $[[3.25,5.25],[2,2]]$ (hai cửa sổ dưới là $\{3,2,1,2\}$ và $\{1,0,3,4\}$).

## Biên tập

- Đã áp dụng no-ai-slop/eval: bỏ khẩu hiệu, câu hỏi tu từ, nhận định quảng bá và kết luận vượt nguồn.
- Đã rà mạch theo nguyên tắc Quill: mỗi cụm có vấn đề, trực giác, ví dụ, hình thức, triển khai và kiểm tra; dữ kiện được truyền từ ví dụ kích thước sang tham số và MAC. Không tạo `quill.json`.
- Các báo cáo phản biện độc lập do điều phối viên quản lý; nhật ký này ghi các quyết định hợp nhất được giao cho vòng chỉnh sửa.

## Kiểm định cuối

- **ĐẠT** kiểm tra tĩnh: đúng 7 `<section>` ngoài với kích thước stack `[8,8,13,4,5,5,1]`; 44 mã `data-slide-id` duy nhất; 44 khối ghi chú; 44 khối nguồn ghi chú; 8 hiệu ứng xuất hiện.
- **ĐẠT** tái kiểm toán toán học bằng worker `z-ai/glm-5.3-flash`: công thức và ví dụ shape, NCHW/OIHW, tương quan chéo, tham số, MAC, gộp, gradient và trường tiếp nhận đều đúng. Bài tập `8×16×32×35 → 8×24×16×35` và gộp trung bình `[[3.25,5.25],[2,2]]` được xác nhận lại độc lập.
- **ĐẠT** tái kiểm mạch viết bằng worker `z-ai/glm-5.3-flash`: cấu trúc stack dọc của RevealJS hỗ trợ tuyến phải → xuống → phải; đủ vai trò, kết nối vào và kết nối ra cho bảy mạch; timing lõi 100 phút và mở rộng 20 phút nhất quán.
- **ĐẠT** KaTeX: Chromium dựng toàn bộ deck với `throwOnError: true`, `strict: "error"`; DOM không có `katex-error`, `ParseError`, `Uncaught` hoặc tài nguyên không tìm thấy.
- **ĐẠT** tài sản: 14 SVG phân tích XML thành công và đều có `role="img"`, `title`, `desc`; 24 tham chiếu cục bộ đều tồn tại; không có raster hoặc tài nguyên từ xa.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Dùng phương án an toàn `python3 -m http.server 8765` chỉ trong thư mục `2627-1/`; URL `http://127.0.0.1:8765/lecture-04-mang-no-ron-tich-chap.html` trả HTTP 200.
- **ĐẠT** rà trực quan: chụp đủ 44 trang ở 1280×720 và 44 trang ở 960×720. Hai lỗi phát hiện được sửa cục bộ: L04-24 đổi từ bốn cột sang hai thẻ theo kênh để bỏ tràn ngang; L04-37 rút câu và giảm hình để hộp cuối không bị cắt. Hai trang đã được chụp lại ở cả hai kích thước và không còn tràn, chồng lấn hoặc chữ bị cắt.
- **ĐẠT** tiêu đề: đã xuất và rà thủ công toàn bộ `h1`, `h2`, `h3`; chỉ giữ các ký hiệu hoặc tên chuẩn cần thiết như MLP, NCHW, MAC và LeNet.
- `2627-1/index.html` đã có liên kết đúng tới deck Bài 04; không cần sửa.

## Bổ sung lecture note và giới hạn DeepSeek (2026-09-03)

### Dossier và tác tử

- Tài liệu nhị phân được trích cục bộ thành UTF-8 theo đúng allowlist: đề cương III.2 → Buổi 4; `lec08_cnn.pdf` PDF 3–29, 38–42, 44–50, 52–53; `hocsau_draft.pdf` PDF 110–135. Không gửi `.env`, bí mật hoặc trang ngoài dải lên OpenRouter.
- Vai lập kế hoạch và ba vai phân tích nguồn chạy bằng `z-ai/glm-5.3-flash`; runtime xác nhận `requested_model = observed_model = z-ai/glm-5.3-flash`, provider `OpenRouter`.
- DeepSeek writer chạy bằng `deepseek/deepseek-v4-flash-0731`; runtime xác nhận model yêu cầu và model thực tế trùng nhau, provider `OpenRouter`.

### Sự cố và checkpoint

- Lượt soạn toàn tệp đầu tiên ghi đúng một lần nhưng làm hỏng Unicode tiếng Việt, KaTeX và hai đường dẫn SVG ở nửa sau tệp. Toàn bộ đầu ra bị loại; checkpoint khôi phục là đặc tả duyệt và mẫu note.
- Lượt thử lại trong staging mới gọi ghi toàn tệp hai lần. Toàn bộ đầu ra bị loại dù lần cuối đọc được; không vá nối tiếp trên sản phẩm vi phạm phạm vi.
- Cầu nối OpenRouter được bổ sung chính sách `MCP_WRITE_POLICY=create-once`: không ghi đè tệp đã tồn tại, vô hiệu hóa `replace_text_file` và kết thúc worker ngay sau lần ghi thành công đầu tiên. Bộ 15 kiểm thử của `openrouter-mcp` đạt.
- Một bản dài 14,8 KB dùng `create-once` vẫn trộn ký tự Cyrillic vào tiếng Việt ở nửa sau và bị loại toàn bộ. Fallback được khóa cho các buổi sau: không thử lại toàn bản quá một lần; chuyển sang các mảnh tuần tự trong staging mới, mỗi mảnh mặc định không quá 2.500 ký tự và vẫn dùng `create-once`.
- Mảnh Cụm 1–2 và các mảnh Cụm 3, 4, 5, 6, 7, phần triển khai–tự kiểm–nguồn được kiểm riêng về UTF-8, ký tự thay thế, ký tự Cyrillic, KaTeX và đường dẫn trước khi hợp nhất. Một mảnh Cụm 3–4 dài bị hỏng đã bị loại toàn bộ.

### Năm vai rà soát lecture note

- Năm vai bắt buộc chạy độc lập bằng `z-ai/glm-5.3-flash`: góc nhìn sinh viên, chuyên gia Học sâu, chính xác toán–tensor–triển khai, phản biện học thuật–giảng dạy và kết nối–mạch viết. Cả năm runtime đều xác nhận đúng model và provider OpenRouter.
- Các sửa đã áp dụng: nêu rõ $C_{in}=1$ trong ví dụ đầu; thêm kích thước đầy đủ cho ví dụ hai kênh; nêu miền $i,j$; giải nghĩa logit; bổ sung câu nối giữa các cụm; thêm câu hỏi trực tiếp về NCHW/OIHW; thu hồi vấn đề làm phẳng ở kết luận; bỏ bình luận về quy trình chọn nguồn khỏi note công khai.
- Báo cáo mạch gắn mức `nghiêm trọng` cho timing nhưng phép cộng của báo cáo sai. Mạch 3 đúng là $2+2+2+3+4+2+1+6\cdot3=34$ phút; lõi vẫn $20+20+34+11+12+3=100$ phút. Đề xuất đổi timing bị bác và lý do được ghi tại đây.
- Nhãn chu trình trường tiếp nhận trong storyboard được sửa thành `hình thức/kiểm tra L04-36 → triển khai L04-37`, loại cách ghi quay ngược L04-36 sau L04-37.

### Biên tập bản cuối

- `$no-ai-slop`: bỏ nhãn quy trình thừa trong note, câu tuyệt đối, bình luận về nguồn, lời nhắc thao tác và chỉ dẫn diễn giả trong deck; giữ câu ngắn, thuật ngữ Việt nhất quán và các nguồn bắt buộc.
- `$quill`: bảy cụm giữ một xương sống tích lũy từ hạn chế của MLP đến phép tính một kênh, hình học, nhiều kênh, gộp, trường tiếp nhận và mạng hoàn chỉnh; các câu nối đã được bổ sung tại ranh giới cụm.
- Deck được rà lại riêng: các câu `dừng`, `hiện đáp án`, `cho người học`, `nhắc cấu hình` đã được thay bằng nội dung giải thích hoặc dữ kiện; chỉ dẫn điều hướng và đáp án chi tiết tiếp tục chỉ nằm trong `note-for-author.md`.

### Kiểm định lecture note và vòng rà deck hiện hành

- Lecture note có một tiêu đề cấp một, 30 cặp vùng mở rộng, 158 biểu thức KaTeX và 14 hình. Toàn bộ biểu thức dựng được với `throwOnError: true`, `strict: "error"`; mọi SVG tồn tại và có `role="img"`, `title`, `desc`.
- Material viewer hiển thị đúng tiêu đề, mục lục, liên kết deck, 14 vùng mở rộng và 14 hình ở khung rộng lẫn hẹp. Các hình dùng tải lười nên phép thử buộc tải trước khi kết luận; sau khi tải, không có ảnh hỏng, lỗi console, lỗi trang hoặc lỗi yêu cầu. Trang từ chối đường dẫn vượt thư mục và trường hợp note/deck khác buổi.
- Ở khung hẹp, tài liệu không cuộn ngang ở cấp trang. Hình kỹ thuật rộng và công thức khối được phép cuộn trong phần tử chứa riêng; phép thử thay đổi `window.scrollX` xác nhận viewport không dịch ngang.
- Deck hiện hành có 7 mạch ngoài, 44 mã trang duy nhất, 44 ghi chú, 147 biểu thức KaTeX và 14 SVG. Kiểm tra tĩnh không phát hiện raster, phụ thuộc mạng cốt lõi, đường dẫn thiếu hoặc dấu vết quy trình trong nội dung công khai.
- Chromium duyệt đủ 44 trang ở 1280×720 và 800×600: không tràn, không chồng lấn, không lỗi tải/chạy; phím xuống, lên và phải lần lượt đi đúng stack RevealJS.
- Lệnh `python3 -m reloadserver 8765` vẫn không dùng được vì môi trường thiếu mô-đun. Vòng này dùng máy chủ cục bộ sẵn có tại cổng 8766 và xác nhận HTTP 200.
- Bề mặt Codex Slides không được cung cấp trong phiên làm việc. Kiểm định trực quan dùng Chromium cục bộ; đây là giới hạn công cụ, không được ghi thành đã kiểm bằng Codex Slides.
- Rà cuối theo `no-ai-slop/eval.md` đã bỏ trạng thái nội bộ như “đã tính lại”, câu nhắc thao tác và đối lập khuôn mẫu khỏi ghi chú diễn giả. Rà mạch theo Quill giữ bảy cụm và thuật ngữ NCHW/OIHW nhất quán; không tạo `quill.json`.

## Đồng bộ deck từ lecture note đã commit

- Pha B chỉ bắt đầu sau khi commit lecture note `29b0d9d` xuất hiện trên `origin/main`. Baseline hẹp gồm note đã commit, deck và bốn tệp planning; không có `.env`, bí mật hoặc symlink.
- Ba vai đọc đầu pha dùng `z-ai/glm-5.3-flash`. Các lượt được nhận đều có `requested_model = observed_model = z-ai/glm-5.3-flash`, `provider = OpenRouter`. Kết luận: mọi `note-topic-id` cốt lõi và mở rộng đã có `data-slide-id`; checklist API và tự kiểm sâu tiếp tục ở note, không đưa thêm lên slide.
- Một báo cáo toán đọc sai NCHW của $X:8×16×32×35$, dùng 16 làm chiều cao và đề xuất $H_{out}=8$. Đề xuất bị bác: NCHW cho $N=8$, $C=16$, $H=32$, $W=35$, nên $H_{out}=16$ và đáp án hiện có đúng. Lượt kiểm toán độc lập sau đó xác nhận lại kết quả này.
- DeepSeek writer nhận đúng một `approved-spec.md`, dùng `MCP_WRITE_POLICY=create-once` và chỉ tạo `deck-delta.md`. Runtime xác nhận `requested_model = observed_model = deepseek/deepseek-v4-flash-0731`, `provider = OpenRouter`. Writer trả nguồn dưới dạng danh sách Markdown; Codex không chèn nguyên văn vào HTML mà chuẩn hóa thành dòng nguồn cục bộ hợp lệ ở L04-31.
- Năm vai review deck đã chạy bằng GLM. Lượt góc nhìn sinh viên đầu vượt giới hạn sáu tool-call nên bị loại toàn bộ; task thay thế chỉ đọc deck và storyboard, hoàn tất đúng model/provider. Bốn vai còn lại hoàn tất ngay lượt đầu. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
- Sửa cục bộ đã áp dụng: nguồn L04-31 nêu riêng slide PDF 39–41 và giáo trình PDF 129–130; OIHW dùng “chiều cao nhân–chiều rộng nhân”; ghi chú L04-X05 và L04-38 bỏ nhãn tiến trình; storyboard đổi câu nối mạch 1 thành phát biểu khớp ghi chú diễn giả.
- Các đề xuất mở rộng bằng ví dụ gộp trong truy hồi trường tiếp nhận, loss/log-sum-exp, công thức gộp có đệm hoặc trang đáp án API không áp dụng vì ngoài delta deck đã duyệt, hoặc đã có câu trả lời trong ghi chú diễn giả/tài liệu tự học. Cỡ chữ L04-38 giữ nguyên vì kiểm định trình duyệt ở cả hai khung không phát hiện tràn và cỡ hiệu dụng vẫn đạt ngưỡng đã khóa.
