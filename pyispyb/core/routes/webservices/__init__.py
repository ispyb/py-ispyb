import os
import logging
from importlib import import_module
from fastapi import FastAPI

from .base import router

logger = logging.getLogger(__name__)


def init_app(app: FastAPI, prefix: str = None, **kwargs):
    """Init app routes."""
    if not app.db_options.enable_webservice_routes:
        logger.info("Webservice routes disabled")
        return

    for module_name in os.listdir(os.path.dirname(__file__)):
        if not module_name.startswith("__") and module_name.endswith(".py"):
            try:
                logger.info(f"importing {module_name}")
                module = import_module(".%s" % module_name[:-3], package=__name__)
                if hasattr(module, "router"):
                    app.include_router(module.router, prefix=prefix)
            except Exception:
                logger.exception(f"Could not import module `{module_name}`")

    app.include_router(router, prefix=prefix)
