# -*- coding: utf-8 -*-
##############################################################################
#
#   RGB Bootswatch Themes
#   Copyright 2015 RGB Consulting, SL
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
    'name': 'RGB Bootswatch Themes',
    'version': '1.0',
    'depends': ['website'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'Themes',
    'summary': 'RGB Bootswatch Themes',
    'description': """
    Adds new themes of bootswatch in the default theme selection:
        Darkly, Lumen, Paper, Sandstone and Superhero
    """,
    'data': [
        'views/bootswatch_view.xml',
    ],
    'installable': True,
}