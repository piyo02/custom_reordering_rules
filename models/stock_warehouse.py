from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class Orderpoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    location_ids = fields.Many2many(
        'stock.location',
        'order_location_rel',
        string='Gudang',
        # required=True
    )
    warehouse_id = fields.Many2one(
        'stock.warehouse', 'Warehouse',
        ondelete="cascade", required=False)


class StockLocation(models.Model):
    _inherit = "stock.location"

    orderpoint_ids = fields.Many2many(
        'stock.warehouse.orderpoint',
        'location_order_rel',
        string='Orderpoint'
    )