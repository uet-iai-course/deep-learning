# Nhật ký rà soát Bài 06

## Quyết định nội dung

| Quyết định | Lý do và truy nguyên |
|---|---|
| Giữ mạch Stanford 63–70 làm xương sống | Đúng `source.md`: dữ liệu chưa nhãn → mã hóa → giải mã → mất mát → tác vụ đích → giới hạn lấy mẫu. |
| Thêm nghiệm đồng nhất, mã thấp chiều, mã thưa và khử nhiễu | Illinois 5–13 và CMU Autoencoders 3–7 khôi phục điều kiện để hiểu vì sao tái tạo đơn thuần chưa đủ. |
| Viết rõ SSE và MSE | Stanford 66 viết mất mát L2; deck phân biệt bình phương chuẩn L2 là tổng và MSE là trung bình để tránh sai hệ số. Ví dụ được tự tính: $0.01+0.04+0.09+0.04=0.18$, $0.18/4=0.045$. |
| Dùng MLP $784\to256\to d\to256\to784$ | Kiến trúc minh họa giúp khóa kích thước; Stanford 64 cho phép nhiều họ bộ mã hóa. Không trình bày đây là cấu hình chuẩn hoặc tối ưu. |
| Khóa NCHW và phép làm phẳng | GT 38–40 xác nhận MNIST 28×28; chi tiết trục được thêm để tránh trộn trục lô. |
| Nêu nút thắt “khuyến khích”, không “bảo đảm” | CMU Autoencoders 3–5 cảnh báo nghiệm vô ích; mạng phi tuyến vẫn có thể ghi nhớ tập hữu hạn. |
| Tách phạt mềm khỏi top-$k$ cứng | CMU 6 dùng $L+\Omega(h)$; Illinois 11 cho top-$k$. Deck dùng $\|Z\|_1/(Nd)$ làm ví dụ phạt mềm với phép rút gọn đã khóa; top-$k$ tính riêng trên hoạt hóa ReLU của từng mẫu. |
| Khử nhiễu so với mục tiêu sạch | CMU Autoencoders 7; công thức thêm ký hiệu $q(\widetilde X\mid X)$ chỉ để xác định cơ chế nhiễu, không khẳng định mô hình sinh. |
| Tách “tham số được cập nhật” khỏi “chế độ huấn luyện/đánh giá” | Cần cho triển khai đóng băng/tinh chỉnh và tránh lỗi với dropout/BatchNorm; nguồn chuyển giao là `lec09_cnn_architectures.pdf` 44–46. |
| Giữ giới hạn lấy mẫu, không mở sang mô hình sinh khác | Stanford 68–70 chỉ ra mã tùy ý có thể không hợp lệ. Đúng cảnh báo phạm vi của `source.md`. |
| Không có code demo | DOCX có hoạt động thực hành, nhưng chỉ dẫn cụ thể của người dùng khóa “không code demo”; bài tập giấy vẫn đủ 50 phút. |
| Không dùng Illinois 14 | LSTM autoencoder không cần cho LLO và làm lệch mạch. |

## Kiểm tra toán học và triển khai

- Kích thước: $N\times1\times28\times28\to N\times784\to N\times256\to N\times d\to N\times256\to N\times784\to N\times1\times28\times28$.
- Với mẫu dạng hàng: $W_{e1}:784\times256$, $W_{e2}:256\times d$, $W_{d1}:d\times256$, $W_{d2}:256\times784$; độ lệch phát theo trục lô. Với $d=32$, tổng tham số có độ lệch là $419120$.
- MSE lô lấy trung bình trên $N\times D$, không gọi SSE là MSE.
- Khử nhiễu: đầu vào $\widetilde X$, mục tiêu $X$ sạch, cùng kích thước.
- Đóng băng: dùng `stopgrad`, $\Delta\theta=0$ và không đưa $\theta$ vào bộ tối ưu; chế độ mô-đun là quyết định độc lập. Logit có kích thước $N\times C$, softmax theo trục lớp và mất mát lấy trung bình theo lô.
- Autoencoder xác định thông thường không cho phép tự giả sử $z\sim\mathcal N(0,I)$.

## Biên tập và khả năng đọc

- Nội dung hiển thị và ghi chú đã rà theo tiêu chí no-ai-slop: bỏ câu hỏi tu từ, khẩu hiệu, cụm kết luận mơ hồ và nhịp ba vế trang trí.
- Quill được dùng để rà thứ tự khái niệm, dữ kiện xuyên suốt, thuật ngữ và câu nối; không tạo `quill.json`.
- Tất cả hình là SVG có `role="img"`, `title`, `desc`; không dùng màu làm tín hiệu duy nhất.
- Mọi chỉ dẫn tuyến giảng, thời lượng, đáp án và phạm vi nằm trong `note-for-author.md`, không đưa vào ghi chú diễn giả.

## Sai khác có chủ ý và đề xuất không áp dụng

- Không chuyển nguyên văn bố cục hoặc hình từ PDF; vẽ lại sơ đồ bằng SVG và Việt hóa nhãn.
- Không dùng kết quả thực nghiệm hoặc benchmark vì các nguồn trong dải duyệt không khóa giao thức đủ chi tiết cho deck này.
- Không tuyên bố mã tiềm ẩn có khả năng diễn giải, bất biến hoặc công bằng; CMU chỉ nêu đây là mong muốn/câu hỏi đánh giá.
- Không đưa phần ngoài phạm vi đã khóa, kể cả các biến thể sinh mẫu hoặc kiến trúc chuỗi.

## Hợp nhất báo cáo độc lập và chỉnh sửa

| Góc rà soát | Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|---|
| Sinh viên | nghiêm trọng | L06-07–15, L06-22–27 | Dữ kiện mẫu/lô và kiến trúc đổi giữa hình, công thức và bài tập; ví dụ thưa không khớp | Hai lớp trong công thức nhưng bốn lớp trên sơ đồ; HTML nói $d=6,k=3$ nhưng SVG nói $d=8,k=2$ | Khóa một chuỗi tensor, đưa ví dụ trước tổng quát, đồng bộ top-$k$ và thêm kiểm tra khử nhiễu. |
| Chuyên gia Học sâu | nghiêm trọng | L06-29–35 | Giao thức chuyển giao và giới hạn lấy mẫu bị diễn đạt quá mạnh | Đóng băng được viết thành gradient bằng 0; bộ giải mã được nói là huấn luyện “gần” mã | Tách cập nhật khỏi chế độ mô-đun; mô tả đúng các điểm mà mất mát được đánh giá và vùng hỗ trợ. |
| Toán học, thuật toán và triển khai | chặn bàn giao | L06-09–10, L06-22–31 | Sai hợp đồng bốn lớp, phép rút gọn thưa chưa khóa, objective khử nhiễu thiếu kỳ vọng | Không thể tái lập số tham số và thang $\lambda$; $\nabla_\theta L=0$ không định nghĩa đóng băng | Viết đủ bốn ma trận, khóa $\Omega/(Nd)$, dùng ước lượng Monte Carlo và `stopgrad`/$\Delta\theta=0$. |
| Học thuật và giảng dạy | nghiêm trọng | L06-11–15, L06-X01–X03 | Thứ tự khái niệm và các trang mở rộng chưa tạo bước tiến | Công thức đến trước ví dụ; X01 hỏi về tuyến tính nhưng hình là phép chia; X03 lặp lõi | Đổi thành vấn đề → ví dụ → hình thức; tính $35=\mathrm{XXXV}$; dùng X03 phân biệt $d,k,\Omega$ và vùng hoạt động. |

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| chặn bàn giao | L06-08–10, bài tập | Công thức và bài tập chỉ dùng hai lớp, trái kiến trúc MLP đã chọn | Sơ đồ nguồn của deck là $784\to256\to d\to256\to784$ | Đã khóa bốn lớp ở HTML, SVG và planning; tự tính lại $419120$ tham số khi $d=32$. |
| nghiêm trọng | L06-22–27 | Phạt mềm và top-$k$ bị trộn; ví dụ, alt và SVG không khớp; thiếu kiểm tra khử nhiễu | HTML nói $d=6,k=3$ nhưng SVG là $d=8,k=2$ | Đã thống nhất $d=8,k=2$; tách $\Omega$ trung bình và top-$k$ cứng theo mẫu; thêm quy tắc gradient/hòa và câu hỏi đích sạch. |
| nghiêm trọng | L06-29–33 | $\nabla_\theta L=0$ không phải định nghĩa đóng băng; bảng trộn gradient với cập nhật và chế độ | Một gradient có thể khác 0 dù tham số không thuộc bộ tối ưu | Đã dùng `stopgrad`, $\Delta\theta=0$; thêm hợp đồng $Z$, logit, trục softmax, phép rút gọn và chế độ từng mô-đun. |
| nghiêm trọng | Bài tập | Phân bổ không khớp `source.md`; bài lấy mẫu thay phần nút thắt | Bản cũ có 5 phút phản biện sampling | Đã đổi đúng 10/15/10/10/5 phút: kích thước, loss, đồng nhất+nút thắt, chọn biến thể, tác vụ đích. |
| trung bình | L06-11–15, L06-21–27 | Hình thức xuất hiện trước ví dụ và dữ kiện mẫu/lô chưa nối rõ | $D=4$ chưa được gọi là ví dụ thu nhỏ | Đã chuyển L06-11 thành vấn đề, L06-12 thành ví dụ, L06-13 tổng quát; storyboard khóa $D=4\to784$ và $X/x^{(n)}$. |
| trung bình | L06-34–35 | “Huấn luyện gần mã” và “mọi nội suy là ngoại suy” quá mạnh | Mất mát chỉ được đánh giá tại các mã phát ra; đoạn nối có thể qua vùng mật độ thấp | Đã diễn đạt theo điểm huấn luyện, vùng hỗ trợ và phân biệt nội suy tọa độ với ngoại suy ngoài hỗ trợ. |
| trung bình | L06-X01–X03 | X01 không khớp phép chia; X02 thiếu giả thiết; X03 lặp lõi | SVG dùng $210/6$; định lý PCA cần dữ liệu định tâm và nghiệm tối ưu | Đã thêm phép tính $35=\mathrm{XXXV}$, khóa giả thiết PCA và tính không duy nhất, đổi X03 sang so sánh $d,k,\Omega$ và vùng hoạt động. |
| nhẹ | L06-X05 | Hạt giống và đánh giá sai lệch chưa được nguồn khóa đủ chi tiết | Dải nguồn chỉ hỗ trợ giao thức và tính hữu ích phụ thuộc tác vụ | Không giữ các tuyên bố đó; thay bằng ba phần dữ liệu tách biệt và chỉ số gắn với tác vụ. |

Rà lại sau đổi cấu trúc đã bao phủ các cụm bị ảnh hưởng và hai trang lân cận: L06-07–15, L06-20–29, L06-27–35, L06-X01–X05. Không đổi số lượng hoặc thứ tự 44 trang; tuyến lõi vẫn 100 phút và tuyến mở rộng 20 phút.

## Hậu kiểm cục bộ cuối

- L06-25 và bảng ký hiệu không còn giả sử nhiễu giữ miền $[0,1]$: $X$ sạch thuộc $[0,1]^{N\times784}$, còn $\widetilde X\in\mathbb R^{N\times784}$ vì nguồn không khóa phép cắt miền.
- L06-29 dùng chéo entropy hợp nhất trực tiếp từ logit với phép log-softmax ổn định; không hướng dẫn tính softmax rồi lấy log thủ công.
- L06-30 ghi rõ chi phí tinh chỉnh đến từ lan truyền ngược qua bộ mã hóa, lưu hoạt hóa và trạng thái bộ tối ưu.
- Bài tập kích thước giữ sản phẩm bắt buộc đúng `source.md`: hoàn thiện sơ đồ bộ mã hóa–mã tiềm ẩn–bộ giải mã và toàn bộ kích thước trong 10 phút; đếm tham số chỉ là phần tùy chọn.
- L06-22 định nghĩa $\lambda$ là hệ số phạt trước khi L06-26 dùng công thức. Storyboard coi X01 là kiểm tra mở rộng và X05 là ứng dụng/tổng kết.

## Kiểm định cuối

- 44 trang, 44 `data-slide-id` duy nhất, 44 khối ghi chú, 8 đáp án dùng fragment; cấu trúc 9 nhóm ngoài và 44 trang trong cân bằng thẻ.
- KaTeX strict: 117 biểu thức, 0 lỗi (`throwOnError: true`, `strict: "error"`).
- Tài nguyên: 0 đường dẫn thiếu; 15/15 SVG được HTML tham chiếu, 0 tài sản thừa.
- SVG XML: 15/15 phân tích được; mỗi tệp có `role="img"`, `title` và `desc`; nhãn nhỏ nhất 22 px.
- Rà trực quan SVG: đã dựng montage cục bộ cho tám hình bị tác động; sửa glyph mũ/ngã không ổn định, nhãn đầu ra bị cắt và nhãn trục bị chồng. Không phát hiện lỗi còn lại trong các hình đã dựng.
- Storyboard: 44 dòng; tuyến lõi 100 phút, tuyến mở rộng 20 phút; bài tập riêng 50 phút.
- Máy chủ: `reloadserver` không có trong môi trường. Cổng 8765 đã có máy chủ; HTML và 15/15 SVG trả HTTP 200, SHA-256 HTML được phục vụ khớp tệp trong kho (`a3611572402557f6b429b0a9b11dbe9155c1243bcc447218affa2c570ab7f3a2`).
- Không có Browser/Chromium/Playwright hoặc công cụ Codex Slides khả dụng trong phiên này; chưa thể tuyên bố đã rà trực quan từng trang ở hai kích thước màn hình.
