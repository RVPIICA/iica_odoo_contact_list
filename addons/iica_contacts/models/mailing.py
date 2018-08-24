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
    __language_list = [('1', 'Spanish'), ('2', 'English'), ('3', 'Both')]
    __newsletter_types = [('1', 'Normal'), ('2', 'Journalists')]

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
    additional_products_ids = fields.Many2many('iica_contacts.additional_products', 'iica_contacts_additional_products_mailing_rel', string='Additional products')
    languages_ids = fields.Many2many('iica_contacts.journalist_languages', 'iica_contacts_languages_mailing_rel', string='Languages')
    country_ids = fields.Many2many('res.country', 'iica_contacts_country_mailing_rel', string='Countries', default=lambda self: self._get_default_country())
    newsletter_type = fields.Selection(selection=__newsletter_types, string='Type', default='1', required=True)

    def _get_default_country(self):
        return self.env.user.authorized_country_id

    #Fills the domain filter with the required areas and topics of interest.
    @api.onchange('language', 'area_interest_ids', 'topic_interest_ids', 'product_interest_ids', 'additional_products_ids', 'country_ids', 'languages_ids', 'newsletter_type')
    def _onchange_interest_ids(self):
        _opt_out = "('opt_out', '=', False),"
        if(self.newsletter_type == '1'): #Normal newsletter            
            _contact_type = "('contact_type', '=', '0'),"
            _language = "('language', 'in', (%s, 3))," % self.language
            _areas_interest = "('area_interest_ids', 'in', %s), " % self.area_interest_ids.ids
            _topics_interest = "('topic_interest_ids', 'in', %s), " % self.topic_interest_ids.ids
            _products_interest = "('product_interest_ids', 'in', %s)," % self.product_interest_ids.ids
            _additional_products = "('additional_products_ids', 'in', %s)" % self.additional_products_ids.ids

            #self.mailing_domain = "['&', '&'," + _opt_out +  _language + "'|', '|', " + _areas_interest + _topics_interest + "'|'," + _products_interest + _additional_products +"]"
            self.mailing_domain = "['&', '&'," + _opt_out +  _language + "'&', " + _contact_type + "  '|', '|', " + _areas_interest + _topics_interest + "'|'," + _products_interest + _additional_products +"]"

        elif(self.newsletter_type == '2'): #Journalist newsletter
            _contact_type = "('contact_type', '=', '1'),"
            _countries = "('country_id', 'in', %s), " % self.country_ids.ids
            _languages = "('j_lang_ids', 'in', %s) " % self.languages_ids.ids

            self.mailing_domain = "['&', '&', " + _opt_out + _contact_type + " '&', " + _countries + _languages + "]"