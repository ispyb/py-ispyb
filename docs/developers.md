# Developer Notes

## Authentication

Authentication is generally handled via [JSON Web Tokens](https://jwt.io/) (JWT) which should be passed in the `Authorization` header with a value `Bearer {token}`. Most the of the py-ISPyB resources require a token to be present.

In certain situations it is not possible to use a JWT. For example when downloading a file it is not possible to pass an Authorization header. For these situations py-ISPyB provides a one time token system. A one time token can be generated for a particular url and this token can then be used as a query parameter to access the specified url a single time. Unused tokens are expired on a short time scale. A signed url can be generated using the `/user/sign` resource, and used as so:

```
GET /datacollections/attachments/2?onetime={token}
```
