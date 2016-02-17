# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import http
from openerp.http import request
from cStringIO import StringIO


class Favicon(http.Controller):
    @http.route("/favicon.ico", auth="public")
    def get_favicon(self):
        web_settings = request.env['website.config.settings'].sudo().search([])

        if web_settings:
            favicon = StringIO(str(web_settings[-1].favicon).decode('base64'))
            write_date = web_settings[-1].write_date

        return http.send_file(favicon, filename='favicon.ico', mtime=write_date)
