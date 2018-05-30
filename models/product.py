# -*- coding: utf-8 -*-

from odoo import fields, api, models, _
import odoo.addons.decimal_precision as dp

class ProductTemplate(models.Model):
	"""docstring for ProductTemplate"""
	_inherit = 'product.template'

	code = fields.Char(string="Code")
	price_ttc = fields.Monetary(string="Prix de vente TTC", default=1.0, compute='_comute_price_ttc', digits=dp.get_precision('Product Price'))

	@api.depends('list_price', 'taxes_id')
	def _comute_price_ttc(self):
		for product in self:
			if product.taxes_id:
				taxe = product.taxes_id[0].amount/100
				product.price_ttc = product.list_price + (product.list_price * taxe) - ((product.list_price + (product.list_price * taxe))%1)
			else:
				product.price_ttc = product.list_price

	def _website_price(self):
		self.mapped('product_variant_id')

		for p in self:
			p.website_price = round(p.product_variant_id.website_price, 1)
			p.website_public_price = p.product_variant_id.website_public_price