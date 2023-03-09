from odoo import models, fields, api


class WizardAttendees(models.TransientModel):
    _name = 'wizard.attendees'

    session_id = fields.Many2one('jidokaacademy.session', string='Session')
    partner_ids = fields.Many2many('res.partner', string='Attendees')

    def process(self):
        self.session_id.partner_ids |= self.partner_ids