# -*- coding: utf-8 -*-
from odoo import models,fields,api

class LibraryBookCategory(models.Model):
	_name='library.book.category'
	_parent_name = 'parent_id'

	name = fields.Char(string='Category')
	parent_id = fields.Many2one('library.book.category',string='Parent Category',ondelete='restrict',index=True)
	child_ids = fields.One2many('library.book.category','parent_id',string='Child Categories')
	#to enabled hierary support also add the following
	_parent_store = True
	parent_left = fields.Integer(index=True)
	parent_right = fields.Integer(index=True)

	@api.constrains('parent_id')
	def _check_hierarchy(self):
		if not self._check_recursion():
			raise models.ValidationError('Error ! You cannot create recursive categories.')