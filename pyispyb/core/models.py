# coding: utf-8
from sqlalchemy import (
    BINARY,
    BigInteger,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    LargeBinary,
    MetaData,
    SmallInteger,
    String,
    Table,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mysql.enumerated import ENUM
from sqlalchemy.dialects.mysql.types import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AbInitioModel(Base):
    __tablename__ = "AbInitioModel"

    abInitioModelId = Column(Integer, primary_key=True)
    modelListId = Column(
        ForeignKey("ModelList.modelListId", ondelete="CASCADE"), index=True
    )
    averagedModelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE"), index=True
    )
    rapidShapeDeterminationModelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE"), index=True
    )
    shapeDeterminationModelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE"), index=True
    )
    comments = Column(String(512))
    creationTime = Column(DateTime)

    Model = relationship(
        "Model",
        primaryjoin="AbInitioModel.averagedModelId == Model.modelId",
        backref="model_model_ab_initio_models",
    )
    ModelList = relationship(
        "ModelList",
        primaryjoin="AbInitioModel.modelListId == ModelList.modelListId",
        backref="ab_initio_models",
    )
    Model1 = relationship(
        "Model",
        primaryjoin="AbInitioModel.rapidShapeDeterminationModelId == Model.modelId",
        backref="model_model_ab_initio_models_0",
    )
    Model2 = relationship(
        "Model",
        primaryjoin="AbInitioModel.shapeDeterminationModelId == Model.modelId",
        backref="model_model_ab_initio_models",
    )


class Additive(Base):
    __tablename__ = "Additive"

    additiveId = Column(Integer, primary_key=True)
    name = Column(String(45))
    additiveType = Column(String(45))
    comments = Column(String(512))
    chemFormulaHead = Column(String(25), server_default=FetchedValue())
    chemFormulaTail = Column(String(25), server_default=FetchedValue())


class AdminActivity(Base):
    __tablename__ = "AdminActivity"

    adminActivityId = Column(Integer, primary_key=True)
    username = Column(
        String(45), nullable=False, unique=True, server_default=FetchedValue()
    )
    action = Column(String(45), index=True)
    comments = Column(String(100))
    dateTime = Column(DateTime)


class AdminVar(Base):
    __tablename__ = "AdminVar"

    varId = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)
    value = Column(String(1024), index=True)


class Aperture(Base):
    __tablename__ = "Aperture"

    apertureId = Column(Integer, primary_key=True)
    sizeX = Column(Float)


class Assembly(Base):
    __tablename__ = "Assembly"

    assemblyId = Column(Integer, primary_key=True)
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    creationDate = Column(DateTime)
    comments = Column(String(255))

    Macromolecule = relationship(
        "Macromolecule",
        primaryjoin="Assembly.macromoleculeId == Macromolecule.macromoleculeId",
        backref="assemblies",
    )


class AssemblyHasMacromolecule(Base):
    __tablename__ = "AssemblyHasMacromolecule"

    AssemblyHasMacromoleculeId = Column(Integer, primary_key=True)
    assemblyId = Column(
        ForeignKey("Assembly.assemblyId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    Assembly = relationship(
        "Assembly",
        primaryjoin="AssemblyHasMacromolecule.assemblyId == Assembly.assemblyId",
        backref="assembly_has_macromolecules",
    )
    Macromolecule = relationship(
        "Macromolecule",
        primaryjoin="AssemblyHasMacromolecule.macromoleculeId == Macromolecule.macromoleculeId",
        backref="assembly_has_macromolecules",
    )


class AssemblyRegion(Base):
    __tablename__ = "AssemblyRegion"

    assemblyRegionId = Column(Integer, primary_key=True)
    assemblyHasMacromoleculeId = Column(
        ForeignKey(
            "AssemblyHasMacromolecule.AssemblyHasMacromoleculeId", ondelete="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    assemblyRegionType = Column(String(45))
    name = Column(String(45))
    fromResiduesBases = Column(String(45))
    toResiduesBases = Column(String(45))

    AssemblyHasMacromolecule = relationship(
        "AssemblyHasMacromolecule",
        primaryjoin="AssemblyRegion.assemblyHasMacromoleculeId == AssemblyHasMacromolecule.AssemblyHasMacromoleculeId",
        backref="assembly_regions",
    )


class AutoProc(Base):
    __tablename__ = "AutoProc"

    autoProcId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcProgramId = Column(Integer, index=True, info="Related program item")
    spaceGroup = Column(String(45), info="Space group")
    refinedCell_a = Column(Float, info="Refined cell")
    refinedCell_b = Column(Float, info="Refined cell")
    refinedCell_c = Column(Float, info="Refined cell")
    refinedCell_alpha = Column(Float, info="Refined cell")
    refinedCell_beta = Column(Float, info="Refined cell")
    refinedCell_gamma = Column(Float, info="Refined cell")
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")


class AutoProcIntegration(Base):
    __tablename__ = "AutoProcIntegration"

    autoProcIntegrationId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        info="DataCollection item",
    )
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        info="Related program item",
    )
    startImageNumber = Column(Integer, info="start image number")
    endImageNumber = Column(Integer, info="end image number")
    refinedDetectorDistance = Column(
        Float, info="Refined DataCollection.detectorDistance"
    )
    refinedXBeam = Column(Float, info="Refined DataCollection.xBeam")
    refinedYBeam = Column(Float, info="Refined DataCollection.yBeam")
    rotationAxisX = Column(Float, info="Rotation axis")
    rotationAxisY = Column(Float, info="Rotation axis")
    rotationAxisZ = Column(Float, info="Rotation axis")
    beamVectorX = Column(Float, info="Beam vector")
    beamVectorY = Column(Float, info="Beam vector")
    beamVectorZ = Column(Float, info="Beam vector")
    cell_a = Column(Float, info="Unit cell")
    cell_b = Column(Float, info="Unit cell")
    cell_c = Column(Float, info="Unit cell")
    cell_alpha = Column(Float, info="Unit cell")
    cell_beta = Column(Float, info="Unit cell")
    cell_gamma = Column(Float, info="Unit cell")
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")
    anomalous = Column(
        Integer, server_default=FetchedValue(), info="boolean type:0 noanoum - 1 anoum"
    )

    AutoProcProgram = relationship(
        "AutoProcProgram",
        primaryjoin="AutoProcIntegration.autoProcProgramId == AutoProcProgram.autoProcProgramId",
        backref="auto_proc_integrations",
    )
    DataCollection = relationship(
        "DataCollection",
        primaryjoin="AutoProcIntegration.dataCollectionId == DataCollection.dataCollectionId",
        backref="auto_proc_integrations",
    )


class AutoProcProgram(Base):
    __tablename__ = "AutoProcProgram"

    autoProcProgramId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    dataCollectionId = Column(
        ForeignKey("DataCollection.dataCollectionId", ondelete="CASCADE"), index=True
    )
    processingCommandLine = Column(
        String(255), info="Command line for running the automatic processing"
    )
    processingPrograms = Column(
        String(255), info="Processing programs (comma separated)"
    )
    processingStatus = Column(
        ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"), info="success (1) / fail (0)"
    )
    processingMessage = Column(String(255), info="warning, error,...")
    processingStartTime = Column(DateTime, info="Processing start time")
    processingEndTime = Column(DateTime, info="Processing end time")
    processingEnvironment = Column(String(255), info="Cpus, Nodes,...")
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")

    DataCollection = relationship(
        "DataCollection",
        primaryjoin="AutoProcProgram.dataCollectionId == DataCollection.dataCollectionId",
        backref="auto_proc_programs",
    )


class AutoProcProgramAttachment(Base):
    __tablename__ = "AutoProcProgramAttachment"

    autoProcProgramAttachmentId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        info="Related autoProcProgram item",
    )
    fileType = Column(ENUM("Log", "Result", "Graph"), info="Type of file Attachment")
    fileName = Column(String(255), info="Attachment filename")
    filePath = Column(String(255), info="Attachment filepath to disk storage")
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")

    AutoProcProgram = relationship(
        "AutoProcProgram",
        primaryjoin="AutoProcProgramAttachment.autoProcProgramId == AutoProcProgram.autoProcProgramId",
        backref="auto_proc_program_attachments",
    )


class AutoProcScaling(Base):
    __tablename__ = "AutoProcScaling"
    __table_args__ = (Index("AutoProcScalingIdx1", "autoProcScalingId", "autoProcId"),)

    autoProcScalingId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcId = Column(
        ForeignKey("AutoProc.autoProcId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="Related autoProc item (used by foreign key)",
    )
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")
    resolutionEllipsoidAxis11 = Column(
        Float, info="Eigenvector for first diffraction limit, coord 1"
    )
    resolutionEllipsoidAxis12 = Column(
        Float, info="Eigenvector for first diffraction limit, coord 2"
    )
    resolutionEllipsoidAxis13 = Column(
        Float, info="Eigenvector for first diffraction limit, coord 3"
    )
    resolutionEllipsoidAxis21 = Column(
        Float, info="Eigenvector for second diffraction limit, coord 1"
    )
    resolutionEllipsoidAxis22 = Column(
        Float, info="Eigenvector for second diffraction limit, coord 2"
    )
    resolutionEllipsoidAxis23 = Column(
        Float, info="Eigenvector for second diffraction limit, coord 3"
    )
    resolutionEllipsoidAxis31 = Column(
        Float, info="Eigenvector for third diffraction limit, coord 1"
    )
    resolutionEllipsoidAxis32 = Column(
        Float, info="Eigenvector for third diffraction limit, coord 2"
    )
    resolutionEllipsoidAxis33 = Column(
        Float, info="Eigenvector for third diffraction limit, coord 3"
    )
    resolutionEllipsoidValue1 = Column(
        Float, info="First (anisotropic) diffraction limit"
    )
    resolutionEllipsoidValue2 = Column(
        Float, info="Second (anisotropic) diffraction limit"
    )
    resolutionEllipsoidValue3 = Column(
        Float, info="Third (anisotropic) diffraction limit"
    )

    AutoProc = relationship(
        "AutoProc",
        primaryjoin="AutoProcScaling.autoProcId == AutoProc.autoProcId",
        backref="auto_proc_scalings",
    )


class AutoProcScalingStatistics(Base):
    __tablename__ = "AutoProcScalingStatistics"

    autoProcScalingStatisticsId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcScalingId = Column(
        ForeignKey(
            "AutoProcScaling.autoProcScalingId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        info="Related autoProcScaling item (used by foreign key)",
    )
    scalingStatisticsType = Column(
        ENUM("overall", "innerShell", "outerShell"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
        info="Scaling statistics type",
    )
    comments = Column(String(255), info="Comments...")
    resolutionLimitLow = Column(Float, info="Low resolution limit")
    resolutionLimitHigh = Column(Float, info="High resolution limit")
    rMerge = Column(Float, info="Rmerge")
    rMeasWithinIPlusIMinus = Column(Float, info="Rmeas (within I+/I-)")
    rMeasAllIPlusIMinus = Column(Float, info="Rmeas (all I+ & I-)")
    rPimWithinIPlusIMinus = Column(Float, info="Rpim (within I+/I-) ")
    rPimAllIPlusIMinus = Column(Float, info="Rpim (all I+ & I-)")
    fractionalPartialBias = Column(Float, info="Fractional partial bias")
    nTotalObservations = Column(Integer, info="Total number of observations")
    nTotalUniqueObservations = Column(Integer, info="Total number unique")
    meanIOverSigI = Column(Float, info="Mean((I)/sd(I))")
    completeness = Column(Float, info="Completeness")
    multiplicity = Column(Float, info="Multiplicity")
    anomalousCompleteness = Column(Float, info="Anomalous completeness")
    anomalousMultiplicity = Column(Float, info="Anomalous multiplicity")
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")
    anomalous = Column(
        Integer, server_default=FetchedValue(), info="boolean type:0 noanoum - 1 anoum"
    )
    ccHalf = Column(Float, info="information from XDS")
    ccAno = Column(Float)
    sigAno = Column(String(45))
    isa = Column(String(45))
    completenessSpherical = Column(
        Float, info="Completeness calculated assuming isotropic diffraction"
    )
    completenessEllipsoidal = Column(
        Float, info="Completeness calculated allowing for anisotropic diffraction"
    )
    anomalousCompletenessSpherical = Column(
        Float, info="Anomalous completeness calculated assuming isotropic diffraction"
    )
    anomalousCompletenessEllipsoidal = Column(
        Float,
        info="Anisotropic completeness calculated allowing for anisotropic diffraction",
    )

    AutoProcScaling = relationship(
        "AutoProcScaling",
        primaryjoin="AutoProcScalingStatistics.autoProcScalingId == AutoProcScaling.autoProcScalingId",
        backref="auto_proc_scaling_statisticss",
    )


class AutoProcScalingHasInt(Base):
    __tablename__ = "AutoProcScaling_has_Int"
    __table_args__ = (
        Index(
            "AutoProcScalingHasInt_FKIndex3",
            "autoProcScalingId",
            "autoProcIntegrationId",
        ),
    )

    autoProcScaling_has_IntId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcScalingId = Column(
        ForeignKey(
            "AutoProcScaling.autoProcScalingId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        info="AutoProcScaling item",
    )
    autoProcIntegrationId = Column(
        ForeignKey(
            "AutoProcIntegration.autoProcIntegrationId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        info="AutoProcIntegration item",
    )
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")

    AutoProcIntegration = relationship(
        "AutoProcIntegration",
        primaryjoin="AutoProcScalingHasInt.autoProcIntegrationId == AutoProcIntegration.autoProcIntegrationId",
        backref="auto_proc_scaling_has_ints",
    )
    AutoProcScaling = relationship(
        "AutoProcScaling",
        primaryjoin="AutoProcScalingHasInt.autoProcScalingId == AutoProcScaling.autoProcScalingId",
        backref="auto_proc_scaling_has_ints",
    )


class AutoProcStatus(Base):
    __tablename__ = "AutoProcStatus"

    autoProcStatusId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    autoProcIntegrationId = Column(
        ForeignKey(
            "AutoProcIntegration.autoProcIntegrationId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    step = Column(
        ENUM("Indexing", "Integration", "Correction", "Scaling", "Importing"),
        nullable=False,
        info="autoprocessing step",
    )
    status = Column(
        ENUM("Launched", "Successful", "Failed"),
        nullable=False,
        info="autoprocessing status",
    )
    comments = Column(String(1024), info="comments")
    bltimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())

    AutoProcIntegration = relationship(
        "AutoProcIntegration",
        primaryjoin="AutoProcStatus.autoProcIntegrationId == AutoProcIntegration.autoProcIntegrationId",
        backref="auto_proc_statuses",
    )


class BFAutomationError(Base):
    __tablename__ = "BF_automationError"

    automationErrorId = Column(Integer, primary_key=True)
    errorType = Column(String(40), nullable=False)
    solution = Column(Text)


class BFAutomationFault(Base):
    __tablename__ = "BF_automationFault"

    automationFaultId = Column(Integer, primary_key=True)
    automationErrorId = Column(
        ForeignKey("BF_automationError.automationErrorId", ondelete="CASCADE"),
        index=True,
    )
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE"), index=True
    )
    severity = Column(ENUM("1", "2", "3"))
    stacktrace = Column(Text)
    resolved = Column(Integer)
    faultTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())

    BF_automationError = relationship(
        "BFAutomationError",
        primaryjoin="BFAutomationFault.automationErrorId == BFAutomationError.automationErrorId",
        backref="bf_automation_faults",
    )
    Container = relationship(
        "Container",
        primaryjoin="BFAutomationFault.containerId == Container.containerId",
        backref="bf_automation_faults",
    )


class BFComponent(Base):
    __tablename__ = "BF_component"

    componentId = Column(Integer, primary_key=True)
    systemId = Column(ForeignKey("BF_system.systemId", ondelete="CASCADE"), index=True)
    name = Column(String(100))
    description = Column(String(200))

    BF_system = relationship(
        "BFSystem",
        primaryjoin="BFComponent.systemId == BFSystem.systemId",
        backref="bf_components",
    )


class BFComponentBeamline(Base):
    __tablename__ = "BF_component_beamline"

    component_beamlineId = Column(Integer, primary_key=True)
    componentId = Column(
        ForeignKey("BF_component.componentId", ondelete="CASCADE"), index=True
    )
    beamlinename = Column(String(20))

    BF_component = relationship(
        "BFComponent",
        primaryjoin="BFComponentBeamline.componentId == BFComponent.componentId",
        backref="bf_component_beamlines",
    )


class BFFault(Base):
    __tablename__ = "BF_fault"

    faultId = Column(Integer, primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    owner = Column(String(50))
    subcomponentId = Column(
        ForeignKey("BF_subcomponent.subcomponentId", ondelete="CASCADE"), index=True
    )
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    beamtimelost = Column(Integer)
    beamtimelost_starttime = Column(DateTime)
    beamtimelost_endtime = Column(DateTime)
    title = Column(String(200))
    description = Column(Text)
    resolved = Column(Integer)
    resolution = Column(Text)
    assignee = Column(String(50))
    attachment = Column(String(200))
    eLogId = Column(Integer)
    personId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)
    assigneeId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)

    Person = relationship(
        "Person",
        primaryjoin="BFFault.assigneeId == Person.personId",
        backref="person_bf_faults",
    )
    Person1 = relationship(
        "Person",
        primaryjoin="BFFault.personId == Person.personId",
        backref="person_bf_faults_0",
    )
    BLSession = relationship(
        "BLSession",
        primaryjoin="BFFault.sessionId == BLSession.sessionId",
        backref="bf_faults",
    )
    BF_subcomponent = relationship(
        "BFSubcomponent",
        primaryjoin="BFFault.subcomponentId == BFSubcomponent.subcomponentId",
        backref="bf_faults",
    )


class BFSubcomponent(Base):
    __tablename__ = "BF_subcomponent"

    subcomponentId = Column(Integer, primary_key=True)
    componentId = Column(
        ForeignKey("BF_component.componentId", ondelete="CASCADE"), index=True
    )
    name = Column(String(100))
    description = Column(String(200))

    BF_component = relationship(
        "BFComponent",
        primaryjoin="BFSubcomponent.componentId == BFComponent.componentId",
        backref="bf_subcomponents",
    )


class BFSubcomponentBeamline(Base):
    __tablename__ = "BF_subcomponent_beamline"

    subcomponent_beamlineId = Column(Integer, primary_key=True)
    subcomponentId = Column(
        ForeignKey("BF_subcomponent.subcomponentId", ondelete="CASCADE"), index=True
    )
    beamlinename = Column(String(20))

    BF_subcomponent = relationship(
        "BFSubcomponent",
        primaryjoin="BFSubcomponentBeamline.subcomponentId == BFSubcomponent.subcomponentId",
        backref="bf_subcomponent_beamlines",
    )


class BFSystem(Base):
    __tablename__ = "BF_system"

    systemId = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(200))


class BFSystemBeamline(Base):
    __tablename__ = "BF_system_beamline"

    system_beamlineId = Column(Integer, primary_key=True)
    systemId = Column(ForeignKey("BF_system.systemId", ondelete="CASCADE"), index=True)
    beamlineName = Column(String(20))

    BF_system = relationship(
        "BFSystem",
        primaryjoin="BFSystemBeamline.systemId == BFSystem.systemId",
        backref="bf_system_beamlines",
    )


class BLSample(Base):
    __tablename__ = "BLSample"
    __table_args__ = (Index("crystalId", "crystalId", "containerId"),)

    blSampleId = Column(Integer, primary_key=True)
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    crystalId = Column(
        ForeignKey("Crystal.crystalId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    name = Column(String(100), index=True)
    code = Column(String(45))
    location = Column(String(45))
    holderLength = Column(Float(asdecimal=True))
    loopLength = Column(Float(asdecimal=True))
    loopType = Column(String(45))
    wireWidth = Column(Float(asdecimal=True))
    comments = Column(String(1024))
    completionStage = Column(String(45))
    structureStage = Column(String(45))
    publicationStage = Column(String(45))
    publicationComments = Column(String(255))
    blSampleStatus = Column(String(20), index=True)
    isInSampleChanger = Column(Integer)
    lastKnownCenteringPosition = Column(String(255))
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )
    SMILES = Column(
        String(400),
        info="the symbolic description of the structure of a chemical compound",
    )
    lastImageURL = Column(String(255))
    positionId = Column(Integer)
    blSubSampleId = Column(Integer)
    screenComponentGroupId = Column(Integer, index=True)
    volume = Column(Float)
    dimension1 = Column(Float(asdecimal=True))
    dimension2 = Column(Float(asdecimal=True))
    dimension3 = Column(Float(asdecimal=True))
    shape = Column(String(15))
    subLocation = Column(
        SmallInteger,
        info="Indicates the sample's location on a multi-sample pin, where 1 is closest to the pin base",
    )

    Container = relationship(
        "Container",
        primaryjoin="BLSample.containerId == Container.containerId",
        backref="bl_samples",
    )
    Crystal = relationship(
        "Crystal",
        primaryjoin="BLSample.crystalId == Crystal.crystalId",
        backref="bl_samples",
    )
    DiffractionPlan = relationship(
        "DiffractionPlan",
        primaryjoin="BLSample.diffractionPlanId == DiffractionPlan.diffractionPlanId",
        backref="diffractionplan_bl_samples",
    )
    DiffractionPlan1 = relationship(
        "DiffractionPlan",
        secondary="BLSample_has_DiffractionPlan",
        backref="diffractionplan_bl_samples_0",
    )
    Project = relationship(
        "Project", secondary="Project_has_BLSample", backref="bl_samples"
    )


class BLSampleGroup(Base):
    __tablename__ = "BLSampleGroup"

    blSampleGroupId = Column(Integer, primary_key=True)
    name = Column(String(100), info="Human-readable name")


class BLSampleGroupHasBLSample(Base):
    __tablename__ = "BLSampleGroup_has_BLSample"

    blSampleGroupId = Column(
        ForeignKey("BLSampleGroup.blSampleGroupId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    order = Column(Integer)
    type = Column(ENUM("background", "container", "sample", "calibrant"))

    BLSampleGroup = relationship(
        "BLSampleGroup",
        primaryjoin="BLSampleGroupHasBLSample.blSampleGroupId == BLSampleGroup.blSampleGroupId",
        backref="bl_sample_group_has_bl_samples",
    )
    BLSample = relationship(
        "BLSample",
        primaryjoin="BLSampleGroupHasBLSample.blSampleId == BLSample.blSampleId",
        backref="bl_sample_group_has_bl_samples",
    )


class BLSampleImage(Base):
    __tablename__ = "BLSampleImage"

    blSampleImageId = Column(Integer, primary_key=True)
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    micronsPerPixelX = Column(Float)
    micronsPerPixelY = Column(Float)
    imageFullPath = Column(String(255))
    blSampleImageScoreId = Column(Integer)
    comments = Column(String(255))
    blTimeStamp = Column(DateTime)
    containerInspectionId = Column(
        ForeignKey("ContainerInspection.containerInspectionId", ondelete="CASCADE"),
        index=True,
    )
    modifiedTimeStamp = Column(DateTime)

    BLSample = relationship(
        "BLSample",
        primaryjoin="BLSampleImage.blSampleId == BLSample.blSampleId",
        backref="bl_sample_images",
    )
    ContainerInspection = relationship(
        "ContainerInspection",
        primaryjoin="BLSampleImage.containerInspectionId == ContainerInspection.containerInspectionId",
        backref="bl_sample_images",
    )


class BLSampleImageAnalysis(Base):
    __tablename__ = "BLSampleImageAnalysis"

    blSampleImageAnalysisId = Column(Integer, primary_key=True)
    blSampleImageId = Column(
        ForeignKey("BLSampleImage.blSampleImageId", ondelete="CASCADE"), index=True
    )
    oavSnapshotBefore = Column(String(255))
    oavSnapshotAfter = Column(String(255))
    deltaX = Column(Integer)
    deltaY = Column(Integer)
    goodnessOfFit = Column(Float)
    scaleFactor = Column(Float)
    resultCode = Column(String(15))
    matchStartTimeStamp = Column(DateTime, server_default=FetchedValue())
    matchEndTimeStamp = Column(DateTime)

    BLSampleImage = relationship(
        "BLSampleImage",
        primaryjoin="BLSampleImageAnalysis.blSampleImageId == BLSampleImage.blSampleImageId",
        backref="bl_sample_image_analyses",
    )


class BLSampleImageScore(Base):
    __tablename__ = "BLSampleImageScore"

    blSampleImageScoreId = Column(Integer, primary_key=True)
    name = Column(String(45))
    score = Column(Float)
    colour = Column(String(15))


class BLSampleTypeHasComponent(Base):
    __tablename__ = "BLSampleType_has_Component"

    blSampleTypeId = Column(
        ForeignKey("Crystal.crystalId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    componentId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    abundance = Column(Float)

    Crystal = relationship(
        "Crystal",
        primaryjoin="BLSampleTypeHasComponent.blSampleTypeId == Crystal.crystalId",
        backref="bl_sample_type_has_components",
    )
    Protein = relationship(
        "Protein",
        primaryjoin="BLSampleTypeHasComponent.componentId == Protein.proteinId",
        backref="bl_sample_type_has_components",
    )


t_BLSample_has_DiffractionPlan = Table(
    "BLSample_has_DiffractionPlan",
    metadata,
    Column(
        "blSampleId",
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "diffractionPlanId",
        ForeignKey("DiffractionPlan.diffractionPlanId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class BLSampleHasEnergyScan(Base):
    __tablename__ = "BLSample_has_EnergyScan"

    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    energyScanId = Column(
        ForeignKey("EnergyScan.energyScanId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    blSampleHasEnergyScanId = Column(Integer, primary_key=True)

    BLSample = relationship(
        "BLSample",
        primaryjoin="BLSampleHasEnergyScan.blSampleId == BLSample.blSampleId",
        backref="bl_sample_has_energy_scans",
    )
    EnergyScan = relationship(
        "EnergyScan",
        primaryjoin="BLSampleHasEnergyScan.energyScanId == EnergyScan.energyScanId",
        backref="bl_sample_has_energy_scans",
    )


class BLSession(Base):
    __tablename__ = "BLSession"

    sessionId = Column(Integer, primary_key=True)
    expSessionPk = Column(Integer, info="smis session Pk ")
    beamLineSetupId = Column(
        ForeignKey(
            "BeamLineSetup.beamLineSetupId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    projectCode = Column(String(45))
    startDate = Column(DateTime, index=True)
    endDate = Column(DateTime, index=True)
    beamLineName = Column(String(45), index=True)
    scheduled = Column(Integer)
    nbShifts = Column(Integer, index=True)
    comments = Column(String(2000))
    beamLineOperator = Column(String(255))
    visit_number = Column(Integer, server_default=FetchedValue())
    bltimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    usedFlag = Column(
        Integer,
        info="indicates if session has Datacollections or XFE or EnergyScans attached",
    )
    sessionTitle = Column(String(255), info="fx accounts only")
    structureDeterminations = Column(Float)
    dewarTransport = Column(Float)
    databackupFrance = Column(Float, info="data backup and express delivery France")
    databackupEurope = Column(Float, info="data backup and express delivery Europe")
    operatorSiteNumber = Column(String(10), index=True, info="matricule site")
    lastUpdate = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="last update timestamp: by default the end of the session, the last collect...",
    )
    protectedData = Column(
        String(1024), info="indicates if the data are protected or not"
    )
    externalId = Column(BINARY(16))
    nbReimbDewars = Column(Integer)

    BeamLineSetup = relationship(
        "BeamLineSetup",
        primaryjoin="BLSession.beamLineSetupId == BeamLineSetup.beamLineSetupId",
        backref="bl_sessions",
    )
    Proposal = relationship(
        "Proposal",
        primaryjoin="BLSession.proposalId == Proposal.proposalId",
        backref="bl_sessions",
    )
    Shipping = relationship(
        "Shipping", secondary="ShippingHasSession", backref="bl_sessions"
    )


class BLSessionHasSCPosition(Base):
    __tablename__ = "BLSession_has_SCPosition"

    blsessionhasscpositionid = Column(Integer, primary_key=True)
    blsessionid = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    scContainer = Column(
        SmallInteger, info="Position of container within sample changer"
    )
    containerPosition = Column(SmallInteger, info="Position of sample within container")

    BLSession = relationship(
        "BLSession",
        primaryjoin="BLSessionHasSCPosition.blsessionid == BLSession.sessionId",
        backref="bl_session_has_sc_positions",
    )


class BLSubSample(Base):
    __tablename__ = "BLSubSample"

    blSubSampleId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="sample",
    )
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        info="eventually diffractionPlan",
    )
    positionId = Column(
        ForeignKey("Position.positionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="position of the subsample",
    )
    position2Id = Column(
        ForeignKey("Position.positionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    blSubSampleUUID = Column(String(45), info="uuid of the blsubsample")
    imgFileName = Column(String(255), info="image filename")
    imgFilePath = Column(String(1024), info="url image")
    comments = Column(String(1024), info="comments")
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )
    motorPositionId = Column(
        ForeignKey(
            "MotorPosition.motorPositionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        info="motor position",
    )

    BLSample = relationship(
        "BLSample",
        primaryjoin="BLSubSample.blSampleId == BLSample.blSampleId",
        backref="bl_sub_samples",
    )
    DiffractionPlan = relationship(
        "DiffractionPlan",
        primaryjoin="BLSubSample.diffractionPlanId == DiffractionPlan.diffractionPlanId",
        backref="bl_sub_samples",
    )
    MotorPosition = relationship(
        "MotorPosition",
        primaryjoin="BLSubSample.motorPositionId == MotorPosition.motorPositionId",
        backref="bl_sub_samples",
    )
    Position = relationship(
        "Position",
        primaryjoin="BLSubSample.position2Id == Position.positionId",
        backref="position_bl_sub_samples",
    )
    Position1 = relationship(
        "Position",
        primaryjoin="BLSubSample.positionId == Position.positionId",
        backref="position_bl_sub_samples_0",
    )


class BeamApertures(Base):
    __tablename__ = "BeamApertures"

    beamAperturesid = Column(Integer, primary_key=True)
    beamlineStatsId = Column(
        ForeignKey("BeamlineStats.beamlineStatsId", ondelete="CASCADE"), index=True
    )
    flux = Column(Float(asdecimal=True))
    x = Column(Float)
    y = Column(Float)
    apertureSize = Column(SmallInteger)

    BeamlineStats = relationship(
        "BeamlineStats",
        primaryjoin="BeamApertures.beamlineStatsId == BeamlineStats.beamlineStatsId",
        backref="beam_aperturess",
    )


class BeamCentres(Base):
    __tablename__ = "BeamCentres"

    beamCentresid = Column(Integer, primary_key=True)
    beamlineStatsId = Column(
        ForeignKey("BeamlineStats.beamlineStatsId", ondelete="CASCADE"), index=True
    )
    x = Column(Float)
    y = Column(Float)
    zoom = Column(Integer)

    BeamlineStats = relationship(
        "BeamlineStats",
        primaryjoin="BeamCentres.beamlineStatsId == BeamlineStats.beamlineStatsId",
        backref="beam_centress",
    )


class BeamLineSetup(Base):
    __tablename__ = "BeamLineSetup"

    beamLineSetupId = Column(Integer, primary_key=True)
    synchrotronMode = Column(String(255))
    undulatorType1 = Column(String(45))
    undulatorType2 = Column(String(45))
    undulatorType3 = Column(String(45))
    focalSpotSizeAtSample = Column(Float)
    focusingOptic = Column(String(255))
    beamDivergenceHorizontal = Column(Float)
    beamDivergenceVertical = Column(Float)
    polarisation = Column(Float)
    monochromatorType = Column(String(255))
    setupDate = Column(DateTime)
    synchrotronName = Column(String(255))
    maxExpTimePerDataCollection = Column(Float(asdecimal=True))
    minExposureTimePerImage = Column(Float(asdecimal=True))
    goniostatMaxOscillationSpeed = Column(Float(asdecimal=True))
    goniostatMinOscillationWidth = Column(Float(asdecimal=True))
    minTransmission = Column(Float(asdecimal=True))
    CS = Column(Float)
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )


class BeamlineAction(Base):
    __tablename__ = "BeamlineAction"

    beamlineActionId = Column(Integer, primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"), index=True
    )
    startTimestamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    endTimestamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    message = Column(String(255))
    parameter = Column(String(50))
    value = Column(String(30))
    loglevel = Column(ENUM("DEBUG", "CRITICAL", "INFO"))
    status = Column(
        ENUM("PAUSED", "RUNNING", "TERMINATED", "COMPLETE", "ERROR", "EPICSFAIL")
    )

    BLSession = relationship(
        "BLSession",
        primaryjoin="BeamlineAction.sessionId == BLSession.sessionId",
        backref="beamline_actions",
    )


class BeamlineStats(Base):
    __tablename__ = "BeamlineStats"

    beamlineStatsId = Column(Integer, primary_key=True)
    beamline = Column(String(10))
    recordTimeStamp = Column(DateTime)
    ringCurrent = Column(Float)
    energy = Column(Float)
    gony = Column(Float)
    beamW = Column(Float)
    beamH = Column(Float)
    flux = Column(Float(asdecimal=True))
    scanFileW = Column(String(255))
    scanFileH = Column(String(255))


class Buffer(Base):
    __tablename__ = "Buffer"

    bufferId = Column(Integer, primary_key=True)
    proposalId = Column(Integer, nullable=False, server_default=FetchedValue())
    safetyLevelId = Column(
        ForeignKey("SafetyLevel.safetyLevelId", ondelete="CASCADE"), index=True
    )
    name = Column(String(45))
    acronym = Column(String(45))
    pH = Column(String(45))
    composition = Column(String(45))
    comments = Column(String(512))
    BLSessionId = Column(Integer)
    electronDensity = Column(Float(7))

    SafetyLevel = relationship(
        "SafetyLevel",
        primaryjoin="Buffer.safetyLevelId == SafetyLevel.safetyLevelId",
        backref="buffers",
    )


class BufferHasAdditive(Base):
    __tablename__ = "BufferHasAdditive"

    bufferHasAdditiveId = Column(Integer, primary_key=True)
    bufferId = Column(
        ForeignKey("Buffer.bufferId", ondelete="CASCADE"), nullable=False, index=True
    )
    additiveId = Column(
        ForeignKey("Additive.additiveId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    measurementUnitId = Column(
        ForeignKey("MeasurementUnit.measurementUnitId", ondelete="CASCADE"), index=True
    )
    quantity = Column(String(45))

    Additive = relationship(
        "Additive",
        primaryjoin="BufferHasAdditive.additiveId == Additive.additiveId",
        backref="buffer_has_additives",
    )
    Buffer = relationship(
        "Buffer",
        primaryjoin="BufferHasAdditive.bufferId == Buffer.bufferId",
        backref="buffer_has_additives",
    )
    MeasurementUnit = relationship(
        "MeasurementUnit",
        primaryjoin="BufferHasAdditive.measurementUnitId == MeasurementUnit.measurementUnitId",
        backref="buffer_has_additives",
    )


class CTF(Base):
    __tablename__ = "CTF"

    CTFid = Column(Integer, primary_key=True)
    motionCorrectionId = Column(Integer, nullable=False, index=True)
    spectraImageThumbnailFullPath = Column(String(512))
    spectraImageFullPath = Column(String(512))
    defocusU = Column(String(45))
    defocusV = Column(String(45))
    angle = Column(String(45))
    crossCorrelationCoefficient = Column(String(45))
    resolutionLimit = Column(String(45))
    estimatedBfactor = Column(String(45))
    logFilePath = Column(String(512))
    createdTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())


class CalendarHash(Base):
    __tablename__ = "CalendarHash"

    calendarHashId = Column(Integer, primary_key=True)
    ckey = Column(String(50))
    hash = Column(String(128))
    beamline = Column(Integer)


class ComponentSubType(Base):
    __tablename__ = "ComponentSubType"

    componentSubTypeId = Column(Integer, primary_key=True)
    name = Column(String(31), nullable=False)
    hasPh = Column(Integer, server_default=FetchedValue())


class ComponentType(Base):
    __tablename__ = "ComponentType"

    componentTypeId = Column(Integer, primary_key=True)
    name = Column(String(31), nullable=False)


t_Component_has_SubType = Table(
    "Component_has_SubType",
    metadata,
    Column(
        "componentId",
        ForeignKey("Protein.proteinId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "componentSubTypeId",
        ForeignKey(
            "ComponentSubType.componentSubTypeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ConcentrationType(Base):
    __tablename__ = "ConcentrationType"

    concentrationTypeId = Column(Integer, primary_key=True)
    name = Column(String(31), nullable=False)
    symbol = Column(String(8), nullable=False)


class Container(Base):
    __tablename__ = "Container"

    containerId = Column(Integer, primary_key=True)
    dewarId = Column(
        ForeignKey("Dewar.dewarId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    code = Column(String(45))
    containerType = Column(String(20))
    capacity = Column(Integer)
    beamlineLocation = Column(String(20), index=True)
    sampleChangerLocation = Column(String(20))
    containerStatus = Column(String(45), index=True)
    bltimeStamp = Column(DateTime)
    barcode = Column(String(45), unique=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"), index=True
    )
    ownerId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)
    screenId = Column(Integer)
    scheduleId = Column(Integer)
    imagerId = Column(Integer)
    scLocationUpdated = Column(DateTime)
    requestedImagerId = Column(Integer)
    requestedReturn = Column(
        Integer,
        server_default=FetchedValue(),
        info="True for requesting return, False means container will be disposed",
    )
    comments = Column(String(255))
    experimentType = Column(String(20))
    storageTemperature = Column(Float)

    Dewar = relationship(
        "Dewar", primaryjoin="Container.dewarId == Dewar.dewarId", backref="containers"
    )
    Person = relationship(
        "Person",
        primaryjoin="Container.ownerId == Person.personId",
        backref="containers",
    )
    BLSession = relationship(
        "BLSession",
        primaryjoin="Container.sessionId == BLSession.sessionId",
        backref="containers",
    )


class ContainerHistory(Base):
    __tablename__ = "ContainerHistory"

    containerHistoryId = Column(Integer, primary_key=True)
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    location = Column(String(45))
    blTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    status = Column(String(45))

    Container = relationship(
        "Container",
        primaryjoin="ContainerHistory.containerId == Container.containerId",
        backref="container_histories",
    )


class ContainerInspection(Base):
    __tablename__ = "ContainerInspection"

    containerInspectionId = Column(Integer, primary_key=True)
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    inspectionTypeId = Column(
        ForeignKey("InspectionType.inspectionTypeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    imagerId = Column(ForeignKey("Imager.imagerId", ondelete="CASCADE"), index=True)
    temperature = Column(Float)
    blTimeStamp = Column(DateTime)
    scheduleComponentid = Column(
        ForeignKey("ScheduleComponent.scheduleComponentId", ondelete="CASCADE"),
        index=True,
    )
    state = Column(String(20))
    priority = Column(SmallInteger)
    manual = Column(Integer)
    scheduledTimeStamp = Column(DateTime)
    completedTimeStamp = Column(DateTime)

    Container = relationship(
        "Container",
        primaryjoin="ContainerInspection.containerId == Container.containerId",
        backref="container_inspections",
    )
    Imager = relationship(
        "Imager",
        primaryjoin="ContainerInspection.imagerId == Imager.imagerId",
        backref="container_inspections",
    )
    InspectionType = relationship(
        "InspectionType",
        primaryjoin="ContainerInspection.inspectionTypeId == InspectionType.inspectionTypeId",
        backref="container_inspections",
    )
    ScheduleComponent = relationship(
        "ScheduleComponent",
        primaryjoin="ContainerInspection.scheduleComponentid == ScheduleComponent.scheduleComponentId",
        backref="container_inspections",
    )


class ContainerQueue(Base):
    __tablename__ = "ContainerQueue"

    containerQueueId = Column(Integer, primary_key=True)
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    createdTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    completedTimeStamp = Column(DateTime)

    Container = relationship(
        "Container",
        primaryjoin="ContainerQueue.containerId == Container.containerId",
        backref="container_queues",
    )
    Person = relationship(
        "Person",
        primaryjoin="ContainerQueue.personId == Person.personId",
        backref="container_queues",
    )


class ContainerQueueSample(Base):
    __tablename__ = "ContainerQueueSample"

    containerQueueSampleId = Column(Integer, primary_key=True)
    containerQueueId = Column(
        ForeignKey(
            "ContainerQueue.containerQueueId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )

    BLSubSample = relationship(
        "BLSubSample",
        primaryjoin="ContainerQueueSample.blSubSampleId == BLSubSample.blSubSampleId",
        backref="container_queue_samples",
    )
    ContainerQueue = relationship(
        "ContainerQueue",
        primaryjoin="ContainerQueueSample.containerQueueId == ContainerQueue.containerQueueId",
        backref="container_queue_samples",
    )


class CryoemInitialModel(Base):
    __tablename__ = "CryoemInitialModel"

    cryoemInitialModelId = Column(Integer, primary_key=True)
    resolution = Column(Float, info="Unit: Angstroms")
    numberOfParticles = Column(Integer)

    ParticleClassification = relationship(
        "ParticleClassification",
        secondary="ParticleClassification_has_CryoemInitialModel",
        backref="cryoem_initial_models",
    )


class Crystal(Base):
    __tablename__ = "Crystal"

    crystalId = Column(Integer, primary_key=True)
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    proteinId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    crystalUUID = Column(String(45))
    name = Column(String(255))
    spaceGroup = Column(String(20))
    morphology = Column(String(255))
    color = Column(String(45))
    size_X = Column(Float(asdecimal=True))
    size_Y = Column(Float(asdecimal=True))
    size_Z = Column(Float(asdecimal=True))
    cell_a = Column(Float(asdecimal=True))
    cell_b = Column(Float(asdecimal=True))
    cell_c = Column(Float(asdecimal=True))
    cell_alpha = Column(Float(asdecimal=True))
    cell_beta = Column(Float(asdecimal=True))
    cell_gamma = Column(Float(asdecimal=True))
    comments = Column(String(255))
    pdbFileName = Column(String(255), info="pdb file name")
    pdbFilePath = Column(String(1024), info="pdb file path")
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )
    abundance = Column(Float)
    packingFraction = Column(Float)

    DiffractionPlan = relationship(
        "DiffractionPlan",
        primaryjoin="Crystal.diffractionPlanId == DiffractionPlan.diffractionPlanId",
        backref="crystals",
    )
    Protein = relationship(
        "Protein",
        primaryjoin="Crystal.proteinId == Protein.proteinId",
        backref="crystals",
    )


class CrystalHasUUID(Base):
    __tablename__ = "Crystal_has_UUID"

    crystal_has_UUID_Id = Column(Integer, primary_key=True)
    crystalId = Column(
        ForeignKey("Crystal.crystalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    UUID = Column(String(45), index=True)
    imageURL = Column(String(255))

    Crystal = relationship(
        "Crystal",
        primaryjoin="CrystalHasUUID.crystalId == Crystal.crystalId",
        backref="crystal_has_uuids",
    )


class DataAcquisition(Base):
    __tablename__ = "DataAcquisition"

    dataAcquisitionId = Column(Integer, primary_key=True)
    sampleCellId = Column(Integer, nullable=False)
    framesCount = Column(String(45))
    energy = Column(String(45))
    waitTime = Column(String(45))
    detectorDistance = Column(String(45))


class DataCollection(Base):
    __tablename__ = "DataCollection"

    dataCollectionId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    dataCollectionGroupId = Column(
        ForeignKey(
            "DataCollectionGroup.dataCollectionGroupId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        info="references DataCollectionGroup table",
    )
    strategySubWedgeOrigId = Column(
        ForeignKey(
            "ScreeningStrategySubWedge.screeningStrategySubWedgeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        info="references ScreeningStrategySubWedge table",
    )
    detectorId = Column(
        ForeignKey("Detector.detectorId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="references Detector table",
    )
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId", ondelete="CASCADE"), index=True
    )
    startPositionId = Column(Integer, index=True)
    endPositionId = Column(Integer, index=True)
    dataCollectionNumber = Column(Integer, index=True)
    startTime = Column(DateTime, index=True, info="Start time of the dataCollection")
    endTime = Column(DateTime, info="end time of the dataCollection")
    runStatus = Column(String(45))
    axisStart = Column(Float)
    axisEnd = Column(Float)
    axisRange = Column(Float)
    overlap = Column(Float)
    numberOfImages = Column(Integer)
    startImageNumber = Column(Integer)
    numberOfPasses = Column(Integer)
    exposureTime = Column(Float)
    imageDirectory = Column(String(255), index=True)
    imagePrefix = Column(String(100), index=True)
    imageSuffix = Column(String(45))
    imageContainerSubPath = Column(
        String(255),
        info="Internal path of a HDF5 file pointing to the data for this data collection",
    )
    fileTemplate = Column(String(255))
    wavelength = Column(Float)
    resolution = Column(Float)
    detectorDistance = Column(Float)
    xBeam = Column(Float)
    yBeam = Column(Float)
    xBeamPix = Column(Float, info="Beam size in pixels")
    yBeamPix = Column(Float, info="Beam size in pixels")
    comments = Column(String(1024))
    printableForReport = Column(Integer, server_default=FetchedValue())
    slitGapVertical = Column(Float)
    slitGapHorizontal = Column(Float)
    transmission = Column(Float)
    synchrotronMode = Column(String(20))
    xtalSnapshotFullPath1 = Column(String(255))
    xtalSnapshotFullPath2 = Column(String(255))
    xtalSnapshotFullPath3 = Column(String(255))
    xtalSnapshotFullPath4 = Column(String(255))
    rotationAxis = Column(ENUM("Omega", "Kappa", "Phi"))
    phiStart = Column(Float)
    kappaStart = Column(Float)
    omegaStart = Column(Float)
    resolutionAtCorner = Column(Float)
    detector2Theta = Column(Float)
    undulatorGap1 = Column(Float)
    undulatorGap2 = Column(Float)
    undulatorGap3 = Column(Float)
    beamSizeAtSampleX = Column(Float)
    beamSizeAtSampleY = Column(Float)
    centeringMethod = Column(String(255))
    averageTemperature = Column(Float)
    actualCenteringPosition = Column(String(255))
    beamShape = Column(String(45))
    flux = Column(Float(asdecimal=True))
    flux_end = Column(Float(asdecimal=True), info="flux measured after the collect")
    totalAbsorbedDose = Column(
        Float(asdecimal=True), info="expected dose delivered to the crystal, EDNA"
    )
    bestWilsonPlotPath = Column(String(255))
    imageQualityIndicatorsPlotPath = Column(String(512))
    imageQualityIndicatorsCSVPath = Column(String(512))
    blSampleId = Column(Integer)
    sessionId = Column(Integer, server_default=FetchedValue())
    experimentType = Column(String(24))
    crystalClass = Column(String(20))
    chiStart = Column(Float)
    detectorMode = Column(String(255))
    actualSampleBarcode = Column(String(45))
    actualSampleSlotInContainer = Column(Integer)
    actualContainerBarcode = Column(String(45))
    actualContainerSlotInSC = Column(Integer)
    positionId = Column(Integer)
    focalSpotSizeAtSampleX = Column(Float)
    polarisation = Column(Float)
    focalSpotSizeAtSampleY = Column(Float)
    apertureId = Column(Integer)
    screeningOrigId = Column(Integer)
    processedDataFile = Column(String(255))
    datFullPath = Column(String(255))
    magnification = Column(Integer, info="Unit: X")
    binning = Column(
        Integer,
        server_default=FetchedValue(),
        info="1 or 2. Number of pixels to process as 1. (Use mean value.)",
    )
    particleDiameter = Column(Float, info="Unit: nm")
    boxSize_CTF = Column(Float, info="Unit: pixels")
    minResolution = Column(Float, info="Unit: A")
    minDefocus = Column(Float, info="Unit: A")
    maxDefocus = Column(Float, info="Unit: A")
    defocusStepSize = Column(Float, info="Unit: A")
    amountAstigmatism = Column(Float, info="Unit: A")
    extractSize = Column(Float, info="Unit: pixels")
    bgRadius = Column(Float, info="Unit: nm")
    voltage = Column(Float, info="Unit: kV")
    objAperture = Column(Float, info="Unit: um")
    c1aperture = Column(Float, info="Unit: um")
    c2aperture = Column(Float, info="Unit: um")
    c3aperture = Column(Float, info="Unit: um")
    c1lens = Column(Float, info="Unit: %")
    c2lens = Column(Float, info="Unit: %")
    c3lens = Column(Float, info="Unit: %")

    BLSubSample = relationship(
        "BLSubSample",
        primaryjoin="DataCollection.blSubSampleId == BLSubSample.blSubSampleId",
        backref="data_collections",
    )
    DataCollectionGroup = relationship(
        "DataCollectionGroup",
        primaryjoin="DataCollection.dataCollectionGroupId == DataCollectionGroup.dataCollectionGroupId",
        backref="data_collections",
    )
    Detector = relationship(
        "Detector",
        primaryjoin="DataCollection.detectorId == Detector.detectorId",
        backref="data_collections",
    )
    ScreeningStrategySubWedge = relationship(
        "ScreeningStrategySubWedge",
        primaryjoin="DataCollection.strategySubWedgeOrigId == ScreeningStrategySubWedge.screeningStrategySubWedgeId",
        backref="data_collections",
    )


class DataCollectionFileAttachment(Base):
    __tablename__ = "DataCollectionFileAttachment"

    dataCollectionFileAttachmentId = Column(Integer, primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    fileFullPath = Column(String(255), nullable=False)
    fileType = Column(
        ENUM("snapshot", "log", "xy", "recip"),
        info="snapshot: image file, usually of the sample. \\r\\nlog: a text file with logging info. \\r\\nxy: x and y data in text format. \\r\\nrecip: a compressed csv file with reciprocal space coordinates.",
    )
    createTime = Column(DateTime, nullable=False, server_default=FetchedValue())

    DataCollection = relationship(
        "DataCollection",
        primaryjoin="DataCollectionFileAttachment.dataCollectionId == DataCollection.dataCollectionId",
        backref="data_collection_file_attachments",
    )


class DataCollectionGroup(Base):
    __tablename__ = "DataCollectionGroup"

    dataCollectionGroupId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="references BLSample table",
    )
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        info="references Session table",
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    experimentType = Column(
        ENUM(
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
    startTime = Column(DateTime, info="Start time of the dataCollectionGroup")
    endTime = Column(DateTime, info="end time of the dataCollectionGroup")
    crystalClass = Column(String(20), info="Crystal Class for industrials users")
    comments = Column(String(1024), info="comments")
    detectorMode = Column(String(255), info="Detector mode")
    actualSampleBarcode = Column(String(45), info="Actual sample barcode")
    actualSampleSlotInContainer = Column(
        Integer, info="Actual sample slot number in container"
    )
    actualContainerBarcode = Column(String(45), info="Actual container barcode")
    actualContainerSlotInSC = Column(
        Integer, info="Actual container slot number in sample changer"
    )
    xtalSnapshotFullPath = Column(String(255))

    BLSample = relationship(
        "BLSample",
        primaryjoin="DataCollectionGroup.blSampleId == BLSample.blSampleId",
        backref="data_collection_groups",
    )
    BLSession = relationship(
        "BLSession",
        primaryjoin="DataCollectionGroup.sessionId == BLSession.sessionId",
        backref="data_collection_groups",
    )
    Workflow = relationship(
        "Workflow",
        primaryjoin="DataCollectionGroup.workflowId == Workflow.workflowId",
        backref="data_collection_groups",
    )
    Project = relationship(
        "Project", secondary="Project_has_DCGroup", backref="data_collection_groups"
    )


class DataCollectionPlanGroup(Base):
    __tablename__ = "DataCollectionPlanGroup"

    dataCollectionPlanGroupId = Column(Integer, primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )

    BLSample = relationship(
        "BLSample",
        primaryjoin="DataCollectionPlanGroup.blSampleId == BLSample.blSampleId",
        backref="data_collection_plan_groups",
    )
    BLSession = relationship(
        "BLSession",
        primaryjoin="DataCollectionPlanGroup.sessionId == BLSession.sessionId",
        backref="data_collection_plan_groups",
    )


class DataReductionStatus(Base):
    __tablename__ = "DataReductionStatus"

    dataReductionStatusId = Column(Integer, primary_key=True)
    dataCollectionId = Column(Integer, nullable=False)
    status = Column(String(15))
    filename = Column(String(255))
    message = Column(String(255))


class DatamatrixInSampleChanger(Base):
    __tablename__ = "DatamatrixInSampleChanger"

    datamatrixInSampleChangerId = Column(Integer, primary_key=True)
    proposalId = Column(
        Integer, nullable=False, index=True, server_default=FetchedValue()
    )
    beamLineName = Column(String(45))
    datamatrixCode = Column(String(45))
    locationInContainer = Column(Integer)
    containerLocationInSC = Column(Integer)
    containerDatamatrixCode = Column(String(45))
    bltimeStamp = Column(DateTime)


class Detector(Base):
    __tablename__ = "Detector"
    __table_args__ = (
        Index(
            "Detector_FKIndex1",
            "detectorType",
            "detectorManufacturer",
            "detectorModel",
            "detectorPixelSizeHorizontal",
            "detectorPixelSizeVertical",
        ),
    )

    detectorId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    detectorType = Column(String(255))
    detectorManufacturer = Column(String(255))
    detectorModel = Column(String(255))
    detectorPixelSizeHorizontal = Column(Float)
    detectorPixelSizeVertical = Column(Float)
    detectorSerialNumber = Column(String(30), unique=True)
    detectorDistanceMin = Column(Float(asdecimal=True))
    detectorDistanceMax = Column(Float(asdecimal=True))
    trustedPixelValueRangeLower = Column(Float(asdecimal=True))
    trustedPixelValueRangeUpper = Column(Float(asdecimal=True))
    sensorThickness = Column(Float)
    overload = Column(Float)
    XGeoCorr = Column(String(255))
    YGeoCorr = Column(String(255))
    detectorMode = Column(String(255))
    detectorMaxResolution = Column(Float)
    detectorMinResolution = Column(Float)
    CS = Column(Float, info="Unit: mm")
    density = Column(Float)
    composition = Column(String(16))
    localName = Column(String(40), info="Colloquial name for the detector")


class Dewar(Base):
    __tablename__ = "Dewar"

    dewarId = Column(Integer, primary_key=True)
    shippingId = Column(
        ForeignKey("Shipping.shippingId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    code = Column(String(45), index=True)
    comments = Column(String)
    storageLocation = Column(String(45))
    dewarStatus = Column(String(45), index=True)
    bltimeStamp = Column(DateTime, server_default=FetchedValue())
    isStorageDewar = Column(Integer, server_default=FetchedValue())
    barCode = Column(String(45), unique=True)
    firstExperimentId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    customsValue = Column(Integer)
    transportValue = Column(Integer)
    trackingNumberToSynchrotron = Column(String(30))
    trackingNumberFromSynchrotron = Column(String(30))
    facilityCode = Column(String(20), info="Unique barcode assigned to each dewar")
    type = Column(
        ENUM("Dewar", "Toolbox"), nullable=False, server_default=FetchedValue()
    )
    isReimbursed = Column(
        Integer,
        server_default=FetchedValue(),
        info="set this dewar as reimbursed by the user office",
    )

    BLSession = relationship(
        "BLSession",
        primaryjoin="Dewar.firstExperimentId == BLSession.sessionId",
        backref="dewars",
    )
    Shipping = relationship(
        "Shipping",
        primaryjoin="Dewar.shippingId == Shipping.shippingId",
        backref="dewars",
    )


class DewarLocation(Base):
    __tablename__ = "DewarLocation"

    eventId = Column(Integer, primary_key=True)
    dewarNumber = Column(String(128), nullable=False, info="Dewar number")
    userId = Column(String(128), info="User who locates the dewar")
    dateTime = Column(DateTime, info="Date and time of locatization")
    locationName = Column(String(128), info="Location of the dewar")
    courierName = Column(String(128), info="Carrier name who's shipping back the dewar")
    courierTrackingNumber = Column(String(128), info="Tracking number of the shippment")


class DewarLocationList(Base):
    __tablename__ = "DewarLocationList"

    locationId = Column(Integer, primary_key=True)
    locationName = Column(
        String(128), nullable=False, server_default=FetchedValue(), info="Location"
    )


class DewarRegistry(Base):
    __tablename__ = "DewarRegistry"

    dewarRegistryId = Column(Integer, primary_key=True)
    facilityCode = Column(String(20), nullable=False, unique=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", onupdate="CASCADE"), index=True
    )
    labContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="SET NULL", onupdate="CASCADE"),
        index=True,
    )
    purchaseDate = Column(DateTime)
    bltimestamp = Column(DateTime, nullable=False, server_default=FetchedValue())

    LabContact = relationship(
        "LabContact",
        primaryjoin="DewarRegistry.labContactId == LabContact.labContactId",
        backref="dewar_registries",
    )
    Proposal = relationship(
        "Proposal",
        primaryjoin="DewarRegistry.proposalId == Proposal.proposalId",
        backref="dewar_registries",
    )


class DewarRegistryHasProposal(Base):
    __tablename__ = "DewarRegistry_has_Proposal"
    __table_args__ = (Index("dewarRegistryId", "dewarRegistryId", "proposalId"),)

    dewarRegistryHasProposalId = Column(Integer, primary_key=True)
    dewarRegistryId = Column(
        ForeignKey("DewarRegistry.dewarRegistryId", ondelete="CASCADE")
    )
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"), index=True
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE"),
        index=True,
        info="Person registering the dewar",
    )
    recordTimestamp = Column(DateTime, server_default=FetchedValue())
    labContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="Owner of the dewar",
    )

    DewarRegistry = relationship(
        "DewarRegistry",
        primaryjoin="DewarRegistryHasProposal.dewarRegistryId == DewarRegistry.dewarRegistryId",
        backref="dewar_registry_has_proposals",
    )
    LabContact = relationship(
        "LabContact",
        primaryjoin="DewarRegistryHasProposal.labContactId == LabContact.labContactId",
        backref="dewar_registry_has_proposals",
    )
    Person = relationship(
        "Person",
        primaryjoin="DewarRegistryHasProposal.personId == Person.personId",
        backref="dewar_registry_has_proposals",
    )
    Proposal = relationship(
        "Proposal",
        primaryjoin="DewarRegistryHasProposal.proposalId == Proposal.proposalId",
        backref="dewar_registry_has_proposals",
    )


class DewarTransportHistory(Base):
    __tablename__ = "DewarTransportHistory"

    DewarTransportHistoryId = Column(Integer, primary_key=True)
    dewarId = Column(
        ForeignKey("Dewar.dewarId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    dewarStatus = Column(String(45), nullable=False)
    storageLocation = Column(String(45))
    arrivalDate = Column(DateTime)

    Dewar = relationship(
        "Dewar",
        primaryjoin="DewarTransportHistory.dewarId == Dewar.dewarId",
        backref="dewar_transport_histories",
    )


class DiffractionPlan(Base):
    __tablename__ = "DiffractionPlan"

    diffractionPlanId = Column(Integer, primary_key=True)
    xmlDocumentId = Column(Integer)
    experimentKind = Column(
        ENUM(
            "Default",
            "MXPressE",
            "MXPressF",
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
    observedResolution = Column(Float)
    minimalResolution = Column(Float)
    exposureTime = Column(Float)
    oscillationRange = Column(Float)
    maximalResolution = Column(Float)
    screeningResolution = Column(Float)
    radiationSensitivity = Column(Float)
    anomalousScatterer = Column(String(255))
    preferredBeamSizeX = Column(Float)
    preferredBeamSizeY = Column(Float)
    preferredBeamDiameter = Column(Float)
    comments = Column(String(1024))
    aimedCompleteness = Column(Float(asdecimal=True))
    aimedIOverSigmaAtHighestRes = Column(Float(asdecimal=True))
    aimedMultiplicity = Column(Float(asdecimal=True))
    aimedResolution = Column(Float(asdecimal=True))
    anomalousData = Column(Integer, server_default=FetchedValue())
    complexity = Column(String(45))
    estimateRadiationDamage = Column(Integer, server_default=FetchedValue())
    forcedSpaceGroup = Column(String(45))
    requiredCompleteness = Column(Float(asdecimal=True))
    requiredMultiplicity = Column(Float(asdecimal=True))
    requiredResolution = Column(Float(asdecimal=True))
    strategyOption = Column(String(45))
    kappaStrategyOption = Column(String(45))
    numberOfPositions = Column(Integer)
    minDimAccrossSpindleAxis = Column(
        Float(asdecimal=True), info="minimum dimension accross the spindle axis"
    )
    maxDimAccrossSpindleAxis = Column(
        Float(asdecimal=True), info="maximum dimension accross the spindle axis"
    )
    radiationSensitivityBeta = Column(Float(asdecimal=True))
    radiationSensitivityGamma = Column(Float(asdecimal=True))
    minOscWidth = Column(Float)
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )
    diffractionPlanUUID = Column(String(1000))
    dataCollectionPlanGroupId = Column(Integer)
    detectorId = Column(Integer)
    distance = Column(Float(asdecimal=True))
    orientation = Column(Float(asdecimal=True))
    monoBandwidth = Column(Float(asdecimal=True))
    monochromator = Column(String(8), info="DMM or DCM")
    energy = Column(Float, info="eV")
    transmission = Column(Float, info="Decimal fraction in range [0,1]")
    boxSizeX = Column(Float, info="microns")
    boxSizeY = Column(Float, info="microns")
    kappaStart = Column(Float, info="degrees")
    axisStart = Column(Float, info="degrees")
    axisRange = Column(Float, info="degrees")
    numberOfImages = Column(Integer, info="The number of images requested")
    presetForProposalId = Column(
        Integer,
        info="Indicates this plan is available to all sessions on given proposal",
    )
    beamLineName = Column(
        String(45),
        info="Indicates this plan is available to all sessions on given beamline",
    )
    userPath = Column(
        String(100),
        info='User-specified relative "root" path inside the session directory to be used for holding collected data',
    )


class DiffractionPlanHasDetector(Base):
    __tablename__ = "DiffractionPlan_has_Detector"

    diffractionPlanId = Column(
        ForeignKey("DiffractionPlan.diffractionPlanId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    detectorId = Column(
        ForeignKey("Detector.detectorId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    exposureTime = Column(Float(asdecimal=True))
    distance = Column(Float(asdecimal=True))
    orientation = Column(Float(asdecimal=True))

    Detector = relationship(
        "Detector",
        primaryjoin="DiffractionPlanHasDetector.detectorId == Detector.detectorId",
        backref="diffraction_plan_has_detectors",
    )
    DiffractionPlan = relationship(
        "DiffractionPlan",
        primaryjoin="DiffractionPlanHasDetector.diffractionPlanId == DiffractionPlan.diffractionPlanId",
        backref="diffraction_plan_has_detectors",
    )


class EMMicroscope(Base):
    __tablename__ = "EMMicroscope"

    emMicroscopeId = Column(Integer, primary_key=True)
    instrumentName = Column(String(100), nullable=False)
    voltage = Column(Float)
    CS = Column(Float, info="Unit: mm")
    detectorPixelSize = Column(Float)
    C2aperture = Column(Float)
    ObjAperture = Column(Float)
    C2lens = Column(Float)


class EnergyScan(Base):
    __tablename__ = "EnergyScan"

    energyScanId = Column(Integer, primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"), index=True
    )
    fluorescenceDetector = Column(String(255))
    scanFileFullPath = Column(String(255))
    choochFileFullPath = Column(String(255))
    jpegChoochFileFullPath = Column(String(255))
    element = Column(String(45))
    startEnergy = Column(Float)
    endEnergy = Column(Float)
    transmissionFactor = Column(Float)
    exposureTime = Column(Float)
    axisPosition = Column(Float)
    synchrotronCurrent = Column(Float)
    temperature = Column(Float)
    peakEnergy = Column(Float)
    peakFPrime = Column(Float)
    peakFDoublePrime = Column(Float)
    inflectionEnergy = Column(Float)
    inflectionFPrime = Column(Float)
    inflectionFDoublePrime = Column(Float)
    xrayDose = Column(Float)
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    edgeEnergy = Column(String(255))
    filename = Column(String(255))
    beamSizeVertical = Column(Float)
    beamSizeHorizontal = Column(Float)
    crystalClass = Column(String(20))
    comments = Column(String(1024))
    flux = Column(Float(asdecimal=True), info="flux measured before the energyScan")
    flux_end = Column(Float(asdecimal=True), info="flux measured after the energyScan")
    workingDirectory = Column(String(45))
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId", ondelete="CASCADE"), index=True
    )
    remoteEnergy = Column(Float)
    remoteFPrime = Column(Float)
    remoteFDoublePrime = Column(Float)

    BLSample = relationship(
        "BLSample",
        primaryjoin="EnergyScan.blSampleId == BLSample.blSampleId",
        backref="energy_scans",
    )
    BLSubSample = relationship(
        "BLSubSample",
        primaryjoin="EnergyScan.blSubSampleId == BLSubSample.blSubSampleId",
        backref="energy_scans",
    )
    BLSession = relationship(
        "BLSession",
        primaryjoin="EnergyScan.sessionId == BLSession.sessionId",
        backref="energy_scans",
    )
    Project = relationship(
        "Project", secondary="Project_has_EnergyScan", backref="energy_scans"
    )


class Experiment(Base):
    __tablename__ = "Experiment"

    experimentId = Column(Integer, primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"), index=True
    )
    proposalId = Column(Integer, nullable=False)
    name = Column(String(255))
    creationDate = Column(DateTime)
    experimentType = Column(String(128))
    sourceFilePath = Column(String(256))
    dataAcquisitionFilePath = Column(
        String(256),
        info="The file path pointing to the data acquisition. Eventually it may be a compressed file with all the files or just the folder",
    )
    status = Column(String(45))
    comments = Column(String(512))

    BLSession = relationship(
        "BLSession",
        primaryjoin="Experiment.sessionId == BLSession.sessionId",
        backref="experiments",
    )


class ExperimentKindDetails(Base):
    __tablename__ = "ExperimentKindDetails"

    experimentKindId = Column(Integer, primary_key=True)
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    exposureIndex = Column(Integer)
    dataCollectionType = Column(String(45))
    dataCollectionKind = Column(String(45))
    wedgeValue = Column(Float)

    DiffractionPlan = relationship(
        "DiffractionPlan",
        primaryjoin="ExperimentKindDetails.diffractionPlanId == DiffractionPlan.diffractionPlanId",
        backref="experiment_kind_detailss",
    )


class FitStructureToExperimentalData(Base):
    __tablename__ = "FitStructureToExperimentalData"

    fitStructureToExperimentalDataId = Column(Integer, primary_key=True)
    structureId = Column(
        ForeignKey("Structure.structureId", ondelete="CASCADE"), index=True
    )
    subtractionId = Column(
        ForeignKey("Subtraction.subtractionId", ondelete="CASCADE"), index=True
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE"), index=True
    )
    fitFilePath = Column(String(255))
    logFilePath = Column(String(255))
    outputFilePath = Column(String(255))
    creationDate = Column(DateTime)
    comments = Column(String(2048))

    Structure = relationship(
        "Structure",
        primaryjoin="FitStructureToExperimentalData.structureId == Structure.structureId",
        backref="fit_structure_to_experimental_datas",
    )
    Subtraction = relationship(
        "Subtraction",
        primaryjoin="FitStructureToExperimentalData.subtractionId == Subtraction.subtractionId",
        backref="fit_structure_to_experimental_datas",
    )
    Workflow = relationship(
        "Workflow",
        primaryjoin="FitStructureToExperimentalData.workflowId == Workflow.workflowId",
        backref="fit_structure_to_experimental_datas",
    )


class Frame(Base):
    __tablename__ = "Frame"

    frameId = Column(Integer, primary_key=True)
    filePath = Column(String(255), index=True)
    comments = Column(String(45))
    creationDate = Column(DateTime, nullable=False, server_default=FetchedValue())
    frameSetId = Column(Integer)


class FrameList(Base):
    __tablename__ = "FrameList"

    frameListId = Column(Integer, primary_key=True)
    comments = Column(Integer)


class FrameSet(Base):
    __tablename__ = "FrameSet"

    frameSetId = Column(Integer, primary_key=True)
    runId = Column(
        ForeignKey("Run.runId", ondelete="CASCADE"), nullable=False, index=True
    )
    frameListId = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"), index=True
    )
    detectorId = Column(Integer)
    detectorDistance = Column(String(45))
    filePath = Column(String(255))
    internalPath = Column(String(255))

    FrameList = relationship(
        "FrameList",
        primaryjoin="FrameSet.frameListId == FrameList.frameListId",
        backref="frame_sets",
    )
    Run = relationship(
        "Run", primaryjoin="FrameSet.runId == Run.runId", backref="frame_sets"
    )


class FrameToList(Base):
    __tablename__ = "FrameToList"

    frameToListId = Column(Integer, primary_key=True)
    frameListId = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    frameId = Column(
        ForeignKey("Frame.frameId", ondelete="CASCADE"), nullable=False, index=True
    )

    Frame = relationship(
        "Frame",
        primaryjoin="FrameToList.frameId == Frame.frameId",
        backref="frame_to_lists",
    )
    FrameList = relationship(
        "FrameList",
        primaryjoin="FrameToList.frameListId == FrameList.frameListId",
        backref="frame_to_lists",
    )


class GeometryClassname(Base):
    __tablename__ = "GeometryClassname"

    geometryClassnameId = Column(Integer, primary_key=True)
    geometryClassname = Column(String(45))
    geometryOrder = Column(Integer, nullable=False)


class GridInfo(Base):
    __tablename__ = "GridInfo"

    gridInfoId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    workflowMeshId = Column(
        ForeignKey(
            "WorkflowMesh.workflowMeshId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    xOffset = Column(Float(asdecimal=True))
    yOffset = Column(Float(asdecimal=True))
    dx_mm = Column(Float(asdecimal=True))
    dy_mm = Column(Float(asdecimal=True))
    steps_x = Column(Float(asdecimal=True))
    steps_y = Column(Float(asdecimal=True))
    meshAngle = Column(Float(asdecimal=True))
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )
    orientation = Column(ENUM("vertical", "horizontal"), server_default=FetchedValue())
    dataCollectionGroupId = Column(
        ForeignKey("DataCollectionGroup.dataCollectionGroupId", ondelete="CASCADE"),
        index=True,
    )
    pixelspermicronX = Column(Float)
    pixelspermicronY = Column(Float)
    snapshot_offsetxpixel = Column(Float)
    snapshot_offsetypixel = Column(Float)

    DataCollectionGroup = relationship(
        "DataCollectionGroup",
        primaryjoin="GridInfo.dataCollectionGroupId == DataCollectionGroup.dataCollectionGroupId",
        backref="grid_infos",
    )
    WorkflowMesh = relationship(
        "WorkflowMesh",
        primaryjoin="GridInfo.workflowMeshId == WorkflowMesh.workflowMeshId",
        backref="grid_infos",
    )


class Image(Base):
    __tablename__ = "Image"
    __table_args__ = (Index("Image_Index3", "fileLocation", "fileName"),)

    imageId = Column(Integer, primary_key=True)
    dataCollectionId = Column(
        ForeignKey("DataCollection.dataCollectionId", ondelete="CASCADE"),
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    motorPositionId = Column(Integer, index=True)
    imageNumber = Column(Integer, index=True)
    fileName = Column(String(255))
    fileLocation = Column(String(255))
    measuredIntensity = Column(Float)
    jpegFileFullPath = Column(String(255))
    jpegThumbnailFileFullPath = Column(String(255))
    temperature = Column(Float)
    cumulativeIntensity = Column(Float)
    synchrotronCurrent = Column(Float)
    comments = Column(String(1024))
    machineMessage = Column(String(1024))
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )

    DataCollection = relationship(
        "DataCollection",
        primaryjoin="Image.dataCollectionId == DataCollection.dataCollectionId",
        backref="datacollection_images",
    )
    DataCollection1 = relationship(
        "DataCollection",
        primaryjoin="Image.dataCollectionId == DataCollection.dataCollectionId",
        backref="datacollection_images_0",
    )


class ImageQualityIndicators(Base):
    __tablename__ = "ImageQualityIndicators"

    imageQualityIndicatorsId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    imageId = Column(Integer, index=True)
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        info="Foreign key to the AutoProcProgram table",
    )
    spotTotal = Column(Integer, info="Total number of spots")
    inResTotal = Column(Integer, info="Total number of spots in resolution range")
    goodBraggCandidates = Column(
        Integer, info="Total number of Bragg diffraction spots"
    )
    iceRings = Column(Integer, info="Number of ice rings identified")
    method1Res = Column(Float, info="Resolution estimate 1 (see publication)")
    method2Res = Column(Float, info="Resolution estimate 2 (see publication)")
    maxUnitCell = Column(
        Float, info="Estimation of the largest possible unit cell edge"
    )
    pctSaturationTop50Peaks = Column(
        Float, info="The fraction of the dynamic range being used"
    )
    inResolutionOvrlSpots = Column(Integer, info="Number of spots overloaded")
    binPopCutOffMethod2Res = Column(
        Float, info="Cut off used in resolution limit calculation"
    )
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")
    totalIntegratedSignal = Column(Float(asdecimal=True))
    dozor_score = Column(Float(asdecimal=True), info="dozor_score")
    dataCollectionId = Column(Integer)
    imageNumber = Column(Integer)

    AutoProcProgram = relationship(
        "AutoProcProgram",
        primaryjoin="ImageQualityIndicators.autoProcProgramId == AutoProcProgram.autoProcProgramId",
        backref="image_quality_indicatorss",
    )


class Imager(Base):
    __tablename__ = "Imager"

    imagerId = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    temperature = Column(Float)
    serial = Column(String(45))
    capacity = Column(SmallInteger)


class InitialModel(Base):
    __tablename__ = "InitialModel"

    initialModelId = Column(Integer, primary_key=True)
    resolution = Column(Float, info="Unit: Angstroms")
    numberOfParticles = Column(Integer)


class InputParameterWorkflow(Base):
    __tablename__ = "InputParameterWorkflow"

    inputParameterId = Column(Integer, primary_key=True)
    workflowId = Column(Integer, nullable=False)
    parameterType = Column(String(255))
    name = Column(String(255))
    value = Column(String(255))
    comments = Column(String(2048))


class InspectionType(Base):
    __tablename__ = "InspectionType"

    inspectionTypeId = Column(Integer, primary_key=True)
    name = Column(String(45))


class Instruction(Base):
    __tablename__ = "Instruction"

    instructionId = Column(Integer, primary_key=True)
    instructionSetId = Column(
        ForeignKey("InstructionSet.instructionSetId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    order = Column(Integer, nullable=False)
    comments = Column(String(255))

    InstructionSet = relationship(
        "InstructionSet",
        primaryjoin="Instruction.instructionSetId == InstructionSet.instructionSetId",
        backref="instructions",
    )


class InstructionSet(Base):
    __tablename__ = "InstructionSet"

    instructionSetId = Column(Integer, primary_key=True)
    type = Column(String(50))


class IspybAutoProcAttachment(Base):
    __tablename__ = "IspybAutoProcAttachment"

    autoProcAttachmentId = Column(Integer, primary_key=True)
    fileName = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    step = Column(
        ENUM("XDS", "XSCALE", "SCALA", "SCALEPACK", "TRUNCATE", "DIMPLE"),
        server_default=FetchedValue(),
        info="step where the file is generated",
    )
    fileCategory = Column(
        ENUM("input", "output", "log", "correction"), server_default=FetchedValue()
    )
    hasGraph = Column(Integer, nullable=False, server_default=FetchedValue())


class IspybCrystalClass(Base):
    __tablename__ = "IspybCrystalClass"

    crystalClassId = Column(Integer, primary_key=True)
    crystalClass_code = Column(String(20), nullable=False)
    crystalClass_name = Column(String(255), nullable=False)


class IspybReference(Base):
    __tablename__ = "IspybReference"

    referenceId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    referenceName = Column(String(255), info="reference name")
    referenceUrl = Column(String(1024), info="url of the reference")
    referenceBibtext = Column(LargeBinary, info="bibtext value of the reference")
    beamline = Column(
        ENUM(
            "All",
            "ID14-4",
            "ID23-1",
            "ID23-2",
            "ID29",
            "ID30A-1",
            "ID30A-2",
            "XRF",
            "AllXRF",
            "Mesh",
        ),
        info="beamline involved",
    )


class LabContact(Base):
    __tablename__ = "LabContact"
    __table_args__ = (
        Index("personAndProposal", "personId", "proposalId"),
        Index("cardNameAndProposal", "cardName", "proposalId"),
    )

    labContactId = Column(Integer, primary_key=True)
    personId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), nullable=False)
    cardName = Column(String(40), nullable=False)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    defaultCourrierCompany = Column(String(45))
    courierAccount = Column(String(45))
    billingReference = Column(String(45))
    dewarAvgCustomsValue = Column(
        Integer, nullable=False, server_default=FetchedValue()
    )
    dewarAvgTransportValue = Column(
        Integer, nullable=False, server_default=FetchedValue()
    )
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )

    Person = relationship(
        "Person",
        primaryjoin="LabContact.personId == Person.personId",
        backref="lab_contacts",
    )
    Proposal = relationship(
        "Proposal",
        primaryjoin="LabContact.proposalId == Proposal.proposalId",
        backref="lab_contacts",
    )


class Laboratory(Base):
    __tablename__ = "Laboratory"

    laboratoryId = Column(Integer, primary_key=True)
    laboratoryUUID = Column(String(45))
    name = Column(String(45))
    address = Column(String(255))
    city = Column(String(45))
    country = Column(String(45))
    url = Column(String(255))
    organization = Column(String(45))
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )
    laboratoryExtPk = Column(Integer)


class Log4Stat(Base):
    __tablename__ = "Log4Stat"

    id = Column(Integer, primary_key=True)
    priority = Column(String(15))
    timestamp = Column(DateTime)
    msg = Column(String(255))
    detail = Column(String(255))
    value = Column(String(255))


class Login(Base):
    __tablename__ = "Login"

    loginId = Column(Integer, primary_key=True)
    token = Column(String(45), nullable=False, index=True)
    username = Column(String(45), nullable=False)
    roles = Column(String(1024), nullable=False)
    siteId = Column(String(45))
    authorized = Column(String(1024))
    expirationTime = Column(DateTime, nullable=False)


class MXMRRun(Base):
    __tablename__ = "MXMRRun"

    mxMRRunId = Column(Integer, primary_key=True)
    autoProcScalingId = Column(
        ForeignKey("AutoProcScaling.autoProcScalingId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    success = Column(
        Integer,
        server_default=FetchedValue(),
        info="Indicates whether the program completed. 1 for success, 0 for failure.",
    )
    message = Column(
        String(255), info="A short summary of the findings, success or failure."
    )
    pipeline = Column(String(50))
    inputCoordFile = Column(String(255))
    outputCoordFile = Column(String(255))
    inputMTZFile = Column(String(255))
    outputMTZFile = Column(String(255))
    runDirectory = Column(String(255))
    logFile = Column(String(255))
    commandLine = Column(String(255))
    rValueStart = Column(Float)
    rValueEnd = Column(Float)
    rFreeValueStart = Column(Float)
    rFreeValueEnd = Column(Float)
    starttime = Column(DateTime)
    endtime = Column(DateTime)

    AutoProcScaling = relationship(
        "AutoProcScaling",
        primaryjoin="MXMRRun.autoProcScalingId == AutoProcScaling.autoProcScalingId",
        backref="mxmr_runs",
    )


class MXMRRunBlob(Base):
    __tablename__ = "MXMRRunBlob"

    mxMRRunBlobId = Column(Integer, primary_key=True)
    mxMRRunId = Column(
        ForeignKey("MXMRRun.mxMRRunId", ondelete="CASCADE"), nullable=False, index=True
    )
    view1 = Column(String(255))
    view2 = Column(String(255))
    view3 = Column(String(255))

    MXMRRun = relationship(
        "MXMRRun",
        primaryjoin="MXMRRunBlob.mxMRRunId == MXMRRun.mxMRRunId",
        backref="mxmr_run_blobs",
    )


class Macromolecule(Base):
    __tablename__ = "Macromolecule"

    macromoleculeId = Column(Integer, primary_key=True)
    proposalId = Column(Integer)
    safetyLevelId = Column(
        ForeignKey("SafetyLevel.safetyLevelId", ondelete="CASCADE"), index=True
    )
    name = Column(String(45, "utf8mb4_unicode_ci"))
    acronym = Column(String(45, "utf8mb4_unicode_ci"))
    extintionCoefficient = Column(String(45))
    molecularMass = Column(String(45))
    sequence = Column(String(1000))
    contactsDescriptionFilePath = Column(String(255))
    symmetry = Column(String(45))
    comments = Column(String(1024, "utf8mb4_unicode_ci"))
    refractiveIndex = Column(String(45))
    solventViscosity = Column(String(45))
    creationDate = Column(DateTime)
    electronDensity = Column(Float(7))

    SafetyLevel = relationship(
        "SafetyLevel",
        primaryjoin="Macromolecule.safetyLevelId == SafetyLevel.safetyLevelId",
        backref="macromolecules",
    )


class MacromoleculeRegion(Base):
    __tablename__ = "MacromoleculeRegion"

    macromoleculeRegionId = Column(Integer, primary_key=True)
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    regionType = Column(String(45))
    id = Column(String(45))
    count = Column(String(45))
    sequence = Column(String(45))

    Macromolecule = relationship(
        "Macromolecule",
        primaryjoin="MacromoleculeRegion.macromoleculeId == Macromolecule.macromoleculeId",
        backref="macromolecule_regions",
    )


class Measurement(Base):
    __tablename__ = "Measurement"

    measurementId = Column(Integer, primary_key=True)
    specimenId = Column(
        ForeignKey("Specimen.specimenId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    runId = Column(ForeignKey("Run.runId", ondelete="CASCADE"), index=True)
    code = Column(String(100))
    imageDirectory = Column(String(512))
    priorityLevelId = Column(Integer)
    exposureTemperature = Column(String(45))
    viscosity = Column(String(45))
    flow = Column(Integer)
    extraFlowTime = Column(String(45))
    volumeToLoad = Column(String(45))
    waitTime = Column(String(45))
    transmission = Column(String(45))
    comments = Column(String(512))
    pathToH5 = Column(String(512))

    Run = relationship(
        "Run", primaryjoin="Measurement.runId == Run.runId", backref="measurements"
    )
    Specimen = relationship(
        "Specimen",
        primaryjoin="Measurement.specimenId == Specimen.specimenId",
        backref="measurements",
    )


class MeasurementToDataCollection(Base):
    __tablename__ = "MeasurementToDataCollection"

    measurementToDataCollectionId = Column(Integer, primary_key=True)
    dataCollectionId = Column(
        ForeignKey("SaxsDataCollection.dataCollectionId", ondelete="CASCADE"),
        index=True,
    )
    measurementId = Column(
        ForeignKey("Measurement.measurementId", ondelete="CASCADE"), index=True
    )
    dataCollectionOrder = Column(Integer)

    SaxsDataCollection = relationship(
        "SaxsDataCollection",
        primaryjoin="MeasurementToDataCollection.dataCollectionId == SaxsDataCollection.dataCollectionId",
        backref="measurement_to_data_collections",
    )
    Measurement = relationship(
        "Measurement",
        primaryjoin="MeasurementToDataCollection.measurementId == Measurement.measurementId",
        backref="measurement_to_data_collections",
    )


class MeasurementUnit(Base):
    __tablename__ = "MeasurementUnit"

    measurementUnitId = Column(Integer, primary_key=True)
    name = Column(String(45))
    unitType = Column(String(45))


class Merge(Base):
    __tablename__ = "Merge"

    mergeId = Column(Integer, primary_key=True)
    measurementId = Column(
        ForeignKey("Measurement.measurementId", ondelete="CASCADE"), index=True
    )
    frameListId = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"), index=True
    )
    discardedFrameNameList = Column(String(1024))
    averageFilePath = Column(String(255))
    framesCount = Column(String(45))
    framesMerge = Column(String(45))
    creationDate = Column(DateTime)

    FrameList = relationship(
        "FrameList",
        primaryjoin="Merge.frameListId == FrameList.frameListId",
        backref="merges",
    )
    Measurement = relationship(
        "Measurement",
        primaryjoin="Merge.measurementId == Measurement.measurementId",
        backref="merges",
    )


class MixtureToStructure(Base):
    __tablename__ = "MixtureToStructure"

    fitToStructureId = Column(Integer, primary_key=True)
    structureId = Column(
        ForeignKey("Structure.structureId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    mixtureId = Column(
        ForeignKey(
            "FitStructureToExperimentalData.fitStructureToExperimentalDataId",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    volumeFraction = Column(String(45))
    creationDate = Column(DateTime)

    FitStructureToExperimentalData = relationship(
        "FitStructureToExperimentalData",
        primaryjoin="MixtureToStructure.mixtureId == FitStructureToExperimentalData.fitStructureToExperimentalDataId",
        backref="mixture_to_structures",
    )
    Structure = relationship(
        "Structure",
        primaryjoin="MixtureToStructure.structureId == Structure.structureId",
        backref="mixture_to_structures",
    )


class Model(Base):
    __tablename__ = "Model"

    modelId = Column(Integer, primary_key=True)
    name = Column(String(45))
    pdbFile = Column(String(255))
    fitFile = Column(String(255))
    firFile = Column(String(255))
    logFile = Column(String(255))
    rFactor = Column(String(45))
    chiSqrt = Column(String(45))
    volume = Column(String(45))
    rg = Column(String(45))
    dMax = Column(String(45))


class ModelBuilding(Base):
    __tablename__ = "ModelBuilding"

    modelBuildingId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        info="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        info="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="Related spaceGroup",
    )
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")

    PhasingAnalysis = relationship(
        "PhasingAnalysis",
        primaryjoin="ModelBuilding.phasingAnalysisId == PhasingAnalysis.phasingAnalysisId",
        backref="model_buildings",
    )
    PhasingProgramRun = relationship(
        "PhasingProgramRun",
        primaryjoin="ModelBuilding.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId",
        backref="model_buildings",
    )
    SpaceGroup = relationship(
        "SpaceGroup",
        primaryjoin="ModelBuilding.spaceGroupId == SpaceGroup.spaceGroupId",
        backref="model_buildings",
    )


class ModelList(Base):
    __tablename__ = "ModelList"

    modelListId = Column(Integer, primary_key=True)
    nsdFilePath = Column(String(255))
    chi2RgFilePath = Column(String(255))


class ModelToList(Base):
    __tablename__ = "ModelToList"

    modelToListId = Column(Integer, primary_key=True)
    modelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE"), nullable=False, index=True
    )
    modelListId = Column(
        ForeignKey("ModelList.modelListId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    Model = relationship(
        "Model",
        primaryjoin="ModelToList.modelId == Model.modelId",
        backref="model_to_lists",
    )
    ModelList = relationship(
        "ModelList",
        primaryjoin="ModelToList.modelListId == ModelList.modelListId",
        backref="model_to_lists",
    )


class MotionCorrection(Base):
    __tablename__ = "MotionCorrection"

    motionCorrectionId = Column(Integer, primary_key=True)
    movieId = Column(ForeignKey("Movie.movieId", ondelete="CASCADE"), index=True)
    firstFrame = Column(String(45))
    lastFrame = Column(String(45))
    dosePerFrame = Column(String(45))
    doseWeight = Column(String(45))
    totalMotion = Column(String(45))
    averageMotionPerFrame = Column(String(45))
    driftPlotFullPath = Column(String(512))
    micrographFullPath = Column(String(512))
    micrographSnapshotFullPath = Column(String(512))
    correctedDoseMicrographFullPath = Column(String(512))
    patchesUsed = Column(String(45))
    logFileFullPath = Column(String(512))
    createdTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())

    Movie = relationship(
        "Movie",
        primaryjoin="MotionCorrection.movieId == Movie.movieId",
        backref="motion_corrections",
    )


class MotorPosition(Base):
    __tablename__ = "MotorPosition"

    motorPositionId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phiX = Column(Float(asdecimal=True))
    phiY = Column(Float(asdecimal=True))
    phiZ = Column(Float(asdecimal=True))
    sampX = Column(Float(asdecimal=True))
    sampY = Column(Float(asdecimal=True))
    omega = Column(Float(asdecimal=True))
    kappa = Column(Float(asdecimal=True))
    phi = Column(Float(asdecimal=True))
    chi = Column(Float(asdecimal=True))
    gridIndexY = Column(Integer)
    gridIndexZ = Column(Integer)
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )


class Movie(Base):
    __tablename__ = "Movie"

    movieId = Column(Integer, primary_key=True)
    dataCollectionId = Column(
        ForeignKey("DataCollection.dataCollectionId", ondelete="CASCADE"), index=True
    )
    movieNumber = Column(Integer)
    movieFullPath = Column(String(255), index=True)
    positionX = Column(String(45))
    positionY = Column(String(45))
    micrographFullPath = Column(String(255))
    micrographSnapshotFullPath = Column(String(255))
    xmlMetaDataFullPath = Column(String(255))
    dosePerImage = Column(String(45))
    createdTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())

    DataCollection = relationship(
        "DataCollection",
        primaryjoin="Movie.dataCollectionId == DataCollection.dataCollectionId",
        backref="movies",
    )


class PDB(Base):
    __tablename__ = "PDB"

    pdbId = Column(Integer, primary_key=True)
    name = Column(String(255))
    contents = Column(String)
    code = Column(String(4))


class PDBEntry(Base):
    __tablename__ = "PDBEntry"

    pdbEntryId = Column(Integer, primary_key=True)
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId", ondelete="CASCADE"), index=True
    )
    code = Column(String(4))
    cell_a = Column(Float)
    cell_b = Column(Float)
    cell_c = Column(Float)
    cell_alpha = Column(Float)
    cell_beta = Column(Float)
    cell_gamma = Column(Float)
    resolution = Column(Float)
    pdbTitle = Column(String(255))
    pdbAuthors = Column(String(600))
    pdbDate = Column(DateTime)
    pdbBeamlineName = Column(String(50))
    beamlines = Column(String(100))
    distance = Column(Float)
    autoProcCount = Column(SmallInteger)
    dataCollectionCount = Column(SmallInteger)
    beamlineMatch = Column(Integer)
    authorMatch = Column(Integer)

    AutoProcProgram = relationship(
        "AutoProcProgram",
        primaryjoin="PDBEntry.autoProcProgramId == AutoProcProgram.autoProcProgramId",
        backref="pdb_entries",
    )


class PDBEntryHasAutoProcProgram(Base):
    __tablename__ = "PDBEntry_has_AutoProcProgram"

    pdbEntryHasAutoProcId = Column(Integer, primary_key=True)
    pdbEntryId = Column(
        ForeignKey("PDBEntry.pdbEntryId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    distance = Column(Float)

    AutoProcProgram = relationship(
        "AutoProcProgram",
        primaryjoin="PDBEntryHasAutoProcProgram.autoProcProgramId == AutoProcProgram.autoProcProgramId",
        backref="pdb_entry_has_auto_proc_programs",
    )
    PDBEntry = relationship(
        "PDBEntry",
        primaryjoin="PDBEntryHasAutoProcProgram.pdbEntryId == PDBEntry.pdbEntryId",
        backref="pdb_entry_has_auto_proc_programs",
    )


class PHPSession(Base):
    __tablename__ = "PHPSession"

    id = Column(String(50), primary_key=True)
    accessDate = Column(DateTime)
    data = Column(String(4000))


class Particle(Base):
    __tablename__ = "Particle"

    particleId = Column(Integer, primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    x = Column(Float)
    y = Column(Float)

    DataCollection = relationship(
        "DataCollection",
        primaryjoin="Particle.dataCollectionId == DataCollection.dataCollectionId",
        backref="particles",
    )


class ParticleClassification(Base):
    __tablename__ = "ParticleClassification"

    particleClassificationId = Column(Integer, primary_key=True)
    particleClassificationGroupId = Column(
        ForeignKey(
            "ParticleClassificationGroup.particleClassificationGroupId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    classNumber = Column(
        Integer, info="Identified of the class. A unique ID given by Relion"
    )
    classImageFullPath = Column(String(255), info="The PNG of the class")
    particlesPerClass = Column(
        Integer,
        info="Number of particles within the selected class, can then be used together with the total number above to calculate the percentage",
    )
    classDistribution = Column(Float)
    rotationAccuracy = Column(Float)
    translationAccuracy = Column(Float, info="Unit: Angstroms")
    estimatedResolution = Column(Float, info="Unit: Angstroms")
    overallFourierCompleteness = Column(Float)

    ParticleClassificationGroup = relationship(
        "ParticleClassificationGroup",
        primaryjoin="ParticleClassification.particleClassificationGroupId == ParticleClassificationGroup.particleClassificationGroupId",
        backref="particle_classifications",
    )


class ParticleClassificationGroup(Base):
    __tablename__ = "ParticleClassificationGroup"

    particleClassificationGroupId = Column(Integer, primary_key=True)
    particlePickerId = Column(
        ForeignKey(
            "ParticlePicker.particlePickerId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    programId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    type = Column(
        ENUM("2D", "3D"), info="Indicates the type of particle classification"
    )
    batchNumber = Column(Integer, info="Corresponding to batch number")
    numberOfParticlesPerBatch = Column(
        Integer, info="total number of particles per batch (a large integer)"
    )
    numberOfClassesPerBatch = Column(Integer)
    symmetry = Column(String(20))

    ParticlePicker = relationship(
        "ParticlePicker",
        primaryjoin="ParticleClassificationGroup.particlePickerId == ParticlePicker.particlePickerId",
        backref="particle_classification_groups",
    )
    AutoProcProgram = relationship(
        "AutoProcProgram",
        primaryjoin="ParticleClassificationGroup.programId == AutoProcProgram.autoProcProgramId",
        backref="particle_classification_groups",
    )


t_ParticleClassification_has_CryoemInitialModel = Table(
    "ParticleClassification_has_CryoemInitialModel",
    metadata,
    Column(
        "particleClassificationId",
        ForeignKey(
            "ParticleClassification.particleClassificationId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "cryoemInitialModelId",
        ForeignKey(
            "CryoemInitialModel.cryoemInitialModelId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ParticlePicker(Base):
    __tablename__ = "ParticlePicker"

    particlePickerId = Column(Integer, primary_key=True)
    programId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    firstMotionCorrectionId = Column(
        ForeignKey(
            "MotionCorrection.motionCorrectionId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    particlePickingTemplate = Column(String(255), info="Cryolo model")
    particleDiameter = Column(Float, info="Unit: nm")
    numberOfParticles = Column(Integer)
    summaryImageFullPath = Column(
        String(255),
        info="Generated summary micrograph image with highlighted particles",
    )

    MotionCorrection = relationship(
        "MotionCorrection",
        primaryjoin="ParticlePicker.firstMotionCorrectionId == MotionCorrection.motionCorrectionId",
        backref="particle_pickers",
    )
    AutoProcProgram = relationship(
        "AutoProcProgram",
        primaryjoin="ParticlePicker.programId == AutoProcProgram.autoProcProgramId",
        backref="particle_pickers",
    )


class Permission(Base):
    __tablename__ = "Permission"

    permissionId = Column(Integer, primary_key=True)
    type = Column(String(15), nullable=False)
    description = Column(String(100))

    UserGroup = relationship(
        "UserGroup", secondary="UserGroup_has_Permission", backref="permissions"
    )


class Person(Base):
    __tablename__ = "Person"

    personId = Column(Integer, primary_key=True)
    laboratoryId = Column(
        ForeignKey("Laboratory.laboratoryId", ondelete="CASCADE"), index=True
    )
    siteId = Column(Integer, index=True)
    personUUID = Column(String(45))
    familyName = Column(String(100), index=True)
    givenName = Column(String(45))
    title = Column(String(45))
    emailAddress = Column(String(60))
    phoneNumber = Column(String(45, "utf8mb3_unicode_ci"))
    login = Column(String(45), index=True)
    passwd = Column(String(45))
    faxNumber = Column(String(45))
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )
    externalId = Column(BINARY(16))
    cache = Column(Text)

    Laboratory = relationship(
        "Laboratory",
        primaryjoin="Person.laboratoryId == Laboratory.laboratoryId",
        backref="people",
    )
    Project = relationship("Project", secondary="Project_has_Person", backref="people")
    UserGroup = relationship(
        "UserGroup", secondary="UserGroup_has_Person", backref="people"
    )


class Phasing(Base):
    __tablename__ = "Phasing"

    phasingId = Column(Integer, primary_key=True, info="Primary key (auto-incremented)")
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        info="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        info="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="Related spaceGroup",
    )
    method = Column(
        ENUM("solvent flattening", "solvent flipping"), info="phasing method"
    )
    solventContent = Column(Float(asdecimal=True))
    enantiomorph = Column(Integer, info="0 or 1")
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())

    PhasingAnalysis = relationship(
        "PhasingAnalysis",
        primaryjoin="Phasing.phasingAnalysisId == PhasingAnalysis.phasingAnalysisId",
        backref="phasings",
    )
    PhasingProgramRun = relationship(
        "PhasingProgramRun",
        primaryjoin="Phasing.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId",
        backref="phasings",
    )
    SpaceGroup = relationship(
        "SpaceGroup",
        primaryjoin="Phasing.spaceGroupId == SpaceGroup.spaceGroupId",
        backref="phasings",
    )


class PhasingAnalysis(Base):
    __tablename__ = "PhasingAnalysis"

    phasingAnalysisId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")


class PhasingProgramAttachment(Base):
    __tablename__ = "PhasingProgramAttachment"

    phasingProgramAttachmentId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        info="Related program item",
    )
    fileType = Column(
        ENUM(
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
    fileName = Column(String(45), info="file name")
    filePath = Column(String(255), info="file path")
    input = Column(Integer)
    recordTimeStamp = Column(
        DateTime,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )

    PhasingProgramRun = relationship(
        "PhasingProgramRun",
        primaryjoin="PhasingProgramAttachment.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId",
        backref="phasing_program_attachments",
    )


class PhasingProgramRun(Base):
    __tablename__ = "PhasingProgramRun"

    phasingProgramRunId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingCommandLine = Column(String(255), info="Command line for phasing")
    phasingPrograms = Column(String(255), info="Phasing programs (comma separated)")
    phasingStatus = Column(Integer, info="success (1) / fail (0)")
    phasingMessage = Column(String(255), info="warning, error,...")
    phasingStartTime = Column(DateTime, info="Processing start time")
    phasingEndTime = Column(DateTime, info="Processing end time")
    phasingEnvironment = Column(String(255), info="Cpus, Nodes,...")
    phasingDirectory = Column(String(255), info="Directory of execution")
    recordTimeStamp = Column(
        DateTime,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )


class PhasingStatistics(Base):
    __tablename__ = "PhasingStatistics"

    phasingStatisticsId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingHasScalingId1 = Column(
        ForeignKey(
            "Phasing_has_Scaling.phasingHasScalingId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        info="the dataset in question",
    )
    phasingHasScalingId2 = Column(
        ForeignKey(
            "Phasing_has_Scaling.phasingHasScalingId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        info="if this is MIT or MAD, which scaling are being compared, null otherwise",
    )
    phasingStepId = Column(
        ForeignKey("PhasingStep.phasingStepId", ondelete="CASCADE"), index=True
    )
    numberOfBins = Column(Integer, info="the total number of bins")
    binNumber = Column(Integer, info="binNumber, 999 for overall")
    lowRes = Column(
        Float(asdecimal=True), info="low resolution cutoff of this binfloat"
    )
    highRes = Column(
        Float(asdecimal=True), info="high resolution cutoff of this binfloat"
    )
    metric = Column(
        ENUM(
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
    statisticsValue = Column(Float(asdecimal=True), info="the statistics value")
    nReflections = Column(Integer)
    recordTimeStamp = Column(
        DateTime,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )

    Phasing_has_Scaling = relationship(
        "PhasingHasScaling",
        primaryjoin="PhasingStatistics.phasingHasScalingId1 == PhasingHasScaling.phasingHasScalingId",
        backref="phasinghasscaling_phasing_statisticss",
    )
    Phasing_has_Scaling1 = relationship(
        "PhasingHasScaling",
        primaryjoin="PhasingStatistics.phasingHasScalingId2 == PhasingHasScaling.phasingHasScalingId",
        backref="phasinghasscaling_phasing_statisticss_0",
    )
    PhasingStep = relationship(
        "PhasingStep",
        primaryjoin="PhasingStatistics.phasingStepId == PhasingStep.phasingStepId",
        backref="phasing_statisticss",
    )


class PhasingStep(Base):
    __tablename__ = "PhasingStep"

    phasingStepId = Column(Integer, primary_key=True)
    previousPhasingStepId = Column(Integer)
    programRunId = Column(
        ForeignKey("PhasingProgramRun.phasingProgramRunId", ondelete="CASCADE"),
        index=True,
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE"), index=True
    )
    autoProcScalingId = Column(
        ForeignKey("AutoProcScaling.autoProcScalingId", ondelete="CASCADE"), index=True
    )
    phasingAnalysisId = Column(Integer, index=True)
    phasingStepType = Column(
        ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        )
    )
    method = Column(String(45))
    solventContent = Column(String(45))
    enantiomorph = Column(String(45))
    lowRes = Column(String(45))
    highRes = Column(String(45))
    groupName = Column(String(45))
    recordTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())

    AutoProcScaling = relationship(
        "AutoProcScaling",
        primaryjoin="PhasingStep.autoProcScalingId == AutoProcScaling.autoProcScalingId",
        backref="phasing_steps",
    )
    PhasingProgramRun = relationship(
        "PhasingProgramRun",
        primaryjoin="PhasingStep.programRunId == PhasingProgramRun.phasingProgramRunId",
        backref="phasing_steps",
    )
    SpaceGroup = relationship(
        "SpaceGroup",
        primaryjoin="PhasingStep.spaceGroupId == SpaceGroup.spaceGroupId",
        backref="phasing_steps",
    )


class PhasingHasScaling(Base):
    __tablename__ = "Phasing_has_Scaling"

    phasingHasScalingId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        info="Related phasing analysis item",
    )
    autoProcScalingId = Column(
        ForeignKey(
            "AutoProcScaling.autoProcScalingId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        info="Related autoProcScaling item",
    )
    datasetNumber = Column(
        Integer,
        info="serial number of the dataset and always reserve 0 for the reference",
    )
    recordTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())

    AutoProcScaling = relationship(
        "AutoProcScaling",
        primaryjoin="PhasingHasScaling.autoProcScalingId == AutoProcScaling.autoProcScalingId",
        backref="phasing_has_scalings",
    )
    PhasingAnalysis = relationship(
        "PhasingAnalysis",
        primaryjoin="PhasingHasScaling.phasingAnalysisId == PhasingAnalysis.phasingAnalysisId",
        backref="phasing_has_scalings",
    )


class PlateGroup(Base):
    __tablename__ = "PlateGroup"

    plateGroupId = Column(Integer, primary_key=True)
    name = Column(String(255))
    storageTemperature = Column(String(45))


class PlateType(Base):
    __tablename__ = "PlateType"

    PlateTypeId = Column(Integer, primary_key=True)
    experimentId = Column(Integer, index=True)
    name = Column(String(45))
    description = Column(String(45))
    shape = Column(String(45))
    rowCount = Column(Integer)
    columnCount = Column(Integer)


class Position(Base):
    __tablename__ = "Position"

    positionId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    relativePositionId = Column(
        ForeignKey("Position.positionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="relative position, null otherwise",
    )
    posX = Column(Float(asdecimal=True))
    posY = Column(Float(asdecimal=True))
    posZ = Column(Float(asdecimal=True))
    scale = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")

    parent = relationship(
        "Position",
        remote_side=[positionId],
        primaryjoin="Position.relativePositionId == Position.positionId",
        backref="positions",
    )


class PreparePhasingData(Base):
    __tablename__ = "PreparePhasingData"

    preparePhasingDataId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        info="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        info="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="Related spaceGroup",
    )
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")

    PhasingAnalysis = relationship(
        "PhasingAnalysis",
        primaryjoin="PreparePhasingData.phasingAnalysisId == PhasingAnalysis.phasingAnalysisId",
        backref="prepare_phasing_datas",
    )
    PhasingProgramRun = relationship(
        "PhasingProgramRun",
        primaryjoin="PreparePhasingData.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId",
        backref="prepare_phasing_datas",
    )
    SpaceGroup = relationship(
        "SpaceGroup",
        primaryjoin="PreparePhasingData.spaceGroupId == SpaceGroup.spaceGroupId",
        backref="prepare_phasing_datas",
    )


class Project(Base):
    __tablename__ = "Project"

    projectId = Column(Integer, primary_key=True)
    personId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)
    title = Column(String(200))
    acronym = Column(String(100))
    owner = Column(String(50))

    Person = relationship(
        "Person", primaryjoin="Project.personId == Person.personId", backref="projects"
    )
    Protein = relationship(
        "Protein", secondary="Project_has_Protein", backref="projects"
    )
    BLSession = relationship(
        "BLSession", secondary="Project_has_Session", backref="projects"
    )
    Shipping = relationship(
        "Shipping", secondary="Project_has_Shipping", backref="projects"
    )
    XFEFluorescenceSpectrum = relationship(
        "XFEFluorescenceSpectrum",
        secondary="Project_has_XFEFSpectrum",
        backref="projects",
    )


t_Project_has_BLSample = Table(
    "Project_has_BLSample",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "blSampleId",
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_DCGroup = Table(
    "Project_has_DCGroup",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "dataCollectionGroupId",
        ForeignKey(
            "DataCollectionGroup.dataCollectionGroupId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_EnergyScan = Table(
    "Project_has_EnergyScan",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "energyScanId",
        ForeignKey("EnergyScan.energyScanId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_Person = Table(
    "Project_has_Person",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "personId",
        ForeignKey("Person.personId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_Protein = Table(
    "Project_has_Protein",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "proteinId",
        ForeignKey("Protein.proteinId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_Session = Table(
    "Project_has_Session",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "sessionId",
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_Shipping = Table(
    "Project_has_Shipping",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "shippingId",
        ForeignKey("Shipping.shippingId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ProjectHasUser(Base):
    __tablename__ = "Project_has_User"

    projecthasuserid = Column(Integer, primary_key=True)
    projectid = Column(
        ForeignKey("Project.projectId", ondelete="CASCADE"), nullable=False, index=True
    )
    username = Column(String(15))

    Project = relationship(
        "Project",
        primaryjoin="ProjectHasUser.projectid == Project.projectId",
        backref="project_has_users",
    )


t_Project_has_XFEFSpectrum = Table(
    "Project_has_XFEFSpectrum",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "xfeFluorescenceSpectrumId",
        ForeignKey(
            "XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId", ondelete="CASCADE"
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class Proposal(Base):
    __tablename__ = "Proposal"
    __table_args__ = (
        Index("Proposal_FKIndexCodeNumber", "proposalCode", "proposalNumber"),
    )

    proposalId = Column(Integer, primary_key=True)
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    title = Column(String(200, "utf8mb4_unicode_ci"))
    proposalCode = Column(String(45))
    proposalNumber = Column(String(45))
    proposalType = Column(String(2), info="Proposal type: MX, BX")
    bltimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    externalId = Column(BINARY(16))
    state = Column(ENUM("Open", "Closed", "Cancelled"), server_default=FetchedValue())

    Person = relationship(
        "Person",
        primaryjoin="Proposal.personId == Person.personId",
        backref="proposals",
    )


class ProposalHasPerson(Base):
    __tablename__ = "ProposalHasPerson"

    proposalHasPersonId = Column(Integer, primary_key=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE"), nullable=False, index=True
    )

    Person = relationship(
        "Person",
        primaryjoin="ProposalHasPerson.personId == Person.personId",
        backref="proposal_has_people",
    )
    Proposal = relationship(
        "Proposal",
        primaryjoin="ProposalHasPerson.proposalId == Proposal.proposalId",
        backref="proposal_has_people",
    )


class Protein(Base):
    __tablename__ = "Protein"
    __table_args__ = (Index("ProteinAcronym_Index", "proposalId", "acronym"),)

    proteinId = Column(Integer, primary_key=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    name = Column(String(255, "utf8mb4_unicode_ci"))
    acronym = Column(String(45), index=True)
    description = Column(Text, info="A description/summary using words and sentences")
    hazardGroup = Column(
        Integer, nullable=False, server_default=FetchedValue(), info="A.k.a. risk group"
    )
    containmentLevel = Column(
        Integer,
        nullable=False,
        server_default=FetchedValue(),
        info="A.k.a. biosafety level, which indicates the level of containment required",
    )
    safetyLevel = Column(ENUM("GREEN", "YELLOW", "RED"))
    molecularMass = Column(Float(asdecimal=True))
    proteinType = Column(String(45))
    sequence = Column(Text)
    personId = Column(Integer, index=True)
    bltimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    isCreatedBySampleSheet = Column(Integer, server_default=FetchedValue())
    externalId = Column(BINARY(16))
    componentTypeId = Column(
        ForeignKey(
            "ComponentType.componentTypeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    modId = Column(String(20))
    concentrationTypeId = Column(Integer)
    _global = Column("global", Integer, server_default=FetchedValue())

    ComponentType = relationship(
        "ComponentType",
        primaryjoin="Protein.componentTypeId == ComponentType.componentTypeId",
        backref="proteins",
    )
    Proposal = relationship(
        "Proposal",
        primaryjoin="Protein.proposalId == Proposal.proposalId",
        backref="proteins",
    )
    ComponentSubType = relationship(
        "ComponentSubType", secondary="Component_has_SubType", backref="proteins"
    )


class ProteinHasLattice(Protein):
    __tablename__ = "Protein_has_Lattice"

    proteinId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE"), primary_key=True
    )
    cell_a = Column(Float(asdecimal=True))
    cell_b = Column(Float(asdecimal=True))
    cell_c = Column(Float(asdecimal=True))
    cell_alpha = Column(Float(asdecimal=True))
    cell_beta = Column(Float(asdecimal=True))
    cell_gamma = Column(Float(asdecimal=True))


class ProteinHasPDB(Base):
    __tablename__ = "Protein_has_PDB"

    proteinhaspdbid = Column(Integer, primary_key=True)
    proteinid = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE"), nullable=False, index=True
    )
    pdbid = Column(
        ForeignKey("PDB.pdbId", ondelete="CASCADE"), nullable=False, index=True
    )

    PDB = relationship(
        "PDB",
        primaryjoin="ProteinHasPDB.pdbid == PDB.pdbId",
        backref="protein_has_pdbs",
    )
    Protein = relationship(
        "Protein",
        primaryjoin="ProteinHasPDB.proteinid == Protein.proteinId",
        backref="protein_has_pdbs",
    )


class RigidBodyModeling(Base):
    __tablename__ = "RigidBodyModeling"

    rigidBodyModelingId = Column(Integer, primary_key=True)
    subtractionId = Column(Integer, nullable=False, index=True)
    fitFilePath = Column(String(255))
    rigidBodyModelFilePath = Column(String(255))
    logFilePath = Column(String(255))
    curveConfigFilePath = Column(String(255))
    subUnitConfigFilePath = Column(String(255))
    crossCorrConfigFilePath = Column(String(255))
    contactDescriptionFilePath = Column(String(255))
    symmetry = Column(String(255))
    creationDate = Column(String(45))


class RobotAction(Base):
    __tablename__ = "RobotAction"

    robotActionId = Column(Integer, primary_key=True)
    blsessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    blsampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"), index=True
    )
    actionType = Column(ENUM("LOAD", "UNLOAD", "DISPOSE", "STORE", "WASH", "ANNEAL"))
    startTimestamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    endTimestamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    status = Column(ENUM("SUCCESS", "ERROR", "CRITICAL", "WARNING", "COMMANDNOTSENT"))
    message = Column(String(255))
    containerLocation = Column(SmallInteger)
    dewarLocation = Column(SmallInteger)
    sampleBarcode = Column(String(45))
    xtalSnapshotBefore = Column(String(255))
    xtalSnapshotAfter = Column(String(255))

    BLSample = relationship(
        "BLSample",
        primaryjoin="RobotAction.blsampleId == BLSample.blSampleId",
        backref="robot_actions",
    )
    BLSession = relationship(
        "BLSession",
        primaryjoin="RobotAction.blsessionId == BLSession.sessionId",
        backref="robot_actions",
    )


class Run(Base):
    __tablename__ = "Run"

    runId = Column(Integer, primary_key=True)
    timePerFrame = Column(String(45))
    timeStart = Column(String(45))
    timeEnd = Column(String(45))
    storageTemperature = Column(String(45))
    exposureTemperature = Column(String(45))
    spectrophotometer = Column(String(45))
    energy = Column(String(45))
    creationDate = Column(DateTime)
    frameAverage = Column(String(45))
    frameCount = Column(String(45))
    transmission = Column(String(45))
    beamCenterX = Column(String(45))
    beamCenterY = Column(String(45))
    pixelSizeX = Column(String(45))
    pixelSizeY = Column(String(45))
    radiationRelative = Column(String(45))
    radiationAbsolute = Column(String(45))
    normalization = Column(String(45))


class SWOnceToken(Base):
    __tablename__ = "SW_onceToken"

    onceTokenId = Column(Integer, primary_key=True)
    token = Column(String(128))
    personId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"), index=True
    )
    validity = Column(String(200))
    recordTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())

    Person = relationship(
        "Person",
        primaryjoin="SWOnceToken.personId == Person.personId",
        backref="sw_once_tokens",
    )
    Proposal = relationship(
        "Proposal",
        primaryjoin="SWOnceToken.proposalId == Proposal.proposalId",
        backref="sw_once_tokens",
    )


class SafetyLevel(Base):
    __tablename__ = "SafetyLevel"

    safetyLevelId = Column(Integer, primary_key=True)
    code = Column(String(45))
    description = Column(String(45))


class SamplePlate(Base):
    __tablename__ = "SamplePlate"

    samplePlateId = Column(Integer, primary_key=True)
    experimentId = Column(
        ForeignKey("Experiment.experimentId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    plateGroupId = Column(
        ForeignKey("PlateGroup.plateGroupId", ondelete="CASCADE"), index=True
    )
    plateTypeId = Column(
        ForeignKey("PlateType.PlateTypeId", ondelete="CASCADE"), index=True
    )
    instructionSetId = Column(
        ForeignKey("InstructionSet.instructionSetId", ondelete="CASCADE"), index=True
    )
    boxId = Column(Integer)
    name = Column(String(45))
    slotPositionRow = Column(String(45))
    slotPositionColumn = Column(String(45))
    storageTemperature = Column(String(45))

    Experiment = relationship(
        "Experiment",
        primaryjoin="SamplePlate.experimentId == Experiment.experimentId",
        backref="sample_plates",
    )
    InstructionSet = relationship(
        "InstructionSet",
        primaryjoin="SamplePlate.instructionSetId == InstructionSet.instructionSetId",
        backref="sample_plates",
    )
    PlateGroup = relationship(
        "PlateGroup",
        primaryjoin="SamplePlate.plateGroupId == PlateGroup.plateGroupId",
        backref="sample_plates",
    )
    PlateType = relationship(
        "PlateType",
        primaryjoin="SamplePlate.plateTypeId == PlateType.PlateTypeId",
        backref="sample_plates",
    )


class SamplePlatePosition(Base):
    __tablename__ = "SamplePlatePosition"

    samplePlatePositionId = Column(Integer, primary_key=True)
    samplePlateId = Column(
        ForeignKey("SamplePlate.samplePlateId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    rowNumber = Column(Integer)
    columnNumber = Column(Integer)
    volume = Column(String(45))

    SamplePlate = relationship(
        "SamplePlate",
        primaryjoin="SamplePlatePosition.samplePlateId == SamplePlate.samplePlateId",
        backref="sample_plate_positions",
    )


class SaxsDataCollection(Base):
    __tablename__ = "SaxsDataCollection"

    dataCollectionId = Column(Integer, primary_key=True)
    experimentId = Column(
        ForeignKey("Experiment.experimentId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    comments = Column(String(5120))

    Experiment = relationship(
        "Experiment",
        primaryjoin="SaxsDataCollection.experimentId == Experiment.experimentId",
        backref="saxs_data_collections",
    )


class ScanParametersModel(Base):
    __tablename__ = "ScanParametersModel"

    scanParametersModelId = Column(Integer, primary_key=True)
    scanParametersServiceId = Column(
        ForeignKey(
            "ScanParametersService.scanParametersServiceId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    dataCollectionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    modelNumber = Column(Integer)
    start = Column(Float(asdecimal=True))
    stop = Column(Float(asdecimal=True))
    step = Column(Float(asdecimal=True))
    array = Column(Text)

    DiffractionPlan = relationship(
        "DiffractionPlan",
        primaryjoin="ScanParametersModel.dataCollectionPlanId == DiffractionPlan.diffractionPlanId",
        backref="scan_parameters_models",
    )
    ScanParametersService = relationship(
        "ScanParametersService",
        primaryjoin="ScanParametersModel.scanParametersServiceId == ScanParametersService.scanParametersServiceId",
        backref="scan_parameters_models",
    )


class ScanParametersService(Base):
    __tablename__ = "ScanParametersService"

    scanParametersServiceId = Column(Integer, primary_key=True)
    name = Column(String(45))
    description = Column(String(45))


class Schedule(Base):
    __tablename__ = "Schedule"

    scheduleId = Column(Integer, primary_key=True)
    name = Column(String(45))


class ScheduleComponent(Base):
    __tablename__ = "ScheduleComponent"

    scheduleComponentId = Column(Integer, primary_key=True)
    scheduleId = Column(
        ForeignKey("Schedule.scheduleId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    inspectionTypeId = Column(
        ForeignKey("InspectionType.inspectionTypeId", ondelete="CASCADE"), index=True
    )
    offset_hours = Column(Integer)

    InspectionType = relationship(
        "InspectionType",
        primaryjoin="ScheduleComponent.inspectionTypeId == InspectionType.inspectionTypeId",
        backref="schedule_components",
    )
    Schedule = relationship(
        "Schedule",
        primaryjoin="ScheduleComponent.scheduleId == Schedule.scheduleId",
        backref="schedule_components",
    )


class SchemaStatus(Base):
    __tablename__ = "SchemaStatus"

    schemaStatusId = Column(Integer, primary_key=True)
    scriptName = Column(String(100), nullable=False, unique=True)
    schemaStatus = Column(String(10))
    recordTimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())


class Screen(Base):
    __tablename__ = "Screen"

    screenId = Column(Integer, primary_key=True)
    name = Column(String(45))
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"), index=True
    )
    _global = Column("global", Integer)

    Proposal = relationship(
        "Proposal",
        primaryjoin="Screen.proposalId == Proposal.proposalId",
        backref="screens",
    )


class ScreenComponent(Base):
    __tablename__ = "ScreenComponent"

    screenComponentId = Column(Integer, primary_key=True)
    screenComponentGroupId = Column(
        ForeignKey("ScreenComponentGroup.screenComponentGroupId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    componentId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE"), index=True
    )
    concentration = Column(Float)
    pH = Column(Float)

    Protein = relationship(
        "Protein",
        primaryjoin="ScreenComponent.componentId == Protein.proteinId",
        backref="screen_components",
    )
    ScreenComponentGroup = relationship(
        "ScreenComponentGroup",
        primaryjoin="ScreenComponent.screenComponentGroupId == ScreenComponentGroup.screenComponentGroupId",
        backref="screen_components",
    )


class ScreenComponentGroup(Base):
    __tablename__ = "ScreenComponentGroup"

    screenComponentGroupId = Column(Integer, primary_key=True)
    screenId = Column(
        ForeignKey("Screen.screenId", ondelete="CASCADE"), nullable=False, index=True
    )
    position = Column(SmallInteger)

    Screen = relationship(
        "Screen",
        primaryjoin="ScreenComponentGroup.screenId == Screen.screenId",
        backref="screen_component_groups",
    )


class Screening(Base):
    __tablename__ = "Screening"

    screeningId = Column(Integer, primary_key=True)
    diffractionPlanId = Column(Integer, index=True, info="references DiffractionPlan")
    dataCollectionGroupId = Column(
        ForeignKey("DataCollectionGroup.dataCollectionGroupId", ondelete="CASCADE"),
        index=True,
    )
    dataCollectionId = Column(Integer)
    bltimeStamp = Column(DateTime, nullable=False, server_default=FetchedValue())
    programVersion = Column(String(45))
    comments = Column(String(255))
    shortComments = Column(String(20))
    xmlSampleInformation = Column(LONGBLOB)

    DataCollectionGroup = relationship(
        "DataCollectionGroup",
        primaryjoin="Screening.dataCollectionGroupId == DataCollectionGroup.dataCollectionGroupId",
        backref="screenings",
    )


class ScreeningInput(Base):
    __tablename__ = "ScreeningInput"

    screeningInputId = Column(Integer, primary_key=True)
    screeningId = Column(
        ForeignKey("Screening.screeningId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    diffractionPlanId = Column(Integer, info="references DiffractionPlan table")
    beamX = Column(Float)
    beamY = Column(Float)
    rmsErrorLimits = Column(Float)
    minimumFractionIndexed = Column(Float)
    maximumFractionRejected = Column(Float)
    minimumSignalToNoise = Column(Float)
    xmlSampleInformation = Column(LONGBLOB)

    Screening = relationship(
        "Screening",
        primaryjoin="ScreeningInput.screeningId == Screening.screeningId",
        backref="screening_inputs",
    )


class ScreeningOutput(Base):
    __tablename__ = "ScreeningOutput"

    screeningOutputId = Column(Integer, primary_key=True)
    screeningId = Column(
        ForeignKey("Screening.screeningId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    statusDescription = Column(String(1024))
    rejectedReflections = Column(Integer)
    resolutionObtained = Column(Float)
    spotDeviationR = Column(Float)
    spotDeviationTheta = Column(Float)
    beamShiftX = Column(Float)
    beamShiftY = Column(Float)
    numSpotsFound = Column(Integer)
    numSpotsUsed = Column(Integer)
    numSpotsRejected = Column(Integer)
    mosaicity = Column(Float)
    iOverSigma = Column(Float)
    diffractionRings = Column(Integer)
    strategySuccess = Column(Integer, nullable=False, server_default=FetchedValue())
    mosaicityEstimated = Column(Integer, nullable=False, server_default=FetchedValue())
    rankingResolution = Column(Float(asdecimal=True))
    program = Column(String(45))
    doseTotal = Column(Float(asdecimal=True))
    totalExposureTime = Column(Float(asdecimal=True))
    totalRotationRange = Column(Float(asdecimal=True))
    totalNumberOfImages = Column(Integer)
    rFriedel = Column(Float(asdecimal=True))
    indexingSuccess = Column(Integer, nullable=False, server_default=FetchedValue())
    screeningSuccess = Column(Integer, server_default=FetchedValue())

    Screening = relationship(
        "Screening",
        primaryjoin="ScreeningOutput.screeningId == Screening.screeningId",
        backref="screening_outputs",
    )


class ScreeningOutputLattice(Base):
    __tablename__ = "ScreeningOutputLattice"

    screeningOutputLatticeId = Column(Integer, primary_key=True)
    screeningOutputId = Column(
        ForeignKey(
            "ScreeningOutput.screeningOutputId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    spaceGroup = Column(String(45))
    pointGroup = Column(String(45))
    bravaisLattice = Column(String(45))
    rawOrientationMatrix_a_x = Column(Float)
    rawOrientationMatrix_a_y = Column(Float)
    rawOrientationMatrix_a_z = Column(Float)
    rawOrientationMatrix_b_x = Column(Float)
    rawOrientationMatrix_b_y = Column(Float)
    rawOrientationMatrix_b_z = Column(Float)
    rawOrientationMatrix_c_x = Column(Float)
    rawOrientationMatrix_c_y = Column(Float)
    rawOrientationMatrix_c_z = Column(Float)
    unitCell_a = Column(Float)
    unitCell_b = Column(Float)
    unitCell_c = Column(Float)
    unitCell_alpha = Column(Float)
    unitCell_beta = Column(Float)
    unitCell_gamma = Column(Float)
    bltimeStamp = Column(DateTime, server_default=FetchedValue())
    labelitIndexing = Column(Integer, server_default=FetchedValue())

    ScreeningOutput = relationship(
        "ScreeningOutput",
        primaryjoin="ScreeningOutputLattice.screeningOutputId == ScreeningOutput.screeningOutputId",
        backref="screening_output_lattices",
    )


class ScreeningRank(Base):
    __tablename__ = "ScreeningRank"

    screeningRankId = Column(Integer, primary_key=True)
    screeningRankSetId = Column(
        ForeignKey(
            "ScreeningRankSet.screeningRankSetId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    screeningId = Column(
        ForeignKey("Screening.screeningId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    rankValue = Column(Float)
    rankInformation = Column(String(1024))

    Screening = relationship(
        "Screening",
        primaryjoin="ScreeningRank.screeningId == Screening.screeningId",
        backref="screening_ranks",
    )
    ScreeningRankSet = relationship(
        "ScreeningRankSet",
        primaryjoin="ScreeningRank.screeningRankSetId == ScreeningRankSet.screeningRankSetId",
        backref="screening_ranks",
    )


class ScreeningRankSet(Base):
    __tablename__ = "ScreeningRankSet"

    screeningRankSetId = Column(Integer, primary_key=True)
    rankEngine = Column(String(255))
    rankingProjectFileName = Column(String(255))
    rankingSummaryFileName = Column(String(255))


class ScreeningStrategy(Base):
    __tablename__ = "ScreeningStrategy"

    screeningStrategyId = Column(Integer, primary_key=True)
    screeningOutputId = Column(
        ForeignKey(
            "ScreeningOutput.screeningOutputId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    phiStart = Column(Float)
    phiEnd = Column(Float)
    rotation = Column(Float)
    exposureTime = Column(Float)
    resolution = Column(Float)
    completeness = Column(Float)
    multiplicity = Column(Float)
    anomalous = Column(Integer, nullable=False, server_default=FetchedValue())
    program = Column(String(45))
    rankingResolution = Column(Float)
    transmission = Column(
        Float, info="Transmission for the strategy as given by the strategy program."
    )

    ScreeningOutput = relationship(
        "ScreeningOutput",
        primaryjoin="ScreeningStrategy.screeningOutputId == ScreeningOutput.screeningOutputId",
        backref="screening_strategies",
    )


class ScreeningStrategySubWedge(Base):
    __tablename__ = "ScreeningStrategySubWedge"

    screeningStrategySubWedgeId = Column(Integer, primary_key=True, info="Primary key")
    screeningStrategyWedgeId = Column(
        ForeignKey(
            "ScreeningStrategyWedge.screeningStrategyWedgeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        info="Foreign key to parent table",
    )
    subWedgeNumber = Column(
        Integer, info="The number of this subwedge within the wedge"
    )
    rotationAxis = Column(String(45), info="Angle where subwedge starts")
    axisStart = Column(Float, info="Angle where subwedge ends")
    axisEnd = Column(Float, info="Exposure time for subwedge")
    exposureTime = Column(Float, info="Transmission for subwedge")
    transmission = Column(Float)
    oscillationRange = Column(Float)
    completeness = Column(Float)
    multiplicity = Column(Float)
    doseTotal = Column(Float, info="Total dose for this subwedge")
    numberOfImages = Column(Integer, info="Number of images for this subwedge")
    comments = Column(String(255))
    resolution = Column(Float)

    ScreeningStrategyWedge = relationship(
        "ScreeningStrategyWedge",
        primaryjoin="ScreeningStrategySubWedge.screeningStrategyWedgeId == ScreeningStrategyWedge.screeningStrategyWedgeId",
        backref="screening_strategy_sub_wedges",
    )


class ScreeningStrategyWedge(Base):
    __tablename__ = "ScreeningStrategyWedge"

    screeningStrategyWedgeId = Column(Integer, primary_key=True, info="Primary key")
    screeningStrategyId = Column(
        ForeignKey(
            "ScreeningStrategy.screeningStrategyId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        info="Foreign key to parent table",
    )
    wedgeNumber = Column(Integer, info="The number of this wedge within the strategy")
    resolution = Column(Float)
    completeness = Column(Float)
    multiplicity = Column(Float)
    doseTotal = Column(Float, info="Total dose for this wedge")
    numberOfImages = Column(Integer, info="Number of images for this wedge")
    phi = Column(Float)
    kappa = Column(Float)
    chi = Column(Float)
    comments = Column(String(255))
    wavelength = Column(Float(asdecimal=True))

    ScreeningStrategy = relationship(
        "ScreeningStrategy",
        primaryjoin="ScreeningStrategyWedge.screeningStrategyId == ScreeningStrategy.screeningStrategyId",
        backref="screening_strategy_wedges",
    )


class SessionType(Base):
    __tablename__ = "SessionType"

    sessionTypeId = Column(Integer, primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    typeName = Column(String(31), nullable=False)

    BLSession = relationship(
        "BLSession",
        primaryjoin="SessionType.sessionId == BLSession.sessionId",
        backref="session_types",
    )


class SessionHasPerson(Base):
    __tablename__ = "Session_has_Person"

    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    role = Column(
        ENUM(
            "Local Contact",
            "Local Contact 2",
            "Staff",
            "Team Leader",
            "Co-Investigator",
            "Principal Investigator",
            "Alternate Contact",
        )
    )
    remote = Column(Integer, server_default=FetchedValue())

    Person = relationship(
        "Person",
        primaryjoin="SessionHasPerson.personId == Person.personId",
        backref="session_has_people",
    )
    BLSession = relationship(
        "BLSession",
        primaryjoin="SessionHasPerson.sessionId == BLSession.sessionId",
        backref="session_has_people",
    )


class Shipping(Base):
    __tablename__ = "Shipping"

    shippingId = Column(Integer, primary_key=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=FetchedValue(),
    )
    shippingName = Column(String(45), index=True)
    deliveryAgent_agentName = Column(String(45))
    deliveryAgent_shippingDate = Column(Date)
    deliveryAgent_deliveryDate = Column(Date)
    deliveryAgent_agentCode = Column(String(45))
    deliveryAgent_flightCode = Column(String(45))
    shippingStatus = Column(String(45), index=True)
    bltimeStamp = Column(DateTime)
    laboratoryId = Column(Integer, index=True)
    isStorageShipping = Column(Integer, server_default=FetchedValue())
    creationDate = Column(DateTime, index=True)
    comments = Column(String(255))
    sendingLabContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="CASCADE"), index=True
    )
    returnLabContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="CASCADE"), index=True
    )
    returnCourier = Column(String(45))
    dateOfShippingToUser = Column(DateTime)
    shippingType = Column(String(45))
    safetyLevel = Column(String(8))

    Proposal = relationship(
        "Proposal",
        primaryjoin="Shipping.proposalId == Proposal.proposalId",
        backref="shippings",
    )
    LabContact = relationship(
        "LabContact",
        primaryjoin="Shipping.returnLabContactId == LabContact.labContactId",
        backref="labcontact_shippings",
    )
    LabContact1 = relationship(
        "LabContact",
        primaryjoin="Shipping.sendingLabContactId == LabContact.labContactId",
        backref="labcontact_shippings_0",
    )


t_ShippingHasSession = Table(
    "ShippingHasSession",
    metadata,
    Column(
        "shippingId",
        ForeignKey("Shipping.shippingId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
    Column(
        "sessionId",
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class SpaceGroup(Base):
    __tablename__ = "SpaceGroup"

    spaceGroupId = Column(Integer, primary_key=True, info="Primary key")
    geometryClassnameId = Column(
        ForeignKey(
            "GeometryClassname.geometryClassnameId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    spaceGroupNumber = Column(Integer, info="ccp4 number pr IUCR")
    spaceGroupShortName = Column(
        String(45), index=True, info="short name without blank"
    )
    spaceGroupName = Column(String(45), info="verbose name")
    bravaisLattice = Column(String(45), info="short name")
    bravaisLatticeName = Column(String(45), info="verbose name")
    pointGroup = Column(String(45), info="point group")
    MX_used = Column(
        Integer,
        nullable=False,
        server_default=FetchedValue(),
        info="1 if used in the crystal form",
    )

    GeometryClassname = relationship(
        "GeometryClassname",
        primaryjoin="SpaceGroup.geometryClassnameId == GeometryClassname.geometryClassnameId",
        backref="space_groups",
    )


class Specimen(Base):
    __tablename__ = "Specimen"

    specimenId = Column(Integer, primary_key=True)
    experimentId = Column(
        ForeignKey("Experiment.experimentId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    bufferId = Column(ForeignKey("Buffer.bufferId", ondelete="CASCADE"), index=True)
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"), index=True
    )
    samplePlatePositionId = Column(
        ForeignKey("SamplePlatePosition.samplePlatePositionId", ondelete="CASCADE"),
        index=True,
    )
    safetyLevelId = Column(
        ForeignKey("SafetyLevel.safetyLevelId", ondelete="CASCADE"), index=True
    )
    stockSolutionId = Column(
        ForeignKey("StockSolution.stockSolutionId", ondelete="CASCADE"), index=True
    )
    code = Column(String(255))
    concentration = Column(String(45))
    volume = Column(String(45))
    comments = Column(String(5120))

    Buffer = relationship(
        "Buffer",
        primaryjoin="Specimen.bufferId == Buffer.bufferId",
        backref="specimens",
    )
    Experiment = relationship(
        "Experiment",
        primaryjoin="Specimen.experimentId == Experiment.experimentId",
        backref="specimens",
    )
    Macromolecule = relationship(
        "Macromolecule",
        primaryjoin="Specimen.macromoleculeId == Macromolecule.macromoleculeId",
        backref="specimens",
    )
    SafetyLevel = relationship(
        "SafetyLevel",
        primaryjoin="Specimen.safetyLevelId == SafetyLevel.safetyLevelId",
        backref="specimens",
    )
    SamplePlatePosition = relationship(
        "SamplePlatePosition",
        primaryjoin="Specimen.samplePlatePositionId == SamplePlatePosition.samplePlatePositionId",
        backref="specimens",
    )
    StockSolution = relationship(
        "StockSolution",
        primaryjoin="Specimen.stockSolutionId == StockSolution.stockSolutionId",
        backref="specimens",
    )


class StockSolution(Base):
    __tablename__ = "StockSolution"

    stockSolutionId = Column(Integer, primary_key=True)
    proposalId = Column(Integer, nullable=False, server_default=FetchedValue())
    bufferId = Column(
        ForeignKey("Buffer.bufferId", ondelete="CASCADE"), nullable=False, index=True
    )
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"), index=True
    )
    instructionSetId = Column(
        ForeignKey("InstructionSet.instructionSetId", ondelete="CASCADE"), index=True
    )
    boxId = Column(Integer)
    name = Column(String(45))
    storageTemperature = Column(String(55))
    volume = Column(String(55))
    concentration = Column(String(55))
    comments = Column(String(255))

    Buffer = relationship(
        "Buffer",
        primaryjoin="StockSolution.bufferId == Buffer.bufferId",
        backref="stock_solutions",
    )
    InstructionSet = relationship(
        "InstructionSet",
        primaryjoin="StockSolution.instructionSetId == InstructionSet.instructionSetId",
        backref="stock_solutions",
    )
    Macromolecule = relationship(
        "Macromolecule",
        primaryjoin="StockSolution.macromoleculeId == Macromolecule.macromoleculeId",
        backref="stock_solutions",
    )


class Stoichiometry(Base):
    __tablename__ = "Stoichiometry"

    stoichiometryId = Column(Integer, primary_key=True)
    hostMacromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    ratio = Column(String(45))

    Macromolecule = relationship(
        "Macromolecule",
        primaryjoin="Stoichiometry.hostMacromoleculeId == Macromolecule.macromoleculeId",
        backref="macromolecule_stoichiometries",
    )
    Macromolecule1 = relationship(
        "Macromolecule",
        primaryjoin="Stoichiometry.macromoleculeId == Macromolecule.macromoleculeId",
        backref="macromolecule_stoichiometries_0",
    )


class Structure(Base):
    __tablename__ = "Structure"

    structureId = Column(Integer, primary_key=True)
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"), index=True
    )
    crystalId = Column(ForeignKey("Crystal.crystalId", ondelete="CASCADE"), index=True)
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"), index=True
    )
    filePath = Column(String(2048))
    structureType = Column(String(45))
    fromResiduesBases = Column(String(45))
    toResiduesBases = Column(String(45))
    sequence = Column(String(45))
    creationDate = Column(DateTime)
    name = Column(String(255))
    symmetry = Column(String(45))
    multiplicity = Column(String(45))
    groupName = Column(String(45))
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"), index=True
    )
    uniprotId = Column(String(45))

    BLSample = relationship(
        "BLSample",
        primaryjoin="Structure.blSampleId == BLSample.blSampleId",
        backref="structures",
    )
    Crystal = relationship(
        "Crystal",
        primaryjoin="Structure.crystalId == Crystal.crystalId",
        backref="structures",
    )
    Macromolecule = relationship(
        "Macromolecule",
        primaryjoin="Structure.macromoleculeId == Macromolecule.macromoleculeId",
        backref="structures",
    )
    Proposal = relationship(
        "Proposal",
        primaryjoin="Structure.proposalId == Proposal.proposalId",
        backref="structures",
    )


class SubstructureDetermination(Base):
    __tablename__ = "SubstructureDetermination"

    substructureDeterminationId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        info="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        info="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        info="Related spaceGroup",
    )
    method = Column(
        ENUM("SAD", "MAD", "SIR", "SIRAS", "MR", "MIR", "MIRAS", "RIP", "RIPAS"),
        info="phasing method",
    )
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")

    PhasingAnalysis = relationship(
        "PhasingAnalysis",
        primaryjoin="SubstructureDetermination.phasingAnalysisId == PhasingAnalysis.phasingAnalysisId",
        backref="substructure_determinations",
    )
    PhasingProgramRun = relationship(
        "PhasingProgramRun",
        primaryjoin="SubstructureDetermination.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId",
        backref="substructure_determinations",
    )
    SpaceGroup = relationship(
        "SpaceGroup",
        primaryjoin="SubstructureDetermination.spaceGroupId == SpaceGroup.spaceGroupId",
        backref="substructure_determinations",
    )


class Subtraction(Base):
    __tablename__ = "Subtraction"

    subtractionId = Column(Integer, primary_key=True)
    dataCollectionId = Column(
        ForeignKey("SaxsDataCollection.dataCollectionId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    rg = Column(String(45))
    rgStdev = Column(String(45))
    I0 = Column(String(45))
    I0Stdev = Column(String(45))
    firstPointUsed = Column(String(45))
    lastPointUsed = Column(String(45))
    quality = Column(String(45))
    isagregated = Column(String(45))
    concentration = Column(String(45))
    gnomFilePath = Column(String(255))
    rgGuinier = Column(String(45))
    rgGnom = Column(String(45))
    dmax = Column(String(45))
    total = Column(String(45))
    volume = Column(String(45))
    creationTime = Column(DateTime)
    kratkyFilePath = Column(String(255))
    scatteringFilePath = Column(String(255))
    guinierFilePath = Column(String(255))
    substractedFilePath = Column(String(255))
    gnomFilePathOutput = Column(String(255))
    sampleOneDimensionalFiles = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"), index=True
    )
    bufferOnedimensionalFiles = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"), index=True
    )
    sampleAverageFilePath = Column(String(255))
    bufferAverageFilePath = Column(String(255))

    FrameList = relationship(
        "FrameList",
        primaryjoin="Subtraction.bufferOnedimensionalFiles == FrameList.frameListId",
        backref="framelist_subtractions",
    )
    SaxsDataCollection = relationship(
        "SaxsDataCollection",
        primaryjoin="Subtraction.dataCollectionId == SaxsDataCollection.dataCollectionId",
        backref="subtractions",
    )
    FrameList1 = relationship(
        "FrameList",
        primaryjoin="Subtraction.sampleOneDimensionalFiles == FrameList.frameListId",
        backref="framelist_subtractions_0",
    )


class SubtractionToAbInitioModel(Base):
    __tablename__ = "SubtractionToAbInitioModel"

    subtractionToAbInitioModelId = Column(Integer, primary_key=True)
    abInitioId = Column(
        ForeignKey("AbInitioModel.abInitioModelId", ondelete="CASCADE"), index=True
    )
    subtractionId = Column(
        ForeignKey("Subtraction.subtractionId", ondelete="CASCADE"), index=True
    )

    AbInitioModel = relationship(
        "AbInitioModel",
        primaryjoin="SubtractionToAbInitioModel.abInitioId == AbInitioModel.abInitioModelId",
        backref="subtraction_to_ab_initio_models",
    )
    Subtraction = relationship(
        "Subtraction",
        primaryjoin="SubtractionToAbInitioModel.subtractionId == Subtraction.subtractionId",
        backref="subtraction_to_ab_initio_models",
    )


class Superposition(Base):
    __tablename__ = "Superposition"

    superpositionId = Column(Integer, primary_key=True)
    subtractionId = Column(Integer, nullable=False, index=True)
    abinitioModelPdbFilePath = Column(String(255))
    aprioriPdbFilePath = Column(String(255))
    alignedPdbFilePath = Column(String(255))
    creationDate = Column(DateTime)


class UntrustedRegion(Base):
    __tablename__ = "UntrustedRegion"

    untrustedRegionId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    detectorId = Column(
        ForeignKey("Detector.detectorId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    x1 = Column(Integer, nullable=False)
    x2 = Column(Integer, nullable=False)
    y1 = Column(Integer, nullable=False)
    y2 = Column(Integer, nullable=False)

    Detector = relationship(
        "Detector",
        primaryjoin="UntrustedRegion.detectorId == Detector.detectorId",
        backref="untrusted_regions",
    )


class UserGroup(Base):
    __tablename__ = "UserGroup"

    userGroupId = Column(Integer, primary_key=True)
    name = Column(String(31), nullable=False, unique=True)


t_UserGroup_has_Permission = Table(
    "UserGroup_has_Permission",
    metadata,
    Column(
        "userGroupId",
        ForeignKey("UserGroup.userGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "permissionId",
        ForeignKey("Permission.permissionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_UserGroup_has_Person = Table(
    "UserGroup_has_Person",
    metadata,
    Column(
        "userGroupId",
        ForeignKey("UserGroup.userGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "personId",
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_V_AnalysisInfo = Table(
    "V_AnalysisInfo",
    metadata,
    Column("experimentCreationDate", DateTime),
    Column("timeStart", String(45)),
    Column("dataCollectionId", Integer, server_default=FetchedValue()),
    Column("measurementId", Integer, server_default=FetchedValue()),
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("proposalCode", String(45)),
    Column("proposalNumber", String(45)),
    Column("priorityLevelId", Integer),
    Column("code", String(100)),
    Column("exposureTemperature", String(45)),
    Column("transmission", String(45)),
    Column("measurementComments", String(512)),
    Column("experimentComments", String(512)),
    Column("experimentId", Integer, server_default=FetchedValue()),
    Column("experimentType", String(128)),
    Column("conc", String(45)),
    Column("bufferAcronym", String(45)),
    Column("macromoleculeAcronym", String(45)),
    Column("bufferId", Integer, server_default=FetchedValue()),
    Column("macromoleculeId", Integer, server_default=FetchedValue()),
    Column("subtractedFilePath", String(255)),
    Column("rgGuinier", String(45)),
    Column("firstPointUsed", String(45)),
    Column("lastPointUsed", String(45)),
    Column("I0", String(45)),
    Column("isagregated", String(45)),
    Column("subtractionId", Integer),
    Column("rgGnom", String(45)),
    Column("total", String(45)),
    Column("dmax", String(45)),
    Column("volume", String(45)),
    Column("i0stdev", String(45)),
    Column("quality", String(45)),
    Column("substractionCreationTime", DateTime),
    Column("bufferBeforeMeasurementId", Integer),
    Column("bufferAfterMeasurementId", Integer),
    Column("bufferBeforeFramesMerged", String(45)),
    Column("bufferBeforeMergeId", Integer),
    Column("bufferBeforeAverageFilePath", String(255)),
    Column("sampleMeasurementId", Integer),
    Column("sampleMergeId", Integer),
    Column("averageFilePath", String(255)),
    Column("framesMerge", String(45)),
    Column("framesCount", String(45)),
    Column("bufferAfterFramesMerged", String(45)),
    Column("bufferAfterMergeId", Integer),
    Column("bufferAfterAverageFilePath", String(255)),
    Column("modelListId1", Integer),
    Column("nsdFilePath", String(255)),
    Column("modelListId2", Integer),
    Column("chi2RgFilePath", String(255)),
    Column("averagedModel", String(255)),
    Column("averagedModelId", Integer),
    Column("rapidShapeDeterminationModel", String(255)),
    Column("rapidShapeDeterminationModelId", Integer),
    Column("shapeDeterminationModel", String(255)),
    Column("shapeDeterminationModelId", Integer),
    Column("abInitioModelId", Integer),
    Column("comments", String(512)),
)


class Workflow(Base):
    __tablename__ = "Workflow"

    workflowId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    workflowTitle = Column(String(255))
    workflowType = Column(
        ENUM(
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
            "MXPressF",
            "MXPressH",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressR",
            "MXPressR_180",
            "MXPressR_dehydration",
            "MeshAndCollect",
            "MeshAndCollectFromFile",
        )
    )
    workflowTypeId = Column(Integer)
    comments = Column(String(1024))
    status = Column(String(255))
    resultFilePath = Column(String(255))
    logFilePath = Column(String(255))
    recordTimeStamp = Column(DateTime, info="Creation or last update date/time")


class WorkflowDehydration(Base):
    __tablename__ = "WorkflowDehydration"

    workflowDehydrationId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        info="Related workflow",
    )
    dataFilePath = Column(String(255))
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )

    Workflow = relationship(
        "Workflow",
        primaryjoin="WorkflowDehydration.workflowId == Workflow.workflowId",
        backref="workflow_dehydrations",
    )


class WorkflowMesh(Base):
    __tablename__ = "WorkflowMesh"

    workflowMeshId = Column(
        Integer, primary_key=True, info="Primary key (auto-incremented)"
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        info="Related workflow",
    )
    bestPositionId = Column(Integer, index=True)
    bestImageId = Column(
        ForeignKey("Image.imageId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    value1 = Column(Float(asdecimal=True))
    value2 = Column(Float(asdecimal=True))
    value3 = Column(Float(asdecimal=True), info="N value")
    value4 = Column(Float(asdecimal=True))
    cartographyPath = Column(String(255))
    recordTimeStamp = Column(
        DateTime,
        nullable=False,
        server_default=FetchedValue(),
        info="Creation or last update date/time",
    )

    Image = relationship(
        "Image",
        primaryjoin="WorkflowMesh.bestImageId == Image.imageId",
        backref="workflow_meshes",
    )
    Workflow = relationship(
        "Workflow",
        primaryjoin="WorkflowMesh.workflowId == Workflow.workflowId",
        backref="workflow_meshes",
    )


class WorkflowStep(Base):
    __tablename__ = "WorkflowStep"

    workflowStepId = Column(Integer, primary_key=True)
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    workflowStepType = Column(String(45))
    status = Column(String(45))
    folderPath = Column(String(1024))
    imageResultFilePath = Column(String(1024))
    htmlResultFilePath = Column(String(1024))
    resultFilePath = Column(String(1024))
    comments = Column(String(2048))
    crystalSizeX = Column(String(45))
    crystalSizeY = Column(String(45))
    crystalSizeZ = Column(String(45))
    maxDozorScore = Column(String(45))
    recordTimeStamp = Column(DateTime)

    Workflow = relationship(
        "Workflow",
        primaryjoin="WorkflowStep.workflowId == Workflow.workflowId",
        backref="workflow_steps",
    )


class WorkflowType(Base):
    __tablename__ = "WorkflowType"

    workflowTypeId = Column(Integer, primary_key=True)
    workflowTypeName = Column(String(45))
    comments = Column(String(2048))
    recordTimeStamp = Column(DateTime)


class XFEFluorescenceSpectrum(Base):
    __tablename__ = "XFEFluorescenceSpectrum"

    xfeFluorescenceSpectrumId = Column(Integer, primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    fittedDataFileFullPath = Column(String(255))
    scanFileFullPath = Column(String(255))
    jpegScanFileFullPath = Column(String(255))
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    filename = Column(String(255))
    energy = Column(Float)
    exposureTime = Column(Float)
    axisPosition = Column(Float)
    beamTransmission = Column(Float)
    annotatedPymcaXfeSpectrum = Column(String(255))
    beamSizeVertical = Column(Float)
    beamSizeHorizontal = Column(Float)
    crystalClass = Column(String(20))
    comments = Column(String(1024))
    flux = Column(Float(asdecimal=True), info="flux measured before the xrfSpectra")
    flux_end = Column(Float(asdecimal=True), info="flux measured after the xrfSpectra")
    workingDirectory = Column(String(512))
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId", ondelete="CASCADE"), index=True
    )

    BLSample = relationship(
        "BLSample",
        primaryjoin="XFEFluorescenceSpectrum.blSampleId == BLSample.blSampleId",
        backref="xfe_fluorescence_spectrums",
    )
    BLSubSample = relationship(
        "BLSubSample",
        primaryjoin="XFEFluorescenceSpectrum.blSubSampleId == BLSubSample.blSubSampleId",
        backref="xfe_fluorescence_spectrums",
    )
    BLSession = relationship(
        "BLSession",
        primaryjoin="XFEFluorescenceSpectrum.sessionId == BLSession.sessionId",
        backref="xfe_fluorescence_spectrums",
    )


class XRFFluorescenceMapping(Base):
    __tablename__ = "XRFFluorescenceMapping"

    xrfFluorescenceMappingId = Column(Integer, primary_key=True)
    xrfFluorescenceMappingROIId = Column(
        ForeignKey(
            "XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    imageNumber = Column(Integer, nullable=False)
    counts = Column(Integer, nullable=False)

    DataCollection = relationship(
        "DataCollection",
        primaryjoin="XRFFluorescenceMapping.dataCollectionId == DataCollection.dataCollectionId",
        backref="xrf_fluorescence_mappings",
    )
    XRFFluorescenceMappingROI = relationship(
        "XRFFluorescenceMappingROI",
        primaryjoin="XRFFluorescenceMapping.xrfFluorescenceMappingROIId == XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId",
        backref="xrf_fluorescence_mappings",
    )


class XRFFluorescenceMappingROI(Base):
    __tablename__ = "XRFFluorescenceMappingROI"

    xrfFluorescenceMappingROIId = Column(Integer, primary_key=True)
    startEnergy = Column(Float, nullable=False)
    endEnergy = Column(Float, nullable=False)
    element = Column(String(2))
    edge = Column(String(2), info="In future may be changed to enum(K, L)")
    r = Column(Integer, info="R colour component")
    g = Column(Integer, info="G colour component")
    b = Column(Integer, info="B colour component")


t_v_Log4Stat = Table(
    "v_Log4Stat",
    metadata,
    Column("id", Integer, server_default=FetchedValue()),
    Column("priority", String(15)),
    Column("timestamp", DateTime),
    Column("msg", String(255)),
    Column("detail", String(255)),
    Column("value", String(255)),
)


t_v_datacollection = Table(
    "v_datacollection",
    metadata,
    Column("dataCollectionId", Integer, server_default=FetchedValue()),
    Column("dataCollectionGroupId", Integer),
    Column("strategySubWedgeOrigId", Integer),
    Column("detectorId", Integer),
    Column("blSubSampleId", Integer),
    Column("dataCollectionNumber", Integer),
    Column("startTime", DateTime),
    Column("endTime", DateTime),
    Column("runStatus", String(45)),
    Column("axisStart", Float),
    Column("axisEnd", Float),
    Column("axisRange", Float),
    Column("overlap", Float),
    Column("numberOfImages", Integer),
    Column("startImageNumber", Integer),
    Column("numberOfPasses", Integer),
    Column("exposureTime", Float),
    Column("imageDirectory", String(255)),
    Column("imagePrefix", String(100)),
    Column("imageSuffix", String(45)),
    Column("fileTemplate", String(255)),
    Column("wavelength", Float),
    Column("resolution", Float),
    Column("detectorDistance", Float),
    Column("xBeam", Float),
    Column("yBeam", Float),
    Column("xBeamPix", Float),
    Column("yBeamPix", Float),
    Column("comments", String(1024)),
    Column("printableForReport", Integer, server_default=FetchedValue()),
    Column("slitGapVertical", Float),
    Column("slitGapHorizontal", Float),
    Column("transmission", Float),
    Column("synchrotronMode", String(20)),
    Column("xtalSnapshotFullPath1", String(255)),
    Column("xtalSnapshotFullPath2", String(255)),
    Column("xtalSnapshotFullPath3", String(255)),
    Column("xtalSnapshotFullPath4", String(255)),
    Column("rotationAxis", ENUM("Omega", "Kappa", "Phi")),
    Column("phiStart", Float),
    Column("kappaStart", Float),
    Column("omegaStart", Float),
    Column("resolutionAtCorner", Float),
    Column("detector2Theta", Float),
    Column("undulatorGap1", Float),
    Column("undulatorGap2", Float),
    Column("undulatorGap3", Float),
    Column("beamSizeAtSampleX", Float),
    Column("beamSizeAtSampleY", Float),
    Column("centeringMethod", String(255)),
    Column("averageTemperature", Float),
    Column("actualCenteringPosition", String(255)),
    Column("beamShape", String(45)),
    Column("flux", Float(asdecimal=True)),
    Column("flux_end", Float(asdecimal=True)),
    Column("totalAbsorbedDose", Float(asdecimal=True)),
    Column("bestWilsonPlotPath", String(255)),
    Column("imageQualityIndicatorsPlotPath", String(512)),
    Column("imageQualityIndicatorsCSVPath", String(512)),
    Column("sessionId", Integer, server_default=FetchedValue()),
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("workflowId", Integer),
    Column("AutoProcIntegration_dataCollectionId", Integer),
    Column("autoProcScalingId", Integer, server_default=FetchedValue()),
    Column("cell_a", Float),
    Column("cell_b", Float),
    Column("cell_c", Float),
    Column("cell_alpha", Float),
    Column("cell_beta", Float),
    Column("cell_gamma", Float),
    Column("anomalous", Integer, server_default=FetchedValue()),
    Column(
        "scalingStatisticsType",
        ENUM("overall", "innerShell", "outerShell"),
        server_default=FetchedValue(),
    ),
    Column("resolutionLimitHigh", Float),
    Column("resolutionLimitLow", Float),
    Column("completeness", Float),
    Column("AutoProc_spaceGroup", String(45)),
    Column("autoProcId", Integer, server_default=FetchedValue()),
    Column("rMerge", Float),
    Column("ccHalf", Float),
    Column("meanIOverSigI", Float),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("AutoProcProgram_processingPrograms", String(255)),
    Column(
        "AutoProcProgram_processingStatus",
        ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column("AutoProcProgram_autoProcProgramId", Integer, server_default=FetchedValue()),
    Column("ScreeningOutput_rankingResolution", Float(asdecimal=True)),
)


t_v_datacollection_autoprocintegration = Table(
    "v_datacollection_autoprocintegration",
    metadata,
    Column(
        "v_datacollection_summary_phasing_autoProcIntegrationId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("v_datacollection_summary_phasing_dataCollectionId", Integer),
    Column("v_datacollection_summary_phasing_cell_a", Float),
    Column("v_datacollection_summary_phasing_cell_b", Float),
    Column("v_datacollection_summary_phasing_cell_c", Float),
    Column("v_datacollection_summary_phasing_cell_alpha", Float),
    Column("v_datacollection_summary_phasing_cell_beta", Float),
    Column("v_datacollection_summary_phasing_cell_gamma", Float),
    Column(
        "v_datacollection_summary_phasing_anomalous",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("v_datacollection_summary_phasing_autoproc_space_group", String(45)),
    Column(
        "v_datacollection_summary_phasing_autoproc_autoprocId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column(
        "v_datacollection_summary_phasing_autoProcScalingId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("v_datacollection_processingPrograms", String(255)),
    Column(
        "v_datacollection_summary_phasing_autoProcProgramId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column(
        "v_datacollection_processingStatus",
        ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column("v_datacollection_processingStartTime", DateTime),
    Column("v_datacollection_processingEndTime", DateTime),
    Column(
        "v_datacollection_summary_session_sessionId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column(
        "v_datacollection_summary_session_proposalId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("AutoProcIntegration_dataCollectionId", Integer),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column(
        "PhasingStep_phasing_phasingStepType",
        ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("SpaceGroup_spaceGroupShortName", String(45)),
    Column("Protein_proteinId", Integer, server_default=FetchedValue()),
    Column("Protein_acronym", String(45)),
    Column("BLSample_name", String(100)),
    Column("DataCollection_dataCollectionNumber", Integer),
    Column("DataCollection_imagePrefix", String(100)),
)


t_v_datacollection_phasing = Table(
    "v_datacollection_phasing",
    metadata,
    Column("phasingStepId", Integer, server_default=FetchedValue()),
    Column("previousPhasingStepId", Integer),
    Column("phasingAnalysisId", Integer),
    Column("autoProcIntegrationId", Integer, server_default=FetchedValue()),
    Column("dataCollectionId", Integer),
    Column("anomalous", Integer, server_default=FetchedValue()),
    Column("spaceGroup", String(45)),
    Column("autoProcId", Integer, server_default=FetchedValue()),
    Column(
        "phasingStepType",
        ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("method", String(45)),
    Column("solventContent", String(45)),
    Column("enantiomorph", String(45)),
    Column("lowRes", String(45)),
    Column("highRes", String(45)),
    Column("autoProcScalingId", Integer, server_default=FetchedValue()),
    Column("spaceGroupShortName", String(45)),
    Column("processingPrograms", String(255)),
    Column("processingStatus", ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1")),
    Column("phasingPrograms", String(255)),
    Column("phasingStatus", Integer),
    Column("phasingStartTime", DateTime),
    Column("phasingEndTime", DateTime),
    Column("sessionId", Integer),
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("blSampleId", Integer, server_default=FetchedValue()),
    Column("name", String(100)),
    Column("code", String(45)),
    Column("acronym", String(45)),
    Column("proteinId", Integer, server_default=FetchedValue()),
)


t_v_datacollection_phasing_program_run = Table(
    "v_datacollection_phasing_program_run",
    metadata,
    Column("phasingStepId", Integer, server_default=FetchedValue()),
    Column("previousPhasingStepId", Integer),
    Column("phasingAnalysisId", Integer),
    Column("autoProcIntegrationId", Integer, server_default=FetchedValue()),
    Column("dataCollectionId", Integer),
    Column("autoProcId", Integer, server_default=FetchedValue()),
    Column(
        "phasingStepType",
        ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("method", String(45)),
    Column("autoProcScalingId", Integer, server_default=FetchedValue()),
    Column("spaceGroupShortName", String(45)),
    Column("phasingPrograms", String(255)),
    Column("phasingStatus", Integer),
    Column("sessionId", Integer),
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("blSampleId", Integer, server_default=FetchedValue()),
    Column("name", String(100)),
    Column("code", String(45)),
    Column("acronym", String(45)),
    Column("proteinId", Integer, server_default=FetchedValue()),
    Column("phasingProgramAttachmentId", Integer, server_default=FetchedValue()),
    Column(
        "fileType",
        ENUM(
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
    ),
    Column("fileName", String(45)),
    Column("filePath", String(255)),
)


t_v_datacollection_summary = Table(
    "v_datacollection_summary",
    metadata,
    Column(
        "DataCollectionGroup_dataCollectionGroupId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("DataCollectionGroup_blSampleId", Integer),
    Column("DataCollectionGroup_sessionId", Integer),
    Column("DataCollectionGroup_workflowId", Integer),
    Column(
        "DataCollectionGroup_experimentType",
        ENUM(
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
    Column("DataCollectionGroup_startTime", DateTime),
    Column("DataCollectionGroup_endTime", DateTime),
    Column("DataCollectionGroup_comments", String(1024)),
    Column("DataCollectionGroup_actualSampleBarcode", String(45)),
    Column("DataCollectionGroup_xtalSnapshotFullPath", String(255)),
    Column("DataCollectionGroup_crystalClass", String(20)),
    Column("BLSample_blSampleId", Integer, server_default=FetchedValue()),
    Column("BLSample_crystalId", Integer),
    Column("BLSample_name", String(100)),
    Column("BLSample_code", String(45)),
    Column("BLSample_location", String(45)),
    Column("BLSample_blSampleStatus", String(20)),
    Column("BLSample_comments", String(1024)),
    Column("Container_containerId", Integer, server_default=FetchedValue()),
    Column("BLSession_sessionId", Integer, server_default=FetchedValue()),
    Column("BLSession_proposalId", Integer, server_default=FetchedValue()),
    Column("BLSession_protectedData", String(1024)),
    Column("Dewar_dewarId", Integer, server_default=FetchedValue()),
    Column("Dewar_code", String(45)),
    Column("Dewar_storageLocation", String(45)),
    Column("Container_containerType", String(20)),
    Column("Container_code", String(45)),
    Column("Container_capacity", Integer),
    Column("Container_beamlineLocation", String(20)),
    Column("Container_sampleChangerLocation", String(20)),
    Column("Protein_proteinId", Integer, server_default=FetchedValue()),
    Column("Protein_name", String(255)),
    Column("Protein_acronym", String(45)),
    Column("DataCollection_dataCollectionId", Integer, server_default=FetchedValue()),
    Column("DataCollection_dataCollectionGroupId", Integer),
    Column("DataCollection_startTime", DateTime),
    Column("DataCollection_endTime", DateTime),
    Column("DataCollection_runStatus", String(45)),
    Column("DataCollection_numberOfImages", Integer),
    Column("DataCollection_startImageNumber", Integer),
    Column("DataCollection_numberOfPasses", Integer),
    Column("DataCollection_exposureTime", Float),
    Column("DataCollection_imageDirectory", String(255)),
    Column("DataCollection_wavelength", Float),
    Column("DataCollection_resolution", Float),
    Column("DataCollection_detectorDistance", Float),
    Column("DataCollection_xBeam", Float),
    Column("transmission", Float),
    Column("DataCollection_yBeam", Float),
    Column("DataCollection_imagePrefix", String(100)),
    Column("DataCollection_comments", String(1024)),
    Column("DataCollection_xtalSnapshotFullPath1", String(255)),
    Column("DataCollection_xtalSnapshotFullPath2", String(255)),
    Column("DataCollection_xtalSnapshotFullPath3", String(255)),
    Column("DataCollection_xtalSnapshotFullPath4", String(255)),
    Column("DataCollection_phiStart", Float),
    Column("DataCollection_kappaStart", Float),
    Column("DataCollection_omegaStart", Float),
    Column("DataCollection_flux", Float(asdecimal=True)),
    Column("DataCollection_flux_end", Float(asdecimal=True)),
    Column("DataCollection_resolutionAtCorner", Float),
    Column("DataCollection_bestWilsonPlotPath", String(255)),
    Column("DataCollection_dataCollectionNumber", Integer),
    Column("DataCollection_axisRange", Float),
    Column("DataCollection_axisStart", Float),
    Column("DataCollection_axisEnd", Float),
    Column("DataCollection_rotationAxis", ENUM("Omega", "Kappa", "Phi")),
    Column("DataCollection_undulatorGap1", Float),
    Column("DataCollection_undulatorGap2", Float),
    Column("DataCollection_undulatorGap3", Float),
    Column("beamSizeAtSampleX", Float),
    Column("beamSizeAtSampleY", Float),
    Column("DataCollection_slitGapVertical", Float),
    Column("DataCollection_slitGapHorizontal", Float),
    Column("DataCollection_beamShape", String(45)),
    Column("DataCollection_voltage", Float),
    Column("DataCollection_xBeamPix", Float),
    Column("Workflow_workflowTitle", String(255)),
    Column(
        "Workflow_workflowType",
        ENUM(
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
            "MXPressF",
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
    Column("Workflow_status", String(255)),
    Column("Workflow_workflowId", Integer, server_default=FetchedValue()),
    Column("AutoProcIntegration_dataCollectionId", Integer),
    Column("autoProcScalingId", Integer, server_default=FetchedValue()),
    Column("cell_a", Float),
    Column("cell_b", Float),
    Column("cell_c", Float),
    Column("cell_alpha", Float),
    Column("cell_beta", Float),
    Column("cell_gamma", Float),
    Column("anomalous", Integer, server_default=FetchedValue()),
    Column(
        "scalingStatisticsType",
        ENUM("overall", "innerShell", "outerShell"),
        server_default=FetchedValue(),
    ),
    Column("resolutionLimitHigh", Float),
    Column("resolutionLimitLow", Float),
    Column("completeness", Float),
    Column("AutoProc_spaceGroup", String(45)),
    Column("autoProcId", Integer, server_default=FetchedValue()),
    Column("rMerge", Float),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("AutoProcProgram_processingPrograms", String(255)),
    Column(
        "AutoProcProgram_processingStatus",
        ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column("AutoProcProgram_autoProcProgramId", Integer, server_default=FetchedValue()),
    Column("Screening_screeningId", Integer, server_default=FetchedValue()),
    Column("Screening_dataCollectionId", Integer),
    Column("Screening_dataCollectionGroupId", Integer),
    Column("ScreeningOutput_strategySuccess", Integer, server_default=FetchedValue()),
    Column("ScreeningOutput_indexingSuccess", Integer, server_default=FetchedValue()),
    Column("ScreeningOutput_rankingResolution", Float(asdecimal=True)),
    Column("ScreeningOutput_mosaicity", Float),
    Column("ScreeningOutputLattice_spaceGroup", String(45)),
    Column("ScreeningOutputLattice_unitCell_a", Float),
    Column("ScreeningOutputLattice_unitCell_b", Float),
    Column("ScreeningOutputLattice_unitCell_c", Float),
    Column("ScreeningOutputLattice_unitCell_alpha", Float),
    Column("ScreeningOutputLattice_unitCell_beta", Float),
    Column("ScreeningOutputLattice_unitCell_gamma", Float),
    Column("ScreeningOutput_totalExposureTime", Float(asdecimal=True)),
    Column("ScreeningOutput_totalRotationRange", Float(asdecimal=True)),
    Column("ScreeningOutput_totalNumberOfImages", Integer),
    Column("ScreeningStrategySubWedge_exposureTime", Float),
    Column("ScreeningStrategySubWedge_transmission", Float),
    Column("ScreeningStrategySubWedge_oscillationRange", Float),
    Column("ScreeningStrategySubWedge_numberOfImages", Integer),
    Column("ScreeningStrategySubWedge_multiplicity", Float),
    Column("ScreeningStrategySubWedge_completeness", Float),
    Column("ScreeningStrategySubWedge_axisStart", Float),
    Column("Shipping_shippingId", Integer, server_default=FetchedValue()),
    Column("Shipping_shippingName", String(45)),
    Column("Shipping_shippingStatus", String(45)),
    Column("diffractionPlanId", Integer, server_default=FetchedValue()),
    Column(
        "experimentKind",
        ENUM(
            "Default",
            "MXPressE",
            "MXPressF",
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
    Column("observedResolution", Float),
    Column("minimalResolution", Float),
    Column("exposureTime", Float),
    Column("oscillationRange", Float),
    Column("maximalResolution", Float),
    Column("screeningResolution", Float),
    Column("radiationSensitivity", Float),
    Column("anomalousScatterer", String(255)),
    Column("preferredBeamSizeX", Float),
    Column("preferredBeamSizeY", Float),
    Column("preferredBeamDiameter", Float),
    Column("DiffractipnPlan_comments", String(1024)),
    Column("aimedCompleteness", Float(asdecimal=True)),
    Column("aimedIOverSigmaAtHighestRes", Float(asdecimal=True)),
    Column("aimedMultiplicity", Float(asdecimal=True)),
    Column("aimedResolution", Float(asdecimal=True)),
    Column("anomalousData", Integer, server_default=FetchedValue()),
    Column("complexity", String(45)),
    Column("estimateRadiationDamage", Integer, server_default=FetchedValue()),
    Column("forcedSpaceGroup", String(45)),
    Column("requiredCompleteness", Float(asdecimal=True)),
    Column("requiredMultiplicity", Float(asdecimal=True)),
    Column("requiredResolution", Float(asdecimal=True)),
    Column("strategyOption", String(45)),
    Column("kappaStrategyOption", String(45)),
    Column("numberOfPositions", Integer),
    Column("minDimAccrossSpindleAxis", Float(asdecimal=True)),
    Column("maxDimAccrossSpindleAxis", Float(asdecimal=True)),
    Column("radiationSensitivityBeta", Float(asdecimal=True)),
    Column("radiationSensitivityGamma", Float(asdecimal=True)),
    Column("minOscWidth", Float),
    Column("Detector_detectorType", String(255)),
    Column("Detector_detectorManufacturer", String(255)),
    Column("Detector_detectorModel", String(255)),
    Column("Detector_detectorPixelSizeHorizontal", Float),
    Column("Detector_detectorPixelSizeVertical", Float),
    Column("Detector_detectorSerialNumber", String(30)),
    Column("Detector_detectorDistanceMin", Float(asdecimal=True)),
    Column("Detector_detectorDistanceMax", Float(asdecimal=True)),
    Column("Detector_trustedPixelValueRangeLower", Float(asdecimal=True)),
    Column("Detector_trustedPixelValueRangeUpper", Float(asdecimal=True)),
    Column("Detector_sensorThickness", Float),
    Column("Detector_overload", Float),
    Column("Detector_XGeoCorr", String(255)),
    Column("Detector_YGeoCorr", String(255)),
    Column("Detector_detectorMode", String(255)),
    Column("BeamLineSetup_undulatorType1", String(45)),
    Column("BeamLineSetup_undulatorType2", String(45)),
    Column("BeamLineSetup_undulatorType3", String(45)),
    Column("BeamLineSetup_synchrotronName", String(255)),
    Column("BeamLineSetup_synchrotronMode", String(255)),
    Column("BeamLineSetup_polarisation", Float),
    Column("BeamLineSetup_focusingOptic", String(255)),
    Column("BeamLineSetup_beamDivergenceHorizontal", Float),
    Column("BeamLineSetup_beamDivergenceVertical", Float),
    Column("BeamLineSetup_monochromatorType", String(255)),
)


t_v_datacollection_summary_autoprocintegration = Table(
    "v_datacollection_summary_autoprocintegration",
    metadata,
    Column("AutoProcIntegration_dataCollectionId", Integer),
    Column("cell_a", Float),
    Column("cell_b", Float),
    Column("cell_c", Float),
    Column("cell_alpha", Float),
    Column("cell_beta", Float),
    Column("cell_gamma", Float),
    Column("anomalous", Integer, server_default=FetchedValue()),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column(
        "v_datacollection_summary_autoprocintegration_processingPrograms", String(255)
    ),
    Column("AutoProcProgram_autoProcProgramId", Integer, server_default=FetchedValue()),
    Column(
        "v_datacollection_summary_autoprocintegration_processingStatus",
        ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column("AutoProcIntegration_phasing_dataCollectionId", Integer),
    Column(
        "PhasingStep_phasing_phasingStepType",
        ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("SpaceGroup_spaceGroupShortName", String(45)),
    Column("autoProcId", Integer, server_default=FetchedValue()),
    Column("AutoProc_spaceGroup", String(45)),
    Column(
        "scalingStatisticsType",
        ENUM("overall", "innerShell", "outerShell"),
        server_default=FetchedValue(),
    ),
    Column("resolutionLimitHigh", Float),
    Column("resolutionLimitLow", Float),
    Column("rMerge", Float),
    Column("meanIOverSigI", Float),
    Column("ccHalf", Float),
    Column("completeness", Float),
    Column("autoProcScalingId", Integer, server_default=FetchedValue()),
)


t_v_datacollection_summary_datacollectiongroup = Table(
    "v_datacollection_summary_datacollectiongroup",
    metadata,
    Column(
        "DataCollectionGroup_dataCollectionGroupId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("DataCollectionGroup_blSampleId", Integer),
    Column("DataCollectionGroup_sessionId", Integer),
    Column("DataCollectionGroup_workflowId", Integer),
    Column(
        "DataCollectionGroup_experimentType",
        ENUM(
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
    Column("DataCollectionGroup_startTime", DateTime),
    Column("DataCollectionGroup_endTime", DateTime),
    Column("DataCollectionGroup_comments", String(1024)),
    Column("DataCollectionGroup_actualSampleBarcode", String(45)),
    Column("DataCollectionGroup_xtalSnapshotFullPath", String(255)),
    Column("BLSample_blSampleId", Integer, server_default=FetchedValue()),
    Column("BLSample_crystalId", Integer),
    Column("BLSample_name", String(100)),
    Column("BLSample_code", String(45)),
    Column("BLSession_sessionId", Integer, server_default=FetchedValue()),
    Column("BLSession_proposalId", Integer, server_default=FetchedValue()),
    Column("BLSession_protectedData", String(1024)),
    Column("Protein_proteinId", Integer, server_default=FetchedValue()),
    Column("Protein_name", String(255)),
    Column("Protein_acronym", String(45)),
    Column("DataCollection_dataCollectionId", Integer, server_default=FetchedValue()),
    Column("DataCollection_dataCollectionGroupId", Integer),
    Column("DataCollection_startTime", DateTime),
    Column("DataCollection_endTime", DateTime),
    Column("DataCollection_runStatus", String(45)),
    Column("DataCollection_numberOfImages", Integer),
    Column("DataCollection_startImageNumber", Integer),
    Column("DataCollection_numberOfPasses", Integer),
    Column("DataCollection_exposureTime", Float),
    Column("DataCollection_imageDirectory", String(255)),
    Column("DataCollection_wavelength", Float),
    Column("DataCollection_resolution", Float),
    Column("DataCollection_detectorDistance", Float),
    Column("DataCollection_xBeam", Float),
    Column("DataCollection_yBeam", Float),
    Column("DataCollection_comments", String(1024)),
    Column("DataCollection_xtalSnapshotFullPath1", String(255)),
    Column("DataCollection_xtalSnapshotFullPath2", String(255)),
    Column("DataCollection_xtalSnapshotFullPath3", String(255)),
    Column("DataCollection_xtalSnapshotFullPath4", String(255)),
    Column("DataCollection_phiStart", Float),
    Column("DataCollection_kappaStart", Float),
    Column("DataCollection_omegaStart", Float),
    Column("DataCollection_resolutionAtCorner", Float),
    Column("DataCollection_bestWilsonPlotPath", String(255)),
    Column("DataCollection_dataCollectionNumber", Integer),
    Column("DataCollection_axisRange", Float),
    Column("DataCollection_axisStart", Float),
    Column("DataCollection_axisEnd", Float),
    Column("Workflow_workflowTitle", String(255)),
    Column(
        "Workflow_workflowType",
        ENUM(
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
            "MXPressF",
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
    Column("Workflow_status", String(255)),
)


t_v_datacollection_summary_phasing = Table(
    "v_datacollection_summary_phasing",
    metadata,
    Column(
        "v_datacollection_summary_phasing_autoProcIntegrationId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("v_datacollection_summary_phasing_dataCollectionId", Integer),
    Column("v_datacollection_summary_phasing_cell_a", Float),
    Column("v_datacollection_summary_phasing_cell_b", Float),
    Column("v_datacollection_summary_phasing_cell_c", Float),
    Column("v_datacollection_summary_phasing_cell_alpha", Float),
    Column("v_datacollection_summary_phasing_cell_beta", Float),
    Column("v_datacollection_summary_phasing_cell_gamma", Float),
    Column(
        "v_datacollection_summary_phasing_anomalous",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("v_datacollection_summary_phasing_autoproc_space_group", String(45)),
    Column(
        "v_datacollection_summary_phasing_autoproc_autoprocId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column(
        "v_datacollection_summary_phasing_autoProcScalingId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("v_datacollection_summary_phasing_processingPrograms", String(255)),
    Column(
        "v_datacollection_summary_phasing_autoProcProgramId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column(
        "v_datacollection_summary_phasing_processingStatus",
        ENUM("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column(
        "v_datacollection_summary_session_sessionId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column(
        "v_datacollection_summary_session_proposalId",
        Integer,
        server_default=FetchedValue(),
    ),
)


t_v_datacollection_summary_screening = Table(
    "v_datacollection_summary_screening",
    metadata,
    Column("Screening_screeningId", Integer, server_default=FetchedValue()),
    Column("Screening_dataCollectionId", Integer),
    Column("Screening_dataCollectionGroupId", Integer),
    Column("ScreeningOutput_strategySuccess", Integer, server_default=FetchedValue()),
    Column("ScreeningOutput_indexingSuccess", Integer, server_default=FetchedValue()),
    Column("ScreeningOutput_rankingResolution", Float(asdecimal=True)),
    Column(
        "ScreeningOutput_mosaicityEstimated", Integer, server_default=FetchedValue()
    ),
    Column("ScreeningOutput_mosaicity", Float),
    Column("ScreeningOutput_totalExposureTime", Float(asdecimal=True)),
    Column("ScreeningOutput_totalRotationRange", Float(asdecimal=True)),
    Column("ScreeningOutput_totalNumberOfImages", Integer),
    Column("ScreeningOutputLattice_spaceGroup", String(45)),
    Column("ScreeningOutputLattice_unitCell_a", Float),
    Column("ScreeningOutputLattice_unitCell_b", Float),
    Column("ScreeningOutputLattice_unitCell_c", Float),
    Column("ScreeningOutputLattice_unitCell_alpha", Float),
    Column("ScreeningOutputLattice_unitCell_beta", Float),
    Column("ScreeningOutputLattice_unitCell_gamma", Float),
    Column("ScreeningStrategySubWedge_exposureTime", Float),
    Column("ScreeningStrategySubWedge_transmission", Float),
    Column("ScreeningStrategySubWedge_oscillationRange", Float),
    Column("ScreeningStrategySubWedge_numberOfImages", Integer),
    Column("ScreeningStrategySubWedge_multiplicity", Float),
    Column("ScreeningStrategySubWedge_completeness", Float),
    Column("ScreeningStrategySubWedge_axisStart", Float),
    Column("ScreeningStrategySubWedge_axisEnd", Float),
    Column("ScreeningStrategySubWedge_rotationAxis", String(45)),
)


t_v_dewar = Table(
    "v_dewar",
    metadata,
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("shippingId", Integer, server_default=FetchedValue()),
    Column("shippingName", String(45)),
    Column("dewarId", Integer, server_default=FetchedValue()),
    Column("dewarName", String(45)),
    Column("dewarStatus", String(45)),
    Column("proposalCode", String(45)),
    Column("proposalNumber", String(45)),
    Column("creationDate", DateTime),
    Column("shippingType", String(45)),
    Column("barCode", String(45)),
    Column("shippingStatus", String(45)),
    Column("beamLineName", String(45)),
    Column("nbEvents", BigInteger, server_default=FetchedValue()),
    Column("storesin", BigInteger, server_default=FetchedValue()),
    Column("nbSamples", BigInteger, server_default=FetchedValue()),
)


t_v_dewarBeamline = Table(
    "v_dewarBeamline",
    metadata,
    Column("beamLineName", String(45)),
    Column("COUNT(*)", BigInteger, server_default=FetchedValue()),
)


t_v_dewarBeamlineByWeek = Table(
    "v_dewarBeamlineByWeek",
    metadata,
    Column("Week", String(23)),
    Column("ID14", BigInteger, server_default=FetchedValue()),
    Column("ID23", BigInteger, server_default=FetchedValue()),
    Column("ID29", BigInteger, server_default=FetchedValue()),
    Column("BM14", BigInteger, server_default=FetchedValue()),
)


t_v_dewarByWeek = Table(
    "v_dewarByWeek",
    metadata,
    Column("Week", String(23)),
    Column("Dewars Tracked", BigInteger, server_default=FetchedValue()),
    Column("Dewars Non-Tracked", BigInteger, server_default=FetchedValue()),
)


t_v_dewarByWeekTotal = Table(
    "v_dewarByWeekTotal",
    metadata,
    Column("Week", String(23)),
    Column("Dewars Tracked", BigInteger, server_default=FetchedValue()),
    Column("Dewars Non-Tracked", BigInteger, server_default=FetchedValue()),
    Column("Total", BigInteger, server_default=FetchedValue()),
)


t_v_dewarList = Table(
    "v_dewarList",
    metadata,
    Column("proposal", String(90)),
    Column("shippingName", String(45)),
    Column("dewarName", String(45)),
    Column("barCode", String(45)),
    Column("creationDate", String(10)),
    Column("shippingType", String(45)),
    Column("nbEvents", BigInteger, server_default=FetchedValue()),
    Column("dewarStatus", String(45)),
    Column("shippingStatus", String(45)),
    Column("nbSamples", BigInteger, server_default=FetchedValue()),
)


t_v_dewarProposalCode = Table(
    "v_dewarProposalCode",
    metadata,
    Column("proposalCode", String(45)),
    Column("COUNT(*)", BigInteger, server_default=FetchedValue()),
)


t_v_dewarProposalCodeByWeek = Table(
    "v_dewarProposalCodeByWeek",
    metadata,
    Column("Week", String(23)),
    Column("MX", BigInteger, server_default=FetchedValue()),
    Column("FX", BigInteger, server_default=FetchedValue()),
    Column("BM14U", BigInteger, server_default=FetchedValue()),
    Column("BM161", BigInteger, server_default=FetchedValue()),
    Column("BM162", BigInteger, server_default=FetchedValue()),
    Column("Others", BigInteger, server_default=FetchedValue()),
)


t_v_dewar_summary = Table(
    "v_dewar_summary",
    metadata,
    Column("shippingName", String(45)),
    Column("deliveryAgent_agentName", String(45)),
    Column("deliveryAgent_shippingDate", Date),
    Column("deliveryAgent_deliveryDate", Date),
    Column("deliveryAgent_agentCode", String(45)),
    Column("deliveryAgent_flightCode", String(45)),
    Column("shippingStatus", String(45)),
    Column("bltimeStamp", DateTime),
    Column("laboratoryId", Integer),
    Column("isStorageShipping", Integer, server_default=FetchedValue()),
    Column("creationDate", DateTime),
    Column("Shipping_comments", String(255)),
    Column("sendingLabContactId", Integer),
    Column("returnLabContactId", Integer),
    Column("returnCourier", String(45)),
    Column("dateOfShippingToUser", DateTime),
    Column("shippingType", String(45)),
    Column("dewarId", Integer, server_default=FetchedValue()),
    Column("shippingId", Integer),
    Column("dewarCode", String(45)),
    Column("comments", String),
    Column("storageLocation", String(45)),
    Column("dewarStatus", String(45)),
    Column("isStorageDewar", Integer, server_default=FetchedValue()),
    Column("barCode", String(45)),
    Column("firstExperimentId", Integer),
    Column("customsValue", Integer),
    Column("transportValue", Integer),
    Column("trackingNumberToSynchrotron", String(30)),
    Column("trackingNumberFromSynchrotron", String(30)),
    Column("type", ENUM("Dewar", "Toolbox"), server_default=FetchedValue()),
    Column("isReimbursed", Integer, server_default=FetchedValue()),
    Column("sessionId", Integer, server_default=FetchedValue()),
    Column("beamlineName", String(45)),
    Column("sessionStartDate", DateTime),
    Column("sessionEndDate", DateTime),
    Column("beamLineOperator", String(255)),
    Column("nbReimbDewars", Integer),
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("containerId", Integer, server_default=FetchedValue()),
    Column("containerType", String(20)),
    Column("capacity", Integer),
    Column("beamlineLocation", String(20)),
    Column("sampleChangerLocation", String(20)),
    Column("containerStatus", String(45)),
    Column("containerCode", String(45)),
)


t_v_em_2dclassification = Table(
    "v_em_2dclassification",
    metadata,
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("sessionId", Integer, server_default=FetchedValue()),
    Column("imageDirectory", String(255)),
    Column("particlePickerId", Integer, server_default=FetchedValue()),
    Column("particleClassificationGroupId", Integer, server_default=FetchedValue()),
    Column("particleClassificationId", Integer, server_default=FetchedValue()),
    Column("classNumber", Integer),
    Column("classImageFullPath", String(255)),
)


t_v_em_classification = Table(
    "v_em_classification",
    metadata,
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("sessionId", Integer, server_default=FetchedValue()),
    Column("imageDirectory", String(255)),
    Column("particlePickerId", Integer, server_default=FetchedValue()),
    Column("numberOfParticles", Integer),
    Column("particleClassificationGroupId", Integer, server_default=FetchedValue()),
    Column("particleClassificationId", Integer, server_default=FetchedValue()),
    Column("classNumber", Integer),
    Column("classImageFullPath", String(255)),
    Column("particlesPerClass", Integer),
    Column("classDistribution", Float),
    Column("rotationAccuracy", Float),
    Column("translationAccuracy", Float),
    Column("estimatedResolution", Float),
    Column("overallFourierCompleteness", Float),
)


t_v_em_movie = Table(
    "v_em_movie",
    metadata,
    Column("Movie_movieId", Integer, server_default=FetchedValue()),
    Column("Movie_dataCollectionId", Integer),
    Column("Movie_movieNumber", Integer),
    Column("Movie_movieFullPath", String(255)),
    Column("Movie_positionX", String(45)),
    Column("Movie_positionY", String(45)),
    Column("Movie_micrographFullPath", String(255)),
    Column("Movie_micrographSnapshotFullPath", String(255)),
    Column("Movie_xmlMetaDataFullPath", String(255)),
    Column("Movie_dosePerImage", String(45)),
    Column("Movie_createdTimeStamp", DateTime, server_default=FetchedValue()),
    Column(
        "MotionCorrection_motionCorrectionId", Integer, server_default=FetchedValue()
    ),
    Column("MotionCorrection_movieId", Integer),
    Column("MotionCorrection_firstFrame", String(45)),
    Column("MotionCorrection_lastFrame", String(45)),
    Column("MotionCorrection_dosePerFrame", String(45)),
    Column("MotionCorrection_doseWeight", String(45)),
    Column("MotionCorrection_totalMotion", String(45)),
    Column("MotionCorrection_averageMotionPerFrame", String(45)),
    Column("MotionCorrection_driftPlotFullPath", String(512)),
    Column("MotionCorrection_micrographFullPath", String(512)),
    Column("MotionCorrection_micrographSnapshotFullPath", String(512)),
    Column("MotionCorrection_correctedDoseMicrographFullPath", String(512)),
    Column("MotionCorrection_patchesUsed", String(45)),
    Column("MotionCorrection_logFileFullPath", String(512)),
    Column("CTF_CTFid", Integer, server_default=FetchedValue()),
    Column("CTF_motionCorrectionId", Integer),
    Column("CTF_spectraImageThumbnailFullPath", String(512)),
    Column("CTF_spectraImageFullPath", String(512)),
    Column("CTF_defocusU", String(45)),
    Column("CTF_defocusV", String(45)),
    Column("CTF_angle", String(45)),
    Column("CTF_crossCorrelationCoefficient", String(45)),
    Column("CTF_resolutionLimit", String(45)),
    Column("CTF_estimatedBfactor", String(45)),
    Column("CTF_logFilePath", String(512)),
    Column("CTF_createdTimeStamp", DateTime, server_default=FetchedValue()),
    Column("Proposal_proposalId", Integer, server_default=FetchedValue()),
    Column("BLSession_sessionId", Integer, server_default=FetchedValue()),
)


t_v_em_stats = Table(
    "v_em_stats",
    metadata,
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("sessionId", Integer, server_default=FetchedValue()),
    Column("imageDirectory", String(255)),
    Column("movieId", Integer, server_default=FetchedValue()),
    Column("movieNumber", Integer),
    Column("createdTimeStamp", DateTime, server_default=FetchedValue()),
    Column("motionCorrectionId", Integer, server_default=FetchedValue()),
    Column("dataCollectionId", Integer, server_default=FetchedValue()),
    Column("totalMotion", String(45)),
    Column("averageMotionPerFrame", String(45)),
    Column("lastFrame", String(45)),
    Column("dosePerFrame", String(45)),
    Column("defocusU", String(45)),
    Column("defocusV", String(45)),
    Column("resolutionLimit", String(45)),
    Column("estimatedBfactor", String(45)),
    Column("angle", String(45)),
)


t_v_energyScan = Table(
    "v_energyScan",
    metadata,
    Column("energyScanId", Integer, server_default=FetchedValue()),
    Column("sessionId", Integer),
    Column("blSampleId", Integer),
    Column("fluorescenceDetector", String(255)),
    Column("scanFileFullPath", String(255)),
    Column("choochFileFullPath", String(255)),
    Column("jpegChoochFileFullPath", String(255)),
    Column("element", String(45)),
    Column("startEnergy", Float),
    Column("endEnergy", Float),
    Column("transmissionFactor", Float),
    Column("exposureTime", Float),
    Column("synchrotronCurrent", Float),
    Column("temperature", Float),
    Column("peakEnergy", Float),
    Column("peakFPrime", Float),
    Column("peakFDoublePrime", Float),
    Column("inflectionEnergy", Float),
    Column("inflectionFPrime", Float),
    Column("inflectionFDoublePrime", Float),
    Column("xrayDose", Float),
    Column("startTime", DateTime),
    Column("endTime", DateTime),
    Column("edgeEnergy", String(255)),
    Column("filename", String(255)),
    Column("beamSizeVertical", Float),
    Column("beamSizeHorizontal", Float),
    Column("crystalClass", String(20)),
    Column("comments", String(1024)),
    Column("flux", Float(asdecimal=True)),
    Column("flux_end", Float(asdecimal=True)),
    Column("remoteEnergy", Float),
    Column("remoteFPrime", Float),
    Column("remoteFDoublePrime", Float),
    Column("BLSample_sampleId", Integer, server_default=FetchedValue()),
    Column("name", String(100)),
    Column("code", String(45)),
    Column("acronym", String(45)),
    Column("BLSession_proposalId", Integer, server_default=FetchedValue()),
)


t_v_hour = Table("v_hour", metadata, Column("num", String(18)))


t_v_logonByHour = Table(
    "v_logonByHour",
    metadata,
    Column("Hour", String(7)),
    Column("Distinct logins", BigInteger, server_default=FetchedValue()),
    Column("Total logins", BigInteger, server_default=FetchedValue()),
)


t_v_logonByMonthDay = Table(
    "v_logonByMonthDay",
    metadata,
    Column("Day", String(5)),
    Column("Distinct logins", BigInteger, server_default=FetchedValue()),
    Column("Total logins", BigInteger, server_default=FetchedValue()),
)


t_v_logonByWeek = Table(
    "v_logonByWeek",
    metadata,
    Column("Week", String(23)),
    Column("Distinct logins", BigInteger, server_default=FetchedValue()),
    Column("Total logins", BigInteger, server_default=FetchedValue()),
)


t_v_logonByWeekDay = Table(
    "v_logonByWeekDay",
    metadata,
    Column("Day", String(64)),
    Column("Distinct logins", BigInteger, server_default=FetchedValue()),
    Column("Total logins", BigInteger, server_default=FetchedValue()),
)


t_v_monthDay = Table("v_monthDay", metadata, Column("num", String(10)))


t_v_mx_autoprocessing_stats = Table(
    "v_mx_autoprocessing_stats",
    metadata,
    Column("autoProcScalingStatisticsId", Integer, server_default=FetchedValue()),
    Column("autoProcScalingId", Integer),
    Column(
        "scalingStatisticsType",
        ENUM("overall", "innerShell", "outerShell"),
        server_default=FetchedValue(),
    ),
    Column("resolutionLimitLow", Float),
    Column("resolutionLimitHigh", Float),
    Column("rMerge", Float),
    Column("rMeasWithinIPlusIMinus", Float),
    Column("rMeasAllIPlusIMinus", Float),
    Column("rPimWithinIPlusIMinus", Float),
    Column("rPimAllIPlusIMinus", Float),
    Column("fractionalPartialBias", Float),
    Column("nTotalObservations", Integer),
    Column("nTotalUniqueObservations", Integer),
    Column("meanIOverSigI", Float),
    Column("completeness", Float),
    Column("multiplicity", Float),
    Column("anomalousCompleteness", Float),
    Column("anomalousMultiplicity", Float),
    Column("recordTimeStamp", DateTime),
    Column("anomalous", Integer, server_default=FetchedValue()),
    Column("ccHalf", Float),
    Column("ccAno", Float),
    Column("sigAno", String(45)),
    Column("ISA", String(45)),
    Column("dataCollectionId", Integer, server_default=FetchedValue()),
    Column("strategySubWedgeOrigId", Integer),
    Column("detectorId", Integer),
    Column("blSubSampleId", Integer),
    Column("dataCollectionNumber", Integer),
    Column("startTime", DateTime),
    Column("endTime", DateTime),
    Column("sessionId", Integer, server_default=FetchedValue()),
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("beamLineName", String(45)),
)


t_v_mx_experiment_stats = Table(
    "v_mx_experiment_stats",
    metadata,
    Column("startTime", DateTime),
    Column("Images", Integer),
    Column("Transmission", Float),
    Column("Res. (corner)", Float),
    Column("En. (Wave.)", Float),
    Column("Omega start (total)", Float),
    Column("Exposure Time", Float),
    Column("Flux", Float(asdecimal=True)),
    Column("Flux End", Float(asdecimal=True)),
    Column("Detector Distance", Float),
    Column("X Beam", Float),
    Column("Y Beam", Float),
    Column("Kappa", Float),
    Column("Phi", Float),
    Column("Axis Start", Float),
    Column("Axis End", Float),
    Column("Axis Range", Float),
    Column("Beam Size X", Float),
    Column("Beam Size Y", Float),
    Column("beamLineName", String(45)),
    Column("comments", String(1024)),
    Column("proposalNumber", String(45)),
)


t_v_mx_sample = Table(
    "v_mx_sample",
    metadata,
    Column("BLSample_blSampleId", Integer, server_default=FetchedValue()),
    Column("BLSample_diffractionPlanId", Integer),
    Column("BLSample_crystalId", Integer),
    Column("BLSample_containerId", Integer),
    Column("BLSample_name", String(100)),
    Column("BLSample_code", String(45)),
    Column("BLSample_location", String(45)),
    Column("BLSample_holderLength", Float(asdecimal=True)),
    Column("BLSample_loopLength", Float(asdecimal=True)),
    Column("BLSample_loopType", String(45)),
    Column("BLSample_wireWidth", Float(asdecimal=True)),
    Column("BLSample_comments", String(1024)),
    Column("BLSample_completionStage", String(45)),
    Column("BLSample_structureStage", String(45)),
    Column("BLSample_publicationStage", String(45)),
    Column("BLSample_publicationComments", String(255)),
    Column("BLSample_blSampleStatus", String(20)),
    Column("BLSample_isInSampleChanger", Integer),
    Column("BLSample_lastKnownCenteringPosition", String(255)),
    Column("BLSample_recordTimeStamp", DateTime, server_default=FetchedValue()),
    Column("BLSample_SMILES", String(400)),
    Column("Protein_proteinId", Integer, server_default=FetchedValue()),
    Column("Protein_name", String(255)),
    Column("Protein_acronym", String(45)),
    Column("Protein_proteinType", String(45)),
    Column("Protein_proposalId", Integer, server_default=FetchedValue()),
    Column("Person_personId", Integer, server_default=FetchedValue()),
    Column("Person_familyName", String(100)),
    Column("Person_givenName", String(45)),
    Column("Person_emailAddress", String(60)),
    Column("Container_containerId", Integer, server_default=FetchedValue()),
    Column("Container_code", String(45)),
    Column("Container_containerType", String(20)),
    Column("Container_containerStatus", String(45)),
    Column("Container_beamlineLocation", String(20)),
    Column("Container_sampleChangerLocation", String(20)),
    Column("Dewar_code", String(45)),
    Column("Dewar_dewarId", Integer, server_default=FetchedValue()),
    Column("Dewar_storageLocation", String(45)),
    Column("Dewar_dewarStatus", String(45)),
    Column("Dewar_barCode", String(45)),
    Column("Shipping_shippingId", Integer, server_default=FetchedValue()),
    Column("sessionId", Integer, server_default=FetchedValue()),
    Column("BLSession_startDate", DateTime),
    Column("BLSession_beamLineName", String(45)),
)


t_v_phasing = Table(
    "v_phasing",
    metadata,
    Column("BLSample_blSampleId", Integer, server_default=FetchedValue()),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("AutoProcIntegration_dataCollectionId", Integer),
    Column("AutoProcIntegration_autoProcProgramId", Integer),
    Column("AutoProcIntegration_startImageNumber", Integer),
    Column("AutoProcIntegration_endImageNumber", Integer),
    Column("AutoProcIntegration_refinedDetectorDistance", Float),
    Column("AutoProcIntegration_refinedXBeam", Float),
    Column("AutoProcIntegration_refinedYBeam", Float),
    Column("AutoProcIntegration_rotationAxisX", Float),
    Column("AutoProcIntegration_rotationAxisY", Float),
    Column("AutoProcIntegration_rotationAxisZ", Float),
    Column("AutoProcIntegration_beamVectorX", Float),
    Column("AutoProcIntegration_beamVectorY", Float),
    Column("AutoProcIntegration_beamVectorZ", Float),
    Column("AutoProcIntegration_cell_a", Float),
    Column("AutoProcIntegration_cell_b", Float),
    Column("AutoProcIntegration_cell_c", Float),
    Column("AutoProcIntegration_cell_alpha", Float),
    Column("AutoProcIntegration_cell_beta", Float),
    Column("AutoProcIntegration_cell_gamma", Float),
    Column("AutoProcIntegration_recordTimeStamp", DateTime),
    Column("AutoProcIntegration_anomalous", Integer, server_default=FetchedValue()),
    Column("SpaceGroup_spaceGroupId", Integer, server_default=FetchedValue()),
    Column("SpaceGroup_geometryClassnameId", Integer),
    Column("SpaceGroup_spaceGroupNumber", Integer),
    Column("SpaceGroup_spaceGroupShortName", String(45)),
    Column("SpaceGroup_spaceGroupName", String(45)),
    Column("SpaceGroup_bravaisLattice", String(45)),
    Column("SpaceGroup_bravaisLatticeName", String(45)),
    Column("SpaceGroup_pointGroup", String(45)),
    Column("SpaceGroup_MX_used", Integer, server_default=FetchedValue()),
    Column("PhasingStep_phasingStepId", Integer, server_default=FetchedValue()),
    Column("PhasingStep_previousPhasingStepId", Integer),
    Column("PhasingStep_programRunId", Integer),
    Column("PhasingStep_spaceGroupId", Integer),
    Column("PhasingStep_autoProcScalingId", Integer),
    Column("PhasingStep_phasingAnalysisId", Integer),
    Column(
        "PhasingStep_phasingStepType",
        ENUM(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("PhasingStep_method", String(45)),
    Column("PhasingStep_solventContent", String(45)),
    Column("PhasingStep_enantiomorph", String(45)),
    Column("PhasingStep_lowRes", String(45)),
    Column("PhasingStep_highRes", String(45)),
    Column("PhasingStep_recordTimeStamp", DateTime, server_default=FetchedValue()),
    Column("DataCollection_dataCollectionId", Integer, server_default=FetchedValue()),
    Column("DataCollection_dataCollectionGroupId", Integer),
    Column("DataCollection_strategySubWedgeOrigId", Integer),
    Column("DataCollection_detectorId", Integer),
    Column("DataCollection_blSubSampleId", Integer),
    Column("DataCollection_dataCollectionNumber", Integer),
    Column("DataCollection_startTime", DateTime),
    Column("DataCollection_endTime", DateTime),
    Column("DataCollection_runStatus", String(45)),
    Column("DataCollection_axisStart", Float),
    Column("DataCollection_axisEnd", Float),
    Column("DataCollection_axisRange", Float),
    Column("DataCollection_overlap", Float),
    Column("DataCollection_numberOfImages", Integer),
    Column("DataCollection_startImageNumber", Integer),
    Column("DataCollection_numberOfPasses", Integer),
    Column("DataCollection_exposureTime", Float),
    Column("DataCollection_imageDirectory", String(255)),
    Column("DataCollection_imagePrefix", String(100)),
    Column("DataCollection_imageSuffix", String(45)),
    Column("DataCollection_fileTemplate", String(255)),
    Column("DataCollection_wavelength", Float),
    Column("DataCollection_resolution", Float),
    Column("DataCollection_detectorDistance", Float),
    Column("DataCollection_xBeam", Float),
    Column("DataCollection_yBeam", Float),
    Column("DataCollection_xBeamPix", Float),
    Column("DataCollection_yBeamPix", Float),
    Column("DataCollection_comments", String(1024)),
    Column("DataCollection_printableForReport", Integer, server_default=FetchedValue()),
    Column("DataCollection_slitGapVertical", Float),
    Column("DataCollection_slitGapHorizontal", Float),
    Column("DataCollection_transmission", Float),
    Column("DataCollection_synchrotronMode", String(20)),
    Column("DataCollection_xtalSnapshotFullPath1", String(255)),
    Column("DataCollection_xtalSnapshotFullPath2", String(255)),
    Column("DataCollection_xtalSnapshotFullPath3", String(255)),
    Column("DataCollection_xtalSnapshotFullPath4", String(255)),
    Column("DataCollection_rotationAxis", ENUM("Omega", "Kappa", "Phi")),
    Column("DataCollection_phiStart", Float),
    Column("DataCollection_kappaStart", Float),
    Column("DataCollection_omegaStart", Float),
    Column("DataCollection_resolutionAtCorner", Float),
    Column("DataCollection_detector2Theta", Float),
    Column("DataCollection_undulatorGap1", Float),
    Column("DataCollection_undulatorGap2", Float),
    Column("DataCollection_undulatorGap3", Float),
    Column("DataCollection_beamSizeAtSampleX", Float),
    Column("DataCollection_beamSizeAtSampleY", Float),
    Column("DataCollection_centeringMethod", String(255)),
    Column("DataCollection_averageTemperature", Float),
    Column("DataCollection_actualCenteringPosition", String(255)),
    Column("DataCollection_beamShape", String(45)),
    Column("DataCollection_flux", Float(asdecimal=True)),
    Column("DataCollection_flux_end", Float(asdecimal=True)),
    Column("DataCollection_totalAbsorbedDose", Float(asdecimal=True)),
    Column("DataCollection_bestWilsonPlotPath", String(255)),
    Column("DataCollection_imageQualityIndicatorsPlotPath", String(512)),
    Column("DataCollection_imageQualityIndicatorsCSVPath", String(512)),
    Column(
        "PhasingProgramRun_phasingProgramRunId", Integer, server_default=FetchedValue()
    ),
    Column("PhasingProgramRun_phasingCommandLine", String(255)),
    Column("PhasingProgramRun_phasingPrograms", String(255)),
    Column("PhasingProgramRun_phasingStatus", Integer),
    Column("PhasingProgramRun_phasingMessage", String(255)),
    Column("PhasingProgramRun_phasingStartTime", DateTime),
    Column("PhasingProgramRun_phasingEndTime", DateTime),
    Column("PhasingProgramRun_phasingEnvironment", String(255)),
    Column("PhasingProgramRun_phasingDirectory", String(255)),
    Column(
        "PhasingProgramRun_recordTimeStamp", DateTime, server_default=FetchedValue()
    ),
    Column("Protein_proteinId", Integer, server_default=FetchedValue()),
    Column("BLSession_sessionId", Integer, server_default=FetchedValue()),
    Column("BLSession_proposalId", Integer, server_default=FetchedValue()),
    Column(
        "PhasingStatistics_phasingStatisticsId", Integer, server_default=FetchedValue()
    ),
    Column(
        "PhasingStatistics_metric",
        ENUM(
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
    ),
    Column("PhasingStatistics_statisticsValue", Float(asdecimal=True)),
)


t_v_sample = Table(
    "v_sample",
    metadata,
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("shippingId", Integer, server_default=FetchedValue()),
    Column("dewarId", Integer, server_default=FetchedValue()),
    Column("containerId", Integer, server_default=FetchedValue()),
    Column("blSampleId", Integer, server_default=FetchedValue()),
    Column("proposalCode", String(45)),
    Column("proposalNumber", String(45)),
    Column("creationDate", DateTime),
    Column("shippingType", String(45)),
    Column("barCode", String(45)),
    Column("shippingStatus", String(45)),
)


t_v_sampleByWeek = Table(
    "v_sampleByWeek",
    metadata,
    Column("Week", String(23)),
    Column("Samples", BigInteger),
)


t_v_saxs_datacollection = Table(
    "v_saxs_datacollection",
    metadata,
    Column("Subtraction_subtractionId", Integer, server_default=FetchedValue()),
    Column("MeasurementToDataCollection_dataCollectionId", Integer),
    Column("MeasurementToDataCollection_dataCollectionOrder", Integer),
    Column(
        "MeasurementToDataCollection_measurementToDataCollectionId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("Specimen_specimenId", Integer, server_default=FetchedValue()),
    Column("Measurement_code", String(100)),
    Column("Measurement_measurementId", Integer, server_default=FetchedValue()),
    Column("Buffer_bufferId", Integer, server_default=FetchedValue()),
    Column("Buffer_proposalId", Integer, server_default=FetchedValue()),
    Column("Buffer_safetyLevelId", Integer),
    Column("Buffer_name", String(45)),
    Column("Buffer_acronym", String(45)),
    Column("Buffer_pH", String(45)),
    Column("Buffer_composition", String(45)),
    Column("Buffer_comments", String(512)),
    Column("Macromolecule_macromoleculeId", Integer, server_default=FetchedValue()),
    Column("Macromolecule_proposalId", Integer),
    Column("Macromolecule_safetyLevelId", Integer),
    Column("Macromolecule_name", String(45)),
    Column("Macromolecule_acronym", String(45)),
    Column("Macromolecule_extintionCoefficient", String(45)),
    Column("Macromolecule_molecularMass", String(45)),
    Column("Macromolecule_sequence", String(1000)),
    Column("Macromolecule_contactsDescriptionFilePath", String(255)),
    Column("Macromolecule_symmetry", String(45)),
    Column("Macromolecule_comments", String(1024)),
    Column("Macromolecule_refractiveIndex", String(45)),
    Column("Macromolecule_solventViscosity", String(45)),
    Column("Macromolecule_creationDate", DateTime),
    Column("Specimen_experimentId", Integer),
    Column("Specimen_bufferId", Integer),
    Column("Specimen_samplePlatePositionId", Integer),
    Column("Specimen_safetyLevelId", Integer),
    Column("Specimen_stockSolutionId", Integer),
    Column("Specimen_code", String(255)),
    Column("Specimen_concentration", String(45)),
    Column("Specimen_volume", String(45)),
    Column("Specimen_comments", String(5120)),
    Column(
        "SamplePlatePosition_samplePlatePositionId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("SamplePlatePosition_samplePlateId", Integer),
    Column("SamplePlatePosition_rowNumber", Integer),
    Column("SamplePlatePosition_columnNumber", Integer),
    Column("SamplePlatePosition_volume", String(45)),
    Column("samplePlateId", Integer, server_default=FetchedValue()),
    Column("experimentId", Integer),
    Column("plateGroupId", Integer),
    Column("plateTypeId", Integer),
    Column("instructionSetId", Integer),
    Column("SamplePlate_boxId", Integer),
    Column("SamplePlate_name", String(45)),
    Column("SamplePlate_slotPositionRow", String(45)),
    Column("SamplePlate_slotPositionColumn", String(45)),
    Column("SamplePlate_storageTemperature", String(45)),
    Column("Experiment_experimentId", Integer, server_default=FetchedValue()),
    Column("Experiment_sessionId", Integer),
    Column("Experiment_proposalId", Integer),
    Column("Experiment_name", String(255)),
    Column("Experiment_creationDate", DateTime),
    Column("Experiment_experimentType", String(128)),
    Column("Experiment_sourceFilePath", String(256)),
    Column("Experiment_dataAcquisitionFilePath", String(256)),
    Column("Experiment_status", String(45)),
    Column("Experiment_comments", String(512)),
    Column("Measurement_priorityLevelId", Integer),
    Column("Measurement_exposureTemperature", String(45)),
    Column("Measurement_viscosity", String(45)),
    Column("Measurement_flow", Integer),
    Column("Measurement_extraFlowTime", String(45)),
    Column("Measurement_volumeToLoad", String(45)),
    Column("Measurement_waitTime", String(45)),
    Column("Measurement_transmission", String(45)),
    Column("Measurement_comments", String(512)),
    Column("Measurement_imageDirectory", String(512)),
    Column("Run_runId", Integer, server_default=FetchedValue()),
    Column("Run_timePerFrame", String(45)),
    Column("Run_timeStart", String(45)),
    Column("Run_timeEnd", String(45)),
    Column("Run_storageTemperature", String(45)),
    Column("Run_exposureTemperature", String(45)),
    Column("Run_spectrophotometer", String(45)),
    Column("Run_energy", String(45)),
    Column("Run_creationDate", DateTime),
    Column("Run_frameAverage", String(45)),
    Column("Run_frameCount", String(45)),
    Column("Run_transmission", String(45)),
    Column("Run_beamCenterX", String(45)),
    Column("Run_beamCenterY", String(45)),
    Column("Run_pixelSizeX", String(45)),
    Column("Run_pixelSizeY", String(45)),
    Column("Run_radiationRelative", String(45)),
    Column("Run_radiationAbsolute", String(45)),
    Column("Run_normalization", String(45)),
    Column("Merge_mergeId", Integer, server_default=FetchedValue()),
    Column("Merge_measurementId", Integer),
    Column("Merge_frameListId", Integer),
    Column("Merge_discardedFrameNameList", String(1024)),
    Column("Merge_averageFilePath", String(255)),
    Column("Merge_framesCount", String(45)),
    Column("Merge_framesMerge", String(45)),
    Column("Merge_creationDate", DateTime),
    Column("Subtraction_dataCollectionId", Integer),
    Column("Subtraction_rg", String(45)),
    Column("Subtraction_rgStdev", String(45)),
    Column("Subtraction_I0", String(45)),
    Column("Subtraction_I0Stdev", String(45)),
    Column("Subtraction_firstPointUsed", String(45)),
    Column("Subtraction_lastPointUsed", String(45)),
    Column("Subtraction_quality", String(45)),
    Column("Subtraction_isagregated", String(45)),
    Column("Subtraction_concentration", String(45)),
    Column("Subtraction_gnomFilePath", String(255)),
    Column("Subtraction_rgGuinier", String(45)),
    Column("Subtraction_rgGnom", String(45)),
    Column("Subtraction_dmax", String(45)),
    Column("Subtraction_total", String(45)),
    Column("Subtraction_volume", String(45)),
    Column("Subtraction_creationTime", DateTime),
    Column("Subtraction_kratkyFilePath", String(255)),
    Column("Subtraction_scatteringFilePath", String(255)),
    Column("Subtraction_guinierFilePath", String(255)),
    Column("Subtraction_substractedFilePath", String(255)),
    Column("Subtraction_gnomFilePathOutput", String(255)),
    Column("Subtraction_sampleOneDimensionalFiles", Integer),
    Column("Subtraction_bufferOnedimensionalFiles", Integer),
    Column("Subtraction_sampleAverageFilePath", String(255)),
    Column("Subtraction_bufferAverageFilePath", String(255)),
)


t_v_session = Table(
    "v_session",
    metadata,
    Column("sessionId", Integer, server_default=FetchedValue()),
    Column("expSessionPk", Integer),
    Column("beamLineSetupId", Integer),
    Column("proposalId", Integer, server_default=FetchedValue()),
    Column("projectCode", String(45)),
    Column("BLSession_startDate", DateTime),
    Column("BLSession_endDate", DateTime),
    Column("beamLineName", String(45)),
    Column("scheduled", Integer),
    Column("nbShifts", Integer),
    Column("comments", String(2000)),
    Column("beamLineOperator", String(255)),
    Column("visit_number", Integer, server_default=FetchedValue()),
    Column("bltimeStamp", DateTime, server_default=FetchedValue()),
    Column("usedFlag", Integer),
    Column("sessionTitle", String(255)),
    Column("structureDeterminations", Float),
    Column("dewarTransport", Float),
    Column("databackupFrance", Float),
    Column("databackupEurope", Float),
    Column("operatorSiteNumber", String(10)),
    Column("BLSession_lastUpdate", DateTime, server_default=FetchedValue()),
    Column("BLSession_protectedData", String(1024)),
    Column("Proposal_title", String(200)),
    Column("Proposal_proposalCode", String(45)),
    Column("Proposal_ProposalNumber", String(45)),
    Column("Proposal_ProposalType", String(2)),
    Column("Person_personId", Integer, server_default=FetchedValue()),
    Column("Person_familyName", String(100)),
    Column("Person_givenName", String(45)),
    Column("Person_emailAddress", String(60)),
)


t_v_tracking_shipment_history = Table(
    "v_tracking_shipment_history",
    metadata,
    Column("Dewar_dewarId", Integer, server_default=FetchedValue()),
    Column("Dewar_code", String(45)),
    Column("Dewar_comments", String),
    Column("Dewar_dewarStatus", String(45)),
    Column("Dewar_barCode", String(45)),
    Column("Dewar_firstExperimentId", Integer),
    Column("Dewar_trackingNumberToSynchrotron", String(30)),
    Column("Dewar_trackingNumberFromSynchrotron", String(30)),
    Column("Dewar_type", ENUM("Dewar", "Toolbox"), server_default=FetchedValue()),
    Column("Shipping_shippingId", Integer, server_default=FetchedValue()),
    Column("Shipping_proposalId", Integer, server_default=FetchedValue()),
    Column("Shipping_shippingName", String(45)),
    Column("deliveryAgent_agentName", String(45)),
    Column("Shipping_deliveryAgent_shippingDate", Date),
    Column("Shipping_deliveryAgent_deliveryDate", Date),
    Column("Shipping_shippingStatus", String(45)),
    Column("Shipping_returnCourier", String(45)),
    Column("Shipping_dateOfShippingToUser", DateTime),
    Column(
        "DewarTransportHistory_DewarTransportHistoryId",
        Integer,
        server_default=FetchedValue(),
    ),
    Column("DewarTransportHistory_dewarStatus", String(45)),
    Column("DewarTransportHistory_storageLocation", String(45)),
    Column("DewarTransportHistory_arrivalDate", DateTime),
)


t_v_week = Table("v_week", metadata, Column("num", String(7)))


t_v_weekDay = Table("v_weekDay", metadata, Column("day", String(10)))


t_v_xfeFluorescenceSpectrum = Table(
    "v_xfeFluorescenceSpectrum",
    metadata,
    Column("xfeFluorescenceSpectrumId", Integer, server_default=FetchedValue()),
    Column("sessionId", Integer),
    Column("blSampleId", Integer),
    Column("fittedDataFileFullPath", String(255)),
    Column("scanFileFullPath", String(255)),
    Column("jpegScanFileFullPath", String(255)),
    Column("startTime", DateTime),
    Column("endTime", DateTime),
    Column("filename", String(255)),
    Column("energy", Float),
    Column("exposureTime", Float),
    Column("beamTransmission", Float),
    Column("annotatedPymcaXfeSpectrum", String(255)),
    Column("beamSizeVertical", Float),
    Column("beamSizeHorizontal", Float),
    Column("crystalClass", String(20)),
    Column("comments", String(1024)),
    Column("flux", Float(asdecimal=True)),
    Column("flux_end", Float(asdecimal=True)),
    Column("workingDirectory", String(512)),
    Column("BLSample_sampleId", Integer, server_default=FetchedValue()),
    Column("BLSession_proposalId", Integer, server_default=FetchedValue()),
)
