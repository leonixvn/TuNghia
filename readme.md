1 Cài Đặt Các Phụ Thuộc
-- pip install -r requirement.txt
2 Cấu Hình Kết Nối Database
 Mở file anonymizeranonymizer và chỉnh sửa theo thông tin kết nối của bạn:
[database]
DB_NAME = odoo
DB_USER = odoo
DB_PASSWORD = your_password_here
DB_HOST = localhost
DB_PORT = 5432
3 Chạy Tool
-- python anonymizer.py
