from odoo import api, SUPERUSER_ID
def create_vn_states(env):
    vietnam = env['res.country'].search([('code', '=', 'VN')], limit=1)
    if vietnam:
        env['res.country.state'].search([('country_id', '=', vietnam.id)]).unlink()
        states = [
            {'name': 'Hà Nội', 'code': 'HN'},
            {'name': 'Hồ Chí Minh', 'code': 'HCM'},
            {'name': 'Đà Nẵng', 'code': 'DN'},
            {'name': 'Hải Phòng', 'code': 'HP'},
            {'name': 'Cần Thơ', 'code': 'CT'},
            {'name': 'Huế', 'code': 'H'},
            {'name': 'Tuyên Quang', 'code': 'VN-01'},
            {'name': 'Lào Cai', 'code': 'VN-02'},
            {'name': 'Thái Nguyên', 'code': 'VN-03'},
            {'name': 'Phú Thọ', 'code': 'VN-04'},
            {'name': 'Bắc Ninh', 'code': 'VN-05'},
            {'name': 'Hưng Yên', 'code': 'VN-06'},
            {'name': 'Lạng Sơn', 'code': 'VN-07'},
            {'name': 'Ninh Bình', 'code': 'VN-08'},
            {'name': 'Điện Biên', 'code': 'VN-09'},
            {'name': 'Lai Châu', 'code': 'VN-10'},
            {'name': 'Sơn La', 'code': 'VN-11'},
            {'name': 'Cao Bằng', 'code': 'VN-12'},
            {'name': 'Quảng Ninh', 'code': 'VN-13'},
            {'name': 'Thanh Hóa', 'code': 'VN-14'},
            {'name': 'Nghệ An', 'code': 'VN-15'},
            {'name': 'Hà Tĩnh', 'code': 'VN-16'},
            {'name': 'Quảng Trị', 'code': 'VN-17'},
            {'name': 'Quảng Ngãi', 'code': 'VN-18'},
            {'name': 'Gia Lai', 'code': 'VN-19'},
            {'name': 'Đắc Lắk', 'code': 'VN-20'},
            {'name': 'Khánh Hòa', 'code': 'VN-21'},
            {'name': 'Lâm Đồng', 'code': 'VN-22'},
            {'name': 'Đồng Nai', 'code': 'VN-23'},
            {'name': 'Tây Ninh', 'code': 'VN-24'},
            {'name': 'Đồng Tháp', 'code': 'VN-25'},
            {'name': 'An Giang', 'code': 'VN-26'},
            {'name': 'Vĩnh Long', 'code': 'VN-27'},
            {'name': 'Cà Mau', 'code': 'VN-28'},          
        ]
    for state in states:
        env['res.country.state'].create({
            'name': state['name'],
            'code': state['code'],
            'country_id': vietnam.id,
        })