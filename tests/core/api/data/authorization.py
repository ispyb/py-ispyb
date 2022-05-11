test_data_session = [
    {
        "name": "all_sessions permission OK",
        "input": {
            "permissions": [
                "all_sessions",
            ],
            "username": "admin",
            "route": "/em/session/70566/stats",
        },
        "expected": {"code": 200},
    },
    {
        "name": "no all_sessions permission DENIED",
        "input": {
            "permissions": ["none"],
            "username": "admin",
            "route": "/em/session/70566/stats",
        },
        "expected": {"code": 403},
    },
    {
        "name": "own_sessions permission OK (proposal.personId)",
        "input": {
            "permissions": [
                "own_sessions",
            ],
            "username": "pasteur",
            "route": "/em/session/70566/stats",
        },
        "expected": {"code": 200},
    },
    {
        "name": "no own_sessions permission DENIED (proposal.personId)",
        "input": {
            "permissions": ["none"],
            "username": "70565",
            "route": "/em/session/70566/stats",
        },
        "expected": {"code": 403},
    },
    {
        "name": "own_sessions permission OK (Session_has_Person.personId)",
        "input": {
            "permissions": [
                "own_sessions",
            ],
            "username": "darwin",
            "route": "/em/session/70565/stats",
        },
        "expected": {"code": 200},
    },
    {
        "name": "no own_sessions permission DENIED (Session_has_Person.personId)",
        "input": {
            "permissions": [
                "none",
            ],
            "username": "darwin",
            "route": "/em/session/70565/stats",
        },
        "expected": {"code": 403},
    },
    {
        "name": "own_sessions permission DENIED",
        "input": {
            "permissions": [
                "own_sessions",
            ],
            "username": "user",
            "route": "/em/session/70566/stats",
        },
        "expected": {"code": 403},
    },
]

test_data_proposal = [
    {
        "name": "all_proposals permission OK",
        "input": {
            "permissions": [
                "all_proposals",
            ],
            "username": "admin",
            "route": "/proposals/MX1",
        },
        "expected": {"code": 200},
    },
    {
        "name": "no all_proposals permission DENIED",
        "input": {
            "permissions": ["none"],
            "username": "admin",
            "route": "/proposals/MX1",
        },
        "expected": {"code": 403},
    },
    {
        "name": "own_proposals permission OK (proposal.personId)",
        "input": {
            "permissions": [
                "own_proposals",
            ],
            "username": "pasteur",
            "route": "/proposals/MX1",
        },
        "expected": {"code": 200},
    },
    {
        "name": "no own_proposals permission DENIED (proposal.personId)",
        "input": {
            "permissions": ["none"],
            "username": "pasteur",
            "route": "/proposals/MX1",
        },
        "expected": {"code": 403},
    },
    {
        "name": "own_proposals permission DENIED",
        "input": {
            "permissions": [
                "own_proposals",
            ],
            "username": "user",
            "route": "/proposals/MX1",
        },
        "expected": {"code": 403},
    },
]
