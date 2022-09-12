from ....app.base import AuthenticatedAPIRouter


router = AuthenticatedAPIRouter(
    prefix="/webservices", tags=["Webservices - Used by external applications"]
)
