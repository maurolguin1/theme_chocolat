# -*- coding: utf-8 -*-

{
  'name':'Chocolaterie theme',
  'description': 'Custom webdesing for Chocolaterie.',
  'version':'1.0',
  'author':'appy.solutions',

  'data': [
    'views/templates.xml',
  	'views/layout.xml',
  	'views/page.xml',
    'views/assets.xml',
    'views/res_company_view.xml',
    'views/product_public_views.xml',
    'views/product_views.xml',
    'views/res_partner_bank_view.xml',
    'views/account_invoice_view.xml',
    'views/sale_view.xml',
    'views/stock_view.xml',
    'views/purchasse_details.xml',
    'views/payment_view.xml',
    'views/res_config_view.xml',
    'views/website_crm_template.xml',

    'report/report_header_view.xml',
    'report/report_invoice_view.xml',
    'report/report_footer_view.xml',
    'report/report_saleorder_view.xml',
    'report/report_delivery.xml',

    'data/mail_template_data.xml',
    'data/mail_template_stock_data.xml',
  	],

  'category': 'Theme/Creative',
  'depends': ['website', 'sale', 'website_sale', 'product','stock'],

  'application': True,
  'installable': True,
  'auto_install': False,
}