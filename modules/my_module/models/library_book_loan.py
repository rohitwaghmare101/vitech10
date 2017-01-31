# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import date,timedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

class LibraryBookLoan(models.Model):
	_name = 'library.book.loan'

	def _default_date(self):
		return fields.Date.today()

	expected_return_date = fields.Date('Due for', required=True)
	book_id = fields.Many2one(comodel_name='library.book',string='Book',required=True)
	member_id = fields.Many2one(comodel_name= 'library.member',string='Borrower',required=True)
	state = fields.Selection(selection=[('ongoing','Ongoing'),('done','Done')],
							 string='State',default='ongoing',required=True)
	date = fields.Date(string='Loan Date',required=True,default=_default_date)
	duration = fields.Integer(string='Duration',default=15)
	date_due = fields.Date(string='Due Date',compute='_compute_date_due',store=True)

	@api.depends('start_date','due_date')
	def _compute_date_due(self):
		res = {}
		for loan in self:
			start_date = fields.Date.from_string(loan.date)
			due_date = start_date + timedelta(days=loan.duration)
			loan.date_due = fields.Date.to_string(due_date)






