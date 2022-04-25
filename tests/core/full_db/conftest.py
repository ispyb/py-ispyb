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
from fastapi.testclient import TestClient
import pytest
import sys
from tests.core.utils import get_all_permissions_token

__license__ = "LGPLv3+"

import os


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, ROOT_DIR)


@pytest.fixture()
def setup_env():
    os.environ["SECRET_KEY"] = "test_secret"
    os.environ[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqlconnector://test:test@127.0.0.1/test"
    os.environ["ISPYB_AUTH"] = "tests/core/auth.yml"


@pytest.fixture()
def ispyb_settings(setup_env):
    from pyispyb.config import settings

    return settings


@pytest.fixture()
def ispyb_app(setup_env):
    from pyispyb.app.main import app

    return TestClient(app)


@pytest.fixture()
def manager_token(ispyb_app):
    return get_all_permissions_token(ispyb_app)
