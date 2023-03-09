# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'jidokaacademy.course'
    _description = 'jidokaacademy.course'

    _sql_constraints = [
        ('check_name_description_different','CHECK (name != description)','Name and description must be different'),
        ('check_name_unique','UNIQUE (name)','Name must be unique')
    ]

    name = fields.Char(string='Title', required=True)
    user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many(
        'jidokaacademy.session', 'course_id', string='session')
    description = fields.Text(string='Description')
    
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', "Copy of {}%".format(self.name))]
        )

        # Kalau tidak ada copy
        if not copied_count:
            new_name = "Copy of {}".format(self.name)
        
        # Kalau ada copy
        else:
            # Copy of Training Odoo (jumlah ada berapa)
            new_name = "Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super (Course, self).copy(default)

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
