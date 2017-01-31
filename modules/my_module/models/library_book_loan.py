# -*- coding: utf-8 -*-
from odoo import models,fields,api

class LibraryBookLoan(models.Model):
	_name = 'library.book.loan'
	#field
	expected_return_date = fields.Date('Due for', required=True)
	book_id = fields.Many2one(comodel_name='library.book',string='Book',required=True)
	member_id = fields.Many2one(comodel_name= 'library.member',string='Borrower',required=True)
	state = fields.Selection(selection=[('ongoing','Ongoing'),('done','Done')],
							 string='State',default='ongoing',required=True)



