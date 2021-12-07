test_data = [
    {
        "route": "/contacts/labs",
        "code": 200,
        "id": "laboratoryId",
        "patch": {"name": "Modified name"}
    },
    {
        "route": "/contacts/persons",
        "code": 200,
        "id": "personId",
        "patch": {"familyName": "Modified name", "phoneNumber": "0172-12233"}
    },
    {
        "route": "/contacts/lab_contacts",
        "code": 200,
        "id": "labContactId",
        "patch": {"defaultCourrierCompany": "FedEX"}
    },
    {
        "route": "/beamline/detectors",
        "code": 200,
        "id": "detectorId",
        "patch": {"detectorModel": "T1_0001"}
    },
    {
        "route": "/beamline/setups",
        "code": 200,
        "id": "beamLineSetupId",
        "patch": {"synchrotronName": "Error"}
    },
    {
        "route": "/samples/proteins",
        "code": 200,
        "id": "proteinId",
        "patch": {"molecularMass": "200"}
    },
    {
        "route": "/samples/diffraction_plans",
        "code": 200,
        "id": "diffractionPlanId",
        "patch": {"observedResolution": "3"}
    },
    {
        "route": "/samples/crystals",
        "code": 200,
        "id": "crystalId",
        "patch": {"spaceGroup": "P2"}
    },
    {
        "route": "/samples",
        "code": 200,
        "id": "blSampleId",
        "patch": {"location": "2"}
    }
]
