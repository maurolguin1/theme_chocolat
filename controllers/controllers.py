# -*- coding: utf-8 -*-

from odoo.addons.website_sale.controllers.main import WebsiteSale

import json
import logging
from werkzeug.exceptions import Forbidden

from odoo import http, tools, _
from odoo.http import request
from odoo.addons.base.ir.ir_qweb.fields import nl2br
from odoo.addons.website.models.website import slug
from odoo.addons.website.controllers.main import QueryURL
from odoo.exceptions import ValidationError
from odoo.addons.website_form.controllers.main import WebsiteForm

class TestWebsite(http.Controller):
	"""docstring for TestWebsite"""
	@http.route('/test', type='http', auth='public')
	def test_website(self):
		return "<h1>Hello world!</h1>"


class ChocoWebsiteSale(WebsiteSale):
	"""docstring for WebsiteSale"""

	@http.route(['/products/products'], auth='public', website=True)
	def index(self, **kw):
		return "<h1>Hello world!</h1>"

	@http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth="public", website=True)
	def shop(self, page=0, category=None, search='', ppg=False, **post):

		categs = request.env['product.public.category'].search([])
		values['categories'] = categs

		rendered = super(ChocoWebsiteSale, self).shop()
		rendered.qcontext['values']['categories'] = categs

		return rendered