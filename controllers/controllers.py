# -*- coding: utf-8 -*-
# from odoo import http


# class SotScheduleEmailSending(http.Controller):
#     @http.route('/sot_schedule_email_sending/sot_schedule_email_sending/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sot_schedule_email_sending/sot_schedule_email_sending/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sot_schedule_email_sending.listing', {
#             'root': '/sot_schedule_email_sending/sot_schedule_email_sending',
#             'objects': http.request.env['sot_schedule_email_sending.sot_schedule_email_sending'].search([]),
#         })

#     @http.route('/sot_schedule_email_sending/sot_schedule_email_sending/objects/<model("sot_schedule_email_sending.sot_schedule_email_sending"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sot_schedule_email_sending.object', {
#             'object': obj
#         })
