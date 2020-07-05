# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


import logging


__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


def init_app(app, **kwargs):
    from importlib import import_module

    for module_name in app.config["MODULES"]:
        log.debug("Loading module %s" % module_name)
        import_module(".%s" % module_name, package=__name__).init_app(app, **kwargs)

    """
    for module_name in app.config["ENABLED_DB_MODULES"]:
        import_module(".%s" % module_name, package=__name__)
    """
