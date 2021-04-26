# -*- coding: utf-8 -*-
from odoo import http


class Hrmanagement(http.Controller):
    @http.route('/hrmanagement/hrmanagement/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/hrmanagement/hrmanagement/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('hrmanagement.listing', {
            'root': '/hrmanagement/hrmanagement',
            'objects': http.request.env['hrmanagement.hrmanagement'].search([]),
        })

    @http.route('/hrmanagement/hrmanagement/objects/<model("hrmanagement.hrmanagement"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('hrmanagement.object', {
            'object': obj
        })
