from contextlib import contextmanager

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.types import ASGIApp

from pyispyb.app.extensions.auth.token import set_token_data
from pyispyb.app.extensions.auth.bearer import JWTBearer, verify_jwt

security = HTTPBearer()


@contextmanager
def mock_permissions(permissions: list[str], app: ASGIApp):
    """Allows overriding the permissions the current user has by replacing the JWTBearer dependency"""

    async def JWTBearerMockPermissions(
        credentials: HTTPAuthorizationCredentials = Depends(security),
    ):
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=401, detail="Invalid authentication scheme."
                )
            decoded = verify_jwt(credentials.credentials)
            if not decoded:
                raise HTTPException(
                    status_code=401, detail="Invalid token or expired token."
                )

            decoded["permissions"] = permissions
            print()
            print(f" - Set permissions for `{decoded['login']}` to {permissions}")
            set_token_data(decoded)

            return credentials.credentials
        else:
            raise HTTPException(status_code=401, detail="No token provided.")

    app.dependency_overrides[JWTBearer] = JWTBearerMockPermissions

    yield

    print(" - Resetting permissions")
    app.dependency_overrides = {}
