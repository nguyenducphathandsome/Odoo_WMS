from odoo import models, fields


class NhaCungCap(models.Model):
    _name = 'my_wms.supplier'
    _description = 'Nha Cung Cap'

    MaNhaCungCap = fields.Char(string='Mã NCC', required=True)
    TenNhaCungCap = fields.Char(string='Mã NCC', required=True)
    Email = fields.Char(string='Email')
    DienThoai = fields.Char(string='Số Điện Thoại', help='Enter the phone number', required=True)
    GhiChu = fields.Text(string='Ghi Chú')
