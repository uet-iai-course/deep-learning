# Ghi chú cho người soạn Bài 08

## Tuyến giảng

- Tuyến lõi đi từ L08-00 đến L08-38 trong 97 phút, rồi kết thúc bằng L08-39 trong 3 phút. Tại L08-38, dùng End để đến thẳng L08-39. Nếu lớp cần thêm thời gian cho phép tính, ưu tiên giữ L08-12–21 và rút ngắn thảo luận ở L08-30–38, nhưng không bỏ định nghĩa hai chiều hoặc bộ mã hóa–giải mã vì chúng thuộc phạm vi DOCX.
- Tuyến đầy đủ bắt đầu phần mở rộng bằng phím Phải tại L08-38, đi xuống L08-X01→X02→X03→X04 rồi đến L08-39. Bốn trang mở rộng có tổng 20 phút; L08-39 vẫn là kết luận cuối.
- Liên kết phím Phải được khóa tại sáu ranh giới L08-06→07, 17→18, 21→22, 29→30, 33→34 và 38→X01 vì Reveal có thể giữ chỉ số dọc của mạch kế tiếp. Phím End luôn đi đến L08-39; không ghi đè các phím khác.
- Khi chuyển từ LSTM sang GRU, cho sinh viên tính $R,Z$ từ dữ kiện L08-24 trước khi khái quát phương trình ở L08-25. Hai nguồn dùng hai quy ước $Z$ đối nhau; phép đổi biến còn yêu cầu đổi dấu tiền kích hoạt.
- Khi nói về gradient, luôn phân biệt “nhánh trực tiếp qua $C$” với “đạo hàm toàn phần”. Không rút gọn đạo hàm toàn phần thành tích cổng quên.
- Không gọi $C_t$ là trạng thái ẩn. Dùng “trạng thái ô” cho $C_t$ và “trạng thái ẩn” cho $H_t$.
- Với chuỗi nguồn đã đệm, dùng $L_n$ hoặc $M^{src}$ để lấy trạng thái cuối hợp lệ; không lấy mặc định $H_T$ sau các bước đệm. Mặt nạ đích $M^{tgt}$ chỉ cân mất mát theo token.
- Cụm dịch máy dùng duy nhất GRU encoder/decoder. $Q$ khởi tạo $S_0$ và không được chèn lại vào đầu vào mỗi bước. $D_e$ là chiều vector nhúng token đích, độc lập với $D_h$.
- Bốn trang mở rộng là bốn trạm đối chiếu liên tiếp: biểu diễn phân loại, chi phí tham số của ô, sinh tự hồi quy và chọn kiến trúc. L08-X02 áp dụng công thức đã có vào kích thước cụ thể; không giảng lại phép đếm tổng quát.
- Không tạo demo phân tích cảm xúc: nguồn GT 315–317 chỉ mô tả kiến trúc và ví dụ, không có code để chuyển; người dùng không yêu cầu demo.

## Đáp án và lỗi dễ mắc

- L08-15: đổi $O_t$ thành 0 không đổi $C_t$; $H_t$ thành 0. Lỗi thường gặp là cho rằng cổng ra xóa bộ nhớ.
- L08-17: với $N=8,D_x=16,D_h=32$, $X_tW_{xi}$ là $8\times32$; $b_i$ là $1\times32$ và được phát theo trục lô.
- L08-21: LSTM không bảo đảm phụ thuộc dài hạn vì $F_t$ có thể nhỏ, các sigmoid/tanh có thể bão hòa, và gradient toàn phần còn đi qua các trọng số cùng nhánh khác.
- L08-29: theo quy ước slide, với $Z_t=0.2$, nhánh giữ trực tiếp có hệ số $1-Z_t=0.8$. Đây không phải đạo hàm toàn phần vì còn các đường qua cổng và ứng viên; không suy ra rằng GRU loại bỏ gradient triệt tiêu.
- L08-31: với LSTM tầng 2, $N=8,D_2=32$, cả $H_t^{(2)}$ và $C_t^{(2)}$ là $8\times32$.
- L08-33: không có trạng thái nghịch đầy đủ nếu dữ liệu tương lai chưa đến. Hệ thống có bộ đệm ngắn chỉ có ngữ cảnh nhìn trước hữu hạn, không phải toàn chuỗi.
- L08-37: ở bước giải mã thứ hai, học theo đáp án dùng $E(y_1)$ còn suy luận dùng $E(\widehat y_1)$.
- L08-39: $Q$ có kích thước $4\times32$, logit $A_{t'}$ có kích thước $4\times10\,000$; $M^{src}$ giữ trạng thái nguồn tại vị trí đệm, còn $M^{tgt}$ chỉ chọn token đích trong chéo entropy. Khi suy luận, dừng từng mẫu tại EOS hoặc độ dài tối đa. Chốt LLO16 bằng giới hạn: cổng giúp giảm nhẹ nhưng không loại bỏ gradient triệt tiêu.
- L08-X04: LSTM hai chiều cho hai trạng thái ẩn $N\times T\times D_h$, ghép thành $N\times T\times2D_h$; trạng thái ô vẫn tách theo từng hướng. GRU không có trạng thái ô riêng.

## Bài tập 50 phút

1. **Tính LSTM, 20 phút.** Cho $c_{t-1}=-0.4$ và các tiền kích hoạt $a_i=0$, $a_f=0.5$, $a_o=1$, $a_g=-0.2$. Yêu cầu tính bốn tín hiệu, $c_t,h_t$, ghi rõ sigmoid/tanh và làm tròn bốn chữ số. Đáp án kiểm tra: $I=0.5$, $F\approx0.6225$, $O\approx0.7311$, $G\approx-0.1974$, $C\approx-0.3477$, $H\approx-0.2444$.
2. **Đường gradient, 10 phút.** Cho $F=(0.95,0.8,0.9,1.0,0.7)$ trên một chiều ẩn. Tính tích nhánh trực tiếp và giải thích vì sao đó chưa phải đạo hàm toàn phần. Đáp án: tích $0.4788$.
3. **So sánh ô, 10 phút.** Với $D_x=16,D_h=32$, đếm tham số ô RNN, GRU, LSTM theo phương trình bài, một bias cho mỗi phép affine/cổng và không tính đầu ra. Đáp án: cơ sở $16\cdot32+32^2+32=1568$; GRU $4704$; LSTM $6272$.
4. **Hai chiều, 10 phút.** Phân loại bốn tác vụ: gán nhãn từ loại ngoại tuyến, dự đoán token kế tiếp trực tuyến, phân tích cảm xúc toàn văn bản, phát hiện sự kiện ngay khi cảm biến phát tín hiệu. Chấp nhận hai chiều cho hai tác vụ có toàn chuỗi; hai tác vụ trực tuyến cần đơn hướng hoặc quy định độ trễ hữu hạn.

## Điểm cần kiểm chứng khi sửa

- Nếu đổi quy ước GRU, phải sửa đồng thời L08-23–29, bảng ký hiệu trong `outline.md`, storyboard, ví dụ số và nhật ký.
- Nếu đổi quy ước tensor, phải sửa L08-05–06, 16–17, 24, 31–38 và L08-X04.
- Nếu đổi mô hình cơ sở mã hóa–giải mã, phải sửa đồng thời L08-34–39, X03, sơ đồ và hợp đồng kích thước; không trộn khởi tạo bằng $Q$ với chèn $Q$ ở mọi bước.
- Không đổi mã liên kết phím dựa trên suy đoán. Kiểm tra sáu ranh giới và phím End trong trình duyệt; chỉ sửa nếu quan sát được điều hướng kép hoặc sai đích.
- Nếu thêm code, phải có nguồn tương ứng hoặc yêu cầu mới của người dùng; hiện không có code demo.
- Khi sửa timing hoặc thứ tự, rà trang bị ảnh hưởng và hai trang lân cận mỗi phía.

## Giới hạn công cụ

- Kiểm tra tự động không thay thế duyệt trực quan. Nếu Browser hoặc Codex Slides không khả dụng, ghi giới hạn trong `review-log.md` và không tuyên bố đã rà ở hai kích thước màn hình.
