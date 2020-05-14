# ISPyB flask server
# https://github.com/IvarsKarpics/ispyb_backend_prototype

from app import create_app
import os
import sys
import pytest

TESTS_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    with app.app_context():
        yield app
