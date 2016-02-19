# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import fields, models, _


class Website(models.Model):
    _inherit = 'website'

    favicon = fields.Binary("Favicon ico")


class WebsiteConfig(models.TransientModel):
    _inherit = 'website.config.settings'

    favicon = fields.Binary("Favicon ico", related="website_id.favicon")
