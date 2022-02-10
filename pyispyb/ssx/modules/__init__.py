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


import os
import logging
from importlib import import_module

__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


def init_app(app, **kwargs):
    """Inits extensions.

    Args:
        app (Flask app): [description]
    """

    for module_name in os.listdir(os.path.dirname(__file__)):
        if not module_name.startswith("__") and module_name.endswith(".py"):
            module = import_module(".%s" % module_name[:-3], package=__name__)
            if hasattr(module, "init_app"):
                module.init_app(app, **kwargs)
