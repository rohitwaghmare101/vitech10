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


	@api.model
	def partners_by_country(self):
		sql = ('SELECT country_id,array_agg(id) '
			   'FROM res_partner '
			   'WHERE active=true AND country_id IS NOT NULL '
			   'GROUP BY country_id ')
		self.env.cr.execute(sql)
		country_model = self.env['res.country']
		result = {}
		for country_id, partner_ids in self.env.cr.fetchall():
			country = country_model.browse(country_id)
			partners = self.search(
				[('id','in',tuple(partner_ids))]
			)
			result[country] = partners

		return result

