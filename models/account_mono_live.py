from odoo import models, api

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.model
    def obfuscate_account_data(self, k):
        """Ẩn danh dữ liệu kế toán bằng cách nhân giá trị gốc với tham số k, đảm bảo k > 0 và k ≠ 1."""
        
        if not isinstance(k, (int, float)) or k <= 0 or k == 1:
            raise ValueError("Tham số k phải là một số lớn hơn 0 và khác 1!")

        for line in self.search([]):
            line.write({
                "debit": line.debit * k,
                "credit": line.credit * k
            })
