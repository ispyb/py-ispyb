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

from tests.core.functional.data.get import test_data

def test_get(ispyb_core_app, ispyb_core_token):
    client = ispyb_core_app.test_client()
    headers = {"Authorization": "Bearer " + ispyb_core_token}

    for test_elem in test_data:
        test_route = ispyb_core_app.config["API_ROOT"] + test_elem['route']
        test_code = test_elem['code']

        response = client.get(test_route, headers=headers)
        res = response.json

        assert response.status_code == test_code, "[GET] %s " % (test_route)
        assert res, "[GET] %s No data returned" % (test_route)

    
