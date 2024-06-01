# -*- coding: utf-8 -*-
{
    "name": "payment_report",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",
    "author": "Billy Butcher",
    "website": "zephertech",
    "support": "billybutcher0004@gmail.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["sale","account"],
    "data": [
        "security/ir.model.access.csv",
        "views/report_template.xml",
        "views/report_action.xml",
        "views/wizard_views.xml",
    ],
    "images": [
        "static/description/icon.png",
    ],
}
