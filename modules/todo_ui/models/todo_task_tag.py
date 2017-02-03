# -*- coding: utf-8 -*-
from odoo import models,fields,api

class TodoTaskTag(models.Model):
	_name = 'todo.task.tag'
	_description = 'To-do Tag'

	name = fields.Char(string='Name',size=40,translate=True)
	#inverse relationship
	task_ids = fields.Many2many(comodel_name='todo.task',string='Task')
	#parent required
	_parent_store = True
	parent_id = fields.Many2one(comodel_name='todo.task.tag',ondelete='restrict')
	parent_left = fields.Integer(string='Parent Left',index=True)
	parent_right = fields.Integer(string='Parent Right',index=True)
	child_ids = fields.One2many(comodel_name='todo.task.tag',inverse_name='parent_id',string='Childs Tags')


