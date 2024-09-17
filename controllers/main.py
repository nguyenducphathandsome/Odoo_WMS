from odoo import http
from odoo.http import request


class WmsController(http.Controller):
    @http.route('/wms', auth='public', type='http')
    def wms_check(self):
        return request.render("web.login")

