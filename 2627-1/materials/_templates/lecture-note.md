# Bài NN — Tên chủ đề

## Mục tiêu và kiến thức tiên quyết

- Nêu mục tiêu có thể quan sát hoặc đánh giá được.
- Nêu kiến thức, ký hiệu và quy ước tensor cần dùng.

## Ký hiệu và quy ước

Nêu miền, kiểu dữ liệu, kích thước tensor, thứ tự trục, chiều lô, quy ước broadcasting và thiết bị trước khi dùng. Ví dụ: $X\in\mathbb R^{B\times d}$.

## Khái niệm trọng tâm

Đi theo mạch tự học **vai trò/nhu cầu → định nghĩa hoặc đặc tả → ví dụ tính được → trực giác → hình thức, thuật toán hoặc chứng minh → triển khai/ứng dụng → tự kiểm tra**. Có thể gộp bước hoặc ghi `không áp dụng` kèm lý do; không tạo đề mục rỗng.

::: example Ví dụ tính được
Nêu dữ kiện, kích thước tensor, phép tính và kết luận có thể kiểm tra.
:::

::: derivation Suy diễn chi tiết
Trình bày từng bước biến đổi, biến lấy đạo hàm, đại lượng được giữ cố định và điều kiện sử dụng.
:::

::: proof Chứng minh
Nêu mục tiêu, ý tưởng, các bước then chốt và điểm dùng giả thiết.
:::

::: exercise Câu hỏi kiểm tra
Đặt một câu hỏi đo đúng mục tiêu của phần.
:::

::: hint
Đưa ra bước khởi đầu, không thay toàn bộ lời giải.
:::

::: solution
Nêu kết quả hoặc cách tự đối chiếu ngắn. Đặt lời giải chi tiết trong `note-for-author.md`.
:::

## Từ công thức đến triển khai

Nối ký hiệu và tensor của ví dụ với lan truyền xuôi, hàm mất mát, lan truyền ngược, bước cập nhật hoặc suy luận khi các bước này thuộc phạm vi nguồn. Không tự tạo code minh họa nếu nguồn không có code.

## Tự kiểm tra

- Kiểm tra kích thước tensor, số tham số, gradient hoặc kết quả số quan trọng.
- Phân biệt dữ liệu, nhãn, tham số, siêu tham số, hàm mất mát, bộ tối ưu, độ đo và dự đoán.

## Tài liệu tham khảo

- Ghi tệp nguồn, số trang hoặc trang chiếu, chương, mục, hình, bảng hay thuật toán cụ thể.
