# Bài 06 — Học biểu diễn và Autoencoder

## Phạm vi và kết quả học tập

- Đối tượng: sinh viên đã học MLP, CNN, lan truyền ngược và quy trình chia dữ liệu.
- LLO11 (nguyên văn DOCX): trình bày được kiến trúc của một Autoencoder cơ bản, bao gồm bộ mã hóa, không gian ẩn và bộ giải mã. Việc tính kích thước tensor và mất mát tái tạo là sản phẩm luyện tập của bài, không phải một phần của LLO gốc.
- LLO12: nối học biểu diễn với tiền huấn luyện và học chuyển giao; phân biệt đóng băng với tinh chỉnh.
- Tuyến lõi 100 phút, tuyến mở rộng có thể cắt 20 phút, bài tập tách riêng 50 phút.
- Không có trình diễn code. Không đưa mô hình tự mã hóa biến phân, autoencoder che mặt, ViT hoặc khuếch tán vào bài.

## Mạch nội dung

1. Biểu diễn quyết định độ khó của tác vụ; học tự giám sát tạo mục tiêu từ dữ liệu chưa gán nhãn.
2. Autoencoder: $x^{(n)}\rightarrow z^{(n)}\rightarrow\hat x^{(n)}$; ví dụ MNIST xuyên suốt.
3. Tổng bình phương sai số (SSE), trung bình bình phương sai số (MSE), quy ước lấy trung bình và vòng huấn luyện.
4. Nghiệm đồng nhất, nút thắt, autoencoder có mã thấp chiều và giới hạn năng lực.
5. Ba cách ràng buộc: mã thấp chiều, mã thưa, khử nhiễu với mục tiêu sạch.
6. Bỏ bộ giải mã, tái sử dụng bộ mã hóa bằng đóng băng hoặc tinh chỉnh; giao thức kiểm định.
7. Giới hạn lấy mẫu: mã tùy ý có thể nằm ngoài vùng mã đã quan sát.
8. Mở rộng: biểu diễn và phép toán, quan hệ tuyến tính với PCA, đa tạp phi tuyến, kiểm định biểu diễn.

## Ký hiệu và hợp đồng tensor

| Ký hiệu | Miền/kích thước | Nghĩa |
|---|---|---|
| $X_{\mathrm{img}}$ | $[0,1]^{N\times1\times28\times28}$ | Lô ảnh MNIST sạch, trục NCHW: lô–kênh–cao–rộng |
| $X$ | $[0,1]^{N\times784}$ | Lô sạch được làm phẳng theo từng mẫu |
| $x^{(n)}$ | $[0,1]^{784}$ | Mẫu thứ $n$ của lô $X$ |
| $H_e,H_d$ | $\mathbb R^{N\times256}$ | Hoạt hóa ẩn của bộ mã hóa và bộ giải mã |
| $Z$ | $\mathbb R^{N\times d}$ | Lô mã tiềm ẩn, $Z=f_\theta(X)$ |
| $z^{(n)}$ | $\mathbb R^d$ | Mã tiềm ẩn của mẫu thứ $n$ |
| $\hat X$ | $(0,1)^{N\times784}$ | Lô tái tạo qua đầu ra sigmoid, $\hat X=g_\phi(Z)$ |
| $\widetilde X$ | $\mathbb R^{N\times784}$ | Đầu vào bị nhiễu; nguồn không khóa phép cắt miền, mục tiêu vẫn là $X$ sạch trong $[0,1]^{N\times784}$ |
| $D$ | $784$ | Số phần tử trên một ảnh đã làm phẳng |
| $\theta,\phi,\psi$ | tham số | Bộ mã hóa, bộ giải mã, bộ phân loại |
| $\theta^\star$ | tham số | Tham số bộ mã hóa sau tiền huấn luyện |
| $C$ | số nguyên dương | Số lớp của tác vụ đích; MNIST có $C=10$ |

Kiến trúc xuyên suốt là $784\to256\to d\to256\to784$. Quy ước MSE là $\|X-\hat X\|_F^2/(ND)$. Ví dụ thu nhỏ $D=4$ có SSE $0.18$ và MSE $0.045$; MNIST dùng $D=784$.

## Ánh xạ nguồn

| Nguồn đã duyệt | Trang PDF | Vai trò và trang đích |
|---|---:|---|
| `stanford-cs231n-2025-lecture13-generative-models.pdf` | 63–64 | Dữ liệu chưa gán nhãn, bộ mã hóa và biểu diễn: L06-00–04 |
| cùng tệp | 65–66 | Bộ giải mã, tái tạo và mất mát L2: L06-06–15 |
| cùng tệp | 67 | Thay bộ giải mã bằng bộ phân loại: L06-28–33 |
| cùng tệp | 68–70 | Giới hạn lấy mẫu mã tùy ý: L06-34–38 |
| `illinois-ece417-fa2023-lecture20-autoencoders.pdf` | 4–8 | Công thức cơ bản, nghiệm đồng nhất, giảm chiều, PCA, độ phức tạp: L06-06–20, L06-X02 |
| cùng tệp | 9–13 | Phân loại biến thể, mã thưa, top-$k$, đa tạp và mạng sâu: L06-21–27, L06-X03–X04 |
| cùng tệp | 14 | Không dùng; LSTM autoencoder nằm ngoài mạch và không cần cho LLO |
| `cmu-11785-s2021-representation-learning.pdf` | 1–6 | Biểu diễn và độ khó phép toán: L06-02–05, L06-X01 |
| cùng tệp | 7–13 | Ứng dụng và mong muốn về biểu diễn: L06-X05 |
| cùng tệp | 14–17 | Tính hữu ích phụ thuộc tác vụ, sai lệch và đánh giá: L06-05, L06-18–20, L06-32, L06-X05 |
| `cmu-11785-s2021-autoencoders.pdf` | 2–3 | Kiến trúc, tái tạo và cảnh báo mất mát đơn thuần: L06-06, L06-11, L06-16 |
| cùng tệp | 4–7 | Thiếu đầy đủ, thưa, khử nhiễu: L06-17, L06-21–27 |
| `lec01_intro.pdf` | 26–37 | Đối chiếu học tự giám sát và tiền huấn luyện; dùng phần phù hợp cho ghi chú L06-04 |
| `lec11_dense.pdf` | 3–10 | Nguồn nối về tiền huấn luyện và học chuyển giao; không phải nguồn cho kích thước MLP hoặc phép làm phẳng (kích thước/làm phẳng khóa từ GT 38–40 và quy ước của học phần) |
| `lec09_cnn_architectures.pdf` | 44–46 | Học chuyển giao, đóng băng và tinh chỉnh: L06-28–33 |
| `hocsau_draft.pdf` | 38–40 | MNIST và đầu vào 784 chiều: L06-07–08 |
| cùng tệp | 105–107 | Đối chiếu MLP/hàm kích hoạt: L06-09 |
| cùng tệp | 168–171 | Học tự giám sát và tiền huấn luyện: L06-04, L06-14 |

## Bản đồ chủ đề lecture note

| Note-topic-id | Nhãn | Vai trò và nguồn | Ánh xạ deck |
|---|---|---|---|
| L06-T01 | cốt lõi | Biểu diễn, dữ liệu chưa nhãn và mục tiêu tự giám sát; Stanford 63–64, CMU representation 1–6 | L06-00–05 |
| L06-T02 | cốt lõi | Bộ mã hóa–mã tiềm ẩn–bộ giải mã và hợp đồng MNIST $784\to256\to d\to256\to784$; Stanford 64–66, GT 38–40 | L06-06–10 |
| L06-T03 | cốt lõi | SSE, MSE, quy ước $1/(ND)$ và ví dụ $0{,}18/0{,}045$; Stanford 65–66 | L06-11–15 |
| L06-T04 | cốt lõi | Nghiệm đồng nhất, mã thấp chiều, năng lực và chọn $d$ bằng kiểm định; Illinois 4–8, CMU autoencoders 2–3 | L06-16–20 |
| L06-T05 | cốt lõi | Mã thấp chiều, mã thưa phạt mềm/top-$k$ cứng và khử nhiễu với đích sạch; Illinois 9–13, CMU autoencoders 4–7 | L06-21–27 |
| L06-T06 | cốt lõi | Tái sử dụng encoder: đóng băng, tinh chỉnh, gradient, chế độ mô-đun và giao thức dữ liệu; Stanford 67, `lec09` 44–46, `lec11` 3–10 | L06-28–33 |
| L06-T07 | cốt lõi | Mã do encoder tạo so với mã tùy ý và giới hạn lấy mẫu; Stanford 68–70 | L06-34–38 |
| L06-T08 | tổng hợp | Quy trình kiểm shape, mất mát, ràng buộc, tác vụ đích và vùng mã; tổng hợp nguồn đã duyệt | L06-37–38 |
| L06-T09 | bổ sung | Độ khó phép toán, quan hệ tuyến tính với PCA, đa tạp phi tuyến và đánh giá biểu diễn; CMU representation 1–17, Illinois 7 cho PCA và 10–13 cho mã thưa/đa tạp | L06-X01–X05 |
| L06-T10 | đọc thêm | VAE, masked autoencoder, ViT, diffusion, LSTM autoencoder và contractive autoencoder nằm ngoài phạm vi; chỉ ghi ranh giới, không triển khai | Không đưa lên slide |

Quyết định hợp nhất: giữ T01–T08 theo mạch Stanford và LLO; dùng Illinois/CMU để sửa thiếu sót về nghiệm đồng nhất, ràng buộc và đánh giá; T09 là phần có thể cắt; T10 chỉ khóa ranh giới. Không tự suy ra phân phối thuận tiện cho mã tiềm ẩn và không biến giới hạn lấy mẫu thành phần giới thiệu VAE.

## Cấu trúc mạch và tuyến

- Bảy mạch trình bày, mỗi mạch một `<section>` ngoài:
  1. Mở đầu: L06-00–05 (6 trang).
  2. Kiến trúc: L06-06–10 (5 trang).
  3. Mất mát: L06-11–15 (5 trang).
  4. Nút thắt: L06-16–20 (5 trang).
  5. Ba biến thể: L06-21–27 (7 trang).
  6. Tái sử dụng: L06-28–33 (6 trang).
  7. Giới hạn lấy mẫu, kiểm tra tổng hợp và tuyến mở rộng: L06-34–37, L06-X01–X05, L06-38 (10 trang).
- L06-38 là slide cuối toàn deck, sau X01–X05; kết luận không đặt trước phần mở rộng.
- Tuyến lõi 100 phút gồm L06-00–37 và L06-38 (3 phút). Tuyến mở rộng 20 phút gồm X01–X05. Bài tập 50 phút tách riêng.

## Tài sản trực quan

Mười lăm SVG vẽ lại tại `2627-1/img/lec-06/`: tuyến biểu diễn, tổng quan autoencoder, chuỗi kích thước MNIST, MLP, nghiệm đồng nhất, nút thắt, mã thưa, khử nhiễu, tái sử dụng, đóng băng–tinh chỉnh, lấy mẫu mã, vùng hỗ trợ bộ giải mã, PCA, đa tạp phi tuyến và biểu diễn chữ số. Không dùng raster.
