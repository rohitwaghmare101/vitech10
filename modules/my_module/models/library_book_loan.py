# -*- coding: utf-8 -*-
from odoo import models,fields

class LibraryBookLoan(models.Model):
	_name = 'library.book.loan'
	#field
	expected_return_date = fields.Date('Due for', required=True)