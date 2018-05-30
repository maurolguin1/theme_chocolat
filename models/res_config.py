# -*- coding: utf-8 -*-


from odoo import api, models, fields


class ChocoWebsiteConfigSettings(models.TransientModel):
    _inherit = 'website.config.settings'

    free_shipping = fields.Boolean("Free shipping")