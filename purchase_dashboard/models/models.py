
from odoo import models, fields, api



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    
    @api.model
    def retrieve_dashboard(self):
        res = super().retrieve_dashboard()
        po = self.env['purchase.order']
        res['total_purchase_count'] = po.search_count([('state', 'in', ['purchase','done'])])
        res['total_purchase_untaxed_amount'] = sum(po.search([]).mapped('amount_untaxed'))
        res['total_purchase_amount'] = sum(po.search([]).mapped('amount_total'))
        return res