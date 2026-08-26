# Quy trình xây dựng trang chiếu Học sâu bằng RevealJS

## Phạm vi

Tệp này áp dụng cho mọi yêu cầu chọn tài liệu trong `source-materials/` và xây dựng trang chiếu RevealJS cho học phần **Học sâu**, học kỳ 1 năm học 2026–2027.

Nguồn có thể gồm slide, textbook, chương sách, paper, ghi chú, hình, dữ liệu hoặc code do người dùng chép vào:

- `source-materials/slides/`;
- `source-materials/textbooks/`;
- `source-materials/papers/`;
- `source-materials/resources/`.

Nếu tài liệu được đặt ở vị trí khác trong kho, điều phối viên vẫn phải kiểm kê và dùng đúng tệp người dùng chỉ định. Không tự chọn bài thay người dùng.

Mỗi yêu cầu phải tạo hoặc cập nhật:

- `2627-1/lecture-NN-<ten-bai>.html`;
- các hình SVG trong `2627-1/img/lec-NN/`;
- bốn tệp quy trình trong `2627-1/planning/lec-NN/`;
- mục tương ứng trong `2627-1/index.html` sau khi bài hoàn thành.

Bốn tệp quy trình gồm:

- `outline.md`;
- `storyboard.md`;
- `review-log.md`;
- `note-for-author.md`.

`NN` lấy theo số bài và luôn có hai chữ số. Ví dụ, bài 1 dùng `lecture-01-<ten-bai>.html`. Nếu số bài, tên bài hoặc ranh giới giữa nhiều tài liệu nguồn không suy ra được chắc chắn, phải hỏi người dùng trước khi soạn.

Điều phối viên phải dùng nhiều tác tử theo quy trình dưới đây. Không giao toàn bộ việc lập kế hoạch, phân tích nguồn, soạn, phản biện và chỉnh sửa cho một tác tử.

## Đối tượng và thời lượng

- Đối tượng mặc định là sinh viên đại học đã học đại số tuyến tính, giải tích, xác suất, lập trình Python và học máy nhập môn.
- Mỗi buổi gồm hai tiết lý thuyết 50 phút và một tiết bài tập 50 phút.
- Mỗi deck phải có đủ nội dung cho 120 phút trình chiếu, không tính tiết bài tập. Storyboard tổ chức tuyến lõi 100 phút và tuyến mở rộng/có thể cắt 20 phút.
- Tiết bài tập 50 phút được thiết kế và ghi riêng, không cộng vào timing 120 phút của deck.
- Chỉ chuyển hoặc chuẩn bị code demo khi nguồn có nội dung tương ứng hoặc người dùng yêu cầu. Không tự tạo notebook, pipeline huấn luyện hoặc thí nghiệm ngoài phạm vi nguồn.
- Nếu nội dung nguồn không thể dạy rõ trong tuyến lõi 100 phút, tác tử lập kế hoạch phải đề xuất gộp, đưa phần phù hợp sang tuyến mở rộng 20 phút hoặc tách thành nhiều bài. Không giải quyết quá tải bằng cách thu nhỏ chữ.

## Ánh xạ nguồn theo buổi

- Trước khi lập kế hoạch cho một deck, phải đọc đầy đủ mục của đúng buổi trong `source.md`.
- Khi người dùng yêu cầu một trong 13 buổi đã ánh xạ, xem các tệp và dải trang trong mục đó là nguồn đã được chọn; không hỏi lại tên tệp.
- DOCX `source-materials/resources/UET_Đề cương học phần_UET.AI3056_Học sâu_7460108.01.24.2506.docx` là chuẩn cao nhất cho số buổi, tên và chủ đề, LLO, phạm vi và ranh giới giữa các buổi. Truy nguyên theo `III.2 → Buổi N → tên trường`; không dựa vào số trang DOCX.
- Trong phạm vi mà DOCX đã khóa cho từng buổi, nguồn ưu tiên về nội dung và trình tự là các slide và dải trang trong `source-materials/slides/` được `source.md` chỉ định. Bước soạn đầu tiên phải Việt hóa đúng các trang đó và giữ mạch chính của slide.
- Bỏ nội dung slide nằm ngoài phạm vi đề cương. Nếu đề cương yêu cầu nội dung mà slide thiếu, ghi rõ phần thiếu và hỏi người dùng cung cấp hoặc duyệt nguồn; không đổi phạm vi để khớp nguồn hiện có.
- Chỉ sau bản chuyển ban đầu mới đánh giá chỗ cần bổ sung, chỉnh sửa, gộp, tách hoặc kết hợp với `source-materials/textbooks/hocsau_draft.pdf`. GT chỉ dùng để khôi phục tiên quyết, kiểm chứng công thức, shape, giả thiết và làm luồng dễ hiểu; không tự thay mạch khi slide đã đủ.
- Mọi sai khác so với slide nguồn, kể cả nội dung lấy từ GT, phải có lý do và được ghi trong `review-log.md`.
- Người dùng đã duyệt 13 PDF bổ sung cho buổi 06, 13 và 14; danh mục, vai trò và dải trang nằm trong `source.md`. Khi làm ba buổi này, phải đọc đúng các dải đã duyệt và không hỏi lại nguồn.
- Chỉ dừng hỏi người dùng cho buổi 06, 13 hoặc 14 nếu tệp đã duyệt bị mất, hỏng, không đọc được hoặc cần dùng nội dung ngoài dải đã duyệt. Không tự nâng GT thành nguồn chính để thay một tệp bổ sung bị thiếu.
- Chỉ dùng các dải trang đã ánh xạ cho buổi. Muốn dùng trang khác phải nêu lý do, kiểm tra không làm đổi phạm vi và ghi quyết định trong `review-log.md`.
- Khi slide và GT xung đột, giữ phạm vi của đề cương, ghi cả hai bằng chứng và quyết định xử lý trong `review-log.md`. Khi nguồn thiếu, không tự lấp bằng kiến thức nhớ lại hoặc nguồn web chưa được người dùng chọn.
- Chỉ xây dựng deck cho các buổi 01–08 và 10–14. Không xây dựng deck 09 (Ôn tập và kiểm tra giữa kỳ) hoặc 15 (Tổng kết), không đánh số lại và không dùng hai số này cho chủ đề khác.
- Không dùng `lec12_detection_intro.pdf`, `lec13_detection.pdf`, `lec18_diffusion.pdf`, `lec19_diffusion_editing.pdf` hoặc `lec20_diffusion_systems.pdf` nếu người dùng chưa chỉ định hoặc duyệt rõ cho buổi đang làm. Nếu được duyệt, phải cập nhật `source.md` trước khi soạn.
- Giữ dấu vết hai lỗi của đề cương: buổi 07 lặp mã `LLO3`; bảng đánh giá đặt giữa kỳ ở tuần 8 nhưng nội dung chi tiết đặt ôn tập và kiểm tra ở buổi 09. Không tự sửa hoặc hòa giải hai điểm này.

## Ngôn ngữ và biên tập

- Viết thuần Việt. Chỉ giữ tiếng Anh cho tên riêng, tên phần mềm, API, ký hiệu chuẩn, tên kiến trúc hoặc thuật ngữ chưa có cách dịch ổn định.
- Tiêu đề trang chiếu không được pha tiếng Anh khi đã có cách diễn đạt tiếng Việt rõ và ổn định. Chỉ giữ tiếng Anh trong tiêu đề khi đó là tên riêng, tên mô hình hoặc kiến trúc, API, ký hiệu chuẩn hay viết tắt thông dụng như MLP, CNN, ReLU, LSTM và Transformer.
- Không viết kiểu “Forward pass phải giữ đúng shape”. Viết “Lan truyền xuôi phải giữ đúng kích thước tensor” hoặc một cách diễn đạt thuần Việt tương đương. Thuật ngữ tiếng Anh cần thiết có thể được giới thiệu trong thân bài hoặc ghi chú ở lần xuất hiện đầu, không dùng để tạo tiêu đề pha ngôn ngữ.
- Khi dùng viết tắt lần đầu, viết đầy đủ bằng tiếng Việt rồi đặt dạng viết tắt trong ngoặc.
- Viết ngắn, trực tiếp và học thuật. Dùng câu ngắn, động từ rõ và thuật ngữ nhất quán.
- Không dùng câu hỏi tu từ, câu cảm thán, khẩu hiệu, lời ca tụng hoặc cách diễn đạt quảng bá.
- Không thêm nhận định, số liệu, benchmark, nguồn hoặc ví dụ thực nghiệm không có căn cứ.
- Trong mọi tệp Markdown, chỉ dùng `$...$` cho công thức nội dòng và `$$...$$` cho công thức khối.
- Dùng `$no-ai-slop` để biên tập nội dung hiển thị và ghi chú diễn giả. Tự kiểm bản cuối theo `no-ai-slop/eval.md`.
- Dùng `$quill` để rà dàn ý, thứ tự khái niệm, thuật ngữ, ký hiệu và tính liên tục giữa các phần. Không khởi tạo `quill.json`.
- Mọi chỉ dẫn dành cho người soạn, tuyến cắt, trạng thái kiểm chứng, quyết định nội bộ và đáp án chi tiết phải ghi trong `note-for-author.md`, không đưa lên mặt trang chiếu hoặc ghi chú diễn giả.

## Thứ tự ưu tiên nguồn

Khi có xung đột, tuân theo thứ tự sau:

1. Chỉ dẫn cụ thể của người dùng cho bài đang làm.
2. DOCX đề cương về số buổi, tên và chủ đề, LLO, phạm vi và ranh giới giữa các buổi.
3. Slide và dải trang được ánh xạ trong `source.md` về nội dung và trình tự bên trong phạm vi buổi.
4. `source-materials/textbooks/hocsau_draft.pdf`, paper, code và tài sản bổ sung do người dùng cung cấp.
5. `2627-1/lecture-template.html` và `2627-1/lecture-style.css` về giao diện và nền kỹ thuật.
6. Các quy ước trong tệp này.

DOCX quyết định phạm vi và ranh giới buổi. Trong phạm vi đó, slide nguồn quyết định mạch chính; GT và paper dùng để khôi phục tiên quyết, kiểm chứng công thức, làm rõ giả thiết hoặc sửa lỗi. Khi các nguồn mâu thuẫn, không âm thầm chọn một phía: ghi bằng chứng và quyết định trong `review-log.md`.

Giữ mạch, thứ tự và ý chính của nguồn. Chỉ gộp, tách, thêm, lược hoặc sắp xếp cục bộ khi cần sửa lỗi, giảm quá tải, khôi phục tiên quyết, hoàn thiện mạch học tập hoặc bảo đảm khả năng đọc. Mọi sai khác phải có lý do và truy nguyên nguồn.

## Tiếp nhận và kiểm kê

Sau khi người dùng chọn nguồn, điều phối viên phải:

- đọc đầy đủ tài liệu chính và kiểm tra các tài liệu liên quan trong `source-materials/`;
- bỏ qua `.DS_Store`, tệp có tiền tố `._` và tệp tạm có tiền tố `~$`;
- xác định số bài, tên bài, mục tiêu, kiến thức tiên quyết, phạm vi, số trang và tài sản được dùng;
- đọc `2627-1/lecture-template.html`, `lecture-style.css` và `index.html` trước khi lập kế hoạch;
- kiểm kê hình, biểu đồ, sơ đồ, bảng, công thức, giả mã, code và kết quả thực nghiệm phải chuyển;
- xác định phần nào là nội dung, bố cục, ghi chú, tài liệu tham khảo, tài sản trực quan hoặc phụ lục;
- đối chiếu slide với textbook/paper theo chương, mục, định lý, thuật toán hoặc số trang;
- xác định môi trường phần mềm, thư viện, phiên bản và dữ liệu nếu nguồn có code hoặc kết quả thực nghiệm;
- chỉ hỏi người dùng về thông tin không thể suy ra từ kho và có thể làm thay đổi đáng kể kết quả.

Nếu người dùng chưa chọn nguồn, dừng sau bước kiểm kê danh mục và yêu cầu tên tệp. Không tự lập một syllabus hoặc chọn chương thay người dùng.

## Tổ chức tệp

Mỗi bài dùng cấu trúc sau:

```text
2627-1/
├── lecture-NN-<ten-bai>.html
├── img/
│   └── lec-NN/
│       └── *.svg
└── planning/
    └── lec-NN/
        ├── outline.md
        ├── storyboard.md
        ├── review-log.md
        └── note-for-author.md
```

- `outline.md` chứa mục tiêu, dàn ý, ánh xạ nguồn và bảng thuật ngữ hoặc ký hiệu.
- `storyboard.md` chứa bản đồ hành trình khái niệm và một mục cho từng trang chiếu.
- `review-log.md` chứa báo cáo rà soát, quyết định chỉnh sửa, sai khác so với nguồn và ngoại lệ đã duyệt.
- `note-for-author.md` chứa tuyến giảng, phương án cắt, đáp án, chỉ dẫn triển khai, điểm cần kiểm chứng và lưu ý chỉ dành cho người soạn.
- HTML nằm trực tiếp trong `2627-1/`. Không đặt HTML trong thư mục planning hoặc img.
- Mọi đường dẫn trong HTML phải tương đối và hợp lệ khi máy chủ được mở tại thư mục gốc của kho.

## Mẫu RevealJS bắt buộc

- Dùng `2627-1/lecture-template.html` làm nền. Chỉ kế thừa cấu trúc, giao diện và cấu hình kỹ thuật; phải thay toàn bộ placeholder, nội dung và metadata.
- Dùng `2627-1/lecture-style.css`, màu, phông chữ, khoảng cách, thẻ, lưới và chân trang hiện có. Không tạo hệ giao diện mới cho từng bài.
- Tham khảo cách tổ chức bố cục trong kho `https://github.com/uet-iai-course/machine-learning`, ưu tiên `SLIDE_STYLE_GUIDE.md` và các tệp `2526-2/lecture-*.html`. Không sao chép nội dung, tài sản hoặc CSS từ kho tham khảo.
- Giữ `lang="vi"`, khung `1280 × 720`, `controlsLayout: "edges"`, `slideNumber: true`, `hashOneBasedIndex: true` và `hash: true`.
- Dùng các thư viện cục bộ trong `2627-1/`: RevealJS, `RevealMath.KaTeX`, `RevealNotes` và `RevealHighlight`.
- Dùng `<section>` ngoài cho từng phần và `<section>` trong cho từng trang chiếu.
- Mỗi trang có `data-slide-id` duy nhất. Mã chỉ xuất hiện trong HTML và các tệp planning; không hiển thị trên mặt trang hoặc trong ghi chú diễn giả.
- Đặt chân trang ở cuối `.slides` và cập nhật đúng tên học phần, học kỳ và số bài.
- Không phụ thuộc mạng cho các thành phần cốt lõi.
- Không sửa RevealJS, plugin, KaTeX hoặc CSS dùng chung nếu có thể giải quyết trong tệp bài giảng.
- Nếu cần sửa `lecture-style.css`, phải kiểm tra các bài hiện có không bị hỏng.

## Chuyển và vẽ lại hình

- Mọi sơ đồ, computational graph, kiến trúc mạng, đồ thị và hình kỹ thuật phải được vẽ lại thành SVG.
- Không trích ảnh raster từ PDF, PPTX hoặc textbook rồi nhúng vào trang chiếu.
- Lưu SVG tại `2627-1/img/lec-NN/`. SVG nhỏ dùng một lần có thể đặt nội dòng khi giúp bố cục hoặc khả năng tiếp cận rõ hơn.
- Giữ đúng quan hệ, tỷ lệ có ý nghĩa, nhãn, chiều mũi tên, chú giải và dữ liệu của hình nguồn. Không thay đổi dữ liệu để làm hình đẹp hơn.
- Đồ thị phải có tên trục, đơn vị, chú giải, phép tổng hợp và nguồn khi các thành phần này có trong nguồn hoặc cần để hiểu hình.
- Mỗi SVG phải có `role="img"`, `title`, `desc` hoặc mô tả thay thế cụ thể. Không dùng màu làm tín hiệu duy nhất.
- Công thức, bảng, tensor shape và code phải dựng bằng KaTeX, HTML hoặc khối code; không chuyển chúng thành ảnh.
- Không dùng ảnh sinh bởi AI thay cho dữ liệu, mẫu huấn luyện, kết quả thực nghiệm hoặc hình mô tả bằng chứng.
- Ảnh chụp, mẫu dữ liệu, logo hoặc screenshot chỉ được giữ ở dạng raster khi không thể tái tạo trung thực bằng SVG và người dùng đã duyệt ngoại lệ. Ghi đường dẫn, lý do, nguồn và phạm vi dùng trong `review-log.md`.
- Nếu ngoại lệ chưa được duyệt, dừng phần bị ảnh hưởng và hỏi người dùng. Không âm thầm giữ raster hoặc bỏ nội dung.

## Cấu trúc học tập

Mỗi khái niệm trọng tâm đi theo chu trình:

**vấn đề → trực giác → ví dụ → hình thức/tính toán → triển khai/ứng dụng → kiểm tra**

- **Vấn đề:** nêu bài toán dự đoán, biểu diễn, tối ưu hoặc sinh dữ liệu cần giải quyết.
- **Trực giác:** dùng dữ liệu, đặc trưng, lớp mạng, tín hiệu gradient hoặc luồng thông tin để chuẩn bị cho ký hiệu.
- **Ví dụ:** dùng một tensor, mạng nhỏ, phép tính hoặc thí nghiệm có thể kiểm tra.
- **Hình thức/tính toán:** nêu hàm, công thức, computational graph, thuật toán, đầu vào, đầu ra và giả thiết.
- **Triển khai/ứng dụng:** nối công thức với forward pass, backward pass, training loop, inference hoặc một bài toán Học sâu.
- **Kiểm tra:** yêu cầu người học tính shape, số tham số, gradient, receptive field, loss, so sánh thiết kế hoặc phản biện kết luận.

Không bắt buộc sáu bước là sáu trang riêng. Có thể gộp khi mỗi trang vẫn có một luận điểm trung tâm. Với khái niệm phụ, dùng chu trình rút gọn nếu storyboard ghi rõ lý do. Không đặt công thức hoặc thuật toán trước khi giới thiệu đủ miền, ký hiệu và trực giác quyết định.

Storyboard phải chỉ ra cho từng cụm:

- mã trang thực hiện từng bước;
- kiến thức đầu vào và sản phẩm học tập;
- tensor, dữ kiện hoặc ký hiệu được truyền từ ví dụ sang công thức và code;
- bước được gộp hoặc ghi `không áp dụng`, kèm lý do;
- câu nối giữa các bước;
- thời lượng dự kiến, tổng thời lượng deck 120 phút, tuyến lõi 100 phút và tuyến mở rộng/có thể cắt 20 phút;
- bài tập 50 phút tách khỏi timing 120 phút của deck;
- tuyến linh hoạt và thao tác điều hướng nếu có trang có thể cắt.

## Tiêu chuẩn nội dung Học sâu

- Phân biệt rõ dữ liệu, nhãn, đặc trưng, tham số, siêu tham số, mô hình, hàm mất mát, bộ tối ưu, metric và dự đoán.
- Nêu miền, kiểu dữ liệu, shape, thứ tự trục, batch dimension, quy ước broadcasting và device trước khi dùng tensor.
- Dùng ký hiệu nhất quán từ ví dụ sang công thức, computational graph, giả mã, code và bài tập.
- Tách rõ forward pass, loss construction, backward pass, optimizer step, trạng thái mô hình khi huấn luyện và inference.
- Khi dùng đạo hàm, kiểm tra biến lấy đạo hàm, shape của Jacobian/gradient, chiều truyền, dấu, hệ số trung bình hoặc tổng và đại lượng được giữ cố định.
- Với softmax, log-sum-exp, cross-entropy và normalization, nêu đúng trục tính, epsilon và biện pháp ổn định số.
- Với mạng nhiều lớp, nêu activation, bias, quy tắc khởi tạo, số tham số, computational graph và điều kiện dùng shared parameters.
- Với convolution, kiểm tra channel order, kernel, stride, padding, dilation, output shape, receptive field và parameter sharing.
- Với recurrent network, LSTM hoặc GRU, phân biệt hidden state, cell state, sequence length, masking, teacher forcing, backpropagation through time và trạng thái khởi tạo khi phù hợp.
- Với attention hoặc Transformer, nêu shape của query, key, value, head dimension, trục softmax, hệ số scale, mask, residual path và quy ước normalization.
- Với autoencoder, variational autoencoder, GAN hoặc diffusion, nêu đúng objective, biến ngẫu nhiên, phân phối, sampling path, approximation và phạm vi kết luận khi các khái niệm xuất hiện.
- Với thuật toán huấn luyện, nêu đầu vào, đầu ra, giả mã, tiêu chuẩn dừng, optimizer state, learning-rate schedule, regularization, model mode và chi phí chính khi nguồn có hoặc khi thiếu sẽ gây hiểu sai.
- Phân biệt training, validation và test; phát hiện data leakage, tuning trên test, preprocessing không nhất quán và metric không phù hợp.
- Không tuyên bố hội tụ, tối ưu toàn cục, khả năng khái quát, tính bất biến, độ bền hoặc ưu thế benchmark nếu thiếu giả thiết và giao thức quyết định kết luận.
- Tự tính lại ví dụ số, shape tensor, số tham số, receptive field, gradient, loss, xác suất, FLOPs ước lượng và kích thước bộ nhớ quan trọng.
- Với benchmark, ghi dataset split, preprocessing, augmentation, metric, seed, số lần chạy, uncertainty, compute budget và phiên bản implementation khi nguồn cung cấp hoặc khi thiếu sẽ làm kết luận mơ hồ.
- Giữ nguồn truy nguyên theo số trang, slide, chương, mục, hình, bảng hoặc thuật toán. Chỉ bổ sung nguồn ngoài khi cần sửa hoặc kiểm chứng mệnh đề và phải ghi nguồn cụ thể.

## Tiêu chuẩn code và trình diễn

- Không tạo code demo nếu nguồn không có code hoặc người dùng không yêu cầu.
- Khi chuyển code, giữ API và hành vi của nguồn; chỉ sửa lỗi cần thiết và ghi quyết định.
- Code trên slide phải ngắn, tập trung vào một cơ chế và đủ lớn để đọc trên máy chiếu.
- Chuyển chi tiết boilerplate, tải dữ liệu và cấu hình dài sang ghi chú hoặc tệp demo riêng khi được yêu cầu.
- Mọi đoạn code phải nêu shape đầu vào/đầu ra, chế độ train/eval, device và nguồn ngẫu nhiên khi chúng ảnh hưởng kết quả.
- Không chạy huấn luyện dài hoặc tải dataset lớn nếu người dùng chưa yêu cầu và chưa cung cấp phạm vi tài nguyên.
- Kết quả demo phải được phân biệt với số liệu trong paper hoặc textbook; không trình bày một lần chạy như bằng chứng tổng quát.

## Tiêu chuẩn trang chiếu và ghi chú

- Mỗi trang chiếu có một luận điểm trung tâm. Tách phép suy diễn, computational graph, giả mã hoặc bảng quá dài thay vì thu nhỏ chữ.
- Tiêu đề ngắn, gọi đúng khái niệm và tuân thủ quy tắc thuần Việt. Không đặt tiêu đề dưới dạng “Tại sao...?”, “Vì sao...?” hoặc câu kể tiến trình. Trước khi bàn giao, rà riêng toàn bộ nội dung trong `h1`, `h2` và `h3` để loại các cụm tiếng Anh không thuộc nhóm ngoại lệ đã cho phép.
- Văn bản thân bài nên từ `0.75em` trở lên. Chỉ dùng dưới `0.65em` cho chú thích ngắn đã được tác tử góc nhìn sinh viên xác nhận đọc được.
- Mỗi gạch đầu dòng không quá hai dòng ở khung 16:9. Chuyển diễn giải dài sang ghi chú diễn giả.
- Công thức, tensor shape và code trung tâm phải đủ lớn, có khoảng trắng và không bị cắt.
- Mọi lời mời tương tác trên mặt trang dùng nhãn **“Câu hỏi:”**.
- Không hiển thị mã nội bộ, nhãn quy trình, phân tuyến, trạng thái kiểm chứng hoặc thời lượng trên mặt trang hay trong ghi chú diễn giả.
- Mỗi trang nội dung có `<aside class="notes">` khi cần giải thích giả thiết, shape, công thức, lỗi dễ mắc, chuyển ý, đáp án hoặc nguồn.
- Ghi chú diễn giả là mạch nói ngắn bằng tiếng Việt; không chỉ chứa metadata và không lặp nguyên văn mặt trang.
- Bộ trang chiếu phải dùng được bằng bàn phím, có tương phản đủ và không dùng màu làm tín hiệu duy nhất.

## Quy trình đa tác tử

### 1. Điều phối và lập kế hoạch

Điều phối viên kiểm kê nguồn, xác nhận đầu ra và mở dự án bền vững trong Codex Slides. Giao một tác tử lập kế hoạch riêng trước khi phân tích chi tiết hoặc sửa tệp.

Tác tử lập kế hoạch:

- xác định mục tiêu, phạm vi, đối tượng, thời lượng và tiêu chí hoàn thành;
- lập danh mục khái niệm trọng tâm và bản đồ chu trình học tập;
- chia việc thành kiểm kê, ánh xạ, soạn, rà soát, chỉnh sửa và kiểm định;
- xác định việc tuần tự, việc có thể chạy song song, đầu vào và đầu ra của từng tác tử;
- nêu rủi ro về thiếu nguồn, hình khó vẽ, ký hiệu, shape, quá tải, tràn trang, code và compute;
- không sửa tệp trang chiếu.

Điều phối viên phải kiểm tra và chấp nhận kế hoạch trước khi triển khai.

### 2. Phân tích nguồn và ánh xạ

Giao một tác tử chỉ đọc:

- lập bảng ánh xạ từng trang nguồn, chương sách và tài sản sang trang đích;
- ghi quyết định `giữ`, `sửa`, `gộp`, `tách`, `thêm` hoặc `bỏ`;
- trích mục tiêu, định nghĩa, công thức, thuật toán, ví dụ, bài tập, code, số liệu và nguồn;
- kiểm kê từng hình và cách vẽ lại thành SVG;
- chỉ ra thiếu giả thiết, sai shape, sai gradient, sai số, mâu thuẫn, ký hiệu không nhất quán và đoạn khó đọc;
- bàn giao đặc tả cho tác tử soạn, không sửa tệp.

### 3. Soạn và triển khai

Giao một tác tử soạn duy nhất:

- tạo bốn tệp planning, HTML và SVG theo đặc tả;
- dịch và biên tập bằng tiếng Việt theo `$no-ai-slop`;
- dùng `$quill` để kiểm tra mạch phần, chuyển ý, thuật ngữ và ký hiệu;
- giữ thứ tự nguồn trừ thay đổi đã được phê duyệt;
- thêm ghi chú diễn giả và nguồn;
- đưa mọi chỉ dẫn người soạn vào `note-for-author.md`;
- không sửa thư viện hoặc CSS dùng chung nếu có thể giải quyết cục bộ.

### 4. Kiểm định storyboard

Giao một tác tử chỉ đọc rà từng trang và từng cụm khái niệm:

- kiểm tra lý do tồn tại của từng trang có cụ thể và kiểm chứng được;
- kiểm tra trang tạo một bước tiến trong lập luận, tính toán, triển khai hoặc luyện tập;
- kiểm tra chu trình sáu bước đúng thứ tự và nối được tensor/dữ kiện từ ví dụ sang hình thức và code;
- phát hiện trang trùng ý, trang trang trí, trang quá tải và khoảng trống cần bổ sung;
- kiểm tra thời lượng 120 phút, tiên quyết và quan hệ trước–sau;
- đề xuất quyết định, bằng chứng và tác động đến trang lân cận;
- không sửa tệp.

Sau thay đổi số lượng hoặc thứ tự, phải rà lại trang bị ảnh hưởng và hai trang lân cận mỗi phía.

### 5. Bốn tác tử rà soát độc lập

Sau bản nháp đầu, chạy song song bốn tác tử chỉ đọc. Mỗi báo cáo dùng các trường `mức độ`, `trang chiếu`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.

- **Góc nhìn sinh viên:** kiểm tra tiên quyết, tải nhận thức, nhịp giảng, khả năng đọc, ví dụ, chuyển ý, câu hỏi kiểm tra và khả năng tự học.
- **Chuyên gia Học sâu:** kiểm tra độ bao phủ, chiều sâu, thuật ngữ, mạch học thuật, liên hệ với học máy và sự phù hợp với 120 phút.
- **Độ chính xác toán học, thuật toán và triển khai:** kiểm tra định nghĩa, giả thiết, shape, broadcasting, gradient, loss, numerical stability, giả mã, kết quả số, độ phức tạp, model mode và training loop.
- **Phản biện học thuật và giảng dạy Học sâu:** đóng vai chuyên gia nghiên cứu và giảng dạy để phản biện công thức, thuật toán và trình tự kiến thức; nêu rõ khi một công thức đúng riêng lẻ nhưng đặt sai thứ tự, thiếu trực giác, thiếu ví dụ, thiếu tiên quyết hoặc không nối được sang triển khai.

Mức độ gồm `chặn bàn giao`, `nghiêm trọng`, `trung bình`, `nhẹ`. Mọi lỗi `chặn bàn giao` và `nghiêm trọng` phải được xử lý.

### 6. Chỉnh sửa

Giao một tác tử chỉnh sửa riêng sau khi bốn báo cáo hoàn tất:

- hợp nhất vấn đề trùng lặp và ưu tiên tính đúng, khả năng học, khả năng đọc;
- sửa tuần tự HTML, SVG và các tệp planning;
- ghi quyết định đối với đề xuất không áp dụng;
- không thay đổi mạch nguồn nếu lỗi có thể sửa cục bộ;
- yêu cầu rà lại độ chính xác cho mọi phần toán, shape, gradient, thuật toán hoặc code đã đổi đáng kể.

Các tác tử sửa tệp không được chạy song song.

### 7. Kiểm định cuối

Điều phối viên hoặc tác tử kiểm thử riêng phải:

- đối chiếu số trang nguồn, bảng ánh xạ, `data-slide-id` và storyboard;
- kiểm tra HTML, cấu trúc `<section>`, KaTeX, plugin, ghi chú, đường dẫn, SVG và liên kết;
- dựng toàn bộ công thức bằng KaTeX với `throwOnError: true`; dùng strict mode khi có thể;
- tìm tham chiếu raster; chỉ chấp nhận ngoại lệ đã được người dùng duyệt và ghi trong nhật ký;
- kiểm tra không có tài nguyên hỏng hoặc phụ thuộc mạng cốt lõi;
- tự tính lại shape, tham số, gradient, loss và ví dụ số quan trọng;
- chạy `python3 -m reloadserver 8765` tại thư mục gốc; cổng là đối số vị trí, không dùng `--port`;
- mở `http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html` và duyệt mọi trang ngang, dọc;
- kiểm tra tràn chữ, chữ nhỏ, chồng lấn, công thức, code, hình, tương phản và bàn phím ở khung 16:9 và một màn hình hẹp;
- xuất danh sách toàn bộ tiêu đề `h1`, `h2`, `h3` và kiểm tra thủ công từng tiêu đề không pha tiếng Anh, trừ tên gọi, ký hiệu chuẩn hoặc viết tắt thông dụng đã được phép;
- dùng Codex Slides để rà trực quan sau cùng và xác minh Design Files khớp bản trong kho;
- chạy lại kiểm định sau mỗi sửa lỗi chặn bàn giao hoặc nghiêm trọng.

Nếu Codex Slides hoặc trình duyệt không khả dụng, phải báo rõ giới hạn, tiếp tục đầy đủ kiểm tra RevealJS cục bộ và không tuyên bố đã rà bằng công cụ không dùng được.

## Cập nhật `index.html`

- `2627-1/index.html` là danh mục riêng của học phần **Học sâu** cho học kỳ 1 năm học 2026–2027.
- Mỗi bài hoàn thành có một thẻ theo thứ tự số bài, gồm tên bài, mô tả một câu và liên kết duy nhất đến tệp HTML của bài giảng.
- Không đặt liên kết đến `outline.md`, `storyboard.md`, `review-log.md`, `note-for-author.md` hoặc thư mục `planning/` trên trang chỉ mục.
- Không thêm bài chưa hoàn thành hoặc liên kết đến tệp chưa tồn tại.
- Giữ giao diện trang chỉ mục trừ nội dung nhận diện học phần và danh sách bài.

## Tiêu chí hoàn thành

Chỉ bàn giao khi:

- bản RevealJS giữ đúng ý chính và mạch nguồn, mọi sai khác đều được ghi;
- nội dung chính bằng tiếng Việt, ngắn, trực tiếp và đã qua `$no-ai-slop`;
- bốn tệp planning nằm đúng `planning/lec-NN/`;
- mọi hình đã được vẽ lại thành SVG hoặc có ngoại lệ raster được duyệt;
- bốn báo cáo độc lập đã có và mọi lỗi bắt buộc đã được xử lý;
- công thức, shape, gradient, ví dụ số, giả mã, code và giả thiết đã được kiểm tra;
- bộ trang chiếu chạy tại cổng `8765`, không có lỗi tài nguyên hoặc hiển thị nghiêm trọng;
- `index.html` chỉ liên kết tới HTML của bài hoàn thành;
- nội dung trong kho khớp bản đã rà trong Codex Slides, hoặc giới hạn công cụ đã được ghi rõ.

Khi bàn giao, nêu ngắn gọn: tệp trang chiếu, URL cục bộ, tệp nguồn, hình đã vẽ lại, kiểm tra đã chạy, sai khác có chủ ý, ngoại lệ và giới hạn còn lại.
