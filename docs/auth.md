# Authentication and authorization

## Authentication

`py-ispyb` relies on plugins to handle different methods of authenticating users to the system. There are some mechanisms that are implemented natively like LDAP, keycloak and dummy that can be used out-of-the-box. However, it is worth noting that anyone can write his own plugin.

There's a dedicated endpoint that allows to use the different plugins that are installed. This endpoint receives as parameters:

- **plugin** - name of the plugin to be used for authentication, as specified in configuration
- **username** _(optional)_
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
  "username": "test",
  "password": "Admin",
  "token": "Admin"

}'
```

If the authentication is successful the response will be a json with the following fields:

```json
{
  "username": "test",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJncm91cHMiOlsiQWRtaW4iXSwicGVybWlzc2lvbnMiOlsiQWRtaW4iXSwiaWF0IjoxNjUwOTgxNjA5LCJleHAiOjE2NTA5OTk2MDl9.3Iq2lGG5RR6Gebss5qEDdASrEMwCIne2jFhaVqp91m0",
  "permissions": ["Admin"],
  "groups": ["Admin"]
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

New plugins should implement one of the two following classes :

- **AbstractAuthentication** : plugin should override `get_user_and_groups(self, username, password, token)` method and return a tuple `(username, groups[])`
- **AbstractDBGroupsAuthentication** : plugin should override `get_person(self, username, password, token)` method and return a `pyispyb.core.models.Person` object. Groups management is delegated to ISPyB database.

### Authorization dependencies

The following dependencies can be used to manage authentication and authorization rules.

#### `permission_required(operator, [permissions])`

Makes the route only accessible to users with the **specified permissions**.

- `operator` is either
  - `"any"` User should have **any** of the specified permissions
  - `"all"` User should have **all** of the specified permissions

#### `proposal_authorisation`

Verifies that the user is **associated to the requested proposal**. To do so, it uses the `proposal_id` parameter.
User must verify any of the following conditions :

- `Person.personId = Proposal.personId`
- `Person.personId = ProposalHasPerson.personId and ProposalHasPerson.proposalId = Proposal.proposalId`
- _has permission_ `all_proposals`

#### `session_authorisation`

Verifies that the user is **associated to the requested session**. To do so, it uses the `session_id` parameter.
User must verify any of the following conditions :

- `Person.personId = Session_has_Person.personId and Session_has_Person.sessionId = BLSession.sessionId`
- `BLSession.proposalId = Proposal.proposalId and Person.personId = Proposal.personId`
- _has permission_ `all_sessions`
