# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Main(http.Controller):
	@http.route('/my_module/books',type='http',auth='none')

	def books(self):
		records = request.env['library.book'].sudo().search([])
		result = '<html><body><table><tr><td>'
		result += '</td></tr><tr><td>'.join(
			records.mapped('name'))
		result += '</td></tr></table></body></html>'
		return result

	@http.route('/my_module/books/json', type='json', auth='none')
	def books_json(self):
		records = request.env['library.book'].sudo().search([])
		return records.read(['name'])

