# -*- coding: utf-8 -*-

from odoo import fields, api, models, _

class PartnerBank(models.Model):
	"""docstring for PartnerBank"""

	_inherit = 'res.partner.bank'

	rib = fields.Integer(string="RIB")


class ResBank(models.Model):
	"""docstring for ResBank"""

	_inherit = 'res.bank'

	bank_code = fields.Integer(string="Bank code")
	counter_code = fields.Char(string="Counter code", size=5)
	iban = fields.Char(string="IBAN")
