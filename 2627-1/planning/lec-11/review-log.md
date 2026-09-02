# Nhật ký rà soát — Bài 11

## Trạng thái

- Deck trình chiếu: 41 trang lõi/100 phút + 4 trang mở rộng/20 phút.
- Bài tập: đủ 50 phút, gồm 40 phút tính toán và 10 phút phòng máy có nguồn PyTorch 2.13 được duyệt.
- Lỗi chặn về nguồn phòng máy đã được xử lý. Vòng chỉnh sửa này giữ nguyên 45 ID, 7 mạch ngoài, thời lượng 100+20 phút và bài tập 50 phút; trạng thái runtime không được tuyên bố lại trong lượt này.

## Phạm vi worker OpenRouter cho ghi chú — 03-09-2026

- Hồ sơ chỉ đọc đặt tại `/tmp/deep-learning-lec11-dossier.ZAYLJ6`; chỉ gồm tệp UTF-8 đã chọn của dự án. Không chép `.env`, khóa, `.git`, tệp tạm hoặc tài liệu ngoài phạm vi Buổi 11 vào hồ sơ.
- Planner, ba tác tử phân tích nguồn và sáu lượt rà được cấp công cụ chỉ đọc. Mọi kết quả được chấp nhận đều có `requested_model = observed_model = z-ai/glm-5.3-flash`, `provider = OpenRouter`.
- Tác tử soạn dùng `deepseek/deepseek-v4-flash-0731` qua OpenRouter. Công việc được chia thành 10 staging độc lập, mỗi staging chỉ được tạo một `fragment.md`; khóa cứng `MCP_WRITE_POLICY=create-once` và `MCP_MAX_WRITE_CHARS=2500`.
- Phân đoạn 1 thử ghi 3.688 byte và bị từ chối toàn bộ trước khi tạo tệp vì vượt giới hạn; lần sau ghi 2.333 ký tự, 2.700 byte và được chấp nhận. Phân đoạn 4 nhận một phản hồi rỗng, được cầu nối thử lại theo cấu hình rồi ghi 2.448 ký tự. Chín phân đoạn còn lại có 1.664–2.499 ký tự. Không có ghi dở hoặc ghi đè.
- Phạm vi DeepSeek chỉ là các mục đã khóa: mở đầu/ký hiệu; cầu nối QKV; vết tính đầu 1; mặt nạ; ba loại chú ý; nhiều đầu; vị trí; khối; ngăn xếp/đầu ra; bài tập. DeepSeek không được sửa tệp dự án, planning, deck, CSS, SVG, index hoặc chọn thêm nguồn.
- Ba phần đầu ra bị loại khi hợp nhất: mô tả tần số sin–cos bị đảo; đáp án chuẩn hóa tầng bị hỏng; nhãn nội bộ và chỉ dẫn quy trình lọt vào bản nháp. Bản công khai do điều phối viên ghép và kiểm lại từ nguồn, không sao chép mù đầu ra worker.
- Điều chỉnh này là quy tắc bền vững cho các buổi sau: nếu một mảnh chạm giới hạn, mở task mới với phạm vi hẹp hơn; không tăng trần, không cấp quyền cập nhật và không chuyển cả kho cho writer.

## Rà ghi chú bài giảng — 03-09-2026

- Tạo `materials/lec-11/lecture-note.md`, dùng đủ 12 SVG hiện có và thêm liên kết trong `index.html`.
- Rà toán học phát hiện hàng thứ hai của vết tính nhân quả bị sai trong cả bản nháp ghi chú và deck: hai điểm hợp lệ là $(.707,.707)$ nên softmax bằng $(.5,.5)$, không phải $(.330,.670)$. Ghi chú đã sửa thành $A_{causal}[2,:]=(.5,.5,0)$ và $O_{causal}[2,:]=(.5,.5)$; deck được để lại cho pha căn chỉnh riêng để giữ mốc commit độc lập.
- Hai báo cáo khác lặp lại $(.330,.670)$ do đọc nhầm cặp điểm thành $(0,.707)$. Quyết định dùng phép tính trực tiếp từ ma trận $S^{(1)}$ và mặt nạ $j\le i$; báo cáo đồng thuận không thay thế phép kiểm số.
- Chuẩn hóa mặt nạ công khai thành $B\times1\times T_q\times T_k$ phát qua trục đầu; thêm lý do chọn ma trận ví dụ, định nghĩa BOS/EOS, `teacher forcing`, ổn định số của chéo entropy, vai trò dropout và câu nối $H_0\to\operatorname{MHA}(H_0)$.
- Tách ranh giới đọc trong cụm ba loại chú ý/nhiều đầu; thêm so sánh định lượng RNN–tích chập–tự chú ý từ đúng dải giáo trình; kết luận thu hồi vấn đề đường truyền tuần tự.
- `lec15_attention.pdf` PDF 41 bị bỏ vì chỉ là hình minh họa/liên kết ngoài, không thêm nội dung cho LLO21–22; nội dung kiến trúc cần thiết đã được giữ và vẽ lại từ các trang 42, 45 và 46.
- Một lượt phản biện học thuật ban đầu hết hạn phản hồi 240 giây và không tạo báo cáo hợp lệ; không dùng kết quả dở. Lượt rà lại phạm vi ngắn được chạy sau chỉnh sửa.

## Quyết định học thuật và sửa lỗi nguồn

| Vùng | Vấn đề nguồn | Quyết định |
|---|---|---|
| L11-10 | Slide ghi `softmax(..., dim=1)` theo bố cục minh họa, mơ hồ khi chuyển sang tensor. | Khóa trục cuối là khóa $T_k$; hàng là truy vấn, cột là khóa. |
| L11-34 | Slide LN dùng ký hiệu độ lệch chuẩn/phương sai không nhất quán và thiếu căn, epsilon. | Dùng $\sqrt{\sigma^2+\varepsilon}$, $\varepsilon>0$, chuẩn hóa theo $D$ cho từng mẫu/vị trí. |
| L11-36 | Slide nguồn ghi cấu hình không nhất quán: $N=12$ nhưng chỉ ghi 6 đầu chú ý. Nguồn duyệt không đủ để sửa hoặc chuẩn hóa cấu hình này. | Giữ dấu vết lỗi tại đây; bỏ hoàn toàn claim cấu hình khỏi deck và chỉ giữ phát biểu số tầng, số đầu là siêu tham số. |
| L11-05–13, L11-30, L11-X01 | Ánh xạ cũ gán `lec15_attention.pdf` PDF 36 cho trace công thức L11-05–13, nhưng trang nguồn này phục vụ lập luận hoán vị và động cơ vị trí. | Chuyển đích chính sang L11-X01 và liên hệ phát biểu mở ở L11-30; không dùng PDF 36 làm nguồn cho trace số. |
| L11-31 | Giá trị cuối của $PE_1$ hiển thị là 1 dưới dấu xấp xỉ nhưng ghi chú chưa nêu phép làm tròn. | Ghi rõ $\cos(1/100)\approx0.99995$ được làm tròn thành 1. |
| L11-38 | Cách viết $N_M=\sum M>0$ trộn định nghĩa với giả thiết dương, dễ đọc thành một chuỗi đẳng thức–bất đẳng thức. | Tách thành $N_M=\sum_{n,t}M_{n,t}$ và $N_M>0$; đồng bộ HTML, storyboard và ghi chú. |
| L11-25–28 | Sau cụm nhân quả, bản cũ không nói rõ trace nhiều đầu quay lại cấu hình không mặt nạ; nguồn của $O^{(1)}$ tại phép ghép còn mơ hồ. | Ghi rõ cả hai đầu dùng $B_M=0$ và $O^{(1)}$ lấy từ L11-13, không lấy kết quả nhân quả L11-17. |
| L11-40 | Câu hỏi tổng kết chưa kiểm tra trực tiếp LLO21 về luồng bộ mã hóa–bộ giải mã. | Thay ý kiểm tra PE bằng truy vết $H^{src}_0\to H^{enc}$; thêm nguồn đầu vào của tự chú ý nhân quả, chú ý chéo và FFN trong một tầng giải mã; đồng bộ đáp án và storyboard với L11-36–37. |
| L11-40–X04 | Phụ lục chưa được định khung như một tuyến có chức năng sau phần lõi. | Dùng bốn phép kiểm sức chịu: đối xứng, chi phí, tham số, vị trí; chốt đây là các đánh đổi mở rộng, không thay bốn hợp đồng lõi. |
| L11-35 | Nguồn chính dùng Add & Norm sau mỗi nhánh. | Giữ chuẩn hóa sau xuyên B11; xóa nội dung pre-norm ngoài nguồn khỏi X04. |
| L11-09–11,23 | Bản trước đưa trục đầu vào mặt nạ trước khi giới thiệu MHA, khiến phép cộng giữa tensor ba và bốn chiều không nhất quán. | Trước L11-25 dùng $S,B_M,A:B\times T_q\times T_k$ và $(B_M)_{n,i,j}$; từ L11-25 mới mở mặt nạ thành $B\times1\times T_q\times T_k$ để phát qua $H_a$ đầu. |
| L11-22 | Nguồn nêu mặt nạ nhưng không quy định cách xử lý hàng bị chặn hoàn toàn. | “Bỏ qua/đưa đầu ra hàng về không” là suy diễn triển khai có chủ ý từ việc softmax của hàng toàn $-\infty$ không xác định; không trình bày như quy tắc duy nhất của nguồn. |
| L11-38–39 | Ký hiệu $A,V$ cho điểm từ vựng xung đột với trọng số chú ý và tensor giá trị. | Dùng $Z$, $W_{vocab}$, $b_{vocab}$, $|V_{tgt}|$; thêm log-sum-exp ổn định và CE có mặt nạ với mẫu số dương. |
| L11-23–38 | Trích dẫn trang nguồn bị lệch giữa positional/MHA/FFN/LN/kiến trúc đầy đủ. | Đối chiếu lại trang thật: `lec15` PDF 43–47 và `lec16` PDF 22, 26, 28, 33, 36; PDF 47 của `lec15` là kết quả và không dùng. |
| L11-25–31 | Mạch deck đặt chú ý nhiều đầu trước mã hóa vị trí, khác thứ tự nguồn. | Giữ thứ tự này để hoàn tất phép tính hai đầu trên $X$ thô trước; sau đó mới tạo đầu vào đầy đủ $H_0=X+PE$. Cách cô lập này tránh đổi số giữa trace MHA và trace vị trí. |
| L11-X04 | So sánh pre-norm/post-norm không có nguồn duyệt trong phạm vi B11. | Xóa và thay bằng quan hệ độ lệch của mã hóa sin–cos từ `lec16` PDF 22 và GT PDF 268. |
| L11-X04 | Ma trận quay in tại GT PDF 268 có dấu không khớp quy ước $[\sin(p\omega),\cos(p\omega)]$ ngay trước đó. | Giữ kết luận có nguồn rằng phép biến đổi chỉ phụ thuộc độ lệch; sửa dấu bằng cách tự kiểm hai công thức cộng góc và ghi ma trận đúng trong deck. |
| L11-28,31,36–37 | Hậu kiểm phát hiện va ký hiệu, thiếu trục lô trong chỉ số và đường dư chưa hiện rõ trên SVG. | Đổi đầu ra nhiều đầu thành $O_{MHA}$; dùng $H_0[0,0,:]$; thêm Dropout vào mọi nhánh và vẽ hai/ba mũi tên dư tới đúng hộp Cộng+LN. |
| BT11-04 | DOCX yêu cầu khảo sát mã cài đặt tự chú ý nhưng các slide và giáo trình ban đầu không có mã hoặc hợp đồng API. | Người dùng duyệt hai tài liệu PyTorch 2.13 ngày 27-08-2026. Dùng SDPA và MHA để kiểm tra kích thước, `batch_first`, mặt nạ Boolean đối nghịch và dropout khi đánh giá. |
| BT11-04 | SDPA và MHA diễn giải `True` khác nhau trên mặt nạ Boolean. | Dùng `keep_mask` cho SDPA và `block_mask = ~keep_mask` cho MHA; yêu cầu sinh viên giải thích phép phủ định thay vì chỉ chạy mã. |
| BT11-04 | SDPA luôn áp dụng dropout theo `dropout_p`, không tự đọc trạng thái `eval()` của mô-đun gọi. | Đặt `dropout_p=0.0` cho SDPA trong lần chạy đánh giá; cấu hình dropout của MHA là `0.1` nhưng gọi `eval()` để tắt khi đánh giá. |
| BT11-01–04 | Bản lab cũ mô tả như thể cùng tensor được truyền từ ba bài tính toán sang bài chạy API. | Khóa tuyến tái áp dụng hợp đồng và kỹ năng: phép tính Q/K/V và softmax → quy tắc mặt nạ → kích thước nhiều đầu → kiểm chứng SDPA/MHA; mỗi bài dùng dữ kiện riêng. |
| BT11-04 | Bốn yêu cầu ban đầu khó hoàn tất trong 10 phút nếu vừa cài môi trường vừa thử đổi `batch_first`. | Chốt nhịp 1–2–4–3 phút; chuyển thử `batch_first=False` thành tùy chọn và yêu cầu chuẩn bị sẵn PyTorch 2.13 trên CPU trước lớp. |
| L11-27 | $O^{(2)}$ được tính từ trọng số đầy đủ nhưng hiển thị $.751/.496$, không khớp làm tròn ba chữ số. | Sửa thành $.752/.497$ và ghi rõ chỉ làm tròn sau phép nhân. |
| L11-36–37 | Công thức cũ chỉ mô tả một khối từ $H_0$ tới đầu ra nên chưa cho thấy truy hồi qua nhiều tầng hoặc đầu ra sau $L_{enc}/L_{dec}$. | Dùng $H^{src}_{\ell-1}\to H^{src}_\ell$, $G_{\ell-1}\to G_\ell$; định nghĩa $H^{enc}=H^{src}_{L_{enc}}$, $H^{dec}=G_{L_{dec}}$. SVG ghi lặp tầng và Bỏ ngẫu nhiên trên từng nhánh. |
| L11-36–37 | Ghi chú cũ không dẫn lời giảng theo đúng thứ tự mũi tên và công thức. | Viết lại mạch nói theo từng nhánh và từng phép Cộng+LN. Giữ 4 phút mỗi trang vì tổng lõi 100 phút đã khóa; kiểm trực quan sau sẽ xác nhận khả năng đọc. |
| L11-38 | Công thức LSE chiếm chỗ nhưng cặp chuỗi dịch nhãn vẫn trừu tượng. | Thêm `[BOS,tôi,học]`/`[tôi,học,EOS]`; giữ loss log-softmax có mặt nạ trên slide và chuyển khai triển LSE ổn định vào notes. |
| BT11-04 | Lab cũ chỉ đối chiếu hai API nên chưa kiểm chứng phép tính tay với SDPA trên cùng dữ kiện; MHA có phép chiếu riêng nên đầu ra không thể so trực tiếp với SDPA. | Thêm nhánh thủ công điểm→scale→mask→softmax→$AV$, dùng cùng Q/K/V/mặt nạ với SDPA và `torch.testing.assert_close`. Giữ MHA để khảo sát giao diện/mặt nạ, dùng `inference_mode`, cấm so hai đầu ra; `batch_first` là điểm thưởng. |

## Xử lý bốn báo cáo độc lập

- Sửa ký hiệu đầu ra từ vựng, hàm mất mát ổn định và mặt nạ ký hiệu tại L11-38.
- Mở rộng L11-36–37 thành trace đầy đủ của bộ mã hóa và bộ giải mã; hai SVG ghi rõ từng lần Cộng+LN.
- Tổng quát hóa MHA tại L11-25 và nối trực tiếp nguồn Q/K/V của chú ý chéo tại L11-37.
- Chuyển công thức sin–cos sang L11-30; L11-31 giữ ví dụ số, sửa chỉ số thành $H_0[0,0,:]$, nối $H_0$ với Q/K/V và thêm câu hỏi kích thước.
- Thống nhất ký hiệu mặt nạ trước/sau khi có trục đầu; thêm giả thiết cho lập luận phương sai và shape của $\gamma,\beta$.
- Tăng `.small` từ `.84em` lên `.88em`, tương đương khoảng `.757em` so với cỡ Reveal gốc khi slide dùng `.86em`.
- Viết đủ đề, dữ kiện, sản phẩm, rubric và đáp án cho 40 phút bài tập có nguồn; thêm bài tập về nhà theo DOCX.
- Bản rà trước giữ nguyên lỗi chặn phòng máy 10 phút vì khi đó chưa có nguồn code/API được duyệt.

## Hợp nhất năm báo cáo mới

| Vai rà soát | Mức cao nhất | Vấn đề chính | Quyết định chỉnh sửa |
|---|---|---|---|
| Góc nhìn sinh viên | trung bình | L11-31 dồn hình, số, công thức Q/K/V và câu hỏi; bốn câu L11-40 khó trả lời đồng loạt. | Chuyển Q/K/V sang notes; tại L11-40 cho sinh viên chọn câu, giảng viên chốt theo tensor hoặc sơ đồ; kịch bản chi tiết đặt trong ghi chú người soạn. |
| Chuyên gia Học sâu | nhẹ | Viết tắt LLO/MHA/BOS/EOS, tiêu đề L11-13, bảng ánh xạ chồng L11-03 và quyết định hàng toàn chặn cần rõ hơn. | Mở rộng thuật ngữ ở lần đầu; sửa tiêu đề và bảng ánh xạ; ghi zero/skip là suy diễn triển khai có chủ ý. |
| Chính xác toán học, thuật toán và triển khai | nhẹ | Các tổng trọng số hiển thị lệch $1$ do làm tròn; môi trường phòng máy vẫn cần kiểm tra đúng PyTorch 2.13. | Giữ số vì deck đã ghi rõ sai số làm tròn; chạy lại lab trên PyTorch 2.13.0+cpu và giữ yêu cầu preflight trước buổi học. |
| Phản biện học thuật và giảng dạy | trung bình | Đáp án L11-24 thêm trục đầu trước khi khái niệm nhiều đầu xuất hiện; tham chiếu sớm tới trục đầu và lý do đảo MHA trước vị trí chưa đủ rõ. | Khóa $A:B\times3\times5$ tại L11-24, chỉ mở thành $B\times H_a\times3\times5$ từ L11-25; sửa câu dẫn và ghi lý do cô lập MHA trên $X$ thô. |
| Kết nối và mạch viết | trung bình | Storyboard thiếu bản đồ chức năng của 7 mạch; kết luận chưa thu hồi vấn đề xử lý tuần tự và tuyến mở rộng chưa có câu chốt. | Thêm bảng 7 mạch với kết nối vào/ra và LLO; sửa L11-40 thu hồi mở bài; dùng X01 như phép kiểm chứng lại và X04 để khép tuyến mở rộng. |

Đề xuất tách L11-30 thành hai luận điểm không áp dụng: mệnh đề hoán vị tạo trực tiếp nhu cầu thêm $PE$, nên vấn đề và lời giải thuộc cùng một bước học tập; tách trang sẽ đổi số trang và timing. Phân tầng hiện có bằng hộp mệnh đề, công thức và dòng kết luận; không thêm CSS. Hướng dẫn mở notes để tự học cũng không đưa lên slide hoặc notes; nếu cần triển khai, chỉ ghi trong `note-for-author.md`.

## Sai khác có chủ ý

- Trace $B=1,T=3,D=4,d_k=d_v=2$, hai bộ ma trận chiếu và mọi kết quả số đều do deck tự dựng để minh họa công thức; không phải bằng chứng thực nghiệm.
- Chọn $W_O=I_4,b_O=0$ để trace ghép đầu có thể kiểm tay.
- Vẽ lại 12 sơ đồ kỹ thuật bằng SVG; không sao chép raster hoặc hình phụ thuộc mạng.
- Bỏ trang kết quả nguồn và các trang ngoài dải đã duyệt.
- Trước ngày 27-08-2026, không tạo mã hoặc giả mã cho phòng máy vì nguồn chưa đủ. Sau khi người dùng duyệt nguồn PyTorch, bổ sung mã tối thiểu theo đúng hợp đồng API và giữ quyết định cũ làm dấu vết.
- Mã lab tự dựng tensor đầu vào nhỏ để kiểm tra API; không trình bày kết quả như bằng chứng thực nghiệm.
- Phạm vi nguồn PyTorch chỉ gồm chữ ký API, kích thước, mặt nạ, `batch_first`, `is_causal`, `dropout_p` và đầu ra. Lab không dùng kernel tối ưu, benchmark hoặc GQA.
- Ví dụ MHA dùng $X$ để cô lập cơ chế; tầng Transformer đầy đủ bắt đầu bằng $H_0=X+PE$. Lý do này được nêu trên L11-31 và trong storyboard.
- Đầu ra sau chiếu nhiều đầu dùng $O_{MHA}$ để không va với $Y^{in},Y^{out}$ của chuỗi đích.
- Không áp đặt cách triệt truy vấn đệm theo tầng vì nguồn duyệt chỉ đủ cho mặt nạ khóa và loại ký hiệu đệm khỏi sai số.

## Rà no-ai-slop và Quill

- Mỗi trang giữ một luận điểm; thuật ngữ truy vấn/khóa/giá trị, điểm/trọng số/đầu ra được dùng nhất quán; $A$ chỉ là trọng số chú ý và $Z$ chỉ là điểm từ vựng.
- Các chu trình đi từ vấn đề và trace số đến công thức, triển khai và kiểm tra.
- BT11-04 nối trực tiếp hợp đồng tensor ở L11-20/23/25 với hai API; thuật ngữ `keep_mask` và `block_mask` giữ nguyên từ đề đến mã, đầu ra và rubric.
- Bốn bài tập tạo một tuyến tái áp dụng hợp đồng và kỹ năng; BT11-04 dùng dữ kiện mới để kiểm tra bằng API các phép tính, mặt nạ và kích thước đã luyện ở BT11-01–03.
- Không có chỉ dẫn người soạn, timing, tuyến cắt hoặc đáp án trong mặt slide/notes.
- Không tạo `quill.json`.

## Kiểm định tĩnh

- HTML có 45 ID duy nhất, 45 ghi chú nguồn và cấu trúc section cân bằng.
- Storyboard có đúng 45 hàng theo cùng thứ tự ID; timing tính lại là lõi 100 phút và mở rộng 20 phút.
- Cấu hình HTML vẫn giữ `throwOnError: true` và `strict: "error"`; lượt này chỉ kiểm tĩnh chuỗi cấu hình, không tuyên bố kết quả dựng công thức runtime.
- Mọi CSS/JS/SVG được tham chiếu đều là tài nguyên cục bộ và tồn tại; không có raster hoặc phụ thuộc mạng.
- 12/12 SVG hợp lệ XML, có `role="img"`, `title`, `desc`; cỡ chữ khai báo nhỏ nhất 24 px.
- `convert` và `montage` dựng lại thành công hai SVG encoder/decoder sau sửa; đã xem montage, sửa nhãn encoder bị đè đường dư. Hai tệp vẫn hợp lệ XML và giữ nhãn chính 34 px/32 px; nhãn Bỏ ngẫu nhiên nhỏ nhất 25 px trong SVG decoder.
- Không có control byte, tiêu đề chứa thuật ngữ nội bộ bị cấm hoặc `quill.json`.
- Runtime BT11-04 mới: **PASS** bằng PyTorch 2.13.0+cpu trên CPU. `torch.testing.assert_close` xác nhận phép tính thủ công khớp SDPA; bốn kích thước và hai ma trận mặt nạ khớp đầu ra dự kiến. Cảnh báo thiếu NumPy trong môi trường kiểm thử tối giản không ảnh hưởng đoạn mã hoặc kết quả.
- Bản in Reveal phát hiện L11-31 tràn sang một trang PDF riêng cho hộp Câu hỏi, làm tổng PDF thành 46 trang. Giữ nguyên cỡ chữ, ID và timing; giới hạn hình `positional-encoding.svg` ở chiều cao 210 px để nội dung nằm lại trên một trang chiếu.
- Môi trường phòng máy vẫn phải qua preflight PyTorch 2.13 trên CPU trước giờ học; thời gian cài đặt không tính vào 10 phút lab.
- Chromium in Reveal ở khung 1280×720 cho đúng 45 trang sau vá L11-31; đã rà toàn bộ contact sheet, không có tràn, chồng lấn hoặc cắt nội dung. Ảnh chụp khung hẹp 900×720 của L11-31, L11-36, L11-37 và L11-38 đều đọc được, không bị cắt.
- Lượt chỉnh sửa này không đánh giá hoặc tuyên bố trạng thái Codex Browser.

## Kiểm định cuối của điều phối viên — 30-08-2026

- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`; điều phối viên dùng `python3 -m http.server 8765 --bind 127.0.0.1` và chỉ phục vụ thư mục `2627-1/`.
- Chromium headless duyệt đủ 45 trang ở khung $1280\times720$ và $900\times720$, tạo 90 ảnh kiểm tra. Không có tài nguyên hỏng, ảnh thiếu, công thức cắt hoặc chồng lấn; cảnh báo biên tại trang bìa là dương tính giả của bố cục tiêu đề và đã được kiểm tra trực quan.
- KaTeX dựng 195 biểu thức, gồm 10 công thức khối, với `throwOnError: true` và `strict: "error"`; không có lỗi KaTeX. Cảnh báo HTTP duy nhất là `favicon.ico` trả 404, không phải tài nguyên cốt lõi.
- Đúng 45 ghi chú, bảy mạch ngoài có kích thước 4, 11, 10, 5, 6, 5, 4 và trang cuối là L11-X04. Sáu tuyến phím Phải qua ranh giới mạch và tuyến đi xuống X01 → X02 → X03 → X04 đều đạt.
- Khối mã BT11-04 được chạy lại bằng PyTorch 2.13.0+cpu trên CPU: phép tính thủ công khớp SDPA qua `torch.testing.assert_close`; bốn kích thước và hai mặt nạ đúng. Cảnh báo thiếu NumPy của môi trường tối giản không ảnh hưởng kết quả.
- Danh sách toàn bộ tiêu đề `h1`, `h2`, `h3` đã được rà thủ công; tiêu đề thuần Việt, chỉ giữ tên riêng Transformer và các thuật ngữ/ký hiệu chuẩn như RNN, softmax.
- Công cụ thao tác Codex Slides trong Browser không có trong môi trường hiện tại; bằng chứng trực quan cuối dùng Chromium cục bộ trên đúng tệp được máy chủ phục vụ.

## Hậu kiểm chỉnh sửa storyboard

- Đã đóng phát hiện về mạch kết luận và tuyến mở rộng: tiêu đề tổng kết nói chính xác việc thay đường truyền trạng thái tuần tự bên trong khối, notes giữ ngoại lệ suy luận tự hồi quy, rồi nối bốn phép kiểm theo chuỗi đối xứng → chi phí ma trận điểm → số tham số → cấu trúc vị trí. Không đổi ID, cấu trúc hoặc timing.
- Đã đối chiếu lại citation trong L11-23–38 và hai trang lân cận: `lec15` PDF 43 positional, 44 MHA, 45 khối Transformer, 46 kiến trúc đầy đủ, 47 kết quả không dùng; `lec16` PDF 22 positional, 26 MHA, 28 FFN, 33 LayerNorm, 36 kiến trúc đầy đủ.
- Đã chuẩn hóa $B$ là ký hiệu cỡ lô trong HTML, SVG và planning; $n$ chỉ còn là chỉ số mẫu, còn $L$ là số tầng trong sơ đồ encoder.
- Bộ phân tích XML chuẩn của Python đọc thành công 12/12 SVG; môi trường không có `xmllint`.

## Lịch sử xử lý nguồn phòng máy

- Bản nháp đầu ghi trạng thái **CHƯA ĐẠT** và không tự chọn thư viện, vì nguồn được duyệt khi đó không có code/API.
- Ngày 27-08-2026, người dùng duyệt tài liệu chính thức PyTorch 2.13 về `scaled_dot_product_attention` và `MultiheadAttention`; hai bản HTML được lưu cục bộ trong `source-materials/resources/` và ánh xạ trong `source.md`.
- Sau phê duyệt, BT11-04 được bổ sung vào bốn tệp planning. Khoảng trống nguồn 10 phút đã đóng; HTML/SVG/index không thuộc lượt sửa này.

## Xử lý vòng bốn báo cáo mới

- Chuyên gia/storyboard: làm rõ truy hồi và đầu ra cuối của $L_{enc}/L_{dec}$ tầng tại L11-36–37; giữ nguyên ID và 4+4 phút.
- Toán học/triển khai: sửa làm tròn L11-27; đổi BT11-04 thành kiểm chứng thủ công≈SDPA trên cùng dữ kiện và tách MHA khỏi phép so sánh đầu ra.
- Góc nhìn sinh viên: thêm cặp chuỗi cụ thể ở L11-38, chuyển khai triển LSE vào notes và biến `batch_first=False` thành điểm thưởng.
- Học thuật/giảng dạy: giữ mạch chuẩn hóa sau của Transformer gốc, bổ sung nhãn lặp tầng và Bỏ ngẫu nhiên trong hai SVG thay vì thêm trang.
- QA của vòng trước được giữ làm lịch sử; lượt chỉnh sửa hiện tại không tuyên bố trạng thái Codex Browser hoặc KaTeX runtime.

## Kiểm định cuối ghi chú — 03-09-2026

- Lượt phản biện học thuật thứ hai tiếp tục hết hạn ở 120 giây và không tạo báo cáo hợp lệ. Lượt thứ ba dùng cùng model, chỉ đọc duy nhất `lecture-note.md`, tối đa bốn vòng và thời hạn 300 giây; kết quả hợp lệ xác nhận `requested_model = observed_model = z-ai/glm-5.3-flash`, `provider = OpenRouter`, không còn lỗi chặn bàn giao hoặc nghiêm trọng.
- Lượt rà toán học sau sửa xác nhận hàng thứ hai của ghi chú là $(.5,.5,0)$ và mọi công thức, kích thước, tham số, mã hóa vị trí, hàm mất mát và bài lab còn lại đều đúng. Báo cáo giữ lỗi cùng vị trí trong deck để xử lý ở pha căn chỉnh.
- Bộ kiểm tĩnh đọc đúng một H1, 28 chỉ thị mở/đóng, dựng 175 biểu thức bằng KaTeX với `throwOnError: true`, `strict: "error"`; dùng đủ 12 SVG và không có lỗi.
- Chromium duyệt trình xem tại 1280×720 và 390×844: 175 biểu thức, 12 ảnh, 7 khối lời giải, không ảnh hỏng, lỗi runtime hoặc cuộn ngang ngoài ý muốn; bàn phím, liên kết bỏ qua điều hướng, bản in, chặn đường dẫn vượt thư mục và chặn ghép sai buổi đều đạt.
- Rà trực tiếp theo `no-ai-slop/eval.md`: giữ giọng học thuật ngắn, bỏ nhãn nội bộ và bốn dấu gạch ngang trang trí trong tên bài tập; không có từ cấm, mở bài vòng vo, kết luận giả sâu, lời quảng bá, chỉ dẫn người viết hay dấu vết worker. Không thêm mệnh đề ngoài nguồn.
- Rà mạch theo nguyên tắc Quill: ký hiệu $X,Q,K,V,S,A,O,H_0,H^{enc},H^{dec},Z$ tích lũy theo đúng thứ tự; mỗi cụm nối đầu ra sang cụm kế; kết luận thu hồi vấn đề xử lý tuần tự và nối rõ sang Buổi 12. Không tạo `quill.json`.
- Codex Slides trong Browser không có trong môi trường hiện tại; kiểm định trực quan dùng Chromium cục bộ trên đúng URL được máy chủ phục vụ và ghi rõ giới hạn này thay vì tuyên bố đã dùng Codex Slides.
