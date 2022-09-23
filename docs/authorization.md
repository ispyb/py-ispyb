# Proposal(s), Session(s), and related entities

Authorization is applied to all user facing resources in py-ISPyB and different permissions are available to grant users and staff access to entities related to the core of ISPyB. These include but not limited to:

- Proposal
- Protein, Crystal, BLSample, Shipping, LabContact
- BLSession, DataCollectionGroup, DataCollection

etc ...

The authorization rules are applied in four ways:

### Users

- A user can access entities related to a Proposal in which they are a member of one or more Session(s) and the DataCollection(s) for the specific Session(s) [linked via SessionHasPerson]. _This is an intrinsic permission and is the default behaviour if the user has no other permissions._
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

A staff member with the `bl0_admin` permission will be able to access Proposal(s) and Session(s) allocated on beamlines `BL01` and `BL02`, but not other beamlines.
