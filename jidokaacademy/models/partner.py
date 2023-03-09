from odoo import models, fields


class InheritPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean('is_instructor', default=False)


# Error
# from odoo import models, fields


# class InheritPartner(models.Model):
#     _inherit = 'res.partner'

#     is_instructor = fields.Boolean('Instructor', default=False)
