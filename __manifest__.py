# -*- coding: utf-8 -*-
{
    'name': "Leonix Custom VietNam State Module",

    'summary': """
        Custom data VN State by Leonix""",

    'description': """
        This module provides custom functionalities developed by Leonix to enhance Odoo features""",

    'author': "Leonix",
    'website': "http://leonix.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '18.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/update_vn_states.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        '',
    ],
    'license': 'OPL-1',
    'post_init_hook': 'create_vn_states',
}