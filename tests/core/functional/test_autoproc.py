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


from tests.core.data import test_proposal


def test_get(ispyb_core_app, ispyb_core_token):
    client = ispyb_core_app.test_client()
    route_root = ispyb_core_app.config["API_ROOT"]
    
    rel_routes = [
        "/autoproc",
        "/autoproc/programs",
        "/autoproc/programs/attachments",
    ]

    headers = {"Authorization": "Bearer " + ispyb_core_token}
    for rel_route in rel_routes:
        print(route_root + rel_route)
        response = client.get(route_root + rel_route, headers=headers)
        data = response.json
        assert response.status_code == 200, "Wrong status code"
        assert len(data["data"]["rows"]) > 0, "No data returned"

def test_put(ispyb_core_app, ispyb_core_token):
    client = ispyb_core_app.test_client()
    route_root = ispyb_core_app.config["API_ROOT"] + "/proposals"
    ispyb_core_token = "MasterToken"

    # TODO Insert all data before posting a new proposal
    return
