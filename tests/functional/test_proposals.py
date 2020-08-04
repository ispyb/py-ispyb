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


import json

from tests.data import test_proposal


def test_get(ispyb_core_app, ispyb_core_token):
    client = ispyb_core_app.test_client()
    route_root = ispyb_core_app.config["API_ROOT"] + "/proposals"

    headers = {"Authorization": "Bearer " + ispyb_core_token}
    response = client.get(route_root, headers=headers)
    data = response.json
    assert response.status_code == 200, "Wrong status code"
    assert len(data["rows"]) > 0, "No proposal returned"

    proposal_id = data["rows"][0]["proposalId"]
    path = route_root + "/" + str(proposal_id)
    response = client.get(path, headers=headers)
    assert response.status_code == 200, "Wrong status code"

    response = client.get(route_root + "?offset=1&limit=1", headers=headers)
    assert response.status_code == 200, "Wrong status code"

    path = route_root + "/params?proposalType=MX"
    response = client.get(path, headers=headers)
    assert response.status_code == 200, "Wrong status code"


def test_put(ispyb_core_app, ispyb_core_token):
    client = ispyb_core_app.test_client()
    route_root = ispyb_core_app.config["API_ROOT"] + "/proposals"

    headers = {"Authorization": "Bearer " + ispyb_core_token}
    response = client.post(route_root, data=test_proposal, headers=headers)

    assert response.status_code == 200, "Wrong status code"
