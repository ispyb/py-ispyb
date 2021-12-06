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


from tests.core.functional.data.post import test_data


def test_post(ispyb_core_app, ispyb_core_token):
    client = ispyb_core_app.test_client()
    headers = {"Authorization": "bearer " + ispyb_core_token}

    prev = {}
    for test_elem in test_data:

        test_route = ispyb_core_app.config["API_ROOT"] + test_elem['route']
        test_json = test_elem['json'](prev)
        test_name = test_elem['name']
        response = client.post(test_route, json=test_json, headers=headers)

        assert response.status_code == 200, "[POST] %s failed" % test_route
        prev[test_name] = response.json
