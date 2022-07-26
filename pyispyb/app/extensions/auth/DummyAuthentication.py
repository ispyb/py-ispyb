from typing import Optional

from ispyb import models

from .AbstractAuthentication import AbstractAuthentication


class DummyAuthentication(AbstractAuthentication):
    """Dummy authentication class."""

    def authenticate_by_login(self, login: str, password: str) -> Optional[models.Person]:
        return models.Person(
            login=login
        )
