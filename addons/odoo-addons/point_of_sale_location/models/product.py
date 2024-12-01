from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    location_name = fields.Char(
        string='Location Name',
        compute='_compute_location_name',
        store=False,
    )

    @api.depends('location_id')
    def _compute_location_name(self):
        for product in self:
            location = self.env['stock.quant'].search([
                ('product_id', '=', product.id),
                ('location_id.usage', '=', 'internal')
            ], limit=1).location_id
            product.location_name = location.complete_name if location else ''