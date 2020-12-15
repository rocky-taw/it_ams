# See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    isAsset = fields.Boolean("Is Asset")
