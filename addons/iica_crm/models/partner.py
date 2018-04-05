# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):

    _inherit = 'res.partner'

    objective = fields.Text(string='Objective', translate=True)   
    working_countries = fields.Many2many('res.country', 'iica_partner_country_rel', string='Working countries')
    working_geographic_zones = fields.Many2many('iica_crm.geographic_regions', 'iica_partner_geographic_zone_rel', string='Geographic zones')
    main_contact = fields.Many2one('res.partner', ondelete='set null',string='Main contact', index=True)    
    national_counterparts = fields.Many2many('res.partner', 'iica_partner_counterpart_rel', string='Counterparts', column1='national_counterparts', column2='national_counterpart_of')
    national_counterpart_of = fields.Many2many('res.partner', 'iica_partner_counterpart_rel', string='Counterparts', column1='national_counterpart_of', column2='national_counterparts')
    instruments_cooperation = fields.One2many('iica_crm.instrument_cooperation', 'partners_rel',string='Instrument of Cooperation')
    lines_cooperation = fields.One2many('iica_crm.line_cooperation', 'partners_rel', string='Lines of cooperation')
    lines_work = fields.One2many('iica_crm.line_work', 'partners_rel', string='Lines of work')
    recent_projects = fields.One2many('iica_crm.project', 'partners_rel', string='Projects')
    internships = fields.One2many('iica_crm.internship', 'partners_rel', string='Internships')
    twitter = fields.Char(string='Twitter')
    linked_in = fields.Char(string='Linked In')
    facebook = fields.Char(string='Facebook')
    languages = fields.Many2many('res.lang', 'iica_partner_lang_rel', string='Languages')
    additional_info = fields.Html(string='Additional info')
    is_company = fields.Boolean(string='Is a Company', default=True, help="Check if the contact is a company, otherwise it is a person")
    