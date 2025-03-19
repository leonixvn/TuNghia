from odoo import models, api, SUPERUSER_ID

def xor_encrypt(text, key="K"):
    """Mã hóa XOR giữ nguyên độ dài"""
    if not text:
        return False
    encrypted_text = ''.join(chr(ord(c) ^ ord(key)) for c in text)
    return encrypted_text.replace("\x00", " ")

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def update_encrypted_data(self):
        partners = self.search([])  # Lấy tất cả bản ghi
        for partner in partners:
            encrypted_name = xor_encrypt(partner.name) if partner.name else False
            encrypted_email = xor_encrypt(partner.email) if partner.email else False
            encrypted_phone = xor_encrypt(partner.phone) if partner.phone else False
            partner.write({
                "name": encrypted_name,
                "email": encrypted_email,
                "phone": encrypted_phone
            })
