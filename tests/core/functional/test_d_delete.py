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

import pytest
from tests.core.functional.data.delete import test_data

# Need to fix test: empty database - nothing to patch
pytestmark = pytest.mark.skip


def test_delete(ispyb_app, manager_token):
    client = ispyb_app.test_client()
    headers = {"Authorization": "Bearer " + manager_token}

    for test_elem in test_data:
        test_route = ispyb_app.config["API_ROOT"] + test_elem["route"]
        test_code = test_elem["code"]
        test_id = test_elem["id"]

        response = client.get(test_route, headers=headers)

        item_id = response.json["data"]["rows"][-1][test_id]
        del_route = (
            test_route
            + "/"
            + str(item_id)
        )
        response = client.delete(del_route, headers=headers)
        assert response.status_code == test_code, "[DELETE] %s " % (del_route)
