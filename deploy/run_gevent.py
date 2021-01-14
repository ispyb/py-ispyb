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
import sys
from gevent.pywsgi import WSGIServer
from pyispyb import create_app

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if len(sys.argv) > 3:
    config_filename = sys.argv[1]
    run_mode = sys.argv[2]
    port = sys.argv[3]
else:
    config_filename = os.path.join(ROOT_DIR, "ispyb_core_config.yml")
    run_mode = "dev"
    port = 5000


app = create_app(config_filename, run_mode)
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
