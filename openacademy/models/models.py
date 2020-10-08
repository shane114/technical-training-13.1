# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
     _name = 'openacademy.course'
     _description = "OpenAcademy Courses"

     name = fields.Char(string="Title", required=True)
     description = fields.Text(string="Full Description")
     about = fields.Text("About this class")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
