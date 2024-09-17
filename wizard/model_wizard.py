from odoo import models, fields, api


class MyWizard(models.TransientModel):
    _name = 'my.wizard'
    _description = 'My Wizard'

    name = fields.Char('Name')
    date = fields.Date('Date')
    amount = fields.Float('Amount')

    @api.model
    def action_confirm(self):
        # Logic xử lý khi người dùng nhấn nút "Confirm"
        return {'type': 'ir.actions.act_window_close'}
