from datetime import datetime
from random import randint
import uuid


proposal_create = [
    {
        'description': 'create a test proposal along with its laboratory and contact',
        'input': {
            'laboratory': {
                'laboratoryUUID': 'UUID',
                'name': 'Test lab',
                'address': 'Test address',
                'city': 'City',
                'country': 'Country',
                'url': 'url',
                'organization': 'Test org',
                'laboratoryPk': 0,
                'postcode': 'Test code',
            },
            'person': {
                'laboratoryId': None,
                'personUUID': 'Person uuid',
                'familyName': 'Family',
                'givenName': 'Name',
                'title': 'Dr',
                'emailAddress': 'email',
                'phoneNumber': '2233',
                'login': uuid.uuid4().hex.upper()[0:6],
                'faxNumber': '222',
                'cache': 'string',
            },
            'proposal':{
                'proposalCode': 'MX',
                'title': 'Test proposal',
                'proposalType': 'MX',
                'personId': None,
                'proposalNumber': randint(1, 1e5),
                'state': 'Open',
            }
        },
        'expected': {
            'code': 200
        }
    },
    {
        'description': 'create an incorrect proposal',
        'input': {
            'laboratory': {
                'laboratoryUUID': 'UUID',
                'name': 'Test lab',
                'address': 'Test address',
                'city': 'City',
                'country': 'Country',
                'url': 'url',
                'organization': 'Test org',
                'laboratoryPk': 0,
                'postcode': 'Test code',
            },
            'person': {
                'laboratoryId': None,
                'personUUID': 'Person uuid',
                'familyName': 'Family',
                'givenName': 'Name',
                'title': 'Dr',
                'emailAddress': 'email',
                'phoneNumber': '2233',
                'login': uuid.uuid4().hex.upper()[0:6],
                'faxNumber': '222',
                'cache': 'string',
            },
            'proposal':{
                'proposalCode': 'MX',
                'title': 'Test proposal',
                'proposalType': 'MX',
                'personId': None,
                'proposalNumber': randint(1, 1e5),
                'state': 'Error',
            }
        },
        'expected': {
            'code': 400
        }
    }
]
