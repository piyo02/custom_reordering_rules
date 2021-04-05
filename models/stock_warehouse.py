from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class Orderpoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    def _default_location_ids(self):
        return self.env['stock.location'].search([
            ('location_id.name', '=', 'TKTAS')
        ]).ids

    location_ids = fields.Many2many(
        'stock.location',
        'order_location_rel',
        string='Gudang',
        default=_default_location_ids,
        # required=True
    )
    warehouse_id = fields.Many2one(
        'stock.warehouse', 'Warehouse',
        ondelete="cascade", required=False)