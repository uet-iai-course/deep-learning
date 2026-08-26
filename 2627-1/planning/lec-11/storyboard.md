# Storyboard — Bài 11

## Điều hướng và quy ước

- Sáu stack lõi ngang: L11-00–03; L11-04–14; L11-15–24; L11-25–29; L11-30–35; L11-36–40.
- Một stack phụ lục dọc: L11-X01 → X02 → X03 → X04. Dùng `↓` trong stack và `→` tại trang cuối stack.
- Vai trò: **VĐ** vấn đề, **TG** trực giác, **VD** ví dụ, **HT** hình thức/tính toán, **UD** triển khai/ứng dụng, **KT** kiểm tra. `KAD` luôn kèm lý do.

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
| L11-23 | 2 | VĐ: đệm can thiệp ở hai nơi; TG: khóa không được đọc, ký hiệu đệm không góp sai số; VD: hai thẻ; HT: sau L25 mặt nạ khóa mở thành $B×1×T_q×T_k$ và phát qua $H_a$; UD: chú ý và CE; KT: phân biệt. | Mặt nạ khóa ba chiều → thêm trục đầu đơn vị; mặt nạ token → sai số. | Kiểm ba loại; `↓` 24. |
| L11-24 | 2 | VĐ: nhầm trục chú ý chéo; TG: hàng đích/cột nguồn; VD: 3 và 5; HT: kích thước/phát tự động; UD: KAD vì kiểm tra; KT: câu hỏi. | L19–23 → $A:B\times3\times5$. | Chia nhiều đầu; `→` 25. |
| L11-25 | 3 | VĐ: một phép chiếu chỉ có một không gian; TG: các đầu song song; VD: SVG self-attention; HT: $\operatorname{MHA}(Q_{in},K_{in},V_{in})$ và $A_{n,h,i,j}$; UD: self dùng cùng đầu vào, cross dùng hai nguồn; KT: KAD vì L29. | Trace đầu 1 → giao diện MHA tổng quát. | Chọn đầu 2; `↓` 26. |
| L11-26 | 2 | VĐ: cần phép chiếu khác; TG: đổi cặp chiều; VD: $W^{(2)}$; HT: QKV đầu 2; UD: KAD vì trace; KT: kiểm hàng 3. | $X$ → $Q^{(2)},K^{(2)},V^{(2)}$. | Tính A/O; `↓` 27. |
| L11-27 | 2 | VĐ: đầu khác có thật sự khác; TG: hàng điểm bằng nhau; VD: $A^{(2)},O^{(2)}$; HT: cùng pipeline; UD: đa dạng phép trộn; KT: kiểm .333. | QKV đầu 2 → A/O đầu 2. | Ghép đầu; `↓` 28. |
| L11-28 | 2 | VĐ: đưa nhiều đầu về D; TG: ghép rồi trộn; VD: $W_O=I$; HT: concat/chiếu; UD: đầu ra MHA; KT: shape $1×3×4$. | $O^{(1)},O^{(2)}$ → $O_{MHA}$. | Đếm tham số; `↓` 29. |
| L11-29 | 2 | VĐ: số đầu và số tham số dễ nhầm; TG: tổng chiều cố định; VD: D=4,H=2; HT: $4D^2$ + bias; UD: thiết kế đầu; KT: câu hỏi. | Shape chiếu → 64/80 tham số. | Thêm vị trí; `→` 30. |
| L11-30 | 2 | VĐ: self-attn chưa có thứ tự; TG: tương đương hoán vị; VD: đổi hàng $X$; HT: công thức sin–cos; UD: tạo tín hiệu cùng $D$; KT: caveat. | $X$ chưa vị trí → công thức $PE$. | Tính và cộng $PE$; `↓` 31. |
| L11-31 | 3 | VĐ: ghép vị trí vào ví dụ; TG: phát $PE:3×4$ qua trục lô; VD: $PE_0,PE_1,PE_2$ và $H_0[0,0,:]$; HT: $H_0=X+PE$; UD: tầng đầu dùng $H_0W_Q,H_0W_K,H_0W_V$; KT: câu hỏi shape và trục cộng. | $X:1×3×4$ + $PE:3×4$ → $H_0[0,0,:]=[1,1,1,1]$; sau đó chỉ giữ kích thước. | Xử lý từng vị trí; `↓` 32. |
| L11-32 | 2 | VĐ: cần phi tuyến sau trộn; TG: FFN theo vị trí; VD: ReLU; HT: D→Dff→D; UD: tham số chia sẻ; KT: kích thước. | $H:B×T×D$ → FFN cùng kích thước. | Thêm đường dư; `↓` 33. |
| L11-33 | 2 | VĐ: đường sâu khó truyền; TG: lối trực tiếp; VD: H+Drop(F(H)); HT: cùng shape; UD: train/eval dropout; KT: điều kiện cộng. | H,F(H) → R. | Chuẩn hóa R; `↓` 34. |
| L11-34 | 2 | VĐ: thang đặc trưng thay đổi; TG: chuẩn hóa từng vectơ; VD: μ,σ²; HT: LN có căn, epsilon và $\gamma,\beta\in\mathbb R^D$; UD: phát tham số qua $B,T$; KT: trục $D$. | $r\in\mathbb R^D$ → LN(r). | Khóa thứ tự nguồn; `↓` 35. |
| L11-35 | 3 | VĐ: cần ghép hai nhánh thành một khối; TG: đường dư rồi LN; VD: SVG; HT: hai công thức post-norm; UD: khối nguồn; KT: nhận dạng thứ tự. | MHA/FFN/residual/LN → $H'$. | Xếp encoder; `→` 36. |
| L11-36 | 4 | VĐ: một khối chưa thành bộ mã hóa sâu; TG: lặp cùng hợp đồng shape; VD: SVG một tầng có hai đường dư, hai nhãn Bỏ ngẫu nhiên và nhãn lặp; HT: $H^{src}_{\ell-1}\to U_\ell\to H^{src}_\ell$; UD: mặt nạ nguồn ở mọi tầng; KT: $H^{enc}=H^{src}_{L_{enc}}:B×T_s×D$. | $H_0^{src}:B×T_s×D$ → $H^{src}_1\to\cdots\to H^{enc}$. | Dùng đầu ra cuối này làm K,V ở mọi tầng decoder; `↓` 37. |
| L11-37 | 4 | VĐ: mỗi tầng đích cần tiền tố và đầu ra mã hóa; TG: lặp ba mô-đun/ba đường dư; VD: SVG có ba nhãn Bỏ ngẫu nhiên và nhãn lặp; HT: $G_{\ell-1}\to U_\ell\to C_\ell\to G_\ell$; UD: chú ý chéo dùng $H^{enc}$; KT: $H^{dec}=G_{L_{dec}}:B×T_t×D$. | $G_0=H_0^{tgt}$ và $H^{enc}$ → $G_1\to\cdots\to H^{dec}$. | Chiếu đầu ra tầng cuối sang từ vựng; `↓` 38. |
| L11-38 | 3 | VĐ: lệch đầu vào/nhãn và điểm từ vựng dễ lẫn trọng số chú ý; TG: dịch một vị trí; VD: cặp `[BOS,tôi,học]`/`[tôi,học,EOS]`; HT: $Z,W_{vocab},b_{vocab},|V_{tgt}|$ và CE có mặt nạ; UD: log-softmax ổn định, trung bình trên token hợp lệ; KT: EOS được tính, mẫu số dương. | $H^{dec}$ → $Z:B×T_t×|V_{tgt}|$ → $\mathcal L$; khai triển LSE chuyển vào notes. | So huấn luyện/suy luận; `↓` 39. |
| L11-39 | 2 | VĐ: lịch tính khác nhau; TG: nhãn có sẵn so tự sinh; VD: hai thẻ; HT: causal mask; UD: active/EOS/eval; KT: caveat tuần tự. | Yin/Yout → train song song/infer tuần tự. | Tổng hợp hợp đồng; `↓` 40. |
| L11-40 | 4 | VĐ: triển khai dễ thiếu một hợp đồng; TG: bốn nhóm; VD: toàn trace; HT: kích thước/PE/trục/mặt nạ–nhãn; UD: danh sách kiểm; KT: bốn ý đánh số, trả lời lần lượt. | Toàn bài → khung triển khai và kiểm tra vai trò của $PE$. | Kết thúc lõi; `→` X01 nếu dạy phụ lục. |
| L11-X01 | 5 | VĐ: PE cần thiết ra sao; TG: hoán vị; VD: đổi hàng X; HT: tương đương hoán vị; UD: PE/mask phá đối xứng; KT: câu hỏi. | L30 → lập luận hình thức. | Chi phí; `↓` X02. |
| L11-X02 | 5 | VĐ: đọc toàn chuỗi tốn gì; TG: ma trận T²; VD: 128→512; HT: O(T²); UD: ngân sách; KT: câu hỏi. | Shape điểm → tỷ lệ 16. | Tham số đầu; `↓` X03. |
| L11-X03 | 5 | VĐ: nhiều đầu có tăng tham số; TG: chia D; VD: 8→16; HT: 4D²; UD: chọn H; KT: câu hỏi. | L29 → tổng quát. | Quan hệ vị trí; `↓` X04. |
| L11-X04 | 5 | VĐ: sin–cos mã hóa quan hệ độ lệch thế nào; TG: dịch vị trí là phép quay; VD: cặp chiều tại $p$ và $p+k$; HT: ma trận quay phụ thuộc $k\omega_i$; UD: đọc cấu trúc vị trí tương đối; KT: câu hỏi phụ thuộc $p$ hay $k$. | L30–31 → quan hệ giữa hai vị trí. | Kết thúc phụ lục. |

## Chu trình và thời lượng

- Tự chú ý: VĐ/TG L03–05 → VD/HT L04–13 → KT L14.
- Nhân quả và mặt nạ: VĐ L15 → TG/VD/HT L16–23 → KT L18,24.
- Nhiều đầu: VĐ/TG L25 → VD/HT L26–28 → UD/KT L29.
- Khối Transformer: VĐ/TG/HT L30 → VD/UD/KT L31 → HT/UD L32–35 → KT L40.
- Encoder–decoder: VĐ/TG/VD/HT L36–37 → HT/UD L38–39 → KT L40.
- Tổng lõi: 100 phút. Phụ lục: 20 phút. Bài tập: 50 phút, gồm ba bài tính toán 40 phút và BT11-04 phòng máy 10 phút.

## Chu trình phòng máy BT11-04

- **Vấn đề:** cần xác nhận các phép tensor đã học thực sự khớp SDPA trước khi khảo sát giao diện MHA.
- **Trực giác:** cùng Q/K/V/mặt nạ phải cho kết quả thủ công và SDPA gần nhau; MHA là giao diện có thêm phép chiếu nên được kiểm riêng.
- **Ví dụ:** $B=1,H_a=2,T=3,d_h=2,D=4$ trên CPU, kiểu `float32`, nguồn ngẫu nhiên cố định.
- **Hình thức/tính toán:** tính `q @ k.transpose`, chia $\sqrt{d_h}$, `masked_fill`, softmax theo khóa và `@ v`; SDPA nhận cùng $Q,K,V:1\times2\times3\times2$.
- **Triển khai/ứng dụng:** dùng `torch.inference_mode()`, `dropout_p=0.0`, `torch.testing.assert_close`; MHA dùng `eval()` và mặt nạ phủ định.
- **Kiểm tra:** xác nhận thủ công≈SDPA, đối chiếu bốn kích thước và hai mặt nạ; không so `y_sdpa` với `y_mha`. `batch_first=False` là điểm thưởng.
- **Đầu vào → sản phẩm:** bảng phép tính BT11-01 → mặt nạ BT11-02 → chuỗi kích thước BT11-03 → mã đã chạy và bản ghi đầu ra BT11-04. Các hợp đồng tensor đến từ L11-20, L11-23 và L11-25.
- **Nhịp 10 phút:** 1 phút dự đoán kích thước/mặt nạ → 2 phút đọc hai hợp đồng API → 4 phút chạy mã → 3 phút đối chiếu mặt nạ và dropout. Thử `batch_first=False` chỉ dùng khi còn thời gian.
- **Điều kiện trước giờ học:** máy phòng thực hành đã có PyTorch 2.13 chạy trên CPU; thời gian cài đặt không tính vào 10 phút.
