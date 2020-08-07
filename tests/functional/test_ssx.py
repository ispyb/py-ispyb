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


def test_ssx(ispyb_ssx_app, ispyb_ssx_token):
    client = ispyb_ssx_app.test_client()
    api_root = ispyb_ssx_app.config["API_ROOT"]

    return
    headers = {"Authorization": "Bearer " + ispyb_ssx_token}
    response = client.get(api_root + "/sample", headers=headers)
    assert response.status_code == 200, "Wrong status code"
    #assert len(response.json) > 0, "No schemas returned"
