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
from requests import ConnectionError


__license__ = "LGPLv3+"


def is_resource_available(service_name):
    status_code = 400
    data = "ISPyB service %s is not available" % service_name
    #000try:
    if True:
        headers = {
            "Authorization": "Bearer %s" % current_app.config["MASTER_TOKEN"],
            "Host": service_name}
        response = get(current_app.config["API_GATEWAY_URL"] + "/schemas/available_names", headers=headers)
        data = response.json()
        status_code = response.status_code
    #except ConnectionError:
    #    pass
    return status_code, data


def get_ispyb_resource(service_name, path):
    status_code, data = is_resource_available("core")
    if status_code != 200:
        return status_code, data
    else:
        headers = {
            "Authorization": "Bearer %s" % current_app.config["MASTER_TOKEN"],
            "Host": service_name}
        response = get(
            current_app.config["API_GATEWAY_URL"] + path,
            headers=headers)
        data = response.json()
        return response.status_code, data
