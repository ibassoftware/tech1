from odoo import fields, models, api


class IBASCrmLead(models.Model):

    _inherit = 'crm.lead'

    partner_id = fields.Many2one('res.partner', string='Customer', tracking=10, index=True,
        domain="['|', ('user_id', '=', uid), ('create_uid', '=', uid)]", help="Linked partner (optional). Usually created when converting the lead. You can find a partner by its Name, TIN, Email or Internal Reference.")