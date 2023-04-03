# patient details 

from odoo import models,fields
from datetime import datetime

class Appointments(models.Model):
    _name = "appointment.record"
    _description = "Appointments"

    name = fields.Integer(string="Appointment ID",required=True)
    patient_status = fields.Selection([
            ('ambulatory', 'Ambulatory'),
            ('outpatient', 'Outpatient'),
            ('inpatient', 'Inpatient'),
        ],default='outpatient')
    appointment_date = fields.Datetime('Appointment Date',required=True,default = fields.Datetime.now)
    description = fields.Text(string="Description")
    diagnosis = fields.Many2many("diagnosis.record")
    patient_id = fields.Many2one('patient.record',default=lambda self: self.env.user)
    # patient_id = fields.Many2one('res.partner')


