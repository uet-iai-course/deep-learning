# Ghi chú cho người soạn — Bài 13

## Tuyến nói lõi

- Giữ hành lang L13-02 trên bảng. L13-15 thêm reward; L13-19 thêm lợi tức; L13-26 thêm đích; L13-31 thêm cập nhật; L13-35 đóng gói đúng chuyển tiếp đó thành một hàng DQN.
- Luôn đọc $R_{t+1}$ là phần thưởng sinh sau $A_t$. Quỹ đạo T bước dừng ở $S_T$.
- L13-13 dùng hai câu quyết định: có hành động chuyên gia thì BC là điểm bắt đầu; có reward và quyền tương tác thì RL có tín hiệu học. Không gọi reward là nhãn hành động.
- L13-16 cho sinh viên trả lời trước khi hiện sáu thành phần. L13-17 mới giới thiệu tuple MDP và giữ policy ở ngoài tuple.
- L13-19, 23 và 26 chờ sinh viên tính rồi mới hiện fragment.
- L13-24 chỉ phân biệt Monte Carlo với sai phân thời gian để chuẩn bị Bellman; không mở rộng sang n-step hoặc eligibility traces.
- L13-27 nhắc giả thiết tập hành động hữu hạn. Hành động liên tục chỉ nằm ở X01.
- L13-35–38 đọc cùng một hàng 5 trường $(S,A,R,S',D^{term})=(s_1,phải,0,s_2,0)$ → $q=.4$ → $Y=.9$ → sai số bình phương $.25$; đóng góp vào trung bình là $.25/B$ nếu $B>1$.
- L13-39 là pha thu thập, không backward; chi tiết warmup/reset/mode nằm trong notes, không đọc hết trên slide. L13-40 là pha cập nhật; optimizer chỉ chứa $\theta$. Reset môi trường khi lượt kết thúc thật; target chỉ triệt bootstrap khi terminal.
- X04 là bài kiểm tra tổng quát hợp đồng tensor DQN với $D_a=4$ tùy ý, không phải ví dụ hành lang; nói rõ điều này khi dạy.
- Timing mạch 5 (8 phút) đã được đề xuất điều chỉnh nhưng không áp dụng vì tổng 100 phút và nhịp đã khóa; nếu lớp chậm, có thể linh hoạt trao đổi thời gian trong mạch 5–6 mà không đổi tổng.
- Nói rõ DQN phi tuyến không có bảo đảm hội tụ tổng quát.

## Điều hướng và cắt

- Lõi 100 phút: đi xuống L13-00→07, đi phải; đi xuống L13-08→12, đi phải; đi xuống L13-13→20, đi phải; đi xuống L13-21→25→27→26, đi phải; đi xuống L13-28→31, đi phải; đi xuống L13-32→34→33→35→…→40, đi phải; dừng ở L13-41. L13-27 đứng trước L13-26 và L13-34 đứng trước L13-33 dù ID lớn hơn.
- Phụ lục 20 phút: L13-41 và X01–X04 cùng một outer stack; từ L13-41 đi xuống để vào X01, rồi tiếp tục xuống X02→X04; không đi phải.
- Không mô tả X01–X04 là các nhánh gắn giữa lõi. Đây là một phụ lục cuối duy nhất.
- Nếu chỉ có 110 phút, dừng ở L13-41; không chọn rời rạc một trang X vì planning đã khóa phụ lục thành tuyến 20 phút.
- Cắt theo mạch nếu thiếu thời gian: mạch 1=24, mạch 2=15, mạch 3=19, mạch 4=14, mạch 5=8, mạch 6=18, L13-41=2; không cắt giữa một mạch.

## Đáp án ngắn

- L13-06: xác suất hành động “phải” tăng.
- L13-12: validation lấy trạng thái từ $d_{\pi_E}$; quỹ đạo vận hành lấy trạng thái từ $d_{\pi_\theta}$.
- L13-16: robot; hành lang; vị trí; trái/phải; reward 1 ở đích; quy tắc chọn hành động.
- L13-19: $G_2=1,G_1=.9,G_0=.81$.
- L13-20: khi $D^{term}=1$, hạng giá trị tương lai bị triệt; phần lợi tức còn lại bằng 0.
- L13-23: kỳ vọng $.5$, cực đại $.8$.
- L13-26: đích $.9$.
- L13-31: chỉ ô $Q(s_1,phải)$ đổi trong cập nhật bảng.
- L13-37–38: $Y=.9$; hạng tử bình phương hàng số $.25$; gradient chỉ qua dự đoán hiện tại.
- L13-41: terminal triệt giá trị tương lai; gradient qua mạng hiện tại; chỉ có demonstration thì bắt đầu bằng BC.
- X01: trung bình hai mode có thể là hành động đi thẳng vào vật cản.
- X02: đích là $Y=R_{t+1}$ vì $D^{term}=1$ triệt giá trị tương lai.
- X03: học ngoài chính sách không thay điều kiện độ phủ.
- X04: $Q_{all}:32\times4$; chỉ số $32\times1$; $q,Y$ có 32 phần tử; mất mát vô hướng. Kiểm tra tổng quát, không phải ví dụ hành lang.

## Bài tập 50 phút

1. 10 phút: từ hai quỹ đạo chuyên gia, viết $\mathcal D_E$, lô B, nhãn và loss BC.
2. 10 phút: vẽ nhánh lỗi và chỉ ra $d_{\pi_E}\ne d_{\pi_\theta}$.
3. 10 phút: điền tác tử, môi trường, trạng thái, hành động, phần thưởng và policy cho hành lang.
4. 15 phút: tính $G_t$, đích Bellman và cập nhật Q; dùng một mẫu terminal và một mẫu giữa lượt.
5. 5 phút: gạch chân bộ nhớ phát lại, phép chọn theo A, ngắt gradient và đồng bộ cứng trong sơ đồ DQN.

## Hậu kiểm cuối

- Duyệt trực quan 46 trang ở 1280×720 và màn hình hẹp; chú ý L13-17, 20, 28, 34 và 39–40.
- Kiểm tra fragment ở L13-06, 12, 16, 19, 20, 23, 26, 31, 41 và X01–X04.
- Kiểm tra KaTeX strict, title tiếng Việt, SVG DQN và đường dẫn cục bộ.
- Lượt chỉnh sửa chỉ tuyên bố kiểm tra tĩnh; kiểm định cuối phải chạy HTTP và Codex Slides nếu công cụ khả dụng.
