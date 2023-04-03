# patient details 

from odoo import models,fields

class Diagnosis(models.Model):
    _name = "diagnosis.record"
    _description = "diagnosis Details"

    name = fields.Char(string="Diagnosis Name",required=True)

    

