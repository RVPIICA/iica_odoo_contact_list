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
    __contact_type = [('0', 'Normal Newsletter'), ('1', 'Journalist')]

    #Field definitions
    name = fields.Char(string='Full Name', required=True)
    company = fields.Char(string='Institution / Organization', index=True)
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', required=True)
    sector = fields.Selection(selection=__sectors, string='Sector')
    language = fields.Selection(selection=__language_list, string='Language')
    email = fields.Char(string='Email', required=True)
    email_formatted = fields.Char(
        'Formatted Email', compute='_compute_email_formatted',
        help='Format email address "Name <email@domain>"')
    phone = fields.Char(string='Phone number')
    radio = fields.Boolean(string='Works in radio', help='This contact works in a radio station', default=False)
    opt_out = fields.Boolean(string='Opt Out', help='The contact has chosen not to receive mails anymore from this list')
    unsubscription_date = fields.Datetime(string='Unsubscription Date')
    area_interest_ids = fields.Many2many('iica_contacts.area_interest', 'iica_contacts_contact_area_rel', string='Areas of interest')
    topic_interest_ids = fields.Many2many('iica_contacts.topic_interest', 'iica_contacts_contact_topic_rel', string='Topics of interest')
    product_interest_ids = fields.Many2many('iica_contacts.products_interest', 'iica_contacts_contact_product_rel', string='Products of interest')
    additional_products_ids = fields.Many2many('iica_contacts.additional_products', 'iica_contacts_contact_additional_products_rel', string='Additional products')
    contact_type = fields.Selection(selection=__contact_type, string='Contact type', required=True, default='0')
    message_bounce = fields.Integer(string='Bounce', help='Counter of the number of bounced emails for this contact.', default='0')

    #Journalist specific fields
    #medium = company, change name in UI
    #phone = work phone, added extension field in case needed
    position = fields.Char(string='Job position')
    extension = fields.Char(string='Phone extension')
    mobile_phone = fields.Char(string='Mobile phone')
    address = fields.Text(string='Address')
    j_channel_ids = fields.Many2many('iica_contacts.journalist_channels', 'iica_contacts_journalist_channels_rel', string='Channels')
    j_topic_ids = fields.Many2many('iica_contacts.journalist_topics', 'iica_contacts_journalist_topic_rel', string='Topics')
    j_lang_ids = fields.Many2many('iica_contacts.journalist_languages', 'iica_contacts_journalist_language_rel', string='Languages')
    
    #Country journalist specific fields.
    visible_in_filter = fields.Boolean(compute='_compute_visible_in_filter', string='Visible in filter', store=False, search='_search_visible_in_filter')

    @api.depends('name', 'email')
    def _compute_email_formatted(self):
        for contact in self:
            contact.email_formatted = formataddr((contact.name, contact.email))

    @api.depends('country_id')
    def _compute_visible_in_filter(self):
        for contact in self:
            if (contact.country_id == self.env.user.authorized_country_id):
                contact.visible_in_filter = True

    @api.multi
    def _search_visible_in_filter(self, operator, value):
        records = self.search([]).filtered(lambda x:x.visible_in_filter is True)
        if records:
            return [('id', 'in', [x.id for x in records])]                 

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
