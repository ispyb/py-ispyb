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


__license__ = "LGPLv3+"


from app import create_app
import os
import sys
import pytest

TESTS_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)


@pytest.fixture(scope="session")
def flask_app():
    app = create_app()
    with app.app_context():
        yield app

@pytest.fixture(scope="session")
def token(flask_app):
    client = flask_app.test_client()
    api_root = flask_app.config["API_ROOT"]

    response = client.get(
        api_root + "/auth/login", headers={"username": "user", "password": "pass"}
    )
    return response.json["token"]

