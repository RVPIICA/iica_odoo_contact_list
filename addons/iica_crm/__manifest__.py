# -*- coding: utf-8 -*-
{
    'name': "IICA CRM",

    'summary': """An adaptation of the CRM module for the IICA requirements.""",

    'description': """
        An adaptation of the CRM module for the IICA requirements.
    """,

    'author': "IICA",
    'website': "http://iica.int",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'IICA Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/partner.xml',
    ],
}