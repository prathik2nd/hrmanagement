#-*- coding: utf-8 -*-

from odoo import models, fields, api


class hrmanagement(models.Model):
    _name = 'hrmanagement.hrmanagement'
    _description = 'hrmanagement.hrmanagement'

    name = fields.Char('Employee Name')
    address = fields.Text('Address')
    email = fields.Char('Email ID')
    phone = fields.Char('Phone No')
    quali = fields.Text('Qualification')

class salary(models.Model):
    _name = 'hrmanagement.salary'
    _description = 'hrmanagement.salary'

    name = fields.Many2one('hrmanagement.hrmanagement','Employee Name')
    bsal = fields.Char('Basic Salary')
    worktime = fields.Char('Work hours')
    ot = fields.Char('Overtime Rate')
    leavedays = fields.Text('Leave Days')


