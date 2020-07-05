# coding: utf-8
from sqlalchemy import (
    BINARY,
    BigInteger,
    Column,
    Date,
    DateTime,
    Float,
    Index,
    Integer,
    LargeBinary,
    SmallInteger,
    String,
    Table,
    Text,
    Time,
)
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.enumerated import ENUM
from sqlalchemy.dialects.mysql.types import LONGBLOB
from flask_sqlalchemy import SQLAlchemy


from app.extensions import db


class AbInitioModel(db.Model):
    __tablename__ = "AbInitioModel"

    abInitioModelId = db.Column(db.Integer, primary_key=True)
    modelListId = db.Column(db.Integer, index=True)
    averagedModelId = db.Column(db.Integer, index=True)
    rapidShapeDeterminationModelId = db.Column(db.Integer, index=True)
    shapeDeterminationModelId = db.Column(db.Integer, index=True)
    comments = db.Column(db.String(512))
    creationTime = db.Column(db.DateTime)


class Additive(db.Model):
    __tablename__ = "Additive"

    additiveId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    additiveType = db.Column(db.String(45))
    comments = db.Column(db.String(512))
    chemFormulaHead = db.Column(db.String(25), server_default=db.FetchedValue())
    chemFormulaTail = db.Column(db.String(25), server_default=db.FetchedValue())


class AdminActivity(db.Model):
    __tablename__ = "AdminActivity"

    adminActivityId = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(45), nullable=False, unique=True, server_default=db.FetchedValue()
    )
    action = db.Column(db.String(45), index=True)
    comments = db.Column(db.String(100))
    dateTime = db.Column(db.DateTime)


class AdminVar(db.Model):
    __tablename__ = "AdminVar"

    varId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    value = db.Column(db.String(1024), index=True)


class Aperture(db.Model):
    __tablename__ = "Aperture"

    apertureId = db.Column(db.Integer, primary_key=True)
    sizeX = db.Column(db.Float)


class Assembly(db.Model):
    __tablename__ = "Assembly"

    assemblyId = db.Column(db.Integer, primary_key=True)
    macromoleculeId = db.Column(db.Integer, nullable=False, index=True)
    creationDate = db.Column(db.DateTime)
    comments = db.Column(db.String(255))


class AssemblyHasMacromolecule(db.Model):
    __tablename__ = "AssemblyHasMacromolecule"

    AssemblyHasMacromoleculeId = db.Column(db.Integer, primary_key=True)
    assemblyId = db.Column(db.Integer, nullable=False, index=True)
    macromoleculeId = db.Column(db.Integer, nullable=False, index=True)


class AssemblyRegion(db.Model):
    __tablename__ = "AssemblyRegion"

    assemblyRegionId = db.Column(db.Integer, primary_key=True)
    assemblyHasMacromoleculeId = db.Column(db.Integer, nullable=False, index=True)
    assemblyRegionType = db.Column(db.String(45))
    name = db.Column(db.String(45))
    fromResiduesBases = db.Column(db.String(45))
    toResiduesBases = db.Column(db.String(45))


class AutoProc(db.Model):
    __tablename__ = "AutoProc"

    autoProcId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcProgramId = db.Column(db.Integer, index=True, info="Related program item")
    spaceGroup = db.Column(db.String(45), info="Space group")
    refinedCell_a = db.Column(db.Float, info="Refined cell")
    refinedCell_b = db.Column(db.Float, info="Refined cell")
    refinedCell_c = db.Column(db.Float, info="Refined cell")
    refinedCell_alpha = db.Column(db.Float, info="Refined cell")
    refinedCell_beta = db.Column(db.Float, info="Refined cell")
    refinedCell_gamma = db.Column(db.Float, info="Refined cell")
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")


class AutoProcIntegration(db.Model):
    __tablename__ = "AutoProcIntegration"

    autoProcIntegrationId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    dataCollectionId = db.Column(
        db.Integer, nullable=False, index=True, info="DataCollection item"
    )
    autoProcProgramId = db.Column(db.Integer, index=True, info="Related program item")
    startImageNumber = db.Column(db.Integer, info="start image number")
    endImageNumber = db.Column(db.Integer, info="end image number")
    refinedDetectorDistance = db.Column(
        db.Float, info="Refined DataCollection.detectorDistance"
    )
    refinedXBeam = db.Column(db.Float, info="Refined DataCollection.xBeam")
    refinedYBeam = db.Column(db.Float, info="Refined DataCollection.yBeam")
    rotationAxisX = db.Column(db.Float, info="Rotation axis")
    rotationAxisY = db.Column(db.Float, info="Rotation axis")
    rotationAxisZ = db.Column(db.Float, info="Rotation axis")
    beamVectorX = db.Column(db.Float, info="Beam vector")
    beamVectorY = db.Column(db.Float, info="Beam vector")
    beamVectorZ = db.Column(db.Float, info="Beam vector")
    cell_a = db.Column(db.Float, info="Unit cell")
    cell_b = db.Column(db.Float, info="Unit cell")
    cell_c = db.Column(db.Float, info="Unit cell")
    cell_alpha = db.Column(db.Float, info="Unit cell")
    cell_beta = db.Column(db.Float, info="Unit cell")
    cell_gamma = db.Column(db.Float, info="Unit cell")
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")
    anomalous = db.Column(
        db.Integer,
        server_default=db.FetchedValue(),
        info="boolean type:0 noanoum - 1 anoum",
    )


class AutoProcProgram(db.Model):
    __tablename__ = "AutoProcProgram"

    autoProcProgramId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    dataCollectionId = db.Column(db.Integer, index=True)
    processingCommandLine = db.Column(
        db.String(255), info="Command line for running the automatic processing"
    )
    processingPrograms = db.Column(
        db.String(255), info="Processing programs (comma separated)"
    )
    processingStatus = db.Column(
        db.ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"), info="success (1) / fail (0)"
    )
    processingMessage = db.Column(db.String(255), info="warning, error,...")
    processingStartTime = db.Column(db.DateTime, info="Processing start time")
    processingEndTime = db.Column(db.DateTime, info="Processing end time")
    processingEnvironment = db.Column(db.String(255), info="Cpus, Nodes,...")
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")
    processingJobId = db.Column(db.Integer, nullable=False)


class AutoProcProgramAttachment(db.Model):
    __tablename__ = "AutoProcProgramAttachment"

    autoProcProgramAttachmentId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcProgramId = db.Column(
        db.Integer, nullable=False, index=True, info="Related autoProcProgram item"
    )
    fileType = db.Column(
        db.ENUM("Log", "Result", "Graph"), info="Type of file Attachment"
    )
    fileName = db.Column(db.String(255), info="Attachment filename")
    filePath = db.Column(db.String(255), info="Attachment filepath to disk storage")
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")


class AutoProcProgramMessage(db.Model):
    __tablename__ = "AutoProcProgramMessage"

    autoProcProgramMessageId = db.Column(db.Integer, primary_key=True)
    autoProcProgramId = db.Column(db.Integer, index=True)
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    severity = db.Column(db.ENUM("ERROR", "WARNING", "INFO"))
    message = db.Column(db.String(200))
    description = db.Column(db.Text)


class AutoProcScaling(db.Model):
    __tablename__ = "AutoProcScaling"
    __table_args__ = (
        db.Index("AutoProcScalingIdx1", "autoProcScalingId", "autoProcId"),
    )

    autoProcScalingId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcId = db.Column(
        db.Integer, index=True, info="Related autoProc item (used by foreign key)"
    )
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")
    resolutionEllipsoidAxis11 = db.Column(
        db.Float, info="Eigenvector for first diffraction limit, coord 1"
    )
    resolutionEllipsoidAxis12 = db.Column(
        db.Float, info="Eigenvector for first diffraction limit, coord 2"
    )
    resolutionEllipsoidAxis13 = db.Column(
        db.Float, info="Eigenvector for first diffraction limit, coord 3"
    )
    resolutionEllipsoidAxis21 = db.Column(
        db.Float, info="Eigenvector for second diffraction limit, coord 1"
    )
    resolutionEllipsoidAxis22 = db.Column(
        db.Float, info="Eigenvector for second diffraction limit, coord 2"
    )
    resolutionEllipsoidAxis23 = db.Column(
        db.Float, info="Eigenvector for second diffraction limit, coord 3"
    )
    resolutionEllipsoidAxis31 = db.Column(
        db.Float, info="Eigenvector for third diffraction limit, coord 1"
    )
    resolutionEllipsoidAxis32 = db.Column(
        db.Float, info="Eigenvector for third diffraction limit, coord 2"
    )
    resolutionEllipsoidAxis33 = db.Column(
        db.Float, info="Eigenvector for third diffraction limit, coord 3"
    )
    resolutionEllipsoidValue1 = db.Column(
        db.Float, info="First (anisotropic) diffraction limit"
    )
    resolutionEllipsoidValue2 = db.Column(
        db.Float, info="Second (anisotropic) diffraction limit"
    )
    resolutionEllipsoidValue3 = db.Column(
        db.Float, info="Third (anisotropic) diffraction limit"
    )


class AutoProcScalingStatistic(db.Model):
    __tablename__ = "AutoProcScalingStatistics"

    autoProcScalingStatisticsId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcScalingId = db.Column(
        db.Integer,
        index=True,
        info="Related autoProcScaling item (used by foreign key)",
    )
    scalingStatisticsType = db.Column(
        db.ENUM("overall", "innerShell", "outerShell"),
        nullable=False,
        index=True,
        server_default=db.FetchedValue(),
        info="Scaling statistics type",
    )
    comments = db.Column(db.String(255), info="Comments...")
    resolutionLimitLow = db.Column(db.Float, info="Low resolution limit")
    resolutionLimitHigh = db.Column(db.Float, info="High resolution limit")
    rMerge = db.Column(db.Float, info="Rmerge")
    rMeasWithinIPlusIMinus = db.Column(db.Float, info="Rmeas (within I+/I-)")
    rMeasAllIPlusIMinus = db.Column(db.Float, info="Rmeas (all I+ & I-)")
    rPimWithinIPlusIMinus = db.Column(db.Float, info="Rpim (within I+/I-) ")
    rPimAllIPlusIMinus = db.Column(db.Float, info="Rpim (all I+ & I-)")
    fractionalPartialBias = db.Column(db.Float, info="Fractional partial bias")
    nTotalObservations = db.Column(db.Integer, info="Total number of observations")
    nTotalUniqueObservations = db.Column(db.Integer, info="Total number unique")
    meanIOverSigI = db.Column(db.Float, info="Mean((I)/sd(I))")
    completeness = db.Column(db.Float, info="Completeness")
    multiplicity = db.Column(db.Float, info="Multiplicity")
    anomalousCompleteness = db.Column(db.Float, info="Anomalous completeness")
    anomalousMultiplicity = db.Column(db.Float, info="Anomalous multiplicity")
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")
    anomalous = db.Column(
        db.Integer,
        server_default=db.FetchedValue(),
        info="boolean type:0 noanoum - 1 anoum",
    )
    ccHalf = db.Column(db.Float, info="information from XDS")
    ccAno = db.Column(db.Float)
    sigAno = db.Column(db.String(45))
    isa = db.Column(db.String(45))
    completenessSpherical = db.Column(
        db.Float, info="Completeness calculated assuming isotropic diffraction"
    )
    completenessEllipsoidal = db.Column(
        db.Float, info="Completeness calculated allowing for anisotropic diffraction"
    )
    anomalousCompletenessSpherical = db.Column(
        db.Float,
        info="Anomalous completeness calculated assuming isotropic diffraction",
    )
    anomalousCompletenessEllipsoidal = db.Column(
        db.Float,
        info="Anisotropic completeness calculated allowing for anisotropic diffraction",
    )
    ccAnomalous = db.Column(db.Float)


class AutoProcScalingHasInt(db.Model):
    __tablename__ = "AutoProcScaling_has_Int"
    __table_args__ = (
        db.Index(
            "AutoProcScalingHasInt_FKIndex3",
            "autoProcScalingId",
            "autoProcIntegrationId",
        ),
    )

    autoProcScaling_has_IntId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcScalingId = db.Column(db.Integer, index=True, info="AutoProcScaling item")
    autoProcIntegrationId = db.Column(
        db.Integer, nullable=False, index=True, info="AutoProcIntegration item"
    )
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")


class AutoProcStatus(db.Model):
    __tablename__ = "AutoProcStatus"

    autoProcStatusId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcIntegrationId = db.Column(db.Integer, nullable=False, index=True)
    step = db.Column(
        db.ENUM("Indexing", "Integration", "Correction", "Scaling", "Importing"),
        nullable=False,
        info="autoprocessing step",
    )
    status = db.Column(
        db.ENUM("Launched", "Successful", "Failed"),
        nullable=False,
        info="autoprocessing status",
    )
    comments = db.Column(db.String(1024), info="comments")
    bltimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )


class BFAutomationError(db.Model):
    __tablename__ = "BF_automationError"

    automationErrorId = db.Column(db.Integer, primary_key=True)
    errorType = db.Column(db.String(40), nullable=False)
    solution = db.Column(db.Text)


class BFAutomationFault(db.Model):
    __tablename__ = "BF_automationFault"

    automationFaultId = db.Column(db.Integer, primary_key=True)
    automationErrorId = db.Column(db.Integer, index=True)
    containerId = db.Column(db.Integer, index=True)
    severity = db.Column(db.ENUM("1", "2", "3"))
    stacktrace = db.Column(db.Text)
    resolved = db.Column(db.Integer)
    faultTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )


class BFComponent(db.Model):
    __tablename__ = "BF_component"

    componentId = db.Column(db.Integer, primary_key=True)
    systemId = db.Column(db.Integer, index=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))


class BFComponentBeamline(db.Model):
    __tablename__ = "BF_component_beamline"

    component_beamlineId = db.Column(db.Integer, primary_key=True)
    componentId = db.Column(db.Integer, index=True)
    beamlinename = db.Column(db.String(20))


class BFFault(db.Model):
    __tablename__ = "BF_fault"

    faultId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.Integer, nullable=False, index=True)
    owner = db.Column(db.String(50))
    subcomponentId = db.Column(db.Integer, index=True)
    starttime = db.Column(db.DateTime)
    endtime = db.Column(db.DateTime)
    beamtimelost = db.Column(db.Integer)
    beamtimelost_starttime = db.Column(db.DateTime)
    beamtimelost_endtime = db.Column(db.DateTime)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    resolved = db.Column(db.Integer)
    resolution = db.Column(db.Text)
    assignee = db.Column(db.String(50))
    attachment = db.Column(db.String(200))
    eLogId = db.Column(db.Integer)
    personId = db.Column(db.Integer, index=True)
    assigneeId = db.Column(db.Integer, index=True)


class BFSubcomponent(db.Model):
    __tablename__ = "BF_subcomponent"

    subcomponentId = db.Column(db.Integer, primary_key=True)
    componentId = db.Column(db.Integer, index=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))


class BFSubcomponentBeamline(db.Model):
    __tablename__ = "BF_subcomponent_beamline"

    subcomponent_beamlineId = db.Column(db.Integer, primary_key=True)
    subcomponentId = db.Column(db.Integer, index=True)
    beamlinename = db.Column(db.String(20))


class BFSystem(db.Model):
    __tablename__ = "BF_system"

    systemId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))


class BFSystemBeamline(db.Model):
    __tablename__ = "BF_system_beamline"

    system_beamlineId = db.Column(db.Integer, primary_key=True)
    systemId = db.Column(db.Integer, index=True)
    beamlineName = db.Column(db.String(20))


class BLSample(db.Model):
    __tablename__ = "BLSample"
    __table_args__ = (db.Index("crystalId", "crystalId", "containerId"),)

    blSampleId = db.Column(db.Integer, primary_key=True)
    diffractionPlanId = db.Column(db.Integer, index=True)
    crystalId = db.Column(db.Integer, index=True)
    containerId = db.Column(db.Integer, index=True)
    name = db.Column(db.String(45), index=True)
    code = db.Column(db.String(45))
    location = db.Column(db.String(45))
    holderLength = db.Column(db.Float(asdecimal=True))
    loopLength = db.Column(db.Float(asdecimal=True))
    loopType = db.Column(db.String(45))
    wireWidth = db.Column(db.Float(asdecimal=True))
    comments = db.Column(db.String(1024))
    completionStage = db.Column(db.String(45))
    structureStage = db.Column(db.String(45))
    publicationStage = db.Column(db.String(45))
    publicationComments = db.Column(db.String(255))
    blSampleStatus = db.Column(db.String(20), index=True)
    isInSampleChanger = db.Column(db.Integer)
    lastKnownCenteringPosition = db.Column(db.String(255))
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )
    SMILES = db.Column(
        db.String(400),
        info="the symbolic description of the structure of a chemical compound",
    )
    lastImageURL = db.Column(db.String(255))
    positionId = db.Column(db.Integer)
    blSubSampleId = db.Column(db.Integer, index=True)
    screenComponentGroupId = db.Column(db.Integer, index=True)
    volume = db.Column(db.Float)
    dimension1 = db.Column(db.Float(asdecimal=True))
    dimension2 = db.Column(db.Float(asdecimal=True))
    dimension3 = db.Column(db.Float(asdecimal=True))
    shape = db.Column(db.String(15))
    subLocation = db.Column(
        db.SmallInteger,
        info="Indicates the sample's location on a multi-sample pin, where 1 is closest to the pin base",
    )
    packingfraction = db.Column(db.Float)


class BLSampleGroup(db.Model):
    __tablename__ = "BLSampleGroup"

    blSampleGroupId = db.Column(db.Integer, primary_key=True)


class BLSampleGroupHasBLSample(db.Model):
    __tablename__ = "BLSampleGroup_has_BLSample"

    blSampleGroupId = db.Column(db.Integer, primary_key=True, nullable=False)
    blSampleId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    order = db.Column(db.Integer)
    type = db.Column(db.ENUM("background", "container", "sample", "calibrant"))


class BLSampleImage(db.Model):
    __tablename__ = "BLSampleImage"

    blSampleImageId = db.Column(db.Integer, primary_key=True)
    blSampleId = db.Column(db.Integer, nullable=False, index=True)
    micronsPerPixelX = db.Column(db.Float)
    micronsPerPixelY = db.Column(db.Float)
    imageFullPath = db.Column(db.String(255))
    blSampleImageScoreId = db.Column(db.Integer)
    comments = db.Column(db.String(255))
    blTimeStamp = db.Column(db.DateTime)
    containerInspectionId = db.Column(db.Integer, index=True)
    modifiedTimeStamp = db.Column(db.DateTime)


class BLSampleImageAnalysi(db.Model):
    __tablename__ = "BLSampleImageAnalysis"

    blSampleImageAnalysisId = db.Column(db.Integer, primary_key=True)
    blSampleImageId = db.Column(db.Integer, index=True)
    oavSnapshotBefore = db.Column(db.String(255))
    oavSnapshotAfter = db.Column(db.String(255))
    deltaX = db.Column(db.Integer)
    deltaY = db.Column(db.Integer)
    goodnessOfFit = db.Column(db.Float)
    scaleFactor = db.Column(db.Float)
    resultCode = db.Column(db.String(15))
    matchStartTimeStamp = db.Column(db.DateTime, server_default=db.FetchedValue())
    matchEndTimeStamp = db.Column(db.DateTime)


class BLSampleImageScore(db.Model):
    __tablename__ = "BLSampleImageScore"

    blSampleImageScoreId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    score = db.Column(db.Float)
    colour = db.Column(db.String(15))


class BLSampleTypeHasComponent(db.Model):
    __tablename__ = "BLSampleType_has_Component"

    blSampleTypeId = db.Column(db.Integer, primary_key=True, nullable=False)
    componentId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    abundance = db.Column(db.Float)


class BLSampleHasDiffractionPlan(db.Model):
    __tablename__ = "BLSample_has_DiffractionPlan"

    blSampleId = db.Column(db.Integer, primary_key=True, nullable=False)
    diffractionPlanId = db.Column(
        db.Integer, primary_key=True, nullable=False, index=True
    )


class BLSampleHasEnergyScan(db.Model):
    __tablename__ = "BLSample_has_EnergyScan"

    blSampleId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    energyScanId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    blSampleHasEnergyScanId = db.Column(db.Integer, primary_key=True)


class BLSession(db.Model):
    __tablename__ = "BLSession"

    sessionId = db.Column(db.Integer, primary_key=True)
    expSessionPk = db.Column(db.Integer, info="smis session Pk ")
    beamLineSetupId = db.Column(db.Integer, index=True)
    proposalId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    beamCalendarId = db.Column(db.Integer, index=True)
    projectCode = db.Column(db.String(45))
    startDate = db.Column(db.DateTime, index=True)
    endDate = db.Column(db.DateTime, index=True)
    beamLineName = db.Column(db.String(45), index=True)
    scheduled = db.Column(db.Integer)
    nbShifts = db.Column(db.Integer)
    comments = db.Column(db.String(2000))
    beamLineOperator = db.Column(db.String(255))
    visit_number = db.Column(db.Integer, server_default=db.FetchedValue())
    bltimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    usedFlag = db.Column(
        db.Integer,
        info="indicates if session has Datacollections or XFE or EnergyScans attached",
    )
    sessionTitle = db.Column(db.String(255), info="fx accounts only")
    structureDeterminations = db.Column(db.Float)
    dewarTransport = db.Column(db.Float)
    databackupFrance = db.Column(
        db.Float, info="data backup and express delivery France"
    )
    databackupEurope = db.Column(
        db.Float, info="data backup and express delivery Europe"
    )
    operatorSiteNumber = db.Column(db.String(10), index=True, info="matricule site")
    lastUpdate = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="last update timestamp: by default the end of the session, the last collect...",
    )
    protectedData = db.Column(
        db.String(1024), info="indicates if the data are protected or not"
    )
    externalId = db.Column(db.BINARY(16))
    nbReimbDewars = db.Column(db.Integer)


class BLSessionHasSCPosition(db.Model):
    __tablename__ = "BLSession_has_SCPosition"

    blsessionhasscpositionid = db.Column(db.Integer, primary_key=True)
    blsessionid = db.Column(db.Integer, nullable=False, index=True)
    scContainer = db.Column(
        db.SmallInteger, info="Position of container within sample changer"
    )
    containerPosition = db.Column(
        db.SmallInteger, info="Position of sample within container"
    )


class BLSubSample(db.Model):
    __tablename__ = "BLSubSample"

    blSubSampleId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    blSampleId = db.Column(db.Integer, nullable=False, index=True, info="sample")
    diffractionPlanId = db.Column(
        db.Integer, index=True, info="eventually diffractionPlan"
    )
    positionId = db.Column(db.Integer, index=True, info="position of the subsample")
    position2Id = db.Column(db.Integer, index=True)
    blSubSampleUUID = db.Column(db.String(45), info="uuid of the blsubsample")
    imgFileName = db.Column(db.String(255), info="image filename")
    imgFilePath = db.Column(db.String(1024), info="url image")
    comments = db.Column(db.String(1024), info="comments")
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )
    motorPositionId = db.Column(db.Integer, index=True, info="motor position")


class BeamAperture(db.Model):
    __tablename__ = "BeamApertures"

    beamAperturesid = db.Column(db.Integer, primary_key=True)
    beamlineStatsId = db.Column(db.Integer, index=True)
    flux = db.Column(db.Float(asdecimal=True))
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    apertureSize = db.Column(db.SmallInteger)


class BeamCalendar(db.Model):
    __tablename__ = "BeamCalendar"

    beamCalendarId = db.Column(db.Integer, primary_key=True)
    run = db.Column(db.String(7), nullable=False)
    beamStatus = db.Column(db.String(24), nullable=False)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)


class BeamCentre(db.Model):
    __tablename__ = "BeamCentres"

    beamCentresid = db.Column(db.Integer, primary_key=True)
    beamlineStatsId = db.Column(db.Integer, index=True)
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    zoom = db.Column(db.Integer)


class BeamLineSetup(db.Model):
    __tablename__ = "BeamLineSetup"

    beamLineSetupId = db.Column(db.Integer, primary_key=True)
    synchrotronMode = db.Column(db.String(255))
    undulatorType1 = db.Column(db.String(45))
    undulatorType2 = db.Column(db.String(45))
    undulatorType3 = db.Column(db.String(45))
    focalSpotSizeAtSample = db.Column(db.Float)
    focusingOptic = db.Column(db.String(255))
    beamDivergenceHorizontal = db.Column(db.Float)
    beamDivergenceVertical = db.Column(db.Float)
    polarisation = db.Column(db.Float)
    monochromatorType = db.Column(db.String(255))
    setupDate = db.Column(db.DateTime)
    synchrotronName = db.Column(db.String(255))
    maxExpTimePerDataCollection = db.Column(db.Float(asdecimal=True))
    minExposureTimePerImage = db.Column(db.Float(asdecimal=True))
    goniostatMaxOscillationSpeed = db.Column(db.Float(asdecimal=True))
    goniostatMinOscillationWidth = db.Column(db.Float(asdecimal=True))
    minTransmission = db.Column(db.Float(asdecimal=True))
    CS = db.Column(db.Float)
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )


class BeamlineAction(db.Model):
    __tablename__ = "BeamlineAction"

    beamlineActionId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.Integer, index=True)
    startTimestamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    endTimestamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    message = db.Column(db.String(255))
    parameter = db.Column(db.String(50))
    value = db.Column(db.String(30))
    loglevel = db.Column(db.ENUM("DEBUG", "CRITICAL", "INFO"))
    status = db.Column(
        db.ENUM("PAUSED", "RUNNING", "TERMINATED", "COMPLETE", "ERROR", "EPICSFAIL")
    )


class BeamlineStat(db.Model):
    __tablename__ = "BeamlineStats"

    beamlineStatsId = db.Column(db.Integer, primary_key=True)
    beamline = db.Column(db.String(10))
    recordTimeStamp = db.Column(db.DateTime)
    ringCurrent = db.Column(db.Float)
    energy = db.Column(db.Float)
    gony = db.Column(db.Float)
    beamW = db.Column(db.Float)
    beamH = db.Column(db.Float)
    flux = db.Column(db.Float(asdecimal=True))
    scanFileW = db.Column(db.String(255))
    scanFileH = db.Column(db.String(255))


class Buffer(db.Model):
    __tablename__ = "Buffer"

    bufferId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    safetyLevelId = db.Column(db.Integer, index=True)
    name = db.Column(db.String(45))
    acronym = db.Column(db.String(45))
    pH = db.Column(db.String(45))
    composition = db.Column(db.String(45))
    comments = db.Column(db.String(512))
    BLSessionId = db.Column(db.Integer)
    electronDensity = db.Column(db.Float(7))


class BufferHasAdditive(db.Model):
    __tablename__ = "BufferHasAdditive"

    bufferHasAdditiveId = db.Column(db.Integer, primary_key=True)
    bufferId = db.Column(db.Integer, nullable=False, index=True)
    additiveId = db.Column(db.Integer, nullable=False, index=True)
    measurementUnitId = db.Column(db.Integer, index=True)
    quantity = db.Column(db.String(45))


class CTF(db.Model):
    __tablename__ = "CTF"

    ctfId = db.Column(db.Integer, primary_key=True)
    motionCorrectionId = db.Column(db.Integer, index=True)
    autoProcProgramId = db.Column(db.Integer, index=True)
    boxSizeX = db.Column(db.Float, info="Box size in x, Units: pixels")
    boxSizeY = db.Column(db.Float, info="Box size in y, Units: pixels")
    minResolution = db.Column(db.Float, info="Minimum resolution for CTF, Units: A")
    maxResolution = db.Column(db.Float, info="Units: A")
    minDefocus = db.Column(db.Float, info="Units: A")
    maxDefocus = db.Column(db.Float, info="Units: A")
    defocusStepSize = db.Column(db.Float, info="Units: A")
    astigmatism = db.Column(db.Float, info="Units: A")
    astigmatismAngle = db.Column(db.Float, info="Units: deg?")
    estimatedResolution = db.Column(db.Float, info="Units: A")
    estimatedDefocus = db.Column(db.Float, info="Units: A")
    amplitudeContrast = db.Column(db.Float, info="Units: %?")
    ccValue = db.Column(db.Float, info="Correlation value")
    fftTheoreticalFullPath = db.Column(
        db.String(255), info="Full path to the jpg image of the simulated FFT"
    )
    comments = db.Column(db.String(255))


class CalendarHash(db.Model):
    __tablename__ = "CalendarHash"

    calendarHashId = db.Column(db.Integer, primary_key=True)
    ckey = db.Column(db.String(50))
    hash = db.Column(db.String(128))
    beamline = db.Column(db.Integer)


class ComponentSubType(db.Model):
    __tablename__ = "ComponentSubType"

    componentSubTypeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(31), nullable=False)
    hasPh = db.Column(db.Integer, server_default=db.FetchedValue())


class ComponentType(db.Model):
    __tablename__ = "ComponentType"

    componentTypeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(31), nullable=False)


class ComponentHasSubType(db.Model):
    __tablename__ = "Component_has_SubType"

    componentId = db.Column(db.Integer, primary_key=True, nullable=False)
    componentSubTypeId = db.Column(
        db.Integer, primary_key=True, nullable=False, index=True
    )


class ConcentrationType(db.Model):
    __tablename__ = "ConcentrationType"

    concentrationTypeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(31), nullable=False)
    symbol = db.Column(db.String(8), nullable=False)


class Container(db.Model):
    __tablename__ = "Container"

    containerId = db.Column(db.Integer, primary_key=True)
    dewarId = db.Column(db.Integer, index=True)
    code = db.Column(db.String(45))
    containerType = db.Column(db.String(20))
    capacity = db.Column(db.Integer)
    beamlineLocation = db.Column(db.String(20), index=True)
    sampleChangerLocation = db.Column(db.String(20))
    containerStatus = db.Column(db.String(45), index=True)
    bltimeStamp = db.Column(db.DateTime)
    barcode = db.Column(db.String(45), unique=True)
    sessionId = db.Column(db.Integer, index=True)
    ownerId = db.Column(db.Integer, index=True)
    screenId = db.Column(db.Integer)
    scheduleId = db.Column(db.Integer)
    imagerId = db.Column(db.Integer)
    scLocationUpdated = db.Column(db.DateTime)
    requestedImagerId = db.Column(db.Integer)
    requestedReturn = db.Column(
        db.Integer,
        server_default=db.FetchedValue(),
        info="True for requesting return, False means container will be disposed",
    )
    comments = db.Column(db.String(255))
    experimentType = db.Column(db.String(20))
    storageTemperature = db.Column(db.Float)
    containerRegistryId = db.Column(db.Integer)


class ContainerHistory(db.Model):
    __tablename__ = "ContainerHistory"

    containerHistoryId = db.Column(db.Integer, primary_key=True)
    containerId = db.Column(db.Integer, index=True)
    location = db.Column(db.String(45))
    blTimeStamp = db.Column(db.DateTime)
    status = db.Column(db.String(45))
    beamlineName = db.Column(db.String(20))


class ContainerInspection(db.Model):
    __tablename__ = "ContainerInspection"

    containerInspectionId = db.Column(db.Integer, primary_key=True)
    containerId = db.Column(db.Integer, nullable=False, index=True)
    inspectionTypeId = db.Column(db.Integer, nullable=False, index=True)
    imagerId = db.Column(db.Integer, index=True)
    temperature = db.Column(db.Float)
    blTimeStamp = db.Column(db.DateTime)
    scheduleComponentid = db.Column(db.Integer, index=True)
    state = db.Column(db.String(20))
    priority = db.Column(db.SmallInteger)
    manual = db.Column(db.Integer)
    scheduledTimeStamp = db.Column(db.DateTime)
    completedTimeStamp = db.Column(db.DateTime)


class ContainerQueue(db.Model):
    __tablename__ = "ContainerQueue"

    containerQueueId = db.Column(db.Integer, primary_key=True)
    containerId = db.Column(db.Integer, index=True)
    personId = db.Column(db.Integer, index=True)
    createdTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    completedTimeStamp = db.Column(db.DateTime)


class ContainerQueueSample(db.Model):
    __tablename__ = "ContainerQueueSample"

    containerQueueSampleId = db.Column(db.Integer, primary_key=True)
    containerQueueId = db.Column(db.Integer, index=True)
    blSubSampleId = db.Column(db.Integer, index=True)


class ContainerRegistry(db.Model):
    __tablename__ = "ContainerRegistry"

    containerRegistryId = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(20))
    comments = db.Column(db.String(255))
    recordTimestamp = db.Column(db.DateTime)


class ContainerRegistryHasProposal(db.Model):
    __tablename__ = "ContainerRegistry_has_Proposal"
    __table_args__ = (
        db.Index("containerRegistryId", "containerRegistryId", "proposalId"),
    )

    containerRegistryHasProposalId = db.Column(db.Integer, primary_key=True)
    containerRegistryId = db.Column(db.Integer)
    proposalId = db.Column(db.Integer, index=True)
    personId = db.Column(
        db.Integer, index=True, info="Person registering the container"
    )
    recordTimestamp = db.Column(db.DateTime)


class ContainerReport(db.Model):
    __tablename__ = "ContainerReport"

    containerReportId = db.Column(db.Integer, primary_key=True)
    containerRegistryId = db.Column(db.Integer, index=True)
    personId = db.Column(db.Integer, index=True, info="Person making report")
    report = db.Column(db.Text)
    attachmentFilePath = db.Column(db.String(255))
    recordTimestamp = db.Column(db.DateTime)


class CourierTermsAccepted(db.Model):
    __tablename__ = "CourierTermsAccepted"

    courierTermsAcceptedId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.Integer, nullable=False, index=True)
    personId = db.Column(db.Integer, nullable=False, index=True)
    shippingName = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime)
    shippingId = db.Column(db.Integer, index=True)


class Crystal(db.Model):
    __tablename__ = "Crystal"

    crystalId = db.Column(db.Integer, primary_key=True)
    diffractionPlanId = db.Column(db.Integer, index=True)
    proteinId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    crystalUUID = db.Column(db.String(45))
    name = db.Column(db.String(255))
    spaceGroup = db.Column(db.String(20))
    morphology = db.Column(db.String(255))
    color = db.Column(db.String(45))
    size_X = db.Column(db.Float(asdecimal=True))
    size_Y = db.Column(db.Float(asdecimal=True))
    size_Z = db.Column(db.Float(asdecimal=True))
    cell_a = db.Column(db.Float(asdecimal=True))
    cell_b = db.Column(db.Float(asdecimal=True))
    cell_c = db.Column(db.Float(asdecimal=True))
    cell_alpha = db.Column(db.Float(asdecimal=True))
    cell_beta = db.Column(db.Float(asdecimal=True))
    cell_gamma = db.Column(db.Float(asdecimal=True))
    comments = db.Column(db.String(255))
    pdbFileName = db.Column(db.String(255), info="pdb file name")
    pdbFilePath = db.Column(db.String(1024), info="pdb file path")
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )
    abundance = db.Column(db.Float)
    packingFraction = db.Column(db.Float)
    theoreticaldensity = db.Column(db.Float)


class DataCollection(db.Model):
    __tablename__ = "DataCollection"

    dataCollectionId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    dataCollectionGroupId = db.Column(
        db.Integer,
        nullable=False,
        index=True,
        info="references DataCollectionGroup table",
    )
    strategySubWedgeOrigId = db.Column(
        db.Integer, index=True, info="references ScreeningStrategySubWedge table"
    )
    detectorId = db.Column(db.Integer, index=True, info="references Detector table")
    blSubSampleId = db.Column(db.Integer, index=True)
    dataCollectionNumber = db.Column(db.Integer, index=True)
    startTime = db.Column(
        db.DateTime, index=True, info="Start time of the dataCollection"
    )
    endTime = db.Column(db.DateTime, info="end time of the dataCollection")
    runStatus = db.Column(db.String(200))
    axisStart = db.Column(db.Float)
    axisEnd = db.Column(db.Float)
    axisRange = db.Column(db.Float)
    overlap = db.Column(db.Float)
    numberOfImages = db.Column(db.Integer)
    startImageNumber = db.Column(db.Integer)
    numberOfPasses = db.Column(db.Integer)
    exposureTime = db.Column(db.Float)
    imageDirectory = db.Column(db.String(255), index=True)
    imagePrefix = db.Column(db.String(45), index=True)
    imageSuffix = db.Column(db.String(45))
    fileTemplate = db.Column(db.String(255))
    wavelength = db.Column(db.Float)
    resolution = db.Column(db.Float)
    detectorDistance = db.Column(db.Float)
    xBeam = db.Column(db.Float)
    yBeam = db.Column(db.Float)
    xBeamPix = db.Column(db.Float, info="Beam size in pixels")
    yBeamPix = db.Column(db.Float, info="Beam size in pixels")
    comments = db.Column(db.String(1024))
    printableForReport = db.Column(db.Integer, server_default=db.FetchedValue())
    slitGapVertical = db.Column(db.Float)
    slitGapHorizontal = db.Column(db.Float)
    transmission = db.Column(db.Float)
    synchrotronMode = db.Column(db.String(20))
    xtalSnapshotFullPath1 = db.Column(db.String(255))
    xtalSnapshotFullPath2 = db.Column(db.String(255))
    xtalSnapshotFullPath3 = db.Column(db.String(255))
    xtalSnapshotFullPath4 = db.Column(db.String(255))
    rotationAxis = db.Column(db.ENUM("Omega", "Kappa", "Phi"))
    phiStart = db.Column(db.Float)
    kappaStart = db.Column(db.Float)
    omegaStart = db.Column(db.Float)
    resolutionAtCorner = db.Column(db.Float)
    detector2Theta = db.Column(db.Float)
    undulatorGap1 = db.Column(db.Float)
    undulatorGap2 = db.Column(db.Float)
    undulatorGap3 = db.Column(db.Float)
    beamSizeAtSampleX = db.Column(db.Float)
    beamSizeAtSampleY = db.Column(db.Float)
    centeringMethod = db.Column(db.String(255))
    averageTemperature = db.Column(db.Float)
    actualCenteringPosition = db.Column(db.String(255))
    beamShape = db.Column(db.String(45))
    flux = db.Column(db.Float(asdecimal=True))
    flux_end = db.Column(
        db.Float(asdecimal=True), info="flux measured after the collect"
    )
    totalAbsorbedDose = db.Column(
        db.Float(asdecimal=True), info="expected dose delivered to the crystal, EDNA"
    )
    bestWilsonPlotPath = db.Column(db.String(255))
    imageQualityIndicatorsPlotPath = db.Column(db.String(512))
    imageQualityIndicatorsCSVPath = db.Column(db.String(512))
    blSampleId = db.Column(db.Integer)
    sessionId = db.Column(db.Integer, server_default=db.FetchedValue())
    experimentType = db.Column(db.String(24))
    crystalClass = db.Column(db.String(20))
    chiStart = db.Column(db.Float)
    detectorMode = db.Column(db.String(255))
    actualSampleBarcode = db.Column(db.String(45))
    actualSampleSlotInContainer = db.Column(db.Integer)
    actualContainerBarcode = db.Column(db.String(45))
    actualContainerSlotInSC = db.Column(db.Integer)
    positionId = db.Column(db.Integer)
    focalSpotSizeAtSampleX = db.Column(db.Float)
    polarisation = db.Column(db.Float)
    focalSpotSizeAtSampleY = db.Column(db.Float)
    apertureId = db.Column(db.Integer)
    screeningOrigId = db.Column(db.Integer)
    processedDataFile = db.Column(db.String(255))
    datFullPath = db.Column(db.String(255))
    magnification = db.Column(db.Integer, info="Unit: X")
    binning = db.Column(
        db.Integer,
        server_default=db.FetchedValue(),
        info="1 or 2. Number of pixels to process as 1. (Use mean value.)",
    )
    particleDiameter = db.Column(db.Float, info="Unit: nm")
    boxSize_CTF = db.Column(db.Float, info="Unit: pixels")
    minResolution = db.Column(db.Float, info="Unit: A")
    minDefocus = db.Column(db.Float, info="Unit: A")
    maxDefocus = db.Column(db.Float, info="Unit: A")
    defocusStepSize = db.Column(db.Float, info="Unit: A")
    amountAstigmatism = db.Column(db.Float, info="Unit: A")
    extractSize = db.Column(db.Float, info="Unit: pixels")
    bgRadius = db.Column(db.Float, info="Unit: nm")
    voltage = db.Column(db.Float, info="Unit: kV")
    objAperture = db.Column(db.Float, info="Unit: um")
    c1aperture = db.Column(db.Float, info="Unit: um")
    c2aperture = db.Column(db.Float, info="Unit: um")
    c3aperture = db.Column(db.Float, info="Unit: um")
    c1lens = db.Column(db.Float, info="Unit: %")
    c2lens = db.Column(db.Float, info="Unit: %")
    c3lens = db.Column(db.Float, info="Unit: %")
    nominalmagnification = db.Column(db.Float)
    nominalDefocus = db.Column(db.Float)
    imageSizeX = db.Column(db.Integer)
    imageSizeY = db.Column(db.Integer)
    pixelSizeOnImage = db.Column(db.Float)
    phasePlate = db.Column(db.Integer)
    totalExposedDose = db.Column(db.Float, info="Units: e-/A^2")


class DataCollectionComment(db.Model):
    __tablename__ = "DataCollectionComment"

    dataCollectionCommentId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, nullable=False, index=True)
    personId = db.Column(db.Integer, nullable=False, index=True)
    comments = db.Column(db.String(4000))
    createTime = db.Column(db.DateTime)
    modTime = db.Column(db.Date)


class DataCollectionFileAttachment(db.Model):
    __tablename__ = "DataCollectionFileAttachment"

    dataCollectionFileAttachmentId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, nullable=False, index=True)
    fileFullPath = db.Column(db.String(255), nullable=False)
    fileType = db.Column(
        db.ENUM("snapshot", "log", "xy", "recip"),
        info="snapshot: image file, usually of the sample. \\nlog: a text file with logging info. \\nxy: x and y data in text format. \\nrecip: a compressed csv file with reciprocal space coordinates.",
    )
    createTime = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )


class DataCollectionGroup(db.Model):
    __tablename__ = "DataCollectionGroup"

    dataCollectionGroupId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    blSampleId = db.Column(db.Integer, index=True, info="references BLSample table")
    sessionId = db.Column(
        db.Integer, nullable=False, index=True, info="references Session table"
    )
    workflowId = db.Column(db.Integer, index=True)
    experimentType = db.Column(
        db.ENUM(
            "EM",
            "SAD",
            "SAD - Inverse Beam",
            "OSC",
            "Collect - Multiwedge",
            "MAD",
            "Helical",
            "Multi-positional",
            "Mesh",
            "Burn",
            "MAD - Inverse Beam",
            "Characterization",
            "Dehydration",
            "Still",
        ),
        info="Experiment type flag",
    )
    startTime = db.Column(db.DateTime, info="Start time of the dataCollectionGroup")
    endTime = db.Column(db.DateTime, info="end time of the dataCollectionGroup")
    crystalClass = db.Column(db.String(20), info="Crystal Class for industrials users")
    comments = db.Column(db.String(1024), info="comments")
    detectorMode = db.Column(db.String(255), info="Detector mode")
    actualSampleBarcode = db.Column(db.String(45), info="Actual sample barcode")
    actualSampleSlotInContainer = db.Column(
        db.Integer, info="Actual sample slot number in container"
    )
    actualContainerBarcode = db.Column(db.String(45), info="Actual container barcode")
    actualContainerSlotInSC = db.Column(
        db.Integer, info="Actual container slot number in sample changer"
    )
    xtalSnapshotFullPath = db.Column(db.String(255))


class DataCollectionPlanGroup(db.Model):
    __tablename__ = "DataCollectionPlanGroup"

    dataCollectionPlanGroupId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.Integer, index=True)
    blSampleId = db.Column(db.Integer, index=True)


class DataReductionStatu(db.Model):
    __tablename__ = "DataReductionStatus"

    dataReductionStatusId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(15))
    filename = db.Column(db.String(255))
    message = db.Column(db.String(255))


class Detector(db.Model):
    __tablename__ = "Detector"
    __table_args__ = (
        db.Index(
            "Detector_FKIndex1",
            "detectorType",
            "detectorManufacturer",
            "detectorModel",
            "detectorPixelSizeHorizontal",
            "detectorPixelSizeVertical",
        ),
    )

    detectorId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    detectorType = db.Column(db.String(255))
    detectorManufacturer = db.Column(db.String(255))
    detectorModel = db.Column(db.String(255))
    detectorPixelSizeHorizontal = db.Column(db.Float)
    detectorPixelSizeVertical = db.Column(db.Float)
    detectorSerialNumber = db.Column(db.String(30))
    detectorDistanceMin = db.Column(db.Float(asdecimal=True))
    detectorDistanceMax = db.Column(db.Float(asdecimal=True))
    trustedPixelValueRangeLower = db.Column(db.Float(asdecimal=True))
    trustedPixelValueRangeUpper = db.Column(db.Float(asdecimal=True))
    sensorThickness = db.Column(db.Float)
    overload = db.Column(db.Float)
    XGeoCorr = db.Column(db.String(255))
    YGeoCorr = db.Column(db.String(255))
    detectorMode = db.Column(db.String(255))
    detectorMaxResolution = db.Column(db.Float)
    detectorMinResolution = db.Column(db.Float)
    CS = db.Column(db.Float, info="Unit: mm")
    density = db.Column(db.Float)
    composition = db.Column(db.String(16))
    numberOfPixelsX = db.Column(db.Integer)
    numberOfPixelsY = db.Column(db.Integer)
    localName = db.Column(db.String(40), info="Colloquial name for the detector")


class Dewar(db.Model):
    __tablename__ = "Dewar"

    dewarId = db.Column(db.Integer, primary_key=True)
    shippingId = db.Column(db.Integer, index=True)
    code = db.Column(db.String(45), index=True)
    comments = db.Column(db.String)
    storageLocation = db.Column(db.String(45))
    dewarStatus = db.Column(db.String(45), index=True)
    bltimeStamp = db.Column(db.DateTime)
    isStorageDewar = db.Column(db.Integer, server_default=db.FetchedValue())
    barCode = db.Column(db.String(45), unique=True)
    firstExperimentId = db.Column(db.Integer, index=True)
    customsValue = db.Column(db.Integer)
    transportValue = db.Column(db.Integer)
    trackingNumberToSynchrotron = db.Column(db.String(30))
    trackingNumberFromSynchrotron = db.Column(db.String(30))
    facilityCode = db.Column(
        db.String(20), info="Unique barcode assigned to each dewar"
    )
    type = db.Column(
        db.ENUM("Dewar", "Toolbox"), nullable=False, server_default=db.FetchedValue()
    )
    isReimbursed = db.Column(
        db.Integer,
        server_default=db.FetchedValue(),
        info="set this dewar as reimbursed by the user office",
    )
    weight = db.Column(db.Float)
    deliveryAgent_barcode = db.Column(db.String(30))


class DewarLocation(db.Model):
    __tablename__ = "DewarLocation"

    eventId = db.Column(db.Integer, primary_key=True)
    dewarNumber = db.Column(db.String(128), nullable=False, info="Dewar number")
    userId = db.Column(db.String(128), info="User who locates the dewar")
    dateTime = db.Column(db.DateTime, info="Date and time of locatization")
    locationName = db.Column(db.String(128), info="Location of the dewar")
    courierName = db.Column(
        db.String(128), info="Carrier name who's shipping back the dewar"
    )
    courierTrackingNumber = db.Column(
        db.String(128), info="Tracking number of the shippment"
    )


class DewarLocationList(db.Model):
    __tablename__ = "DewarLocationList"

    locationId = db.Column(db.Integer, primary_key=True)
    locationName = db.Column(
        db.String(128),
        nullable=False,
        server_default=db.FetchedValue(),
        info="Location",
    )


class DewarRegistry(db.Model):
    __tablename__ = "DewarRegistry"

    facilityCode = db.Column(db.String(20), primary_key=True)
    proposalId = db.Column(db.Integer, nullable=False, index=True)
    labContactId = db.Column(db.Integer, nullable=False, index=True)
    purchaseDate = db.Column(db.DateTime)
    bltimestamp = db.Column(db.DateTime)


class DewarReport(db.Model):
    __tablename__ = "DewarReport"

    dewarReportId = db.Column(db.Integer, primary_key=True)
    facilityCode = db.Column(db.String(20), nullable=False, index=True)
    report = db.Column(db.Text)
    attachment = db.Column(db.String(255))
    bltimestamp = db.Column(db.DateTime)


class DewarTransportHistory(db.Model):
    __tablename__ = "DewarTransportHistory"

    DewarTransportHistoryId = db.Column(db.Integer, primary_key=True)
    dewarId = db.Column(db.Integer, index=True)
    dewarStatus = db.Column(db.String(45), nullable=False)
    storageLocation = db.Column(db.String(45))
    arrivalDate = db.Column(db.DateTime)


class DiffractionPlan(db.Model):
    __tablename__ = "DiffractionPlan"

    diffractionPlanId = db.Column(db.Integer, primary_key=True)
    xmlDocumentId = db.Column(db.Integer)
    experimentKind = db.Column(
        db.ENUM(
            "Default",
            "MXPressE",
            "MXPressO",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressI",
            "MXPressE_SAD",
            "MXScore",
            "MXPressM",
            "MAD",
            "SAD",
            "Fixed",
            "Ligand binding",
            "Refinement",
            "OSC",
            "MAD - Inverse Beam",
            "SAD - Inverse Beam",
        )
    )
    observedResolution = db.Column(db.Float)
    minimalResolution = db.Column(db.Float)
    exposureTime = db.Column(db.Float)
    oscillationRange = db.Column(db.Float)
    maximalResolution = db.Column(db.Float)
    screeningResolution = db.Column(db.Float)
    radiationSensitivity = db.Column(db.Float)
    anomalousScatterer = db.Column(db.String(255))
    preferredBeamSizeX = db.Column(db.Float)
    preferredBeamSizeY = db.Column(db.Float)
    preferredBeamDiameter = db.Column(db.Float)
    comments = db.Column(db.String(1024))
    aimedCompleteness = db.Column(db.Float(asdecimal=True))
    aimedIOverSigmaAtHighestRes = db.Column(db.Float(asdecimal=True))
    aimedMultiplicity = db.Column(db.Float(asdecimal=True))
    aimedResolution = db.Column(db.Float(asdecimal=True))
    anomalousData = db.Column(db.Integer, server_default=db.FetchedValue())
    complexity = db.Column(db.String(45))
    estimateRadiationDamage = db.Column(db.Integer, server_default=db.FetchedValue())
    forcedSpaceGroup = db.Column(db.String(45))
    requiredCompleteness = db.Column(db.Float(asdecimal=True))
    requiredMultiplicity = db.Column(db.Float(asdecimal=True))
    requiredResolution = db.Column(db.Float(asdecimal=True))
    strategyOption = db.Column(db.String(45))
    kappaStrategyOption = db.Column(db.String(45))
    numberOfPositions = db.Column(db.Integer)
    minDimAccrossSpindleAxis = db.Column(
        db.Float(asdecimal=True), info="minimum dimension accross the spindle axis"
    )
    maxDimAccrossSpindleAxis = db.Column(
        db.Float(asdecimal=True), info="maximum dimension accross the spindle axis"
    )
    radiationSensitivityBeta = db.Column(db.Float(asdecimal=True))
    radiationSensitivityGamma = db.Column(db.Float(asdecimal=True))
    minOscWidth = db.Column(db.Float)
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )
    diffractionPlanUUID = db.Column(db.String(1000))
    dataCollectionPlanGroupId = db.Column(db.Integer)
    detectorId = db.Column(db.Integer)
    distance = db.Column(db.Float(asdecimal=True))
    orientation = db.Column(db.Float(asdecimal=True))
    monoBandwidth = db.Column(db.Float(asdecimal=True))
    monochromator = db.Column(db.String(8), info="DMM or DCM")
    energy = db.Column(db.Float, info="eV")
    transmission = db.Column(db.Float, info="Decimal fraction in range [0,1]")
    boxSizeX = db.Column(db.Float, info="microns")
    boxSizeY = db.Column(db.Float, info="microns")
    kappaStart = db.Column(db.Float, info="degrees")
    axisStart = db.Column(db.Float, info="degrees")
    axisRange = db.Column(db.Float, info="degrees")
    numberOfImages = db.Column(db.Integer, info="The number of images requested")
    presetForProposalId = db.Column(
        db.Integer,
        info="Indicates this plan is available to all sessions on given proposal",
    )
    beamLineName = db.Column(
        db.String(45),
        info="Indicates this plan is available to all sessions on given beamline",
    )
    centringmethod = db.Column(db.ENUM("xray", "loop", "diffraction", "optical"))


class DiffractionPlanHasDetector(db.Model):
    __tablename__ = "DiffractionPlan_has_Detector"

    diffractionPlanId = db.Column(db.Integer, primary_key=True, nullable=False)
    detectorId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    exposureTime = db.Column(db.Float(asdecimal=True))
    distance = db.Column(db.Float(asdecimal=True))
    orientation = db.Column(db.Float(asdecimal=True))


class EMMicroscope(db.Model):
    __tablename__ = "EMMicroscope"

    emMicroscopeId = db.Column(db.Integer, primary_key=True)
    instrumentName = db.Column(db.String(100), nullable=False)
    voltage = db.Column(db.Float)
    CS = db.Column(db.Float, info="Unit: mm")
    detectorPixelSize = db.Column(db.Float)
    C2aperture = db.Column(db.Float)
    ObjAperture = db.Column(db.Float)
    C2lens = db.Column(db.Float)


class EnergyScan(db.Model):
    __tablename__ = "EnergyScan"

    energyScanId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.Integer, nullable=False, index=True)
    blSampleId = db.Column(db.Integer, index=True)
    fluorescenceDetector = db.Column(db.String(255))
    scanFileFullPath = db.Column(db.String(255))
    choochFileFullPath = db.Column(db.String(255))
    jpegChoochFileFullPath = db.Column(db.String(255))
    element = db.Column(db.String(45))
    startEnergy = db.Column(db.Float)
    endEnergy = db.Column(db.Float)
    transmissionFactor = db.Column(db.Float)
    exposureTime = db.Column(db.Float)
    axisPosition = db.Column(db.Float)
    synchrotronCurrent = db.Column(db.Float)
    temperature = db.Column(db.Float)
    peakEnergy = db.Column(db.Float)
    peakFPrime = db.Column(db.Float)
    peakFDoublePrime = db.Column(db.Float)
    inflectionEnergy = db.Column(db.Float)
    inflectionFPrime = db.Column(db.Float)
    inflectionFDoublePrime = db.Column(db.Float)
    xrayDose = db.Column(db.Float)
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    edgeEnergy = db.Column(db.String(255))
    filename = db.Column(db.String(255))
    beamSizeVertical = db.Column(db.Float)
    beamSizeHorizontal = db.Column(db.Float)
    crystalClass = db.Column(db.String(20))
    comments = db.Column(db.String(1024))
    flux = db.Column(
        db.Float(asdecimal=True), info="flux measured before the energyScan"
    )
    flux_end = db.Column(
        db.Float(asdecimal=True), info="flux measured after the energyScan"
    )
    workingDirectory = db.Column(db.String(45))
    blSubSampleId = db.Column(db.Integer, index=True)


class Experiment(db.Model):
    __tablename__ = "Experiment"

    experimentId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.Integer, index=True)
    proposalId = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255))
    creationDate = db.Column(db.DateTime)
    experimentType = db.Column(db.String(128))
    sourceFilePath = db.Column(db.String(256))
    dataAcquisitionFilePath = db.Column(
        db.String(256),
        info="The file path pointing to the data acquisition. Eventually it may be a compressed file with all the files or just the folder",
    )
    status = db.Column(db.String(45))
    comments = db.Column(db.String(512))


class ExperimentKindDetail(db.Model):
    __tablename__ = "ExperimentKindDetails"

    experimentKindId = db.Column(db.Integer, primary_key=True)
    diffractionPlanId = db.Column(db.Integer, nullable=False, index=True)
    exposureIndex = db.Column(db.Integer)
    dataCollectionType = db.Column(db.String(45))
    dataCollectionKind = db.Column(db.String(45))
    wedgeValue = db.Column(db.Float)


class FitStructureToExperimentalDatum(db.Model):
    __tablename__ = "FitStructureToExperimentalData"

    fitStructureToExperimentalDataId = db.Column(db.Integer, primary_key=True)
    structureId = db.Column(db.Integer, index=True)
    subtractionId = db.Column(db.Integer, index=True)
    workflowId = db.Column(db.Integer, index=True)
    fitFilePath = db.Column(db.String(255))
    logFilePath = db.Column(db.String(255))
    outputFilePath = db.Column(db.String(255))
    creationDate = db.Column(db.DateTime)
    comments = db.Column(db.String(2048))


class Frame(db.Model):
    __tablename__ = "Frame"

    frameId = db.Column(db.Integer, primary_key=True)
    filePath = db.Column(db.String(255))
    comments = db.Column(db.String(45))
    creationDate = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    frameSetId = db.Column(db.Integer)


class FrameList(db.Model):
    __tablename__ = "FrameList"

    frameListId = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.Integer)


class FrameSet(db.Model):
    __tablename__ = "FrameSet"

    frameSetId = db.Column(db.Integer, primary_key=True)
    runId = db.Column(db.Integer, nullable=False, index=True)
    frameListId = db.Column(db.Integer, index=True)
    detectorId = db.Column(db.Integer)
    detectorDistance = db.Column(db.String(45))
    filePath = db.Column(db.String(255))
    internalPath = db.Column(db.String(255))


class FrameToList(db.Model):
    __tablename__ = "FrameToList"

    frameToListId = db.Column(db.Integer, primary_key=True)
    frameListId = db.Column(db.Integer, nullable=False, index=True)
    frameId = db.Column(db.Integer, nullable=False, index=True)


class GeometryClassname(db.Model):
    __tablename__ = "GeometryClassname"

    geometryClassnameId = db.Column(db.Integer, primary_key=True)
    geometryClassname = db.Column(db.String(45))
    geometryOrder = db.Column(db.Integer, nullable=False)


class GridInfo(db.Model):
    __tablename__ = "GridInfo"

    gridInfoId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    workflowMeshId = db.Column(db.Integer, index=True)
    xOffset = db.Column(db.Float(asdecimal=True))
    yOffset = db.Column(db.Float(asdecimal=True))
    dx_mm = db.Column(db.Float(asdecimal=True))
    dy_mm = db.Column(db.Float(asdecimal=True))
    steps_x = db.Column(db.Float(asdecimal=True))
    steps_y = db.Column(db.Float(asdecimal=True))
    meshAngle = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )
    orientation = db.Column(
        db.ENUM("vertical", "horizontal"), server_default=db.FetchedValue()
    )
    dataCollectionGroupId = db.Column(db.Integer, index=True)
    pixelspermicronX = db.Column(db.Float)
    pixelspermicronY = db.Column(db.Float)
    snapshot_offsetxpixel = db.Column(db.Float)
    snapshot_offsetypixel = db.Column(db.Float)
    snaked = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class Image(db.Model):
    __tablename__ = "Image"
    __table_args__ = (db.Index("Image_Index3", "fileLocation", "fileName"),)

    imageId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    motorPositionId = db.Column(db.Integer, index=True)
    imageNumber = db.Column(db.Integer, index=True)
    fileName = db.Column(db.String(255))
    fileLocation = db.Column(db.String(255))
    measuredIntensity = db.Column(db.Float)
    jpegFileFullPath = db.Column(db.String(255))
    jpegThumbnailFileFullPath = db.Column(db.String(255))
    temperature = db.Column(db.Float)
    cumulativeIntensity = db.Column(db.Float)
    synchrotronCurrent = db.Column(db.Float)
    comments = db.Column(db.String(1024))
    machineMessage = db.Column(db.String(1024))
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )


class ImageQualityIndicator(db.Model):
    __tablename__ = "ImageQualityIndicators"

    imageQualityIndicatorsId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    imageId = db.Column(db.Integer, index=True)
    autoProcProgramId = db.Column(
        db.Integer,
        nullable=False,
        index=True,
        info="Foreign key to the AutoProcProgram table",
    )
    spotTotal = db.Column(db.Integer, info="Total number of spots")
    inResTotal = db.Column(db.Integer, info="Total number of spots in resolution range")
    goodBraggCandidates = db.Column(
        db.Integer, info="Total number of Bragg diffraction spots"
    )
    iceRings = db.Column(db.Integer, info="Number of ice rings identified")
    method1Res = db.Column(db.Float, info="Resolution estimate 1 (see publication)")
    method2Res = db.Column(db.Float, info="Resolution estimate 2 (see publication)")
    maxUnitCell = db.Column(
        db.Float, info="Estimation of the largest possible unit cell edge"
    )
    pctSaturationTop50Peaks = db.Column(
        db.Float, info="The fraction of the dynamic range being used"
    )
    inResolutionOvrlSpots = db.Column(db.Integer, info="Number of spots overloaded")
    binPopCutOffMethod2Res = db.Column(
        db.Float, info="Cut off used in resolution limit calculation"
    )
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")
    totalIntegratedSignal = db.Column(db.Float(asdecimal=True))
    dozor_score = db.Column(db.Float(asdecimal=True), info="dozor_score")
    dataCollectionId = db.Column(db.Integer)
    imageNumber = db.Column(db.Integer)


class Imager(db.Model):
    __tablename__ = "Imager"

    imagerId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    temperature = db.Column(db.Float)
    serial = db.Column(db.String(45))
    capacity = db.Column(db.SmallInteger)


class InputParameterWorkflow(db.Model):
    __tablename__ = "InputParameterWorkflow"

    inputParameterId = db.Column(db.Integer, primary_key=True)
    workflowId = db.Column(db.Integer, nullable=False)
    parameterType = db.Column(db.String(255))
    name = db.Column(db.String(255))
    value = db.Column(db.String(255))
    comments = db.Column(db.String(2048))


class InspectionType(db.Model):
    __tablename__ = "InspectionType"

    inspectionTypeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))


class Instruction(db.Model):
    __tablename__ = "Instruction"

    instructionId = db.Column(db.Integer, primary_key=True)
    instructionSetId = db.Column(db.Integer, nullable=False, index=True)
    order = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(255))


class InstructionSet(db.Model):
    __tablename__ = "InstructionSet"

    instructionSetId = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))


class IspybAutoProcAttachment(db.Model):
    __tablename__ = "IspybAutoProcAttachment"

    autoProcAttachmentId = db.Column(db.Integer, primary_key=True)
    fileName = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    step = db.Column(
        db.ENUM("XDS", "XSCALE", "SCALA", "SCALEPACK", "TRUNCATE", "DIMPLE"),
        server_default=db.FetchedValue(),
        info="step where the file is generated",
    )
    fileCategory = db.Column(
        db.ENUM("input", "output", "log", "correction"),
        server_default=db.FetchedValue(),
    )
    hasGraph = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class IspybCrystalClas(db.Model):
    __tablename__ = "IspybCrystalClass"

    crystalClassId = db.Column(db.Integer, primary_key=True)
    crystalClass_code = db.Column(db.String(20), nullable=False)
    crystalClass_name = db.Column(db.String(255), nullable=False)


class IspybReference(db.Model):
    __tablename__ = "IspybReference"

    referenceId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    referenceName = db.Column(db.String(255), info="reference name")
    referenceUrl = db.Column(db.String(1024), info="url of the reference")
    referenceBibtext = db.Column(db.LargeBinary, info="bibtext value of the reference")
    beamline = db.Column(
        db.ENUM("All", "ID14-4", "ID23-1", "ID23-2", "ID29", "XRF", "AllXRF", "Mesh"),
        info="beamline involved",
    )


class LabContact(db.Model):
    __tablename__ = "LabContact"
    __table_args__ = (
        db.Index("cardNameAndProposal", "cardName", "proposalId"),
        db.Index("personAndProposal", "personId", "proposalId"),
    )

    labContactId = db.Column(db.Integer, primary_key=True)
    personId = db.Column(db.Integer, nullable=False)
    cardName = db.Column(db.String(40), nullable=False)
    proposalId = db.Column(db.Integer, nullable=False, index=True)
    defaultCourrierCompany = db.Column(db.String(45))
    courierAccount = db.Column(db.String(45))
    billingReference = db.Column(db.String(45))
    dewarAvgCustomsValue = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue()
    )
    dewarAvgTransportValue = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue()
    )
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )


class Laboratory(db.Model):
    __tablename__ = "Laboratory"

    laboratoryId = db.Column(db.Integer, primary_key=True)
    laboratoryUUID = db.Column(db.String(45))
    name = db.Column(db.String(45))
    address = db.Column(db.String(255))
    city = db.Column(db.String(45))
    country = db.Column(db.String(45))
    url = db.Column(db.String(255))
    organization = db.Column(db.String(45))
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )
    laboratoryExtPk = db.Column(db.Integer)
    postcode = db.Column(db.String(15))


class Login(db.Model):
    __tablename__ = "Login"

    loginId = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(45), nullable=False, index=True)
    username = db.Column(db.String(45), nullable=False)
    roles = db.Column(db.String(1024), nullable=False)
    siteId = db.Column(db.String(45))
    authorized = db.Column(db.String(1024))
    expirationTime = db.Column(db.DateTime, nullable=False)


class MXMRRun(db.Model):
    __tablename__ = "MXMRRun"

    mxMRRunId = db.Column(db.Integer, primary_key=True)
    autoProcScalingId = db.Column(db.Integer, nullable=False, index=True)
    success = db.Column(
        db.Integer,
        server_default=db.FetchedValue(),
        info="Indicates whether the program completed. 1 for success, 0 for failure.",
    )
    message = db.Column(
        db.String(255), info="A short summary of the findings, success or failure."
    )
    pipeline = db.Column(db.String(50))
    inputCoordFile = db.Column(db.String(255))
    outputCoordFile = db.Column(db.String(255))
    inputMTZFile = db.Column(db.String(255))
    outputMTZFile = db.Column(db.String(255))
    runDirectory = db.Column(db.String(255))
    logFile = db.Column(db.String(255))
    commandLine = db.Column(db.String(255))
    rValueStart = db.Column(db.Float)
    rValueEnd = db.Column(db.Float)
    rFreeValueStart = db.Column(db.Float)
    rFreeValueEnd = db.Column(db.Float)
    starttime = db.Column(db.DateTime)
    endtime = db.Column(db.DateTime)


class MXMRRunBlob(db.Model):
    __tablename__ = "MXMRRunBlob"

    mxMRRunBlobId = db.Column(db.Integer, primary_key=True)
    mxMRRunId = db.Column(db.Integer, nullable=False, index=True)
    view1 = db.Column(db.String(255))
    view2 = db.Column(db.String(255))
    view3 = db.Column(db.String(255))


class Macromolecule(db.Model):
    __tablename__ = "Macromolecule"

    macromoleculeId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.Integer)
    safetyLevelId = db.Column(db.Integer, index=True)
    name = db.Column(db.String(45))
    acronym = db.Column(db.String(45))
    extintionCoefficient = db.Column(db.String(45))
    molecularMass = db.Column(db.String(45))
    sequence = db.Column(db.String(1000))
    contactsDescriptionFilePath = db.Column(db.String(255))
    symmetry = db.Column(db.String(45))
    comments = db.Column(db.String(1024))
    refractiveIndex = db.Column(db.String(45))
    solventViscosity = db.Column(db.String(45))
    creationDate = db.Column(db.DateTime)
    electronDensity = db.Column(db.Float(7))


class MacromoleculeRegion(db.Model):
    __tablename__ = "MacromoleculeRegion"

    macromoleculeRegionId = db.Column(db.Integer, primary_key=True)
    macromoleculeId = db.Column(db.Integer, nullable=False, index=True)
    regionType = db.Column(db.String(45))
    id = db.Column(db.String(45))
    count = db.Column(db.String(45))
    sequence = db.Column(db.String(45))


class Measurement(db.Model):
    __tablename__ = "Measurement"

    measurementId = db.Column(db.Integer, primary_key=True)
    specimenId = db.Column(db.Integer, nullable=False, index=True)
    runId = db.Column(db.Integer, index=True)
    code = db.Column(db.String(100))
    imageDirectory = db.Column(db.String(512))
    priorityLevelId = db.Column(db.Integer)
    exposureTemperature = db.Column(db.String(45))
    viscosity = db.Column(db.String(45))
    flow = db.Column(db.Integer)
    extraFlowTime = db.Column(db.String(45))
    volumeToLoad = db.Column(db.String(45))
    waitTime = db.Column(db.String(45))
    transmission = db.Column(db.String(45))
    comments = db.Column(db.String(512))
    pathToH5 = db.Column(db.String(512))


class MeasurementToDataCollection(db.Model):
    __tablename__ = "MeasurementToDataCollection"

    measurementToDataCollectionId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, index=True)
    measurementId = db.Column(db.Integer, index=True)
    dataCollectionOrder = db.Column(db.Integer)


class MeasurementUnit(db.Model):
    __tablename__ = "MeasurementUnit"

    measurementUnitId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    unitType = db.Column(db.String(45))


class Merge(db.Model):
    __tablename__ = "Merge"

    mergeId = db.Column(db.Integer, primary_key=True)
    measurementId = db.Column(db.Integer, index=True)
    frameListId = db.Column(db.Integer, index=True)
    discardedFrameNameList = db.Column(db.String(1024))
    averageFilePath = db.Column(db.String(255))
    framesCount = db.Column(db.String(45))
    framesMerge = db.Column(db.String(45))
    creationDate = db.Column(db.DateTime)


class MixtureToStructure(db.Model):
    __tablename__ = "MixtureToStructure"

    fitToStructureId = db.Column(db.Integer, primary_key=True)
    structureId = db.Column(db.Integer, nullable=False, index=True)
    mixtureId = db.Column(db.Integer, nullable=False, index=True)
    volumeFraction = db.Column(db.String(45))
    creationDate = db.Column(db.DateTime)


class Model(db.Model):
    __tablename__ = "Model"

    modelId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    pdbFile = db.Column(db.String(255))
    fitFile = db.Column(db.String(255))
    firFile = db.Column(db.String(255))
    logFile = db.Column(db.String(255))
    rFactor = db.Column(db.String(45))
    chiSqrt = db.Column(db.String(45))
    volume = db.Column(db.String(45))
    rg = db.Column(db.String(45))
    dMax = db.Column(db.String(45))


class ModelBuilding(db.Model):
    __tablename__ = "ModelBuilding"

    modelBuildingId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingAnalysisId = db.Column(
        db.Integer, nullable=False, index=True, info="Related phasing analysis item"
    )
    phasingProgramRunId = db.Column(
        db.Integer, nullable=False, index=True, info="Related program item"
    )
    spaceGroupId = db.Column(db.Integer, index=True, info="Related spaceGroup")
    lowRes = db.Column(db.Float(asdecimal=True))
    highRes = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")


class ModelList(db.Model):
    __tablename__ = "ModelList"

    modelListId = db.Column(db.Integer, primary_key=True)
    nsdFilePath = db.Column(db.String(255))
    chi2RgFilePath = db.Column(db.String(255))


class ModelToList(db.Model):
    __tablename__ = "ModelToList"

    modelToListId = db.Column(db.Integer, primary_key=True)
    modelId = db.Column(db.Integer, nullable=False, index=True)
    modelListId = db.Column(db.Integer, nullable=False, index=True)


class MotionCorrection(db.Model):
    __tablename__ = "MotionCorrection"

    motionCorrectionId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, index=True)
    autoProcProgramId = db.Column(db.Integer, index=True)
    imageNumber = db.Column(
        db.SmallInteger, info="Movie number, sequential in time 1-n"
    )
    firstFrame = db.Column(db.SmallInteger, info="First frame of movie used")
    lastFrame = db.Column(db.SmallInteger, info="Last frame of movie used")
    dosePerFrame = db.Column(db.Float, info="Dose per frame, Units: e-/A^2")
    doseWeight = db.Column(db.Float, info="Dose weight, Units: dimensionless")
    totalMotion = db.Column(db.Float, info="Total motion, Units: A")
    averageMotionPerFrame = db.Column(
        db.Float, info="Average motion per frame, Units: A"
    )
    driftPlotFullPath = db.Column(db.String(255), info="Full path to the drift plot")
    micrographFullPath = db.Column(db.String(255), info="Full path to the micrograph")
    micrographSnapshotFullPath = db.Column(
        db.String(255), info="Full path to a snapshot (jpg) of the micrograph"
    )
    patchesUsedX = db.Column(
        db.Integer, info="Number of patches used in x (for motioncor2)"
    )
    patchesUsedY = db.Column(
        db.Integer, info="Number of patches used in y (for motioncor2)"
    )
    fftFullPath = db.Column(
        db.String(255), info="Full path to the jpg image of the raw micrograph FFT"
    )
    fftCorrectedFullPath = db.Column(
        db.String(255),
        info="Full path to the jpg image of the drift corrected micrograph FFT",
    )
    comments = db.Column(db.String(255))
    movieId = db.Column(db.Integer, index=True)


class MotorPosition(db.Model):
    __tablename__ = "MotorPosition"

    motorPositionId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phiX = db.Column(db.Float(asdecimal=True))
    phiY = db.Column(db.Float(asdecimal=True))
    phiZ = db.Column(db.Float(asdecimal=True))
    sampX = db.Column(db.Float(asdecimal=True))
    sampY = db.Column(db.Float(asdecimal=True))
    omega = db.Column(db.Float(asdecimal=True))
    kappa = db.Column(db.Float(asdecimal=True))
    phi = db.Column(db.Float(asdecimal=True))
    chi = db.Column(db.Float(asdecimal=True))
    gridIndexY = db.Column(db.Integer)
    gridIndexZ = db.Column(db.Integer)
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )


class Movie(db.Model):
    __tablename__ = "Movie"

    movieId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, index=True)
    movieNumber = db.Column(db.Integer)
    movieFullPath = db.Column(db.String(255))
    positionX = db.Column(db.String(45))
    positionY = db.Column(db.String(45))
    nominalDefocus = db.Column(db.Float)
    micrographFullPath = db.Column(db.String(255))
    micrographSnapshotFullPath = db.Column(db.String(255))
    xmlMetaDataFullPath = db.Column(db.String(255))
    dosePerImage = db.Column(db.String(45))
    createdTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )


class PDB(db.Model):
    __tablename__ = "PDB"

    pdbId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    contents = db.Column(db.String)
    code = db.Column(db.String(4))


class PDBEntry(db.Model):
    __tablename__ = "PDBEntry"

    pdbEntryId = db.Column(db.Integer, primary_key=True)
    autoProcProgramId = db.Column(db.Integer, index=True)
    code = db.Column(db.String(4))
    cell_a = db.Column(db.Float)
    cell_b = db.Column(db.Float)
    cell_c = db.Column(db.Float)
    cell_alpha = db.Column(db.Float)
    cell_beta = db.Column(db.Float)
    cell_gamma = db.Column(db.Float)
    resolution = db.Column(db.Float)
    pdbTitle = db.Column(db.String(255))
    pdbAuthors = db.Column(db.String(600))
    pdbDate = db.Column(db.DateTime)
    pdbBeamlineName = db.Column(db.String(50))
    beamlines = db.Column(db.String(100))
    distance = db.Column(db.Float)
    autoProcCount = db.Column(db.SmallInteger)
    dataCollectionCount = db.Column(db.SmallInteger)
    beamlineMatch = db.Column(db.Integer)
    authorMatch = db.Column(db.Integer)


class PDBEntryHasAutoProcProgram(db.Model):
    __tablename__ = "PDBEntry_has_AutoProcProgram"

    pdbEntryHasAutoProcId = db.Column(db.Integer, primary_key=True)
    pdbEntryId = db.Column(db.Integer, nullable=False, index=True)
    autoProcProgramId = db.Column(db.Integer, nullable=False, index=True)
    distance = db.Column(db.Float)


class PHPSession(db.Model):
    __tablename__ = "PHPSession"

    id = db.Column(db.String(50), primary_key=True)
    accessDate = db.Column(db.DateTime)
    data = db.Column(db.String(4000))


class Particle(db.Model):
    __tablename__ = "Particle"

    particleId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, nullable=False, index=True)
    x = db.Column(db.Float)
    y = db.Column(db.Float)


class Permission(db.Model):
    __tablename__ = "Permission"

    permissionId = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(100))


class Person(db.Model):
    __tablename__ = "Person"

    personId = db.Column(db.Integer, primary_key=True)
    laboratoryId = db.Column(db.Integer, index=True)
    siteId = db.Column(db.Integer, index=True)
    personUUID = db.Column(db.String(45))
    familyName = db.Column(db.String(100), index=True)
    givenName = db.Column(db.String(45))
    title = db.Column(db.String(45))
    emailAddress = db.Column(db.String(60))
    phoneNumber = db.Column(db.String(45))
    login = db.Column(db.String(45), index=True)
    faxNumber = db.Column(db.String(45))
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )
    externalId = db.Column(db.BINARY(16))
    cache = db.Column(db.Text)


class Phasing(db.Model):
    __tablename__ = "Phasing"

    phasingId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingAnalysisId = db.Column(
        db.Integer, nullable=False, index=True, info="Related phasing analysis item"
    )
    phasingProgramRunId = db.Column(
        db.Integer, nullable=False, index=True, info="Related program item"
    )
    spaceGroupId = db.Column(db.Integer, index=True, info="Related spaceGroup")
    method = db.Column(
        db.ENUM("solvent flattening", "solvent flipping"), info="phasing method"
    )
    solventContent = db.Column(db.Float(asdecimal=True))
    enantiomorph = db.Column(db.Integer, info="0 or 1")
    lowRes = db.Column(db.Float(asdecimal=True))
    highRes = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )


class PhasingAnalysi(db.Model):
    __tablename__ = "PhasingAnalysis"

    phasingAnalysisId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")


class PhasingProgramAttachment(db.Model):
    __tablename__ = "PhasingProgramAttachment"

    phasingProgramAttachmentId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingProgramRunId = db.Column(
        db.Integer, nullable=False, index=True, info="Related program item"
    )
    fileType = db.Column(
        db.ENUM(
            "DSIGMA_RESOLUTION",
            "OCCUPANCY_SITENUMBER",
            "CONTRAST_CYCLE",
            "CCALL_CCWEAK",
            "IMAGE",
            "Map",
            "Logfile",
            "PDB",
            "CSV",
            "INS",
            "RES",
            "TXT",
        ),
        info="file type",
    )
    fileName = db.Column(db.String(45), info="file name")
    filePath = db.Column(db.String(255), info="file path")
    input = db.Column(db.Integer)
    recordTimeStamp = db.Column(
        db.DateTime,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )


class PhasingProgramRun(db.Model):
    __tablename__ = "PhasingProgramRun"

    phasingProgramRunId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingCommandLine = db.Column(db.String(255), info="Command line for phasing")
    phasingPrograms = db.Column(
        db.String(255), info="Phasing programs (comma separated)"
    )
    phasingStatus = db.Column(db.Integer, info="success (1) / fail (0)")
    phasingMessage = db.Column(db.String(255), info="warning, error,...")
    phasingStartTime = db.Column(db.DateTime, info="Processing start time")
    phasingEndTime = db.Column(db.DateTime, info="Processing end time")
    phasingEnvironment = db.Column(db.String(255), info="Cpus, Nodes,...")
    phasingDirectory = db.Column(db.String(255), info="Directory of execution")
    recordTimeStamp = db.Column(
        db.DateTime,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )


class PhasingStatistic(db.Model):
    __tablename__ = "PhasingStatistics"

    phasingStatisticsId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingHasScalingId1 = db.Column(
        db.Integer, nullable=False, index=True, info="the dataset in question"
    )
    phasingHasScalingId2 = db.Column(
        db.Integer,
        index=True,
        info="if this is MIT or MAD, which scaling are being compared, null otherwise",
    )
    phasingStepId = db.Column(db.Integer, index=True)
    numberOfBins = db.Column(db.Integer, info="the total number of bins")
    binNumber = db.Column(db.Integer, info="binNumber, 999 for overall")
    lowRes = db.Column(
        db.Float(asdecimal=True), info="low resolution cutoff of this binfloat"
    )
    highRes = db.Column(
        db.Float(asdecimal=True), info="high resolution cutoff of this binfloat"
    )
    metric = db.Column(
        db.ENUM(
            "Rcullis",
            "Average Fragment Length",
            "Chain Count",
            "Residues Count",
            "CC",
            "PhasingPower",
            "FOM",
            '<d"/sig>',
            "Best CC",
            "CC(1/2)",
            "Weak CC",
            "CFOM",
            "Pseudo_free_CC",
            "CC of partial model",
            "Start R-work",
            "Start R-free",
            "Final R-work",
            "Final R-free",
        ),
        info="metric",
    )
    statisticsValue = db.Column(db.Float(asdecimal=True), info="the statistics value")
    nReflections = db.Column(db.Integer)
    recordTimeStamp = db.Column(
        db.DateTime,
        server_default=db.FetchedValue(),
        info="Creation or last update date/time",
    )


class PhasingStep(db.Model):
    __tablename__ = "PhasingStep"

    phasingStepId = db.Column(db.Integer, primary_key=True)
    previousPhasingStepId = db.Column(db.Integer)
    programRunId = db.Column(db.Integer, index=True)
    spaceGroupId = db.Column(db.Integer, index=True)
    autoProcScalingId = db.Column(db.Integer, index=True)
    phasingAnalysisId = db.Column(db.Integer, index=True)
    phasingStepType = db.Column(
        db.ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        )
    )
    method = db.Column(db.String(45))
    solventContent = db.Column(db.String(45))
    enantiomorph = db.Column(db.String(45))
    lowRes = db.Column(db.String(45))
    highRes = db.Column(db.String(45))
    groupName = db.Column(db.String(45))
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )


class PhasingHasScaling(db.Model):
    __tablename__ = "Phasing_has_Scaling"

    phasingHasScalingId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingAnalysisId = db.Column(
        db.Integer, nullable=False, index=True, info="Related phasing analysis item"
    )
    autoProcScalingId = db.Column(
        db.Integer, nullable=False, index=True, info="Related autoProcScaling item"
    )
    datasetNumber = db.Column(
        db.Integer,
        info="serial number of the dataset and always reserve 0 for the reference",
    )
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )


class PlateGroup(db.Model):
    __tablename__ = "PlateGroup"

    plateGroupId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    storageTemperature = db.Column(db.String(45))


class PlateType(db.Model):
    __tablename__ = "PlateType"

    PlateTypeId = db.Column(db.Integer, primary_key=True)
    experimentId = db.Column(db.Integer, index=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(45))
    shape = db.Column(db.String(45))
    rowCount = db.Column(db.Integer)
    columnCount = db.Column(db.Integer)


class Position(db.Model):
    __tablename__ = "Position"

    positionId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    relativePositionId = db.Column(
        db.Integer, index=True, info="relative position, null otherwise"
    )
    posX = db.Column(db.Float(asdecimal=True))
    posY = db.Column(db.Float(asdecimal=True))
    posZ = db.Column(db.Float(asdecimal=True))
    scale = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")


class PreparePhasingDatum(db.Model):
    __tablename__ = "PreparePhasingData"

    preparePhasingDataId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingAnalysisId = db.Column(
        db.Integer, nullable=False, index=True, info="Related phasing analysis item"
    )
    phasingProgramRunId = db.Column(
        db.Integer, nullable=False, index=True, info="Related program item"
    )
    spaceGroupId = db.Column(db.Integer, index=True, info="Related spaceGroup")
    lowRes = db.Column(db.Float(asdecimal=True))
    highRes = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")


class ProcessingJob(db.Model):
    __tablename__ = "ProcessingJob"

    processingJobId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, index=True)
    displayName = db.Column(db.String(80), info="xia2, fast_dp, dimple, etc")
    comments = db.Column(
        db.String(255),
        info="For users to annotate the job and see the motivation for the job",
    )
    recordTimestamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info="When job was submitted",
    )
    recipe = db.Column(db.String(50), info="What we want to run (xia, dimple, etc).")
    automatic = db.Column(
        db.Integer,
        info="Whether this processing job was triggered automatically or not",
    )


class ProcessingJobImageSweep(db.Model):
    __tablename__ = "ProcessingJobImageSweep"

    processingJobImageSweepId = db.Column(db.Integer, primary_key=True)
    processingJobId = db.Column(db.Integer, index=True)
    dataCollectionId = db.Column(db.Integer, index=True)
    startImage = db.Column(db.Integer)
    endImage = db.Column(db.Integer)


class ProcessingJobParameter(db.Model):
    __tablename__ = "ProcessingJobParameter"

    processingJobParameterId = db.Column(db.Integer, primary_key=True)
    processingJobId = db.Column(db.Integer, index=True)
    parameterKey = db.Column(
        db.String(80), info="E.g. resolution, spacegroup, pipeline"
    )
    parameterValue = db.Column(db.String(1024))


class Project(db.Model):
    __tablename__ = "Project"

    projectId = db.Column(db.Integer, primary_key=True)
    personId = db.Column(db.Integer, index=True)
    title = db.Column(db.String(200))
    acronym = db.Column(db.String(100))
    owner = db.Column(db.String(50))


class ProjectHasBLSample(db.Model):
    __tablename__ = "Project_has_BLSample"

    projectId = db.Column(db.Integer, primary_key=True, nullable=False)
    blSampleId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)


class ProjectHasDCGroup(db.Model):
    __tablename__ = "Project_has_DCGroup"

    projectId = db.Column(db.Integer, primary_key=True, nullable=False)
    dataCollectionGroupId = db.Column(
        db.Integer, primary_key=True, nullable=False, index=True
    )


class ProjectHasEnergyScan(db.Model):
    __tablename__ = "Project_has_EnergyScan"

    projectId = db.Column(db.Integer, primary_key=True, nullable=False)
    energyScanId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)


class ProjectHasPerson(db.Model):
    __tablename__ = "Project_has_Person"

    projectId = db.Column(db.Integer, primary_key=True, nullable=False)
    personId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)


class ProjectHasProtein(db.Model):
    __tablename__ = "Project_has_Protein"

    projectId = db.Column(db.Integer, primary_key=True, nullable=False)
    proteinId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)


class ProjectHasSession(db.Model):
    __tablename__ = "Project_has_Session"

    projectId = db.Column(db.Integer, primary_key=True, nullable=False)
    sessionId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)


class ProjectHasShipping(db.Model):
    __tablename__ = "Project_has_Shipping"

    projectId = db.Column(db.Integer, primary_key=True, nullable=False)
    shippingId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)


class ProjectHasUser(db.Model):
    __tablename__ = "Project_has_User"

    projecthasuserid = db.Column(db.Integer, primary_key=True)
    projectid = db.Column(db.Integer, nullable=False, index=True)
    username = db.Column(db.String(15))


class ProjectHasXFEFSpectrum(db.Model):
    __tablename__ = "Project_has_XFEFSpectrum"

    projectId = db.Column(db.Integer, primary_key=True, nullable=False)
    xfeFluorescenceSpectrumId = db.Column(
        db.Integer, primary_key=True, nullable=False, index=True
    )


class Proposal(db.Model):
    __tablename__ = "Proposal"
    __table_args__ = (
        db.Index("Proposal_FKIndexCodeNumber", "proposalCode", "proposalNumber"),
    )

    proposalId = db.Column(db.Integer, primary_key=True)
    personId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    title = db.Column(db.String(200, "utf8mb4_unicode_ci"))
    proposalCode = db.Column(db.String(45))
    proposalNumber = db.Column(db.String(45))
    proposalType = db.Column(db.String(2), info="Proposal type: MX, BX")
    bltimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    externalId = db.Column(db.BINARY(16))
    state = db.Column(
        db.ENUM("Open", "Closed", "Cancelled"), server_default=db.FetchedValue()
    )


class ProposalHasPerson(db.Model):
    __tablename__ = "ProposalHasPerson"

    proposalHasPersonId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.Integer, nullable=False, index=True)
    personId = db.Column(db.Integer, nullable=False, index=True)


class Protein(db.Model):
    __tablename__ = "Protein"
    __table_args__ = (db.Index("ProteinAcronym_Index", "proposalId", "acronym"),)

    proteinId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    name = db.Column(db.String(255, "utf8mb4_unicode_ci"))
    acronym = db.Column(db.String(45), index=True)
    safetyLevel = db.Column(db.ENUM("GREEN", "YELLOW", "RED"))
    molecularMass = db.Column(db.Float(asdecimal=True))
    proteinType = db.Column(db.String(45))
    sequence = db.Column(db.Text)
    personId = db.Column(db.Integer, index=True)
    bltimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    isCreatedBySampleSheet = db.Column(db.Integer, server_default=db.FetchedValue())
    externalId = db.Column(db.BINARY(16))
    density = db.Column(db.Float)
    componentTypeId = db.Column(db.Integer, index=True)
    modId = db.Column(db.String(20))
    concentrationTypeId = db.Column(db.Integer)
    _global = db.Column("global", db.Integer, server_default=db.FetchedValue())


class ProteinHasLattice(db.Model):
    __tablename__ = "Protein_has_Lattice"

    proteinId = db.Column(db.Integer, primary_key=True)
    cell_a = db.Column(db.Float(asdecimal=True))
    cell_b = db.Column(db.Float(asdecimal=True))
    cell_c = db.Column(db.Float(asdecimal=True))
    cell_alpha = db.Column(db.Float(asdecimal=True))
    cell_beta = db.Column(db.Float(asdecimal=True))
    cell_gamma = db.Column(db.Float(asdecimal=True))


class ProteinHasPDB(db.Model):
    __tablename__ = "Protein_has_PDB"

    proteinhaspdbid = db.Column(db.Integer, primary_key=True)
    proteinid = db.Column(db.Integer, nullable=False, index=True)
    pdbid = db.Column(db.Integer, nullable=False, index=True)


class RigidBodyModeling(db.Model):
    __tablename__ = "RigidBodyModeling"

    rigidBodyModelingId = db.Column(db.Integer, primary_key=True)
    subtractionId = db.Column(db.Integer, nullable=False, index=True)
    fitFilePath = db.Column(db.String(255))
    rigidBodyModelFilePath = db.Column(db.String(255))
    logFilePath = db.Column(db.String(255))
    curveConfigFilePath = db.Column(db.String(255))
    subUnitConfigFilePath = db.Column(db.String(255))
    crossCorrConfigFilePath = db.Column(db.String(255))
    contactDescriptionFilePath = db.Column(db.String(255))
    symmetry = db.Column(db.String(255))
    creationDate = db.Column(db.String(45))


class RobotAction(db.Model):
    __tablename__ = "RobotAction"

    robotActionId = db.Column(db.Integer, primary_key=True)
    blsessionId = db.Column(db.Integer, nullable=False, index=True)
    blsampleId = db.Column(db.Integer, index=True)
    actionType = db.Column(
        db.ENUM("LOAD", "UNLOAD", "DISPOSE", "STORE", "WASH", "ANNEAL")
    )
    startTimestamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    endTimestamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    status = db.Column(
        db.ENUM("SUCCESS", "ERROR", "CRITICAL", "WARNING", "COMMANDNOTSENT")
    )
    message = db.Column(db.String(255))
    containerLocation = db.Column(db.SmallInteger)
    dewarLocation = db.Column(db.SmallInteger)
    sampleBarcode = db.Column(db.String(45))
    xtalSnapshotBefore = db.Column(db.String(255))
    xtalSnapshotAfter = db.Column(db.String(255))


class Run(db.Model):
    __tablename__ = "Run"

    runId = db.Column(db.Integer, primary_key=True)
    timePerFrame = db.Column(db.String(45))
    timeStart = db.Column(db.String(45))
    timeEnd = db.Column(db.String(45))
    storageTemperature = db.Column(db.String(45))
    exposureTemperature = db.Column(db.String(45))
    spectrophotometer = db.Column(db.String(45))
    energy = db.Column(db.String(45))
    creationDate = db.Column(db.DateTime)
    frameAverage = db.Column(db.String(45))
    frameCount = db.Column(db.String(45))
    transmission = db.Column(db.String(45))
    beamCenterX = db.Column(db.String(45))
    beamCenterY = db.Column(db.String(45))
    pixelSizeX = db.Column(db.String(45))
    pixelSizeY = db.Column(db.String(45))
    radiationRelative = db.Column(db.String(45))
    radiationAbsolute = db.Column(db.String(45))
    normalization = db.Column(db.String(45))


class SWOnceToken(db.Model):
    __tablename__ = "SW_onceToken"

    onceTokenId = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(128))
    personId = db.Column(db.Integer, index=True)
    proposalId = db.Column(db.Integer, index=True)
    validity = db.Column(db.String(200))
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )


class SafetyLevel(db.Model):
    __tablename__ = "SafetyLevel"

    safetyLevelId = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(45))
    description = db.Column(db.String(45))


class SamplePlate(db.Model):
    __tablename__ = "SamplePlate"

    samplePlateId = db.Column(db.Integer, primary_key=True)
    experimentId = db.Column(db.Integer, nullable=False, index=True)
    plateGroupId = db.Column(db.Integer, index=True)
    plateTypeId = db.Column(db.Integer, index=True)
    instructionSetId = db.Column(db.Integer, index=True)
    boxId = db.Column(db.Integer)
    name = db.Column(db.String(45))
    slotPositionRow = db.Column(db.String(45))
    slotPositionColumn = db.Column(db.String(45))
    storageTemperature = db.Column(db.String(45))


class SamplePlatePosition(db.Model):
    __tablename__ = "SamplePlatePosition"

    samplePlatePositionId = db.Column(db.Integer, primary_key=True)
    samplePlateId = db.Column(db.Integer, nullable=False, index=True)
    rowNumber = db.Column(db.Integer)
    columnNumber = db.Column(db.Integer)
    volume = db.Column(db.String(45))


class SaxsDataCollection(db.Model):
    __tablename__ = "SaxsDataCollection"

    dataCollectionId = db.Column(db.Integer, primary_key=True)
    experimentId = db.Column(db.Integer, nullable=False, index=True)
    comments = db.Column(db.String(5120))


class ScanParametersModel(db.Model):
    __tablename__ = "ScanParametersModel"

    scanParametersModelId = db.Column(db.Integer, primary_key=True)
    scanParametersServiceId = db.Column(db.Integer, index=True)
    dataCollectionPlanId = db.Column(db.Integer, index=True)
    modelNumber = db.Column(db.Integer)
    start = db.Column(db.Float(asdecimal=True))
    stop = db.Column(db.Float(asdecimal=True))
    step = db.Column(db.Float(asdecimal=True))
    array = db.Column(db.Text)


class ScanParametersService(db.Model):
    __tablename__ = "ScanParametersService"

    scanParametersServiceId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(45))


class Schedule(db.Model):
    __tablename__ = "Schedule"

    scheduleId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))


class ScheduleComponent(db.Model):
    __tablename__ = "ScheduleComponent"

    scheduleComponentId = db.Column(db.Integer, primary_key=True)
    scheduleId = db.Column(db.Integer, nullable=False, index=True)
    inspectionTypeId = db.Column(db.Integer, index=True)
    offset_hours = db.Column(db.Integer)


class SchemaStatu(db.Model):
    __tablename__ = "SchemaStatus"

    schemaStatusId = db.Column(db.Integer, primary_key=True)
    scriptName = db.Column(db.String(100), nullable=False, unique=True)
    schemaStatus = db.Column(db.String(10))
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )


class Screen(db.Model):
    __tablename__ = "Screen"

    screenId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    proposalId = db.Column(db.Integer, index=True)
    _global = db.Column("global", db.Integer)


class ScreenComponent(db.Model):
    __tablename__ = "ScreenComponent"

    screenComponentId = db.Column(db.Integer, primary_key=True)
    screenComponentGroupId = db.Column(db.Integer, nullable=False, index=True)
    componentId = db.Column(db.Integer, index=True)
    concentration = db.Column(db.Float)
    pH = db.Column(db.Float)


class ScreenComponentGroup(db.Model):
    __tablename__ = "ScreenComponentGroup"

    screenComponentGroupId = db.Column(db.Integer, primary_key=True)
    screenId = db.Column(db.Integer, nullable=False, index=True)
    position = db.Column(db.SmallInteger)


class Screening(db.Model):
    __tablename__ = "Screening"

    screeningId = db.Column(db.Integer, primary_key=True)
    diffractionPlanId = db.Column(
        db.Integer, index=True, info="references DiffractionPlan"
    )
    dataCollectionGroupId = db.Column(db.Integer, index=True)
    dataCollectionId = db.Column(db.Integer)
    bltimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue()
    )
    programVersion = db.Column(db.String(45))
    comments = db.Column(db.String(255))
    shortComments = db.Column(db.String(20))
    xmlSampleInformation = db.Column(db.LONGBLOB)


class ScreeningInput(db.Model):
    __tablename__ = "ScreeningInput"

    screeningInputId = db.Column(db.Integer, primary_key=True)
    screeningId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    diffractionPlanId = db.Column(db.Integer, info="references DiffractionPlan table")
    beamX = db.Column(db.Float)
    beamY = db.Column(db.Float)
    rmsErrorLimits = db.Column(db.Float)
    minimumFractionIndexed = db.Column(db.Float)
    maximumFractionRejected = db.Column(db.Float)
    minimumSignalToNoise = db.Column(db.Float)
    xmlSampleInformation = db.Column(db.LONGBLOB)


class ScreeningOutput(db.Model):
    __tablename__ = "ScreeningOutput"

    screeningOutputId = db.Column(db.Integer, primary_key=True)
    screeningId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    statusDescription = db.Column(db.String(1024))
    rejectedReflections = db.Column(db.Integer)
    resolutionObtained = db.Column(db.Float)
    spotDeviationR = db.Column(db.Float)
    spotDeviationTheta = db.Column(db.Float)
    beamShiftX = db.Column(db.Float)
    beamShiftY = db.Column(db.Float)
    numSpotsFound = db.Column(db.Integer)
    numSpotsUsed = db.Column(db.Integer)
    numSpotsRejected = db.Column(db.Integer)
    mosaicity = db.Column(db.Float)
    iOverSigma = db.Column(db.Float)
    diffractionRings = db.Column(db.Integer)
    strategySuccess = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue()
    )
    mosaicityEstimated = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue()
    )
    rankingResolution = db.Column(db.Float(asdecimal=True))
    program = db.Column(db.String(45))
    doseTotal = db.Column(db.Float(asdecimal=True))
    totalExposureTime = db.Column(db.Float(asdecimal=True))
    totalRotationRange = db.Column(db.Float(asdecimal=True))
    totalNumberOfImages = db.Column(db.Integer)
    rFriedel = db.Column(db.Float(asdecimal=True))
    indexingSuccess = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue()
    )
    screeningSuccess = db.Column(db.Integer, server_default=db.FetchedValue())
    alignmentSuccess = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue()
    )


class ScreeningOutputLattice(db.Model):
    __tablename__ = "ScreeningOutputLattice"

    screeningOutputLatticeId = db.Column(db.Integer, primary_key=True)
    screeningOutputId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    spaceGroup = db.Column(db.String(45))
    pointGroup = db.Column(db.String(45))
    bravaisLattice = db.Column(db.String(45))
    rawOrientationMatrix_a_x = db.Column(db.Float)
    rawOrientationMatrix_a_y = db.Column(db.Float)
    rawOrientationMatrix_a_z = db.Column(db.Float)
    rawOrientationMatrix_b_x = db.Column(db.Float)
    rawOrientationMatrix_b_y = db.Column(db.Float)
    rawOrientationMatrix_b_z = db.Column(db.Float)
    rawOrientationMatrix_c_x = db.Column(db.Float)
    rawOrientationMatrix_c_y = db.Column(db.Float)
    rawOrientationMatrix_c_z = db.Column(db.Float)
    unitCell_a = db.Column(db.Float)
    unitCell_b = db.Column(db.Float)
    unitCell_c = db.Column(db.Float)
    unitCell_alpha = db.Column(db.Float)
    unitCell_beta = db.Column(db.Float)
    unitCell_gamma = db.Column(db.Float)
    bltimeStamp = db.Column(db.DateTime, server_default=db.FetchedValue())
    labelitIndexing = db.Column(db.Integer, server_default=db.FetchedValue())


class ScreeningRank(db.Model):
    __tablename__ = "ScreeningRank"

    screeningRankId = db.Column(db.Integer, primary_key=True)
    screeningRankSetId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    screeningId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    rankValue = db.Column(db.Float)
    rankInformation = db.Column(db.String(1024))


class ScreeningRankSet(db.Model):
    __tablename__ = "ScreeningRankSet"

    screeningRankSetId = db.Column(db.Integer, primary_key=True)
    rankEngine = db.Column(db.String(255))
    rankingProjectFileName = db.Column(db.String(255))
    rankingSummaryFileName = db.Column(db.String(255))


class ScreeningStrategy(db.Model):
    __tablename__ = "ScreeningStrategy"

    screeningStrategyId = db.Column(db.Integer, primary_key=True)
    screeningOutputId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    phiStart = db.Column(db.Float)
    phiEnd = db.Column(db.Float)
    rotation = db.Column(db.Float)
    exposureTime = db.Column(db.Float)
    resolution = db.Column(db.Float)
    completeness = db.Column(db.Float)
    multiplicity = db.Column(db.Float)
    anomalous = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    program = db.Column(db.String(45))
    rankingResolution = db.Column(db.Float)
    transmission = db.Column(
        db.Float, info="Transmission for the strategy as given by the strategy program."
    )


class ScreeningStrategySubWedge(db.Model):
    __tablename__ = "ScreeningStrategySubWedge"

    screeningStrategySubWedgeId = db.Column(
        db.Integer, primary_key=True, info="Primary key"
    )
    screeningStrategyWedgeId = db.Column(
        db.Integer, index=True, info="Foreign key to parent table"
    )
    subWedgeNumber = db.Column(
        db.Integer, info="The number of this subwedge within the wedge"
    )
    rotationAxis = db.Column(db.String(45), info="Angle where subwedge starts")
    axisStart = db.Column(db.Float, info="Angle where subwedge ends")
    axisEnd = db.Column(db.Float, info="Exposure time for subwedge")
    exposureTime = db.Column(db.Float, info="Transmission for subwedge")
    transmission = db.Column(db.Float)
    oscillationRange = db.Column(db.Float)
    completeness = db.Column(db.Float)
    multiplicity = db.Column(db.Float)
    doseTotal = db.Column(db.Float, info="Total dose for this subwedge")
    numberOfImages = db.Column(db.Integer, info="Number of images for this subwedge")
    comments = db.Column(db.String(255))
    resolution = db.Column(db.Float)


class ScreeningStrategyWedge(db.Model):
    __tablename__ = "ScreeningStrategyWedge"

    screeningStrategyWedgeId = db.Column(
        db.Integer, primary_key=True, info="Primary key"
    )
    screeningStrategyId = db.Column(
        db.Integer, index=True, info="Foreign key to parent table"
    )
    wedgeNumber = db.Column(
        db.Integer, info="The number of this wedge within the strategy"
    )
    resolution = db.Column(db.Float)
    completeness = db.Column(db.Float)
    multiplicity = db.Column(db.Float)
    doseTotal = db.Column(db.Float, info="Total dose for this wedge")
    numberOfImages = db.Column(db.Integer, info="Number of images for this wedge")
    phi = db.Column(db.Float)
    kappa = db.Column(db.Float)
    chi = db.Column(db.Float)
    comments = db.Column(db.String(255))
    wavelength = db.Column(db.Float(asdecimal=True))


class SessionType(db.Model):
    __tablename__ = "SessionType"

    sessionTypeId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.Integer, nullable=False, index=True)
    typeName = db.Column(db.String(31), nullable=False)


class SessionHasPerson(db.Model):
    __tablename__ = "Session_has_Person"

    sessionId = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
        index=True,
        server_default=db.FetchedValue(),
    )
    personId = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
        index=True,
        server_default=db.FetchedValue(),
    )
    role = db.Column(
        db.ENUM(
            "Local Contact",
            "Local Contact 2",
            "Staff",
            "Team Leader",
            "Co-Investigator",
            "Principal Investigator",
            "Alternate Contact",
        )
    )
    remote = db.Column(db.Integer, server_default=db.FetchedValue())


class Shipping(db.Model):
    __tablename__ = "Shipping"

    shippingId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(
        db.Integer, nullable=False, index=True, server_default=db.FetchedValue()
    )
    shippingName = db.Column(db.String(45), index=True)
    deliveryAgent_agentName = db.Column(db.String(45))
    deliveryAgent_shippingDate = db.Column(db.Date)
    deliveryAgent_deliveryDate = db.Column(db.Date)
    deliveryAgent_agentCode = db.Column(db.String(45))
    deliveryAgent_flightCode = db.Column(db.String(45))
    shippingStatus = db.Column(db.String(45), index=True)
    bltimeStamp = db.Column(db.DateTime)
    laboratoryId = db.Column(db.Integer, index=True)
    isStorageShipping = db.Column(db.Integer, server_default=db.FetchedValue())
    creationDate = db.Column(db.DateTime, index=True)
    comments = db.Column(db.String(255))
    sendingLabContactId = db.Column(db.Integer, index=True)
    returnLabContactId = db.Column(db.Integer, index=True)
    returnCourier = db.Column(db.String(45))
    dateOfShippingToUser = db.Column(db.DateTime)
    shippingType = db.Column(db.String(45))
    safetyLevel = db.Column(db.String(8))
    deliveryAgent_label = db.Column(db.Text)
    readyByTime = db.Column(db.Time)
    closeTime = db.Column(db.Time)
    physicalLocation = db.Column(db.String(50))
    deliveryAgent_pickupConfirmationTimestamp = db.Column(db.DateTime)
    deliveryAgent_pickupConfirmation = db.Column(db.String(10))
    deliveryAgent_readyByTime = db.Column(db.Time)
    deliveryAgent_callinTime = db.Column(db.Time)
    deliveryAgent_productcode = db.Column(db.String(10))
    deliveryAgent_flightCodePersonId = db.Column(db.Integer)
    deliveryAgent_flightCodeTimestamp = db.Column(db.DateTime)


class ShippingHasSession(db.Model):
    __tablename__ = "ShippingHasSession"

    shippingId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    sessionId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)


class SpaceGroup(db.Model):
    __tablename__ = "SpaceGroup"

    spaceGroupId = db.Column(db.Integer, primary_key=True, info="Primary key")
    geometryClassnameId = db.Column(db.Integer, index=True)
    spaceGroupNumber = db.Column(db.Integer, info="ccp4 number pr IUCR")
    spaceGroupShortName = db.Column(
        db.String(45), index=True, info="short name without blank"
    )
    spaceGroupName = db.Column(db.String(45), info="verbose name")
    bravaisLattice = db.Column(db.String(45), info="short name")
    bravaisLatticeName = db.Column(db.String(45), info="verbose name")
    pointGroup = db.Column(db.String(45), info="point group")
    MX_used = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue(),
        info="1 if used in the crystal form",
    )


class Speciman(db.Model):
    __tablename__ = "Specimen"

    specimenId = db.Column(db.Integer, primary_key=True)
    experimentId = db.Column(db.Integer, nullable=False, index=True)
    bufferId = db.Column(db.Integer, index=True)
    macromoleculeId = db.Column(db.Integer, index=True)
    samplePlatePositionId = db.Column(db.Integer, index=True)
    safetyLevelId = db.Column(db.Integer, index=True)
    stockSolutionId = db.Column(db.Integer, index=True)
    code = db.Column(db.String(255))
    concentration = db.Column(db.String(45))
    volume = db.Column(db.String(45))
    comments = db.Column(db.String(5120))


class StockSolution(db.Model):
    __tablename__ = "StockSolution"

    stockSolutionId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    bufferId = db.Column(db.Integer, nullable=False, index=True)
    macromoleculeId = db.Column(db.Integer, index=True)
    instructionSetId = db.Column(db.Integer, index=True)
    boxId = db.Column(db.Integer)
    name = db.Column(db.String(45))
    storageTemperature = db.Column(db.String(55))
    volume = db.Column(db.String(55))
    concentration = db.Column(db.String(55))
    comments = db.Column(db.String(255))


class Stoichiometry(db.Model):
    __tablename__ = "Stoichiometry"

    stoichiometryId = db.Column(db.Integer, primary_key=True)
    hostMacromoleculeId = db.Column(db.Integer, nullable=False, index=True)
    macromoleculeId = db.Column(db.Integer, nullable=False, index=True)
    ratio = db.Column(db.String(45))


class Structure(db.Model):
    __tablename__ = "Structure"

    structureId = db.Column(db.Integer, primary_key=True)
    macromoleculeId = db.Column(db.Integer, index=True)
    crystalId = db.Column(db.Integer, index=True)
    blSampleId = db.Column(db.Integer, index=True)
    filePath = db.Column(db.String(2048))
    structureType = db.Column(db.String(45))
    fromResiduesBases = db.Column(db.String(45))
    toResiduesBases = db.Column(db.String(45))
    sequence = db.Column(db.String(45))
    creationDate = db.Column(db.DateTime)
    name = db.Column(db.String(255))
    symmetry = db.Column(db.String(45))
    multiplicity = db.Column(db.String(45))
    groupName = db.Column(db.String(45))
    proposalId = db.Column(db.Integer, index=True)


class SubstructureDetermination(db.Model):
    __tablename__ = "SubstructureDetermination"

    substructureDeterminationId = db.Column(
        db.Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingAnalysisId = db.Column(
        db.Integer, nullable=False, index=True, info="Related phasing analysis item"
    )
    phasingProgramRunId = db.Column(
        db.Integer, nullable=False, index=True, info="Related program item"
    )
    spaceGroupId = db.Column(db.Integer, index=True, info="Related spaceGroup")
    method = db.Column(
        db.ENUM("SAD", "MAD", "SIR", "SIRAS", "MR", "MIR", "MIRAS", "RIP", "RIPAS"),
        info="phasing method",
    )
    lowRes = db.Column(db.Float(asdecimal=True))
    highRes = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(db.DateTime, info="Creation or last update date/time")


class Subtraction(db.Model):
    __tablename__ = "Subtraction"

    subtractionId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, nullable=False, index=True)
    rg = db.Column(db.String(45))
    rgStdev = db.Column(db.String(45))
    I0 = db.Column(db.String(45))
    I0Stdev = db.Column(db.String(45))
    firstPointUsed = db.Column(db.String(45))
    lastPointUsed = db.Column(db.String(45))
    quality = db.Column(db.String(45))
    isagregated = db.Column(db.String(45))
    concentration = db.Column(db.String(45))
    gnomFilePath = db.Column(db.String(255))
    rgGuinier = db.Column(db.String(45))
    rgGnom = db.Column(db.String(45))
    dmax = db.Column(db.String(45))
    total = db.Column(db.String(45))
    volume = db.Column(db.String(45))
    creationTime = db.Column(db.DateTime)
    kratkyFilePath = db.Column(db.String(255))
    scatteringFilePath = db.Column(db.String(255))
    guinierFilePath = db.Column(db.String(255))
    substractedFilePath = db.Column(db.String(255))
    gnomFilePathOutput = db.Column(db.String(255))
    sampleOneDimensionalFiles = db.Column(db.Integer, index=True)
    bufferOnedimensionalFiles = db.Column(db.Integer, index=True)
    sampleAverageFilePath = db.Column(db.String(255))
    bufferAverageFilePath = db.Column(db.String(255))


class SubtractionToAbInitioModel(db.Model):
    __tablename__ = "SubtractionToAbInitioModel"

    subtractionToAbInitioModelId = db.Column(db.Integer, primary_key=True)
    abInitioId = db.Column(db.Integer, index=True)
    subtractionId = db.Column(db.Integer, index=True)


class Superposition(db.Model):
    __tablename__ = "Superposition"

    superpositionId = db.Column(db.Integer, primary_key=True)
    subtractionId = db.Column(db.Integer, nullable=False, index=True)
    abinitioModelPdbFilePath = db.Column(db.String(255))
    aprioriPdbFilePath = db.Column(db.String(255))
    alignedPdbFilePath = db.Column(db.String(255))
    creationDate = db.Column(db.DateTime)


class UserGroup(db.Model):
    __tablename__ = "UserGroup"

    userGroupId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(31), nullable=False, unique=True)


class UserGroupHasPermission(db.Model):
    __tablename__ = "UserGroup_has_Permission"

    userGroupId = db.Column(db.Integer, primary_key=True, nullable=False)
    permissionId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)


class UserGroupHasPerson(db.Model):
    __tablename__ = "UserGroup_has_Person"

    userGroupId = db.Column(db.Integer, primary_key=True, nullable=False)
    personId = db.Column(db.Integer, primary_key=True, nullable=False, index=True)


t_V_AnalysisInfo = db.Table(
    "V_AnalysisInfo",
    db.Column("experimentCreationDate", db.DateTime),
    db.Column("timeStart", db.String(45)),
    db.Column("dataCollectionId", db.Integer),
    db.Column("measurementId", db.Integer),
    db.Column("proposalId", db.Integer),
    db.Column("proposalCode", db.String(45)),
    db.Column("proposalNumber", db.String(45)),
    db.Column("priorityLevelId", db.Integer),
    db.Column("code", db.String(100)),
    db.Column("exposureTemperature", db.String(45)),
    db.Column("transmission", db.String(45)),
    db.Column("measurementComments", db.String(512)),
    db.Column("experimentComments", db.String(512)),
    db.Column("experimentId", db.Integer),
    db.Column("experimentType", db.String(128)),
    db.Column("conc", db.String(45)),
    db.Column("bufferAcronym", db.String(45)),
    db.Column("macromoleculeAcronym", db.String(45)),
    db.Column("bufferId", db.Integer),
    db.Column("macromoleculeId", db.Integer),
    db.Column("subtractedFilePath", db.String(255)),
    db.Column("rgGuinier", db.String(45)),
    db.Column("firstPointUsed", db.String(45)),
    db.Column("lastPointUsed", db.String(45)),
    db.Column("I0", db.String(45)),
    db.Column("isagregated", db.String(45)),
    db.Column("subtractionId", db.BigInteger),
    db.Column("rgGnom", db.String(45)),
    db.Column("total", db.String(45)),
    db.Column("dmax", db.String(45)),
    db.Column("volume", db.String(45)),
    db.Column("i0stdev", db.String(45)),
    db.Column("quality", db.String(45)),
    db.Column("substractionCreationTime", db.DateTime),
    db.Column("bufferBeforeMeasurementId", db.BigInteger),
    db.Column("bufferAfterMeasurementId", db.BigInteger),
    db.Column("bufferBeforeFramesMerged", db.String(45)),
    db.Column("bufferBeforeMergeId", db.BigInteger),
    db.Column("bufferBeforeAverageFilePath", db.String(255)),
    db.Column("sampleMeasurementId", db.BigInteger),
    db.Column("sampleMergeId", db.BigInteger),
    db.Column("averageFilePath", db.String(255)),
    db.Column("framesMerge", db.String(45)),
    db.Column("framesCount", db.String(45)),
    db.Column("bufferAfterFramesMerged", db.String(45)),
    db.Column("bufferAfterMergeId", db.BigInteger),
    db.Column("bufferAfterAverageFilePath", db.String(255)),
    db.Column("modelListId1", db.BigInteger),
    db.Column("nsdFilePath", db.String(255)),
    db.Column("modelListId2", db.BigInteger),
    db.Column("chi2RgFilePath", db.String(255)),
    db.Column("averagedModel", db.String(255)),
    db.Column("averagedModelId", db.BigInteger),
    db.Column("rapidShapeDeterminationModel", db.String(255)),
    db.Column("rapidShapeDeterminationModelId", db.BigInteger),
    db.Column("shapeDeterminationModel", db.String(255)),
    db.Column("shapeDeterminationModelId", db.BigInteger),
    db.Column("abInitioModelId", db.BigInteger),
    db.Column("comments", db.String(512)),
)


t_v_datacollection = db.Table(
    "v_datacollection",
    db.Column("dataCollectionId", db.Integer),
    db.Column("dataCollectionGroupId", db.Integer),
    db.Column("strategySubWedgeOrigId", db.Integer),
    db.Column("detectorId", db.Integer),
    db.Column("blSubSampleId", db.Integer),
    db.Column("dataCollectionNumber", db.Integer),
    db.Column("startTime", db.DateTime),
    db.Column("endTime", db.DateTime),
    db.Column("runStatus", db.String(200)),
    db.Column("axisStart", db.Float),
    db.Column("axisEnd", db.Float),
    db.Column("axisRange", db.Float),
    db.Column("overlap", db.Float),
    db.Column("numberOfImages", db.Integer),
    db.Column("startImageNumber", db.Integer),
    db.Column("numberOfPasses", db.Integer),
    db.Column("exposureTime", db.Float),
    db.Column("imageDirectory", db.String(255)),
    db.Column("imagePrefix", db.String(45)),
    db.Column("imageSuffix", db.String(45)),
    db.Column("fileTemplate", db.String(255)),
    db.Column("wavelength", db.Float),
    db.Column("resolution", db.Float),
    db.Column("detectorDistance", db.Float),
    db.Column("xBeam", db.Float),
    db.Column("yBeam", db.Float),
    db.Column("xBeamPix", db.Float),
    db.Column("yBeamPix", db.Float),
    db.Column("comments", db.String(1024)),
    db.Column("printableForReport", db.Integer),
    db.Column("slitGapVertical", db.Float),
    db.Column("slitGapHorizontal", db.Float),
    db.Column("transmission", db.Float),
    db.Column("synchrotronMode", db.String(20)),
    db.Column("xtalSnapshotFullPath1", db.String(255)),
    db.Column("xtalSnapshotFullPath2", db.String(255)),
    db.Column("xtalSnapshotFullPath3", db.String(255)),
    db.Column("xtalSnapshotFullPath4", db.String(255)),
    db.Column("rotationAxis", db.ENUM("Omega", "Kappa", "Phi")),
    db.Column("phiStart", db.Float),
    db.Column("kappaStart", db.Float),
    db.Column("omegaStart", db.Float),
    db.Column("resolutionAtCorner", db.Float),
    db.Column("detector2Theta", db.Float),
    db.Column("undulatorGap1", db.Float),
    db.Column("undulatorGap2", db.Float),
    db.Column("undulatorGap3", db.Float),
    db.Column("beamSizeAtSampleX", db.Float),
    db.Column("beamSizeAtSampleY", db.Float),
    db.Column("centeringMethod", db.String(255)),
    db.Column("averageTemperature", db.Float),
    db.Column("actualCenteringPosition", db.String(255)),
    db.Column("beamShape", db.String(45)),
    db.Column("flux", db.Float(asdecimal=True)),
    db.Column("flux_end", db.Float(asdecimal=True)),
    db.Column("totalAbsorbedDose", db.Float(asdecimal=True)),
    db.Column("bestWilsonPlotPath", db.String(255)),
    db.Column("imageQualityIndicatorsPlotPath", db.String(512)),
    db.Column("imageQualityIndicatorsCSVPath", db.String(512)),
    db.Column("sessionId", db.Integer),
    db.Column("proposalId", db.Integer),
    db.Column("workflowId", db.Integer),
    db.Column("AutoProcIntegration_dataCollectionId", db.Integer),
    db.Column("autoProcScalingId", db.Integer),
    db.Column("cell_a", db.Float),
    db.Column("cell_b", db.Float),
    db.Column("cell_c", db.Float),
    db.Column("cell_alpha", db.Float),
    db.Column("cell_beta", db.Float),
    db.Column("cell_gamma", db.Float),
    db.Column("anomalous", db.Integer),
    db.Column("scalingStatisticsType", db.ENUM("overall", "innerShell", "outerShell")),
    db.Column("resolutionLimitHigh", db.Float),
    db.Column("resolutionLimitLow", db.Float),
    db.Column("completeness", db.Float),
    db.Column("AutoProc_spaceGroup", db.String(45)),
    db.Column("autoProcId", db.Integer),
    db.Column("rMerge", db.Float),
    db.Column("AutoProcIntegration_autoProcIntegrationId", db.Integer),
    db.Column("AutoProcProgram_processingPrograms", db.String(255)),
    db.Column(
        "AutoProcProgram_processingStatus",
        db.ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    db.Column("AutoProcProgram_autoProcProgramId", db.Integer),
    db.Column("ScreeningOutput_rankingResolution", db.Float(asdecimal=True)),
)


t_v_datacollection_autoprocintegration = db.Table(
    "v_datacollection_autoprocintegration",
    db.Column("v_datacollection_summary_phasing_autoProcIntegrationId", db.Integer),
    db.Column("v_datacollection_summary_phasing_dataCollectionId", db.Integer),
    db.Column("v_datacollection_summary_phasing_cell_a", db.Float),
    db.Column("v_datacollection_summary_phasing_cell_b", db.Float),
    db.Column("v_datacollection_summary_phasing_cell_c", db.Float),
    db.Column("v_datacollection_summary_phasing_cell_alpha", db.Float),
    db.Column("v_datacollection_summary_phasing_cell_beta", db.Float),
    db.Column("v_datacollection_summary_phasing_cell_gamma", db.Float),
    db.Column("v_datacollection_summary_phasing_anomalous", db.Integer),
    db.Column("v_datacollection_summary_phasing_autoproc_space_group", db.String(45)),
    db.Column("v_datacollection_summary_phasing_autoproc_autoprocId", db.Integer),
    db.Column("v_datacollection_summary_phasing_autoProcScalingId", db.Integer),
    db.Column("v_datacollection_processingPrograms", db.String(255)),
    db.Column("v_datacollection_summary_phasing_autoProcProgramId", db.Integer),
    db.Column(
        "v_datacollection_processingStatus",
        db.ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    db.Column("v_datacollection_processingStartTime", db.DateTime),
    db.Column("v_datacollection_processingEndTime", db.DateTime),
    db.Column("v_datacollection_summary_session_sessionId", db.Integer),
    db.Column("v_datacollection_summary_session_proposalId", db.Integer),
    db.Column("AutoProcIntegration_dataCollectionId", db.Integer),
    db.Column("AutoProcIntegration_autoProcIntegrationId", db.Integer),
    db.Column(
        "PhasingStep_phasing_phasingStepType",
        db.ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    db.Column("SpaceGroup_spaceGroupShortName", db.String(45)),
    db.Column("Protein_proteinId", db.Integer),
    db.Column("Protein_acronym", db.String(45)),
    db.Column("BLSample_name", db.String(45)),
    db.Column("DataCollection_dataCollectionNumber", db.Integer),
    db.Column("DataCollection_imagePrefix", db.String(45)),
)


t_v_datacollection_summary = db.Table(
    "v_datacollection_summary",
    db.Column("DataCollectionGroup_dataCollectionGroupId", db.Integer),
    db.Column("DataCollectionGroup_blSampleId", db.Integer),
    db.Column("DataCollectionGroup_sessionId", db.Integer),
    db.Column("DataCollectionGroup_workflowId", db.Integer),
    db.Column(
        "DataCollectionGroup_experimentType",
        db.ENUM(
            "EM",
            "SAD",
            "SAD - Inverse Beam",
            "OSC",
            "Collect - Multiwedge",
            "MAD",
            "Helical",
            "Multi-positional",
            "Mesh",
            "Burn",
            "MAD - Inverse Beam",
            "Characterization",
            "Dehydration",
            "Still",
        ),
    ),
    db.Column("DataCollectionGroup_startTime", db.DateTime),
    db.Column("DataCollectionGroup_endTime", db.DateTime),
    db.Column("DataCollectionGroup_comments", db.String(1024)),
    db.Column("DataCollectionGroup_actualSampleBarcode", db.String(45)),
    db.Column("DataCollectionGroup_xtalSnapshotFullPath", db.String(255)),
    db.Column("DataCollectionGroup_crystalClass", db.String(20)),
    db.Column("BLSample_blSampleId", db.Integer),
    db.Column("BLSample_crystalId", db.Integer),
    db.Column("BLSample_name", db.String(45)),
    db.Column("BLSample_code", db.String(45)),
    db.Column("BLSample_location", db.String(45)),
    db.Column("BLSample_blSampleStatus", db.String(20)),
    db.Column("BLSample_comments", db.String(1024)),
    db.Column("Container_containerId", db.Integer),
    db.Column("BLSession_sessionId", db.Integer),
    db.Column("BLSession_proposalId", db.Integer),
    db.Column("BLSession_protectedData", db.String(1024)),
    db.Column("Dewar_dewarId", db.Integer),
    db.Column("Dewar_code", db.String(45)),
    db.Column("Dewar_storageLocation", db.String(45)),
    db.Column("Container_containerType", db.String(20)),
    db.Column("Container_code", db.String(45)),
    db.Column("Container_capacity", db.Integer),
    db.Column("Container_beamlineLocation", db.String(20)),
    db.Column("Container_sampleChangerLocation", db.String(20)),
    db.Column("Protein_proteinId", db.Integer),
    db.Column("Protein_name", db.String(255)),
    db.Column("Protein_acronym", db.String(45)),
    db.Column("DataCollection_dataCollectionId", db.Integer),
    db.Column("DataCollection_dataCollectionGroupId", db.Integer),
    db.Column("DataCollection_startTime", db.DateTime),
    db.Column("DataCollection_endTime", db.DateTime),
    db.Column("DataCollection_runStatus", db.String(200)),
    db.Column("DataCollection_numberOfImages", db.Integer),
    db.Column("DataCollection_startImageNumber", db.Integer),
    db.Column("DataCollection_numberOfPasses", db.Integer),
    db.Column("DataCollection_exposureTime", db.Float),
    db.Column("DataCollection_imageDirectory", db.String(255)),
    db.Column("DataCollection_wavelength", db.Float),
    db.Column("DataCollection_resolution", db.Float),
    db.Column("DataCollection_detectorDistance", db.Float),
    db.Column("DataCollection_xBeam", db.Float),
    db.Column("transmission", db.Float),
    db.Column("DataCollection_yBeam", db.Float),
    db.Column("DataCollection_imagePrefix", db.String(45)),
    db.Column("DataCollection_comments", db.String(1024)),
    db.Column("DataCollection_xtalSnapshotFullPath1", db.String(255)),
    db.Column("DataCollection_xtalSnapshotFullPath2", db.String(255)),
    db.Column("DataCollection_xtalSnapshotFullPath3", db.String(255)),
    db.Column("DataCollection_xtalSnapshotFullPath4", db.String(255)),
    db.Column("DataCollection_phiStart", db.Float),
    db.Column("DataCollection_kappaStart", db.Float),
    db.Column("DataCollection_omegaStart", db.Float),
    db.Column("DataCollection_flux", db.Float(asdecimal=True)),
    db.Column("DataCollection_flux_end", db.Float(asdecimal=True)),
    db.Column("DataCollection_resolutionAtCorner", db.Float),
    db.Column("DataCollection_bestWilsonPlotPath", db.String(255)),
    db.Column("DataCollection_dataCollectionNumber", db.Integer),
    db.Column("DataCollection_axisRange", db.Float),
    db.Column("DataCollection_axisStart", db.Float),
    db.Column("DataCollection_axisEnd", db.Float),
    db.Column("DataCollection_rotationAxis", db.ENUM("Omega", "Kappa", "Phi")),
    db.Column("DataCollection_undulatorGap1", db.Float),
    db.Column("DataCollection_undulatorGap2", db.Float),
    db.Column("DataCollection_undulatorGap3", db.Float),
    db.Column("beamSizeAtSampleX", db.Float),
    db.Column("beamSizeAtSampleY", db.Float),
    db.Column("DataCollection_slitGapVertical", db.Float),
    db.Column("DataCollection_slitGapHorizontal", db.Float),
    db.Column("DataCollection_beamShape", db.String(45)),
    db.Column("DataCollection_voltage", db.Float),
    db.Column("DataCollection_xBeamPix", db.Float),
    db.Column("Workflow_workflowTitle", db.String(255)),
    db.Column(
        "Workflow_workflowType",
        db.ENUM(
            "Characterisation",
            "Undefined",
            "BioSAXS Post Processing",
            "EnhancedCharacterisation",
            "LineScan",
            "MeshScan",
            "Dehydration",
            "KappaReorientation",
            "BurnStrategy",
            "XrayCentering",
            "DiffractionTomography",
            "TroubleShooting",
            "VisualReorientation",
            "HelicalCharacterisation",
            "GroupedProcessing",
            "MXPressE",
            "MXPressO",
            "MXPressL",
            "MXScore",
            "MXPressI",
            "MXPressM",
            "MXPressA",
            "CollectAndSpectra",
            "LowDoseDC",
            "EnergyInterleavedMAD",
            "MXPressH",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressR",
            "MXPressR_180",
            "MXPressR_dehydration",
            "MeshAndCollect",
            "MeshAndCollectFromFile",
        ),
    ),
    db.Column("Workflow_status", db.String(255)),
    db.Column("Workflow_workflowId", db.Integer),
    db.Column("AutoProcIntegration_dataCollectionId", db.Integer),
    db.Column("autoProcScalingId", db.Integer),
    db.Column("cell_a", db.Float),
    db.Column("cell_b", db.Float),
    db.Column("cell_c", db.Float),
    db.Column("cell_alpha", db.Float),
    db.Column("cell_beta", db.Float),
    db.Column("cell_gamma", db.Float),
    db.Column("anomalous", db.Integer),
    db.Column("scalingStatisticsType", db.ENUM("overall", "innerShell", "outerShell")),
    db.Column("resolutionLimitHigh", db.Float),
    db.Column("resolutionLimitLow", db.Float),
    db.Column("completeness", db.Float),
    db.Column("AutoProc_spaceGroup", db.String(45)),
    db.Column("autoProcId", db.Integer),
    db.Column("rMerge", db.Float),
    db.Column("AutoProcIntegration_autoProcIntegrationId", db.Integer),
    db.Column("AutoProcProgram_processingPrograms", db.String(255)),
    db.Column(
        "AutoProcProgram_processingStatus",
        db.ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    db.Column("AutoProcProgram_autoProcProgramId", db.Integer),
    db.Column("Screening_screeningId", db.Integer),
    db.Column("Screening_dataCollectionId", db.Integer),
    db.Column("Screening_dataCollectionGroupId", db.Integer),
    db.Column("ScreeningOutput_strategySuccess", db.Integer),
    db.Column("ScreeningOutput_indexingSuccess", db.Integer),
    db.Column("ScreeningOutput_rankingResolution", db.Float(asdecimal=True)),
    db.Column("ScreeningOutput_mosaicity", db.Float),
    db.Column("ScreeningOutputLattice_spaceGroup", db.String(45)),
    db.Column("ScreeningOutputLattice_unitCell_a", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_b", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_c", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_alpha", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_beta", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_gamma", db.Float),
    db.Column("ScreeningOutput_totalExposureTime", db.Float(asdecimal=True)),
    db.Column("ScreeningOutput_totalRotationRange", db.Float(asdecimal=True)),
    db.Column("ScreeningOutput_totalNumberOfImages", db.Integer),
    db.Column("ScreeningStrategySubWedge_exposureTime", db.Float),
    db.Column("ScreeningStrategySubWedge_transmission", db.Float),
    db.Column("ScreeningStrategySubWedge_oscillationRange", db.Float),
    db.Column("ScreeningStrategySubWedge_numberOfImages", db.Integer),
    db.Column("ScreeningStrategySubWedge_multiplicity", db.Float),
    db.Column("ScreeningStrategySubWedge_completeness", db.Float),
    db.Column("ScreeningStrategySubWedge_axisStart", db.Float),
    db.Column("Shipping_shippingId", db.Integer),
    db.Column("Shipping_shippingName", db.String(45)),
    db.Column("Shipping_shippingStatus", db.String(45)),
    db.Column("diffractionPlanId", db.Integer),
    db.Column(
        "experimentKind",
        db.ENUM(
            "Default",
            "MXPressE",
            "MXPressO",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressI",
            "MXPressE_SAD",
            "MXScore",
            "MXPressM",
            "MAD",
            "SAD",
            "Fixed",
            "Ligand binding",
            "Refinement",
            "OSC",
            "MAD - Inverse Beam",
            "SAD - Inverse Beam",
        ),
    ),
    db.Column("observedResolution", db.Float),
    db.Column("minimalResolution", db.Float),
    db.Column("exposureTime", db.Float),
    db.Column("oscillationRange", db.Float),
    db.Column("maximalResolution", db.Float),
    db.Column("screeningResolution", db.Float),
    db.Column("radiationSensitivity", db.Float),
    db.Column("anomalousScatterer", db.String(255)),
    db.Column("preferredBeamSizeX", db.Float),
    db.Column("preferredBeamSizeY", db.Float),
    db.Column("preferredBeamDiameter", db.Float),
    db.Column("DiffractipnPlan_comments", db.String(1024)),
    db.Column("aimedCompleteness", db.Float(asdecimal=True)),
    db.Column("aimedIOverSigmaAtHighestRes", db.Float(asdecimal=True)),
    db.Column("aimedMultiplicity", db.Float(asdecimal=True)),
    db.Column("aimedResolution", db.Float(asdecimal=True)),
    db.Column("anomalousData", db.Integer),
    db.Column("complexity", db.String(45)),
    db.Column("estimateRadiationDamage", db.Integer),
    db.Column("forcedSpaceGroup", db.String(45)),
    db.Column("requiredCompleteness", db.Float(asdecimal=True)),
    db.Column("requiredMultiplicity", db.Float(asdecimal=True)),
    db.Column("requiredResolution", db.Float(asdecimal=True)),
    db.Column("strategyOption", db.String(45)),
    db.Column("kappaStrategyOption", db.String(45)),
    db.Column("numberOfPositions", db.Integer),
    db.Column("minDimAccrossSpindleAxis", db.Float(asdecimal=True)),
    db.Column("maxDimAccrossSpindleAxis", db.Float(asdecimal=True)),
    db.Column("radiationSensitivityBeta", db.Float(asdecimal=True)),
    db.Column("radiationSensitivityGamma", db.Float(asdecimal=True)),
    db.Column("minOscWidth", db.Float),
    db.Column("Detector_detectorType", db.String(255)),
    db.Column("Detector_detectorManufacturer", db.String(255)),
    db.Column("Detector_detectorModel", db.String(255)),
    db.Column("Detector_detectorPixelSizeHorizontal", db.Float),
    db.Column("Detector_detectorPixelSizeVertical", db.Float),
    db.Column("Detector_detectorSerialNumber", db.String(30)),
    db.Column("Detector_detectorDistanceMin", db.Float(asdecimal=True)),
    db.Column("Detector_detectorDistanceMax", db.Float(asdecimal=True)),
    db.Column("Detector_trustedPixelValueRangeLower", db.Float(asdecimal=True)),
    db.Column("Detector_trustedPixelValueRangeUpper", db.Float(asdecimal=True)),
    db.Column("Detector_sensorThickness", db.Float),
    db.Column("Detector_overload", db.Float),
    db.Column("Detector_XGeoCorr", db.String(255)),
    db.Column("Detector_YGeoCorr", db.String(255)),
    db.Column("Detector_detectorMode", db.String(255)),
    db.Column("BeamLineSetup_undulatorType1", db.String(45)),
    db.Column("BeamLineSetup_undulatorType2", db.String(45)),
    db.Column("BeamLineSetup_undulatorType3", db.String(45)),
    db.Column("BeamLineSetup_synchrotronName", db.String(255)),
    db.Column("BeamLineSetup_synchrotronMode", db.String(255)),
    db.Column("BeamLineSetup_polarisation", db.Float),
    db.Column("BeamLineSetup_focusingOptic", db.String(255)),
    db.Column("BeamLineSetup_beamDivergenceHorizontal", db.Float),
    db.Column("BeamLineSetup_beamDivergenceVertical", db.Float),
    db.Column("BeamLineSetup_monochromatorType", db.String(255)),
)


t_v_datacollection_summary_autoprocintegration = db.Table(
    "v_datacollection_summary_autoprocintegration",
    db.Column("AutoProcIntegration_dataCollectionId", db.Integer),
    db.Column("cell_a", db.Float),
    db.Column("cell_b", db.Float),
    db.Column("cell_c", db.Float),
    db.Column("cell_alpha", db.Float),
    db.Column("cell_beta", db.Float),
    db.Column("cell_gamma", db.Float),
    db.Column("anomalous", db.Integer),
    db.Column("AutoProcIntegration_autoProcIntegrationId", db.Integer),
    db.Column(
        "v_datacollection_summary_autoprocintegration_processingPrograms",
        db.String(255),
    ),
    db.Column("AutoProcProgram_autoProcProgramId", db.Integer),
    db.Column(
        "v_datacollection_summary_autoprocintegration_processingStatus",
        db.ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    db.Column("AutoProcIntegration_phasing_dataCollectionId", db.Integer),
    db.Column(
        "PhasingStep_phasing_phasingStepType",
        db.ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    db.Column("SpaceGroup_spaceGroupShortName", db.String(45)),
    db.Column("autoProcId", db.Integer),
    db.Column("AutoProc_spaceGroup", db.String(45)),
    db.Column("scalingStatisticsType", db.ENUM("overall", "innerShell", "outerShell")),
    db.Column("resolutionLimitHigh", db.Float),
    db.Column("resolutionLimitLow", db.Float),
    db.Column("rMerge", db.Float),
    db.Column("completeness", db.Float),
    db.Column("autoProcScalingId", db.Integer),
)


t_v_datacollection_summary_datacollectiongroup = db.Table(
    "v_datacollection_summary_datacollectiongroup",
    db.Column("DataCollectionGroup_dataCollectionGroupId", db.Integer),
    db.Column("DataCollectionGroup_blSampleId", db.Integer),
    db.Column("DataCollectionGroup_sessionId", db.Integer),
    db.Column("DataCollectionGroup_workflowId", db.Integer),
    db.Column(
        "DataCollectionGroup_experimentType",
        db.ENUM(
            "EM",
            "SAD",
            "SAD - Inverse Beam",
            "OSC",
            "Collect - Multiwedge",
            "MAD",
            "Helical",
            "Multi-positional",
            "Mesh",
            "Burn",
            "MAD - Inverse Beam",
            "Characterization",
            "Dehydration",
            "Still",
        ),
    ),
    db.Column("DataCollectionGroup_startTime", db.DateTime),
    db.Column("DataCollectionGroup_endTime", db.DateTime),
    db.Column("DataCollectionGroup_comments", db.String(1024)),
    db.Column("DataCollectionGroup_actualSampleBarcode", db.String(45)),
    db.Column("DataCollectionGroup_xtalSnapshotFullPath", db.String(255)),
    db.Column("BLSample_blSampleId", db.Integer),
    db.Column("BLSample_crystalId", db.Integer),
    db.Column("BLSample_name", db.String(45)),
    db.Column("BLSample_code", db.String(45)),
    db.Column("BLSession_sessionId", db.Integer),
    db.Column("BLSession_proposalId", db.Integer),
    db.Column("BLSession_protectedData", db.String(1024)),
    db.Column("Protein_proteinId", db.Integer),
    db.Column("Protein_name", db.String(255)),
    db.Column("Protein_acronym", db.String(45)),
    db.Column("DataCollection_dataCollectionId", db.Integer),
    db.Column("DataCollection_dataCollectionGroupId", db.Integer),
    db.Column("DataCollection_startTime", db.DateTime),
    db.Column("DataCollection_endTime", db.DateTime),
    db.Column("DataCollection_runStatus", db.String(200)),
    db.Column("DataCollection_numberOfImages", db.Integer),
    db.Column("DataCollection_startImageNumber", db.Integer),
    db.Column("DataCollection_numberOfPasses", db.Integer),
    db.Column("DataCollection_exposureTime", db.Float),
    db.Column("DataCollection_imageDirectory", db.String(255)),
    db.Column("DataCollection_wavelength", db.Float),
    db.Column("DataCollection_resolution", db.Float),
    db.Column("DataCollection_detectorDistance", db.Float),
    db.Column("DataCollection_xBeam", db.Float),
    db.Column("DataCollection_yBeam", db.Float),
    db.Column("DataCollection_comments", db.String(1024)),
    db.Column("DataCollection_xtalSnapshotFullPath1", db.String(255)),
    db.Column("DataCollection_xtalSnapshotFullPath2", db.String(255)),
    db.Column("DataCollection_xtalSnapshotFullPath3", db.String(255)),
    db.Column("DataCollection_xtalSnapshotFullPath4", db.String(255)),
    db.Column("DataCollection_phiStart", db.Float),
    db.Column("DataCollection_kappaStart", db.Float),
    db.Column("DataCollection_omegaStart", db.Float),
    db.Column("DataCollection_resolutionAtCorner", db.Float),
    db.Column("DataCollection_bestWilsonPlotPath", db.String(255)),
    db.Column("Workflow_workflowTitle", db.String(255)),
    db.Column(
        "Workflow_workflowType",
        db.ENUM(
            "Characterisation",
            "Undefined",
            "BioSAXS Post Processing",
            "EnhancedCharacterisation",
            "LineScan",
            "MeshScan",
            "Dehydration",
            "KappaReorientation",
            "BurnStrategy",
            "XrayCentering",
            "DiffractionTomography",
            "TroubleShooting",
            "VisualReorientation",
            "HelicalCharacterisation",
            "GroupedProcessing",
            "MXPressE",
            "MXPressO",
            "MXPressL",
            "MXScore",
            "MXPressI",
            "MXPressM",
            "MXPressA",
            "CollectAndSpectra",
            "LowDoseDC",
            "EnergyInterleavedMAD",
            "MXPressH",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressR",
            "MXPressR_180",
            "MXPressR_dehydration",
            "MeshAndCollect",
            "MeshAndCollectFromFile",
        ),
    ),
    db.Column("Workflow_status", db.String(255)),
)


t_v_datacollection_summary_phasing = db.Table(
    "v_datacollection_summary_phasing",
    db.Column("v_datacollection_summary_phasing_phasingStepId", db.Integer),
    db.Column("v_datacollection_summary_phasing_previousPhasingStepId", db.Integer),
    db.Column("v_datacollection_summary_phasing_autoProcIntegrationId", db.Integer),
    db.Column("v_datacollection_summary_phasing_dataCollectionId", db.Integer),
    db.Column(
        "v_datacollection_summary_phasing_phasingStepType",
        db.ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    db.Column("v_datacollection_summary_phasing_method", db.String(45)),
    db.Column("v_datacollection_summary_phasing_solventContent", db.String(45)),
    db.Column("v_datacollection_summary_phasing_enantiomorph", db.String(45)),
    db.Column("v_datacollection_summary_phasing_lowRes", db.String(45)),
    db.Column("v_datacollection_summary_phasing_highRes", db.String(45)),
    db.Column("v_datacollection_summary_phasing_autoProcScalingId", db.Integer),
    db.Column("v_datacollection_summary_phasing_spaceGroupShortName", db.String(45)),
)


t_v_datacollection_summary_screening = db.Table(
    "v_datacollection_summary_screening",
    db.Column("Screening_screeningId", db.Integer),
    db.Column("Screening_dataCollectionId", db.Integer),
    db.Column("Screening_dataCollectionGroupId", db.Integer),
    db.Column("ScreeningOutput_strategySuccess", db.Integer),
    db.Column("ScreeningOutput_indexingSuccess", db.Integer),
    db.Column("ScreeningOutput_rankingResolution", db.Float(asdecimal=True)),
    db.Column("ScreeningOutput_mosaicityEstimated", db.Integer),
    db.Column("ScreeningOutput_mosaicity", db.Float),
    db.Column("ScreeningOutput_totalExposureTime", db.Float(asdecimal=True)),
    db.Column("ScreeningOutput_totalRotationRange", db.Float(asdecimal=True)),
    db.Column("ScreeningOutput_totalNumberOfImages", db.Integer),
    db.Column("ScreeningOutputLattice_spaceGroup", db.String(45)),
    db.Column("ScreeningOutputLattice_unitCell_a", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_b", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_c", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_alpha", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_beta", db.Float),
    db.Column("ScreeningOutputLattice_unitCell_gamma", db.Float),
    db.Column("ScreeningStrategySubWedge_exposureTime", db.Float),
    db.Column("ScreeningStrategySubWedge_transmission", db.Float),
    db.Column("ScreeningStrategySubWedge_oscillationRange", db.Float),
    db.Column("ScreeningStrategySubWedge_numberOfImages", db.Integer),
    db.Column("ScreeningStrategySubWedge_multiplicity", db.Float),
    db.Column("ScreeningStrategySubWedge_completeness", db.Float),
    db.Column("ScreeningStrategySubWedge_axisStart", db.Float),
    db.Column("ScreeningStrategySubWedge_axisEnd", db.Float),
    db.Column("ScreeningStrategySubWedge_rotationAxis", db.String(45)),
)


t_v_dewar = db.Table(
    "v_dewar",
    db.Column("proposalId", db.Integer),
    db.Column("shippingId", db.Integer),
    db.Column("shippingName", db.String(45)),
    db.Column("dewarId", db.Integer),
    db.Column("dewarName", db.String(45)),
    db.Column("dewarStatus", db.String(45)),
    db.Column("proposalCode", db.String(45)),
    db.Column("proposalNumber", db.String(45)),
    db.Column("creationDate", db.DateTime),
    db.Column("shippingType", db.String(45)),
    db.Column("barCode", db.String(45)),
    db.Column("shippingStatus", db.String(45)),
    db.Column("beamLineName", db.String(45)),
    db.Column("nbEvents", db.BigInteger),
    db.Column("storesin", db.BigInteger),
    db.Column("nbSamples", db.BigInteger),
)


t_v_dewarBeamline = db.Table(
    "v_dewarBeamline",
    db.Column("beamLineName", db.String(45)),
    db.Column("COUNT(*)", db.BigInteger),
)


t_v_dewarBeamlineByWeek = db.Table(
    "v_dewarBeamlineByWeek",
    db.Column("Week", db.String(16)),
    db.Column("P12", db.BigInteger),
    db.Column("P13", db.BigInteger),
    db.Column("P14", db.BigInteger),
)


t_v_dewarByWeek = db.Table(
    "v_dewarByWeek",
    db.Column("Week", db.String(16)),
    db.Column("Dewars Tracked", db.BigInteger),
    db.Column("Dewars Non-Tracked", db.BigInteger),
)


t_v_dewarList = db.Table(
    "v_dewarList",
    db.Column("proposal", db.String(90)),
    db.Column("shippingName", db.String(45)),
    db.Column("dewarName", db.String(45)),
    db.Column("barCode", db.String(45)),
    db.Column("creationDate", db.String(10)),
    db.Column("shippingType", db.String(45)),
    db.Column("nbEvents", db.BigInteger),
    db.Column("dewarStatus", db.String(45)),
    db.Column("shippingStatus", db.String(45)),
    db.Column("nbSamples", db.BigInteger),
)


t_v_dewarProposalCode = db.Table(
    "v_dewarProposalCode",
    db.Column("proposalCode", db.String(45)),
    db.Column("COUNT(*)", db.BigInteger),
)


t_v_dewarProposalCodeByWeek = db.Table(
    "v_dewarProposalCodeByWeek",
    db.Column("Week", db.String(16)),
    db.Column("MX", db.BigInteger),
    db.Column("FX", db.BigInteger),
    db.Column("P12", db.BigInteger),
    db.Column("P13", db.BigInteger),
    db.Column("P14", db.BigInteger),
    db.Column("Others", db.BigInteger),
)


t_v_dewar_summary = db.Table(
    "v_dewar_summary",
    db.Column("shippingName", db.String(45)),
    db.Column("deliveryAgent_agentName", db.String(45)),
    db.Column("deliveryAgent_shippingDate", db.Date),
    db.Column("deliveryAgent_deliveryDate", db.Date),
    db.Column("deliveryAgent_agentCode", db.String(45)),
    db.Column("deliveryAgent_flightCode", db.String(45)),
    db.Column("shippingStatus", db.String(45)),
    db.Column("bltimeStamp", db.DateTime),
    db.Column("laboratoryId", db.Integer),
    db.Column("isStorageShipping", db.Integer),
    db.Column("creationDate", db.DateTime),
    db.Column("Shipping_comments", db.String(255)),
    db.Column("sendingLabContactId", db.Integer),
    db.Column("returnLabContactId", db.Integer),
    db.Column("returnCourier", db.String(45)),
    db.Column("dateOfShippingToUser", db.DateTime),
    db.Column("shippingType", db.String(45)),
    db.Column("dewarId", db.Integer),
    db.Column("shippingId", db.Integer),
    db.Column("dewarCode", db.String(45)),
    db.Column("comments", db.String),
    db.Column("storageLocation", db.String(45)),
    db.Column("dewarStatus", db.String(45)),
    db.Column("isStorageDewar", db.Integer),
    db.Column("barCode", db.String(45)),
    db.Column("firstExperimentId", db.Integer),
    db.Column("customsValue", db.Integer),
    db.Column("transportValue", db.Integer),
    db.Column("trackingNumberToSynchrotron", db.String(30)),
    db.Column("trackingNumberFromSynchrotron", db.String(30)),
    db.Column("type", db.ENUM("Dewar", "Toolbox")),
    db.Column("isReimbursed", db.Integer),
    db.Column("sessionId", db.Integer),
    db.Column("beamlineName", db.String(45)),
    db.Column("sessionStartDate", db.DateTime),
    db.Column("sessionEndDate", db.DateTime),
    db.Column("beamLineOperator", db.String(255)),
    db.Column("nbReimbDewars", db.Integer),
    db.Column("proposalId", db.Integer),
    db.Column("containerId", db.Integer),
    db.Column("containerType", db.String(20)),
    db.Column("capacity", db.Integer),
    db.Column("beamlineLocation", db.String(20)),
    db.Column("sampleChangerLocation", db.String(20)),
    db.Column("containerStatus", db.String(45)),
    db.Column("containerCode", db.String(45)),
)


t_v_energyScan = db.Table(
    "v_energyScan",
    db.Column("energyScanId", db.Integer),
    db.Column("sessionId", db.Integer),
    db.Column("blSampleId", db.Integer),
    db.Column("fluorescenceDetector", db.String(255)),
    db.Column("scanFileFullPath", db.String(255)),
    db.Column("choochFileFullPath", db.String(255)),
    db.Column("jpegChoochFileFullPath", db.String(255)),
    db.Column("element", db.String(45)),
    db.Column("startEnergy", db.Float),
    db.Column("endEnergy", db.Float),
    db.Column("transmissionFactor", db.Float),
    db.Column("exposureTime", db.Float),
    db.Column("synchrotronCurrent", db.Float),
    db.Column("temperature", db.Float),
    db.Column("peakEnergy", db.Float),
    db.Column("peakFPrime", db.Float),
    db.Column("peakFDoublePrime", db.Float),
    db.Column("inflectionEnergy", db.Float),
    db.Column("inflectionFPrime", db.Float),
    db.Column("inflectionFDoublePrime", db.Float),
    db.Column("xrayDose", db.Float),
    db.Column("startTime", db.DateTime),
    db.Column("endTime", db.DateTime),
    db.Column("edgeEnergy", db.String(255)),
    db.Column("filename", db.String(255)),
    db.Column("beamSizeVertical", db.Float),
    db.Column("beamSizeHorizontal", db.Float),
    db.Column("crystalClass", db.String(20)),
    db.Column("comments", db.String(1024)),
    db.Column("flux", db.Float(asdecimal=True)),
    db.Column("flux_end", db.Float(asdecimal=True)),
    db.Column("BLSample_sampleId", db.Integer),
    db.Column("name", db.String(45)),
    db.Column("code", db.String(45)),
    db.Column("acronym", db.String(45)),
    db.Column("BLSession_proposalId", db.Integer),
)


t_v_hour = db.Table("v_hour", db.Column("num", db.String(18)))
