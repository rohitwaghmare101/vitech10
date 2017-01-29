# -*- coding: utf-8 -*-
from odoo import http

# class Modules/myScaffolded(http.Controller):
#     @http.route('/modules/my_scaffolded/modules/my_scaffolded/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modules/my_scaffolded/modules/my_scaffolded/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modules/my_scaffolded.listing', {
#             'root': '/modules/my_scaffolded/modules/my_scaffolded',
#             'objects': http.request.env['modules/my_scaffolded.modules/my_scaffolded'].search([]),
#         })

#     @http.route('/modules/my_scaffolded/modules/my_scaffolded/objects/<model("modules/my_scaffolded.modules/my_scaffolded"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modules/my_scaffolded.object', {
#             'object': obj
#         })