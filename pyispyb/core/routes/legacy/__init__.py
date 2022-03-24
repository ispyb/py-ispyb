import os
import logging
from importlib import import_module
from fastapi import FastAPI

from .base import router

logger = logging.getLogger(__name__)


def init_app(app: FastAPI, prefix: str = None, **kwargs):
    """Init app routes."""
    for module_name in os.listdir(os.path.dirname(__file__)):
        if not module_name.startswith("__") and module_name.endswith(".py"):
            try:
                logger.info(f"importing {module_name}")
                import_module(".%s" % module_name[:-3], package=__name__)
            except Exception:
                logger.exception(f"Could not import module `{module_name}`")

    app.include_router(router, prefix=prefix)
