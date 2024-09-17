from odoo import models, fields, api


class ProductUpdateWizard(models.TransientModel):
    _name = 'product.update.wizard'
    _description = 'Product Update Wizard'

    product_id = fields.Many2one('my_wms.product', string='Product', required=True)
    ma_san_pham = fields.Char(string='Mã Sản Phẩm', required=True)
    loai_san_pham = fields.Many2one('my_wms.product_type', string='Loại Sản Phẩm', required=True)
    ten_san_pham = fields.Char(string='Tên Sản Phẩm', required=True)
    don_vi_tinh = fields.Many2one('my_wms.unit.of.measure', string='Đơn Vị Tính', required=True)
    ghi_chu = fields.Text(string='Ghi Chú')

    @api.model
    def default_get(self, fields):
        res = super(ProductUpdateWizard, self).default_get(fields)
        product_id = self._context.get('active_id')
        if product_id:
            product = self.env['my_wms.product'].browse(product_id)
            res.update({
                'product_id': product.id,
                'ma_san_pham': product.MaSanPham,
                'loai_san_pham': product.LoaiSanPham.id,
                'ten_san_pham': product.TenSanPham,
                'don_vi_tinh': product.DonViTinh.id,
                'ghi_chu': product.GhiChu,
            })
        return res

    def action_update_product(self):
        self.ensure_one()
        self.product_id.write({
            'MaSanPham': self.ma_san_pham,
            'LoaiSanPham': self.loai_san_pham.id,
            'TenSanPham': self.ten_san_pham,
            'DonViTinh': self.don_vi_tinh.id,
            'GhiChu': self.ghi_chu,
        })
        return {'type': 'ir.actions.act_window_close'}
