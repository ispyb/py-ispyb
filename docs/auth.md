# Authentication

`py-ispyb` relies on plugins to handle different methods of authenticating users to the system. There are some mechanisms that are implemented natively like LDAP, keycloak and dummy that can be used out-of-the-box. However, it is worth noting that anyone can write his own plugin.

There's a dedicated endpoint that allows to use the different plugins that are installed. This endpoint receives as parameters:

- **plugin** - name of the plugin to be used for authentication, as specified in configuration
- **login** _(optional)_
- **password** _(optional)_
- **token** _(optional)_

Example of the request:

```bash
curl -X 'POST' \
  'http://localhost:8000/ispyb/api/v1/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "plugin": "dummy",
  "login": "test",
  "password": "Admin",
  "token": "Admin"

}'
```

If the authentication is successful the response will be a json with the following fields:

```json
{
  "login": "test",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJncm91cHMiOlsiQWRtaW4iXSwicGVybWlzc2lvbnMiOlsiQWRtaW4iXSwiaWF0IjoxNjUwOTgxNjA5LCJleHAiOjE2NTA5OTk2MDl9.3Iq2lGG5RR6Gebss5qEDdASrEMwCIne2jFhaVqp91m0",
  "permissions": ["Admin"]
}
```

## Authorization

For any authentication plugin, permissions are configured in the **database** using the following tables (with example data):

- **UserGroup**: [Admin, user]
- **Permission**: [own_proposals, own_sessions, all_proposals, all_sessions]
- **UserGroup_has_Permission**: [{Admin, all_proposals}, {Admin, all_sessions}, {user, own_proposals}, {user, own_sessions}]

## Configure a plugin

One or more plugin can be enabled at the same time. A configuration file called `auth.yml` at the root of the project contains their configuration parameters.

The next examples shows how to enable the dummy authentication plugin:

```yml
AUTH:
  - dummy:
      ENABLED: true
      AUTH_MODULE: "pyispyb.app.extensions.auth.DummyAuthentication"
      AUTH_CLASS: "DummyAuthentication"
```

## List of plugins

py-ISPyB is using the following authentication plugins, which code you can find in `pyispyb/app/extension/auth`.

### DummyAuthentication

Provides easy authentication for `tests`. Permissions listed in the password field are given.

Configuration

```yml
AUTH:
  - dummy: # /!\/!\/!\ ONLY USE FOR TESTS /!\/!\/!\
      ENABLED: false
      AUTH_MODULE: "pyispyb.app.extensions.auth.DummyAuthentication"
      AUTH_CLASS: "DummyAuthentication"
```

### `KeycloakDBGroupsAuthentication`

Provides authentication using keycloak with DB-managed groups.

Configuration

```yml
AUTH:
  ENABLED: true
  AUTH_MODULE: "pyispyb.app.extensions.auth.KeycloakDBGroupsAuthentication"
  AUTH_CLASS: "KeycloakDBGroupsAuthentication"
  CONFIG:
    KEYCLOAK_SERVER_URL: "your_server"
    KEYCLOAK_CLIENT_ID: "your_client"
    KEYCLOAK_REALM_NAME: "your_realm"
    KEYCLOAK_CLIENT_SECRET_KEY: "your_secret"
```

### `LdapAuthentication`

Provides authentication using LDAP users and groups.

Configuration

```yml
AUTH:
  - ldap:
      ENABLED: true
      AUTH_MODULE: "pyispyb.app.extensions.auth.LdapAuthentication"
      AUTH_CLASS: "LdapAuthentication"
      CONFIG:
        LDAP_URI: "ldap://your_ldap"
        LDAP_BASE_INTERNAL: "ou=People,dc=test,dc=fr"
        LDAP_BASE_EXTERNAL: "ou=Pxwebgroups,dc=test,dc=fr"
```

## Implementing new plugins

New plugins should inherit from `AbstractAuthentication` and override either `authenticate_by_login` or `authenticate_by_token` dependning on whether they accept a login / password combination or an authorisation token. Both functions return `Person` on success. This can be prepopulated with `familyName`, `givenName`, and `emailAddress`, which can be used to auto-create a new `Person` entry if the option is enabled (disabled by default)

For example:

```python
from typing import Optional

from ispyb import models

from .AbstractAuthentication import AbstractAuthentication


class MyAuthentication(AbstractAuthentication):
    """My authentication class."""

    def configure(self, config: dict[str, Any]):
      self._config = config

    def authenticate_by_login(self, login: str, password: str) -> Optional[models.Person]:
        if ...
            return models.Person(
                login=login,
                familyName=...,
                givenName=...,
            )
        else:
          logger.exception("Something went wrong")
```

Or for token based authentication:

```python
from typing import Optional

from ispyb import models

from .AbstractAuthentication import AbstractAuthentication, AuthType


class MyAuthentication(AbstractAuthentication):
    """My authentication class."""

    authentication_type = AuthType.token

    def configure(self, config: dict[str, Any]):
      self._config = config

    def authenticate_by_token(self, token: str) -> Optional[models.Person]:
        if ...
            return models.Person(
              login=login
            )
        else:
            logger.exception("Something went wrong")
```

Plugins can export specific config variables to the UI as well by defining `config_export`, these properties are made available to the `/auth/config` endpoint:

```python
from typing import Optional

from ispyb import models

from .AbstractAuthentication import AbstractAuthentication, AuthType


class MyAuthentication(AbstractAuthentication):
    """My authentication class."""

    authentication_type = AuthType.token
    config_export = ["MY_CONFIG_PROPERTY"]

    ...
```
