import logging

from odoo import models, api

_logger = logging.getLogger(__name__)


class ProductReport(models.TransientModel):
    _name = 'my_wms.report_product_template'
    _description = 'Product Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['my_wms.product'].browse(docids)
        _logger.info("Report Docs: %s", docs.read(['MaSanPham', 'TenSanPham', 'LoaiSanPham', 'DonViTinh', 'GhiChu']))
        return {
            'doc_ids': docids,
            'doc_model': 'my_wms.product',
            'docs': docs,
        }
