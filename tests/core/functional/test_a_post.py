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


from tests.core import data


def test_post(ispyb_core_app, ispyb_core_token):
    client = ispyb_core_app.test_client()
    headers = {"Authorization": "Bearer " + ispyb_core_token}
    
    route = ispyb_core_app.config["API_ROOT"] + "/contacts/labs"
    response = client.post(route, json=data.test_laboratory, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    laboratory_id = response.json["laboratoryId"]
    assert laboratory_id

    route = ispyb_core_app.config["API_ROOT"] + "/contacts/persons"
    person_dict = data.get_test_person()
    person_dict["laboratoryId"] = laboratory_id
    response = client.post(route, json=person_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    person_id = response.json["personId"]
    assert person_id

    route = ispyb_core_app.config["API_ROOT"] + "/proposals"
    proposal_dict = data.test_proposal
    proposal_dict["personId"] = person_id
    response = client.post(route, json=proposal_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    proposal_id = response.json["proposalId"]
    assert proposal_id