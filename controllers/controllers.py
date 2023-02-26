# -*- coding: utf-8 -*-
# from odoo import http


# class Nba(http.Controller):
#     @http.route('/nba/nba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nba/nba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nba.listing', {
#             'root': '/nba/nba',
#             'objects': http.request.env['nba.nba'].search([]),
#         })

#     @http.route('/nba/nba/objects/<model("nba.nba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nba.object', {
#             'object': obj
#         })
