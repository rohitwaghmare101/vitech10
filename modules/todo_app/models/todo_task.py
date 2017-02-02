# -*- coding: utf-8 -*-
from odoo import models,fields,api

class TodoTask(models.Model):
	_name = 'todo.task'
	_description = 'To-do Task'

	name = fields.Char(string='Description',required=True)
	is_done = fields.Boolean(string='Done?')
	active = fields.Boolean(string='Active?',default=True)

	#action from ui button
	@api.multi
	def do_toggle_done(self):
		for task in self:
			task.is_done = not task.is_done
		return True

	@api.model
	def do_clear_done(self,args):
		dones = self.search([('is_done','=',True)])
		dones.write({'active' :False})
		return True