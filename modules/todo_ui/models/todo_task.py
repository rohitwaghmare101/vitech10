# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
	_inherit = 'todo.task'
	stage_id = fields.Many2one(comodel_name='todo.task.stage',string='Stage')
	tag_ids = fields.Many2many(comodel_name='todo.task.tag',
							   relation='todo_task_tag_rel',
							   column1='task_id',column2='tag_id',string='Tags')
	refers_to = fields.Reference([('res.users','User'),('res.partner','Partner')],string='Refers to')
	# Related fields by selection
	state = fields.Selection(related = 'stage_id.state',string='Stage State',store=True)
	stage_fold = fields.Boolean(string='Stage Folded?',compute='_compute_stage_fold',
								search='_search_stage_fold',inverse='_write_stage_fold',store=True)

	stage_state = fields.Selection(related='stage_id.state',string='Stage State')
	effort_estimate = fields.Integer('Effort Estimate')
	user_todo_count = fields.Integer(string='User To-Do Count',compute='compute_user_todo_count')
	docs = fields.Html('Documentation')

	_sql_constraints = [
		('todo_task_name_unique','UNIQUE(name,active)','Task Title must be unique')
	]

	@api.depends('stage_id.fold')
	def _compute_stage_fold(self):
		for task in self:
			task.stage_fold = task.stage_id.fold

	def _search_stage_fold(self,operator,value):
		return  [('stage.id.fold',operator,value)]

	def _write_stage_fold(self):
		self.stage_id.fold = self.stage_fold

	@api.constrains
	def _check_name_size(self):
		for todo in self:
			if len(todo.name) < 5:
				raise ValidationError('Must have 5 chars')

	# Chapter 06 Smart Button statistic
	def compute_user_todo_count(self):
		for task in self:
			task.user_todo_count = task.search_count(
				[('user_id', '=', task.user_id.id)])





