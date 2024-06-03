# -*- coding: utf-8 -*-
{
    "name": "purchase_dashboard",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",
    "author": "Billy Butcher",
    "website": "zephertech",
    "support": "billybutcher0004@gmail.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["purchase"],
    "data": [
        # "security/ir.model.access.csv",
        # "views/views.xml",
    ],
    'assets': {
        'web.assets_backend': [
            '/purchase_dashboard/static/src/views/purchase_dashboard.xml'
        ],
    },
    "images": [
        "static/description/icon.png",
    ],
}