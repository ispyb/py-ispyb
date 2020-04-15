# ISPyB flask server
# https://github.com/IvarsKarpics/ispyb_backend_prototype

import os
import sys

TESTS_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

sys.path.insert(0, ROOT_DIR)
