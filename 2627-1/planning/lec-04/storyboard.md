# Bảng phân cảnh Bài 04

## Bản đồ hành trình — bảy mạch

Mạch 1 (L04-00–07, 20 phút) → mạch 2 (L04-08–15, 20 phút) → mạch 3 (L04-16–28, 34 phút) → mạch 4 (L04-29–32, 11 phút) → mạch 5 (L04-33–37, 12 phút) → mạch 6 mở rộng (L04-X01–X05, 20 phút) → mạch 7 kết luận (L04-38, 3 phút). Tuyến lõi đi mạch 1–5 rồi End tại L04-37 tới L04-38 (100 phút). Tuyến đầy đủ từ L04-37 nhấn phải tới X01, nhấn xuống qua X02–X05, rồi nhấn phải tới L04-38 (120 phút).

| Mạch | Vai trò trong mạch | Kết nối vào | Kết nối ra |
|---|---|---|---|
| 1 | Mở vấn đề làm phẳng và thiết lập cục bộ, chia sẻ | Đầu bài | Hai giả định dẫn tới phép tính trên một cửa sổ. |
| 2 | Xây phép tương quan chéo một kênh từ ví dụ kiểm chứng được | Từ L04-07 | Khóa trục và hình học cho cả lô |
| 3 | Mở rộng sang kích thước, nhiều kênh, tham số và MAC | Từ L04-15 | Sang phép tóm tắt không có tham số |
| 4 | Xây phép gộp và giới hạn phát biểu về bất biến | Từ L04-28 | Đo vùng phụ thuộc của đơn vị sâu |
| 5 | Xây truy hồi trường tiếp nhận và nối sang thân–đầu mạng | Từ L04-32 | End tới mạch 7 hoặc nhấn phải sang mạch 6 |
| 6 | Mở rộng tự chọn, bỏ nguyên mạch không làm đứt tuyến lõi | Từ L04-37 bằng phím phải | Từ X05 nhấn phải sang mạch 7 |
| 7 | Thu hồi vấn đề mở đầu và chốt bốn phép kiểm | Từ L04-37 bằng End hoặc từ X05 bằng phím phải | Kết thúc bài |

## Tuyến lõi — 100 phút

| Mã | Phút | Bước | Luận điểm | Nguồn |
|---|---:|---|---|---|
| L04-00 | 2 | Vấn đề | Ảnh có cấu trúc không gian | đề cương |
| L04-01 | 2 | Mục tiêu/quy ước | Mục tiêu và quy ước | đề cương |
| L04-02 | 2 | Vấn đề | Làm phẳng giữ giá trị nhưng không mã hóa tường minh quan hệ cục bộ | slide 3–4; GT 110 |
| L04-03 | 2 | Vấn đề/tính toán | Tầng đầy đủ tăng tham số theo kích thước ảnh | GT 110–112 |
| L04-04 | 3 | Trực giác | Kết nối cục bộ | slide 5–7; GT 113–114 |
| L04-05 | 3 | Hình thức | Chia sẻ cùng nhân theo vị trí | slide 5–7; GT 113 |
| L04-06 | 3 | Triển khai | Tương đương dịch chuyển có điều kiện | GT 111–114 |
| L04-07 | 3 | Kiểm tra | Phân biệt cục bộ và chia sẻ | tổng hợp |
| L04-08 | 2 | Vấn đề | Một cửa sổ phải tạo một ô đầu ra | slide 8–16 |
| L04-09 | 3 | Trực giác | Tương quan chéo giữ nguyên hướng nhân | GT 114 |
| L04-10 | 3 | Ví dụ | Khóa $X,K,b$, vùng đệm và bước trượt | GT 116–119 |
| L04-11 | 2 | Ví dụ/tính toán | Tính $Y_{00}=19$ | tính lại |
| L04-12 | 3 | Ví dụ/tính toán | Tính đủ ma trận đầu ra | tính lại |
| L04-13 | 3 | Hình thức | Khái quát phép tính một kênh | GT 116–119 |
| L04-14 | 2 | Kiểm tra cơ chế | Trượt một cột thay dữ liệu nhưng giữ tham số | slide 9–16 |
| L04-15 | 2 | Kiểm tra | Đối chiếu quy ước API và phép tính tay | GT 114 |
| L04-16 | 2 | Hình thức | Khóa NCHW/OIHW | GT 123–126 |
| L04-17 | 2 | Trực giác | Vùng đệm quyết định biên | slide 17–20; GT 119–121 |
| L04-18 | 2 | Trực giác | Bước trượt quyết định điểm đặt cửa sổ | slide 17–20 |
| L04-19 | 3 | Hình thức | Công thức $H_{out},W_{out}$ | GT 121–123 |
| L04-20 | 4 | Ví dụ/tính toán | Ví dụ $2×3×6×7\to2×4×3×4$ | tính lại |
| L04-21 | 2 | Hình thức | Điều kiện giữ kích thước khi bước trượt 1 | GT 120–123 |
| L04-22 | 1 | Kiểm tra | Điều kiện cửa sổ hợp lệ | tổng hợp |
| L04-23 | 3 | Vấn đề/trực giác | Một kênh ra phải gom mọi kênh vào; định nghĩa $\widetilde X$ | GT 123–125 |
| L04-24 | 3 | Ví dụ | Khóa hai ma trận vào, hai lát nhân, $b=0$ và tính 56 | GT 125 |
| L04-25 | 3 | Kiểm tra ví dụ | Tái lập lát $Y_{0,0,:,:}=[[56,72],[104,120]]$ | GT 125 |
| L04-26 | 3 | Hình thức | Nối $K$ sang tensor $W$ và nhiều kênh ra | slide 23–28 |
| L04-27 | 3 | Tính toán/ứng dụng chi phí | Đếm tham số $C_{out}(C_{in}K_hK_w+1)$ | GT 126 |
| L04-28 | 3 | Tính toán/ứng dụng chi phí | MAC theo mẫu và theo lô | slide 29; tính lại |
| L04-29 | 3 | Vấn đề | Phép gộp tóm tắt cửa sổ | slide 38–42; GT 127–130 |
| L04-30 | 4 | Tính toán | Gộp cực đại ví dụ 4×4 | slide 39–41 |
| L04-31 | 2 | Tính toán | Gộp trung bình cùng cửa sổ | tính lại |
| L04-32 | 2 | Kiểm tra | Thường giảm độ phân giải; độc lập theo kênh; không bất biến tuyệt đối | GT 129–130 |
| L04-33 | 2 | Vấn đề | Định nghĩa vùng trên đầu vào hoặc tầng tham chiếu | slide 44–45 |
| L04-34 | 3 | Trực giác | Theo dõi $r_l,j_l$ trên cùng tầng tham chiếu | slide 46–50 |
| L04-35 | 2 | Ví dụ | Ba tầng dùng nhân 3×3, bước trượt 1: $r=7$ | slide 46–48 |
| L04-36 | 3 | Hình thức/kiểm tra | Truy hồi giải thích bước trượt làm tăng khoảng nhảy và trường tiếp nhận | slide 49–50 |
| L04-37 | 2 | Cầu nối ứng dụng thân–đầu | Tích chập, kích hoạt, thân mạng và đầu dự đoán | slide 52–53 |

Tổng lõi mạch 1–5: **97 phút**; cộng kết luận L04-38 (3 phút) là **100 phút**.

## Tuyến mở rộng — 20 phút

| Mã | Phút | Nội dung | Nguồn |
|---|---:|---|---|
| L04-X01 | 4 | Nhân phát hiện cạnh | GT 116–119 |
| L04-X02 | 4 | Tích chập 1×1 trộn kênh | GT PDF 126–127 |
| L04-X03 | 3 | Lan truyền ngược qua gộp cực đại | slide 42 |
| L04-X04 | 6 | Dấu vết kích thước LeNet | GT 132–134 |
| L04-X05 | 3 | Cầu nối sang huấn luyện | GT 131–132 |

Tổng mở rộng: **20 phút**.

## Kết luận — 3 phút

| Mã | Phút | Nội dung | Nguồn |
|---|---:|---|---|
| L04-38 | 3 | Bốn phép kiểm; thu hồi vấn đề mở đầu | tổng hợp |

## Điều hướng

- Tuyến lõi: đi ngang L04-00 → L04-37; tại L04-37 bấm **End** tới trang cuối L04-38.
- Tuyến đầy đủ: từ L04-37 nhấn **phải** tới X01; nhấn **xuống** qua X02–X05; sau X05 nhấn **phải** tới L04-38.
- Không đưa chỉ dẫn điều hướng hoặc timing lên mặt slide hay ghi chú diễn giả.

## Chu trình học tập và dữ kiện truyền

| Cụm | Sáu bước và mã trang | Đầu vào → sản phẩm | Dữ kiện truyền | Bước gộp hoặc không áp dụng | Câu nối | Thời lượng và điều hướng |
|---|---|---|---|---|---|---|
| Cục bộ và chia sẻ | Vấn đề L04-02–03 → trực giác L04-04 → ví dụ L04-05 → hình thức L04-05 → triển khai L04-06 → kiểm tra L04-07 | Ảnh và tầng đầy đủ → phân biệt hai giả định kiến trúc | $C_{in},H_{in},W_{in},K_h,K_w,W$ | Ví dụ và hình thức chia sẻ gộp ở L04-05 vì cùng sơ đồ một $W$ dùng ở nhiều vị trí | Hai giả định dẫn tới phép tính trên một cửa sổ. | 16 phút; đi ngang L04-02→07 |
| Tương quan chéo một kênh | Vấn đề L04-08 → trực giác L04-09 → ví dụ L04-10–12 → hình thức L04-13 → triển khai L04-14 → kiểm tra L04-15 | Cửa sổ cục bộ → công thức và ma trận đầu ra kiểm chứng được | $X,K,b=0$, không đệm, $S=1$, kết quả 19→$Y$ | Tính toán gộp với ví dụ ở L04-11–12; triển khai cơ chế trượt dùng hiệu ứng xuất hiện ở L04-14 | “Khóa thêm trục và hình học để áp dụng phép tính cho cả lô.” | 20 phút; hiệu ứng hiện đáp án ở L04-14 |
| Kích thước tensor | Vấn đề/quy ước L04-16 → trực giác L04-17–18 → hình thức L04-19 → ví dụ/tính toán L04-20 → hình thức L04-21 → kiểm tra L04-22 | NCHW/OIHW và hình học → $Y:2×4×3×4$ | $P_t=P_b=P_l=P_r=1$, $S_h=S_w=2$, $K=3$ | L04-16 gộp vấn đề với quy ước trục cần có trước trực giác; không có mã vì nguồn không có | “Một kênh ra còn phải gom thông tin qua trục kênh vào.” | 16 phút; hiệu ứng hiện đáp án ở L04-22 |
| Nhiều kênh và chi phí | Vấn đề L04-23 → trực giác L04-23 → ví dụ L04-24 → kiểm tra ví dụ L04-25 → hình thức L04-26 → tính toán/ứng dụng chi phí L04-27–28 | Hai kênh vào → một kênh ra, rồi $C_{out}$ kênh và chi phí | $X_{0,0,:,:},X_{0,1,:,:},W_{0,0,:,:},W_{0,1,:,:},b_0=0$, 56→$Y_{0,0,:,:}$; kích thước từ L04-20 | Định nghĩa tensor đệm phải gộp ở L04-23 để công thức không dùng chỉ số ngoài miền; kiểm tra ví dụ L04-25 đứng trước khái quát $C_{out}$ ở L04-26 vì bám ngay dữ kiện vừa tính | “Sau tầng có tham số, xét phép tóm tắt cửa sổ không có tham số.” | 18 phút; hiệu ứng hiện kết quả ở L04-25 |
| Phép gộp | Vấn đề/trực giác L04-29 → ví dụ và hình thức L04-30–31 → triển khai không áp dụng → kiểm tra L04-32 | Ma trận 4×4 → hai đầu ra 2×2 và giới hạn về bất biến | Cửa sổ 2×2, $S=2$, cùng $X$ cho cực đại và trung bình | Hình thức gộp với tính toán của hai ví dụ; không có triển khai API vì nguồn không có mã | “Độ sâu của mạng làm một đơn vị phụ thuộc vùng đầu vào lớn đến đâu?” | 11 phút; đi ngang L04-29→32 |
| Trường tiếp nhận | Vấn đề L04-33 → trực giác L04-34 → ví dụ L04-35 → hình thức/kiểm tra L04-36 → triển khai L04-37 | Tầng tham chiếu → truy hồi $r,j$ và thân mạng nhiều tầng | $r_0=j_0=1$, $(K,S)$, chuỗi 3→5→7 | Kiểm tra gộp với hình thức ở L04-36 vì câu hỏi giải thích đúng hạng $(K_l-1)j_{l-1}$ | “Dùng kích thước, chi phí và trường tiếp nhận để kiểm tra toàn tầng.” | 12 phút; đi ngang L04-33→37; tại L04-37 chọn End tới kết luận hoặc nhấn phải sang mở rộng |

Các trang L04-00–01 chiếm 4 phút mở đầu và nêu quy ước; tổng các cụm còn lại là 93 phút, cộng L04-38 là 100 phút lõi. Tuyến mở rộng nằm ở mạch 6 và có thể bỏ nguyên mạch mà không đứt mạch kết luận L04-38.

## Bài tập 50 phút riêng

1. Tính tương quan chéo bằng tay: 15 phút.
2. Tính kích thước tensor và số tham số: 15 phút.
3. Phép gộp: 10 phút.
4. Trường tiếp nhận: 10 phút.

Đề và đáp án ở `note-for-author.md`.
