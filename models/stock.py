# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError
import datetime


class StockPicking(models.Model):
	"""docstring for StockPicking"""
	_inherit = 'stock.picking'

	company_id = fields.Many2one('res.company', string='Company', required=False, index=True, default=lambda self: self.env.user.company_id)
	user_id = fields.Many2one('res.users', string='Responsible', required=False, default=lambda self: self.env.user)
	# order_id = fields.Many2one('sale.order', string='Sale Order', compute='_compute_order', ondelete='cascade')
	# autres = fields.Text(compute='_compute_autres')
	client_name = fields.Char(string="Partner", compute="_compute_client")
	client_street_address = fields.Char(string="Street", compute="_compute_client")
	code_zip = fields.Char(string="Zip", compute="_compute_client")
	city = fields.Char(string="City", compute="_compute_client")
	country = fields.Char(string="Country", compute="_compute_client")
	phone = fields.Char(string="Phone", compute="_compute_client")
	delivery_date = fields.Char(string="Delivery date", compute="_compute_delivery_date")

	# client_info=fields.Boolean(invisible=1)
	# adresse_livraison=fields.Many2one('sale.order', compute='_compute_adresse_livraison', store=True)
	# adresse_facturation=fields.Many2one('sale.order', inverse="partner_shipping_id")
	# client_company_name=fields.Char(compute='_compute_client')
	# website=fields.Char(compute='_compute_client')
	# email=fields.Char(compute='_compute_client')
	# position_fiscal=fields.Char(compute='_compute_client')
	# num_fiscal=fields.Char(compute='_compute_client')

	@api.multi
	@api.depends('origin')
	def _compute_client(self):
		order = self.env['sale.order'].search([('name','=',self.origin)])
		self.client_name = order.partner_shipping_id.name
		self.client_street_address = order.partner_shipping_id.street
		self.code_zip = order.partner_shipping_id.zip
		self.city = order.partner_shipping_id.city
		self.country = order.partner_shipping_id.country_id.name
		self.phone = order.partner_shipping_id.phone

	@api.multi
	@api.depends('min_date')
	def _compute_delivery_date(self):
		self.ensure_one()
		deliv_date_str = (self.min_date).split(' ')[0]
		deliv_date = datetime.datetime.strptime(deliv_date_str, '%Y-%m-%d') + datetime.timedelta(days=4)
		self.delivery_date = deliv_date.date().strftime('%d/%m/%Y')
		# day = int(deliv_date.split('-')[2]) + 4
		# self.delivery_date = str(day) + '/' + deliv_date.split('-')[1] + '/' + deliv_date.split('-')[0]

		# self.website=s_o.partner_shipping_id.website
		# self.client_company_name=s_o.partner_shipping_id.company_name
		# self.email=s_o.partner_id.email
		# self.position_fiscal=s_o.partner_id.property_account_position_id.name
		# self.num_fiscal=s_o.partner_id.vat

	# @api.multi
	# @api.depends('origin')
	# def _compute_autres(self):
	# 	s_o = self.env['sale.order'].search([('name','=',self.origin)])
	# 	self.autres='Bon de commande: '+str(s_o.name) + u"\u000A" + 'Date de confirmation: '+str(s_o.confirmation_date)+u"\u000A"+'Condition de reglement: '+str(s_o.payment_term_id.name)+u"\u000A"+'Methode de livraison: '+ str(s_o.carrier_id.id)+u"\u000A"+'Entrepot: '+str(s_o.warehouse_id.name)+u"\u000A"+"Politique d'expedition: "+str(s_o.picking_policy)+u"\u000A"+'Vendeur: '+str(s_o.user_id.name)


	# @api.multi
	# @api.depends('origin')
	# def _compute_order(self):
	# 	for delivery in self:
	# 		delivery.order_id = self.env['sale.order'].search([('name','=',self.origin)])[0] if delivery.order_id else False

	@api.multi
	def action_delivery_order_sent(self):
		""" Open a window to compose an email, with the edi invoice template
				message loaded by default
		"""

		self.ensure_one()
		template = self.env.ref('theme_chocolat.choco_mail_template_delivery_wizard', False)
		compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
		ctx = dict(
			default_model='stock.picking',
			default_res_id=self.id,
			default_use_template=bool(template),
			default_template_id=template and template.id or False,
			default_composition_mode='comment',
			mark_invoice_as_sent=True,
			custom_layout="theme_chocolat.choco_mail_template_delivery_order"
		)
		return {
			'name': _('Delivery Order - Send by mail'),
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(compose_form.id, 'form')],
			'view_id': compose_form.id,
			'target': 'new',
			'context': ctx,
		}
