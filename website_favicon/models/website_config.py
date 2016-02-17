# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import fields, models, _


class WebsiteConfig(models.Model):
    _inherit = 'website.config.settings'

    favicon = fields.Binary("Favicon ico")
