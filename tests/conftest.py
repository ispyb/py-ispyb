# ISPyB flask server
# https://github.com/IvarsKarpics/ispyb_backend_prototype

import os
import sys
import pytest

TESTS_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.insert(0, ROOT_DIR)

#print ROOT_DIR

from app import create_app
from tests import data as test_data

@pytest.fixture(scope='module')
def app():
    app = create_app()

    yield app




@pytest.fixture
def data():
    return test_data
