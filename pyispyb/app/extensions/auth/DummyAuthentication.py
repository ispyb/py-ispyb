from typing import Optional

from .AbstractAuthentication import AbstractAuthentication


class DummyAuthentication(AbstractAuthentication):
    """Dummy authentication class."""

    def authenticate_by_login(self, login: str, password: str) -> Optional[str]:
        return login
