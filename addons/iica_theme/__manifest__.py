# -*- coding: utf-8 -*-
{
    'name': "IICA Responsive Theme",

    'summary': "IICA Responsive theme developed for the CRM.",

    'description': """
        IICA Responsive theme developed for the CRM.
    """,

    'author': "IICA",
    'website': "http://iica.int",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'IICA Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web_responsive',],

    # always loaded
    'data': [
        'views/assets.xml',
    ],
}