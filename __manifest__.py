{
    'name': 'Warehouse Manager',
    'version': '1.0',
    'summary': 'Module for managing warehouse operations',
    'sequence': 10,
    'description': """
Warehouse Management Module
""",
    'author': 'Nguyen Duc Phat',
    'website': "http://www.nguyenducphat57@gmail.com",
    'category': 'Inventory',
    'depends': ['base', 'stock', 'website'],
    'data': [
        'views/my_custom_model_views.xml',
        'views/location_view.xml',
        'views/supplier_view.xml',
        'views/stock.xml',
        'views/dashboard_view.xml',
        'views/product_type_view.xml',
        'views/unit_of_measure_view.xml',
        'views/product_view.xml',
        'views/wms_menu.xml',
        'wizard/website_page.xml',
        'wizard/my_wizard.xml',
        'wizard/product_update_wizard.xml',
        'report/product_report.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'module-warehouse/static/src/css/dashboard.css',
        ],
        'web.assets_frontend': [
            'module-warehouse/static/src/css/custom_styles.css',  # Add your frontend CSS
        ],
        'data': [
            'security/ir.model.access.csv',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
