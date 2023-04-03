# patient details 

from odoo import models,fields,api

class Bills(models.Model):
    _name = "bills.record"
    _description = "bills Details"

    bill_number = fields.Integer(string="Bill Number",required=True)
    patient_id = fields.Many2one('patient.record',string='Patient Name')
    number_of_days = fields.Integer(string="Number Of Days")
    doctor_id = fields.Many2one('doctor.record',string='Doctor Name')
    doctor_fees = fields.Float(related = "doctor_id.fees",string="Doctor Fees") 
    bed_type = fields.Many2one('bed.record',string="Bed Type")
    bed_price = fields.Float(related = "bed_type.price",string="Bed Price")
    total_price = fields.Float(compute='compute_total_price', string='Total Price')
    status = fields.Selection(
        selection=[
            ('paid', 'Paid'),
            ('due', 'Due'),
        ]
    )
    total_bill = fields.Float(string="Total Bill",compute="compute_total_bill")

    @api.depends('bed_price','number_of_days')
    def compute_total_price(self):
        for record in self:
            record.total_price = record.bed_price * record.number_of_days

    

    

