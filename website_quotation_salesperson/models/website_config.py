# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import fields, models, api
from openerp import SUPERUSER_ID


class Website(models.Model):
    _inherit = 'website'

    salesperson_id = fields.Many2one(comodel_name='res.users', string='Salesperson')

    @api.multi
    def sale_get_order(self, force_create=False, code=None, update_pricelist=None, context=None):
        res = super(Website, self).sale_get_order(
            force_create=force_create,
            code=code,
            update_pricelist=update_pricelist,
            context=context)
        if res:
            if res.user_id.id == SUPERUSER_ID:
                website = self.browse(self.id)
                res.write({'user_id': website.salesperson_id.id})
        return res


class WebsiteConfig(models.TransientModel):
    _inherit = 'website.config.settings'

    salesperson = fields.Many2one(related='website_id.salesperson_id', comodel_name='res.users', string='Salesperson')
