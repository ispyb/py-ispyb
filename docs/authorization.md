# Proposal(s), Session(s), and related entities

Authorization is applied to all user facing resources in py-ISPyB and different permissions are available to grant users and staff access to entities related to the core of ISPyB. These include but not limited to:

- Proposal
- Protein, Crystal, BLSample, Shipping, LabContact
- BLSession, DataCollectionGroup, DataCollection

etc ...

The authorization rules are applied in four ways:

### Users

- A user can access entities related to a Proposal and the DataCollection(s) in which they are a member of one or more Session(s) [linked via SessionHasPerson]. _This is an intrinsic permission and is the default behaviour if the user has no other permissions._
- A user can access entities related to all Session(s) in a Proposal [linked via ProposalHasPerson]

### Administrators

- An administrator can view all Sessions on a Proposal for specific beamline(s) via a `BeamLineGroup` permission
- An administrator can access all Sessions and Proposals via `all_proposals`

## BeamLineGroups

Beamline groups provide a way to grant access to all Proposals, Sessions and related entities to a set of staff members for a particular group of beamlines.

For example:

```json
"beamLineGroups": [
    {
        "groupName": "BL0x",
        "uiGroup": "mx",
        "permission": "bl0_admin",
        "beamlines": [
            {"beamLineName": "BL01"},
            {"beamLineName": "BL02"},
        ],
    },
]
```

A staff member with the `bl0_admin` permission will be able to access Proposal(s) and Session(s) allocated on beamlines `BL01` and `BL02`, but not other beamlines. `uiGroup` specifies how this group should be rendered in the UI.

# Permissions

Routes can require a specific permission by using the `permission` dependency.

```python
from pyispyb.dependencies import permission


@router.get(
    "/path",
)
def get_something(depends: bool = Depends(permission("my_permission"))):
    ...
```

# Deprecated Authorization Mechanisms

These functions are deprecated and currently only used in the legacy API resources. They should not be used for new developments.

## Authorization dependencies

The following decorators can be used to manage authentication and authorization rules.

### `permission_required(operator, [permissions])`

Makes the route only accessible to users with the **specified permissions**.

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
