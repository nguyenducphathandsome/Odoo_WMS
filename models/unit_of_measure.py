from odoo import models, fields


class DonViTinh(models.Model):
    _name = "my_wms.unit.of.measure"
    _description = "Unit of Measure"

    DonViTinh = fields.Char(string="Đơn Vị Tính", required=True)
    GhiChu = fields.Char(string="Ghi Chú", required=False)
