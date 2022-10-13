#
{
    'name': 'RealEstate',
    'category': 'Website/Real Estate',
    'sequence': 1,
    'author': 'Mai Thành Duy An',
    'summary': 'Real Estate',
    'website': 'https://demosoft/app/resl-estate',
    'version': '1.0',
    'description': "",
    'installable': True,
    'application': True,
    'depend': ['base', 'product'],
    'data': [
        'views/assets_view.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [],
    'css': ['static/src/css/assets.css'],
    'assets': {},
    'license': 'LGPL-3',
}
