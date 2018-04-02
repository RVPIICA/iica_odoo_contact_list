# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class Geographic_Regions(models.Model):

    _name = 'iica_crm.geographic_regions'
    _description = 'Geographic region for the partner'

    _order ='name desc'

    name = fields.Char(string='Name', required=True, translate=True)
    partners = fields.Many2many('res.partner', 'iica_partner_country_rel', string='Partners')


class Counterpart(models.Model):

    _name = 'iica_crm.counterpart'
    _description = 'Counterpart'

    _order = 'name desc'

    name = fields.Char(string='Name', required=True)


class Line_Cooperation(models.Model):

    _name = 'iica_crm.line_cooperation'
    _description = 'Lines of cooperation'

    _order = 'name desc'

    name = fields.Char(string='Name', required=True)
    partners_rel = fields.Many2one('res.partner', string='Partners')

class Instrument_Cooperation(models.Model):

    _name = 'iica_crm.instrument_cooperation'
    _description = 'Instrument of Cooperation'

    _order = 'name desc'

    name = fields.Char(string='Name', required=True, translate=True)
    uploaded_file = fields.Binary(string='File')
    uploaded_file_name = fields.Char(string='Fila Name')    
    date_from = fields.Date(string='Starting date', default=fields.Date.context_today)
    date_to = fields.Date(string='Ending date')
    partners_rel = fields.Many2one('res.partner', string='Partners')

class Line_Work(models.Model):

    _name = 'iica_crm.line_work'
    _description = 'Lines of work'

    _order = 'name desc'

    name = fields.Char(string='Name', required=True)
    partners_rel = fields.Many2one('res.partner', string='Partners')
    
class IICA_Project(models.Model):

    @api.model
    def _get_user_currency(self):
        currency_id = self.env['res.users'].browse(self._uid).company_id.currency_id
        return currency_id or self._get_euro()

    _name = 'iica_crm.project'
    _description = 'Proyect'

    _order = 'name desc'

    name = fields.Char(string='Name', required=True)
    year = fields.Selection([(num, str(num)) for num in range(1980, (datetime.datetime.today().year)+5 )], default=datetime.datetime.today().year, string='Proyect year')
    funds = fields.Float(string='Funds')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self._get_user_currency())
    partners_rel = fields.Many2one('res.partner', string='Partners')
        

class Internship(models.Model):

    _name = 'iica_crm.internship'
    _description = 'Internship'

    _order = 'name desc'

    name = fields.Char(string='Name', required=True)
    year = fields.Selection([(num, str(num)) for num in range(1980, (datetime.datetime.today().year)+5 )], default=datetime.datetime.today().year, string='Proyect year')
    institution = fields.Many2one('iica_crm.university', string='University')
    university = fields.Many2one('iica_crm.institution', ondelete='set null', string='Institution', index=True)
    partners_rel = fields.Many2one('res.partner', string='Partners')

class Language(models.Model):

    _name = 'iica_crm.language'
    _description = 'Language'

    _order = 'name desc'

    name = fields.Char(string='Name', required=True)

class University(models.Model):

    _name = 'iica_crm.university'
    _description = 'University'

    _order = 'name desc'

    name = fields.Char(string='name', required=True)

class Institution(models.Model):

    _name = 'iica_crm.institution'
    _description = 'Institution'

    _order = 'name desc'

    name = fields.Char(string='name', required=True)