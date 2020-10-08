# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
     _name = 'openacademy.course'
     _description = "OpenAcademy Courses"

     name = fields.Char(string="Title", required=True)
     description = fields.Text(string="Full Description")
     about = fields.Text("About this class")



class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    
    

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
