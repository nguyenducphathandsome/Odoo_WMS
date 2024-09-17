from odoo import models, fields


class Location(models.Model):
    _name = 'my_wms.location'
    _description = 'Location'

    MaViTri = fields.Char(string='Mã Vị Trí', required=True)
    TenViTri = fields.Char(string='Tên Vị Trí', required=True)
    DayKe = fields.Char(string='Dãy Kệ')
    Tang = fields.Char(string='Tầng')
    GhiChu = fields.Text(string='Ghi Chú')
