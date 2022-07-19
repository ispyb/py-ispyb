import ldap
import logging
from typing import Any, Optional

from .AbstractAuthentication import AbstractAuthentication


logger = logging.getLogger(__name__)


class LdapAuthentication(AbstractAuthentication):
    def configure(self, config: dict[str, Any]) -> None:
        self.ldap_conn = ldap.initialize(config["LDAP_URI"])
        self.ldap_base_internal = config["LDAP_BASE_INTERNAL"]
        self.ldap_base_groups = config["LDAP_BASE_GROUPS"]

    def authenticate_by_user(self, login: str, password: str) -> Optional[str]:
        try:
            logger.debug(
                f"LDAP login: try to authenticate user `{login}` as internal user"
            )
            self.ldap_conn.simple_bind_s(
                f"uid={login},{self.ldap_base_internal}", password
            )
            self.ldap_conn.search_s(
                self.ldap_base_internal,
                ldap.SCOPE_ONELEVEL,
                f"(uid={login})",
                ["*"],
            )
            return login
        except ldap.INVALID_CREDENTIALS:
            logger.exception(f"LDAP login: unable to authenticate user {login}")
