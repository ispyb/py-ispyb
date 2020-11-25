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


def test_delete(ispyb_core_app, ispyb_core_token):
    client = ispyb_core_app.test_client()
    headers = {"Authorization": "Bearer " + ispyb_core_token}

    route = ispyb_core_app.config["API_ROOT"] + "/proposals"
    response = client.get(route, headers=headers)
    proposal_id = response.json["data"]["rows"][-1]["proposalId"]

    route = ispyb_core_app.config["API_ROOT"] + "/proposals/" + str(proposal_id)
    response = client.delete(route, headers=headers)
    assert response.status_code == 200, "[DELTE] %s " % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/contacts/persons"
    response = client.get(route, headers=headers)
    person_id = response.json["data"]["rows"][-1]["personId"]
    route = ispyb_core_app.config["API_ROOT"] + "/contacts/persons/" + str(person_id)
    response = client.delete(route, headers=headers)
    assert response.status_code == 200, "[DELETE] %s " % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/contacts/labs"
    response = client.get(route, headers=headers)
    lab_id = response.json["data"]["rows"][-1]["laboratoryId"]
    route = ispyb_core_app.config["API_ROOT"] + "/contacts/labs/" + str(lab_id)
    response = client.delete(route, headers=headers)
    assert response.status_code == 200, "[DELETE] %s " % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/beamline/setups"
    response = client.get(route, headers=headers)
    beamline_setup_id = response.json["data"]["rows"][-1]["beamLineSetupId"]
    route = ispyb_core_app.config["API_ROOT"] + "/beamline/setups/" + str(beamline_setup_id)
    response = client.delete(route, headers=headers)
    assert response.status_code == 200, "[DELETE] %s " % (route)