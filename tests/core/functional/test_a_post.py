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

    print("Laboratory id: %d" % laboratory_id)
    route = ispyb_core_app.config["API_ROOT"] + "/contacts/persons"
    person_dict = data.get_test_person()
    person_dict["laboratoryId"] = laboratory_id
    response = client.post(route, json=person_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    person_id = response.json["personId"]
    assert person_id
    print("Person id: %d" % person_id)

    route = ispyb_core_app.config["API_ROOT"] + "/proposals"
    proposal_dict = data.get_test_proposal()
    proposal_dict["personId"] = person_id
    response = client.post(route, json=proposal_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    proposal_id = response.json["proposalId"]
    assert proposal_id
    print("Proposal id: %d" % proposal_id)

    route = ispyb_core_app.config["API_ROOT"] + "/contacts/lab_contacts"
    lab_contact_dict = data.test_lab_contact
    lab_contact_dict["personId"] = person_id
    lab_contact_dict["proposalId"] = proposal_id
    response = client.post(route, json=lab_contact_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    lab_contact_id = response.json["labContactId"]
    print("LabContact id: %d" % lab_contact_id)
    assert lab_contact_id


    route = ispyb_core_app.config["API_ROOT"] + "/beamline/detectors"
    detector_dict = data.get_test_detector()
    response = client.post(route, json=detector_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    detector_id = response.json["detectorId"]

    print("Detector id: %d" % detector_id)
    assert detector_id


    route = ispyb_core_app.config["API_ROOT"] + "/beamline/setups"
    beamline_setup_dict = data.test_beamline_setup
    beamline_setup_dict["detectorId"] = detector_id
    response = client.post(route, json=beamline_setup_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    beamline_setup_id = response.json["beamLineSetupId"]

    print("BeamlineSetup id: %d" % beamline_setup_id)
    assert beamline_setup_id


    route = ispyb_core_app.config["API_ROOT"] + "/samples/proteins"
    protein_dict = data.test_protein
    proposal_dict["proposalId"] = proposal_id
    proposal_dict["personId"] = person_id
    response = client.post(route, json=protein_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    protein_id = response.json["proteinId"]

    print("Protein id: %d" % protein_id)
    assert protein_id


    route = ispyb_core_app.config["API_ROOT"] + "/samples/diffraction_plans"
    diffraction_plan_dict = data.test_diffraction_plan
    diffraction_plan_dict["presetForProposalId"] = proposal_id
    diffraction_plan_dict["detectorId"] = detector_id
    response = client.post(route, json=diffraction_plan_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    diffraction_plan_id = response.json["diffractionPlanId"]

    print("Diffraction plan id: %d" % diffraction_plan_id)
    assert diffraction_plan_id


    route = ispyb_core_app.config["API_ROOT"] + "/samples/crystals"
    crystal_dict = data.test_crystal
    crystal_dict["proteinId"] = protein_id
    crystal_dict["diffractionPlanId"] = diffraction_plan_id
    response = client.post(route, json=crystal_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    crystal_id = response.json["crystalId"]

    print("Crystal id: %d" % crystal_id)
    assert crystal_id

    route = ispyb_core_app.config["API_ROOT"] + "/samples"
    sample_dict = data.test_sample
    sample_dict["crystalId"] = crystal_id
    response = client.post(route, json=sample_dict, headers=headers)

    assert response.status_code == 200, "[POST] %s failed" % route
    sample_id = response.json["blSampleId"]

    print("Sample id: %d" % sample_id)
    assert sample_id
