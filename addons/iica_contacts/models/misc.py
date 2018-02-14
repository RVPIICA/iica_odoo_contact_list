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
