# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import date, timedelta

class LibraryLoanWizard(models.Model):
	_name = 'library.loan.wizard'

	@api.multi
	def _record_loans(self):
		for wizard in self:
			loan = self.with_env['library.book.loan']
			for book in wizard.book_ids:
				values = self._prepare_loan(book)
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