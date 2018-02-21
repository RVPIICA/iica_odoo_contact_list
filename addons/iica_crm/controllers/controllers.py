# -*- coding: utf-8 -*-
from odoo import http

# class IicaCrm(http.Controller):
#     @http.route('/iica_crm/iica_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iica_crm/iica_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iica_crm.listing', {
#             'root': '/iica_crm/iica_crm',
#             'objects': http.request.env['iica_crm.iica_crm'].search([]),
#         })

#     @http.route('/iica_crm/iica_crm/objects/<model("iica_crm.iica_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iica_crm.object', {
#             'object': obj
#         })