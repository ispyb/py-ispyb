import importlib
import logging
from typing import Optional

from ispyb import models

from ....config import settings


log = logging.getLogger(__name__)


class AuthProvider:
    """Allows to authentificate users."""

    def __init__(self):
        self.site_authentications = {}

    def init_app(self, app):
        """Init extension."""

        auth_list = settings.auth
        for auth_plugin in auth_list:
            for auth_name in auth_plugin:
                enabled = auth_plugin[auth_name]["ENABLED"]
                if enabled:
                    module_name: str = auth_plugin[auth_name]["AUTH_MODULE"]
                    class_name: str = auth_plugin[auth_name]["AUTH_CLASS"]
                    config = {}
                    if "CONFIG" in auth_plugin[auth_name]:
                        config = auth_plugin[auth_name]["CONFIG"]
                    cls = getattr(importlib.import_module(module_name), class_name)
                    instance = cls()
                    instance.configure(config)
                    self.site_authentications[auth_name] = instance

    def get_auth(
        self,
        *,
        plugin: str,
        login: str | None,
        password: str | None,
        token: str | None
    ) -> Optional[models.Person]:
        """
        Check the user is authenticated and return the login.

        Basically this is the main authentification method where site_auth is site specific authentication class.

        Args:
            plugin (str): plugin to be used
            login (str): auth login
            password (str): auth password
            token (str): auth token

        Returns:
            person (models.Person): The current `Person`
        """
        if plugin not in self.site_authentications:
            return None

        return self.site_authentications[plugin].authenticate(login, password, token)


auth_provider = AuthProvider()
