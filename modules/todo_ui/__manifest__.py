# -*- coding: utf-8 -*-
{
    'name': "UI To-Do app",
    'summary': """
        User Interface improvements to the To-Do app""",

    'description': """
        User Friendly Feature
    """,
    'author': "Suhendar",
    'website': "http://www.vileo.co.id",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['todo_user'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application' : False,
    'installable': True,
    'auto_install' : False,
}