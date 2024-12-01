{
    'name': 'POS Product Location',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Display product location in POS product popup',
    'description': """
        This module adds the product's location information to the product popup in Point of Sale.
    """,
    'depends': ['point_of_sale', 'stock'],  # Added stock dependency
    'assets': {
        'point_of_sale.assets': [
            "/point_of_sale_location/static/src/js/models.js",
            "/point_of_sale_location/static/src/xml/pos_location_popup.xml",
            "/point_of_sale_location/static/src/scss/pos_location.scss",
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}