# -*- coding: utf-8 -*-
{
	'name' : "Mulituser To DO",
	'summary' : "Multi User TO DO System",
	'category' : "Task",
	'description' : "Extend the To-DO app to multiuser",
	'author' : "Suhendar",
	'depends' : [
		'todo_app','mail'
	],
	'demo' : [
		'data/todo.task.csv',
		'data/todo.task.xml',
	],
	'data' : [
		'security/todo_access_rules.xml',
		'views/todo_task.xml',
	],
	'application' : False,
	'installable' : True,
	'auto_install' : False
}