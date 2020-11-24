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

    endpoint_list = [
        "/proposals",
        "/proposals?offset=1&limit=1",
        "/proposals?proposalCode=cm",
        "/contacts/labs",
        "/contacts/labs?offset=1&limit=1",
        "/contacts/labs?city=City",
        "/contacts/lab_contacts",
        "/contacts/lab_contacts?offset=1&limit=1",
        "/contacts/lab_contacts?defaultCourrierCompany=DHL",
        "/contacts/persons",
        "/contacts/persons?offset=1&limit=1",
        "/contacts/persons?login=boaty",
        "/data_collections",
        "/data_collections?offset=1&limit=1",
        "/beamline/detectors",
        "/beamline/detectors?offset=1&limit=1",
        "/beamline/detectors?detectorModel=T1",
        "/beamline/setups"
        "/beamline/setups?offset=1&limit=1",
        "/beamline/setups?beamlineName=testBeamline"
    ]

    headers = {"Authorization": "Bearer " + ispyb_core_token}

    for endpoint in endpoint_list:
        route = ispyb_core_app.config["API_ROOT"] + endpoint
        response = client.get(route, headers=headers)
        data = response.json

        assert response.status_code == 200, "[GET] %s " % (route)
        assert data, "[GET] %s No data returned" % route