from odoo import models, fields, _
from odoo.exceptions import UserError


class PaymentReportWizard(models.TransientModel):
    _name = "payment.report.wizard"
    _description = "payment.report.wizard"

    date_start = fields.Date("From")
    date_end = fields.Date("To")

    def print_report(self):
        if self.date_start > self.date_end:
            raise UserError(_("Enter a valid date range...!"))
        data = {
            "ids": self.ids,
            "model": self._name,
            "form": {
                "date_start": self.date_start,
                "date_end": self.date_end,
            },
        }
        return self.env.ref(
            "payment_report.action_report_payment_report"
        ).report_action(self, data=data, config=False)
