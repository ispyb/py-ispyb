from ....app.base import AuthenticatedAPIRouter

router = AuthenticatedAPIRouter(prefix="/admin", tags=["Admin"])
