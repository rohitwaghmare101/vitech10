# -*- coding: utf-8 -*-
from odoo import models,fields
from odoo import api

class ResPartner(models.Model):
	_inherit = 'res.partner'
	_order = 'name'

	#book_ids = fields.Many2many('library.book','publisher_id',string='Published Books')
	authored_book_ids = fields.Many2many('library.book',string='Authored Book')
	count_books = fields.Integer(string="Number of Authored Book",compute='_compute_count_book')

	@api.depends('authored_book_ids')
	def _compute_count_book(self):
		for record in self:
			record.count_books = len(record.authored_book_ids)
