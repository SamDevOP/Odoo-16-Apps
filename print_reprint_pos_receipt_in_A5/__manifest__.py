{
    "name": "Reprint POS order receipt in A4, A5",
    "category": " Point of Sale",
    "author": "Sam Dev",
    "sequence": 1,
    "summary": """Reprint POS order receipt""",
    "website": "samkinyanjui101@gmail.com",
    "version": "",
    "description": """Reprint POS order receipt in A4, A5""",
    "license": "LGPL-3",
    "support": "samkinyanjui101@gmail.com",
    "price": "5100",
    "currency:": "KES",
    "images": ["static/description/icon.png"],
    # any module necessary for this one to work correctly
    "depends": ['point_of_sale'],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        'reports/report_template.xml',
        'reports/reports.xml'
    ],
    
    # only loaded in demonstration mode
    "demo": [],
    'application': True,
    'license': 'LGPL-3',
}
