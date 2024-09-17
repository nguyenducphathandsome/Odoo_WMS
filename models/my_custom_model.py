from odoo import models, fields


class MyCustomModel(models.Model):
    _name = 'my_wms.custom'
    _description = 'My Custom Model'

    Ten = fields.Char(string='Tên Kho', required=True)
    GhiChu = fields.Text(string='Ghi Chú', required=True)
