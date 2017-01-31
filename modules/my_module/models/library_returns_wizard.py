# -*- coding: utf-8 -*-
from odoo import models,fields,api

class LibraryReturnsWizard(models.TransientModel):
	_name = 'library.returns.wizard'

	member_id = fields.Many2one(comodel_name='library.member',string='Member')
	book_ids = fields.Many2many(comodel_name='library.book',string='Books')

	@api.multi
	def record_returns(self):
		loan = self.env['library.book.loan']
		for record in self:
			loans = loan.search(
				[
					('state','=','ongoing'),
					('book_id', 'in', record.book_ids.ids),
					('member_id', '=', record.member_id.id)
				]
			)
			loans.write({'state' : 'done'})

	"""
	@api.onchange('member_id')
	def onchange_member(self):
		loan = self.env['library.book.loan']
		loans = loan.search(
			[
				('state','=','ongoing'),
				('member_id','=',self.member_id.id)
			]
		)
		self.book_ids = loans.mapped('book_id')
	"""

	@api.onchange('member_id')
	def onchange_member(self):
		loan = self.env['library.book.loan']
		loans = loan.search(
			[
				('state', '=', 'ongoing'),
				('member_id','=',self.member_id.id)
			]
		)

		self.book_ids = loans.mapped('book_id')
		result = {
			'book_ids': [
				('id', 'in', self.book_ids.ids)
			]
		}

		late_domain = [
			('id', 'in', loans.ids),
			('expected_return_date', '<', fields.Date.today())
		]

		late_loans = loans.search(late_domain)

		if late_loans:
			message = ('Warn the meber that the following'
					   'book are late:\n')
			titles = late_loans.mapped('book_id.name')
			result['warning'] = {
				'title': 'Late books',
				'message': message + '\n'.join(titles)
			}

		return result
