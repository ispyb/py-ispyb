# Technical description

pyispyb is in python written ISPyB backend server based on Flask and sqlalchemy. To access underlaying database sqlalchemy, flask-sqlalchemy and marchmallow libraries are used. A modified flask-restx is used to define REST api.

## Overall architecture

The project is developed in a microservice manner, allowing to plugin and use several ispyb components as microservice. Currently the following services are available:

- core : core componenets of ispyb
- ssx : serial crystallography
- em : electron microscopy.

The core microservice is the main component and other services depend on it. Each service can reuse the software code and

```python
# Adds a namespace called Proposals
# REST api base path http://localhost:5000/ispyb/api/v1/proposals

api = Namespace(
    "Proposals", description="Proposal related namespace", path="/proposals"
)
api_v1.add_namespace(api)

@api.route("", endpoint="proposals")                        #
@api.doc(security="apikey")
class Proposals(Resource):
"""Allows to get all proposals"""

    @token_required
    @authorization_required
    def get(self):
        """Returns proposals based on query parameters"""

        api.logger.info("Get all proposals")
        return proposal.get_proposals(request)

    @api.expect(proposal_schemas.f_schema)
    @api.marshal_with(proposal_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        """Adds a new proposal"""

        api.logger.info("Inserts a new proposal")
        return proposal.add_proposal(api.payload)
```
