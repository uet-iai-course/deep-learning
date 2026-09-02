# Goal: tạo ghi chú bài giảng rồi đồng bộ bộ trang chiếu cho một buổi Học sâu

## Đầu vào

Buổi cần xử lý: `<NN>`

Chỉ chấp nhận `NN` thuộc `01`–`08` hoặc `10`–`14`. Xử lý đúng một buổi trong mỗi lần chạy goal này. Suy ra tên bài, slug, LLO, phạm vi và toàn bộ nguồn từ mục đúng buổi trong `source.md`, rồi đối chiếu chuẩn cao nhất là `III.2 → Buổi N → tên trường` của DOCX đề cương. Không làm buổi 09 hoặc 15, không đánh số lại và không tự chọn nguồn.

## Quyền đã được người dùng cấp

> Tôi cho phép commit/push sau khi hoàn tất từng lecture note hoặc slide deck.

> Tôi cho phép gửi các file nội bộ project lên OpenRouter, trừ .env và các bí mật.

Quyền thứ hai loại trừ mọi `.env`, `.env.*`, khóa API, token, mật khẩu, cookie, khóa riêng, thông tin xác thực và mọi tệp hoặc đoạn dữ liệu chứa bí mật. Worker OpenRouter không được đọc các nội dung đó; không chép chúng vào prompt, log, dossier hoặc dữ liệu gửi đi. Codex chính chỉ được kiểm tra cục bộ tên và dấu hiệu bí mật để loại tệp khỏi dossier, không in giá trị ra log. Quyền commit/push chỉ áp dụng cho sản phẩm đã vượt checkpoint; không cho phép sửa, xóa, hoàn tác hoặc đưa thay đổi bẩn của người dùng ngoài phạm vi vào commit.

## Hợp đồng điều phối

Làm việc tại kho `deep-learning`. Đọc đầy đủ `AGENTS.md` hiện hành trước mọi thao tác. Tham khảo kho thực tế `../ds-foundation-algorithms`, đặc biệt quy trình ghi chú, viewer, index và điều phối OpenRouter, nhưng **chỉ kế thừa quy trình và mẫu hành vi**; không sao chép nội dung môn học, tên học phần, nguồn, tài sản hay quyết định phạm vi từ kho đó.

Codex chính là điều phối viên: duyệt đầu ra ở từng điểm hợp nhất, tự tính lại nội dung kỹ thuật quan trọng, áp dụng thay đổi vào kho, kiểm định cuối và quản lý Git. Worker OpenRouter đảm nhiệm các vai dự án; không thay ngầm bằng worker khác khi một worker lỗi.

- Reader và reviewer: `z-ai/glm-5.3-flash`.
- Writer: `deepseek/deepseek-v4-flash-0731`.
- Mọi lệnh worker phải truyền rõ `--model ... --json`, cùng `--repo-root`, `--task-profile`, mục tiêu, tệp được phép đọc/ghi, sản phẩm bàn giao và điều kiện dừng.
- Dùng `uv run openrouter-mcp-reader`, `uv run openrouter-mcp-reviewer`, `uv run openrouter-mcp-writer` từ `openrouter-mcp/`. Không cấp gốc kho thật cho worker. Codex chính phải trích đúng dải PDF/DOCX thành UTF-8, giữ mốc tệp–trang/slide/mục, rồi tạo một thư mục dossier tạm theo allowlist cho từng stage. Reader và reviewer chỉ đọc dossier; writer chỉ ghi trong một staging root hẹp chứa dossier và bản sao các tệp đích đã khóa.
- Không dùng các ví dụ cũ có `--repo-root ..` hoặc `MCP_REPO_ROOT=..` trong `openrouter-mcp/README.md` cho quy trình này. Chúng không đáp ứng biên bí mật của goal; các lệnh dưới đây thay thế chúng.
- Sau **mỗi** lệnh, kiểm tra metadata máy trả về: `requested_model`, `observed_model`, `provider`. Chỉ nhận nếu hai model đều đúng model đã yêu cầu và `provider` là OpenRouter. Nếu lệch model, thiếu metadata, lỗi, timeout hoặc đầu ra dở dang, dừng giai đoạn phụ thuộc, giữ kho ở trạng thái an toàn và báo nguyên văn lỗi; không dùng kết quả lỗi và không tự đổi model/provider.

Mẫu tối thiểu của các lệnh là:

```bash
uv run openrouter-mcp-reader --repo-root "$DOSSIER_ROOT" --model z-ai/glm-5.3-flash --json --task-profile plan "<nhiệm vụ chỉ đọc>"
uv run openrouter-mcp-reviewer --repo-root "$REVIEW_ROOT" --model z-ai/glm-5.3-flash --json --task-profile review "<nhiệm vụ rà soát>"
uv run openrouter-mcp-writer --repo-root "$WRITER_ROOT" --model deepseek/deepseek-v4-flash-0731 --json --task-profile write "<nhiệm vụ ghi có phạm vi hẹp>"
```

Với lượt soạn toàn tệp, bắt buộc thêm `MCP_WRITE_POLICY=create-once` trước
`uv run`. Hàng rào này từ chối lần ghi thứ hai vào cùng đường dẫn và vô hiệu
hóa `replace_text_file`; cầu nối kết thúc worker ngay sau lần ghi thành công
đầu tiên. Luôn dùng staging mới, nơi tệp đích chưa tồn tại.

### Ngân sách phạm vi cho DeepSeek writer

Không giao cho một lượt writer đồng thời đọc toàn bộ dossier, soạn nhiều tệp dài, tự kiểm toàn bộ và viết báo cáo. Lượt soạn và lượt tự kiểm là hai công đoạn tuần tự, dùng cùng model nhưng có staging/checkpoint riêng:

1. **Lượt soạn:** sau checkpoint A1, mặc định chỉ đọc `approved-spec.md`, mẫu sản phẩm và tối đa ba tệp đích liên quan trực tiếp; không đọc lại gói trích đoạn nguồn thô. `approved-spec.md` phải chứa đủ mốc nguồn, phép tính khóa và quyết định phạm vi đã được GLM/Codex đối chiếu. Chỉ cấp thêm một trích đoạn ngắn, đã định danh khi thiếu bằng chứng cụ thể trong đặc tả. Nếu cần cập nhật nhiều hơn ba tệp, chia theo sản phẩm: `lecture-note.md` trước, planning sau; HTML/SVG trước, planning sau.
2. **Lượt tự kiểm:** chỉ đọc các tệp vừa ghi và checklist ngắn; không đọc lại toàn bộ dossier. Mặc định lượt này **chỉ báo cáo**, tạo `writer-report.md` và không sửa sản phẩm. Chỉ mở task sửa riêng khi báo cáo chỉ ra tối đa ba thay thế ngắn đã khóa bằng điểm neo; task đó chỉ trả các mảnh thay thế, không viết lại toàn tệp. Mọi yêu cầu “đánh bóng”, “hiệu chỉnh toàn văn” hoặc tự viết lại sản phẩm trong lượt tự kiểm đều bị cấm.
3. Mỗi task phải liệt kê chính xác tệp được đọc, tệp được ghi và thứ tự ưu tiên. Một task không được vừa thực hiện nhiều lệnh thay thế cục bộ vừa tạo tệp thứ hai. Lượt soạn toàn tệp chỉ được gọi thao tác ghi toàn bộ tệp **đúng một lần**; sau khi tệp hợp lệ đã tồn tại, writer phải dừng và không phát lại toàn văn để tự đánh bóng. Khi chỉ có tối đa ba thay thế đã khóa, task sửa riêng mới được trả thay thế cục bộ. Yêu cầu writer ghi checkpoint/tệp đích ngay sau khi đã có nội dung hợp lệ, không dành một vòng dài để suy luận toàn bộ rồi mới ghi.
4. Không yêu cầu writer “kiểm tra mọi thứ” hoặc “đọc khi cần” mà không khóa danh sách tệp. Mọi kiểm định rộng, đối chiếu nguồn chéo và hợp nhất năm vai thuộc về GLM reviewer và Codex chính.
5. Nếu một lượt chạm `finish_reason=length`, vượt giới hạn tool-call, timeout hoặc chưa tạo đủ tệp bàn giao, coi lượt đó là lỗi và không nhập đầu ra. Ghi nguyên nhân, số tệp/phạm vi đã giao và cách chia nhỏ vào `review-log.md`; chạy lại đúng model với task hẹp hơn từ checkpoint an toàn. Không tăng token hay số vòng như cách khắc phục đầu tiên.
6. Mẫu đã ổn định cho các buổi sau là: **soạn một sản phẩm → kiểm tra tệp tồn tại → tự kiểm cục bộ và viết báo cáo → Codex/GLM rà rộng**. Mọi ngoại lệ phải ghi lý do trong `review-log.md`.
7. Với tệp planning hoặc HTML dài, không yêu cầu writer phát lại toàn tệp nếu phần thay đổi chỉ là bổ sung/cục bộ. Writer tạo một mảnh Markdown/HTML có điểm neo rõ, mặc định dưới 1.500 từ hoặc dưới 6.000 ký tự; Codex kiểm rồi chèn bằng `apply_patch`. Chỉ viết lại toàn tệp khi đầu ra ước tính chắc chắn nằm trong ngân sách và cấu trúc thay đổi trên diện rộng. `invalid_json` khi ghi một tool-call dài được xử lý bằng mảnh bổ sung, không bằng tăng token hay lặp lại nguyên task.
8. Mỗi task writer dùng một staging root vật lý riêng chỉ chứa đúng các đầu vào đã liệt kê và thư mục cho một đầu ra. Không tái dùng staging có sản phẩm/báo cáo của task trước, vì worker có thể tự liệt kê hoặc mở chúng và tiêu hao vòng gọi dù prompt đã cấm. Sau khi task PASS metadata, Codex mới chuyển đầu ra sang bước hợp nhất.
9. Khi viết lại ghi chú diễn giả trong HTML, chia theo tối đa **5 khối `<aside class="notes">` mỗi task**. Mỗi task chỉ nhận các khối cần sửa cùng `data-slide-id`, trả đúng các khối thay thế và không phát lại toàn HTML. Kinh nghiệm Buổi 01 cho thấy lô 10 khối không ổn định: ba lô đầu có thể hoàn tất nhưng lô cuối dở dang; chia 5+5 đã hoàn tất trên cùng model. Vì vậy 5 là trần mặc định cho các đợt sau, không phải giá trị để tự động tăng khi một lượt thành công. Nếu một khối riêng vượt 1.500 từ/6.000 ký tự, tách tiếp theo điểm neo nội bộ.
10. Với bản nháp lecture note, mẫu ổn định từ Buổi 02 là **hai đầu vào, một đầu ra**: lượt soạn chỉ nhận `approved-spec.md` và mẫu lecture note, chỉ ghi `lecture-note.md` đúng một lần. Lượt tự kiểm dùng staging mới, chỉ nhận bản nháp và checklist, rồi chỉ ghi `writer-report.md`. Không gộp báo cáo, planning, index hoặc SVG vào hai lượt này. Nếu cần tạo SVG mới, chạy một task riêng cho từng nhóm tài sản đã khóa sau khi nội dung và nhãn hình được duyệt.
11. Nếu writer lặp thao tác ghi toàn bộ tệp, tự kiểm làm hỏng công thức/Unicode/đường dẫn, hoặc đầu ra sai danh sách tệp, loại bỏ toàn bộ đầu ra của task đó và quay về checkpoint hợp lệ gần nhất. Không vá nối tiếp trên bản hỏng. Ghi sự cố, dấu hiệu phát hiện, checkpoint khôi phục và phạm vi task thay thế vào `review-log.md` để các buổi sau không lặp lại.
12. Nếu một bản tiếng Việt dài vẫn hỏng Unicode/KaTeX dù đã dùng `create-once`, không thử lại toàn bản quá một lần. Chuyển sang các task mảnh tuần tự trong staging mới, mỗi mảnh chỉ bao phủ một hoặc hai mục đã khóa và mặc định không quá 2.500 ký tự; mỗi task phải đặt cả `MCP_WRITE_POLICY=create-once` và `MCP_MAX_WRITE_CHARS=2500`. Server từ chối toàn bộ lần ghi vượt trần và không tạo tệp đích một phần. Codex kiểm UTF-8, ký tự thay thế, ký tự Cyrillic lẫn vào tiếng Việt, KaTeX và đường dẫn trước khi hợp nhất bằng `apply_patch`. Bác toàn bộ mảnh có lỗi; không sửa nối tiếp trên mảnh hỏng.

Khóa phải được điều phối viên nạp qua môi trường hoặc launcher `codex-orchestrator`; CLI hiện tại không có tùy chọn `--api-key-root`. Trước mỗi lệnh, liệt kê toàn bộ dossier theo allowlist, từ chối symlink và quét cả tên lẫn nội dung để loại `.env*`, khóa, token, mật khẩu, cookie, khóa riêng, thông tin xác thực và chuỗi bí mật. Không chép tệp nhị phân nguồn, đường dẫn khóa hay nội dung bí mật vào dossier, task, log hoặc kết quả worker. Nếu không chứng minh được dossier đã lọc, dừng trước khi gọi OpenRouter.

## Tiền kiểm hạ tầng ghi chú

Hạ tầng ghi chú đã được bootstrap trong kho. Trước buổi đầu tiên, chỉ **kiểm tra**, không tái tạo vô điều kiện:

- `2627-1/material-viewer.html`, `material-viewer.css`, `material-viewer.js`, `material-index.css`;
- mẫu ghi chú trong `2627-1/materials/_templates/`;
- KaTeX hiện có, Marked `18.0.7` và DOMPurify `3.4.7` trong `2627-1/vendor/`;
- quy ước ghi chú/viewer/index/semantic contract/OpenRouter trong `AGENTS.md`;
- các ngoại lệ theo dõi `materials/`, viewer, template và tài sản cần thiết trong `.gitignore`.

Chỉ sửa hạ tầng khi kiểm tra cho thấy lỗi hoặc khoảng trống cụ thể. Nếu phải sửa, cập nhật `AGENTS.md` và `.gitignore` có chủ đích để phản ánh đúng cấu trúc theo dõi; không mở rộng whitelist quá mức, không theo dõi tệp tạm/log/dossier, và kiểm tra ảnh hưởng tới các bài khác. Ghi lý do, diff và kiểm định hồi quy trong `review-log.md`. Viewer phải giới hạn `doc` vào `materials/lec-NN/lecture-note.md`, buộc số buổi của `doc` và `deck` trùng nhau, làm sạch HTML trước khi gắn DOM, không thực thi HTML/script từ Markdown, dùng KaTeX cục bộ và không phụ thuộc mạng cho chức năng cốt lõi.

## Đầu ra bắt buộc của buổi

- `2627-1/materials/lec-NN/lecture-note.md`;
- tệp `2627-1/lecture-NN-SLUG.html`, trong đó `SLUG` được suy ra từ bài hiện có hoặc tên bài trong nguồn; chỉ cập nhật ở pha bộ trang chiếu;
- SVG cần thiết tại `2627-1/img/lec-NN/`;
- đủ bốn tệp `2627-1/planning/lec-NN/outline.md`, `storyboard.md`, `review-log.md`, `note-for-author.md`;
- mục bài tương ứng trong `2627-1/index.html`.

Ghi chú là tài liệu tự học công khai, đọc độc lập với slide nhưng dùng cùng thuật ngữ, ký hiệu, giả thiết, ví dụ và thứ tự khái niệm. Không sao chép nguyên văn slide hoặc ghi chú diễn giả. Mã nội bộ, tuyến cắt, đáp án chi tiết của hoạt động trên lớp, trạng thái kiểm chứng và chỉ dẫn triển khai chỉ nằm trong planning, đặc biệt `note-for-author.md`, không hiện trong ghi chú công khai, mặt slide hoặc ghi chú diễn giả. Khối `solution` công khai, nếu dùng, chỉ chứa kết quả hoặc cách tự đối chiếu ngắn có căn cứ nguồn; lời giải chi tiết vẫn đặt trong `note-for-author.md`.

`index.html` phải giữ thẻ đúng thứ tự và có hai tài nguyên mang nhãn `Bài giảng` và `Ghi chú bài giảng`. Chỉ sau khi ghi chú vượt QA mới liên kết:

```text
material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-SLUG.html
```

Trước đó hiển thị trạng thái `Chưa có`, không tạo liên kết giả. Không liên kết bất kỳ tệp planning nào.

## Nguồn và bản đồ chủ đề

Đọc đầy đủ mục của buổi trong `source.md`, đúng dải trang đã ánh xạ, DOCX đề cương và các nguồn được mục đó duyệt. DOCX khóa phạm vi; slide được ánh xạ khóa mạch chính trong phạm vi; giáo trình `hocsau_draft.pdf` chỉ khôi phục tiên quyết, kiểm chứng công thức/shape/giả thiết và làm rõ luồng. Với buổi 06, 13, 14 dùng đúng các PDF và dải đã duyệt. Không dùng trang ngoài dải, nguồn web, kiến thức nhớ lại hay các PDF bị cấm nếu chưa được người dùng duyệt. Nếu nguồn được yêu cầu thiếu/hỏng hoặc đề cương yêu cầu nội dung mà nguồn duyệt không đủ, dừng phần phụ thuộc và hỏi người dùng.

Hai reader độc lập đề xuất bản đồ chủ đề. Mỗi chủ đề có `note-topic-id` duy nhất và đúng một nhãn:

- `cốt lõi`: trực tiếp thực hiện phạm vi/LLO và mạch slide nguồn;
- `cầu nối`: bổ sung định nghĩa, tiên quyết hoặc bước suy luận thiếu để nối hai chủ đề cốt lõi;
- `bổ sung`: làm rõ bằng ví dụ, chứng minh, trường hợp biên hay triển khai có nguồn đã duyệt;
- `đọc thêm`: hữu ích nhưng không cần cho tuyến chính hoặc chưa đủ nguồn để soạn thành mệnh đề học thuật.

Mỗi đề xuất `cầu nối` hoặc `bổ sung` phải nêu khoảng trống cụ thể, nguồn trong dải đã chọn và tác động đến mạch. `đọc thêm` chỉ ghi chỉ dẫn đọc và nguồn đã duyệt, không lén mở rộng phạm vi. Điều phối viên hợp nhất và ghi quyết định `giữ`, `thêm`, `gộp`, `tách`, `chuyển đọc thêm` hoặc `bỏ` vào `outline.md` và `review-log.md` trước khi writer chạy.

Thiết lập hợp đồng ngữ nghĩa trong storyboard:

- ánh xạ mỗi `note-topic-id` tới một hay nhiều `data-slide-id`, và mỗi trang nội dung tới chủ đề mà nó phục vụ;
- ghi phần chung về thuật ngữ, ký hiệu, giả thiết, ví dụ, kết luận và nguồn;
- lập `delta deck` cho từng chủ đề với quyết định `giữ nguyên`, `sửa cục bộ`, `thêm trang`, `gộp/tách`, `đổi thứ tự cục bộ` hoặc `không đưa lên slide`, kèm lý do và các trang lân cận bị ảnh hưởng;
- không ép quan hệ một-một: ghi chú được phép sâu hơn, còn slide phải giữ một luận điểm trung tâm và thời lượng theo `AGENTS.md`.

Mỗi chủ đề trọng tâm của ghi chú đi theo mạch tự học: **vai trò/nhu cầu → định nghĩa hoặc đặc tả → ví dụ tính được → trực giác → hình thức, thuật toán hoặc chứng minh → triển khai/ứng dụng → tự kiểm tra**. Có thể gộp bước hoặc ghi `không áp dụng` kèm lý do; không tạo đề mục rỗng. Dùng cùng dữ kiện và ký hiệu xuyên suốt. Đây là mạch của tài liệu tự học, không thay thế chu trình riêng của slide trong `AGENTS.md`.

## Pipeline của một buổi

Dùng pipeline stage/fan-out/fan-in. Chụp một baseline chỉ đọc ở đầu buổi. Cho phép song song **trong cùng buổi** khi các worker chỉ đọc cùng baseline ổn định hoặc ghi vào các thư mục tạm tách biệt. Mọi writer và mọi lần áp dụng diff vào kho đều tuần tự. Không gối pipeline của hai buổi: phải hoàn tất ghi chú, commit/push, cập nhật deck, commit/push của buổi hiện tại rồi mới bắt đầu buổi kế tiếp, vì quy tắc tham khảo và các tệp dùng chung/index dễ xung đột.

### Pha A — Ghi chú bài giảng

1. **Chốt phạm vi và dossier.** Kiểm kê dirty worktree, nguồn, dải trang, deck hiện tại, bốn planning file, viewer/index và tài sản. Giữ nguyên thay đổi của người dùng ngoài phạm vi. Codex chính đọc nguồn nhị phân, trích đúng dải sang UTF-8 có mốc truy nguyên, lọc bí mật và đóng băng dossier chỉ đọc. Tạo goal và tiêu chí đạt cho đúng buổi.
2. **Fan-out chỉ đọc.** Chạy song song reader lập kế hoạch và reader phân tích nguồn; khi baseline đủ ổn định, chạy thêm reader/reviewer kiến trúc bản đồ chủ đề. Không tác tử nào sửa tệp.
3. **Fan-in checkpoint A1.** Kiểm metadata model/provider; hợp nhất ánh xạ trang nguồn, inventory công thức/hình/code, rủi ro, bản đồ chủ đề, semantic contract và kế hoạch QA. Codex chính duyệt phạm vi trước khi viết.
4. **Writer tuần tự.** Tạo staging root tối thiểu từ dossier đã duyệt và bản sao các tệp đích. Một DeepSeek writer soạn `lecture-note.md`, SVG cần thiết và đề xuất cập nhật planning. Codex kiểm diff, nguồn, phép tính và văn phong rồi mới áp dụng bằng `apply_patch`. Không cho writer sửa index hoặc hạ tầng ngoài danh sách đã khóa.
5. **Fan-out rà soát.** Chạy song song năm GLM reviewer chỉ đọc: góc nhìn sinh viên; chuyên gia Học sâu; toán–thuật toán–triển khai; phản biện học thuật–giảng dạy; kết nối–nguồn–mạch viết. Mỗi báo cáo có `mức độ`, `vị trí`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.
6. **Fan-in checkpoint A2.** Hợp nhất lỗi; một writer sửa tuần tự; Codex áp dụng và tính lại. Rà lại bằng reviewer độ chính xác sau thay đổi toán/shape/gradient/code, và reviewer mạch sau thay đổi cấu trúc. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
7. **Biên tập cuối, QA và xuất bản ghi chú.** Đọc toàn bộ lecture note, chạy lượt `$no-ai-slop` cuối và tự kiểm theo `no-ai-slop/eval.md` trước QA kỹ thuật. Xóa dấu vết soạn bằng AI, lời dẫn rỗng, câu hỏi tu từ, nhịp câu máy móc, kết luận lặp, siêu bình luận, nhãn quy trình, trạng thái kiểm chứng và mọi hướng dẫn dành cho người viết. Chuyển chỉ dẫn nội bộ còn cần thiết sang `note-for-author.md`; không để chúng trong tài liệu công khai. Sau đó kiểm Markdown, heading, công thức `$...$`/`$$...$$`, KaTeX, SVG và alt text, bảng, code, nguồn, liên kết, mục lục, khối gập, bàn phím, tương phản, màn hình rộng/hẹp và bản in. Các khối lời giải/gợi ý phải gập mặc định, thao tác được bằng bàn phím và mở khi in. Cập nhật liên kết ghi chú trong index chỉ sau khi PASS.
8. **Checkpoint A3 — Git.** Chạy `git status --short`, xem diff, chỉ stage sản phẩm ghi chú của buổi, SVG/planning/index và sửa hạ tầng thật sự liên quan. Ở ghi chú đầu tiên, đưa đúng các asset bootstrap đang chờ theo dõi vào cùng commit sau khi đã kiểm định; không tạo commit bootstrap riêng bằng quyền này và không gom thay đổi có sẵn ngoài phạm vi. Commit theo dạng `feat(materials-NN): add TEN_BAI lecture note` hoặc `fix(materials-NN): revise TEN_BAI lecture note`, trong đó `TEN_BAI` được suy ra từ nguồn, rồi `git push origin main`. Không force, rebase hoặc viết lại lịch sử. Nếu push lỗi, giữ commit cục bộ, báo lỗi và dừng trước pha B.

### Pha B — Đồng bộ bộ trang chiếu theo delta

Chỉ bắt đầu sau khi commit ghi chú xuất hiện trên `origin/main`.

1. **Baseline mới.** Đọc lại deck, note đã commit, semantic contract và `delta deck`. Không viết lại toàn bộ deck nếu delta chỉ cần sửa cục bộ; giữ mạch nguồn và mọi yêu cầu RevealJS trong `AGENTS.md`.
2. **Fan-out chỉ đọc.** Chạy song song reader kiểm độ phủ nguồn/ghi chú, reader kiểm toán–shape–triển khai và reviewer kiểm storyboard/mạch 5–7 phần. Fan-in thành đặc tả sửa theo `data-slide-id`, trang lân cận và ranh giới phần.
3. **Checkpoint B1.** Codex duyệt delta: lý do, nguồn, tác động timing 100 phút lõi + 20 phút mở rộng, bài tập 50 phút tách riêng, và các trang cần tái rà. Không đưa chiều sâu chỉ phù hợp tài liệu tự học lên slide.
4. **Writer tuần tự.** Một DeepSeek writer sửa HTML/SVG/planning trong phạm vi đã khóa. Codex kiểm và áp dụng diff. Dùng đủ bốn planning file; mọi sai khác với slide nguồn và mọi chủ đề không đưa lên deck phải có quyết định trong `review-log.md`/`note-for-author.md`.
5. **Fan-out/fan-in review.** Kiểm định storyboard, rồi chạy song song năm vai bắt buộc của `AGENTS.md`. Một writer sửa tuần tự. Rà lại chính xác và mạch đúng phạm vi sau sửa; nếu đổi mở bài, kết bài hay luận điểm trung tâm, rà lại toàn deck.
6. **Checkpoint B2 — Biên tập cuối và Reveal QA.** Đọc toàn bộ nội dung hiển thị và mọi `<aside class="notes">`, chạy lượt `$no-ai-slop` cuối rồi tự kiểm theo `no-ai-slop/eval.md`. Xóa dấu vết soạn bằng AI, lời dẫn rỗng, câu hỏi tu từ, khẩu hiệu, kết luận lặp, nhịp câu máy móc, siêu bình luận và nhãn quy trình. Ghi chú diễn giả chỉ giữ mạch nói, giả thiết, lỗi dễ mắc, chuyển ý tự nhiên, đáp án hoặc nguồn cần cho giảng dạy; bỏ các chỉ dẫn kiểu “câu nối”, “trang này hình thức hóa”, “người soạn cần”, “mục này phục vụ” và chuyển hướng dẫn triển khai còn cần sang `note-for-author.md`. Không xóa nội dung kỹ thuật hoặc nguồn chỉ để làm văn bản ngắn hơn. Sau lượt này, xác nhận mỗi `data-slide-id` duy nhất, 5–7 `<section>` ngoài gồm mở đầu/kết luận trừ ngoại lệ đã ghi, cấu hình Reveal bắt buộc, thư viện cục bộ, ghi chú diễn giả, chân trang, đường dẫn tương đối, SVG truy cập được và không có raster chưa duyệt. Chạy server từ gốc kho:

   ```bash
   python3 -m reloadserver 8765
   ```

   Kiểm deck và viewer tại cổng 8765 bằng bàn phím, màn hình rộng/hẹp và bản in; render mọi công thức bằng KaTeX với chế độ nghiêm ngặt phù hợp. Rà riêng toàn bộ `h1`, `h2`, `h3` để loại tiêu đề pha tiếng Anh trái quy ước. Dùng Codex Slides để rà trực quan và xác minh đúng phiên bản hiển thị; nếu công cụ không khả dụng, ghi rõ giới hạn, vẫn hoàn tất QA RevealJS cục bộ và không tuyên bố đã dùng Codex Slides.
7. **Checkpoint B3 — Git.** Chỉ khi QA PASS, kiểm status/diff, stage đúng HTML/SVG/bốn planning file/index và sửa dùng chung thực sự liên quan. Commit dạng `feat(lecture-NN): add TEN_BAI slide deck` hoặc `fix(lecture-NN): revise TEN_BAI slide deck`, trong đó `TEN_BAI` được suy ra từ nguồn, rồi `git push origin main`. Nếu lỗi, giữ commit cục bộ và báo nguyên văn; không force/rebase.

## Biên tập và điều kiện dừng

Dùng `$no-ai-slop` cho nội dung hiển thị, ghi chú diễn giả và lecture note ở cả lượt sửa nội dung lẫn cổng kiểm định bản cuối; tự kiểm trực tiếp theo `no-ai-slop/eval.md` và ghi phạm vi thay đổi vào `review-log.md`, không thêm mục “What changed” vào sản phẩm công khai. Xóa dấu vết AI, chú giải quy trình và hướng dẫn cho diễn giả hoặc người viết khỏi lecture note, mặt slide và ghi chú diễn giả; chuyển phần nội bộ còn cần sang `note-for-author.md`. Dùng `$quill` để rà dàn ý, trật tự khái niệm, thuật ngữ, ký hiệu và tính liên tục; không tạo `quill.json`. Viết thuần Việt theo `AGENTS.md`, không thêm benchmark, ví dụ, mệnh đề hoặc nguồn không có căn cứ.

Chỉ kết thúc goal khi cả hai commit riêng của buổi — ghi chú trước, deck sau — đã được đẩy lên `origin/main`, index trỏ đúng sản phẩm đã kiểm định, bốn planning file phản ánh trạng thái cuối và không còn lỗi bắt buộc. Báo cáo bàn giao ngắn gồm: tệp sản phẩm, URL cục bộ, nguồn/dải trang, bản đồ chủ đề và phần bổ sung đã duyệt, semantic delta đã áp dụng, SVG, QA đã chạy, metadata các worker được chấp nhận, hai commit hash/push, sai khác có chủ ý và giới hạn còn lại.
