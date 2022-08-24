from ....app.base import AuthenticatedAPIRouter


router = AuthenticatedAPIRouter(
    prefix="/webservices", tags=["To be used by external applications"]
)
