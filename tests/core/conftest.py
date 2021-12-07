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


from pyispyb import create_app
__license__ = "LGPLv3+"


import os
import sys
import pytest
from pyispyb.app.extensions import db


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, ROOT_DIR)

app = create_app(ROOT_DIR+"/tests/ispyb_core_config_test.yml", "test")


@pytest.fixture()
def ispyb_app():
    with app.app_context():
        yield app


def _clean_db():
    tables = db.engine.execute(
        "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'pydb_test' AND TABLE_TYPE = 'BASE TABLE';")
    for table in tables:
        db.engine.execute('SET FOREIGN_KEY_CHECKS=0; TRUNCATE TABLE ' +
                          table[0]+';')


@pytest.fixture()
def clean_db_before_test(ispyb_app):
    _clean_db()
    yield


@pytest.fixture()
def clean_db_after_test(ispyb_app):
    yield
    _clean_db()


@pytest.fixture()
def manager_token(ispyb_app):
    client = ispyb_app.test_client()
    api_root = ispyb_app.config["API_ROOT"]

    response = client.get(
        api_root + "/auth/login", headers={"username": "manager", "password": "pass"}
    )
    yield response.json["token"]
