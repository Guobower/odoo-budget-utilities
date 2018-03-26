# -*- coding: utf-8 -*-
{
    'name': "Budget Utilities",
    'version': '11.0.0.1',
    'summary': 'Budget Utilities Module',
    'sequence': 1,
    'description': """
Utilities
==============================
- record_lock_mixin - abstractModelMixin for locking a record
- num_to_shorthand - function converting number to shorthand (eg. 1000 -> 1K)
- choices_tuple - create a tuple of pairs with a given list
- odoo_to_pandas_list - odoo query to panda list
- int_to_roman - convert integer to roman numeral
    """,
    'category': 'TBPC Budget',
    'website': "https://github.com/mpdevilleres",
    'author': "Marc Philippe de Villeres",
    'depends': [
        'base',
    ],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
