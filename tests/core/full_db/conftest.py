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
from tests.core.utils import clean_db, get_all_permissions_token
__license__ = "LGPLv3+"


import os
import sys
import pytest
from pyispyb.app.extensions import db


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, ROOT_DIR)

app = create_app(
    ROOT_DIR+"/ispyb_core_config_test_full_db.yml", "test")


@pytest.fixture()
def ispyb_app():
    with app.app_context():
        yield app


@pytest.fixture()
def manager_token(ispyb_app):
    yield get_all_permissions_token(ispyb_app)
