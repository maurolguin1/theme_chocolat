# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AccountInvoice(models.Model):
	"""docstring for AccountInvoice"""
	_inherit = 'account.invoice'

	payment_date = fields.Date(string="Payment date", readonly=True)


class account_payment(models.Model):
	"""docstring for AccountPayment"""
	_inherit = 'account.payment'

	@api.multi
	def post(self):
		""" Create the journal items for the payment and update the payment's state to 'posted'.
			A journal entry is created containing an item in the source liquidity account (selected journal's default_debit or default_credit)
			and another in the destination reconciliable account (see _compute_destination_account_id).
			If invoice_ids is not empty, there will be one reconciliable move line per invoice to reconcile with.
			If the payment is a transfer, a second journal entry is created in the destination journal to receive money from the transfer account.
		"""
		rec = super(account_payment, self).post()

		for record in self:
			for invoice in record.invoice_ids:
				invoice.write({'payment_date': record.payment_date})