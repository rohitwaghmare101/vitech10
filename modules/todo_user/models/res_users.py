# -*- coding: utf-8 -*-
from odoo import models,fields

class User(models.Model):
	_name = 'res.users'
	_inherit = {'res.partners' : 'partner_id'}
	partner_id = fields.Many2one(comodel_name='res.partner')

	