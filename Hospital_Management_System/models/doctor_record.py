# patient details 

from odoo import models,fields,api
from odoo.exceptions import UserError
import re
from dateutil.relativedelta import relativedelta

class HospitalPatient(models.Model):
    _name = "doctor.record"
    _description = "Doctor Details"

    name = fields.Char(string="Name",required=True)
    qualification = fields.Char(string="Qualification")
    success_rate = fields.Integer('Success Rate')
    date = fields.Date(readonly = True, default= lambda a: fields.datetime.now().date())
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age")
    contact_no = fields.Char(string="Contact")
    gender = fields.Selection(
        selection=[
            ('male','Male'),
            ('female','Female'),
            ('others','Others'),
        ],string="Gender"   
    )
    email = fields.Char(string='E-mail')
    specialization = fields.Char(string='Specialist In')
    fees = fields.Float(string='Fees', required=True)
    list_patients = fields.One2many('patient.record','doctor_id',readonly=True)
    appointment_id = fields.One2many('appointment.record','doctor_id',string="Appointments")

    appointment_count = fields.Integer(compute="_compute_doctor_count")

    _sql_constraints = [
        ('check_success_rate', 'CHECK(success_rate <= 100 AND success_rate >= 0)',
         'The Success rate should be appropriate')
    ]

    @api.constrains('contact_no')
    def _check_number(self):
        for record in self:
            print(record.contact_no)
            if len(record.contact_no)<10:
                raise UserError("Contact number must be >10")
            else:
                return True
            

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            print(record.email)
            validation = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
            if not re.match(validation,record.email):
                raise UserError("This Email is not valid")
            
    @api.depends('date','date_of_birth')
    def _compute_age(self):
        for record in self:
            record.age = relativedelta(record.date,record.date_of_birth).years

    @api.depends('appointment_id')
    def _compute_doctor_count(self):
        for record in self:
            print(record.read())
            record.appointment_count = len(record.appointment_id)
    


