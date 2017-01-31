# -*- coding: utf-8 -*-
from odoo import models,fields

class LibraryMember(models.Model):
	_name = 'library.member'
	_inherit = {'res.partner' : 'partner_id'}

	partner_id = fields.Many2one('res.partner',ondelete='cascade')
	date_start = fields.Date(string='Member Since')
	date_end = fields.Date(string='Termination Date')
	member_number = fields.Char(string='Member number')
	loan_duration = fields.Integer(string='Loan duration',default=15,required=True)

	