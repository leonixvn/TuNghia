import psycopg2

# Thông tin kết nối database PostgreSQL của Odoo
DB_NAME = "odoo"
DB_USER = "odoo"
DB_PASSWORD = "odoo"
DB_HOST = "localhost"
DB_PORT = "5432"

# Hàm mã hóa XOR giữ nguyên độ dài
def xor_encrypt(text, key="K"):
    """Mã hóa XOR giữ nguyên độ dài"""
    if not text:
        return text
    return ''.join(chr(ord(c) ^ ord(key)) for c in text)

def anonymize_data():
    """Ẩn danh dữ liệu trong bảng res_partner"""
    try:
        # Kết nối database
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()

        # Lấy danh sách các đối tác (partners)
        cur.execute("SELECT id, name, email, phone FROM res_partner;")
        partners = cur.fetchall()

        # Duyệt qua từng partner và ẩn danh dữ liệu
        for partner_id, name, email, phone in partners:
            update_fields = {}
            
            if name:
                update_fields["name"] = xor_encrypt(name)
            if email:
                update_fields["email"] = xor_encrypt(email)
            if phone:
                update_fields["phone"] = xor_encrypt(phone)

            # Nếu có dữ liệu cần cập nhật, thực hiện truy vấn UPDATE
            if update_fields:
                update_query = "UPDATE res_partner SET " + ", ".join(f"{field} = %s" for field in update_fields.keys()) + " WHERE id = %s"
                values = list(update_fields.values()) + [partner_id]
                cur.execute(update_query, values)

        # Lưu thay đổi vào database
        conn.commit()

        print("✅ Dữ liệu đã được ẩn danh thành công!")

    except Exception as e:
        print(f"❌ Lỗi khi ẩn danh dữ liệu: {e}")
    finally:
        cur.close()
        conn.close()

# Chạy chương trình
if __name__ == "__main__":
    anonymize_data()
