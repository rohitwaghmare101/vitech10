# -*- coding: utf-8 -*-
{
    'name': "To-DO Application",
    'summary': """
       TO DO Apps
       """,
    'description': """
       Manage your personal To-Do Task
    """,
    'license' : "LGPL-3",

    'author': "Suhendar",
    'website': "http://www.vileo.co.id",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Task',
    'version': '10.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
		'security/todo_access_rules.xml',
        'views/views.xml',
        'views/templates.xml',
		'views/todo_task.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	'application': True,
    'installable' : True,
    'auto_install' : False,
}