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
from tests.core.empty_db.functional.data.proposal import proposal_create


@pytest.mark.parametrize("test_elem", proposal_create)
def test_proposal_create(ispyb_app, manager_token, clean_db_before_test, test_elem):
    client = ispyb_app.test_client()
    headers = {"Authorization": "bearer " + manager_token}

    test_description, test_input, test_expected = test_elem[
        'description'],  test_elem['input'],  test_elem['expected']

    response_lab = client.post(ispyb_app.config["API_ROOT"] +
                               "/contacts/labs", json=test_input["laboratory"], headers=headers)
    assert response_lab.status_code == 200, test_description

    test_input["person"]["laboratoryId"] = response_lab.json["laboratoryId"]
    response_person = client.post(ispyb_app.config["API_ROOT"] +
                                  "/contacts/persons", json=test_input["person"], headers=headers)
    assert response_person.status_code == 200, test_description

    test_input["proposal"]["personId"] = response_person.json["personId"]
    response_proposal = client.post(ispyb_app.config["API_ROOT"] +
                                    "/proposals", json=test_input["proposal"], headers=headers)

    assert response_proposal.status_code == test_expected["code"], test_description

# Add other test methods on proposals here
