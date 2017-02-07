# -*- coding: utf-8 -*-
from odoo import http

# class TodoWizard(http.Controller):
#     @http.route('/todo_wizard/todo_wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_wizard/todo_wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_wizard.listing', {
#             'root': '/todo_wizard/todo_wizard',
#             'objects': http.request.env['todo_wizard.todo_wizard'].search([]),
#         })

#     @http.route('/todo_wizard/todo_wizard/objects/<model("todo_wizard.todo_wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_wizard.object', {
#             'object': obj
#         })