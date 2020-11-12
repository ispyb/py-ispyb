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



def test_patch(ispyb_core_app, ispyb_core_token):
    client = ispyb_core_app.test_client()
    headers = {"Authorization": "Bearer " + ispyb_core_token}

    route = ispyb_core_app.config["API_ROOT"] + "/contacts/labs"
    response = client.get(route, headers=headers)
    lab_id = response.json["data"]["rows"][0]["laboratoryId"]
    route = ispyb_core_app.config["API_ROOT"] + "/contacts/labs/" + str(lab_id)
    mod_laboratory = {"name": "Modified name"}

    response = client.patch(route, json=mod_laboratory, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)

    
    route = ispyb_core_app.config["API_ROOT"] + "/contacts/persons"
    response = client.get(route, headers=headers)
    person_id = response.json["data"]["rows"][0]["personId"]
    route = ispyb_core_app.config["API_ROOT"] + "/contacts/persons/" + str(person_id)
    mod_person = {
        "familyName": "Modified name",
        "phoneNumber": "0172-12233"
    }

    response = client.patch(route, json=mod_person, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)


    route = ispyb_core_app.config["API_ROOT"] + "/contacts/lab_contacts"
    response = client.get(route, headers=headers)
    lab_contact_id = response.json["data"]["rows"][0]["labContactId"]
    route = ispyb_core_app.config["API_ROOT"] + "/contacts/lab_contacts/" + str(lab_contact_id)
    mod_lab_contact = {
        "defaultCourrierCompany": "FedEX"
    }

    response = client.patch(route, json=mod_lab_contact, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)
