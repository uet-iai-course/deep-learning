# Storyboard — Bài 12

## Trạng thái và điều hướng

- Lõi có 100 phút. Mở rộng có 20 phút. Bài tập riêng 50 phút.
- Có bảy stack ngang. Trong mỗi stack dùng `↓`; ở trang cuối stack dùng `→` sang stack kế tiếp.
- Stack 1: L12-00–03. Stack 2: L12-04–08. Stack 3: L12-09–17. Stack 4: L12-18–23. Stack 5: L12-24–35. Stack 6: L12-36–37. Stack 7 là phụ lục dọc duy nhất: L12-X01 → L12-X02 → L12-X03 → L12-X04.
- Ký hiệu sáu vai trò: **VĐ** vấn đề, **TG** trực giác, **VD** ví dụ, **HT** hình thức/tính toán, **UD** triển khai/ứng dụng, **KT** kiểm tra. `KAD` nghĩa là không áp dụng và luôn kèm lý do.

## Từng trang

| ID | Phút | Sáu vai trò | Đầu vào → đầu ra; dữ kiện truyền | Câu nối và điều hướng |
|---|---:|---|---|---|
| L12-00 | 2 | VĐ: phạm vi bài; TG/VD/HT/UD/KT: KAD vì là bìa. | Tên buổi → chủ đề Transformer nâng cao. | Mở mục tiêu; `↓` L12-01. |
| L12-01 | 3 | VĐ: ba LLO; TG: sản phẩm học; VD/HT/UD/KT: KAD vì là hợp đồng học tập. | Tiên quyết B10–11 → LLO23–25. | Dùng một chuỗi để nối các họ; `↓` L12-02. |
| L12-02 | 3 | VĐ: cùng dữ liệu cho tín hiệu khác; TG: giữ chuỗi cố định; VD: chuỗi “mạng nơ-ron học”; HT/UD/KT: KAD vì là ví dụ mở. | Chuỗi ký hiệu → ba cách tạo đầu vào/nhãn. | Khái quát thành ba họ; `↓` L12-03. |
| L12-03 | 2 | VĐ: chọn họ nào; TG: luồng thông tin quyết định; VD: ba cột; HT: mặt nạ/mục tiêu khái quát; UD: chọn kiến trúc; KT: KAD vì sẽ kiểm từng cụm. | Ba tín hiệu L02 → bản đồ ba họ. | Đi vào họ hai chiều; `→` L12-04. |
| L12-04 | 3 | VĐ: đọc hai phía mà không đọc khóa đệm; TG: hàng truy vấn/cột khóa; VD: mỗi truy vấn hợp lệ đọc các khóa hợp lệ; HT: $M^{enc}$; UD: Boolean hoặc cộng, loại vị trí đệm khỏi loss; KT: KAD vì L08 kiểm. | $N,T_q,T_k$ → mặt nạ $N\times1\times T_q\times T_k$. | Áp dụng vào vị trí che; `↓` L12-05. |
| L12-05 | 3 | VĐ: tạo nhãn từ chính chuỗi; TG: che một ký hiệu; VD: “học”→MASK; HT: vị trí được chọn; UD: đầu vào/nhãn; KT: KAD vì L08 kiểm. | Chuỗi L02 → $\widetilde X$ và vị trí cần khôi phục. | Chỉ vị trí nào góp sai số; `↓` L12-06. |
| L12-06 | 3 | VĐ: không tính mọi vị trí; TG: $\Omega$ chọn giám sát; VD: vị trí “học”; HT: công thức MLM, $|\Omega|>0$; UD: CE hợp nhất; KT: điều kiện lô được nêu. | $\widetilde X,\Omega,V$ → sai số trung bình trên vị trí hợp lệ. | Biểu diễn được dùng lại ra sao; `↓` L12-07. |
| L12-07 | 3 | VĐ: chuyển từ huấn luyện trước sang tác vụ; TG: đọc CLS hoặc từng vị trí; VD: phân loại/gán nhãn; HT: KAD vì không thêm công thức đầu đọc; UD: tinh chỉnh; KT: KAD vì X01 mở rộng. | Biểu diễn bộ mã hóa → đầu tác vụ. | Khóa phân biệt ngữ cảnh và giám sát; `↓` L12-08. |
| L12-08 | 2 | VĐ: dễ nhầm vị trí đọc và vị trí chịu sai số; TG: hai đường khác nhau; VD: vị trí 4/5; HT: $\Omega$; UD: KAD vì là kiểm tra; KT: câu hỏi+đáp án mảnh. | Mặt nạ L04 + $\Omega$ L06 → câu trả lời kiểm chứng. | Chuyển sang luồng một chiều; `→` L12-09. |
| L12-09 | 3 | VĐ: sinh khi tương lai chưa có; TG: tiền tố quyết định bước kế; VD: chuỗi L02 dịch trái; HT: phân rã xác suất; UD: sinh; KT: KAD vì L13 kiểm. | Chuỗi cố định → các cặp tiền tố/nhãn. | Cần chặn khóa tương lai; `↓` L12-10. |
| L12-10 | 3 | VĐ: ngăn rò nhãn tương lai; TG: tam giác dưới; VD: SVG 5 vị trí; HT: $M^{causal}$; UD: Boolean/cộng, chặn khóa đệm, phát theo đầu; KT: KAD vì L13. | $M^{valid}$ + thứ tự $i,j$ → mặt nạ $N\times1\times T\times T$. | Từ mặt nạ sang sai số; `↓` L12-11. |
| L12-11 | 3 | VĐ: tổng hợp sai số theo độ dài thật; TG: chỉ ký hiệu đích hợp lệ; VD: EOS hợp lệ; HT: CLM và mẫu số dương; UD: CE/log-softmax ổn định; KT: điều kiện miền. | $Z^{CLM},Y,M^{tgt}$ → sai số trung bình theo ký hiệu. | Khi dự đoán chưa biết thì dùng lại đầu ra; `↓` L12-12. |
| L12-12 | 3 | VĐ: tiền tố suy luận không có nhãn thật; TG: đưa dự đoán trở lại; VD: hai bước đầu; HT: phân phối bước kế; UD: vòng lặp EOS/giới hạn; KT: KAD vì L13. | BOS → tiền tố tăng dần. | Kiểm tra song song và nhân quả; `↓` L12-13. |
| L12-13 | 2 | VĐ: nhầm huấn luyện song song với nhìn tương lai; TG: mặt nạ giữ nhân quả; VD: vị trí đang dự đoán; HT: quan hệ tiền tố; UD: KAD vì là kiểm tra; KT: câu hỏi+đáp án mảnh. | L09–12 → giải thích đúng huấn luyện/suy luận. | Thêm chuỗi nguồn; `↓` L12-14. |
| L12-14 | 3 | VĐ: căn chỉnh đầu vào/nhãn đích; TG: dịch một vị trí; VD: BOS và EOS; HT: $Y^{in},Y^{out}\in N\times T_t$; UD: học theo đáp án; KT: KAD vì L17. | Chuỗi đích → hai tensor lệch một vị trí. | Ba luồng cần ba mặt nạ; `↓` L12-15. |
| L12-15 | 3 | VĐ: nguồn, đích và chú ý chéo có trục khác; TG: hàng truy vấn/cột khóa; VD: bảng ba luồng; HT: ba kích thước; UD: chặn khóa đệm, loại vị trí đích đệm khỏi loss; KT: KAD vì L17. | $T_s,T_t$ → ba mặt nạ phát theo đầu. | Ghép biểu diễn với nhãn; `↓` L12-16. |
| L12-16 | 2 | VĐ: nối bộ mã hóa với dự đoán từ vựng; TG: $H^{enc}\to H^{dec}\to Z^{tgt}$; VD: kích thước ba tensor; HT: CE trục $V$ và trung bình hợp lệ; UD: hàm hợp nhất; KT: mẫu số dương. | $Y^{out},M^{tgt},H^{enc}$ → $Z^{tgt}$ và $\mathcal L$. | Đối chiếu huấn luyện với suy luận; `↓` L12-17. |
| L12-17 | 2 | VĐ: cùng mô hình nhưng lịch tính khác; TG: nhãn có sẵn so với tự sinh; VD: BOS/EOS; HT: mặt nạ nhân quả; UD: cờ đang hoạt động theo mẫu; KT: câu hỏi+đáp án mảnh. | L14–16 → hợp đồng train/infer. | Từ mục tiêu sang huấn luyện trước; `→` L12-18. |
| L12-18 | 3 | VĐ: tham số dùng lại hình thành thế nào; TG: mục tiêu tạo tín hiệu từ dữ liệu; VD: MLM che “học” và CLM dịch chuỗi; HT: KAD vì công thức đã có ở L06/L11; UD: tiền huấn luyện→thích nghi; KT: KAD vì L20. | Hai mục tiêu đã học → quy trình dùng lại tham số. | Định nghĩa LLM ở đúng mức nguồn; `↓` L12-19. |
| L12-19 | 3 | VĐ: chữ “lớn” không có ngưỡng phổ quát; TG: định nghĩa làm việc; VD: mô hình ngôn ngữ nơ-ron huấn luyện trước; HT: KAD vì nguồn không khóa ngưỡng; UD: có thể thích nghi cho nhiều nhiệm vụ; KT: KAD vì L20. | Huấn luyện trước L18 → định nghĩa làm việc nhất quán. | Kiểm tra một kết luận không được phép; `↓` L12-20. |
| L12-20 | 2 | VĐ: tên gọi dễ bị dùng như bảo chứng; TG: tên gọi khác kết quả đánh giá; VD: đúng/an toàn/phù hợp miền; HT: KAD vì là kiểm tra khái niệm; UD: yêu cầu giao thức riêng; KT: câu hỏi một nghĩa+đáp án mảnh. | Định nghĩa L19 → giới hạn kết luận. | Đổi từ một phương thức sang cặp ảnh–văn bản; `↓` L12-21. |
| L12-21 | 2 | VĐ: cần liên hệ hai loại dữ liệu; TG: mô hình đa phương thức xử lý từ hai loại dữ liệu; VD: CLIP với cặp $(x_i,t_i)$; HT: hai vectơ cùng chiều $D$; UD: hai bộ mã hóa, chiếu và chuẩn hóa; KT: KAD vì L22–23. | Huấn luyện trước L18 + ảnh/văn bản → trường hợp CLIP và $E_I,E_T$. | So mọi ảnh với mọi văn bản trong lô; `↓` L12-22. |
| L12-22 | 3 | VĐ: tạo tín hiệu học từ cặp đúng; TG: đường chéo là nhãn; VD: ma trận $N\times N$; HT: $S$, hai log-softmax có $1/N$ và loss đối xứng; UD: cross-entropy hợp nhất/log-softmax ổn định; KT: khóa hàng ảnh, cột văn bản. | $E_I,E_T,\tau$ → $S$, $\mathcal L_{I\to T}$, $\mathcal L_{T\to I}$ và $\mathcal L_{CLIP}$. | Dùng nhánh văn bản để tạo lớp mới; `↓` L12-23. |
| L12-23 | 2 | VĐ: phân loại không khớp đầu lớp trên dữ liệu có nhãn đích; TG: mô tả lớp thành vectơ; VD: câu nhắc chó/xe/chim; HT: $E_T^{cls}$ và $Z\in\mathbb R^{N\times K}$; UD: softmax theo $K$; KT: câu hỏi shape/trục+giới hạn zero-shot. | $E_I$ + $K$ mô tả lớp → $E_T^{cls}$ và $Z:N\times K$. | ViT là một lựa chọn nhánh ảnh tạo $E_I$; `→` L12-24. |
| L12-24 | 2 | VĐ: Transformer nhận chuỗi, ảnh là lưới; TG: chia mảnh theo raster; VD: $N=2,C=3,H=W=32,P=8$ cho 16 mảnh, 192 số/mảnh; HT: KAD để ví dụ đi trước công thức; UD: điều kiện không chồng lấp/chia hết; KT: tự đối chiếu lưới $4\times4$. | Ảnh cụ thể → dữ kiện mảnh cụ thể. | Tổng quát hóa ví dụ; `↓` L12-25. |
| L12-25 | 3 | VĐ: cần hợp đồng cho mọi $H,W,P$; TG: giữ trục lô và trục mảnh; VD: thay lại bộ số L24; HT: $T_p=(H/P)(W/P)$ và $X_{patch}:N\times T_p\times CP^2$; UD: điều kiện $P\mid H,W$; KT: thu lại 16 và 192. | Ví dụ L24 → công thức và shape tổng quát. | Xem trước toàn tuyến; `↓` L12-26. |
| L12-26 | 3 | VĐ: cần biết các bước sau phép chia; TG: sơ đồ toàn tuyến; VD: 16 mảnh→CLS→đầu ra; HT: KAD vì L27–32 khóa công thức; UD: phân biệt đầu lớp độc lập với chiếu+chuẩn hóa tạo $E_I$; KT: KAD vì L34. | Mảnh L25 → hai đích dùng CLS cuối: $Z^{cls}$ hoặc $E_I$. | Khóa phép chiếu mảnh; `↓` L12-27. |
| L12-27 | 3 | VĐ: chiều 192 chưa phải chiều mô hình; TG: một phép chiếu dùng chung; VD: $D=64$; HT: $E_{patch}=X_{patch}W_E+b_E$; UD: phát độ lệch; KT: kiểm kích thước. | $2\times16\times192$ → $2\times16\times64$. | Thêm vị trí đọc phân loại; `↓` L12-28. |
| L12-28 | 3 | VĐ: cần vị trí tổng hợp và mã vị trí; TG: thêm CLS rồi cộng $E_{pos}$; VD: 16→17; HT: $Z_0$; UD: phát theo lô; KT: KAD vì L34. | $E_{patch}$ → $Z_0:2\times17\times64$. | Đi qua khối ViT; `↓` L12-29. |
| L12-29 | 3 | VĐ: thứ tự chuẩn hóa và đường dư; TG: chuẩn hóa trước nhánh; VD: hai nhánh; HT: công thức với Drop; UD: LN theo $D$, epsilon, train/eval; KT: KAD vì L34. | $Z_{\ell-1}$ → $U_\ell,Z_\ell$ cùng kích thước. | Xem luồng trong khối; `↓` L12-30. |
| L12-30 | 3 | VĐ: theo dõi hai đường dư; TG: SVG khối; VD: $17\times64$; HT: bảo toàn kích thước; UD: điều kiện chia đầu; KT: KAD vì L34. | Công thức L29 → sơ đồ tính. | Tổng hợp toàn chuỗi kích thước; `↓` L12-31. |
| L12-31 | 3 | VĐ: lỗi trục dễ lan qua nhiều bước; TG: bảng liên tục; VD: bộ số L25; HT: năm kích thước; UD: đầu vào bộ phân loại; KT: tự dò từng hàng. | Ảnh → mảnh → chiếu → CLS/vị trí → $L$ khối. | Đọc CLS để phân loại; `↓` L12-32. |
| L12-32 | 2 | VĐ: biến chuỗi thành dự đoán ảnh; TG: lấy vị trí 0; VD: $q$ và $Z^{cls}$; HT: $W_c,b_c$, trục $K$; UD: CE hợp nhất; KT: KAD vì L34. | $Z_L:2\times17\times64$ → $Z^{cls}:N\times K$. | Đánh đổi $P$ và chi phí; `↓` L12-33. |
| L12-33 | 3 | VĐ: mảnh nhỏ làm chuỗi dài; TG: chú ý bậc hai; VD: 17→65; HT: $65^2/17^2\approx14{,}62$; UD: phân biệt tỷ số hữu hạn/tiệm cận; KT: KAD vì L34/X04. | $P=8$ và $P=4$ → tỷ số chi phí theo chuỗi. | Kiểm tra toàn tuyến ViT; `↓` L12-34. |
| L12-34 | 2 | VĐ: quên CLS hoặc sai trục; TG: lần ngược chuỗi; VD: ảnh $2\times3\times32\times32$; HT: tính 17/65; UD: KAD vì là kiểm tra; KT: câu hỏi+đáp án mảnh. | Dữ kiện L25–33 → hai kết quả kích thước. | So sánh thiên kiến ViT/CNN; `↓` L12-35. |
| L12-35 | 2 | VĐ: kiến trúc mã hóa có thiên kiến khác nhau; TG: cục bộ so với tương tác toàn cục; VD: CNN/ViT; HT: KAD vì không có công thức mới; UD: chọn theo dữ liệu/giao thức; KT: giới hạn không có ưu thế tuyệt đối. | Chuỗi ViT → so sánh phạm vi. | Chuyển sang tình huống triển khai; `→` L12-36. |
| L12-36 | 3 | VĐ: trợ lý tuyển sinh có ba rủi ro cụ thể; TG: mỗi rủi ro cần bằng chứng; VD: thiên lệch, riêng tư, thông tin sai; HT: KAD vì là thảo luận có nguồn; UD: chọn phép kiểm và hành động; KT: câu hỏi thảo luận, đáp án chỉ ở note-for-author. | Hệ thống LLM cụ thể → rủi ro, bằng chứng và quyết định. | Tổng hợp các cấu hình kỹ thuật; `↓` L12-37. |
| L12-37 | 2 | VĐ: dễ trộn tên kiến trúc với mục tiêu; TG: đối chiếu theo luồng; VD: encoder, decoder, encoder–decoder, CLIP, ViT; HT: bảng luồng/đầu ra; UD: bốn hợp đồng thiết kế; KT: câu hỏi+đáp án mảnh. | Toàn bài → bảng năm cấu hình và khung quyết định. | Kết thúc lõi; `→` L12-X01 nếu dạy phụ lục. |
| L12-X01 | 5 | VĐ: biến biểu diễn hai chiều thành phân loại; TG: đọc vị trí 0; VD: $H$; HT: $N\times D\to N\times K$; UD: tinh chỉnh; KT: câu hỏi+đáp án mảnh. | L12-07 → phép chiếu phân loại. | Sang sinh tự hồi quy; `↓` L12-X02. |
| L12-X02 | 5 | VĐ: vòng sinh vận hành thế nào; TG: đầu ra quay lại đầu vào; VD: hai bước BOS; HT: điểm $1\times V$; UD: EOS/giới hạn/cờ hoạt động; KT: câu hỏi dừng. | L12-12 → hai bước triển khai cụ thể. | Sang phép tính CLIP; `↓` L12-X03. |
| L12-X03 | 5 | VĐ: chuyển ma trận tương đồng thành sai số; TG: hai hướng dùng cùng đường chéo; VD: $N=D=2$, $E_I=E_T=I_2$, $\tau=1/\ln3$; HT: lập $S$ và hai phép trung bình L22; UD: KAD vì là bài tính; KT: giải thích khi hai hướng bằng nhau, fragment cho kết quả. | Công thức L22 → $S=\operatorname{diag}(\ln3,\ln3)$ và $\mathcal L_{CLIP}=\ln(4/3)$. | Sang đánh đổi kích thước mảnh; `↓` L12-X04. |
| L12-X04 | 5 | VĐ: mảnh nhỏ không miễn phí; TG: chi tiết đổi lấy chuỗi dài; VD: 17 so với 65; HT: tỷ số 14,62 và tiệm cận 16; UD: chọn theo ngân sách; KT: câu hỏi+đáp án mảnh. | L12-33 → bảng đánh đổi. | Kết thúc stack phụ lục. |

## Chu trình khái niệm

- Bộ mã hóa: VĐ L04 → TG/VD L05 → HT/UD L06–07 → KT L08.
- Bộ giải mã: VĐ/TG/VD L09 → HT/UD L10–12 → KT L13.
- Mã hóa–giải mã: VĐ/VD L14 → TG/HT L15–16 → UD/KT L17.
- LLM: VĐ/TG/VD L18 → định nghĩa/UD L19 → KT L20; không thêm thuật toán LLM ngoài nguồn.
- CLIP đa phương thức: VĐ/TG/VD L21 → HT/UD L22–23 → KT lõi L23; X03 là phép tính kiểm tra mở rộng.
- ViT: VĐ/TG/VD L24 → HT L25,27–32 → UD/cầu nối CLIP L26 và đánh đổi L33,35 → KT L34; X04 là kiểm tra mở rộng.
- Đạo đức: tình huống/VĐ/VD L36 → thảo luận UD/KT ngay L36; đáp án chi tiết không lên deck. L37 tổng hợp năm cấu hình.

## Thời lượng

- Lõi: 100 phút.
- Mở rộng: 20 phút.
- Bài tập: 50 phút riêng.
- Phân bổ bài tập: 30 phút bài kỹ thuật từ bộ trang chiếu + 20 phút động não dự án cuối kỳ theo DOCX Buổi 12. Hoạt động dự án không bù vào thời lượng trình chiếu 100+20.
- L12-21–23 dùng đúng 7 phút lõi cho phần đa phương thức; X03 dùng 5 phút mở rộng để tính sai số đối xứng.
