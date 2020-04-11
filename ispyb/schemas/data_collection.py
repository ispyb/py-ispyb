
from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields as f_fields

data_collection_dict = {
        'dataCollectionId': f_fields.Integer(),
        'BLSAMPLEID': f_fields.Integer(),
        'SESSIONID': f_fields.Integer(),
        'experimenttype': f_fields.String(),
        'dataCollectionNumber': f_fields.Integer(),
        'startTime': f_fields.Integer(),
        'endTime': f_fields.Integer(),
        'runStatus': f_fields.String(),
        'axisStart': f_fields.String(),
        'axisEnd': f_fields.String(),
        'axisRange': f_fields.String(),
        'overlap': f_fields.String(),
        'numberOfImages': f_fields.Integer(),
        'startImageNumber': f_fields.Integer(),
        'numberOfPasses': f_fields.Integer(),
        'exposureTime': f_fields.Integer(),
        'imageDirectory': f_fields.String(),
        'imagePrefix': f_fields.String(),
        'imageSuffix': f_fields.String(),
        'imageContainerSubPath': f_fields.String(),
        'fileTemplate': f_fields.String(),
        'wavelength': f_fields.String(),
        'resolution': f_fields.String(),
        'detectorDistance': f_fields.String(),
        'xBeam': f_fields.String(),
        'yBeam': f_fields.String(),
        'comments': f_fields.String(),
        'printableForReport': f_fields.String(),
        'CRYSTALCLASS': f_fields.String(),
        'slitGapVertical': f_fields.String(),
        'slitGapHorizontal': f_fields.String(),
        'transmission': f_fields.String(),
        'synchrotronMode': f_fields.String(),
        'xtalSnapshotFullPath1': f_fields.String(),
        'xtalSnapshotFullPath2': f_fields.String(),
        'xtalSnapshotFullPath3': f_fields.String(),
        'xtalSnapshotFullPath4': f_fields.String(),
        'rotationAxis': f_fields.String(),
        'phiStart': f_fields.String(),
        'kappaStart': f_fields.String(),
        'omegaStart': f_fields.String(),
        'chiStart': f_fields.String(),
        'resolutionAtCorner': f_fields.String(),
        'detector2Theta': f_fields.String(),
        'DETECTORMODE': f_fields.String(),
        'undulatorGap1': f_fields.String(),
        'undulatorGap2': f_fields.String(),
        'undulatorGap3': f_fields.String(),
        'beamSizeAtSampleX': f_fields.String(),
        'beamSizeAtSampleY': f_fields.String(),
        'centeringMethod': f_fields.String(),
        'averageTemperature': f_fields.String(),
        'ACTUALSAMPLEBARCODE': f_fields.String(),
        'ACTUALSAMPLESLOTINCONTAINER': f_fields.Integer(),
        'ACTUALCONTAINERBARCODE': f_fields.String(),
        'ACTUALCONTAINERSLOTINSC': f_fields.Integer(),
        'actualCenteringPosition': f_fields.String(),
        'beamShape': f_fields.String(),
        'dataCollectionGroupId': f_fields.Integer(),
        'POSITIONID': f_fields.Integer(),
        'detectorId': f_fields.Integer(),
        'FOCALSPOTSIZEATSAMPLEX': f_fields.Integer(),
        'POLARISATION': f_fields.Integer(),
        'FOCALSPOTSIZEATSAMPLEY': f_fields.Integer(),
        'APERTUREID': f_fields.Integer(),
        'screeningOrigId': f_fields.Integer(),
        'startPositionId': f_fields.Integer(),
        'endPositionId': f_fields.Integer(),
        'flux': f_fields.Integer(),
        'strategySubWedgeOrigId': f_fields.Integer(),
        'blSubSampleId': f_fields.Integer(),
        'flux_end': f_fields.Integer(),
        'bestWilsonPlotPath': f_fields.String(),
        'processedDataFile': f_fields.String(),
        'datFullPath': f_fields.String(),
        'magnification': f_fields.String(),
        'totalAbsorbedDose': f_fields.String(),
        'binning': f_fields.String(),
        'particleDiameter': f_fields.String(),
        'boxSize_CTF': f_fields.String(),
        'minResolution': f_fields.String(),
        'minDefocus': f_fields.String(),
        'maxDefocus': f_fields.String(),
        'defocusStepSize': f_fields.String(),
        'amountAstigmatism': f_fields.String(),
        'extractSize': f_fields.String(),
        'bgRadius': f_fields.String(),
        'voltage': f_fields.String(),
        'objAperture': f_fields.String(),
        'c1aperture': f_fields.String(),
        'c2aperture': f_fields.String(),
        'c3aperture': f_fields.String(),
        'c1lens': f_fields.String(),
        'c2lens': f_fields.String(),
        'c3lens': f_fields.String(),
        'totalExposedDose': f_fields.String(),
        'nominalMagnification': f_fields.String(),
        'nominalDefocus': f_fields.String(),
        'imageSizeX': f_fields.String(),
        'imageSizeY': f_fields.String(),
        'pixelSizeOnImage': f_fields.String(),
        'phasePlate': f_fields.String(),
        }

class DataCollectionSchema(Schema):
    dataCollectionId = ma_fields.Integer()
    BLSAMPLEID = ma_fields.Integer()
    SESSIONID = ma_fields.Integer()
    experimenttype = ma_fields.String()
    dataCollectionNumber = ma_fields.Integer()
    startTime = ma_fields.Integer()
    endTime = ma_fields.Integer()
    runStatus = ma_fields.String()
    axisStart = ma_fields.String()
    axisEnd = ma_fields.String()
    axisRange = ma_fields.String()
    overlap = ma_fields.String()
    numberOfImages = ma_fields.Integer()
    startImageNumber = ma_fields.Integer()
    numberOfPasses = ma_fields.Integer()
    exposureTime = ma_fields.Integer()
    imageDirectory = ma_fields.String()
    imagePrefix = ma_fields.String()
    imageSuffix = ma_fields.String()
    imageContainerSubPath = ma_fields.String()
    fileTemplate = ma_fields.String()
    wavelength = ma_fields.String()
    resolution = ma_fields.String()
    detectorDistance = ma_fields.String()
    xBeam = ma_fields.String()
    yBeam = ma_fields.String()
    comments = ma_fields.String()
    printableForReport = ma_fields.String()
    CRYSTALCLASS = ma_fields.String()
    slitGapVertical = ma_fields.String()
    slitGapHorizontal = ma_fields.String()
    transmission = ma_fields.String()
    synchrotronMode = ma_fields.String()
    xtalSnapshotFullPath1 = ma_fields.String()
    xtalSnapshotFullPath2 = ma_fields.String()
    xtalSnapshotFullPath3 = ma_fields.String()
    xtalSnapshotFullPath4 = ma_fields.String()
    rotationAxis = ma_fields.String()
    phiStart = ma_fields.String()
    kappaStart = ma_fields.String()
    omegaStart = ma_fields.String()
    chiStart = ma_fields.String()
    resolutionAtCorner = ma_fields.String()
    detector2Theta = ma_fields.String()
    DETECTORMODE = ma_fields.String()
    undulatorGap1 = ma_fields.String()
    undulatorGap2 = ma_fields.String()
    undulatorGap3 = ma_fields.String()
    beamSizeAtSampleX = ma_fields.String()
    beamSizeAtSampleY = ma_fields.String()
    centeringMethod = ma_fields.String()
    averageTemperature = ma_fields.String()
    ACTUALSAMPLEBARCODE = ma_fields.String()
    ACTUALSAMPLESLOTINCONTAINER = ma_fields.Integer()
    ACTUALCONTAINERBARCODE = ma_fields.String()
    ACTUALCONTAINERSLOTINSC = ma_fields.Integer()
    actualCenteringPosition = ma_fields.String()
    beamShape = ma_fields.String()
    dataCollectionGroupId = ma_fields.Integer()
    POSITIONID = ma_fields.Integer()
    detectorId = ma_fields.Integer()
    FOCALSPOTSIZEATSAMPLEX = ma_fields.Integer()
    POLARISATION = ma_fields.Integer()
    FOCALSPOTSIZEATSAMPLEY = ma_fields.Integer()
    APERTUREID = ma_fields.Integer()
    screeningOrigId = ma_fields.Integer()
    startPositionId = ma_fields.Integer()
    endPositionId = ma_fields.Integer()
    flux = ma_fields.Integer()
    strategySubWedgeOrigId = ma_fields.Integer()
    blSubSampleId = ma_fields.Integer()
    flux_end = ma_fields.Integer()
    bestWilsonPlotPath = ma_fields.String()
    processedDataFile = ma_fields.String()
    datFullPath = ma_fields.String()
    magnification = ma_fields.String()
    totalAbsorbedDose = ma_fields.String()
    binning = ma_fields.String()
    particleDiameter = ma_fields.String()
    boxSize_CTF = ma_fields.String()
    minResolution = ma_fields.String()
    minDefocus = ma_fields.String()
    maxDefocus = ma_fields.String()
    defocusStepSize = ma_fields.String()
    amountAstigmatism = ma_fields.String()
    extractSize = ma_fields.String()
    bgRadius = ma_fields.String()
    voltage = ma_fields.String()
    objAperture = ma_fields.String()
    c1aperture = ma_fields.String()
    c2aperture = ma_fields.String()
    c3aperture = ma_fields.String()
    c1lens = ma_fields.String()
    c2lens = ma_fields.String()
    c3lens = ma_fields.String()
    totalExposedDose = ma_fields.String()
    nominalMagnification = ma_fields.String()
    nominalDefocus = ma_fields.String()
    imageSizeX = ma_fields.String()
    imageSizeY = ma_fields.String()
    pixelSizeOnImage = ma_fields.String()
    phasePlate = ma_fields.String()
