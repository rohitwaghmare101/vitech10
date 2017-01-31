# -*- coding: utf-8 -*-
from odoo import models,fields,api,exceptions
from datetime import  date,timedelta
from odoo.exceptions import UserError
from odoo.tools import _ ,DEFAULT_SERVER_DATE_FORMAT

class LibraryMember(models.Model):
	_name = 'library.member'
	_inherit = {'res.partner' : 'partner_id'}

	partner_id = fields.Many2one('res.partner',ondelete='cascade')
	date_start = fields.Date(string='Member Since')
	date_end = fields.Date(string='Termination Date')
	number = fields.Char(string='Number')
	loan_duration = fields.Integer(string='Loan duration',default=10,required=True)

	@api.multi
	def return_all_books(self):
		self.ensure_one()
		wizard = self.env['library.returns.wizard']
		values = {'member_id':self.id}
		specs = wizard._onchange_spec()
		updates = wizard.onchange(values, ['member_id'], specs)
		values.update(updates.get('value', {}))
		record = wizard.create(values)

	@api.onchange('date_end')
	def on_change_date_end(self):
		date_end = fields.Date.from_string(self.date_end)
		today = date.today()
		if date_end <= today:
			self.loan_duration = 0
			return {
				'warning' : {
					'title' : 'expired membership',
					'message' : 'This member membership ' \
								'has expired !'
				},
			}

	@api.multi
	def borrow_books(self,book_ids):
		if len(self) != 1:
			raise exceptions.UserError('Error ! it is forbidden to loan the same books to multiple member')

		loan_model = self.env['library.book.loan']

		for book in self.env['library.book'].browse(book_ids):
			val= self._prepare_loan(book)
			loan = loan_model.create(val)

	@api.multi
	def _prepare_loan(self,book):
		return {'book_id': book.id,
				'member_id': self.id,
				'duration': self.loan_duration
		}

