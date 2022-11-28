import ldap
import logging
from typing import Any, Optional

from ispyb import models

from .AbstractAuthentication import AbstractAuthentication


logger = logging.getLogger(__name__)


class LdapAuthentication(AbstractAuthentication):
    def configure(self, config: dict[str, Any]) -> None:
        self.ldap_url = config["LDAP_URI"]
        self.ldap_base_internal = config["LDAP_BASE_INTERNAL"]
        self.ldap_base_groups = config["LDAP_BASE_GROUPS"]

    def authenticate_by_login(
        self, login: str, password: str
    ) -> Optional[models.Person]:
        try:
            logger.debug(
                f"LDAP login: try to authenticate user `{login}` as internal user"
            )
            self.ldap_conn = ldap.initialize(self.ldap_url)
            self.ldap_conn.simple_bind_s(
                f"uid={login},{self.ldap_base_internal}", password
            )
            res = self.ldap_conn.search_s(
                self.ldap_base_internal,
                ldap.SCOPE_ONELEVEL,
                f"(uid={login})",
                ["*"],
            )[0][1]
            return models.Person(
                login=login,
                emailAddress=res["mail"][0],
                siteId=res["uidNumber"][0],
                familyName=res["sn"][0],
                givenName=res["givenName"][0],
                phoneNumber=res["telephoneNumber"][0],
            )
        except ldap.INVALID_CREDENTIALS:
            logger.exception(f"LDAP login: unable to authenticate user {login}")
