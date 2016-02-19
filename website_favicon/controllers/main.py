# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import http
from openerp.http import request
from cStringIO import StringIO
from werkzeug.wrappers import Response


class Favicon(http.Controller):
    @http.route(["/favicon.png", "/favicon.ico",], auth="public")
    def get_favicon(self):
        hostname = request.httprequest.environ.get('HTTP_HOST', '').split(':')[0]
        website = request.env['website'].search([('name', '=', hostname)])
        if not website:
            website = request.env['website'].search([], limit=1)

        if website and website[0].favicon:
            try:
                favicon = StringIO(str(website[0].favicon).decode('base64'))
                write_date = website[0].write_date
                return http.send_file(favicon, filename='favicon.ico', mtime=write_date)
            except Exception:
                pass
        return request.env['website']._image_placeholder(Response())
