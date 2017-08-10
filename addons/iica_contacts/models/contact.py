# -*- coding: utf-8 -*-

from email.utils import formataddr
from odoo import models, fields, api

class Contact(models.Model):
    """Model for the IICA contacts, inherits and modifies the partner model
    adding new fields.
        - Ésta clase hereda de mail.thread para realizar las gestiones requeridas para el envío de correos.
    """
    _inherit = 'mail.thread'
    _name = 'iica_contacts.contact'

    #Lists of static values
    __language_list = [('1', 'Spanish'), ('2', 'English'), ('3', 'Both')]
    __sectors = [('1', 'Public'), ('2', 'Private'), ('3', 'ONG'), ('4', 'International organization'), ('5', 'Financial'), ('6', 'Other')]

    #Field definitions
    name = fields.Char(string='Full Name', required=True)
    company = fields.Char(string='Place of work', index=True)
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', required=True)
    sector = fields.Selection(selection=__sectors, string='Sector')
    language = fields.Selection(selection=__language_list, string='Language', required=True)
    email = fields.Char(string='Email', required=True)
    email_formatted = fields.Char(
        'Formatted Email', compute='_compute_email_formatted',
        help='Format email address "Name <email@domain>"')
    phone = fields.Char(string='Phone number')
    opt_out = fields.Boolean(string='Opt Out', help='The contact has chosen not to receive mails anymore from this list')
    unsubscription_date = fields.Datetime(string='Unsubscription Date')
    area_interest_ids = fields.Many2many('iica_contacts.area_interest', 'iica_contacts_contact_area_rel', string='Areas of interest')
    topic_interest_ids = fields.Many2many('iica_contacts.topic_interest', 'iica_contacts_contact_topic_rel', string='Topics of interest')
    product_interest_ids = fields.Many2many('iica_contacts.products_interest', 'iica_contacts_contact_product_rel', string='Products of interest')

    # @api.depends('first_name', 'last_name')
    # def _compute_full_name(self):
    #     for contact in self:
    #         if not contact.last_name:
    #             contact.name = contact.first_name
    #         else:
    #             contact.name = contact.first_name + ' ' + contact.last_name

    @api.depends('name', 'email')
    def _compute_email_formatted(self):
        for contact in self:
            contact.email_formatted = formataddr((contact.name, contact.email))


    @api.multi
    def message_get_default_recipients(self):
        return dict((record.id, {'partner_ids': [], 'email_to': record.email, 'email_cc': False}) for record in self)

    @api.model
    def create(self, vals):
        if 'opt_out' in vals:
            vals['unsubscription_date'] = vals['opt_out'] and fields.Datetime.now()
        return super(Contact, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'opt_out' in vals:
            vals['unsubscription_date'] = vals['opt_out'] and fields.Datetime.now()
        return super(Contact, self).write(vals)

class Message(models.Model):
    """ Mail Message updated to avoid """
    _inherit = 'mail.message'

    @api.model
    def _get_default_from(self):
        return formataddr(("IICA", "comunicacion.social@iica.int"))
