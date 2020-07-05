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


from flask import current_app
from requests import get, post


__license__ = "LGPLv3+"


def get_ispyb_resource(service_name, path):
    root_url = current_app.config["SERVICE_CONNECTOR"][service_name]
    headers = {"Authorization": "Bearer %s" % current_app.config["MASTER_TOKEN"]}
    response = get(root_url + path, headers=headers)
    data = response.json()
    return data, response.status_code
