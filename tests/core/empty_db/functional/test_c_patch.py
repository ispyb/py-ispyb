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
from tests.core.empty_db.functional.data.patch import test_data

# Need to fix test: empty database - nothing to delete
pytestmark = pytest.mark.skip


@pytest.mark.parametrize("test_elem", test_data)
def test_patch(ispyb_app, manager_token, test_elem):
    client = ispyb_app.test_client()
    headers = {"Authorization": "Bearer " + manager_token}

    test_route = ispyb_app.config["API_ROOT"] + test_elem["route"]
    test_code = test_elem["code"]
    test_id = test_elem["id"]
    test_patch = test_elem["patch"]

    response = client.get(test_route, headers=headers)

    item_id = response.json["data"]["rows"][-1][test_id]
    patch_route = (
        test_route
        + "/"
        + str(item_id)
    )
    response = client.patch(patch_route, json=test_patch, headers=headers)
    assert response.status_code == test_code, "[PATCH] %s " % (patch_route)
