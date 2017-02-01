# -*- coding: utf-8 -*-
from odoo import models,fields

class ConfigSettings(models.TransientModel):
	_inherit = 'res_config_settings'
	group_release_dates = fields.Boolean(string='Manage Book release date',group='base.group.user',
										 implied_group='my_module.group_release_dates')
	module_note = fields.Boolean(string='Install note app')

