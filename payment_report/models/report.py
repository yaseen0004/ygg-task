from odoo import models, api, _


class ReportPayment_report(models.AbstractModel):
    _name = "report.payment_report.customer_payment_report"

    @api.model
    def _get_report_values(self, docids, data):
        date_start = data["form"]["date_start"]
        date_end = data["form"]["date_end"]
        self.env.cr.execute(
            """
            SELECT
                rp.name,
                min(so.create_date),
                count(so.id),
                sum(so.amount_total),
                sum(ap.amount) as paid
            FROM
                sale_order so
                JOIN res_partner rp ON rp.id = so.partner_id
                LEFT JOIN account_payment ap ON ap.partner_id = so.partner_id
            WHERE
                so.state IN ('sale', 'done')
                AND so.create_date >= %s
                AND so.create_date <= %s
            GROUP BY
                rp.name
            """,
            [date_start, date_end],
        )
        vals = self.env.cr.fetchall()
        return {"vals": vals}
