# See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    isAsset = fields.Boolean("Is Asset")
