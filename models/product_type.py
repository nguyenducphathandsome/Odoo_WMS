from odoo import models, fields


class Product_type(models.Model):
    _name = 'my_wms.product_type'
    _description = 'Product Type'

    LoaiSanPham = fields.Char(string='Loại Sản Phẩm', required=True)