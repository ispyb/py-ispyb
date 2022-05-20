# from https://github.com/tiangolo/fastapi/issues/1173
from fastapi.openapi.utils import get_openapi
import json

from pyispyb.app.main import app, custom_openapi

app.openapi = custom_openapi

with open("openapi.json", "w") as f:
    json.dump(
        get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
            # openapi_prefix=app.openapi_prefix,
        ),
        f,
    )
