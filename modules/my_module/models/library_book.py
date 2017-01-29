# -*- coding: utf-8 -*-
from odoo import models,fields
from odoo.addons import decimal_precision as dp
from datetime import timedelta,datetime
from odoo import api

class BaseArchive(models.AbstractModel):
    _name = 'base.archive'
    active = fields.Boolean(default=True)

    def do_archive(self):
        for record in self:
            record.active = not record.active

class LibraryBook(models.Model):
	_name = 'library.book'
	_inherit = ['base.archive']
	_description = 'Library Book'
	_order = 'date_release desc,name asc'
	_rec_name = 'short_name'

	name = fields.Char(string='Title',required=True)
	date_release = fields.Date(string='Release Date')
	author_ids = fields.Many2many('res.partner',string='Author')
	short_name = fields.Char(string='Short Title',size=100,translate=False)
	notes = fields.Text(string="Internal Notes")
	state = fields.Selection([
		('draft','Not Available'),
		('available','Available'),
		('lost','Lost')
	],string="State")
	description=fields.Html(string="Description",sanitize=True,strip_style=False,translate=False)
	cover = fields.Binary(string="Book Cover")
	out_of_print = fields.Boolean(string='Out of Print')
	date_updated = fields.Datetime(string='Last Updated')
	pages = fields.Integer(string='Number of Page',default=0,help='Total book page count',
						   groups='base.group_user',states={'cancel' : [('readonly',True)]},
						   copy=True,index=False,readonly=False,required=False,company_dependent=False)
	reader_rating = fields.Float(string='Reader Average Rating',digits=(14,4))
	active = fields.Boolean(string='Active',default=True)
	cost_price = fields.Float(string='Book Cost',digits=dp.get_precision('Book Price'))
	currency_id = fields.Many2one('res.currency',string='Currency')
	retail_price = fields.Monetary(string='Retail Price')
	publisher_id = fields.Many2one('res.partner',string='Publisher',ondelete='set null',context={},domain=[])
	publisher_city = fields.Char('Publisher City',related='publisher_id.city')
	age_days = fields.Float(string='Days Since Release',compute='_compute_age',
							search='_search_age',store=True,compute_sudo=False)

	def name_get(self):
		result = []
		for record in self:
			result.append(
				(record.id,
				 u"%s (%s)" % (record.name, record.date_release)
				 ))
		return result

	_sql_constraints = [
		('name_uniq','UNIQUE (name)','Book Title must be unique.')
	]

	@api.constrains('date_release')
	def _check_release_date(self):
		for record in self:
			if record.date_release > fields.Date.today():
				raise models.ValidationError('Error ! Release date must be in past')

	@api.depends('date_release')
	def _compute_age(self):
		today = fields.Date.from_string(fields.Date.today())
		for book in self.filtered('date_release'):
			delta = (fields.Date.from_string(book.date_release) - today)
			book.age_days = delta.days

	"""
	def _inverse_age(self):
		today = fields.Date.from_string(fields.Date.today())
		for book in self.filtered('date_release'):
			delta = timedelta(days=book.age_days) - today
			book.date_release = fields.Date.to_string(delta)
		"""

	def _search_age(self, operator, value):
		today = fields.Date.from_string(fields.Date.today())
		value_days = timedelta(days=value)
		value_date = fields.Date.to_string(today - value_days)
		return [('date_release',operator,value_date)]

	@api.model
	def _referencable_models(self):
		models = self.env['res.request.link'].search([])
		return [(x.object, x.name) for x in models]

	ref_doc_id = fields.Reference(
		selection=_referencable_models,
		string='Reference Document')


