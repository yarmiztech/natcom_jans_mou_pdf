# -*- coding: utf-8 -*-
{
    'name': "Natcom PDF MOU",
    'author':
        'Enzapps',
    'summary': """
This module is for creating api for Invoices.
""",

    'description': """
        This module consist of track page of cargo which extend the website.
        It consist of 2 tabs Brief and History
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['sale','purchase','base','account','natcom_jan_pdf','web'],
    "images": ['static/description/icon.png'],
    'data': [
        'reports/reports.xml',
         'reports/reports_no_new_view.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
