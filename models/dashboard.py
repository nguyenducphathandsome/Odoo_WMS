# file: module-warehouse/models/dashboard.py

from odoo import models, fields, api


class DashboardOverview(models.Model):
    _name = 'dashboard.overview'
    _description = 'Dashboard Overview'

    name = fields.Char(string='Name')
    count = fields.Integer(string='Count')
    type = fields.Selection([
        ('unit_of_measure', 'Unit of Measure'),
        ('product', 'Product'),
    ], string='Type')

    @api.model # dung de dinh nghia mot phuong thuc khong lien quan den model
    def init(self):
        self.env.cr.execute('DELETE FROM dashboard_overview')

        # Recordset dem so luong ban ghi trong model my_wms.unit.of.measure hien thi len dashboard
        unit_of_measure_count = self.env['my_wms.unit.of.measure'].search_count([])
        self.create({
            'name': 'Unit of Measure',
            'count': unit_of_measure_count,
            'type': 'unit_of_measure'
        })

        # Recordset dem so luong ban ghi trong model my_wms.product thi len dashboard
        product_count = self.env['my_wms.product'].search_count([])
        self.create({
            'name': 'Product',
            'count': product_count,
            'type': 'product'
        })
