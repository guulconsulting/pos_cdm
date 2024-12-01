from odoo import models
import logging

_logger = logging.getLogger(__name__)

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].extend([
            'qty_available',
            'location_id',
        ])
        return result

    def _get_pos_ui_product_product(self, params):
        result = super()._get_pos_ui_product_product(params)
        Location = self.env['stock.location']
        
        for product in result:
            quants = self.env['stock.quant'].search([
                ('product_id', '=', product['id']),
                ('location_id.usage', '=', 'internal')
            ], limit=1)
            
            if quants:
                location = quants.location_id
                product['location_name'] = location.complete_name
            else:
                product['location_name'] = 'No stock location'
            
            _logger.info(f"Product {product['id']} location: {product['location_name']}")
        
        return result