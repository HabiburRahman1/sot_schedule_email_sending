# -*- coding: utf-8 -*-

from odoo import models, fields, api
class ScheduleEmailSending(models.TransientModel):
    _name = 'mail.compose.message'
    _inherit = 'mail.compose.message'

    scheduled_date = fields.Datetime(string='Scheduled Date')


    # partner_ids = fields.Many2many(
    #     'res.partner', 'schedule_mail_compose_message_res_partner_rel',
    #     'wizard_id', 'partner_id', 'Additional Contacts',
    #     domain=[('type', '!=', 'private')])
    # attachment_ids = fields.Many2many(
    #     'ir.attachment', 'schedule_mail_compose_message_ir_attachments_rel',
    #     'wizard_id', 'attachment_id', 'Attachments')

    # @api.model
    # def create(self, vals):

    #     return super(ScheduleEmailSending, self).create(vals)
        
    
    # @api.model
    # def cron_email_schedule(self):
    #     machines = self.env['biometric.device.machine'].search([])
    #     for machine in machines:
    #         machine.download_attendance()

    # def action_send_mail(self):
    #     for isdf in self:
    #         print(isdf.id)

    #     print("action_send_mail")
    #     print("action_send_mail")
    #     print("action_send_mail")
    #     print("action_send_mail")
    #     print("action_send_mail")
    #     machines = self.env['mail.compose.message'].search([])
    #     for machine in machines:
    #         print(machine.id)
    #         print(machine.name)
    #         print(machine.id)


class ScheduleEmailSending(models.Model):
    _name = 'schedule.email.sending'
    _inherit = 'mail.compose.message'

    scheduled_date = fields.Datetime(string='Scheduled Date')

    partner_ids = fields.Many2many(
        'res.partner', 'schedule_mail_compose_message_res_partner_rel',
        'wizard_id', 'partner_id', 'Additional Contacts',
        domain=[('type', '!=', 'private')])
    attachment_ids = fields.Many2many(
        'ir.attachment', 'schedule_mail_compose_message_ir_attachments_rel',
        'wizard_id', 'attachment_id', 'Attachments')

    
    def action_send_mail(self):
        for isdf in self:
            print(isdf.id)

        print("action_send_mail")
        print("action_send_mail")
        print("action_send_mail")
        print("action_send_mail")
        print("action_send_mail")
        machines = self.env['mail.compose.message'].search([])
        for machine in machines:
            print(machine.id)
            print(machine.name)
            print(machine.id)