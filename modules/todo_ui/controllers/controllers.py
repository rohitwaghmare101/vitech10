# -*- coding: utf-8 -*-
from odoo import http

# class TodoUi(http.Controller):
#     @http.route('/todo_ui/todo_ui/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_ui/todo_ui/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_ui.listing', {
#             'root': '/todo_ui/todo_ui',
#             'objects': http.request.env['todo_ui.todo_ui'].search([]),
#         })

#     @http.route('/todo_ui/todo_ui/objects/<model("todo_ui.todo_ui"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_ui.object', {
#             'object': obj
#         })