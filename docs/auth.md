# py-ISPyB Authentication and authorization system

---

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

-   **AbstractAuthentication** : plugin should override `get_user_and_groups(self, username, password, token)` method and return a tuple `(username, groups[])`
-   **AbstractDBGroupsAuthentication** : plugin should override `get_person(self, username, password, token)` method and return a `pyispyb.core.models.Person` object. Groups managment is delegated to ISPyB database.

---

## Configuration

Authentication plugins to be activated are configured in the `ispyb_core_config.yml` file like this:

```yml
server:
    AUTH:
        - keycloak:
              AUTH_MODULE: "pyispyb.app.extensions.auth.KeycloakDBGroupsAuthentication"
              AUTH_CLASS: "KeycloakDBGroupsAuthentication"
              CONFIG:
                  KEYCLOAK_SERVER_URL: "your_server"
                  KEYCLOAK_CLIENT_ID: "your_client"
                  KEYCLOAK_REALM_NAME: "your_realm"
                  KEYCLOAK_CLIENT_SECRET_KEY: "your_secret"
        - ldap:
              AUTH_MODULE: "pyispyb.app.extensions.auth.LdapAuthentication"
              AUTH_CLASS: "LdapAuthentication"
              CONFIG:
                  LDAP_URI: "ldap://your_ldap"
                  LDAP_BASE_INTERNAL: "ou=People,dc=esrf,dc=fr"
                  LDAP_BASE_EXTERNAL: "ou=Pxwebgroups,dc=esrf,dc=fr"
        - dummy: # /!\/!\/!\ ONLY USE FOR TESTS /!\/!\/!\
              AUTH_MODULE: "pyispyb.app.extensions.auth.DummyAuthentication"
              AUTH_CLASS: "DummyAuthentication"
```

---

## Database groups and permissions

Fore some authentication plugins (for instance `KeycloakDBGroupsAuthentication`), groups are configured in the **database** using the following tables:

-   **UserGroup**
-   **Person**
-   **UserGroup_has_Person**

For all authentication plugins, permissions are configured in the **database** using the following tables:

-   **UserGroup**
-   **Permission**
-   **UserGroup_has_Permission**

---

## How to authentify

To authentify their requests, users should get a py-ISPyB token. This token is provided by the `/auth/login` route with `POST` method and the following parameters in json body:

-   **plugin** - name of the plugin to be used for authentication, as specified in configuration
-   **username** _(optional)_
-   **password** _(optional)_
-   **token** _(optional)_

Then you can authorize your requets using this token in the `Authorization` header: `Bearer YOUR_TOKEN`. For example to retrieve proposals use:

```bash
curl -X GET -H 'Authorization: Bearer YOUR_TOKEN' -i http://localhost:5000/ispyb/api/v1/proposals
```

---

## Decorators

The following decorators (from `pyispyb.app.extensions.auth.decorators`) can be used on the routes to manage authentication and authorization rules.

### `@authentication_required`

Makes the route only accesible to **authenticated users** (no permissions checking).

### `@permission_required(operator, [permissions])`

Makes the route only accesible to users with the **specified permissions**.

-   `operator` is either
    -   `"any"` User should have **any** of the specified permissions
    -   `"all"` User should have **all** of the specified permissions

### `@proposal_authorization_required`

Verifies that the user is **associated to the requested proposal**. To do so, this decorator uses the `proposal_id` parameter in the route.
User must verify any of the following conditions :

-   `Person.personId = Proposal.personId`
-   `Person.personId = ProposalHasPerson.personId and ProposalHasPerson.proposalId = Proposal.proposalId`
-   _has permission_ `all_proposals`

### `@session_authorization_required`

Verifies that the user is **associated to the requested session**. To do so, this decorator uses the `session_id` parameter in the route.
User must verify any of the following conditions :

-   `Person.personId = Session_has_Person.personId and Session_has_Person.sessionId = BLSession.sessionId`
-   `BLSession.proposalId = Proposal.proposalId and Person.personId = Proposal.personId`
-   _has permission_ `all_sessions`
