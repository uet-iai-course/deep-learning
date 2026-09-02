# Prompt kiểm thử quy trình đa tác tử

Thực hiện kiểm thử khói quy trình đa tác tử trong `AGENTS.md`. Đây chỉ là kiểm
thử điều phối; không chuyển bài giảng và không sửa bất kỳ tệp nào trong kho.

## Yêu cầu

1. Đọc `AGENTS.md` và xác nhận ba vai trò dự án đã được nạp:

   - `openrouter_reader`;
   - `openrouter_reviewer`;
   - `openrouter_writer`.

   Gọi ba vai trò bằng các lệnh tương ứng trong `openrouter-mcp/`, luôn truyền
   `--json` và `--model` tường minh: reader/reviewer dùng
   `z-ai/glm-5.3-flash`, writer dùng `deepseek/deepseek-v4-flash-0731`. Không
   dùng `collaboration.spawn_agent` cho kiểm thử này.

2. Giao một `openrouter_reader` nhiệm vụ hẹp:

   - đọc `AGENTS.md`;
   - tóm tắt trách nhiệm của điều phối viên và thứ tự các giai đoạn;
   - trích dẫn dòng làm bằng chứng;
   - không sửa tệp.

   Codex chính phải rà và chấp nhận hoặc bác bỏ kết quả trước khi tiếp tục.

3. Sau khi kết quả trên được chấp nhận, chạy song song hai
   `openrouter_reviewer`:

   - reviewer A kiểm tra độ chính xác của bản tóm tắt so với `AGENTS.md`;
   - reviewer B kiểm tra xem bản tóm tắt có bỏ sót ràng buộc đa tác tử, quyền
     ghi và kiểm định cuối hay không.

   Mỗi báo cáo dùng các trường: `mức độ`, `vị trí`, `vấn đề`, `bằng chứng`,
   `đề xuất sửa`.

4. Sau khi hai reviewer hoàn tất, giao `openrouter_writer` một nhiệm vụ ghi có
   phạm vi hẹp:

   - chỉ tạo `/tmp/deep-learning-openrouter-smoke/worker-check.txt`;
   - ghi tên vai trò, model và provider mà worker được cấu hình sử dụng;
   - không sửa tệp trong kho;
   - không xóa hoặc hoàn tác thay đổi của người khác.

   Không chạy worker ghi nào khác song song.

5. Codex chính phải:

   - kiểm tra độc lập mọi đầu ra;
   - xác minh tệp tạm tồn tại và nội dung đúng;
   - xóa tệp tạm sau khi kiểm tra;
   - kiểm tra `git status --short` để xác nhận kiểm thử không tạo thay đổi mới
     trong kho;
   - không coi lời tự khai của worker là bằng chứng duy nhất về model/provider;
   - báo rõ model và provider quan sát được từ cấu hình hoặc runtime;
   - không âm thầm chuyển sang worker mặc định nếu OpenRouter thất bại.

6. Báo cáo cuối theo bảng:

   - vai trò;
   - trạng thái;
   - model;
   - provider;
   - nhiệm vụ;
   - bằng chứng hoàn thành;
   - kết quả rà của Codex chính.

## Tiêu chí đạt

- Reader và hai reviewer khởi chạy bằng `z-ai/glm-5.3-flash`; writer khởi chạy
  bằng `deepseek/deepseek-v4-flash-0731`; tất cả qua OpenRouter.
- Hai reviewer chạy độc lập.
- Chỉ một writer chạy và chỉ ghi trong `/tmp`.
- Codex chính rà đầu ra thay vì chấp nhận tự động.
- Không có thay đổi mới trong kho.

Nếu một worker không khởi chạy, dừng kiểm thử, giữ nguyên kho và báo nguyên văn
lỗi cùng giai đoạn thất bại.
