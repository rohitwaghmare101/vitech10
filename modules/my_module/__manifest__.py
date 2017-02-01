# -*- coding: utf-8 -*-
{
	'name':"Library Book",
	'summary':"Odoo 10.0 Training",
	'description' : """Long Description""",
	'author' : "Suhendar",
	'license':"AGPL-3",
	'website':"vileo.co.id",
	'category':"Library",
	'version':"10.0.1.0.0",
	'depends':[
		"base","decimal_precision"
	],
	'data':[
		"security/ir.model.access.csv",
		"views/library_book.xml",
		"views/library_loan_wizard.xml",
		"views/inherence.xml",
        "security/library_security.xml",
		#"views/res_config_settings.xml",

	],
	'demo':[
		#"demo.xml",
	],
	'installable': True,
	'application': True,
	'auto_install': False,
}