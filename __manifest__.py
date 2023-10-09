# -*- coding: utf-8 -*-
{
    'name': "Mattermost Custom Webhook For Stock",
    'summary': 
    """Configure to trigger incoming webhooks bot for stock
    """,

    'description': 
    """
       Configure to trigger incoming webhooks bot for stock
    """,

    'author': "Agustian Suharono",
    'website': "bernieiwnl@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'stock',
    'version': '1.0',
    'application' : True,
    'installable' : True,

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}