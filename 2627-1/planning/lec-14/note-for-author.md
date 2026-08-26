# Ghi chú cho người soạn — Bài 14

## Tuyến nói lõi

- L14-02 đặt nhu cầu bằng tình huống nguồn 5-way 1-shot, rồi mới phân biệt phân phối mẫu và phân phối tác vụ.
- L14-04–10 khóa support/query, N/K/R/B, shape, split và episode G. Không cho query tham gia thích nghi.
- L14-11–15 dùng chính G để tạo cặp Siamese. Nhấn mạnh đây là bộ xác minh cặp; không tự dựng luật N-way.
- L14-16–25 truyền G qua prototype $(1,5)$, broadcasting, log-softmax, gather và NLL. Cho sinh viên trả lời trước khi hiện fragment.
- L14-26–37 giữ G khi chuyển sang MAML: classifier logistic, inner gradient, phi, query loss, outer objective, thuật toán rồi meta-gradient/meta-test.
- L14-39–41 so sánh ba họ trên cùng dữ liệu G. Câu hỏi cuối phải yêu cầu nhận diện trạng thái thích nghi và kiểu dự đoán.

## Đáp án lõi

- L14-10: 12 mẫu hỗ trợ, 6 mẫu truy vấn; không trộn ba tác vụ.
- L14-15: $z=1$; $-\log .9<-\log .6$ nên mất mát giảm.
- L14-19: $c_A=1,c_B=5$.
- L14-21: khoảng cách bình phương query A là 2.25 và 6.25.
- L14-23: NLL G xấp xỉ .00908.
- L14-25: query vào prototype là rò rỉ query→adaptation.
- L14-29: gradient trung bình theo $(w,b)$ là $(-1,0)$.
- L14-30: $\phi=(1,0)$.
- L14-31: cả hai query đúng lớp; NLL trung bình xấp xỉ .3377.
- L14-41: ProtoNet tạo prototype; MAML cập nhật phi; Siamese chỉ cho điểm cặp khi chưa có quy tắc N-way.

## Phụ lục và điều hướng

- Lõi: đi xuống L14-00–15, phải; xuống L14-16–26, phải; xuống L14-27–41 và dừng.
- Phụ lục: từ L14-41 đi phải đúng một lần sang X01, sau đó đi xuống X02–X04.
- X01 phân biệt prompting; X02 cảnh báo variable-K; X03 dùng I cho exact/FO/HVP; X04 là tình huống land-cover nguồn PDF26–31.
- Nếu chỉ có 100 phút, không mở phụ lục. Không nhắc nhãn “core/extension” hoặc thời lượng trên mặt trang và trong notes.

## Bài tập 50 phút riêng

1. 10 phút: từ một lô episode, ghi N/K/R/B, shape support/query và kiểm tra split.
2. 15 phút: tính prototype, khoảng cách, log-softmax và NLL của G; yêu cầu nêu đúng trục mean/softmax.
3. 15 phút: với một tác vụ khả vi, tính một inner update và viết outer objective trên query; không yêu cầu exact/FO hay HVP.
4. 10 phút: so ProtoNet và MAML về $A_\theta(S)$, đường gradient và chi phí meta-test.

## Lưu ý triển khai

- ProtoNet: mean theo K; broadcast `[B,NR,1,D]-[B,1,N,D]`; log-softmax theo N; gather nhãn cục bộ; mean query rồi task.
- MAML: không cập nhật theta tại chỗ trong vòng trong; giữ phi riêng từng task. Exact giữ graph; FO xấp xỉ Jacobian bằng I. Không chọn biến thể BatchNorm nếu nguồn không khóa giao thức.
- Ví dụ I ở X03 không được dùng trong bảng so sánh ba phương pháp. Không biến land-cover thành claim benchmark.
- Hậu kiểm cần duyệt 46 trang ở 1280×720 và màn hình hẹp, nhất là L14-06, L14-13, L14-20, L14-23, L14-33, L14-39–40 và X03.
