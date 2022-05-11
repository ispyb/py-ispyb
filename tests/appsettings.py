import os

# We need to override these env variables for test context before the
# "settings" and "app" modules are initialized since they will read them.
# After doing so, we re-export them so that all test files refer to this
# initialization module instead of the original ones.

os.environ["SECRET_KEY"] = "test_secret"
os.environ[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+mysqlconnector://test:test@127.0.0.1/test"
os.environ["ISPYB_AUTH"] = "tests/config/auth.yml"

from pyispyb.config import settings, Settings  # noqa
from pyispyb.app.main import app  # noqa
