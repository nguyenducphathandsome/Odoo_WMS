from odoo import models, fields


class Product(models.Model):
    _name = 'my_wms.product'
    _description = 'Product'

    MaSanPham = fields.Char(string='Mã Sản Phẩm', required=True)
    LoaiSanPham = fields.Many2one('my_wms.product_type', string='Loại Sản Phẩm', required=True, ondelete='restrict')
    TenSanPham = fields.Char(string='Tên Sản Phẩm', required=True)
    DonViTinh = fields.Many2one('my_wms.unit.of.measure', string='Đơn Vị Tính', required=True, ondelete='restrict')
    GhiChu = fields.Text(string='Ghi Chú', required=False)
