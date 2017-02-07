# -*- coding: utf-8 -*-
{
    'name': "To-do Task Management Assistant",
    'summary': """
        Management Assistant To do Wizard""",

    'description': """
        Mass Edit your to-do backlog
    """,

    'author': "Suhendar",
    'website': "http://www.vileo.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/todo_wizard_view.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}