from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'my_wms.custom'

    MaKho = fields.Char(string='Mã Kho', requied=True)
    DiaChi = fields.Char(string = 'Địa Chỉ', requied=True)
    DienThoai = fields.Char(string='Số Điện Thoại', help='Enter the phone number', required=True)