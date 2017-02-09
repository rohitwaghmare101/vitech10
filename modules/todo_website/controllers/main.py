# -*- coding: utf-8 -*-
from odoo import http

# class TodoWebsite(http.Controller):
#     @http.route('/todo_website/todo_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_website/todo_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_website.listing', {
#             'root': '/todo_website/todo_website',
#             'objects': http.request.env['todo_website.todo_website'].search([]),
#         })

#     @http.route('/todo_website/todo_website/objects/<model("todo_website.todo_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_website.object', {
#             'object': obj
#         })


from odoo import http