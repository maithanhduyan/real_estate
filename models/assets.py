# -*- coding: utf-8 -*-
from odoo import models, fields


class AssetAsset(models.Model):
    _name = "asset.asset"
    _description = "Asset Model"

    name = fields.Char('Name', index=True, required=True)
    photo = fields.Binary(string='Image')
    type = fields.Selection(
        [('buy', 'Buy'), ('sell', 'Sell'), ('transfer', 'Transfer')], required=True, string='Type')
    author_ids = fields.Many2many(
        'res.partner',
        string='Owner'
    )
    note = fields.Char('Note')
