from typing import Any
import logging
from logging.config import dictConfig
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from pyispyb.app.extensions.database.utils import enable_debug_logging
from pyispyb.app.extensions.database.middleware import get_session
from pyispyb.app.extensions.options.base import setup_options
from pyispyb.app.globals import GlobalsMiddleware

from ..config import settings, LogConfig
from pyispyb.app import routes as base_routes
from pyispyb.core import routes as core_routes
from pyispyb.app.extensions.auth import auth_provider

dictConfig(LogConfig().dict())
logger = logging.getLogger("ispyb")


app = FastAPI(openapi_url=f"{settings.api_root}/openapi.json")
app.add_middleware(GlobalsMiddleware)


@app.middleware("http")
async def get_session_as_middleware(request, call_next):
    with get_session():
        return await call_next(request)


setup_options(app)


def enable_cors() -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if settings.cors:
    enable_cors()

if settings.query_debug:
    enable_debug_logging()


def custom_openapi() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="py-ISPyB",
        version="0.1alpha",
        description="FastAPI Prototype",
        routes=app.routes,
    )

    # Convert nullable to ["null", type] for rjsf
    # https://github.com/rjsf-team/react-jsonschema-form/pull/1213
    # This is technically incorrect for OpenAPI v3, but nullable is not yet supported in rjsf
    for schema_name, schema in openapi_schema["components"]["schemas"].items():
        if "properties" in schema:
            for property_name, property in schema["properties"].items():
                if property.get("nullable"):
                    property["type"] = ["null", property["type"]]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


setattr(app, "openapi", custom_openapi)

auth_provider.init_app(app)
base_routes.init_app(app, prefix=settings.api_root)
core_routes.init_app(app, prefix=settings.api_root)
