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
    mod_person = {"familyName": "Modified name", "phoneNumber": "0172-12233"}

    response = client.patch(route, json=mod_person, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/contacts/lab_contacts"
    response = client.get(route, headers=headers)
    lab_contact_id = response.json["data"]["rows"][0]["labContactId"]
    route = (
        ispyb_core_app.config["API_ROOT"]
        + "/contacts/lab_contacts/"
        + str(lab_contact_id)
    )
    mod_lab_contact = {"defaultCourrierCompany": "FedEX"}

    response = client.patch(route, json=mod_lab_contact, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/beamline/detectors"
    response = client.get(route, headers=headers)
    detector_id = response.json["data"]["rows"][0]["detectorId"]
    route = (
        ispyb_core_app.config["API_ROOT"] + "/beamline/detectors/" + str(detector_id)
    )
    mod_detector = {"detectorModel": "T1_0001"}

    response = client.patch(route, json=mod_detector, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/beamline/setups"
    response = client.get(route, headers=headers)
    beamline_setup_id = response.json["data"]["rows"][0]["beamLineSetupId"]
    route = (
        ispyb_core_app.config["API_ROOT"] + "/beamline/setups/" + str(beamline_setup_id)
    )
    mode_beamline_setup = {"synchrotronName": "Error"}

    response = client.patch(route, json=mode_beamline_setup, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/samples/proteins"
    response = client.get(route, headers=headers)
    protein_id = response.json["data"]["rows"][0]["proteinId"]
    route = ispyb_core_app.config["API_ROOT"] + "/samples/proteins/" + str(protein_id)
    mod_protein = {"molecularMass": "200"}

    response = client.patch(route, json=mod_protein, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/samples/diffraction_plans"
    response = client.get(route, headers=headers)
    diffraction_plan_id = response.json["data"]["rows"][0]["diffractionPlanId"]
    route = (
        ispyb_core_app.config["API_ROOT"]
        + "/samples/diffraction_plans/"
        + str(diffraction_plan_id)
    )
    mod_diffraction_plan = {"observedResolution": "3"}

    response = client.patch(route, json=mod_diffraction_plan, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/samples/crystals"
    response = client.get(route, headers=headers)
    crystal_id = response.json["data"]["rows"][0]["crystalId"]
    route = ispyb_core_app.config["API_ROOT"] + "/samples/crystals/" + str(crystal_id)
    mod_crystal = {"spaceGroup": "P2"}

    response = client.patch(route, json=mod_crystal, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)

    route = ispyb_core_app.config["API_ROOT"] + "/samples"
    response = client.get(route, headers=headers)
    sample_id = response.json["data"]["rows"][0]["blSampleId"]
    route = ispyb_core_app.config["API_ROOT"] + "/samples/" + str(sample_id)
    mod_sample = {"location": "2"}

    response = client.patch(route, json=mod_sample, headers=headers)
    assert response.status_code == 200, "[PATCH] %s failed" % (route)
