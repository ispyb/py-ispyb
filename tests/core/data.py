import time

from datetime import datetime
from random import randint
import uuid

test_proposal = {
    "proposalCode": "MX",
    "title": "Test proposal",
    "proposalType": "MX",
    "personId": 1,
    "proposalNumber": "111",
    #"bltimeStamp": datetime.strptime("2015-12-21 16:20:43", "%Y-%m-%d %H:%M:%S"),
    "state": "Open",
}

def get_test_proposal():
    proposal = test_proposal
    proposal["proposalNumber"] = randint(1, 1e5)
    return proposal

test_beam_calendar = {
    "run": "1",
    "beamStatus": "Open",
    "endDate":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "startDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

test_session = {
    "bltimeStamp": "2015-12-21 16:20:44",
    "proposalId": 37027,
    "beamLineName": "i03",
    "visit_number": 2,
    "archived": 0,
    "beamLineSetupId": 1,
    "endDate":  "2015-12-21 16:20:44",
    "startDate": "2015-12-21 16:20:44",
}


test_data_collection = {
    "binning": 1,
    "FOCALSPOTSIZEATSAMPLEY": 20,
    "detectorDistance": 193.087,
    "xtalSnapshotFullPath3": "/path/to_snapshot3",
    "printableForReport": 1,
    "dataCollectionGroupId": 988855,
    "slitGapHorizontal": 0.099937,
    "axisStart": 45,
    "xtalSnapshotFullPath1": "/path/to_snapshot1",
    "imageDirectory": "/path/o/image/dir",
    "BLSAMPLEID": 374695,
    "xBeam": 215.62,
    "SESSIONID": 55167,
    "comments": "Test_comm",
    "fileTemplate": "tlys_jan_4_1_####.cbf",
    "imageSuffix": "cbf",
    "flux": 833107367454.3083,
    "overlap": 0,
    "wavelength": 1.28255,
    "axisEnd": 0.1,
    "slitGapVertical": 0.059918,
    "beamSizeAtSampleX": 0.05,
    "omegaStart": 45,
    "endTime": datetime.strptime("2016-01-14 12:41:54", "%Y-%m-%d %H:%M:%S"),
    "dataCollectionNumber": 1,
    "imagePrefix": "tlys_jan_4",
    "xtalSnapshotFullPath4": "/path/to_snapshot4",
    "yBeam": 208.978,
    "synchrotronMode": "User",
    "numberOfPasses": 1,
    "resolution": 1.6,
    "undulatorGap1": 5.685,
    "xtalSnapshotFullPath2": "/path/to_snapshot2",
    "FOCALSPOTSIZEATSAMPLEX": 80,
    "runStatus": "DataCollection Successful",
    "dataCollectionId": 993677,
    "axisRange": 0.1,
    "POSITIONID": 595236,
    "numberOfImages": 3600,
    "beamSizeAtSampleY": 0.02,
    "transmission": 40.1936,
    "startImageNumber": 1,
    "rotationAxis": "Omega",
    "exposureTime": 0.02,
    "startTime": datetime.strptime("2016-01-14 12:40:34", "%Y-%m-%d %H:%M:%S"),
}

test_lab_contact = {
    "personId": 1,
    "cardName": "Card",
    "proposalId": 37027,
    "defaultCourrierCompany": "DHL",
    "courierAccount": "01",
    "billingReference": "02",
    "dewarAvgCustomsValue": 0,
    "dewarAvgTransportValue": 0,
}

test_shippment = {
    "proposalId": 37027,
    "shippingName": "Test shipment",
    "deliveryAgent_agentName": "DHL",
    "deliveryAgent_agentCode": "Code",
    "deliveryAgent_flightCode": "Code",
    "shippingStatus": "Open",
    "laboratoryId": 1,
    "isStorageShipping": 0,
    "comments": "Comment",
    "sendingLabContactId": 1,
    "returnLabContactId": 1,
    "returnCourier": "DHL",
    "deliveryAgent_label": "Label",
    "physicalLocation": "Store",
}

test_laboratory = {
    "laboratoryUUID": "UUID",
    "name": "Test lab",
    "address": "Test address",
    "city": "City",
    "country": "Country",
    "url": "url",
    "organization": "Test org",
    "laboratoryPk": 0,
    "postcode": "Test code"
}

test_person = {
    "laboratoryId": 1,
    "personUUID": "Person uuid",
    "familyName": "Family",
    "givenName": "Name",
    "title": "Dr",
    "emailAddress": "email",
    "phoneNumber": "2233",
    "login": "login",
    "faxNumber": "222",
    "cache": "string",
}

def get_test_person():
    test_person_dict = test_person
    test_person_dict["login"] = uuid.uuid4().hex.upper()[0:6]
    return test_person_dict

test_detector = {
    "detectorType": "PixelCounting",
    "detectorManufacturer": "TestManufacturer",
    "detectorModel": "T1",
    "detectorPixelSizeHorizontal": 0.75,
    "detectorPixelSizeVertical": 0.75,
    "DETECTORMAXRESOLUTION": 0.6,
    "DETECTORMINRESOLUTION": 6,
    "detectorSerialNumber": "00AA11",
    "detectorDistanceMin": "100",
    "detectorDistanceMax": "1000",
    "trustedPixelValueRangeLower": "1",
    "trustedPixelValueRangeUpper": "2",
    "sensorThickness": 1,
    "overload": 1,
    "XGeoCorr": "100",
    "YGeoCorr": "200",
    "detectorMode": "testMode",
    "density": 1,
    "composition": "comp",
    "numberOfPixelsX": 8000,
    "numberOfPixelsY": 8000,
    "detectorRollMin": "1",
    "detectorRollMax": "2",
    "localName": "TestDetector"
}

def get_test_detector():
    test_detector_dict = test_detector
    test_detector_dict["detectorSerialNumber"] = uuid.uuid4().hex.upper()[0:6]
    return test_detector_dict

test_beamline_setup = {
    "detectorId": 0,
    "synchrotronMode": "Test mode",
    "undulatorType1": "Si111",
    "focalSpotSizeAtSample": 10,
    "focusingOptic": "CRL",
    "beamDivergenceHorizontal": 0.1,
    "beamDivergenceVertical": 0.1,
    "polarisation": 0,
    "monochromatorType": "T",
    "setupDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "synchrotronName": "TestSynch",
    "maxExpTimePerDataCollection": "0.04",
    "maxExposureTimePerImage": 10,
    "minExposureTimePerImage": "0",
    "goniostatMaxOscillationSpeed": "1",
    "goniostatMaxOscillationWidth": "1",
    "goniostatMinOscillationWidth": "1",
    "maxTransmission": "100",
    "minTransmission": "0",
    "beamlineName": "testBeamline",
    "beamSizeXMin": 10,
    "beamSizeXMax": 200,
    "beamSizeYMin": 10,
    "beamSizeYMax": 200,
    "energyMin": 5,
    "energyMax": 15,
    "omegaMin": 0,
    "omegaMax": 360,
    "kappaMin": 0,
    "kappaMax": 360,
    "phiMin": 0,
    "phiMax": 180,
    "active": 0,
    "numberOfImagesMax": 1000000,
    "numberOfImagesMin": 1,
}

test_protein = {
    "proposalId": 37027,
    "name": "Protein name",
    "acronym": "ancr",
    "molecularMass": "2",
    "proteinType": "2",
    "personId": 1
}

test_diffraction_plan = {
    "name": "Test",
    "experimentKind": "OSC",
    "observedResolution": 2,
    "minimalResolution": 2,
    "exposureTime": 0.04,
    "oscillationRange": 360,
    "maximalResolution": 1,
    "screeningResolution": 2,
    "radiationSensitivity": 0,
    "preferredBeamSizeX": 20,
    "preferredBeamSizeY": 20,
    "preferredBeamDiameter": 20,
    "comments": "Test comment",
    "DIFFRACTIONPLANUUID": "uuid",
    "aimedCompleteness": "99",
    "aimedIOverSigmaAtHighestRes": "1",
    "aimedMultiplicity": "1",
    "aimedResolution": "1",
    "anomalousData": 0,
    "complexity": "1",
    "estimateRadiationDamage": 0,
    "forcedSpaceGroup": "P4",
    "requiredCompleteness": "99",
    "requiredMultiplicity": "1",
    "requiredResolution": "1",
    "numberOfPositions": 1,
    "minOscWidth": 0.1,
    "energy": 12.70,
    "transmission": 100,
    "kappaStart": 0,
    "axisStart": 0,
    "axisRange": 0.1,
    "numberOfImages": 3600,
    "beamLineName": "test beamline",
    "distance": "200",
}

test_crystal = {
    "diffractionPlanId": 0,
    "proteinId": 0,
    "crystalUUID": "crUUID",
    "name": "Test crystal",
    "spaceGroup": "P4",
    "morphology": "No",
    "color": "Green",
    "size_X": "10",
    "size_Y": "10",
    "size_Z": "100",
    "cell_a": "1",
    "cell_b": "1",
    "cell_c": "1",
    "cell_alpha": "2",
    "cell_beta": "2",
    "cell_gamma": "2",
    "comments": "Comment",
    "pdbFileName": "pdf_filename",
    "pdbFilePath": "pdf_filen_path",
    "abundance": 0,
    "theoreticalDensity": 0
}

test_sample = {
    "blSampleId": 0,
    "diffractionPlanId": 0,
    "crystalId": 0,
    "containerId": 0,
    "name": "Test sample",
    "code": "code",
    "location": "1",
    "holderLength": "22",
    "loopLength": "22",
    "loopType": "N",
    "wireWidth": "1",
    "comments": "Test comment",
    "isInSampleChanger": 0,
    "POSITIONID": 0,
    "SMILES": "string",
    "blSubSampleId": 0,
    "lastImageURL": "string",
    "screenComponentGroupId": 0,
    "volume": 0,
    "packingFraction": 0,
    "preparationTemeprature": 0,
    "preparationHumidity": 0,
    "blottingTime": 0,
    "blottingForce": 0,
    "blottingDrainTime": 0,
    "support": "string",
    "subLocation": 0
}

test_container = {
    "dewarId": 0,
    "code": "code",
    "containerType": "cane",
    "capacity": 10,
    "sampleChangerLocation": "1",
    "containerStatus": "ready",
    "beamlineLocation": "no",
    "screenId": 0,
    "scheduleId": 0,
    "barcode": "barcode",
    "imagerId": 0,
    "sessionId": 0,
    "ownerId": 0,
    "requestedImagerId": 0,
    "requestedReturn": 0,
    "comments": "string",
    "experimentType": "MX",
    "storageTemperature": 8,
    "containerRegistryId": 0
}

test_dewar = {
    "shippingId": 0,
    "code": "00001",
    "comments": "comments",
    "storageLocation": "string",
    "dewarStatus": "open",
    "isStorageDewar": 1,
    "barCode": "code",
    "firstExperimentId": 0,
    "customsValue": 10,
    "transportValue": 100,
    "trackingNumberToSynchrotron": "00001",
    "trackingNumberFromSynchrotron": "00002",
    "type": "Dewar",
    "FACILITYCODE": "fac",
    "weight": 30,
    "deliveryAgent_barcode": "test"
}

def get_test_dewar():
    dewar_dict = test_dewar
    dewar_dict["barCode"] = uuid.uuid4().hex.upper()[0:6]
    return dewar_dict
