# -*- coding: utf-8 -*-
{
    'name': "IICA Contacts and Mailing",

    'summary': """
        Manage IICA contacts and use the mass mailing module to send them mass emails.""",

    'description': """
        Manage the IICA contact list with custom fields and allow each user to subscribe to certain newsletter
        as well as allowing mass emails to be send.
    """,

    'author': "Randall Vargas Padilla - UTIC",
    'website': "http://www.iica.int",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'IICA Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mass_mailing', 'website'],

    # always loaded
    'data': [
        'views/contact.xml',
        'views/mailing.xml',
        'views/registration_templates.xml',
        'views/snippets_themes.xml',
        'views/themes_templates.xml',
        'views/editor_field_html.xml',
        #Defaul module data
        'default_data/areas.xml',
        'default_data/topics.xml',
        'default_data/products.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
