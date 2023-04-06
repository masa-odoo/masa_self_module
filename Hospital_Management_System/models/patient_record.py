# patient details 

from odoo import models,fields,api
from datetime import datetime
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
import re

class HospitalPatient(models.Model):
    _name = "patient.record"
    _description = "Patient Details"

    name = fields.Char(string="Name",required=True)
    age = fields.Integer(string="Age",compute="_compute_age", store=True)
    gender = fields.Selection(
        selection=[
            ('male','Male'),
            ('female','Female'),
            ('others','Others'),
        ],string="Gender"   
    )
    email = fields.Char(string='E-mail',copy=False)
    height = fields.Float('Height')
    weight = fields.Float('Weight')
    contact_no = fields.Char(string="Contact")
    address = fields.Char(string="Address")
    diagnosis = fields.Many2many("diagnosis.record")
    date = fields.Date(readonly = True, default= lambda a: fields.datetime.now().date())
    date_of_birth = fields.Date(string="Date of Birth")
    deceased = fields.Boolean(string='Deceased')
    marital_status = fields.Selection([('s','Single'),('m','Married'),('w','Widowed'),('d','Divorced'),('x','Seperated')],string='Marital Status')
    blood_type = fields.Selection([('A', 'A'),('B', 'B'),('AB', 'AB'),('O', 'O')], string ="Blood Type")
    description = fields.Text(string="Description")
    doctor_id = fields.Many2one('doctor.record', string="Doctor")
    bill_ids = fields.One2many('bills.record','patient_id',string='Billing')
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('billing', 'Billing'),
            ('treated', 'Treated'),
            ('untreated', 'Untreated'),
            ('discharge', 'Discharge')
        ], default="new"
    )

    _sql_constraints = [
        ('check_height', 'CHECK( height >= 0.0 )',
         'The Height must be postive'),

        ('check_weight', 'CHECK(weight >= 0.0 )',
         'The Weight price must be postive'),
    ]

    _sql_constraints = [
        ('check_email', 'unique( email)',
         'The Email must be postive'),
    ]

    @api.constrains('contact_no')
    def _check_number(self):
        for record in self:
            # print(record.contact_no)
            if len(record.contact_no)<10:
                raise UserError("Contact number must be >10")
            else:
                return True
            
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            # print(record.email)
            validation = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
            if not re.match(validation,record.email):
                raise UserError("This Email is not valid")

    @api.depends('date','date_of_birth')
    def _compute_age(self):
        for record in self:
            record.age = relativedelta(record.date,record.date_of_birth).years

    def action_treated(self):
        for record in self:
            print(record.bill_ids.status)
            if record.bill_ids.status == "paid":
                record.state = "treated"
            else:
                raise UserError("First Pay the Bill")

    def action_untreated(self):
        for record in self:
            if record.state == "treated":
                raise UserError("patient is already treated")
            else:
                record.state = "untreated"
        return True

            
            
    



