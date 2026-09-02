# Ghi chú dành cho người soạn — Bài 06

## Tuyến giảng và điều hướng

- Tuyến lõi: L06-00 đến L06-37 rồi L06-38, 100 phút (L06-38 tính vào lõi dù đứng sau phần mở rộng trong DOM). Đi xuống trong từng cụm; chỉ nhấn phải ở L06-05, 10, 15, 20, 27 và 33 để sang mạch kế.
- Tại L06-37: nhấn **End** để nhảy tới L06-38 (slide cuối toàn deck, hành vi End mặc định của RevealJS) — tuyến lõi. Hoặc nhấn Xuống để vào L06-X01 rồi đi xuống qua X02–X05, sau đó Xuống tiếp tới L06-38 — tuyến đầy đủ.
- Câu nối X05→38: "Sau khi đào sâu các khía cạnh mở rộng, quay lại kiểm tra tổng hợp ở trang cuối."
- Tuyến mở rộng X01–X05: 20 phút; có thể cắt toàn bộ.
- Bài tập 50 phút không nằm trong thời lượng deck.
- Nếu chậm 5 phút trong tuyến lõi, rút L06-19 và L06-26 thành lời nhắc 30 giây. Nếu vẫn chậm, trình bày L06-23 trực tiếp từ hình, không chờ lớp, rồi gộp phần nói của L06-34–35; không bỏ L06-36–38. Tuyến mở rộng X01–X05 vẫn là khối cắt 20 phút độc lập.

## Điểm chờ và đáp án

| Trang | Thời gian chờ | Đáp án/điểm cần nghe |
|---|---:|---|
| L06-05 | 45 giây | Không chắc; tái tạo và phân loại là hai mục tiêu khác nhau. |
| L06-10 | 60 giây | $Z:32\times64$, $W_{e2}:256\times64$, $W_{d1}:64\times256$, $b_{d2}:784$, phát trên lô. |
| L06-15 | 45 giây | Thiếu mẫu số/trục lấy trung bình; 0.18 là SSE, 0.045 là MSE trên 4 phần tử. |
| L06-20 | 45 giây | Không thể kết luận mã tốt: lỗi tái tạo kiểm định thấp nhưng kết quả phân loại từ $z$ kém. Nút thắt chưa bảo đảm giữ thông tin cho tác vụ đích. |
| L06-27 | 60 giây | Top-$k$, $k=32$; mục tiêu khử nhiễu là $X$ sạch. |
| L06-X01 | 45 giây | $210/6=35=\mathrm{XXXV}$; không suy ra phép chia trở thành tuyến tính. |
| L06-33 | 60 giây | Dropout và thống kê BatchNorm có thể đổi hành vi dù không có gradient. |
| L06-38 | 60 giây | Chưa kết luận hữu ích tác vụ, không ghi nhớ, hoặc sinh được từ mã tùy ý. |

## Bài tập 50 phút

1. **Hoàn thiện sơ đồ và kích thước — 10 phút.** Với $N=16$, $d=32$, điền đủ sơ đồ bộ mã hóa–mã tiềm ẩn–bộ giải mã $784\to256\to32\to256\to784$ và ghi kích thước mọi tensor. Sản phẩm bắt buộc: $16\times784\to16\times256\to16\times32\to16\times256\to16\times784$. Nếu còn thời gian, tính thêm $419120$ tham số có độ lệch.
2. **Mất mát — 15 phút.** Tính SSE/MSE của bốn phần tử ở L06-12, sau đó tính MSE cho lô hai mẫu khi mẫu hai có SSE 0.10. Đáp án: tổng lô 0.28, MSE $0.28/(2\cdot4)=0.035$.
3. **Nghiệm đồng nhất và nút thắt — 10 phút.** Giải thích vì sao lỗi tái tạo bằng 0 chưa chứng minh mã hữu ích; nêu điều $d<784$ khuyến khích và điều nó không bảo đảm. Đáp án: loại phép chép trực tiếp theo từng tọa độ nhưng mạng vẫn có thể ghi nhớ tập hữu hạn; phải kiểm tra dữ liệu chưa thấy và tác vụ đích.
4. **Chọn biến thể — 10 phút.** Ghép ba tình huống với ràng buộc: giảm chiều; mã 1024 chiều nhưng 32 hoạt hóa; đầu vào nhiễu nhưng đích sạch. Đáp án: mã thấp chiều; mã thưa top-$k$; khử nhiễu.
5. **Tác vụ đích — 5 phút.** Với bộ mã hóa đóng băng và bộ phân loại đang học, nêu tham số thuộc bộ tối ưu và chế độ của từng mô-đun. Đáp án: chỉ $\psi$ được cập nhật; bộ mã hóa ở chế độ đánh giá, bộ phân loại ở chế độ huấn luyện.

## Phạm vi và lưu ý

- Không mở sang mô hình tự mã hóa biến phân, autoencoder che mặt, ViT, khuếch tán hoặc autoencoder chuỗi.
- Không thêm code demo hoặc notebook. Nếu cần hoạt động trên lớp, dùng bài tập giấy ở trên.
- Khi nói PCA ở L06-X02, luôn khóa: tuyến tính, dữ liệu đã định tâm, nút thắt $K$, mất mát bình phương; tại nghiệm tối ưu, khôi phục không gian con chính $K$ chiều; chỉ không gian con trùng, không nhất thiết trọng số trùng vectơ riêng. Giả thiết định tâm là bổ sung toán học để phát biểu chính xác.
- Khi nói nút thắt, dùng “khuyến khích nén”; không nói “bảo đảm không ghi nhớ”.
- Khi nói mã thưa, phân biệt phạt mềm $\Omega$ với top-$k$ cứng; top-$k$ áp dụng theo từng mẫu trên hoạt hóa ReLU không âm.
- Khi nói khử nhiễu, lặp lại một lần: đầu vào nhiễu, mục tiêu sạch.
- Khi nói chuyển giao, không trộn “đóng băng gradient” với `eval`; đây là hai thao tác độc lập.
- Không dùng tập kiểm tra để chọn $d$, $\lambda$, mức nhiễu, số epoch hoặc chính sách tinh chỉnh.
- Không dùng ảnh kiểm định hoặc kiểm tra trong tiền huấn luyện ở giao thức đã khóa trên L06-32.
- Đáp án chi tiết và kịch bản chờ nằm trong tệp này; storyboard chỉ giữ tóm tắt vai trò, thời lượng và điều hướng.

## Kiểm kê hình

Mọi SVG trong `img/lec-06/` phải được HTML tham chiếu ít nhất một lần. Không thêm raster. Các SVG dùng lại hợp lý: `numeral-representation.svg` ở L06-02 và X01. `sparse-code.svg` chỉ dùng ở L06-23; L06-X03 không dùng hình.
