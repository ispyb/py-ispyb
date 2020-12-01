"""
Project: py-ispyb
https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along
"""


from app import create_app

__license__ = "LGPLv3+"


import os
import sys
import pytest


TESTS_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, ROOT_DIR)


@pytest.fixture(scope="session")
def ispyb_core_app():
    app = create_app("ispyb_core_config.yml", "test")
    with app.app_context():
        yield app


@pytest.fixture()
def ispyb_core_token(ispyb_core_app):
    client = ispyb_core_app.test_client()
    api_root = ispyb_core_app.config["API_ROOT"]

    response = client.get(
        api_root + "/auth/login", headers={"username": "admin", "password": "pass"}
    )
    return response.json["token"]
