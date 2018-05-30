# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResCountry(models.Model):
	"""docstring for ResCountry"""
	_inherit = 'res.country'

	active = fields.Boolean(default=True)

class ResCompany(models.Model):
	"""docstring for ResCompany"""
	_inherit = 'res.company'

	nif = fields.Char(string="NIF", required=True)
	stat = fields.Char(string="STAT", required=True)
	form_juridique = fields.Selection([('ei', 'EI'),
                                      ('eirl', 'EIRL'),
                                      ('snc', 'SNC'),
                                      ('sarl', 'SARL'),
                                      ('sarlu', 'SARLU'),
                                      ('selarl', 'SELARL'),
                                      ('scp', 'SCP'),
                                      ('sas', 'SAS'),
                                      ('sasu', 'SASU')],
   default='sarl', string="Forme juridique", required=True)
	capital = fields.Char(string="Capital", size=128)
	rcs = fields.Char(string="RCS", required=True)

	commercial_partner_id = fields.Many2one('res.partner', string="Commercial")