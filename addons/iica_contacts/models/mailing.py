# -*- coding: utf-8 -*-

from datetime import datetime
import random

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval
from odoo.tools.translate import html_translate

class MassMailing(models.Model):
    """MassMailing extends the core mass mailing module to interact with the IICA contacts."""

    _inherit = 'mail.mass_mailing'

    #Lists of static values
    __language_list = [('1', 'Spanish'), ('2', 'English')]

    def _get_mailing_model(self):
        res = []
        res.append(('iica_contacts.contact', _('Areas of Interest')))
        return res

    _mailing_model = lambda self: self._get_mailing_model()

    mailing_model = fields.Selection(selection=_mailing_model, string='Recipients Model', required=True, default='iica_contacts.contact')
    contact_ids = fields.Many2many('iica_contacts.contact', 'iica_contacts_contact_mailing_rel', string='Contacs')
    language = fields.Selection(selection=__language_list, string='Language')
    area_interest_ids = fields.Many2many('iica_contacts.area_interest', 'iica_contacts_area_interest_mailing_rel', string='Areas of interes')
    topic_interest_ids = fields.Many2many('iica_contacts.topic_interest', 'iica_contacts_topic_interest_mailing_rel', string='Topics of interes')
    product_interest_ids = fields.Many2many('iica_contacts.products_interest', 'iica_contacts_products_interest_mailing_rel', string='Products of interes')

    #Fills the domain filter with the required areas and topics of interest.
    @api.onchange('language', 'area_interest_ids', 'topic_interest_ids', 'product_interest_ids')
    def _onchange_interest_ids(self):
        _language = "('language', '=', %s)," % self.language
        _areas_interest = "('area_interest_ids', 'in', %s), " % self.area_interest_ids.ids
        _topics_interest = "('topic_interest_ids', 'in', %s), " % self.topic_interest_ids.ids
        _products_interest = "('product_interest_ids', 'in', %s)" % self.product_interest_ids.ids


        self.mailing_domain = "['&', '&', ('opt_out', '=', False), "+ _language +" '|', " + _areas_interest + " '|', " + _topics_interest + _products_interest + "]"
        #self.mailing_domain = "[('opt_out', '=', False), '|', " + _areas_interest + _topics_interest + _products_interest +"]"
        #self.mailing_domain = "[('area_interest_ids', 'in', %s), ('opt_out', '=', False)]" % self.area_interest_ids.ids
