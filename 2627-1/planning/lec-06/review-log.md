# Nhật ký rà soát Bài 06

## Pipeline lecture note (2026-09-03)

- Dossier chỉ chứa mục chi tiết DOCX Buổi 6 và các dải đã duyệt trong `source.md`; mọi PDF/DOCX được trích cục bộ thành UTF-8. Không có `.env`, bí mật, symlink hoặc tệp nhị phân trong dossier gửi OpenRouter.
- Vai lập kế hoạch chạy riêng trước phân tích chi tiết bằng `z-ai/glm-5.3-flash`, provider OpenRouter; model yêu cầu và thực tế trùng nhau. Điều phối viên giữ đề xuất song song cho các vai đọc, nhưng không tạo lại 15 SVG đã có và không cho DeepSeek ghi song song.
- Ba vai nguồn chạy song song trên Stanford, Illinois/CMU và hợp đồng toán/tensor. Cả ba xác nhận đúng model/provider. Giữ mạch Stanford; dùng nguồn bổ sung để khóa nghiệm đồng nhất, mã thấp chiều, thưa, khử nhiễu, PCA/đa tạp và đánh giá; không đưa câu dẫn VAE ở Stanford 70 vào nội dung.
- Tái lập $419.120$ tham số cho $d=32$ có độ lệch: $200.960+8.224+8.448+201.488$. Khóa MSE $\|X-\hat X\|_F^2/(ND)$, ví dụ SSE $0{,}18$, MSE $0{,}045$; đóng băng gradient độc lập với chế độ mô-đun. Hai bản đồ nguồn được hợp nhất thành L06-T01–T10 trong `outline.md`.
- DeepSeek writer chạy tuần tự 10 mảnh trong 10 staging root mới, `create-once`, trần cứng 2.500 ký tự; độ dài từ 1.270 đến 2.417 ký tự. Mọi lượt xác nhận `requested_model=observed_model=deepseek/deepseek-v4-flash-0731`, provider OpenRouter.
- Loại toàn bộ mảnh mất mát do Unicode tiếng Việt hỏng. Bác các mệnh đề sai/quá mạnh từ các mảnh còn lại: mã không tự được chứng minh chứa cấu trúc nhận dạng; $F=0$ không kéo theo mất mát bằng 0; đóng băng không biến $d$ thành tham số đầu tác vụ; tổ hợp mã PCA không tự bảo đảm hợp lệ; khoảng cách Euclid không tự bằng khoảng cách trên đa tạp. Codex chỉ lấy dữ kiện phù hợp semantic contract và viết lại bằng `apply_patch`.
- Năm vai phản biện lecture note chạy song song đúng `z-ai/glm-5.3-flash`/OpenRouter. Sửa lỗi `\qquad`, bổ sung tiên quyết chế độ mô-đun, ví dụ cụ thể cho $\Omega$, kiểm tra ở Cụm 2/6/7, câu nối nội dung và phần bổ sung X01–X05. Chỉ gọi tên VAE để khóa ranh giới; không triển khai cơ chế VAE.
- Hai lượt tái kiểm toán/mạch và lượt mạch cuối đều xác nhận đúng model/provider. KaTeX, shape, tổng 419.120 tham số, SSE/MSE, mã thưa, khử nhiễu, stop-gradient và ranh giới AE/VAE đều đạt; bảy cụm đều có câu kiểm tra, phần bổ sung phủ đủ vai trò X01–X05. Không còn lỗi nghiêm trọng hoặc chặn bàn giao.
- Kiểm bản cuối theo `no-ai-slop/eval.md`: bỏ câu hỏi tu từ, lời dẫn sân khấu, giọng quảng bá, dấu vết AI/quy trình và chỉ dẫn cho người viết/diễn giả. Rà theo nguyên tắc Quill xác nhận chuỗi $X_{img}\to X\to Z\to\hat X$, ký hiệu $d,k,\Omega$ và các câu nối tích lũy liên tục; không tạo `quill.json`.
- Trình xem lecture note đạt ở 1280×720 và 390×844: 99 công thức KaTeX không lỗi, 15/15 SVG tải được, bảy lời giải đóng mặc định và mở bằng bàn phím, không tràn ngang, lỗi console hoặc request. Chế độ in mở lời giải và ẩn điều hướng; traversal và ghép sai số bài đều bị từ chối. Rà trực quan toàn trang xác nhận bảng, công thức và hình đọc được ở cả hai khung.

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
| Không có code demo | Nhiệm vụ hiện tại là rà/chỉnh deck; quy tắc AGENTS chỉ chuyển code khi nguồn có nội dung code tương ứng hoặc người dùng yêu cầu. Các dải trích được duyệt không chứa code hoặc chỉ dẫn API triển khai, nên không tạo code demo. Bài tập giấy vẫn đủ 50 phút. |
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
- Mọi phương án cắt, thời lượng, đáp án chi tiết và quyết định nội bộ nằm trong `note-for-author.md`, không đưa vào ghi chú diễn giả.

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
| trung bình | L06-X02 | Giả thiết "dữ liệu đã định tâm" và phát biểu "tại nghiệm tối ưu" không có nguyên văn trong Illinois 7 | Illinois 65–83 chỉ nêu điều kiện của nghiệm, không dùng cụm "toàn cục" | Giữ giả thiết định tâm như bổ sung toán học chuẩn để phát biểu chính xác; phát biểu ở mức "tại nghiệm tối ưu, khôi phục không gian con chính $K$ chiều", tránh cụm "nghiệm tối ưu toàn cục". |
| trung bình | L06-X03, note-for-author | note-for-author tuyên bố `sparse-code.svg` dùng ở X03 nhưng HTML X03 không có hình | HTML X03 chỉ có hai card văn bản | Sửa note-for-author: `sparse-code.svg` chỉ dùng ở L06-23; không thêm hình chỉ để khớp ghi chú. |
| nhẹ | L06-04 | Thiếu truy nguyên `lec01_intro.pdf` 26–37 dù outline gán dải này | Ghi chú nguồn trên slide chỉ nêu Stanford và GT | Đã thêm "lec01_intro, tr. 26–37" vào ghi chú nguồn của L06-04. |
| nhẹ | L06-37 | LLO12 yêu cầu nối "trong các mô hình lớn" nhưng deck dừng ở đóng băng/tinh chỉnh | DOCX Buổi 06 | Thêm một câu nối ngắn ở L06-37: cơ chế tiền huấn luyện–tái sử dụng cũng là nền tảng của các mô hình lớn; chi tiết để bài sau, không mở rộng thành phần LLM. |
| nhẹ | L06-17 | DOCX dùng "nút cổ chai", deck dùng "nút thắt" | docx-text.txt 262 | Thêm chú giải một lần: "nút thắt (nút cổ chai)". |
| nhẹ | L06-X05 | Hạt giống và đánh giá sai lệch chưa được nguồn khóa đủ chi tiết | Dải nguồn chỉ hỗ trợ giao thức và tính hữu ích phụ thuộc tác vụ | Không giữ các tuyên bố đó; thay bằng ba phần dữ liệu tách biệt và chỉ số gắn với tác vụ. |

Rà lại sau đổi cấu trúc đã bao phủ các cụm bị ảnh hưởng và hai trang lân cận: L06-07–15, L06-20–29, L06-27–35, L06-X01–X05. Không đổi số lượng hoặc thứ tự 44 trang; tuyến lõi vẫn 100 phút và tuyến mở rộng 20 phút.

## Hợp nhất năm báo cáo hiện tại sau bản nháp

| Nguồn rà | Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|---|
| Chuyên gia; kết nối và mạch viết | chặn bàn giao | Toàn deck; các ranh giới L06-05/06, 10/11, 15/16, 20/21, 27/28, 33/34 | HTML thực chỉ có một `<section>` ngoài, trái hồ sơ bảy mạch và làm mất điều hướng ngang | Trước lượt chỉnh sửa, HTML có một thẻ ngoài bao cả 44 trang | Đã đóng/mở ngăn xếp tại sáu ranh giới, tạo đúng bảy section ngoài với kích thước [6, 5, 5, 5, 7, 6, 10]. Giữ L06-38 ở cuối. |
| Sinh viên; học thuật và giảng dạy | trung bình | Toàn deck | Hai báo cáo đếm nhầm HTML trước sửa thành bảy section ngoài | Kiểm tra DOM của điều phối viên và hai báo cáo Chuyên gia/Kết nối cùng xác nhận chỉ có một section ngoài | Không áp dụng nhận định “đã có bảy section”. Sửa theo bằng chứng DOM; yêu cầu điều phối viên rà lại mạch và các ranh giới sau lượt này. |
| Kết nối và mạch viết | trung bình | L06-05, 10, 15, 20, 27, 33; L06-01, 37 | Chỉ dẫn mũi tên phải liệt kê cả các trang không phải cuối mạch | Mạch 1 chứa L06-00–05; mạch 7 chứa L06-34–37, X01–X05, L06-38 | Đã khóa mũi tên phải ở cuối sáu mạch đầu. L06-37 dùng End cho tuyến lõi hoặc Xuống cho tuyến đầy đủ; L06-01 đi Xuống. |
| Kết nối và mạch viết | trung bình | L06-X05 → L06-38 | Câu nối chỉ có trong planning, chưa nằm trong ghi chú diễn giả của X05 | Ghi chú X05 trước sửa kết thúc ở giao thức đánh giá | Đã thêm câu chuyển về kiểm tra tổng hợp và ba giới hạn vào ghi chú X05. |
| Sinh viên; học thuật; toán học và triển khai | trung bình | L06-29; outline | $\theta^\star$ và $C$ xuất hiện trước khi được định nghĩa; cụm tái sử dụng thiếu ví dụ tensor | Công thức dùng $f_{\theta^\star}$ và $N\times C$; bảng ký hiệu cũ chỉ có $\theta,\phi,\psi$ | Đã định nghĩa $\theta^\star$, $C$; thêm MNIST $N=32$, $Z:32\times d$, $S:32\times10$ và chỉ $\psi$ thuộc bộ tối ưu. Không thêm phép đếm tham số vì không cần cho luận điểm. |
| Học thuật và giảng dạy | trung bình | L06-14 | Vòng huấn luyện thiếu số epoch và cách chọn tốc độ học | Ghi chú cũ chỉ mô tả một bước cập nhật; L06-32 mới nhắc chọn siêu tham số | Đã ghi lặp trên các lô qua số epoch định trước; chọn tốc độ học và số epoch trên tập kiểm định, nối L06-32. Không thêm code. |
| Sinh viên | nhẹ | L06-09, L06-13; outline | Miền của $X$ và $\hat X$ bị gộp, trong khi đầu ra sigmoid thuộc miền mở | L06-09 ghi $\hat X\in(0,1)$ nhưng L06-13 cũ ghi cả hai thuộc $[0,1]$ | Đã tách $X\in[0,1]$ và $\hat X\in(0,1)$ ở L06-13 và bảng ký hiệu. |
| Sinh viên | nhẹ | L06-12, L06-25, L06-31 | $D$, $p_{\mathrm{train}}$ và “trích đặc trưng” chưa được giải thích tại chỗ | Các ký hiệu/thuật ngữ chỉ có trong planning hoặc phải suy từ trang khác | Đã viết “$D=4$ phần tử”, định nghĩa phân phối dữ liệu huấn luyện và chú giải trích đặc trưng là đóng băng bộ mã hóa, chỉ huấn luyện bộ phân loại. |
| Chuyên gia; học thuật và giảng dạy | nhẹ | L06-22, L06-26 | “Giảm dần hoạt hóa” mô tả sai cơ chế phạt mềm; $\Omega$ chưa được định nghĩa | Phạt $L_1$ tác động qua hạng thêm vào mất mát; bảng cũ chỉ ghi $\Omega$ | Đã mô tả hạng phạt tạo áp lực đưa hoạt hóa về 0 và định nghĩa $\Omega$ là hàm phạt thưa. |
| Toán học và triển khai | nhẹ | L06-23 | Hai số 1,8 và 2,4 có thể bị đọc nhầm là vị trí | Câu cũ không phân biệt giá trị và chỉ số; X03 dùng vị trí 2 và 4 | Đã ghi rõ đây là hai giá trị lớn nhất tại vị trí 2 và 4; các vị trí khác bằng 0. |
| Học thuật; kết nối và mạch viết | nhẹ | L06-18–21 | L06-20 lặp kết luận về $d$ thay vì tạo bước tiến | L06-18 đã nêu nút thắt không bảo đảm; câu hỏi cũ chỉ hỏi lại $d<784$ | Đã đổi thành tình huống lỗi tái tạo kiểm định thấp nhưng phân loại từ $z$ kém; ghi chú nối sang ba điểm can thiệp ở L06-21. |
| Chuyên gia | trung bình | L06-37 | Liên hệ LLO12 với mô hình lớn chỉ có trong ghi chú | Mặt trang cũ chỉ có bốn câu hỏi sử dụng mã | Đã thêm một câu ngắn về cơ chế tiền huấn luyện–tái sử dụng biểu diễn, không mở sang kiến trúc cụ thể. |
| Sinh viên; học thuật; kết nối và mạch viết | nhẹ | L06-38 | Kết luận cần thu hồi rõ ba luồng thay vì chỉ lặp ý hữu ích tác vụ | Ba luồng đã được thiết lập ở L06-05, L06-18–20 và L06-34–36 | Giữ câu hỏi; đáp án nay gắn nhãn hữu ích tác vụ, ghi nhớ và lấy mẫu. Ghi chú nêu rõ ba điểm được thu hồi. |
| Chuyên gia | nhẹ | note-for-author | Tuyến 100 phút dày và chỉ có một mức dự phòng | Các điểm chờ ở L06-23, 27, 33 có thể làm tràn giờ | Giữ timing chính 100/20/50; thêm mức dự phòng: không chờ ở L06-23 và gộp phần nói L06-34–35, nhưng vẫn giữ L06-36–38. |
| Sinh viên; toán học; học thuật | trung bình | Toàn deck | Chưa có bằng chứng dựng KaTeX và rà trực quan cho bản sau sửa | Các kết quả ở mục Kiểm định cuối thuộc phiên trước | Không tuyên bố đã chạy lại trong lượt biên tập. Chuyển việc dựng KaTeX, HTTP và duyệt hai kích thước cho điều phối viên kiểm định cuối. |

Các đề xuất không áp dụng: không thêm phép đếm tham số bộ phân loại ở L06-29 vì ví dụ tensor đã đủ; không thêm hình vào L06-X03 vì nội dung hiện không cần hình lặp; không cài phím End tùy chỉnh vì L06-38 là slide cuối và tuyến đã khóa dùng hành vi mặc định của RevealJS; không thêm code, raster hoặc nội dung ngoài dải nguồn. Các câu mới đã rà theo `no-ai-slop`; thứ tự khái niệm, ký hiệu và câu nối đã rà theo Quill, không tạo `quill.json`.

## Tái kiểm độ chính xác và mạch viết

Hai báo cáo tái kiểm xác nhận không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`; cấu trúc, timing, số liệu, kích thước tensor, mất mát, top-$k$, đóng băng–tinh chỉnh, PCA và giới hạn lấy mẫu đều đạt. Các quyết định cho vấn đề nhẹ:

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nhẹ | L06-09 | Ghi chú chưa phân biệt miền mở của đầu ra sigmoid với miền điểm ảnh | Mặt trang khóa $\hat X\in(0,1)$, còn ghi chú cũ nói khớp $[0,1]$ | Đã sửa: sigmoid cho giá trị trong $(0,1)$ và gần khớp miền điểm ảnh $[0,1]$. |
| nhẹ | L06-26 | Báo cáo đề xuất đổi mẫu số phạt thưa từ $Nd$ thành $ND$ | $Z\in\mathbb R^{N\times d}$ nên $\lVert Z\rVert_1$ có $Nd$ phần tử; $D$ là số phần tử đầu vào | Không áp dụng đề xuất. Giữ $\lambda\lVert Z\rVert_1/(Nd)$; đổi sang $ND$ sẽ lấy trung bình theo sai số phần tử. |
| nhẹ | L06-X02 | “Độ lệch” có thể bị hiểu là sai lệch thống kê | Ngữ cảnh nói tham số cộng của lớp tuyến tính | Đã viết rõ “vector độ lệch (bias) phù hợp”. |
| nhẹ | L06-25 | Công thức theo mẫu và ký hiệu lô chưa có câu nối | Kỳ vọng dùng $x,\widetilde x$ với mẫu số $D$; dòng dưới dùng $X,\widetilde X$ | Đã ghi trong notes: trung bình theo $N$ mẫu của lô và theo $D$ phần tử cho quy ước $1/(ND)$. |
| nhẹ | L06-27 → L06-28 | Ranh giới từ ba biến thể sang tái sử dụng thiếu tín hiệu chuyển | Câu nối mới chỉ có trong storyboard | Đã thêm vào notes L06-27: kiểm tra giá trị của mã bằng tác vụ có nhãn. |
| nhẹ | L06-33 → L06-34 | Ranh giới từ giao thức đánh giá sang giới hạn lấy mẫu còn đột ngột | Câu nối mới chỉ có trong storyboard | Đã mở notes L06-34 bằng câu hỏi về việc dùng mã ngoài các điểm dữ liệu đã huấn luyện. |
| nhẹ | L06-37 | Điểm rẽ tuyến chưa báo phần mở rộng nằm bên dưới | Mặt trang không nên chứa chỉ dẫn nội bộ; note-for-author đã khóa hai tuyến | Đã ghi trong notes rằng phần mở rộng nằm bên dưới và có thể bỏ; không đưa chỉ dẫn lên mặt trang. |
| nhẹ | L06-38 | Có thể thêm tín hiệu kết luận rõ hơn | Đáp án đã gắn nhãn ba luồng và notes đã thu hồi ba phần | Không sửa thêm; nội dung hiện đã thực hiện đúng vai trò kết luận. |

Tái kiểm cuối phát hiện lỗi V1: mã slide nội bộ xuất hiện trong ghi chú diễn giả. Đã thay các tham chiếu ở ghi chú của phần huấn luyện, nút thắt, khử nhiễu và kết luận bằng mô tả tự nhiên; đồng thời rà toàn HTML và loại tham chiếu tương tự trong ghi chú nguồn của trang kiểm tra mất mát. Mã `L06-*` nay chỉ còn trong thuộc tính `data-slide-id`, đúng yêu cầu không hiển thị mã nội bộ trên mặt trang hoặc trong ghi chú diễn giả.

## Hậu kiểm cục bộ cuối

- L06-25 và bảng ký hiệu không còn giả sử nhiễu giữ miền $[0,1]$: $X$ sạch thuộc $[0,1]^{N\times784}$, còn $\widetilde X\in\mathbb R^{N\times784}$ vì nguồn không khóa phép cắt miền.
- L06-29 dùng chéo entropy hợp nhất trực tiếp từ logit với phép log-softmax ổn định; không hướng dẫn tính softmax rồi lấy log thủ công.
- L06-30 ghi rõ chi phí tinh chỉnh đến từ lan truyền ngược qua bộ mã hóa, lưu hoạt hóa và trạng thái bộ tối ưu.
- Bài tập kích thước giữ sản phẩm bắt buộc đúng `source.md`: hoàn thiện sơ đồ bộ mã hóa–mã tiềm ẩn–bộ giải mã và toàn bộ kích thước trong 10 phút; đếm tham số chỉ là phần tùy chọn.
- L06-22 định nghĩa $\lambda$ là hệ số phạt trước khi L06-26 dùng công thức. Storyboard coi X01 là kiểm tra mở rộng và X05 là ứng dụng/tổng kết.

## Kiểm định cuối

- Cấu trúc: đúng 7 section ngoài với kích thước [6, 5, 5, 5, 7, 6, 10]; 44 trang, 44 `data-slide-id` duy nhất, 44 khối ghi chú, 8 đáp án dùng fragment. Mạch 7 chứa L06-34–37, L06-X01–X05 rồi L06-38; L06-38 là slide cuối toàn deck, kết luận không đặt trước phần mở rộng.
- Ánh xạ `lec11_dense.pdf` 3–10 đã sửa trong outline: dải này là nguồn nối về tiền huấn luyện/học chuyển giao, không phải nguồn cho kích thước MLP hoặc phép làm phẳng (kích thước/làm phẳng khóa từ GT 38–40 và quy ước của học phần).
- LLO11 ở L06-01 đã trả về nguyên văn DOCX: "Trình bày được kiến trúc của một Autoencoder cơ bản, bao gồm bộ mã hóa, không gian ẩn và bộ giải mã." Phần tính kích thước/mất mát được ghi rõ là sản phẩm luyện tập của bài, không giả làm LLO gốc.
- Điều hướng: tại L06-37 nhấn End tới L06-38 (hành vi End mặc định của RevealJS vì L06-38 là slide cuối); tuyến đầy đủ đi Xuống qua X01–X05 rồi tới L06-38. Câu nối X05→38 đã ghi trong storyboard và note-for-author.
- Storyboard: 44 dòng slide, timing từng trang không đổi; tuyến lõi 100 phút gồm cả L06-38 (3 phút), tuyến mở rộng 20 phút, bài tập riêng 50 phút.
- KaTeX strict: bản hiện tại dựng 130 cụm `.katex`, gồm 7 công thức khối, không có `.katex-error`; RevealJS sẵn sàng và nhận đủ 44 trang. Cấu hình giữ `throwOnError: true`, `strict: "error"`.
- Máy chủ: `python3 -m reloadserver 8765` không khả dụng trong môi trường. Đã phục vụ cục bộ từ thư mục `2627-1/` bằng cổng 8766; HTML và mọi tài nguyên cốt lõi trả HTTP 200. Một yêu cầu tự động tới `favicon.ico` trả 404, không phải tài nguyên của deck. SHA-256 của HTML phục vụ khớp tệp trong kho: `a8864b3bec76fc07fcd3efa6c72de682c93d222b6583829848cf4a5ccb37b1bb`.
- Rà trực quan: đã dựng 88 ảnh chụp, gồm 44 trang ở 1280×720 và 44 trang ở 960×720. Bộ đo biên viewport ghi nhận 0 tràn, 0 phần tử văn bản dưới 18 px, 0 lỗi trang và 0 yêu cầu tài nguyên cốt lõi thất bại. Đã rà hai contact sheet toàn deck; không thấy chữ bị cắt, chồng lấn, công thức hoặc hình vỡ.
- Điều hướng bàn phím đã kiểm trực tiếp: End tại L06-37 tới L06-38; tuyến Xuống đi qua L06-X01, fragment của X01, X02, X03, X04, X05 rồi L06-38.

## Đợt kiểm định deck cuối ngày 2026-09-03

### Phạm vi DeepSeek được khóa cho các đợt sau

- Ba task deck tuần tự, mỗi task đúng năm `data-slide-id`, chạy trong staging mới với `MCP_WRITE_POLICY=create-once` và `MCP_MAX_WRITE_CHARS=2500`. Mỗi task chỉ được tạo một `writer-delta.md`; không được đọc hoặc sửa dự án, không được phát lại toàn HTML và không được thêm hướng dẫn diễn giả. Đây là trần mặc định cho các buổi sau, không tự tăng theo một lượt thành công.
- Cả ba lượt được chấp nhận về runtime đều xác nhận `requested_model=observed_model=deepseek/deepseek-v4-flash-0731`, provider OpenRouter; độ dài đầu ra lần lượt 1.105, 715 và 877 ký tự. Ba lượt sandbox trước đó thất bại do DNS và không được tính là kết quả mô hình.
- Cả ba đầu ra bị bác về chất lượng vì chỉ diễn giải lại đặc tả, không cung cấp chuỗi thay thế có thể kiểm tra. Điều phối viên dùng chính đặc tả đã duyệt để sửa cục bộ bằng `apply_patch`; không nới trần, không giao lại toàn deck và không ghép nội dung chưa kiểm chứng.
- Quy tắc bền vững đã nằm trong `prompt_lecture_note_deck.md` và `openrouter-mcp/README.md`: task dài hỏng Unicode/KaTeX chỉ được thử lại toàn bản một lần; sau đó phải chia thành mảnh một hoặc hai mục, mặc định không quá 2.500 ký tự. Đầu ra có Unicode hỏng, KaTeX sai, đường dẫn sai, sai danh sách tệp hoặc chỉ lặp yêu cầu phải bị loại toàn bộ.

### Hợp nhất năm báo cáo độc lập

- Năm báo cáo hợp lệ đều xác nhận `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter. Hai lượt đầu của vai sinh viên và toán học vượt giới hạn gọi công cụ nên không được chấp nhận; hai vai được chạy lại trên danh sách tệp hẹp và hoàn tất đúng model/provider.
- Không báo cáo hợp lệ nào còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`. Đã áp dụng các sửa có bằng chứng: thống nhất $0{,}18$ và $0{,}045$; viết mẫu số thưa thành $N\cdot d$ và giải thích $D$ khác $d$; đổi nhãn L06-36 thành “Đã có/Còn thiếu”; thêm cầu nối nội dung ở L06-28 và L06-34; sửa hai ánh xạ trang nguồn trong `outline.md`; làm rõ vai trò cụm Mở rộng và phân nơi lưu kịch bản chờ.
- Không áp dụng đề xuất đưa X01–X05 ra sau L06-38 hoặc thêm một trang kết mới. Cấu trúc hiện tại cố ý giữ L06-38 là trang cuối trong DOM: tuyến lõi dùng End từ L06-37, tuyến đầy đủ đi qua X01–X05 rồi cùng kết ở L06-38. Đổi cấu trúc sẽ phá điểm hội tụ này.
- Không áp dụng đề xuất thêm notebook/code hay triển khai VAE. Nguồn đã duyệt không yêu cầu code demo; VAE chỉ được gọi tên để khóa ranh giới, đúng phạm vi, không dạy phân phối tiên nghiệm hay cơ chế huấn luyện. Không đổi $\lVert Z\rVert_1/(N\cdot d)$ thành mẫu số $ND$ vì $Z$ có $N\cdot d$ phần tử.
- Hai lượt tái kiểm toán và mạch sau sửa đều hoàn tất đúng GLM/OpenRouter. Toán học xác nhận không có lỗi mới; mạch xác nhận đúng bảy section ngoài với kích thước [6, 5, 5, 5, 7, 6, 10], các cầu nối và L06-38 là kết luận cuối của cả hai tuyến.

### Biên tập và kiểm định phát hành

- Lượt cuối theo `no-ai-slop/eval.md` đã bỏ lời dẫn sân khấu, chỉ dẫn điều hướng, tự biện hộ về nguồn, metadata tuyến và các cụm “trang kế/phần kế tiếp”. Ghi chú diễn giả chỉ còn nội dung học thuật, giả thiết, lỗi dễ mắc, đáp án và nguồn. Nguyên tắc Quill được dùng để rà chuỗi biểu diễn → kiến trúc → mất mát → ràng buộc → tái sử dụng → giới hạn lấy mẫu; không tạo `quill.json`.
- Rà tiêu đề `h1`, `h2`, `h3` xác nhận không còn tiêu đề pha tiếng Anh ngoài tên/viết tắt/ký hiệu được phép như MLP, MNIST, ReLU, PCA, LLO và top-$k$. Tên công khai dùng “mạng tự mã hóa”; thuật ngữ `autoencoder` chỉ được giới thiệu trong nội dung/nguồn khi cần.
- Kiểm tra tĩnh: 44 trang, 44 `data-slide-id` duy nhất, 44 ghi chú, 7 section ngoài, 142 biểu thức KaTeX dựng với `throwOnError: true` và strict mode, 16 tham chiếu tới 15 SVG, không thiếu tài nguyên, không có raster hoặc phụ thuộc mạng cốt lõi. `git diff --check` đạt. SHA-256 của HTML: `0fb5189baf68c9b836cf0d08092e6186e670639ae4ff24800e8398fc244f9e84`.
- Chromium headless duyệt đủ 44 trang ở 1280×720 và 800×600: không lỗi console/request, không tràn khung. Bàn phím đạt cho L06-00 → L06-01 bằng mũi tên xuống, quay lại bằng mũi tên lên và L06-00 → L06-06 bằng mũi tên phải. Hai contact sheet cuối đã được rà trực quan; công thức, bảng, SVG và chữ trên các trang sửa đều hiển thị đúng.
- Codex Slides không có bề mặt trình duyệt/plugin khả dụng trong môi trường này; kiểm định trực quan dùng Chromium cục bộ. `python3 -m reloadserver 8765` vẫn không khả dụng; máy chủ cục bộ trên cổng 8766 được dùng cho lần kiểm định này. Không tuyên bố đã dùng Codex Slides hoặc reloadserver.
