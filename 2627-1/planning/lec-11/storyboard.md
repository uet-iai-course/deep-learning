# Storyboard — Bài 11

## Điều hướng và quy ước

- Sáu stack lõi ngang: L11-00–03; L11-04–14; L11-15–24; L11-25–29; L11-30–35; L11-36–40.
- Một stack phụ lục dọc: L11-X01 → X02 → X03 → X04. Dùng `↓` trong stack và `→` tại trang cuối stack.
- Vai trò: **VĐ** vấn đề, **TG** trực giác, **VD** ví dụ, **HT** hình thức/tính toán, **UD** triển khai/ứng dụng, **KT** kiểm tra. `KAD` luôn kèm lý do.

## Bảy mạch trình bày

| Mạch ngoài | Chức năng | Kết nối vào và dữ kiện truyền | Kết nối ra | Đóng góp kết quả học tập |
|---|---|---|---|---|
| L11-00–03 | Mở vấn đề xử lý tuần tự và nối chú ý chéo của bài trước sang tự chú ý. | Kiến thức Bài 10, nguồn Q/K/V và giới hạn đường truyền theo chuỗi. | Khóa tensor $X$ và câu hỏi nguồn Q/K/V cho trace số. | Đặt đích cho LLO21; mở cơ chế của LLO22. |
| L11-04–14 | Tính trọn một đầu chú ý không mặt nạ. | $X:B\times T\times D$, ba phép chiếu và quy ước hàng truy vấn/cột khóa. | $O^{(1)}$ và hợp đồng kích thước trước khi thêm mặt nạ. | Kiểm chứng tự chú ý bằng phép tính cụ thể cho LLO22. |
| L11-15–24 | Thêm nhân quả, đệm và phân biệt ba loại chú ý. | Điểm và đầu ra của trace đầu 1; tập khóa hợp lệ. | Chú ý chéo có $A:B\times3\times5$ trước khi xuất hiện trục đầu; hợp đồng mặt nạ. | Nối cơ chế chú ý với bộ mã hóa–giải mã cho LLO21–22. |
| L11-25–29 | Mở rộng trace sang chú ý nhiều đầu rồi ghép và chiếu ra. | Quay lại $X$ không mặt nạ, $B_M=0$ cho hai đầu; $O^{(1)}$ từ L11-13. | $O_{MHA}:B\times T\times D$ và phép đếm 64/80 tham số. | Hoàn tất phần chú ý nhiều đầu của LLO22. |
| L11-30–35 | Bổ sung vị trí và dựng khối Transformer chuẩn hóa sau. | $X$ thô đã dùng để cô lập MHA; mệnh đề tương đương hoán vị. | $H_0=X+PE$ và hợp đồng MHA–FFN–đường dư–LN. | Hoàn tất mã hóa vị trí của LLO22, chuẩn bị kiến trúc của LLO21. |
| L11-36–40 | Ghép và lặp các khối thành bộ mã hóa, bộ giải mã, mục tiêu huấn luyện và suy luận. | $H_0^{src},H_0^{tgt}$, mặt nạ nguồn/nhân quả và đầu ra MHA. | $H^{enc}$, $H^{dec}$, điểm từ vựng, sai số và bốn hợp đồng tổng kết. | Kiểm tra trực tiếp LLO21 và thu hồi vấn đề xử lý tuần tự; củng cố LLO22. |
| L11-X01–X04 | Kiểm chứng lại đối xứng và suy các đánh đổi mở rộng. | Bốn hợp đồng lõi, mệnh đề hoán vị, kích thước điểm và số tham số. | Kết luận về đối xứng, chi phí $T^2$, số đầu và cấu trúc vị trí tương đối. | Mở rộng khả năng phản biện mà không đổi phạm vi LLO21–22. |

Ranh giới L11-24→25 cố ý hoàn tất mặt nạ và nguồn Q/K/V trước khi thêm trục đầu. Ranh giới L11-29→30 cố ý hoàn tất phép tính MHA trên $X$ thô rồi mới thêm $PE$: thứ tự này cô lập hai cơ chế, giữ nguyên trace số và tránh làm lại toàn bộ Q/K/V sau khi đổi đầu vào thành $H_0$.

## Từng trang

| ID | Phút | Sáu vai trò | Đầu vào → đầu ra; dữ kiện truyền | Chuyển ý và điều hướng |
|---|---:|---|---|---|
| L11-00 | 2 | VĐ: phạm vi; TG/VD/HT/UD/KT: KAD vì là bìa. | Tên buổi → chủ đề kiến trúc. | Mở LLO; `↓` 01. |
| L11-01 | 3 | VĐ: sản phẩm cần đạt; TG: truy vết tensor; VD/HT/UD/KT: KAD vì là hợp đồng học. | Tiên quyết → LLO21–22. | So sánh ba họ xử lý chuỗi; `↓` 02. |
| L11-02 | 3 | VĐ: phụ thuộc dài; TG: đường thông tin; VD: RNN/tích chập/Transformer; HT: KAD vì chưa cần công thức; UD: encoder đọc mọi khóa nguồn hợp lệ trong một tầng, decoder chỉ đọc tiền tố; KT: câu hỏi mở đầu. | Kiến thức B07–10 → động cơ Transformer và phạm vi khóa của hai nhánh. | Nối attention B10; `↓` 03. |
| L11-03 | 3 | VĐ: truy vấn lấy từ đâu; TG: đổi nguồn QKV; VD: SVG; HT: nguồn Q/K/V; UD: chọn loại chú ý; KT: KAD vì L24. | Chú ý chéo B10 → tự chú ý. | Khóa trace số; `→` 04. |
| L11-04 | 2 | VĐ: cần ví dụ kiểm tay; TG: bỏ trục lô tạm thời; VD: $X$; HT: $B,T,D,d_k,d_v$; UD: khôi phục trục lô; KT: kiểm ba hàng. | $X:3\times4$ → hợp đồng trace. | Tạo QKV; `↓` 05. |
| L11-05 | 2 | VĐ: một tensor cần ba vai trò; TG: tìm/cung cấp/nội dung; VD: sơ đồ; HT: $XW_Q,XW_K,XW_V$; UD: tham số học; KT: KAD vì L14. | $X,D$ → Q,K,V và kích thước. | Chọn ma trận đầu 1; `↓` 06. |
| L11-06 | 2 | VĐ: biến công thức thành số; TG: chọn cặp chiều; VD: $W^{(1)}$; HT: nhân ma trận; UD: KAD vì là trace; KT: kiểm Q=K. | $X$ → $Q^{(1)},K^{(1)},V^{(1)}$. | So khớp mọi cặp; `↓` 07. |
| L11-07 | 2 | VĐ: mỗi truy vấn cần so với mọi khóa; TG: hàng/cột; VD: SVG; HT: $QK^\top$; UD: ma trận tương thích; KT: kiểm $3\times3$. | Q,K đầu 1 → điểm thô. | Scale điểm; `↓` 08. |
| L11-08 | 3 | VĐ: tích vô hướng tăng độ lớn theo chiều; TG: phương sai với trung bình gần 0 và tích gần không tương quan; VD: ma trận số; HT: chia $\sqrt{d_k}$; UD: giữ softmax ổn định; KT: caveat xấp xỉ. | Điểm thô → $S^{(1)}$. | Chèn mặt nạ trước softmax; `↓` 09. |
| L11-09 | 3 | VĐ: khóa nào được phép; TG: Boolean↔cộng; VD: SVG; HT: $S,B_M,\widetilde S:B×T_q×T_k$ và $(B_M)_{n,i,j}$; UD: cộng hai tensor cùng shape; KT: KAD vì L24. | $S:B×T_q×T_k$ + mặt nạ cùng shape → điểm đã che. | Chuẩn hóa theo khóa; `↓` 10. |
| L11-10 | 3 | VĐ: trục softmax mơ hồ; TG: mỗi truy vấn phân phối trên $\mathcal K_i$; VD: một hàng; HT: $A_{n,i,j}$ và $A:B×T_q×T_k$ trước MHA; UD: trục khóa; KT: tổng hàng 1. | Điểm ba chiều đã che → $A$ ba chiều. | Tính số đầu 1; `↓` 11. |
| L11-11 | 2 | VĐ: xác nhận trọng số; TG: $B_M=0_{1×3×3}$ nên mọi khóa hợp lệ; VD: $A^{(1)}$; HT: phép mũ/chia; UD: sai số làm tròn; KT: tổng hàng. | $S^{(1)},B_M:1×3×3$ → $A^{(1)}$. | Trộn V; `↓` 12. |
| L11-12 | 2 | VĐ: trọng số chưa phải đầu ra; TG: tổng có trọng số; VD: SVG; HT: $AV$; UD: co trục khóa; KT: kích thước. | $A,V$ → $O$. | Tính số cụ thể; `↓` 13. |
| L11-13 | 2 | VĐ: đóng trace đầu 1; TG: đóng góp phụ thuộc A và V; VD: $O^{(1)}$; HT: nhân ma trận; UD: KAD vì là phép tính; KT: phản ví dụ trọng số lớn. | $A^{(1)},V^{(1)}$ → $O^{(1)}$. | Kiểm cả tuyến; `↓` 14. |
| L11-14 | 2 | VĐ: dễ co sai trục; TG: lần QK→AV; VD: kích thước đầu 1; HT: ba phép co; UD: KAD vì là kiểm tra; KT: câu hỏi. | Trace L04–13 → kết quả kích thước. | Thêm nhân quả; `→` 15. |
| L11-15 | 2 | VĐ: rò tương lai; TG: chỉ $j\le i$; VD: dự đoán vị trí; HT: $M^{causal}$; UD: decoder; KT: KAD vì L18. | Trace không mask → tập khóa nhân quả. | Vẽ ma trận cộng; `↓` 16. |
| L11-16 | 2 | VĐ: biểu diễn điều kiện nhân quả; TG: tam giác dưới; VD: SVG/ma trận; HT: 0/−∞; UD: cộng trước softmax; KT: cảnh báo không mask sau. | $S^{(1)}$ → điểm causal. | Chuẩn hóa lại; `↓` 17. |
| L11-17 | 3 | VĐ: lượng hóa tác động; TG: hai hàng đầu đổi; VD: $A_c,O_c$; HT: softmax trên tập hợp lệ; UD: decoder; KT: kiểm hàng 3. | QKV đầu 1 → đầu ra causal. | Diễn giải; `↓` 18. |
| L11-18 | 2 | VĐ: nhớ hình nhưng không hiểu; TG: tập khóa theo hàng; VD: hàng 1/3; HT: KAD vì là kiểm tra; UD: KAD; KT: câu hỏi. | $A$ và $A_c$ → giải thích. | Khái quát ba loại; `↓` 19. |
| L11-19 | 3 | VĐ: QKV không luôn cùng nguồn; TG: ba cột; VD: SVG; HT: nguồn tensor; UD: encoder/decoder/cross; KT: KAD vì L24. | Self/casual trace → ba loại chú ý. | Khóa shape self; `↓` 20. |
| L11-20 | 2 | VĐ: kích thước tự chú ý; TG: $T_q=T_k$; VD: tensor tổng quát; HT: QKV/O; UD: hai mặt nạ; KT: kiểm chiều. | $B,T,D$ → kích thước self-attention. | Khóa kích thước cross-attention; `↓` 21. |
| L11-21 | 2 | VĐ: nguồn/đích khác độ dài; TG: hàng đích/cột nguồn; VD: $T_t,T_s$; HT: $A,O$; UD: cross-attn; KT: kiểm softmax khóa. | Trạng thái encoder/decoder → shape cross. | Xử lý hàng không hợp lệ; `↓` 22. |
| L11-22 | 2 | VĐ: hàng toàn −∞; TG: không có phân phối; VD: softmax không xác định; HT: điều kiện ít nhất một khóa; UD: zero/skip; KT: caveat. | Mask → hợp đồng hàng hợp lệ. | Tách padding key/query; `↓` 23. |
| L11-23 | 2 | VĐ: đệm can thiệp ở hai nơi; TG: khóa không được đọc, ký hiệu đệm không góp sai số; VD: hai thẻ; HT: mặt nạ khóa phải khớp tensor điểm trước phép cộng; UD: chú ý và CE; KT: phân biệt. | Mặt nạ khóa → điểm đã che; mặt nạ ký hiệu → sai số. | Kiểm ba loại; `↓` 24. |
| L11-24 | 2 | VĐ: nhầm trục chú ý chéo; TG: hàng đích/cột nguồn; VD: 3 và 5; HT: kích thước trước MHA; UD: KAD vì kiểm tra; KT: câu hỏi. | L19–23 → $A:B\times3\times5$ trước MHA. | Sang L25 mới thêm trục đầu để được $B\times H_a\times3\times5$; `→` 25. |
| L11-25 | 3 | VĐ: một phép chiếu chỉ có một không gian; TG: các đầu song song; VD: SVG tự chú ý; HT: $\operatorname{MHA}(Q_{in},K_{in},V_{in})$, phép ghép theo đặc trưng và $A_{n,h,i,j}$; UD: quay lại cấu hình không mặt nạ, hai đầu cùng dùng $X$ và $B_M=0$; KT: KAD vì L29. | Trace đầu 1 không mặt nạ → giao diện MHA tổng quát; mặt nạ mở thành $B\times1\times T_q\times T_k$ rồi phát qua đầu. | Chọn đầu 2 với cùng mặt nạ; cấu hình nhân quả trở lại ở bộ giải mã; `↓` 26. |
| L11-26 | 2 | VĐ: cần phép chiếu khác; TG: đổi cặp chiều; VD: $W^{(2)}$; HT: QKV đầu 2; UD: cả hai đầu dùng $B_M=0$, không dùng kết quả nhân quả L17; KT: kiểm hàng 3. | $X,B_M=0$ → $Q^{(2)},K^{(2)},V^{(2)}$. | Tính A/O; `↓` 27. |
| L11-27 | 2 | VĐ: đầu khác có thật sự khác; TG: hàng điểm bằng nhau; VD: $A^{(2)},O^{(2)}$; HT: cùng pipeline; UD: đa dạng phép trộn; KT: kiểm .333. | QKV đầu 2 → A/O đầu 2. | Ghép đầu; `↓` 28. |
| L11-28 | 2 | VĐ: đưa nhiều đầu về D; TG: ghép rồi trộn; VD: $W_O=I$; HT: concat/chiếu; UD: đầu ra MHA; KT: kích thước $1×3×4$. | $O^{(1)}$ từ L11-13 và $O^{(2)}$ từ L11-27 → $O_{MHA}$. | Đếm tham số; `↓` 29. |
| L11-29 | 2 | VĐ: số đầu và số tham số dễ nhầm; TG: tổng chiều cố định; VD: D=4,H=2; HT: $4D^2$ và độ lệch; UD: thiết kế đầu; KT: câu hỏi. | Shape chiếu → 64 tham số không độ lệch, 80 tham số có độ lệch. | Hoàn tất trace MHA trên $X$ thô rồi mới thêm vị trí; `→` 30. |
| L11-30 | 2 | VĐ: self-attn chưa có thứ tự; TG: tương đương hoán vị; VD: đổi hàng $X$; HT: công thức sin–cos; UD: tạo tín hiệu cùng $D$; KT: caveat. | $X$ chưa vị trí → công thức $PE$. | Tính và cộng $PE$; `↓` 31. |
| L11-31 | 3 | VĐ: ghép vị trí vào ví dụ; TG: phát $PE:3×4$ qua trục lô; VD: $PE_0,PE_1,PE_2$ và $H_0[0,0,:]$, ghi rõ $\cos(1/100)\approx0.99995$ được làm tròn thành 1; HT: $H_0=X+PE$; UD: notes nối $H_0$ sang $H_0W_Q,H_0W_K,H_0W_V$; KT: câu hỏi shape và trục cộng. | $X:1×3×4$ + $PE:3×4$ → $H_0[0,0,:]=[1,1,1,1]$; sau đó chỉ giữ kích thước và nối sang attention trong mạch nói. | Xử lý từng vị trí; `↓` 32. |
| L11-32 | 2 | VĐ: cần phi tuyến sau trộn; TG: FFN theo vị trí; VD: ReLU; HT: D→Dff→D; UD: tham số chia sẻ; KT: kích thước. | $H:B×T×D$ → FFN cùng kích thước. | Thêm đường dư; `↓` 33. |
| L11-33 | 2 | VĐ: đường sâu khó truyền; TG: lối trực tiếp; VD: H+Drop(F(H)); HT: cùng shape; UD: train/eval dropout; KT: điều kiện cộng. | H,F(H) → R. | Chuẩn hóa R; `↓` 34. |
| L11-34 | 2 | VĐ: thang đặc trưng thay đổi; TG: chuẩn hóa từng vectơ; VD: μ,σ²; HT: LN có căn, epsilon và $\gamma,\beta\in\mathbb R^D$; UD: phát tham số qua $B,T$; KT: trục $D$. | $r\in\mathbb R^D$ → LN(r). | Khóa thứ tự nguồn; `↓` 35. |
| L11-35 | 3 | VĐ: cần ghép hai nhánh thành một khối; TG: đường dư rồi LN; VD: SVG; HT: hai công thức post-norm; UD: khối nguồn; KT: nhận dạng thứ tự. | MHA/FFN/residual/LN → $H'$. | Xếp encoder; `→` 36. |
| L11-36 | 4 | VĐ: một khối chưa thành bộ mã hóa sâu; TG: lặp cùng hợp đồng shape; VD: SVG một tầng có hai đường dư, hai nhãn Bỏ ngẫu nhiên và nhãn lặp; HT: $H^{src}_{\ell-1}\to U_\ell\to H^{src}_\ell$; UD: mặt nạ nguồn ở mọi tầng; KT: $H^{enc}=H^{src}_{L_{enc}}:B×T_s×D$. | $H_0^{src}:B×T_s×D$ → $H^{src}_1\to\cdots\to H^{enc}$. | Dùng đầu ra cuối này làm K,V ở mọi tầng decoder; `↓` 37. |
| L11-37 | 4 | VĐ: mỗi tầng đích cần tiền tố và đầu ra mã hóa; TG: lặp ba mô-đun/ba đường dư; VD: SVG có ba nhãn Bỏ ngẫu nhiên và nhãn lặp; HT: $G_{\ell-1}\to U_\ell\to C_\ell\to G_\ell$; UD: chú ý chéo dùng $H^{enc}$; KT: $H^{dec}=G_{L_{dec}}:B×T_t×D$. | $G_0=H_0^{tgt}$ và $H^{enc}$ → $G_1\to\cdots\to H^{dec}$. | Chiếu đầu ra tầng cuối sang từ vựng; `↓` 38. |
| L11-38 | 3 | VĐ: lệch đầu vào/nhãn và điểm từ vựng dễ lẫn trọng số chú ý; TG: dịch một vị trí; VD: cặp `[BOS,tôi,học]`/`[tôi,học,EOS]`, với BOS/EOS là dấu bắt đầu/kết thúc chuỗi; HT: $Z,W_{vocab},b_{vocab},|V_{tgt}|$, $N_M=\sum_{n,t}M_{n,t}$ và giả thiết riêng $N_M>0$; UD: log-softmax ổn định, trung bình trên ký hiệu hợp lệ; KT: EOS được tính, mẫu số dương. | $H^{dec}$ → $Z:B×T_t×|V_{tgt}|$ → $\mathcal L$; khai triển LSE chuyển vào notes. | So huấn luyện/suy luận; `↓` 39. |
| L11-39 | 2 | VĐ: lịch tính khác nhau; TG: nhãn có sẵn so tự sinh; VD: hai thẻ; HT: causal mask; UD: active/EOS/eval; KT: caveat tuần tự. | Yin/Yout → train song song/infer tuần tự. | Tổng hợp hợp đồng; `↓` 40. |
| L11-40 | 4 | VĐ: thu hồi giới hạn truyền trạng thái tuần tự ở mở bài; TG: chú ý nối trực tiếp các vị trí rồi được ghép thành khối; VD: toàn trace; HT: kích thước trong MHA, truy hồi bộ mã hóa, nguồn đầu vào ba nhánh bộ giải mã, trục và mặt nạ; UD: danh sách kiểm; KT: sinh viên chọn một trong bốn ý, giảng viên chốt theo tensor/sơ đồ. | Toàn bài → kiểm tra $H^{src}_0\to H^{enc}$ và $G_{\ell-1},H^{enc}\to G_\ell$ cùng các hợp đồng tensor. | Kết thúc lõi bằng câu trả lời cho vấn đề xử lý tuần tự; `→` X01 nếu dạy tuyến mở rộng. |
| L11-X01 | 5 | VĐ: PE cần thiết ra sao; TG: hoán vị; VD: đổi hàng X; HT: tương đương hoán vị; UD: PE/mask phá đối xứng; KT: kiểm chứng lại mệnh đề đã gặp ở L11-30. | Bốn hợp đồng lõi L40 → phép kiểm sức chịu thứ nhất về đối xứng. | Tiếp tục với chi phí; `↓` X02. |
| L11-X02 | 5 | VĐ: đọc toàn chuỗi tốn gì; TG: ma trận T²; VD: 128→512; HT: O(T²); UD: ngân sách; KT: câu hỏi. | Shape điểm → tỷ lệ 16. | Tham số đầu; `↓` X03. |
| L11-X03 | 5 | VĐ: nhiều đầu có tăng tham số; TG: chia D; VD: 8→16; HT: 4D²; UD: chọn H; KT: câu hỏi. | L29 → tổng quát. | Quan hệ vị trí; `↓` X04. |
| L11-X04 | 5 | VĐ: sin–cos mã hóa quan hệ độ lệch thế nào; TG: dịch vị trí là phép quay; VD: cặp chiều tại $p$ và $p+k$; HT: ma trận quay phụ thuộc $k\omega_i$; UD: đọc cấu trúc vị trí tương đối; KT: câu hỏi phụ thuộc $p$ hay $k$. | Ba phép kiểm đối xứng/chi phí/tham số → phép kiểm cuối về vị trí. | Chốt: bốn đánh đổi mở rộng đều suy từ các hợp đồng tensor của phần lõi. |

## Chu trình và thời lượng

- Tự chú ý: VĐ/TG L03–05 → VD/HT L04–13 → KT L14.
- Nhân quả và mặt nạ: VĐ L15 → TG/VD/HT L16–23 → KT L18,24.
- Nhiều đầu: VĐ/TG L25 → VD/HT L26–28 → UD/KT L29.
- Khối Transformer: VĐ/TG/VD/HT L30 → UD/KT L31 → HT/UD L32–35 → KT L40.
- Encoder–decoder: VĐ/TG/VD/HT L36–37 → HT/UD L38–39 → KT L40.
- Tổng lõi: 100 phút. Phụ lục: 20 phút. Bài tập: 50 phút, gồm ba bài tính toán 40 phút và BT11-04 phòng máy 10 phút.

## Chu trình phòng máy BT11-04

- **Vấn đề:** cần xác nhận các phép tensor đã học thực sự khớp SDPA trước khi khảo sát giao diện MHA.
- **Trực giác:** cùng Q/K/V/mặt nạ phải cho kết quả thủ công và SDPA gần nhau; MHA là giao diện có thêm phép chiếu nên được kiểm riêng.
- **Ví dụ:** $B=1,H_a=2,T=3,d_h=2,D=4$ trên CPU, kiểu `float32`, nguồn ngẫu nhiên cố định.
- **Hình thức/tính toán:** tính `q @ k.transpose`, chia $\sqrt{d_h}$, `masked_fill`, softmax theo khóa và `@ v`; SDPA nhận cùng $Q,K,V:1\times2\times3\times2$.
- **Triển khai/ứng dụng:** dùng `torch.inference_mode()`, `dropout_p=0.0`, `torch.testing.assert_close`; MHA dùng `eval()` và mặt nạ phủ định.
- **Kiểm tra:** xác nhận thủ công≈SDPA, đối chiếu bốn kích thước và hai mặt nạ; không so `y_sdpa` với `y_mha`. `batch_first=False` là điểm thưởng.
- **Hợp đồng và kỹ năng được tái áp dụng:** phép tính BT11-01 → quy tắc mặt nạ BT11-02 → truy vết kích thước BT11-03 → kiểm chứng và bản ghi API BT11-04. Mỗi bài dùng tensor riêng; các hợp đồng chung đến từ L11-20, L11-23 và L11-25.
- **Nhịp 10 phút:** 1 phút dự đoán kích thước/mặt nạ → 2 phút đọc hai hợp đồng API → 4 phút chạy mã → 3 phút đối chiếu mặt nạ và dropout. Thử `batch_first=False` chỉ dùng khi còn thời gian.
- **Điều kiện trước giờ học:** máy phòng thực hành đã có PyTorch 2.13 chạy trên CPU; thời gian cài đặt không tính vào 10 phút.
