# Data Anonymizer Tool

**Phiên bản:** 1.0  
**Tác giả:** Leonix

## Giới thiệu

Data Anonymizer Tool là một công cụ đơn giản được xây dựng bằng Python nhằm ẩn danh dữ liệu tên, email, sdt trong bảng `res_partner` của PostgreSQL bằng thuật toán mã hóa XOR. Công cụ này hoạt động độc lập, không phụ thuộc vào Odoo, cho phép bạn cập nhật dữ liệu nhạy cảm một cách nhanh chóng và bảo mật. 

Các bước dưới đây sẽ hướng dẫn chi tiết cách clone repository, cài đặt môi trường Python ảo, cấu hình kết nối cơ sở dữ liệu và chạy tool.

---

### 1. Clone Repository

1. Mở Command Prompt (hoặc Terminal).
2. Chạy lệnh sau để clone repository:
   ```bash
    git clone --branch anonymizer_script --single-branch https://github.com/leonixvn/TuNghia.git

### 2. Yêu cầu
1. Có python 3.8+
2. Có PostgreSQL và data mẫu của oDoo

### 3. Cài Đặt Các Phụ Thuộc
   ```bash
   pip install -r requirement.txt
### 4. Cấu Hình Kết Nối Database
1. Vào file anonymizer.py để chỉnh sửa theo cấu trúc sau:
DB_NAME = odoo
DB_USER = odoo
DB_PASSWORD = your_password_here
DB_HOST = localhost
DB_PORT = 5432
### 5. Chạy Tool
   ```bash
    python anonymizer.py
Nếu file chạy thành công thì sẽ có thông báo Dữ liệu đã được ẩn danh thành công
Nếu file chạy thất bại thì sẽ có thông báo Lỗi khi ẩn danh dữ liệu
