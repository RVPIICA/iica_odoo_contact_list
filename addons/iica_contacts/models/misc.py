from odoo import models, fields

class Area_Interest(models.Model):
    """Areas of interest for the contacts"""
    _name = 'iica_contacts.area_interest'
    _description = 'Areas of interest for IICA contacts'
    _order = 'name asc'

    name = fields.Char(string='Area', required=True, translate=True)
    description = fields.Text(string='Description')
    contact_ids = fields.Many2many('iica_contacts.contact', 'iica_contacts_contact_area_rel', string='Contacts')


class Topic_Interest(models.Model):
    """Topics of interest for the contacts"""
    _name = 'iica_contacts.topic_interest'
    _inherit = 'iica_contacts.area_interest'
    _description = 'Topics of interest for IICA contacts'

    name = fields.Char(string='Topic', required=True, translate=True)
    contact_ids = fields.Many2many('iica_contacts.contact', 'iica_contacts_contact_topic_rel', string='Contacts')

class Products_Interest(models.Model):
    """Distinct IICA products that a subscriber might want to receive"""
    _name = 'iica_contacts.products_interest'
    _inherit = 'iica_contacts.area_interest'
    _description = 'Products that a subscriber might want to receive'

    name = fields.Char(string='Product', required=True, translate=True)
    contact_ids = fields.Many2many('iica_contacts.contact', 'iica_contacts_contact_product_rel', string='Contacts')

class Additional_Products(models.Model):
    """Additional products for select IICA subscribers such as the press newsletter."""
    _name = 'iica_contacts.additional_products'
    _inherit = 'iica_contacts.area_interest'
    _description = 'Additional select IICA products the a subscriber will receive'

    name = fields.Char(string='Product', required=True, translate=True)
    short_desc = fields.Char(string='Short Description', translate=True)
    contact_ids = fields.Many2many('iica_contacts.contact', 'iica_contacts_contact_additional_products_rel', string='Contacts')


class Channels(models.Model):
    """Channels for the IICA journalists"""
    _name = 'iica_contacts.journalist_channels'
    _description = 'Channels for the IICA journalists'

    name = fields.Char(string='Channel name', required=True, translate=True)
    contacts = fields.Many2many('iica_contacts.contact', 'iica_contacts_journalist_channels_rel', string='Contacts')

class Topics(models.Model):
    """Topics for the IICA journalists"""
    _name = 'iica_contacts.journalist_topics'
    _description = 'Topics for the IICA journalists'

    name = fields.Char(string='Topic name', required=True, translate=True)
    contacts = fields.Many2many('iica_contacts.contact', 'iica_contacts_journalist_topic_rel', string='Contacts')

class Languages(models.Model):
    """Languages for the journalists"""
    _name = 'iica_contacts.journalist_languages'
    _description = 'Languages for the IICA journalists'

    name = fields.Char(string='Language name', required=True, translate=True)
    contacts = fields.Many2many('iica_contacts.contact', 'iica_contacts_journalist_language_rel', string='Contacts')

class Users(models.Model):
    """User fields"""
    _inherit = 'res.users'

    authorized_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')

class Countries(models.Model):
    """Countries"""
    _inherit = 'res.country'

    authorized_users_ids = fields.One2many('res.users', 'authorized_country_id')