# -*- coding: utf-8 -*-
from odoo import http

# class TodoKanban(http.Controller):
#     @http.route('/todo_kanban/todo_kanban/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_kanban/todo_kanban/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_kanban.listing', {
#             'root': '/todo_kanban/todo_kanban',
#             'objects': http.request.env['todo_kanban.todo_kanban'].search([]),
#         })

#     @http.route('/todo_kanban/todo_kanban/objects/<model("todo_kanban.todo_kanban"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_kanban.object', {
#             'object': obj
#         })