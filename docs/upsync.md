# User Portal Sync

To import/sync User Portal data into py-ISPyB each facility needs to create a specific JSON structure as input for the sync route.

Currently, there is a single API route to import a proposal including: sessions, lab contacts, proteins, etc.

The API endpoint is using a JSON schema to validate the incoming data.

## JSON schema

To get the current User Portal Sync JSON schema just use the following API route: `/ispyb/api/v1/webservices/userportalsync/sync_proposal/schema`

Your User Portal application may use this route to test/validate the input data.

## Syncronize a proposal

To sync a proposal just use the following route: `/ispyb/api/v1/webservices/userportalsync/sync_proposal`

You may check more information about the User Portal Sync routes/endpoints at:
[https://ispyb.github.io/py-ispyb/api/](https://ispyb.github.io/py-ispyb/api/)

or by running a local version of py-ISPyB and simply opening the `/docs` route.

## Example JSON data

You can check for User Portal Sync JSON example data at:
[https://github.com/ispyb/py-ispyb/tree/master/tests/core/api/data](https://github.com/ispyb/py-ispyb/tree/master/tests/core/api/data)

## Sync process details per entity

The sync process currently takes into account two options to establish the relation between the User Portal entities and the ISPyB DB, in order to keep backward compatibility with the legacy ISPyB Java API. The externalId field currently present in several ISPyB entities, is a MySQL binary(16) field. A binary(16) field can contain maximum 16 characters. The externalId fields must be properly encoded/decoded when dealing with the DB, and this is not the case with the Java API, since those fields were never used by it.

The externalId fields can keep an encoded version of an external primary key or UUID from a User Portal to be able to create an entity link between the User Portal and the ISPyB database.

At the time when the legacy Java API is not used anymore, it would be possible to switch exclusively to the externalId fields. 

### Person

The Person sync is based on the **externalId** field or the **login** field.

### Laboratory

The Laboratory sync is based on the **laboratoryExtPk** field or the laboratory **name** and **city** and **country** fields.

### Proposal

The Proposal sync is based on the **externalId** field or the **proposalCode** (Ex: "MX") and **proposalNumber** (Ex: "3456")

### Proposal participants

Every proposal participant will have a relation within the **ProposalHasPerson** table and only the first one in the proposal persons list (Ex: the PI/Leader) will be added as **personID** within the Proposal table.

### Lab Contacts

Every entry within the JSON proposal persons list will create/update a lab contact entity in the DB. 

The Lab Contact sync is based on the **cardName** field.

### Proteins

The Protein sync is based on the **externalId** field or the **acronym** field.

### Sessions

The Session sync is based on the **externalId** field or the **expSessionPk** field.

### Session participants

Every session participant will have a relation within the **Session_has_Person** table.