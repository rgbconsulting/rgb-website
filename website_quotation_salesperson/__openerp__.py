# -*- coding: utf-8 -*-
##############################################################################
#
#   Website Salesperson
#   Copyright 2016 RGB Consulting, SL
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Website Salesperson",
    'version': '1.0',
    'depends': ['website_sale'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'Website',
    'summary': """Saleperson for website sales""",
    'description': """
Website Salesperson
===================
This module allows to configure the saleperson to be used in
quotations generated from the Webshop.
    """,

    'data': [
        'views/website_config.xml',
    ],

    'demo': [
    ],
}
