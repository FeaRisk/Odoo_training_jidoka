from odoo import api, models, fields
from odoo.exceptions import ValidationError

class session(models.Model):
    _name = 'jidokaacademy.session'
    _description = 'jidokaacademy.session'
  
    name = fields.Char(string='Title', required=True)
    start_date = fields.Date(string='Start Date', default= fields.Date.today())
    duration = fields.Float(string='Duration')
    number_of_seats = fields.Float('Number of seats')
    description = fields.Text('Description')
    partner_id = fields.Many2one(
        'res.partner', string='Instructor', domain="[('is_instructor','=',True)]")
    partner_ids = fields.Many2many('res.partner', string='Attendees')
    course_id = fields.Many2one(
        'jidokaacademy.course', string='Course', required=True)
    taken_seats = fields.Float("Taken Seats", compute='_count_taken_seats')
    active = fields.Boolean(default=True)
    number_of_attendees = fields.Float('Number of Attendees', compute='count_attendees', store=True)

    @api.depends('partner_ids')
    def count_attendees(self):
        for rec in self:
            rec.number_of_attendees = len(rec.partner_ids)

    def _count_taken_seats(self):
        for rec in self:
            if rec.partner_ids and rec.number_of_seats:
                rec.taken_seats = len(rec.partner_ids) / rec.number_of_seats * 100
            else:
                rec.taken_seats = 0

# Error 1
    @api.onchange('number_of_seats','partner_ids')
    def _onchange_number_of_seats(self):
        if self.number_of_seats < 0:
            return {
                'warning': {
                    'title': "Invalid Value",
                    'message': "Cannot add negatif number on seats ",
                }
            }
        if len(self.partner_ids) > self.number_of_seats:
            return {
                'warning': {
                    'title': "Something bad happened",
                    'message': "Participants more than seats",
                }
            }


    @api.constrains('partner_ids','partner_id')
    def _check_attendees(self):
        for record in self:
            if record.partner_id in record.partner_ids:
                raise ValidationError("Instructor Cannot be attendees: %s" % record.partner_id.name)
