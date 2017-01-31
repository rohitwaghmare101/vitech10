# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import date, timedelta

class LibraryLoanWizard(models.TransientModel):
	_name = 'library.loan.wizard'

	member_id =fields.Many2one(comodel_name='library.member',string='Member')
	book_ids = fields.Many2many(comodel_name='library.book',string='Books')

	@api.multi
	def record_loans(self):
		for wizard in self:
			member  = wizard.member_id
			books = wizard.book_ids
			loan = self.with_env['library.book.loan']
			for book in wizard.book_ids:
				#values = self._prepare_loan(book)
				values = {
					'member_id' : member.id,
					'book_id' : book.id
				}
				loan.create(values)

	@api.multi
	def _prepare_loan(self,book):
		values = super(LibraryLoanWizard, self)._prepare_loan(book)
		loan_duration = self.member_id.loan_duration
		expected = date.today() + timedelta(days=loan_duration)
		values.update(
			{'expected_return_date': fields.Date.to_string(expected)}
		)
		return values