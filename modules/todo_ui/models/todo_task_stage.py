# -*- coding: utf-8 -*-
from odoo import models,fields,api

class TodoTaskStage(models.Model):
	_name = 'todo.task.stage'
	_description = 'To-do Stage'
	_order ='sequence,name'

	name = fields.Char(string='Name',size=40,translate=True)
	desc = fields.Text(string='Description')
	state = fields.Selection(string='State',
							 selection=[
								 ('draft','New'),('open','Started'),('done','Closed')
							 ])
	docs = fields.Html(string='Documentation')
	sequence = fields.Integer(string='Sequence')
	perc_complete = fields.Float(string='% Complete',digits=(3,2))
	date_effective = fields.Date(string='Effective Date')
	date_changed = fields.Datetime(string='Last Changed')
	#other field
	fold = fields.Boolean(string='Folded?')
	image = fields.Binary(string='Image')

	# inverse relationship
	tasks = fields.One2many(comodel_name='todo.task',inverse_name='stage_id')
