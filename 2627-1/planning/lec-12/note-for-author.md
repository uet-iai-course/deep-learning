# Ghi chú cho người soạn — Bài 12

## Trạng thái

- Tuyến lõi đủ 100 phút; tuyến mở rộng đủ 20 phút; bài tập riêng 50 phút.
- LLO24 dùng CLIP làm trường hợp mô hình đa phương thức hai bộ mã hóa, theo nguồn Radford và cộng sự (2021), PDF 1–3.
- `hocsau_draft.pdf` PDF 312–314 không được dùng làm nguồn cho CLIP.

## Tuyến giảng hiện có

- Giữ chuỗi “mạng nơ-ron học” từ L12-02 đến L12-17; chỉ thay đầu vào, nhãn và đường thông tin.
- Ở L12-04, L12-10 và L12-15, luôn đọc mặt nạ theo hàng là truy vấn, cột là khóa. Chặn khóa đệm trước softmax và dùng $M^{tgt}$ để loại vị trí đệm khỏi sai số. Không nói rằng mọi triển khai bắt buộc đưa đầu ra tại truy vấn đệm về không.
- Ở L12-14, viết hai hàng $Y^{in}/Y^{out}$ trước khi sang mặt nạ và kích thước. EOS thuộc nhãn hợp lệ; BOS chỉ mở đầu vào.
- Ở L12-17, nêu cờ đang hoạt động theo từng mẫu. Mẫu đã sinh EOS không tiếp tục tạo đầu ra có nghĩa.
- Giữ mạch L12-18–23: ví dụ MLM/CLM → huấn luyện trước → định nghĩa làm việc LLM → giới hạn tên gọi → định nghĩa đa phương thức → CLIP hai bộ mã hóa → ma trận $S$ → phân loại zero-shot. Không gọi CLIP là mô hình sinh, không mô tả hai nhánh bằng chú ý chéo.
- Ở L12-22, hàng của $S$ là ảnh và cột là văn bản. Chuẩn hóa $E_I,E_T$ theo hàng; hai loss đều là trung bình $1/N$ của log-softmax theo hàng trên $S$ và $S^\top$. Dùng cross-entropy hợp nhất hoặc log-softmax ổn định, không softmax rồi lấy log. $1/\tau$ tương ứng hệ số nhiệt độ học được trong giả mã nguồn.
- Ở L12-23, dùng $E_T^{cls}\in\mathbb R^{K\times D}$ cho các câu nhắc lớp, $Z$ cho điểm lớp và softmax theo $K$. “Zero-shot” không đồng nghĩa với không cần đánh giá trên tập đích.
- Ở L12-24–25, luôn làm ví dụ $32\times32,P=8$ trước rồi mới tổng quát hóa $T_p$ và $X_{patch}$. Ở L12-26, nói rõ ViT chỉ là một lựa chọn nhánh ảnh của CLIP: CLS cuối → chiếu → chuẩn hóa L2 → một hàng $E_I$. Đầu phân loại độc lập tạo $Z^{cls}$ là đường khác.
- Giữ bộ số ViT $N=2,C=3,H=W=32,P=8,D=64$ từ L12-24 đến L12-34.
- Ở L12-29, LN theo chiều $D$ với epsilon dương. Nếu dùng dropout, đặt trên đầu ra nhánh trước phép cộng đường dư; bật khi huấn luyện và tắt khi đánh giá.
- Ở L12-33/X04, 14,62 là tỷ số đúng cho 65 và 17; 16 chỉ là tỷ số tiệm cận khi bỏ qua CLS.

## Điều hướng

- Có bảy stack ngang. Dùng mũi tên xuống trong mỗi stack và mũi tên phải ở L12-03, 08, 17, 23, 35, 37.
- Stack phụ lục duy nhất gồm L12-X01 → L12-X02 → L12-X03 → L12-X04.
- Kết thúc lõi ở L12-37 sau 100 phút. Nếu cần cắt, bỏ nguyên tuyến mở rộng; không cắt L12-21–23 vì đây là phần đa phương thức của LLO24.

## Đáp án kiểm tra

- L12-08: vị trí che được đọc vị trí hợp lệ ở cả hai phía; chỉ vị trí thuộc $\Omega$ góp trực tiếp vào sai số MLM.
- L12-13: huấn luyện tính đồng thời vì toàn bộ chuỗi nhãn đã có; mặt nạ nhân quả vẫn chặn khóa tương lai. Suy luận phải chờ dự đoán trước.
- L12-17: huấn luyện nhận toàn bộ $Y^{in}$ và tính song song; suy luận bắt đầu từ BOS, sinh tuần tự, dừng theo mẫu tại EOS hoặc giới hạn dài.
- L12-20: không thể kết luận đầu ra luôn đúng, an toàn hoặc phù hợp miền chỉ từ tên gọi LLM; các thuộc tính này cần giao thức đánh giá riêng.
- L12-22: hàng chọn văn bản đúng cho mỗi ảnh; hàng của $S^\top$ chọn ảnh đúng cho mỗi văn bản; cả hai dùng nhãn đường chéo và trung bình trên $N$ cặp.
- L12-23: với $K$ mô tả lớp, nhánh văn bản tạo $E_T^{cls}\in\mathbb R^{K\times D}$; $Z=E_I(E_T^{cls})^\top/\tau\in\mathbb R^{N\times K}$ và softmax chạy theo $K$.
- L12-34: $2\times17\times64$; với $P=4$ có 64 mảnh và 65 ký hiệu kể cả CLS.
- L12-37: biểu diễn đầu vào, luồng chú ý/mặt nạ, điểm–nhãn–sai số, giao thức đánh giá.
- X01: $H[:,0,:]$ có kích thước $N\times D$; phép chiếu tạo $N\times K$.
- X02: dừng khi sinh EOS hoặc đạt giới hạn dài; mẫu đã kết thúc không phát ký hiệu mới.
- X03: vì $E_I=E_T=I_2$ và $1/\tau=\ln3$:

  $$S=\begin{bmatrix}\ln3&0\\0&\ln3\end{bmatrix}.$$

  Mỗi hàng và mỗi cột gán xác suất $3/(3+1)=3/4$ cho cặp đúng, nên $\mathcal L_I=\mathcal L_T=\ln(4/3)$ và $\mathcal L_{CLIP}=\ln(4/3)$. Hai hướng bằng nhau vì $S$ đối xứng và hai cặp có cùng biên điểm.
- X04: mảnh nhỏ giữ chi tiết không gian mịn hơn nhưng tăng độ dài, bộ nhớ và phép tính chú ý.

## Đáp án điều phối thảo luận L12-36

Không đưa bảng này lên mặt trang chiếu hoặc ghi chú diễn giả. Dùng để hỏi tiếp khi nhóm chỉ nêu tên rủi ro mà chưa nêu bằng chứng hoặc hành động.

| Rủi ro đã chọn | Bằng chứng cần thu trước triển khai | Hành động nếu phép kiểm thất bại |
|---|---|---|
| Chênh lệch giữa nhóm người học | Xác định nhóm có căn cứ và hợp pháp; so sánh tỷ lệ lỗi hoặc chất lượng câu trả lời theo nhóm trên cùng giao thức; báo số mẫu và độ bất định. | Sửa dữ liệu hoặc phạm vi dùng, điều chỉnh quy trình duyệt và kiểm tra lại; không triển khai cho nhóm chưa đủ bằng chứng. |
| Lặp lại dữ liệu cá nhân | Kiểm kê nguồn dữ liệu; dùng truy vấn kiểm tra ghi nhớ trên dữ liệu được phép; ghi lại loại thông tin bị lộ và điều kiện truy vấn. | Loại hoặc hạn chế dữ liệu, giới hạn đầu ra/quyền truy cập, bổ sung người duyệt và chạy lại phép kiểm. |
| Thông tin sai nhưng có vẻ chắc chắn | Lập tập câu hỏi tuyển sinh thật có đáp án nguồn; chấm độ đúng, dẫn nguồn và mức độ chắc chắn; tách các câu có hậu quả cao. | Buộc đối chiếu nguồn, hiển thị giới hạn, chuyển câu rủi ro cao cho người phụ trách và thu hẹp phạm vi trả lời. |

Không coi một phép kiểm đơn lẻ là chứng nhận an toàn. Mọi hành động phải được đánh giá lại bằng cùng giao thức sau khi sửa.

## Bài tập 50 phút

1. 10 phút: điền bảng kiến trúc, mặt nạ chú ý, vị trí chịu sai số và ứng dụng cho ba họ.
2. 10 phút: dựng mặt nạ cho hai chuỗi dài 4 và 2 trong cùng lô; ghi riêng mặt nạ chú ý và mặt nạ giám sát.
3. 10 phút: với $N=4,C=3,H=W=64,P=16,D=128,K=10$, tính các kích thước từ ảnh tới điểm phân loại và xác định trục softmax.
4. 20 phút: động não dự án cuối kỳ dùng một kiến trúc Transformer hoặc LLM có sẵn.

### Hoạt động dự án 20 phút

- Mục tiêu: mỗi nhóm đề xuất một dự án có bài toán, dữ liệu, mô hình có sẵn, đầu ra và cách đánh giá đủ cụ thể để kiểm tra tính khả thi.
- Tiến trình: 3 phút chọn bài toán; 7 phút điền phiếu ý tưởng; 5 phút trao đổi chéo giữa hai nhóm; 5 phút sửa và nộp.
- Sản phẩm: một phiếu một trang gồm người dùng hoặc tình huống, dữ liệu có thể tiếp cận, kiến trúc Transformer/LLM dự kiến dùng, cách thích nghi, đầu ra, thước đo, nguồn lực và rủi ro chính.
- Không yêu cầu huấn luyện mô hình trong lớp. Không chấm độ mới lạ nếu ý tưởng không nêu được dữ liệu, đầu ra hoặc cách đánh giá.

### Thang chấm hoạt động dự án — 10 điểm

| Tiêu chí | Điểm | Bằng chứng cần có |
|---|---:|---|
| Tính khả thi | 6 | Dữ liệu có thể tiếp cận (2); mô hình và nguồn lực phù hợp thời gian học phần (2); đầu ra, thước đo và phép kiểm rõ (2). |
| Tính sáng tạo | 4 | Bài toán hoặc cách dùng mô hình có nét riêng và liên quan tình huống (2); lựa chọn Transformer/LLM được giải thích bằng luồng thông tin hoặc mục tiêu đã học (2). |

Nguồn hoạt động và hai tiêu chí: DOCX đề cương, `III.2 → Buổi 12 → Hoạt động/Đánh giá`. Thang chấm chi tiết hóa hai tiêu chí để chấm nhất quán; không phải nội dung từ slide/PDF và không được đưa lên mặt trang chiếu hay ghi chú diễn giả.

## Nguồn CLIP và sai khác triển khai

- Nguồn: Radford và cộng sự (2021), *Learning Transferable Visual Models From Natural Language Supervision*, PMLR 139, PDF 1–3, Hình 1 và Hình 3.
- Ba SVG là bản vẽ lại quan hệ trong Hình 1 và Hình 3; không sao chép bố cục hay ảnh mẫu.
- Ví dụ X03 dùng $N=D=2$, hai ma trận đơn vị và nhiệt độ tự chọn để tạo phép tính chính xác. Đây không phải kết quả thực nghiệm trong bài báo.
- Không dùng benchmark, quy mô tập dữ liệu, chi tiết huấn luyện ngoài PDF 1–3 hoặc khẳng định CLIP là mô hình sinh/có chú ý chéo.

## Hậu kiểm cuối

- Đã duyệt đủ 42 trang ở 1280×720; L12-21–23 và L12-36–37 đã được rà thêm ở 900×720. Không còn tràn hoặc chồng lấn quan sát được.
- Hậu kiểm toán và học thuật sau sửa đều PASS. Nếu tiếp tục đổi L12-21–26 hoặc X03, phải rà lại chuẩn hóa, trục log-softmax, hệ số $1/N$, nhiệt độ, cầu nối ViT→$E_I$ và ký hiệu $E_I,E_T,S,Z$.
- Codex Slides chưa thể nhận Design File do lỗi HTTP 500 của plugin; không xem dự án Codex Slides là bản đã đồng bộ với kho.
