from odoo import models, fields

class HospitalModel(models.Model):
    _name = "bed.record"
    _description = "Hospital Bed allocation - bed type Model"

    name = fields.Char('Type', required=True)
    price = fields.Float(string='Price', required=True)

    _sql_constraints = [
        ('check_name', 'unique(name)',
         'The type of bed should be unique')
    ]