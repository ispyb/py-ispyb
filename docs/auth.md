# Authentication and authorization

`py-ispyb` relies on plugins to handle different methods of authenticating users to the system. There are some mechanisms that are implemented natively like LDAP, keycloak and dummy that can be used out-of-the-box but it is worth noting that anyone can write his own plugin.

There's a dedicated endpoint that allows to use the different plugins that are installed. This endpoint receives as parameters: `plugin`, `username`, `password` and `token`

Example of the request:

```
curl -X 'POST' \
  'http://localhost:8000/ispyb/api/v1/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "plugin": "dummy",
  "username": "test",
  "password": "Admin",
  "token": "Admin"

}'
```

If the authentication is successful the response will be a json with the following fields:

```
{
  "username": "test",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJncm91cHMiOlsiQWRtaW4iXSwicGVybWlzc2lvbnMiOlsiQWRtaW4iXSwiaWF0IjoxNjUwOTgxNjA5LCJleHAiOjE2NTA5OTk2MDl9.3Iq2lGG5RR6Gebss5qEDdASrEMwCIne2jFhaVqp91m0",
  "permissions": [
    "Admin"
  ],
  "groups": [
    "Admin"
  ]
}
```

The HS256 token is:

```
{
  "username": "test",
  "groups": [
    "Admin"
  ],
  "permissions": [
    "Admin"
  ],
  "iat": 1650981609,
  "exp": 1650999609
}

```

## Configure the authentication plugins

One or more plugin can be enabled at the same time. A configuration file called `auth.yml` at the root of the project contains their configuration parameters.

The next configuration will enable the plugin dummy:

```
AUTH:
    - dummy:
          ENABLED: true
          AUTH_MODULE: "pyispyb.app.extensions.auth.DummyAuthentication"
          AUTH_CLASS: "DummyAuthentication"
```

## Plugins

py-ISPyB is using the following authentication plugins, which you can find in `pyispyb/app/extension/auth`.

### `DummyAuthentication`

Provides easy authentication for tests. Permissions listed in the password field are given.

### `KeycloakDBGroupsAuthentication`

Provides authentication using keycloak with DB-managed groups.

### `LdapAuthentication`

Provides authentication using LDAP users and groups.

### Implementing new plugins

New plugins should implement one of the two following classes :

- **AbstractAuthentication** : plugin should override `get_user_and_groups(self, username, password, token)` method and return a tuple `(username, groups[])`
- **AbstractDBGroupsAuthentication** : plugin should override `get_person(self, username, password, token)` method and return a `pyispyb.core.models.Person` object. Groups managment is delegated to ISPyB database.

---

## Configuration

Authentication plugins to be activated are configured in the `auth.yml` file like this:

```yml
AUTH:
  - keycloak:
      ENABLED: true
      AUTH_MODULE: "pyispyb.app.extensions.auth.KeycloakDBGroupsAuthentication"
      AUTH_CLASS: "KeycloakDBGroupsAuthentication"
      CONFIG:
        KEYCLOAK_SERVER_URL: "your_server"
        KEYCLOAK_CLIENT_ID: "your_client"
        KEYCLOAK_REALM_NAME: "your_realm"
        KEYCLOAK_CLIENT_SECRET_KEY: "your_secret"
  - ldap:
      ENABLED: true
      AUTH_MODULE: "pyispyb.app.extensions.auth.LdapAuthentication"
      AUTH_CLASS: "LdapAuthentication"
      CONFIG:
        LDAP_URI: "ldap://your_ldap"
        LDAP_BASE_INTERNAL: "ou=People,dc=esrf,dc=fr"
        LDAP_BASE_EXTERNAL: "ou=Pxwebgroups,dc=esrf,dc=fr"
  - dummy: # /!\/!\/!\ ONLY USE FOR TESTS /!\/!\/!\
      ENABLED: false
      AUTH_MODULE: "pyispyb.app.extensions.auth.DummyAuthentication"
      AUTH_CLASS: "DummyAuthentication"
```

---

## How to authenticate

To authenticate their requests, users should get a py-ISPyB token. This token is provided by the `/auth/login` route with `POST` method and the following parameters in json body:

- **plugin** - name of the plugin to be used for authentication, as specified in configuration
- **username** _(optional)_
- **password** _(optional)_
- **token** _(optional)_

Then you can authorize your requets using this token in the `Authorization` header: `Bearer YOUR_TOKEN`. For example to retrieve proposals use:

```bash
curl -X GET -H 'Authorization: Bearer YOUR_TOKEN' -i http://localhost:8000/ispyb/api/v1/proposals
```

---

# Authorization

## Database groups and permissions

Fore some authentication plugins (for instance `KeycloakDBGroupsAuthentication`), groups are configured in the **database** using the following tables:

- **UserGroup**
- **Person**
- **UserGroup_has_Person**

For all authentication plugins, permissions are configured in the **database** using the following tables:

- **UserGroup**
- **Permission**
- **UserGroup_has_Permission**

---

## Authorization dependencies

The following dependencies can be used to manage authentication and authorization rules.

### `permission_required(operator, [permissions])`

Makes the route only accesible to users with the **specified permissions**.

- `operator` is either
  - `"any"` User should have **any** of the specified permissions
  - `"all"` User should have **all** of the specified permissions

### `proposal_authorisation`

Verifies that the user is **associated to the requested proposal**. To do so, it uses the `proposal_id` parameter.
User must verify any of the following conditions :

- `Person.personId = Proposal.personId`
- `Person.personId = ProposalHasPerson.personId and ProposalHasPerson.proposalId = Proposal.proposalId`
- _has permission_ `all_proposals`

### `session_authorisation`

Verifies that the user is **associated to the requested session**. To do so, it uses the `session_id` parameter.
User must verify any of the following conditions :

- `Person.personId = Session_has_Person.personId and Session_has_Person.sessionId = BLSession.sessionId`
- `BLSession.proposalId = Proposal.proposalId and Person.personId = Proposal.personId`
- _has permission_ `all_sessions`
