import importlib

from ispyb import config

module_name = config['auth']['module']
class_name = config['auth']['class']
cls = getattr(importlib.import_module(module_name), class_name)

auth = cls()
