# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):

    _inherit = 'res.partner'

    objectives = fields.Text(string='Objective', translate=True)
    workspace = fields.Text(string='Workspace', translate=True)    
    geographic_zone = fields.Many2many('res.country', 'iica_partner_country_rel', string='Geographic zones')
    cooperation_sectors = fields.Html('Cooperation sectors')
    #related_partners = fields.Many2many('res.partner', 'iica_partner_partner_rel', string='Related partners')
    iica_cooperation = fields.Html('IICA Cooperation')    