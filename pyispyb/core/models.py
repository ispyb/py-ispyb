# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


from pyispyb.app.extensions import db


class AbInitioModel(db.Model):
    __tablename__ = 'AbInitioModel'

    abInitioModelId = db.Column(db.Integer, primary_key=True)
    modelListId = db.Column(db.ForeignKey('ModelList.modelListId'), index=True)
    averagedModelId = db.Column(db.ForeignKey('Model.modelId'), index=True)
    rapidShapeDeterminationModelId = db.Column(
        db.ForeignKey('Model.modelId'), index=True)
    shapeDeterminationModelId = db.Column(
        db.ForeignKey('Model.modelId'), index=True)
    comments = db.Column(db.String(512))
    creationTime = db.Column(db.DateTime)

    Model = db.relationship(
        'Model', primaryjoin='AbInitioModel.averagedModelId == Model.modelId')
    ModelList = db.relationship(
        'ModelList',
        primaryjoin='AbInitioModel.modelListId == ModelList.modelListId')
    Model1 = db.relationship(
        'Model',
        primaryjoin='AbInitioModel.rapidShapeDeterminationModelId == Model.modelId')
    Model2 = db.relationship(
        'Model',
        primaryjoin='AbInitioModel.shapeDeterminationModelId == Model.modelId')


class Additive(db.Model):
    __tablename__ = 'Additive'

    additiveId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    additiveType = db.Column(db.String(45))
    comments = db.Column(db.String(512))
    chemFormulaHead = db.Column(
        db.String(25), server_default=db.FetchedValue())
    chemFormulaTail = db.Column(
        db.String(25), server_default=db.FetchedValue())


class AdminActivity(db.Model):
    __tablename__ = 'AdminActivity'

    adminActivityId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False,
                         unique=True, server_default=db.FetchedValue())
    action = db.Column(db.String(45), index=True)
    comments = db.Column(db.String(100))
    dateTime = db.Column(db.DateTime)


class AdminVar(db.Model):
    __tablename__ = 'AdminVar'

    varId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    value = db.Column(db.String(1024), index=True)


class Aperture(db.Model):
    __tablename__ = 'Aperture'

    apertureId = db.Column(db.Integer, primary_key=True)
    sizeX = db.Column(db.Float)


class Assembly(db.Model):
    __tablename__ = 'Assembly'

    assemblyId = db.Column(db.Integer, primary_key=True)
    macromoleculeId = db.Column(db.ForeignKey(
        'Macromolecule.macromoleculeId'), nullable=False, index=True)
    creationDate = db.Column(db.DateTime)
    comments = db.Column(db.String(255))

    Macromolecule = db.relationship(
        'Macromolecule',
        primaryjoin='Assembly.macromoleculeId == Macromolecule.macromoleculeId')


class AssemblyHasMacromolecule(db.Model):
    __tablename__ = 'AssemblyHasMacromolecule'

    AssemblyHasMacromoleculeId = db.Column(db.Integer, primary_key=True)
    assemblyId = db.Column(db.ForeignKey(
        'Assembly.assemblyId'), nullable=False, index=True)
    macromoleculeId = db.Column(db.ForeignKey(
        'Macromolecule.macromoleculeId'), nullable=False, index=True)

    Assembly = db.relationship(
        'Assembly',
        primaryjoin='AssemblyHasMacromolecule.assemblyId == Assembly.assemblyId')
    Macromolecule = db.relationship(
        'Macromolecule',
        primaryjoin='AssemblyHasMacromolecule.macromoleculeId == Macromolecule.macromoleculeId')


class AssemblyRegion(db.Model):
    __tablename__ = 'AssemblyRegion'

    assemblyRegionId = db.Column(db.Integer, primary_key=True)
    assemblyHasMacromoleculeId = db.Column(
        db.ForeignKey('AssemblyHasMacromolecule.AssemblyHasMacromoleculeId'),
        nullable=False,
        index=True)
    assemblyRegionType = db.Column(db.String(45))
    name = db.Column(db.String(45))
    fromResiduesBases = db.Column(db.String(45))
    toResiduesBases = db.Column(db.String(45))

    AssemblyHasMacromolecule = db.relationship(
        'AssemblyHasMacromolecule',
        primaryjoin='AssemblyRegion.assemblyHasMacromoleculeId == AssemblyHasMacromolecule.AssemblyHasMacromoleculeId')


class AutoProc(db.Model):
    __tablename__ = 'AutoProc'

    autoProcId = db.Column(db.Integer, primary_key=True,
                           info='Primary key (auto-incremented)')
    autoProcProgramId = db.Column(
        db.Integer, index=True, info='Related program item')
    spaceGroup = db.Column(db.String(45), info='Space group')
    refinedCell_a = db.Column(db.Float, info='Refined cell')
    refinedCell_b = db.Column(db.Float, info='Refined cell')
    refinedCell_c = db.Column(db.Float, info='Refined cell')
    refinedCell_alpha = db.Column(db.Float, info='Refined cell')
    refinedCell_beta = db.Column(db.Float, info='Refined cell')
    refinedCell_gamma = db.Column(db.Float, info='Refined cell')
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')


class AutoProcIntegration(db.Model):
    __tablename__ = 'AutoProcIntegration'

    autoProcIntegrationId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    dataCollectionId = db.Column(
        db.ForeignKey(
            'DataCollection.dataCollectionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='DataCollection item')
    autoProcProgramId = db.Column(
        db.ForeignKey(
            'AutoProcProgram.autoProcProgramId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='Related program item')
    startImageNumber = db.Column(db.Integer, info='start image number')
    endImageNumber = db.Column(db.Integer, info='end image number')
    refinedDetectorDistance = db.Column(
        db.Float, info='Refined DataCollection.detectorDistance')
    refinedXBeam = db.Column(db.Float, info='Refined DataCollection.xBeam')
    refinedYBeam = db.Column(db.Float, info='Refined DataCollection.yBeam')
    rotationAxisX = db.Column(db.Float, info='Rotation axis')
    rotationAxisY = db.Column(db.Float, info='Rotation axis')
    rotationAxisZ = db.Column(db.Float, info='Rotation axis')
    beamVectorX = db.Column(db.Float, info='Beam vector')
    beamVectorY = db.Column(db.Float, info='Beam vector')
    beamVectorZ = db.Column(db.Float, info='Beam vector')
    cell_a = db.Column(db.Float, info='Unit cell')
    cell_b = db.Column(db.Float, info='Unit cell')
    cell_c = db.Column(db.Float, info='Unit cell')
    cell_alpha = db.Column(db.Float, info='Unit cell')
    cell_beta = db.Column(db.Float, info='Unit cell')
    cell_gamma = db.Column(db.Float, info='Unit cell')
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')
    anomalous = db.Column(db.Integer, server_default=db.FetchedValue(
    ), info='boolean type:0 noanoum - 1 anoum')

    AutoProcProgram = db.relationship(
        'AutoProcProgram',
        primaryjoin='AutoProcIntegration.autoProcProgramId == AutoProcProgram.autoProcProgramId')
    DataCollection = db.relationship(
        'DataCollection',
        primaryjoin='AutoProcIntegration.dataCollectionId == DataCollection.dataCollectionId')


class AutoProcProgram(db.Model):
    __tablename__ = 'AutoProcProgram'

    autoProcProgramId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    dataCollectionId = db.Column(db.ForeignKey(
        'DataCollection.dataCollectionId'), index=True)
    processingCommandLine = db.Column(
        db.String(255),
        info='Command line for running the automatic processing')
    processingPrograms = db.Column(
        db.String(255), info='Processing programs (comma separated)')
    processingStatus = db.Column(
        db.Enum(
            'RUNNING',
            'FAILED',
            'SUCCESS',
            '0',
            '1'),
        info='success (1) / fail (0)')
    processingMessage = db.Column(db.String(255), info='warning, error,...')
    processingStartTime = db.Column(db.DateTime, info='Processing start time')
    processingEndTime = db.Column(db.DateTime, info='Processing end time')
    processingEnvironment = db.Column(db.String(255), info='Cpus, Nodes,...')
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')

    DataCollection = db.relationship(
        'DataCollection',
        primaryjoin='AutoProcProgram.dataCollectionId == DataCollection.dataCollectionId')


class AutoProcProgramAttachment(db.Model):
    __tablename__ = 'AutoProcProgramAttachment'

    autoProcProgramAttachmentId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    autoProcProgramId = db.Column(
        db.ForeignKey(
            'AutoProcProgram.autoProcProgramId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related autoProcProgram item')
    fileType = db.Column(db.Enum('Log', 'Result', 'Graph'),
                         info='Type of file Attachment')
    fileName = db.Column(db.String(255), info='Attachment filename')
    filePath = db.Column(
        db.String(255), info='Attachment filepath to disk storage')
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')

    AutoProcProgram = db.relationship(
        'AutoProcProgram',
        primaryjoin='AutoProcProgramAttachment.autoProcProgramId == AutoProcProgram.autoProcProgramId')


class AutoProcScaling(db.Model):
    __tablename__ = 'AutoProcScaling'
    __table_args__ = (
        db.Index('AutoProcScalingIdx1', 'autoProcScalingId', 'autoProcId'),
    )

    autoProcScalingId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    autoProcId = db.Column(
        db.ForeignKey(
            'AutoProc.autoProcId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='Related autoProc item (used by foreign key)')
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')
    resolutionEllipsoidAxis11 = db.Column(
        db.Float, info='Eigenvector for first diffraction limit, coord 1')
    resolutionEllipsoidAxis12 = db.Column(
        db.Float, info='Eigenvector for first diffraction limit, coord 2')
    resolutionEllipsoidAxis13 = db.Column(
        db.Float, info='Eigenvector for first diffraction limit, coord 3')
    resolutionEllipsoidAxis21 = db.Column(
        db.Float, info='Eigenvector for second diffraction limit, coord 1')
    resolutionEllipsoidAxis22 = db.Column(
        db.Float, info='Eigenvector for second diffraction limit, coord 2')
    resolutionEllipsoidAxis23 = db.Column(
        db.Float, info='Eigenvector for second diffraction limit, coord 3')
    resolutionEllipsoidAxis31 = db.Column(
        db.Float, info='Eigenvector for third diffraction limit, coord 1')
    resolutionEllipsoidAxis32 = db.Column(
        db.Float, info='Eigenvector for third diffraction limit, coord 2')
    resolutionEllipsoidAxis33 = db.Column(
        db.Float, info='Eigenvector for third diffraction limit, coord 3')
    resolutionEllipsoidValue1 = db.Column(
        db.Float, info='First (anisotropic) diffraction limit')
    resolutionEllipsoidValue2 = db.Column(
        db.Float, info='Second (anisotropic) diffraction limit')
    resolutionEllipsoidValue3 = db.Column(
        db.Float, info='Third (anisotropic) diffraction limit')

    AutoProc = db.relationship(
        'AutoProc',
        primaryjoin='AutoProcScaling.autoProcId == AutoProc.autoProcId')


class AutoProcScalingStatistic(db.Model):
    __tablename__ = 'AutoProcScalingStatistics'

    autoProcScalingStatisticsId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    autoProcScalingId = db.Column(
        db.ForeignKey(
            'AutoProcScaling.autoProcScalingId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='Related autoProcScaling item (used by foreign key)')
    scalingStatisticsType = db.Column(
        db.Enum(
            'overall',
            'innerShell',
            'outerShell'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue(),
        info='Scaling statistics type')
    comments = db.Column(db.String(255), info='Comments...')
    resolutionLimitLow = db.Column(db.Float, info='Low resolution limit')
    resolutionLimitHigh = db.Column(db.Float, info='High resolution limit')
    rMerge = db.Column(db.Float, info='Rmerge')
    rMeasWithinIPlusIMinus = db.Column(db.Float, info='Rmeas (within I+/I-)')
    rMeasAllIPlusIMinus = db.Column(db.Float, info='Rmeas (all I+ & I-)')
    rPimWithinIPlusIMinus = db.Column(db.Float, info='Rpim (within I+/I-) ')
    rPimAllIPlusIMinus = db.Column(db.Float, info='Rpim (all I+ & I-)')
    fractionalPartialBias = db.Column(db.Float, info='Fractional partial bias')
    nTotalObservations = db.Column(
        db.Integer, info='Total number of observations')
    nTotalUniqueObservations = db.Column(
        db.Integer, info='Total number unique')
    meanIOverSigI = db.Column(db.Float, info='Mean((I)/sd(I))')
    completeness = db.Column(db.Float, info='Completeness')
    multiplicity = db.Column(db.Float, info='Multiplicity')
    anomalousCompleteness = db.Column(db.Float, info='Anomalous completeness')
    anomalousMultiplicity = db.Column(db.Float, info='Anomalous multiplicity')
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')
    anomalous = db.Column(db.Integer, server_default=db.FetchedValue(
    ), info='boolean type:0 noanoum - 1 anoum')
    ccHalf = db.Column(db.Float, info='information from XDS')
    ccAno = db.Column(db.Float)
    sigAno = db.Column(db.String(45))
    isa = db.Column(db.String(45))
    completenessSpherical = db.Column(
        db.Float, info='Completeness calculated assuming isotropic diffraction')
    completenessEllipsoidal = db.Column(
        db.Float, info='Completeness calculated allowing for anisotropic diffraction')
    anomalousCompletenessSpherical = db.Column(
        db.Float, info='Anomalous completeness calculated assuming isotropic diffraction')
    anomalousCompletenessEllipsoidal = db.Column(
        db.Float,
        info='Anisotropic completeness calculated allowing for anisotropic diffraction')

    AutoProcScaling = db.relationship(
        'AutoProcScaling',
        primaryjoin='AutoProcScalingStatistic.autoProcScalingId == AutoProcScaling.autoProcScalingId')


class AutoProcScalingHasInt(db.Model):
    __tablename__ = 'AutoProcScaling_has_Int'
    __table_args__ = (
        db.Index('AutoProcScalingHasInt_FKIndex3',
                 'autoProcScalingId', 'autoProcIntegrationId'),
    )

    autoProcScaling_has_IntId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    autoProcScalingId = db.Column(
        db.ForeignKey(
            'AutoProcScaling.autoProcScalingId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='AutoProcScaling item')
    autoProcIntegrationId = db.Column(
        db.ForeignKey(
            'AutoProcIntegration.autoProcIntegrationId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='AutoProcIntegration item')
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')

    AutoProcIntegration = db.relationship(
        'AutoProcIntegration',
        primaryjoin='AutoProcScalingHasInt.autoProcIntegrationId == AutoProcIntegration.autoProcIntegrationId')
    AutoProcScaling = db.relationship(
        'AutoProcScaling',
        primaryjoin='AutoProcScalingHasInt.autoProcScalingId == AutoProcScaling.autoProcScalingId')


class AutoProcStatus(db.Model):
    __tablename__ = 'AutoProcStatus'

    autoProcStatusId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    autoProcIntegrationId = db.Column(
        db.ForeignKey(
            'AutoProcIntegration.autoProcIntegrationId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    step = db.Column(
        db.Enum(
            'Indexing',
            'Integration',
            'Correction',
            'Scaling',
            'Importing'),
        nullable=False,
        info='autoprocessing step')
    status = db.Column(db.Enum('Launched', 'Successful', 'Failed'),
                       nullable=False, info='autoprocessing status')
    comments = db.Column(db.String(1024), info='comments')
    bltimeStamp = db.Column(db.DateTime, nullable=False,
                            server_default=db.FetchedValue())

    AutoProcIntegration = db.relationship(
        'AutoProcIntegration',
        primaryjoin='AutoProcStatus.autoProcIntegrationId == AutoProcIntegration.autoProcIntegrationId')


class BFAutomationError(db.Model):
    __tablename__ = 'BF_automationError'

    automationErrorId = db.Column(db.Integer, primary_key=True)
    errorType = db.Column(db.String(40), nullable=False)
    solution = db.Column(db.Text)


class BFAutomationFault(db.Model):
    __tablename__ = 'BF_automationFault'

    automationFaultId = db.Column(db.Integer, primary_key=True)
    automationErrorId = db.Column(db.ForeignKey(
        'BF_automationError.automationErrorId'), index=True)
    containerId = db.Column(db.ForeignKey('Container.containerId'), index=True)
    severity = db.Column(db.Enum('1', '2', '3'))
    stacktrace = db.Column(db.Text)
    resolved = db.Column(db.Integer)
    faultTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())

    BF_automationError = db.relationship(
        'BFAutomationError',
        primaryjoin='BFAutomationFault.automationErrorId == BFAutomationError.automationErrorId')
    Container = db.relationship(
        'Container',
        primaryjoin='BFAutomationFault.containerId == Container.containerId')


class BFComponent(db.Model):
    __tablename__ = 'BF_component'

    componentId = db.Column(db.Integer, primary_key=True)
    systemId = db.Column(db.ForeignKey('BF_system.systemId'), index=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))

    BF_system = db.relationship(
        'BFSystem', primaryjoin='BFComponent.systemId == BFSystem.systemId')


class BFComponentBeamline(db.Model):
    __tablename__ = 'BF_component_beamline'

    component_beamlineId = db.Column(db.Integer, primary_key=True)
    componentId = db.Column(db.ForeignKey(
        'BF_component.componentId'), index=True)
    beamlinename = db.Column(db.String(20))

    BF_component = db.relationship(
        'BFComponent',
        primaryjoin='BFComponentBeamline.componentId == BFComponent.componentId')


class BFFault(db.Model):
    __tablename__ = 'BF_fault'

    faultId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.ForeignKey(
        'BLSession.sessionId'), nullable=False, index=True)
    owner = db.Column(db.String(50))
    subcomponentId = db.Column(db.ForeignKey(
        'BF_subcomponent.subcomponentId'), index=True)
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
    personId = db.Column(db.ForeignKey('Person.personId'), index=True)
    assigneeId = db.Column(db.ForeignKey('Person.personId'), index=True)

    Person = db.relationship(
        'Person', primaryjoin='BFFault.assigneeId == Person.personId')
    Person1 = db.relationship(
        'Person', primaryjoin='BFFault.personId == Person.personId')
    BLSession = db.relationship(
        'BLSession', primaryjoin='BFFault.sessionId == BLSession.sessionId')
    BF_subcomponent = db.relationship(
        'BFSubcomponent',
        primaryjoin='BFFault.subcomponentId == BFSubcomponent.subcomponentId')


class BFSubcomponent(db.Model):
    __tablename__ = 'BF_subcomponent'

    subcomponentId = db.Column(db.Integer, primary_key=True)
    componentId = db.Column(db.ForeignKey(
        'BF_component.componentId'), index=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))

    BF_component = db.relationship(
        'BFComponent',
        primaryjoin='BFSubcomponent.componentId == BFComponent.componentId')


class BFSubcomponentBeamline(db.Model):
    __tablename__ = 'BF_subcomponent_beamline'

    subcomponent_beamlineId = db.Column(db.Integer, primary_key=True)
    subcomponentId = db.Column(db.ForeignKey(
        'BF_subcomponent.subcomponentId'), index=True)
    beamlinename = db.Column(db.String(20))

    BF_subcomponent = db.relationship(
        'BFSubcomponent',
        primaryjoin='BFSubcomponentBeamline.subcomponentId == BFSubcomponent.subcomponentId')


class BFSystem(db.Model):
    __tablename__ = 'BF_system'

    systemId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))


class BFSystemBeamline(db.Model):
    __tablename__ = 'BF_system_beamline'

    system_beamlineId = db.Column(db.Integer, primary_key=True)
    systemId = db.Column(db.ForeignKey('BF_system.systemId'), index=True)
    beamlineName = db.Column(db.String(20))

    BF_system = db.relationship(
        'BFSystem',
        primaryjoin='BFSystemBeamline.systemId == BFSystem.systemId')


class BLSample(db.Model):
    __tablename__ = 'BLSample'
    __table_args__ = (
        db.Index('crystalId', 'crystalId', 'containerId'),
    )

    blSampleId = db.Column(db.Integer, primary_key=True)
    diffractionPlanId = db.Column(
        db.ForeignKey(
            'DiffractionPlan.diffractionPlanId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    crystalId = db.Column(
        db.ForeignKey(
            'Crystal.crystalId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    containerId = db.Column(
        db.ForeignKey(
            'Container.containerId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    name = db.Column(db.String(100), index=True)
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
        info='Creation or last update date/time')
    SMILES = db.Column(
        db.String(400),
        info='the symbolic description of the structure of a chemical compound')
    lastImageURL = db.Column(db.String(255))
    positionId = db.Column(db.Integer)
    blSubSampleId = db.Column(db.Integer)
    screenComponentGroupId = db.Column(db.Integer, index=True)
    volume = db.Column(db.Float)
    dimension1 = db.Column(db.Float(asdecimal=True))
    dimension2 = db.Column(db.Float(asdecimal=True))
    dimension3 = db.Column(db.Float(asdecimal=True))
    shape = db.Column(db.String(15))
    subLocation = db.Column(
        db.SmallInteger,
        info="Indicates the sample's location on a multi-sample pin, where 1 is closest to the pin base")

    Container = db.relationship(
        'Container',
        primaryjoin='BLSample.containerId == Container.containerId')
    Crystal = db.relationship(
        'Crystal', primaryjoin='BLSample.crystalId == Crystal.crystalId')
    DiffractionPlan = db.relationship(
        'DiffractionPlan',
        primaryjoin='BLSample.diffractionPlanId == DiffractionPlan.diffractionPlanId')
    DiffractionPlan1 = db.relationship(
        'DiffractionPlan', secondary='BLSample_has_DiffractionPlan')
    Project = db.relationship('Project', secondary='Project_has_BLSample')


class BLSampleGroup(db.Model):
    __tablename__ = 'BLSampleGroup'

    blSampleGroupId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), info='Human-readable name')


class BLSampleGroupHasBLSample(db.Model):
    __tablename__ = 'BLSampleGroup_has_BLSample'

    blSampleGroupId = db.Column(db.ForeignKey(
        'BLSampleGroup.blSampleGroupId'), primary_key=True, nullable=False)
    blSampleId = db.Column(db.ForeignKey(
        'BLSample.blSampleId'), primary_key=True, nullable=False, index=True)
    order = db.Column(db.Integer)
    type = db.Column(db.Enum('background', 'container', 'sample', 'calibrant'))

    BLSampleGroup = db.relationship(
        'BLSampleGroup',
        primaryjoin='BLSampleGroupHasBLSample.blSampleGroupId == BLSampleGroup.blSampleGroupId')
    BLSample = db.relationship(
        'BLSample',
        primaryjoin='BLSampleGroupHasBLSample.blSampleId == BLSample.blSampleId')


class BLSampleImage(db.Model):
    __tablename__ = 'BLSampleImage'

    blSampleImageId = db.Column(db.Integer, primary_key=True)
    blSampleId = db.Column(
        db.ForeignKey(
            'BLSample.blSampleId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    micronsPerPixelX = db.Column(db.Float)
    micronsPerPixelY = db.Column(db.Float)
    imageFullPath = db.Column(db.String(255))
    blSampleImageScoreId = db.Column(db.Integer)
    comments = db.Column(db.String(255))
    blTimeStamp = db.Column(db.DateTime)
    containerInspectionId = db.Column(db.ForeignKey(
        'ContainerInspection.containerInspectionId'), index=True)
    modifiedTimeStamp = db.Column(db.DateTime)

    BLSample = db.relationship(
        'BLSample',
        primaryjoin='BLSampleImage.blSampleId == BLSample.blSampleId')
    ContainerInspection = db.relationship(
        'ContainerInspection',
        primaryjoin='BLSampleImage.containerInspectionId == ContainerInspection.containerInspectionId')


class BLSampleImageAnalysi(db.Model):
    __tablename__ = 'BLSampleImageAnalysis'

    blSampleImageAnalysisId = db.Column(db.Integer, primary_key=True)
    blSampleImageId = db.Column(db.ForeignKey(
        'BLSampleImage.blSampleImageId'), index=True)
    oavSnapshotBefore = db.Column(db.String(255))
    oavSnapshotAfter = db.Column(db.String(255))
    deltaX = db.Column(db.Integer)
    deltaY = db.Column(db.Integer)
    goodnessOfFit = db.Column(db.Float)
    scaleFactor = db.Column(db.Float)
    resultCode = db.Column(db.String(15))
    matchStartTimeStamp = db.Column(
        db.DateTime, server_default=db.FetchedValue())
    matchEndTimeStamp = db.Column(db.DateTime)

    BLSampleImage = db.relationship(
        'BLSampleImage',
        primaryjoin='BLSampleImageAnalysi.blSampleImageId == BLSampleImage.blSampleImageId')


class BLSampleImageScore(db.Model):
    __tablename__ = 'BLSampleImageScore'

    blSampleImageScoreId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    score = db.Column(db.Float)
    colour = db.Column(db.String(15))


class BLSampleTypeHasComponent(db.Model):
    __tablename__ = 'BLSampleType_has_Component'

    blSampleTypeId = db.Column(
        db.ForeignKey(
            'Crystal.crystalId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False)
    componentId = db.Column(
        db.ForeignKey(
            'Protein.proteinId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True)
    abundance = db.Column(db.Float)

    Crystal = db.relationship(
        'Crystal',
        primaryjoin='BLSampleTypeHasComponent.blSampleTypeId == Crystal.crystalId')
    Protein = db.relationship(
        'Protein',
        primaryjoin='BLSampleTypeHasComponent.componentId == Protein.proteinId')


t_BLSample_has_DiffractionPlan = db.Table(
    'BLSample_has_DiffractionPlan',
    db.Column(
        'blSampleId',
        db.ForeignKey('BLSample.blSampleId'),
        primary_key=True,
        nullable=False),
    db.Column(
        'diffractionPlanId',
        db.ForeignKey('DiffractionPlan.diffractionPlanId'),
        primary_key=True,
        nullable=False,
        index=True))


class BLSampleHasEnergyScan(db.Model):
    __tablename__ = 'BLSample_has_EnergyScan'

    blSampleId = db.Column(
        db.ForeignKey(
            'BLSample.blSampleId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    energyScanId = db.Column(
        db.ForeignKey(
            'EnergyScan.energyScanId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    blSampleHasEnergyScanId = db.Column(db.Integer, primary_key=True)

    BLSample = db.relationship(
        'BLSample',
        primaryjoin='BLSampleHasEnergyScan.blSampleId == BLSample.blSampleId')
    EnergyScan = db.relationship(
        'EnergyScan',
        primaryjoin='BLSampleHasEnergyScan.energyScanId == EnergyScan.energyScanId')


class BLSession(db.Model):
    __tablename__ = 'BLSession'

    sessionId = db.Column(db.Integer, primary_key=True)
    expSessionPk = db.Column(db.Integer, info='smis session Pk ')
    beamLineSetupId = db.Column(
        db.ForeignKey(
            'BeamLineSetup.beamLineSetupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    proposalId = db.Column(
        db.ForeignKey(
            'Proposal.proposalId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    projectCode = db.Column(db.String(45))
    startDate = db.Column(db.DateTime, index=True)
    endDate = db.Column(db.DateTime, index=True)
    beamLineName = db.Column(db.String(45), index=True)
    scheduled = db.Column(db.Integer)
    nbShifts = db.Column(db.Integer, index=True)
    comments = db.Column(db.String(2000))
    beamLineOperator = db.Column(db.String(255))
    visit_number = db.Column(db.Integer, server_default=db.FetchedValue())
    bltimeStamp = db.Column(db.DateTime, nullable=False,
                            server_default=db.FetchedValue())
    usedFlag = db.Column(
        db.Integer,
        info='indicates if session has Datacollections or XFE or EnergyScans attached')
    sessionTitle = db.Column(db.String(255), info='fx accounts only')
    structureDeterminations = db.Column(db.Float)
    dewarTransport = db.Column(db.Float)
    databackupFrance = db.Column(
        db.Float, info='data backup and express delivery France')
    databackupEurope = db.Column(
        db.Float, info='data backup and express delivery Europe')
    operatorSiteNumber = db.Column(
        db.String(10), index=True, info='matricule site')
    lastUpdate = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(
    ), info='last update timestamp: by default the end of the session, the last collect...')
    protectedData = db.Column(
        db.String(1024), info='indicates if the data are protected or not')
    externalId = db.Column(db.BINARY(16))
    nbReimbDewars = db.Column(db.Integer)

    BeamLineSetup = db.relationship(
        'BeamLineSetup',
        primaryjoin='BLSession.beamLineSetupId == BeamLineSetup.beamLineSetupId')
    Proposal = db.relationship(
        'Proposal', primaryjoin='BLSession.proposalId == Proposal.proposalId')
    Shipping = db.relationship('Shipping', secondary='ShippingHasSession')


class BLSessionHasSCPosition(db.Model):
    __tablename__ = 'BLSession_has_SCPosition'

    blsessionhasscpositionid = db.Column(db.Integer, primary_key=True)
    blsessionid = db.Column(
        db.ForeignKey(
            'BLSession.sessionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    scContainer = db.Column(
        db.SmallInteger, info='Position of container within sample changer')
    containerPosition = db.Column(
        db.SmallInteger, info='Position of sample within container')

    BLSession = db.relationship(
        'BLSession',
        primaryjoin='BLSessionHasSCPosition.blsessionid == BLSession.sessionId')


class BLSubSample(db.Model):
    __tablename__ = 'BLSubSample'

    blSubSampleId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    blSampleId = db.Column(
        db.ForeignKey(
            'BLSample.blSampleId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='sample')
    diffractionPlanId = db.Column(
        db.ForeignKey(
            'DiffractionPlan.diffractionPlanId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='eventually diffractionPlan')
    positionId = db.Column(
        db.ForeignKey(
            'Position.positionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='position of the subsample')
    position2Id = db.Column(
        db.ForeignKey(
            'Position.positionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    blSubSampleUUID = db.Column(db.String(45), info='uuid of the blsubsample')
    imgFileName = db.Column(db.String(255), info='image filename')
    imgFilePath = db.Column(db.String(1024), info='url image')
    comments = db.Column(db.String(1024), info='comments')
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info='Creation or last update date/time')
    motorPositionId = db.Column(
        db.ForeignKey(
            'MotorPosition.motorPositionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='motor position')

    BLSample = db.relationship(
        'BLSample',
        primaryjoin='BLSubSample.blSampleId == BLSample.blSampleId')
    DiffractionPlan = db.relationship(
        'DiffractionPlan',
        primaryjoin='BLSubSample.diffractionPlanId == DiffractionPlan.diffractionPlanId')
    MotorPosition = db.relationship(
        'MotorPosition',
        primaryjoin='BLSubSample.motorPositionId == MotorPosition.motorPositionId')
    Position = db.relationship(
        'Position',
        primaryjoin='BLSubSample.position2Id == Position.positionId')
    Position1 = db.relationship(
        'Position',
        primaryjoin='BLSubSample.positionId == Position.positionId')


class BeamAperture(db.Model):
    __tablename__ = 'BeamApertures'

    beamAperturesid = db.Column(db.Integer, primary_key=True)
    beamlineStatsId = db.Column(db.ForeignKey(
        'BeamlineStats.beamlineStatsId', ondelete='CASCADE'), index=True)
    flux = db.Column(db.Float(asdecimal=True))
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    apertureSize = db.Column(db.SmallInteger)

    BeamlineStat = db.relationship(
        'BeamlineStat',
        primaryjoin='BeamAperture.beamlineStatsId == BeamlineStat.beamlineStatsId')


class BeamCentre(db.Model):
    __tablename__ = 'BeamCentres'

    beamCentresid = db.Column(db.Integer, primary_key=True)
    beamlineStatsId = db.Column(db.ForeignKey(
        'BeamlineStats.beamlineStatsId', ondelete='CASCADE'), index=True)
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    zoom = db.Column(db.Integer)

    BeamlineStat = db.relationship(
        'BeamlineStat',
        primaryjoin='BeamCentre.beamlineStatsId == BeamlineStat.beamlineStatsId')


class BeamLineSetup(db.Model):
    __tablename__ = 'BeamLineSetup'

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
        info='Creation or last update date/time')


class BeamlineAction(db.Model):
    __tablename__ = 'BeamlineAction'

    beamlineActionId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.ForeignKey('BLSession.sessionId'), index=True)
    startTimestamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())
    endTimestamp = db.Column(db.DateTime, nullable=False,
                             server_default=db.FetchedValue())
    message = db.Column(db.String(255))
    parameter = db.Column(db.String(50))
    value = db.Column(db.String(30))
    loglevel = db.Column(db.Enum('DEBUG', 'CRITICAL', 'INFO'))
    status = db.Column(db.Enum('PAUSED', 'RUNNING',
                       'TERMINATED', 'COMPLETE', 'ERROR', 'EPICSFAIL'))

    BLSession = db.relationship(
        'BLSession',
        primaryjoin='BeamlineAction.sessionId == BLSession.sessionId')


class BeamlineStat(db.Model):
    __tablename__ = 'BeamlineStats'

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
    __tablename__ = 'Buffer'

    bufferId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.Integer, nullable=False,
                           server_default=db.FetchedValue())
    safetyLevelId = db.Column(db.ForeignKey(
        'SafetyLevel.safetyLevelId'), index=True)
    name = db.Column(db.String(45))
    acronym = db.Column(db.String(45))
    pH = db.Column(db.String(45))
    composition = db.Column(db.String(45))
    comments = db.Column(db.String(512))
    BLSessionId = db.Column(db.Integer)
    electronDensity = db.Column(db.Float(7))

    SafetyLevel = db.relationship(
        'SafetyLevel',
        primaryjoin='Buffer.safetyLevelId == SafetyLevel.safetyLevelId')


class BufferHasAdditive(db.Model):
    __tablename__ = 'BufferHasAdditive'

    bufferHasAdditiveId = db.Column(db.Integer, primary_key=True)
    bufferId = db.Column(db.ForeignKey('Buffer.bufferId'),
                         nullable=False, index=True)
    additiveId = db.Column(db.ForeignKey(
        'Additive.additiveId'), nullable=False, index=True)
    measurementUnitId = db.Column(db.ForeignKey(
        'MeasurementUnit.measurementUnitId'), index=True)
    quantity = db.Column(db.String(45))

    Additive = db.relationship(
        'Additive',
        primaryjoin='BufferHasAdditive.additiveId == Additive.additiveId')
    Buffer = db.relationship(
        'Buffer', primaryjoin='BufferHasAdditive.bufferId == Buffer.bufferId')
    MeasurementUnit = db.relationship(
        'MeasurementUnit',
        primaryjoin='BufferHasAdditive.measurementUnitId == MeasurementUnit.measurementUnitId')


class CTF(db.Model):
    __tablename__ = 'CTF'

    CTFid = db.Column(db.Integer, primary_key=True)
    motionCorrectionId = db.Column(db.Integer, nullable=False, index=True)
    spectraImageThumbnailFullPath = db.Column(db.String(512))
    spectraImageFullPath = db.Column(db.String(512))
    defocusU = db.Column(db.String(45))
    defocusV = db.Column(db.String(45))
    angle = db.Column(db.String(45))
    crossCorrelationCoefficient = db.Column(db.String(45))
    resolutionLimit = db.Column(db.String(45))
    estimatedBfactor = db.Column(db.String(45))
    logFilePath = db.Column(db.String(512))
    createdTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())


class CalendarHash(db.Model):
    __tablename__ = 'CalendarHash'

    calendarHashId = db.Column(db.Integer, primary_key=True)
    ckey = db.Column(db.String(50))
    hash = db.Column(db.String(128))
    beamline = db.Column(db.Integer)


class ComponentSubType(db.Model):
    __tablename__ = 'ComponentSubType'

    componentSubTypeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(31), nullable=False)
    hasPh = db.Column(db.Integer, server_default=db.FetchedValue())


class ComponentType(db.Model):
    __tablename__ = 'ComponentType'

    componentTypeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(31), nullable=False)


t_Component_has_SubType = db.Table(
    'Component_has_SubType',
    db.Column(
        'componentId',
        db.ForeignKey(
            'Protein.proteinId',
            ondelete='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'componentSubTypeId',
        db.ForeignKey(
            'ComponentSubType.componentSubTypeId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


class ConcentrationType(db.Model):
    __tablename__ = 'ConcentrationType'

    concentrationTypeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(31), nullable=False)
    symbol = db.Column(db.String(8), nullable=False)


class Container(db.Model):
    __tablename__ = 'Container'

    containerId = db.Column(db.Integer, primary_key=True)
    dewarId = db.Column(db.ForeignKey(
        'Dewar.dewarId', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    code = db.Column(db.String(45))
    containerType = db.Column(db.String(20))
    capacity = db.Column(db.Integer)
    beamlineLocation = db.Column(db.String(20), index=True)
    sampleChangerLocation = db.Column(db.String(20))
    containerStatus = db.Column(db.String(45), index=True)
    bltimeStamp = db.Column(db.DateTime)
    barcode = db.Column(db.String(45), unique=True)
    sessionId = db.Column(db.ForeignKey('BLSession.sessionId'), index=True)
    ownerId = db.Column(db.ForeignKey('Person.personId'), index=True)
    screenId = db.Column(db.Integer)
    scheduleId = db.Column(db.Integer)
    imagerId = db.Column(db.Integer)
    scLocationUpdated = db.Column(db.DateTime)
    requestedImagerId = db.Column(db.Integer)
    requestedReturn = db.Column(db.Integer, server_default=db.FetchedValue(
    ), info='True for requesting return, False means container will be disposed')
    comments = db.Column(db.String(255))
    experimentType = db.Column(db.String(20))
    storageTemperature = db.Column(db.Float)

    Dewar = db.relationship(
        'Dewar', primaryjoin='Container.dewarId == Dewar.dewarId')
    Person = db.relationship(
        'Person', primaryjoin='Container.ownerId == Person.personId')
    BLSession = db.relationship(
        'BLSession', primaryjoin='Container.sessionId == BLSession.sessionId')


class ContainerHistory(db.Model):
    __tablename__ = 'ContainerHistory'

    containerHistoryId = db.Column(db.Integer, primary_key=True)
    containerId = db.Column(
        db.ForeignKey(
            'Container.containerId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    location = db.Column(db.String(45))
    blTimeStamp = db.Column(db.DateTime, nullable=False,
                            server_default=db.FetchedValue())
    status = db.Column(db.String(45))

    Container = db.relationship(
        'Container',
        primaryjoin='ContainerHistory.containerId == Container.containerId')


class ContainerInspection(db.Model):
    __tablename__ = 'ContainerInspection'

    containerInspectionId = db.Column(db.Integer, primary_key=True)
    containerId = db.Column(
        db.ForeignKey(
            'Container.containerId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    inspectionTypeId = db.Column(db.ForeignKey(
        'InspectionType.inspectionTypeId'), nullable=False, index=True)
    imagerId = db.Column(db.ForeignKey('Imager.imagerId'), index=True)
    temperature = db.Column(db.Float)
    blTimeStamp = db.Column(db.DateTime)
    scheduleComponentid = db.Column(db.ForeignKey(
        'ScheduleComponent.scheduleComponentId'), index=True)
    state = db.Column(db.String(20))
    priority = db.Column(db.SmallInteger)
    manual = db.Column(db.Integer)
    scheduledTimeStamp = db.Column(db.DateTime)
    completedTimeStamp = db.Column(db.DateTime)

    Container = db.relationship(
        'Container',
        primaryjoin='ContainerInspection.containerId == Container.containerId')
    Imager = db.relationship(
        'Imager',
        primaryjoin='ContainerInspection.imagerId == Imager.imagerId')
    InspectionType = db.relationship(
        'InspectionType',
        primaryjoin='ContainerInspection.inspectionTypeId == InspectionType.inspectionTypeId')
    ScheduleComponent = db.relationship(
        'ScheduleComponent',
        primaryjoin='ContainerInspection.scheduleComponentid == ScheduleComponent.scheduleComponentId')


class ContainerQueue(db.Model):
    __tablename__ = 'ContainerQueue'

    containerQueueId = db.Column(db.Integer, primary_key=True)
    containerId = db.Column(
        db.ForeignKey(
            'Container.containerId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    personId = db.Column(db.ForeignKey(
        'Person.personId', onupdate='CASCADE'), index=True)
    createdTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())
    completedTimeStamp = db.Column(db.DateTime)

    Container = db.relationship(
        'Container',
        primaryjoin='ContainerQueue.containerId == Container.containerId')
    Person = db.relationship(
        'Person', primaryjoin='ContainerQueue.personId == Person.personId')


class ContainerQueueSample(db.Model):
    __tablename__ = 'ContainerQueueSample'

    containerQueueSampleId = db.Column(db.Integer, primary_key=True)
    containerQueueId = db.Column(
        db.ForeignKey(
            'ContainerQueue.containerQueueId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    blSubSampleId = db.Column(
        db.ForeignKey(
            'BLSubSample.blSubSampleId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)

    BLSubSample = db.relationship(
        'BLSubSample',
        primaryjoin='ContainerQueueSample.blSubSampleId == BLSubSample.blSubSampleId')
    ContainerQueue = db.relationship(
        'ContainerQueue',
        primaryjoin='ContainerQueueSample.containerQueueId == ContainerQueue.containerQueueId')


class CryoemInitialModel(db.Model):
    __tablename__ = 'CryoemInitialModel'

    cryoemInitialModelId = db.Column(db.Integer, primary_key=True)
    resolution = db.Column(db.Float, info='Unit: Angstroms')
    numberOfParticles = db.Column(db.Integer)

    ParticleClassification = db.relationship(
        'ParticleClassification',
        secondary='ParticleClassification_has_CryoemInitialModel')


class Crystal(db.Model):
    __tablename__ = 'Crystal'

    crystalId = db.Column(db.Integer, primary_key=True)
    diffractionPlanId = db.Column(
        db.ForeignKey(
            'DiffractionPlan.diffractionPlanId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    proteinId = db.Column(
        db.ForeignKey(
            'Protein.proteinId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
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
    pdbFileName = db.Column(db.String(255), info='pdb file name')
    pdbFilePath = db.Column(db.String(1024), info='pdb file path')
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info='Creation or last update date/time')
    abundance = db.Column(db.Float)
    packingFraction = db.Column(db.Float)

    DiffractionPlan = db.relationship(
        'DiffractionPlan',
        primaryjoin='Crystal.diffractionPlanId == DiffractionPlan.diffractionPlanId')
    Protein = db.relationship(
        'Protein', primaryjoin='Crystal.proteinId == Protein.proteinId')


class CrystalHasUUID(db.Model):
    __tablename__ = 'Crystal_has_UUID'

    crystal_has_UUID_Id = db.Column(db.Integer, primary_key=True)
    crystalId = db.Column(
        db.ForeignKey(
            'Crystal.crystalId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    UUID = db.Column(db.String(45), index=True)
    imageURL = db.Column(db.String(255))

    Crystal = db.relationship(
        'Crystal', primaryjoin='CrystalHasUUID.crystalId == Crystal.crystalId')


class DataAcquisition(db.Model):
    __tablename__ = 'DataAcquisition'

    dataAcquisitionId = db.Column(db.Integer, primary_key=True)
    sampleCellId = db.Column(db.Integer, nullable=False)
    framesCount = db.Column(db.String(45))
    energy = db.Column(db.String(45))
    waitTime = db.Column(db.String(45))
    detectorDistance = db.Column(db.String(45))


class DataCollection(db.Model):
    __tablename__ = 'DataCollection'

    dataCollectionId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    dataCollectionGroupId = db.Column(
        db.ForeignKey(
            'DataCollectionGroup.dataCollectionGroupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='references DataCollectionGroup table')
    strategySubWedgeOrigId = db.Column(
        db.ForeignKey(
            'ScreeningStrategySubWedge.screeningStrategySubWedgeId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='references ScreeningStrategySubWedge table')
    detectorId = db.Column(
        db.ForeignKey(
            'Detector.detectorId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='references Detector table')
    blSubSampleId = db.Column(db.ForeignKey(
        'BLSubSample.blSubSampleId'), index=True)
    startPositionId = db.Column(db.Integer, index=True)
    endPositionId = db.Column(db.Integer, index=True)
    dataCollectionNumber = db.Column(db.Integer, index=True)
    startTime = db.Column(db.DateTime, index=True,
                          info='Start time of the dataCollection')
    endTime = db.Column(db.DateTime, info='end time of the dataCollection')
    runStatus = db.Column(db.String(45))
    axisStart = db.Column(db.Float)
    axisEnd = db.Column(db.Float)
    axisRange = db.Column(db.Float)
    overlap = db.Column(db.Float)
    numberOfImages = db.Column(db.Integer)
    startImageNumber = db.Column(db.Integer)
    numberOfPasses = db.Column(db.Integer)
    exposureTime = db.Column(db.Float)
    imageDirectory = db.Column(db.String(255), index=True)
    imagePrefix = db.Column(db.String(100), index=True)
    imageSuffix = db.Column(db.String(45))
    imageContainerSubPath = db.Column(
        db.String(255),
        info='Internal path of a HDF5 file pointing to the data for this data collection')
    fileTemplate = db.Column(db.String(255))
    wavelength = db.Column(db.Float)
    resolution = db.Column(db.Float)
    detectorDistance = db.Column(db.Float)
    xBeam = db.Column(db.Float)
    yBeam = db.Column(db.Float)
    xBeamPix = db.Column(db.Float, info='Beam size in pixels')
    yBeamPix = db.Column(db.Float, info='Beam size in pixels')
    comments = db.Column(db.String(1024))
    printableForReport = db.Column(
        db.Integer, server_default=db.FetchedValue())
    slitGapVertical = db.Column(db.Float)
    slitGapHorizontal = db.Column(db.Float)
    transmission = db.Column(db.Float)
    synchrotronMode = db.Column(db.String(20))
    xtalSnapshotFullPath1 = db.Column(db.String(255))
    xtalSnapshotFullPath2 = db.Column(db.String(255))
    xtalSnapshotFullPath3 = db.Column(db.String(255))
    xtalSnapshotFullPath4 = db.Column(db.String(255))
    rotationAxis = db.Column(db.Enum('Omega', 'Kappa', 'Phi'))
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
    flux_end = db.Column(db.Float(asdecimal=True),
                         info='flux measured after the collect')
    totalAbsorbedDose = db.Column(
        db.Float(
            asdecimal=True),
        info='expected dose delivered to the crystal, EDNA')
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
    magnification = db.Column(db.Integer, info='Unit: X')
    binning = db.Column(db.Integer, server_default=db.FetchedValue(
    ), info='1 or 2. Number of pixels to process as 1. (Use mean value.)')
    particleDiameter = db.Column(db.Float, info='Unit: nm')
    boxSize_CTF = db.Column(db.Float, info='Unit: pixels')
    minResolution = db.Column(db.Float, info='Unit: A')
    minDefocus = db.Column(db.Float, info='Unit: A')
    maxDefocus = db.Column(db.Float, info='Unit: A')
    defocusStepSize = db.Column(db.Float, info='Unit: A')
    amountAstigmatism = db.Column(db.Float, info='Unit: A')
    extractSize = db.Column(db.Float, info='Unit: pixels')
    bgRadius = db.Column(db.Float, info='Unit: nm')
    voltage = db.Column(db.Float, info='Unit: kV')
    objAperture = db.Column(db.Float, info='Unit: um')
    c1aperture = db.Column(db.Float, info='Unit: um')
    c2aperture = db.Column(db.Float, info='Unit: um')
    c3aperture = db.Column(db.Float, info='Unit: um')
    c1lens = db.Column(db.Float, info='Unit: %')
    c2lens = db.Column(db.Float, info='Unit: %')
    c3lens = db.Column(db.Float, info='Unit: %')

    BLSubSample = db.relationship(
        'BLSubSample',
        primaryjoin='DataCollection.blSubSampleId == BLSubSample.blSubSampleId')
    DataCollectionGroup = db.relationship(
        'DataCollectionGroup',
        primaryjoin='DataCollection.dataCollectionGroupId == DataCollectionGroup.dataCollectionGroupId')
    Detector = db.relationship(
        'Detector',
        primaryjoin='DataCollection.detectorId == Detector.detectorId')
    ScreeningStrategySubWedge = db.relationship(
        'ScreeningStrategySubWedge',
        primaryjoin='DataCollection.strategySubWedgeOrigId == ScreeningStrategySubWedge.screeningStrategySubWedgeId')


class DataCollectionFileAttachment(db.Model):
    __tablename__ = 'DataCollectionFileAttachment'

    dataCollectionFileAttachmentId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(
        db.ForeignKey(
            'DataCollection.dataCollectionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    fileFullPath = db.Column(db.String(255), nullable=False)
    fileType = db.Column(
        db.Enum(
            'snapshot',
            'log',
            'xy',
            'recip'),
        info='snapshot: image file, usually of the sample. \\r\\nlog: a text file with logging info. \\r\\nxy: x and y data in text format. \\r\\nrecip: a compressed csv file with reciprocal space coordinates.')
    createTime = db.Column(db.DateTime, nullable=False,
                           server_default=db.FetchedValue())

    DataCollection = db.relationship(
        'DataCollection',
        primaryjoin='DataCollectionFileAttachment.dataCollectionId == DataCollection.dataCollectionId')


class DataCollectionGroup(db.Model):
    __tablename__ = 'DataCollectionGroup'

    dataCollectionGroupId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    blSampleId = db.Column(
        db.ForeignKey(
            'BLSample.blSampleId',
            onupdate='CASCADE'),
        index=True,
        info='references BLSample table')
    sessionId = db.Column(
        db.ForeignKey(
            'BLSession.sessionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='references Session table')
    workflowId = db.Column(
        db.ForeignKey(
            'Workflow.workflowId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    experimentType = db.Column(
        db.Enum(
            'EM',
            'SAD',
            'SAD - Inverse Beam',
            'OSC',
            'Collect - Multiwedge',
            'MAD',
            'Helical',
            'Multi-positional',
            'Mesh',
            'Burn',
            'MAD - Inverse Beam',
            'Characterization',
            'Dehydration',
            'Still'),
        info='Experiment type flag')
    startTime = db.Column(
        db.DateTime, info='Start time of the dataCollectionGroup')
    endTime = db.Column(
        db.DateTime, info='end time of the dataCollectionGroup')
    crystalClass = db.Column(
        db.String(20), info='Crystal Class for industrials users')
    comments = db.Column(db.String(1024), info='comments')
    detectorMode = db.Column(db.String(255), info='Detector mode')
    actualSampleBarcode = db.Column(
        db.String(45), info='Actual sample barcode')
    actualSampleSlotInContainer = db.Column(
        db.Integer, info='Actual sample slot number in container')
    actualContainerBarcode = db.Column(
        db.String(45), info='Actual container barcode')
    actualContainerSlotInSC = db.Column(
        db.Integer, info='Actual container slot number in sample changer')
    xtalSnapshotFullPath = db.Column(db.String(255))

    BLSample = db.relationship(
        'BLSample',
        primaryjoin='DataCollectionGroup.blSampleId == BLSample.blSampleId')
    BLSession = db.relationship(
        'BLSession',
        primaryjoin='DataCollectionGroup.sessionId == BLSession.sessionId')
    Workflow = db.relationship(
        'Workflow',
        primaryjoin='DataCollectionGroup.workflowId == Workflow.workflowId')
    Project = db.relationship('Project', secondary='Project_has_DCGroup')


class DataCollectionPlanGroup(db.Model):
    __tablename__ = 'DataCollectionPlanGroup'

    dataCollectionPlanGroupId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.ForeignKey(
        'BLSession.sessionId', onupdate='CASCADE'), index=True)
    blSampleId = db.Column(db.ForeignKey(
        'BLSample.blSampleId', onupdate='CASCADE'), index=True)

    BLSample = db.relationship(
        'BLSample',
        primaryjoin='DataCollectionPlanGroup.blSampleId == BLSample.blSampleId')
    BLSession = db.relationship(
        'BLSession',
        primaryjoin='DataCollectionPlanGroup.sessionId == BLSession.sessionId')


class DataReductionStatu(db.Model):
    __tablename__ = 'DataReductionStatus'

    dataReductionStatusId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(15))
    filename = db.Column(db.String(255))
    message = db.Column(db.String(255))


class DatamatrixInSampleChanger(db.Model):
    __tablename__ = 'DatamatrixInSampleChanger'

    datamatrixInSampleChangerId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.Integer, nullable=False,
                           index=True, server_default=db.FetchedValue())
    beamLineName = db.Column(db.String(45))
    datamatrixCode = db.Column(db.String(45))
    locationInContainer = db.Column(db.Integer)
    containerLocationInSC = db.Column(db.Integer)
    containerDatamatrixCode = db.Column(db.String(45))
    bltimeStamp = db.Column(db.DateTime)


class Detector(db.Model):
    __tablename__ = 'Detector'
    __table_args__ = (
        db.Index(
            'Detector_FKIndex1',
            'detectorType',
            'detectorManufacturer',
            'detectorModel',
            'detectorPixelSizeHorizontal',
            'detectorPixelSizeVertical'),
    )

    detectorId = db.Column(db.Integer, primary_key=True,
                           info='Primary key (auto-incremented)')
    detectorType = db.Column(db.String(255))
    detectorManufacturer = db.Column(db.String(255))
    detectorModel = db.Column(db.String(255))
    detectorPixelSizeHorizontal = db.Column(db.Float)
    detectorPixelSizeVertical = db.Column(db.Float)
    detectorSerialNumber = db.Column(db.String(30), unique=True)
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
    CS = db.Column(db.Float, info='Unit: mm')
    density = db.Column(db.Float)
    composition = db.Column(db.String(16))
    localName = db.Column(
        db.String(40), info='Colloquial name for the detector')


class Dewar(db.Model):
    __tablename__ = 'Dewar'

    dewarId = db.Column(db.Integer, primary_key=True)
    shippingId = db.Column(
        db.ForeignKey(
            'Shipping.shippingId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    code = db.Column(db.String(45), index=True)
    comments = db.Column(db.String)
    storageLocation = db.Column(db.String(45))
    dewarStatus = db.Column(db.String(45), index=True)
    bltimeStamp = db.Column(db.DateTime, server_default=db.FetchedValue())
    isStorageDewar = db.Column(db.Integer, server_default=db.FetchedValue())
    barCode = db.Column(db.String(45), unique=True)
    firstExperimentId = db.Column(
        db.ForeignKey(
            'BLSession.sessionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    customsValue = db.Column(db.Integer)
    transportValue = db.Column(db.Integer)
    trackingNumberToSynchrotron = db.Column(db.String(30))
    trackingNumberFromSynchrotron = db.Column(db.String(30))
    facilityCode = db.Column(
        db.String(20), info='Unique barcode assigned to each dewar')
    type = db.Column(db.Enum('Dewar', 'Toolbox'),
                     nullable=False, server_default=db.FetchedValue())
    isReimbursed = db.Column(db.Integer, server_default=db.FetchedValue(
    ), info='set this dewar as reimbursed by the user office')

    BLSession = db.relationship(
        'BLSession',
        primaryjoin='Dewar.firstExperimentId == BLSession.sessionId')
    Shipping = db.relationship(
        'Shipping', primaryjoin='Dewar.shippingId == Shipping.shippingId')


class DewarLocation(db.Model):
    __tablename__ = 'DewarLocation'

    eventId = db.Column(db.Integer, primary_key=True)
    dewarNumber = db.Column(
        db.String(128), nullable=False, info='Dewar number')
    userId = db.Column(db.String(128), info='User who locates the dewar')
    dateTime = db.Column(db.DateTime, info='Date and time of locatization')
    locationName = db.Column(db.String(128), info='Location of the dewar')
    courierName = db.Column(
        db.String(128), info="Carrier name who's shipping back the dewar")
    courierTrackingNumber = db.Column(
        db.String(128), info='Tracking number of the shippment')


class DewarLocationList(db.Model):
    __tablename__ = 'DewarLocationList'

    locationId = db.Column(db.Integer, primary_key=True)
    locationName = db.Column(
        db.String(128),
        nullable=False,
        server_default=db.FetchedValue(),
        info='Location')


class DewarRegistry(db.Model):
    __tablename__ = 'DewarRegistry'

    dewarRegistryId = db.Column(db.Integer, primary_key=True)
    facilityCode = db.Column(db.String(20), nullable=False, unique=True)
    proposalId = db.Column(db.ForeignKey(
        'Proposal.proposalId', onupdate='CASCADE'), index=True)
    labContactId = db.Column(
        db.ForeignKey(
            'LabContact.labContactId',
            ondelete='SET NULL',
            onupdate='CASCADE'),
        index=True)
    purchaseDate = db.Column(db.DateTime)
    bltimestamp = db.Column(db.DateTime, nullable=False,
                            server_default=db.FetchedValue())

    LabContact = db.relationship(
        'LabContact',
        primaryjoin='DewarRegistry.labContactId == LabContact.labContactId')
    Proposal = db.relationship(
        'Proposal',
        primaryjoin='DewarRegistry.proposalId == Proposal.proposalId')


class DewarRegistryHasProposal(db.Model):
    __tablename__ = 'DewarRegistry_has_Proposal'
    __table_args__ = (
        db.Index('dewarRegistryId', 'dewarRegistryId', 'proposalId'),
    )

    dewarRegistryHasProposalId = db.Column(db.Integer, primary_key=True)
    dewarRegistryId = db.Column(db.ForeignKey('DewarRegistry.dewarRegistryId'))
    proposalId = db.Column(db.ForeignKey('Proposal.proposalId'), index=True)
    personId = db.Column(db.ForeignKey('Person.personId'),
                         index=True, info='Person registering the dewar')
    recordTimestamp = db.Column(db.DateTime, server_default=db.FetchedValue())
    labContactId = db.Column(
        db.ForeignKey(
            'LabContact.labContactId',
            onupdate='CASCADE'),
        index=True,
        info='Owner of the dewar')

    DewarRegistry = db.relationship(
        'DewarRegistry',
        primaryjoin='DewarRegistryHasProposal.dewarRegistryId == DewarRegistry.dewarRegistryId')
    LabContact = db.relationship(
        'LabContact',
        primaryjoin='DewarRegistryHasProposal.labContactId == LabContact.labContactId')
    Person = db.relationship(
        'Person',
        primaryjoin='DewarRegistryHasProposal.personId == Person.personId')
    Proposal = db.relationship(
        'Proposal',
        primaryjoin='DewarRegistryHasProposal.proposalId == Proposal.proposalId')


class DewarTransportHistory(db.Model):
    __tablename__ = 'DewarTransportHistory'

    DewarTransportHistoryId = db.Column(db.Integer, primary_key=True)
    dewarId = db.Column(db.ForeignKey(
        'Dewar.dewarId', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    dewarStatus = db.Column(db.String(45), nullable=False)
    storageLocation = db.Column(db.String(45))
    arrivalDate = db.Column(db.DateTime)

    Dewar = db.relationship(
        'Dewar', primaryjoin='DewarTransportHistory.dewarId == Dewar.dewarId')


class DiffractionPlan(db.Model):
    __tablename__ = 'DiffractionPlan'

    diffractionPlanId = db.Column(db.Integer, primary_key=True)
    xmlDocumentId = db.Column(db.Integer)
    experimentKind = db.Column(
        db.Enum(
            'Default',
            'MXPressE',
            'MXPressF',
            'MXPressO',
            'MXPressP',
            'MXPressP_SAD',
            'MXPressI',
            'MXPressE_SAD',
            'MXScore',
            'MXPressM',
            'MAD',
            'SAD',
            'Fixed',
            'Ligand binding',
            'Refinement',
            'OSC',
            'MAD - Inverse Beam',
            'SAD - Inverse Beam'))
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
    estimateRadiationDamage = db.Column(
        db.Integer, server_default=db.FetchedValue())
    forcedSpaceGroup = db.Column(db.String(45))
    requiredCompleteness = db.Column(db.Float(asdecimal=True))
    requiredMultiplicity = db.Column(db.Float(asdecimal=True))
    requiredResolution = db.Column(db.Float(asdecimal=True))
    strategyOption = db.Column(db.String(45))
    kappaStrategyOption = db.Column(db.String(45))
    numberOfPositions = db.Column(db.Integer)
    minDimAccrossSpindleAxis = db.Column(
        db.Float(
            asdecimal=True),
        info='minimum dimension accross the spindle axis')
    maxDimAccrossSpindleAxis = db.Column(
        db.Float(
            asdecimal=True),
        info='maximum dimension accross the spindle axis')
    radiationSensitivityBeta = db.Column(db.Float(asdecimal=True))
    radiationSensitivityGamma = db.Column(db.Float(asdecimal=True))
    minOscWidth = db.Column(db.Float)
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info='Creation or last update date/time')
    diffractionPlanUUID = db.Column(db.String(1000))
    dataCollectionPlanGroupId = db.Column(db.Integer)
    detectorId = db.Column(db.Integer)
    distance = db.Column(db.Float(asdecimal=True))
    orientation = db.Column(db.Float(asdecimal=True))
    monoBandwidth = db.Column(db.Float(asdecimal=True))
    monochromator = db.Column(db.String(8), info='DMM or DCM')
    energy = db.Column(db.Float, info='eV')
    transmission = db.Column(db.Float, info='Decimal fraction in range [0,1]')
    boxSizeX = db.Column(db.Float, info='microns')
    boxSizeY = db.Column(db.Float, info='microns')
    kappaStart = db.Column(db.Float, info='degrees')
    axisStart = db.Column(db.Float, info='degrees')
    axisRange = db.Column(db.Float, info='degrees')
    numberOfImages = db.Column(
        db.Integer, info='The number of images requested')
    presetForProposalId = db.Column(
        db.Integer,
        info='Indicates this plan is available to all sessions on given proposal')
    beamLineName = db.Column(
        db.String(45),
        info='Indicates this plan is available to all sessions on given beamline')
    userPath = db.Column(
        db.String(100),
        info='User-specified relative "root" path inside the session directory to be used for holding collected data')


class DiffractionPlanHasDetector(db.Model):
    __tablename__ = 'DiffractionPlan_has_Detector'

    diffractionPlanId = db.Column(db.ForeignKey(
        'DiffractionPlan.diffractionPlanId'), primary_key=True, nullable=False)
    detectorId = db.Column(db.ForeignKey(
        'Detector.detectorId'), primary_key=True, nullable=False, index=True)
    exposureTime = db.Column(db.Float(asdecimal=True))
    distance = db.Column(db.Float(asdecimal=True))
    orientation = db.Column(db.Float(asdecimal=True))

    Detector = db.relationship(
        'Detector',
        primaryjoin='DiffractionPlanHasDetector.detectorId == Detector.detectorId')
    DiffractionPlan = db.relationship(
        'DiffractionPlan',
        primaryjoin='DiffractionPlanHasDetector.diffractionPlanId == DiffractionPlan.diffractionPlanId')


class EMMicroscope(db.Model):
    __tablename__ = 'EMMicroscope'

    emMicroscopeId = db.Column(db.Integer, primary_key=True)
    instrumentName = db.Column(db.String(100), nullable=False)
    voltage = db.Column(db.Float)
    CS = db.Column(db.Float, info='Unit: mm')
    detectorPixelSize = db.Column(db.Float)
    C2aperture = db.Column(db.Float)
    ObjAperture = db.Column(db.Float)
    C2lens = db.Column(db.Float)


class EnergyScan(db.Model):
    __tablename__ = 'EnergyScan'

    energyScanId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(
        db.ForeignKey(
            'BLSession.sessionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    blSampleId = db.Column(db.ForeignKey('BLSample.blSampleId'), index=True)
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
    flux = db.Column(db.Float(asdecimal=True),
                     info='flux measured before the energyScan')
    flux_end = db.Column(db.Float(asdecimal=True),
                         info='flux measured after the energyScan')
    workingDirectory = db.Column(db.String(45))
    blSubSampleId = db.Column(db.ForeignKey(
        'BLSubSample.blSubSampleId'), index=True)
    remoteEnergy = db.Column(db.Float)
    remoteFPrime = db.Column(db.Float)
    remoteFDoublePrime = db.Column(db.Float)

    BLSample = db.relationship(
        'BLSample', primaryjoin='EnergyScan.blSampleId == BLSample.blSampleId')
    BLSubSample = db.relationship(
        'BLSubSample',
        primaryjoin='EnergyScan.blSubSampleId == BLSubSample.blSubSampleId')
    BLSession = db.relationship(
        'BLSession', primaryjoin='EnergyScan.sessionId == BLSession.sessionId')
    Project = db.relationship('Project', secondary='Project_has_EnergyScan')


class Experiment(db.Model):
    __tablename__ = 'Experiment'

    experimentId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.ForeignKey('BLSession.sessionId'), index=True)
    proposalId = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255))
    creationDate = db.Column(db.DateTime)
    experimentType = db.Column(db.String(128))
    sourceFilePath = db.Column(db.String(256))
    dataAcquisitionFilePath = db.Column(
        db.String(256),
        info='The file path pointing to the data acquisition. Eventually it may be a compressed file with all the files or just the folder')
    status = db.Column(db.String(45))
    comments = db.Column(db.String(512))

    BLSession = db.relationship(
        'BLSession', primaryjoin='Experiment.sessionId == BLSession.sessionId')


class ExperimentKindDetail(db.Model):
    __tablename__ = 'ExperimentKindDetails'

    experimentKindId = db.Column(db.Integer, primary_key=True)
    diffractionPlanId = db.Column(
        db.ForeignKey(
            'DiffractionPlan.diffractionPlanId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    exposureIndex = db.Column(db.Integer)
    dataCollectionType = db.Column(db.String(45))
    dataCollectionKind = db.Column(db.String(45))
    wedgeValue = db.Column(db.Float)

    DiffractionPlan = db.relationship(
        'DiffractionPlan',
        primaryjoin='ExperimentKindDetail.diffractionPlanId == DiffractionPlan.diffractionPlanId')


class FitStructureToExperimentalDatum(db.Model):
    __tablename__ = 'FitStructureToExperimentalData'

    fitStructureToExperimentalDataId = db.Column(db.Integer, primary_key=True)
    structureId = db.Column(db.ForeignKey('Structure.structureId'), index=True)
    subtractionId = db.Column(db.ForeignKey(
        'Subtraction.subtractionId'), index=True)
    workflowId = db.Column(db.ForeignKey('Workflow.workflowId'), index=True)
    fitFilePath = db.Column(db.String(255))
    logFilePath = db.Column(db.String(255))
    outputFilePath = db.Column(db.String(255))
    creationDate = db.Column(db.DateTime)
    comments = db.Column(db.String(2048))

    Structure = db.relationship(
        'Structure',
        primaryjoin='FitStructureToExperimentalDatum.structureId == Structure.structureId')
    Subtraction = db.relationship(
        'Subtraction',
        primaryjoin='FitStructureToExperimentalDatum.subtractionId == Subtraction.subtractionId')
    Workflow = db.relationship(
        'Workflow',
        primaryjoin='FitStructureToExperimentalDatum.workflowId == Workflow.workflowId')


class Frame(db.Model):
    __tablename__ = 'Frame'

    frameId = db.Column(db.Integer, primary_key=True)
    filePath = db.Column(db.String(255), index=True)
    comments = db.Column(db.String(45))
    creationDate = db.Column(db.DateTime, nullable=False,
                             server_default=db.FetchedValue())
    frameSetId = db.Column(db.Integer)


class FrameList(db.Model):
    __tablename__ = 'FrameList'

    frameListId = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.Integer)


class FrameSet(db.Model):
    __tablename__ = 'FrameSet'

    frameSetId = db.Column(db.Integer, primary_key=True)
    runId = db.Column(db.ForeignKey('Run.runId'), nullable=False, index=True)
    frameListId = db.Column(db.ForeignKey('FrameList.frameListId'), index=True)
    detectorId = db.Column(db.Integer)
    detectorDistance = db.Column(db.String(45))
    filePath = db.Column(db.String(255))
    internalPath = db.Column(db.String(255))

    FrameList = db.relationship(
        'FrameList',
        primaryjoin='FrameSet.frameListId == FrameList.frameListId')
    Run = db.relationship('Run', primaryjoin='FrameSet.runId == Run.runId')


class FrameToList(db.Model):
    __tablename__ = 'FrameToList'

    frameToListId = db.Column(db.Integer, primary_key=True)
    frameListId = db.Column(db.ForeignKey(
        'FrameList.frameListId'), nullable=False, index=True)
    frameId = db.Column(db.ForeignKey('Frame.frameId'),
                        nullable=False, index=True)

    Frame = db.relationship(
        'Frame', primaryjoin='FrameToList.frameId == Frame.frameId')
    FrameList = db.relationship(
        'FrameList',
        primaryjoin='FrameToList.frameListId == FrameList.frameListId')


class GeometryClassname(db.Model):
    __tablename__ = 'GeometryClassname'

    geometryClassnameId = db.Column(db.Integer, primary_key=True)
    geometryClassname = db.Column(db.String(45))
    geometryOrder = db.Column(db.Integer, nullable=False)


class GridInfo(db.Model):
    __tablename__ = 'GridInfo'

    gridInfoId = db.Column(db.Integer, primary_key=True,
                           info='Primary key (auto-incremented)')
    workflowMeshId = db.Column(
        db.ForeignKey(
            'WorkflowMesh.workflowMeshId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
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
        info='Creation or last update date/time')
    orientation = db.Column(
        db.Enum('vertical', 'horizontal'), server_default=db.FetchedValue())
    dataCollectionGroupId = db.Column(db.ForeignKey(
        'DataCollectionGroup.dataCollectionGroupId'), index=True)
    pixelspermicronX = db.Column(db.Float)
    pixelspermicronY = db.Column(db.Float)
    snapshot_offsetxpixel = db.Column(db.Float)
    snapshot_offsetypixel = db.Column(db.Float)

    DataCollectionGroup = db.relationship(
        'DataCollectionGroup',
        primaryjoin='GridInfo.dataCollectionGroupId == DataCollectionGroup.dataCollectionGroupId')
    WorkflowMesh = db.relationship(
        'WorkflowMesh',
        primaryjoin='GridInfo.workflowMeshId == WorkflowMesh.workflowMeshId')


class Image(db.Model):
    __tablename__ = 'Image'
    __table_args__ = (
        db.Index('Image_Index3', 'fileLocation', 'fileName'),
    )

    imageId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(
        db.ForeignKey(
            'DataCollection.dataCollectionId',
            ondelete='CASCADE'),
        db.ForeignKey(
            'DataCollection.dataCollectionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
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
        info='Creation or last update date/time')

    DataCollection = db.relationship(
        'DataCollection',
        primaryjoin='Image.dataCollectionId == DataCollection.dataCollectionId')
    DataCollection1 = db.relationship(
        'DataCollection',
        primaryjoin='Image.dataCollectionId == DataCollection.dataCollectionId')


class ImageQualityIndicator(db.Model):
    __tablename__ = 'ImageQualityIndicators'

    imageQualityIndicatorsId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    imageId = db.Column(db.Integer, index=True)
    autoProcProgramId = db.Column(
        db.ForeignKey(
            'AutoProcProgram.autoProcProgramId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Foreign key to the AutoProcProgram table')
    spotTotal = db.Column(db.Integer, info='Total number of spots')
    inResTotal = db.Column(
        db.Integer, info='Total number of spots in resolution range')
    goodBraggCandidates = db.Column(
        db.Integer, info='Total number of Bragg diffraction spots')
    iceRings = db.Column(db.Integer, info='Number of ice rings identified')
    method1Res = db.Column(
        db.Float, info='Resolution estimate 1 (see publication)')
    method2Res = db.Column(
        db.Float, info='Resolution estimate 2 (see publication)')
    maxUnitCell = db.Column(
        db.Float, info='Estimation of the largest possible unit cell edge')
    pctSaturationTop50Peaks = db.Column(
        db.Float, info='The fraction of the dynamic range being used')
    inResolutionOvrlSpots = db.Column(
        db.Integer, info='Number of spots overloaded')
    binPopCutOffMethod2Res = db.Column(
        db.Float, info='Cut off used in resolution limit calculation')
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')
    totalIntegratedSignal = db.Column(db.Float(asdecimal=True))
    dozor_score = db.Column(db.Float(asdecimal=True), info='dozor_score')
    dataCollectionId = db.Column(db.Integer)
    imageNumber = db.Column(db.Integer)

    AutoProcProgram = db.relationship(
        'AutoProcProgram',
        primaryjoin='ImageQualityIndicator.autoProcProgramId == AutoProcProgram.autoProcProgramId')


class Imager(db.Model):
    __tablename__ = 'Imager'

    imagerId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    temperature = db.Column(db.Float)
    serial = db.Column(db.String(45))
    capacity = db.Column(db.SmallInteger)


class InitialModel(db.Model):
    __tablename__ = 'InitialModel'

    initialModelId = db.Column(db.Integer, primary_key=True)
    resolution = db.Column(db.Float, info='Unit: Angstroms')
    numberOfParticles = db.Column(db.Integer)


class InputParameterWorkflow(db.Model):
    __tablename__ = 'InputParameterWorkflow'

    inputParameterId = db.Column(db.Integer, primary_key=True)
    workflowId = db.Column(db.Integer, nullable=False)
    parameterType = db.Column(db.String(255))
    name = db.Column(db.String(255))
    value = db.Column(db.String(255))
    comments = db.Column(db.String(2048))


class InspectionType(db.Model):
    __tablename__ = 'InspectionType'

    inspectionTypeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))


class Instruction(db.Model):
    __tablename__ = 'Instruction'

    instructionId = db.Column(db.Integer, primary_key=True)
    instructionSetId = db.Column(db.ForeignKey(
        'InstructionSet.instructionSetId'), nullable=False, index=True)
    order = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(255))

    InstructionSet = db.relationship(
        'InstructionSet',
        primaryjoin='Instruction.instructionSetId == InstructionSet.instructionSetId')


class InstructionSet(db.Model):
    __tablename__ = 'InstructionSet'

    instructionSetId = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))


class IspybAutoProcAttachment(db.Model):
    __tablename__ = 'IspybAutoProcAttachment'

    autoProcAttachmentId = db.Column(db.Integer, primary_key=True)
    fileName = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    step = db.Column(
        db.Enum(
            'XDS',
            'XSCALE',
            'SCALA',
            'SCALEPACK',
            'TRUNCATE',
            'DIMPLE'),
        server_default=db.FetchedValue(),
        info='step where the file is generated')
    fileCategory = db.Column(
        db.Enum(
            'input',
            'output',
            'log',
            'correction'),
        server_default=db.FetchedValue())
    hasGraph = db.Column(db.Integer, nullable=False,
                         server_default=db.FetchedValue())


class IspybCrystalClas(db.Model):
    __tablename__ = 'IspybCrystalClass'

    crystalClassId = db.Column(db.Integer, primary_key=True)
    crystalClass_code = db.Column(db.String(20), nullable=False)
    crystalClass_name = db.Column(db.String(255), nullable=False)


class IspybReference(db.Model):
    __tablename__ = 'IspybReference'

    referenceId = db.Column(db.Integer, primary_key=True,
                            info='Primary key (auto-incremented)')
    referenceName = db.Column(db.String(255), info='reference name')
    referenceUrl = db.Column(db.String(1024), info='url of the reference')
    referenceBibtext = db.Column(
        db.LargeBinary, info='bibtext value of the reference')
    beamline = db.Column(
        db.Enum(
            'All',
            'ID14-4',
            'ID23-1',
            'ID23-2',
            'ID29',
            'ID30A-1',
            'ID30A-2',
            'XRF',
            'AllXRF',
            'Mesh'),
        info='beamline involved')


class LabContact(db.Model):
    __tablename__ = 'LabContact'
    __table_args__ = (
        db.Index('personAndProposal', 'personId', 'proposalId'),
        db.Index('cardNameAndProposal', 'cardName', 'proposalId')
    )

    labContactId = db.Column(db.Integer, primary_key=True)
    personId = db.Column(db.ForeignKey('Person.personId'), nullable=False)
    cardName = db.Column(db.String(40), nullable=False)
    proposalId = db.Column(db.ForeignKey(
        'Proposal.proposalId'), nullable=False, index=True)
    defaultCourrierCompany = db.Column(db.String(45))
    courierAccount = db.Column(db.String(45))
    billingReference = db.Column(db.String(45))
    dewarAvgCustomsValue = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue())
    dewarAvgTransportValue = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue())
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info='Creation or last update date/time')

    Person = db.relationship(
        'Person', primaryjoin='LabContact.personId == Person.personId')
    Proposal = db.relationship(
        'Proposal', primaryjoin='LabContact.proposalId == Proposal.proposalId')


class Laboratory(db.Model):
    __tablename__ = 'Laboratory'

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
        info='Creation or last update date/time')
    laboratoryExtPk = db.Column(db.Integer)


class Log4Stat(db.Model):
    __tablename__ = 'Log4Stat'

    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.String(15))
    timestamp = db.Column(db.DateTime)
    msg = db.Column(db.String(255))
    detail = db.Column(db.String(255))
    value = db.Column(db.String(255))


class Login(db.Model):
    __tablename__ = 'Login'

    loginId = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(45), nullable=False, index=True)
    username = db.Column(db.String(45), nullable=False)
    roles = db.Column(db.String(1024), nullable=False)
    siteId = db.Column(db.String(45))
    authorized = db.Column(db.String(1024))
    expirationTime = db.Column(db.DateTime, nullable=False)


class MXMRRun(db.Model):
    __tablename__ = 'MXMRRun'

    mxMRRunId = db.Column(db.Integer, primary_key=True)
    autoProcScalingId = db.Column(db.ForeignKey(
        'AutoProcScaling.autoProcScalingId'), nullable=False, index=True)
    success = db.Column(
        db.Integer,
        server_default=db.FetchedValue(),
        info='Indicates whether the program completed. 1 for success, 0 for failure.')
    message = db.Column(
        db.String(255),
        info='A short summary of the findings, success or failure.')
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

    AutoProcScaling = db.relationship(
        'AutoProcScaling',
        primaryjoin='MXMRRun.autoProcScalingId == AutoProcScaling.autoProcScalingId')


class MXMRRunBlob(db.Model):
    __tablename__ = 'MXMRRunBlob'

    mxMRRunBlobId = db.Column(db.Integer, primary_key=True)
    mxMRRunId = db.Column(db.ForeignKey(
        'MXMRRun.mxMRRunId'), nullable=False, index=True)
    view1 = db.Column(db.String(255))
    view2 = db.Column(db.String(255))
    view3 = db.Column(db.String(255))

    MXMRRun = db.relationship(
        'MXMRRun', primaryjoin='MXMRRunBlob.mxMRRunId == MXMRRun.mxMRRunId')


class Macromolecule(db.Model):
    __tablename__ = 'Macromolecule'

    macromoleculeId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.Integer)
    safetyLevelId = db.Column(db.ForeignKey(
        'SafetyLevel.safetyLevelId'), index=True)
    name = db.Column(db.String(45, 'utf8mb4_unicode_ci'))
    acronym = db.Column(db.String(45, 'utf8mb4_unicode_ci'))
    extintionCoefficient = db.Column(db.String(45))
    molecularMass = db.Column(db.String(45))
    sequence = db.Column(db.String(1000))
    contactsDescriptionFilePath = db.Column(db.String(255))
    symmetry = db.Column(db.String(45))
    comments = db.Column(db.String(1024, 'utf8mb4_unicode_ci'))
    refractiveIndex = db.Column(db.String(45))
    solventViscosity = db.Column(db.String(45))
    creationDate = db.Column(db.DateTime)
    electronDensity = db.Column(db.Float(7))

    SafetyLevel = db.relationship(
        'SafetyLevel',
        primaryjoin='Macromolecule.safetyLevelId == SafetyLevel.safetyLevelId')


class MacromoleculeRegion(db.Model):
    __tablename__ = 'MacromoleculeRegion'

    macromoleculeRegionId = db.Column(db.Integer, primary_key=True)
    macromoleculeId = db.Column(db.ForeignKey(
        'Macromolecule.macromoleculeId'), nullable=False, index=True)
    regionType = db.Column(db.String(45))
    id = db.Column(db.String(45))
    count = db.Column(db.String(45))
    sequence = db.Column(db.String(45))

    Macromolecule = db.relationship(
        'Macromolecule',
        primaryjoin='MacromoleculeRegion.macromoleculeId == Macromolecule.macromoleculeId')


class Measurement(db.Model):
    __tablename__ = 'Measurement'

    measurementId = db.Column(db.Integer, primary_key=True)
    specimenId = db.Column(db.ForeignKey(
        'Specimen.specimenId'), nullable=False, index=True)
    runId = db.Column(db.ForeignKey('Run.runId'), index=True)
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

    Run = db.relationship('Run', primaryjoin='Measurement.runId == Run.runId')
    Speciman = db.relationship(
        'Speciman',
        primaryjoin='Measurement.specimenId == Speciman.specimenId')


class MeasurementToDataCollection(db.Model):
    __tablename__ = 'MeasurementToDataCollection'

    measurementToDataCollectionId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.ForeignKey(
        'SaxsDataCollection.dataCollectionId'), index=True)
    measurementId = db.Column(db.ForeignKey(
        'Measurement.measurementId'), index=True)
    dataCollectionOrder = db.Column(db.Integer)

    SaxsDataCollection = db.relationship(
        'SaxsDataCollection',
        primaryjoin='MeasurementToDataCollection.dataCollectionId == SaxsDataCollection.dataCollectionId')
    Measurement = db.relationship(
        'Measurement',
        primaryjoin='MeasurementToDataCollection.measurementId == Measurement.measurementId')


class MeasurementUnit(db.Model):
    __tablename__ = 'MeasurementUnit'

    measurementUnitId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    unitType = db.Column(db.String(45))


class Merge(db.Model):
    __tablename__ = 'Merge'

    mergeId = db.Column(db.Integer, primary_key=True)
    measurementId = db.Column(db.ForeignKey(
        'Measurement.measurementId'), index=True)
    frameListId = db.Column(db.ForeignKey('FrameList.frameListId'), index=True)
    discardedFrameNameList = db.Column(db.String(1024))
    averageFilePath = db.Column(db.String(255))
    framesCount = db.Column(db.String(45))
    framesMerge = db.Column(db.String(45))
    creationDate = db.Column(db.DateTime)

    FrameList = db.relationship(
        'FrameList', primaryjoin='Merge.frameListId == FrameList.frameListId')
    Measurement = db.relationship(
        'Measurement',
        primaryjoin='Merge.measurementId == Measurement.measurementId')


class MixtureToStructure(db.Model):
    __tablename__ = 'MixtureToStructure'

    fitToStructureId = db.Column(db.Integer, primary_key=True)
    structureId = db.Column(db.ForeignKey(
        'Structure.structureId'), nullable=False, index=True)
    mixtureId = db.Column(
        db.ForeignKey('FitStructureToExperimentalData.fitStructureToExperimentalDataId'),
        nullable=False,
        index=True)
    volumeFraction = db.Column(db.String(45))
    creationDate = db.Column(db.DateTime)

    FitStructureToExperimentalDatum = db.relationship(
        'FitStructureToExperimentalDatum',
        primaryjoin='MixtureToStructure.mixtureId == FitStructureToExperimentalDatum.fitStructureToExperimentalDataId')
    Structure = db.relationship(
        'Structure',
        primaryjoin='MixtureToStructure.structureId == Structure.structureId')


class Model(db.Model):
    __tablename__ = 'Model'

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
    __tablename__ = 'ModelBuilding'

    modelBuildingId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    phasingAnalysisId = db.Column(
        db.ForeignKey(
            'PhasingAnalysis.phasingAnalysisId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related phasing analysis item')
    phasingProgramRunId = db.Column(
        db.ForeignKey(
            'PhasingProgramRun.phasingProgramRunId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related program item')
    spaceGroupId = db.Column(
        db.ForeignKey(
            'SpaceGroup.spaceGroupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='Related spaceGroup')
    lowRes = db.Column(db.Float(asdecimal=True))
    highRes = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')

    PhasingAnalysi = db.relationship(
        'PhasingAnalysi',
        primaryjoin='ModelBuilding.phasingAnalysisId == PhasingAnalysi.phasingAnalysisId')
    PhasingProgramRun = db.relationship(
        'PhasingProgramRun',
        primaryjoin='ModelBuilding.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId')
    SpaceGroup = db.relationship(
        'SpaceGroup',
        primaryjoin='ModelBuilding.spaceGroupId == SpaceGroup.spaceGroupId')


class ModelList(db.Model):
    __tablename__ = 'ModelList'

    modelListId = db.Column(db.Integer, primary_key=True)
    nsdFilePath = db.Column(db.String(255))
    chi2RgFilePath = db.Column(db.String(255))


class ModelToList(db.Model):
    __tablename__ = 'ModelToList'

    modelToListId = db.Column(db.Integer, primary_key=True)
    modelId = db.Column(db.ForeignKey('Model.modelId'),
                        nullable=False, index=True)
    modelListId = db.Column(db.ForeignKey(
        'ModelList.modelListId'), nullable=False, index=True)

    Model = db.relationship(
        'Model', primaryjoin='ModelToList.modelId == Model.modelId')
    ModelList = db.relationship(
        'ModelList',
        primaryjoin='ModelToList.modelListId == ModelList.modelListId')


class MotionCorrection(db.Model):
    __tablename__ = 'MotionCorrection'

    motionCorrectionId = db.Column(db.Integer, primary_key=True)
    movieId = db.Column(db.ForeignKey('Movie.movieId'), index=True)
    firstFrame = db.Column(db.String(45))
    lastFrame = db.Column(db.String(45))
    dosePerFrame = db.Column(db.String(45))
    doseWeight = db.Column(db.String(45))
    totalMotion = db.Column(db.String(45))
    averageMotionPerFrame = db.Column(db.String(45))
    driftPlotFullPath = db.Column(db.String(512))
    micrographFullPath = db.Column(db.String(512))
    micrographSnapshotFullPath = db.Column(db.String(512))
    correctedDoseMicrographFullPath = db.Column(db.String(512))
    patchesUsed = db.Column(db.String(45))
    logFileFullPath = db.Column(db.String(512))
    createdTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())

    Movie = db.relationship(
        'Movie', primaryjoin='MotionCorrection.movieId == Movie.movieId')


class MotorPosition(db.Model):
    __tablename__ = 'MotorPosition'

    motorPositionId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
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
        info='Creation or last update date/time')


class Movie(db.Model):
    __tablename__ = 'Movie'

    movieId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.ForeignKey(
        'DataCollection.dataCollectionId'), index=True)
    movieNumber = db.Column(db.Integer)
    movieFullPath = db.Column(db.String(255), index=True)
    positionX = db.Column(db.String(45))
    positionY = db.Column(db.String(45))
    micrographFullPath = db.Column(db.String(255))
    micrographSnapshotFullPath = db.Column(db.String(255))
    xmlMetaDataFullPath = db.Column(db.String(255))
    dosePerImage = db.Column(db.String(45))
    createdTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())

    DataCollection = db.relationship(
        'DataCollection',
        primaryjoin='Movie.dataCollectionId == DataCollection.dataCollectionId')


class PDB(db.Model):
    __tablename__ = 'PDB'

    pdbId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    contents = db.Column(db.String)
    code = db.Column(db.String(4))


class PDBEntry(db.Model):
    __tablename__ = 'PDBEntry'

    pdbEntryId = db.Column(db.Integer, primary_key=True)
    autoProcProgramId = db.Column(db.ForeignKey(
        'AutoProcProgram.autoProcProgramId', ondelete='CASCADE'), index=True)
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

    AutoProcProgram = db.relationship(
        'AutoProcProgram',
        primaryjoin='PDBEntry.autoProcProgramId == AutoProcProgram.autoProcProgramId')


class PDBEntryHasAutoProcProgram(db.Model):
    __tablename__ = 'PDBEntry_has_AutoProcProgram'

    pdbEntryHasAutoProcId = db.Column(db.Integer, primary_key=True)
    pdbEntryId = db.Column(db.ForeignKey(
        'PDBEntry.pdbEntryId', ondelete='CASCADE'), nullable=False, index=True)
    autoProcProgramId = db.Column(
        db.ForeignKey(
            'AutoProcProgram.autoProcProgramId',
            ondelete='CASCADE'),
        nullable=False,
        index=True)
    distance = db.Column(db.Float)

    AutoProcProgram = db.relationship(
        'AutoProcProgram',
        primaryjoin='PDBEntryHasAutoProcProgram.autoProcProgramId == AutoProcProgram.autoProcProgramId')
    PDBEntry = db.relationship(
        'PDBEntry',
        primaryjoin='PDBEntryHasAutoProcProgram.pdbEntryId == PDBEntry.pdbEntryId')


class PHPSession(db.Model):
    __tablename__ = 'PHPSession'

    id = db.Column(db.String(50), primary_key=True)
    accessDate = db.Column(db.DateTime)
    data = db.Column(db.String(4000))


class Particle(db.Model):
    __tablename__ = 'Particle'

    particleId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(
        db.ForeignKey(
            'DataCollection.dataCollectionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    x = db.Column(db.Float)
    y = db.Column(db.Float)

    DataCollection = db.relationship(
        'DataCollection',
        primaryjoin='Particle.dataCollectionId == DataCollection.dataCollectionId')


class ParticleClassification(db.Model):
    __tablename__ = 'ParticleClassification'

    particleClassificationId = db.Column(db.Integer, primary_key=True)
    particleClassificationGroupId = db.Column(
        db.ForeignKey(
            'ParticleClassificationGroup.particleClassificationGroupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    classNumber = db.Column(
        db.Integer,
        info='Identified of the class. A unique ID given by Relion')
    classImageFullPath = db.Column(db.String(255), info='The PNG of the class')
    particlesPerClass = db.Column(
        db.Integer,
        info='Number of particles within the selected class, can then be used together with the total number above to calculate the percentage')
    classDistribution = db.Column(db.Float)
    rotationAccuracy = db.Column(db.Float)
    translationAccuracy = db.Column(db.Float, info='Unit: Angstroms')
    estimatedResolution = db.Column(db.Float, info='Unit: Angstroms')
    overallFourierCompleteness = db.Column(db.Float)

    ParticleClassificationGroup = db.relationship(
        'ParticleClassificationGroup',
        primaryjoin='ParticleClassification.particleClassificationGroupId == ParticleClassificationGroup.particleClassificationGroupId')


class ParticleClassificationGroup(db.Model):
    __tablename__ = 'ParticleClassificationGroup'

    particleClassificationGroupId = db.Column(db.Integer, primary_key=True)
    particlePickerId = db.Column(
        db.ForeignKey(
            'ParticlePicker.particlePickerId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    programId = db.Column(db.ForeignKey(
        'AutoProcProgram.autoProcProgramId', onupdate='CASCADE'), index=True)
    type = db.Column(db.Enum('2D', '3D'),
                     info='Indicates the type of particle classification')
    batchNumber = db.Column(db.Integer, info='Corresponding to batch number')
    numberOfParticlesPerBatch = db.Column(
        db.Integer, info='total number of particles per batch (a large integer)')
    numberOfClassesPerBatch = db.Column(db.Integer)
    symmetry = db.Column(db.String(20))

    ParticlePicker = db.relationship(
        'ParticlePicker',
        primaryjoin='ParticleClassificationGroup.particlePickerId == ParticlePicker.particlePickerId')
    AutoProcProgram = db.relationship(
        'AutoProcProgram',
        primaryjoin='ParticleClassificationGroup.programId == AutoProcProgram.autoProcProgramId')


t_ParticleClassification_has_CryoemInitialModel = db.Table(
    'ParticleClassification_has_CryoemInitialModel',
    db.Column(
        'particleClassificationId',
        db.ForeignKey(
            'ParticleClassification.particleClassificationId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'cryoemInitialModelId',
        db.ForeignKey(
            'CryoemInitialModel.cryoemInitialModelId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


class ParticlePicker(db.Model):
    __tablename__ = 'ParticlePicker'

    particlePickerId = db.Column(db.Integer, primary_key=True)
    programId = db.Column(db.ForeignKey(
        'AutoProcProgram.autoProcProgramId', onupdate='CASCADE'), index=True)
    firstMotionCorrectionId = db.Column(db.ForeignKey(
        'MotionCorrection.motionCorrectionId', onupdate='CASCADE'), index=True)
    particlePickingTemplate = db.Column(db.String(255), info='Cryolo model')
    particleDiameter = db.Column(db.Float, info='Unit: nm')
    numberOfParticles = db.Column(db.Integer)
    summaryImageFullPath = db.Column(
        db.String(255),
        info='Generated summary micrograph image with highlighted particles')

    MotionCorrection = db.relationship(
        'MotionCorrection',
        primaryjoin='ParticlePicker.firstMotionCorrectionId == MotionCorrection.motionCorrectionId')
    AutoProcProgram = db.relationship(
        'AutoProcProgram',
        primaryjoin='ParticlePicker.programId == AutoProcProgram.autoProcProgramId')


class Permission(db.Model):
    __tablename__ = 'Permission'

    permissionId = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(100))

    UserGroup = db.relationship(
        'UserGroup',
        secondary='UserGroup_has_Permission',
        backref="permissions")


class Person(db.Model):
    __tablename__ = 'Person'

    personId = db.Column(db.Integer, primary_key=True)
    laboratoryId = db.Column(db.ForeignKey(
        'Laboratory.laboratoryId'), index=True)
    siteId = db.Column(db.Integer, index=True)
    personUUID = db.Column(db.String(45))
    familyName = db.Column(db.String(100), index=True)
    givenName = db.Column(db.String(45))
    title = db.Column(db.String(45))
    emailAddress = db.Column(db.String(60))
    phoneNumber = db.Column(db.String(45, 'utf8_unicode_ci'))
    login = db.Column(db.String(45), index=True)
    passwd = db.Column(db.String(45))
    faxNumber = db.Column(db.String(45))
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info='Creation or last update date/time')
    externalId = db.Column(db.BINARY(16))
    cache = db.Column(db.Text)

    Laboratory = db.relationship(
        'Laboratory',
        primaryjoin='Person.laboratoryId == Laboratory.laboratoryId')
    Project = db.relationship('Project', secondary='Project_has_Person')
    UserGroup = db.relationship('UserGroup', secondary='UserGroup_has_Person')


class Phasing(db.Model):
    __tablename__ = 'Phasing'

    phasingId = db.Column(db.Integer, primary_key=True,
                          info='Primary key (auto-incremented)')
    phasingAnalysisId = db.Column(
        db.ForeignKey(
            'PhasingAnalysis.phasingAnalysisId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related phasing analysis item')
    phasingProgramRunId = db.Column(
        db.ForeignKey(
            'PhasingProgramRun.phasingProgramRunId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related program item')
    spaceGroupId = db.Column(
        db.ForeignKey(
            'SpaceGroup.spaceGroupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='Related spaceGroup')
    method = db.Column(db.Enum('solvent flattening',
                       'solvent flipping'), info='phasing method')
    solventContent = db.Column(db.Float(asdecimal=True))
    enantiomorph = db.Column(db.Integer, info='0 or 1')
    lowRes = db.Column(db.Float(asdecimal=True))
    highRes = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())

    PhasingAnalysi = db.relationship(
        'PhasingAnalysi',
        primaryjoin='Phasing.phasingAnalysisId == PhasingAnalysi.phasingAnalysisId')
    PhasingProgramRun = db.relationship(
        'PhasingProgramRun',
        primaryjoin='Phasing.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId')
    SpaceGroup = db.relationship(
        'SpaceGroup',
        primaryjoin='Phasing.spaceGroupId == SpaceGroup.spaceGroupId')


class PhasingAnalysi(db.Model):
    __tablename__ = 'PhasingAnalysis'

    phasingAnalysisId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')


class PhasingProgramAttachment(db.Model):
    __tablename__ = 'PhasingProgramAttachment'

    phasingProgramAttachmentId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    phasingProgramRunId = db.Column(
        db.ForeignKey(
            'PhasingProgramRun.phasingProgramRunId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related program item')
    fileType = db.Column(
        db.Enum(
            'DSIGMA_RESOLUTION',
            'OCCUPANCY_SITENUMBER',
            'CONTRAST_CYCLE',
            'CCALL_CCWEAK',
            'IMAGE',
            'Map',
            'Logfile',
            'PDB',
            'CSV',
            'INS',
            'RES',
            'TXT'),
        info='file type')
    fileName = db.Column(db.String(45), info='file name')
    filePath = db.Column(db.String(255), info='file path')
    input = db.Column(db.Integer)
    recordTimeStamp = db.Column(db.DateTime, server_default=db.FetchedValue(
    ), info='Creation or last update date/time')

    PhasingProgramRun = db.relationship(
        'PhasingProgramRun',
        primaryjoin='PhasingProgramAttachment.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId')


class PhasingProgramRun(db.Model):
    __tablename__ = 'PhasingProgramRun'

    phasingProgramRunId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    phasingCommandLine = db.Column(
        db.String(255), info='Command line for phasing')
    phasingPrograms = db.Column(
        db.String(255), info='Phasing programs (comma separated)')
    phasingStatus = db.Column(db.Integer, info='success (1) / fail (0)')
    phasingMessage = db.Column(db.String(255), info='warning, error,...')
    phasingStartTime = db.Column(db.DateTime, info='Processing start time')
    phasingEndTime = db.Column(db.DateTime, info='Processing end time')
    phasingEnvironment = db.Column(db.String(255), info='Cpus, Nodes,...')
    phasingDirectory = db.Column(db.String(255), info='Directory of execution')
    recordTimeStamp = db.Column(db.DateTime, server_default=db.FetchedValue(
    ), info='Creation or last update date/time')


class PhasingStatistic(db.Model):
    __tablename__ = 'PhasingStatistics'

    phasingStatisticsId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    phasingHasScalingId1 = db.Column(
        db.ForeignKey(
            'Phasing_has_Scaling.phasingHasScalingId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='the dataset in question')
    phasingHasScalingId2 = db.Column(
        db.ForeignKey(
            'Phasing_has_Scaling.phasingHasScalingId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='if this is MIT or MAD, which scaling are being compared, null otherwise')
    phasingStepId = db.Column(db.ForeignKey(
        'PhasingStep.phasingStepId'), index=True)
    numberOfBins = db.Column(db.Integer, info='the total number of bins')
    binNumber = db.Column(db.Integer, info='binNumber, 999 for overall')
    lowRes = db.Column(db.Float(asdecimal=True),
                       info='low resolution cutoff of this binfloat')
    highRes = db.Column(db.Float(asdecimal=True),
                        info='high resolution cutoff of this binfloat')
    metric = db.Column(
        db.Enum(
            'Rcullis',
            'Average Fragment Length',
            'Chain Count',
            'Residues Count',
            'CC',
            'PhasingPower',
            'FOM',
            '<d"/sig>',
            'Best CC',
            'CC(1/2)',
            'Weak CC',
            'CFOM',
            'Pseudo_free_CC',
            'CC of partial model',
            'Start R-work',
            'Start R-free',
            'Final R-work',
            'Final R-free'),
        info='metric')
    statisticsValue = db.Column(
        db.Float(asdecimal=True), info='the statistics value')
    nReflections = db.Column(db.Integer)
    recordTimeStamp = db.Column(db.DateTime, server_default=db.FetchedValue(
    ), info='Creation or last update date/time')

    Phasing_has_Scaling = db.relationship(
        'PhasingHasScaling',
        primaryjoin='PhasingStatistic.phasingHasScalingId1 == PhasingHasScaling.phasingHasScalingId')
    Phasing_has_Scaling1 = db.relationship(
        'PhasingHasScaling',
        primaryjoin='PhasingStatistic.phasingHasScalingId2 == PhasingHasScaling.phasingHasScalingId')
    PhasingStep = db.relationship(
        'PhasingStep',
        primaryjoin='PhasingStatistic.phasingStepId == PhasingStep.phasingStepId')


class PhasingStep(db.Model):
    __tablename__ = 'PhasingStep'

    phasingStepId = db.Column(db.Integer, primary_key=True)
    previousPhasingStepId = db.Column(db.Integer)
    programRunId = db.Column(db.ForeignKey(
        'PhasingProgramRun.phasingProgramRunId'), index=True)
    spaceGroupId = db.Column(db.ForeignKey(
        'SpaceGroup.spaceGroupId'), index=True)
    autoProcScalingId = db.Column(db.ForeignKey(
        'AutoProcScaling.autoProcScalingId'), index=True)
    phasingAnalysisId = db.Column(db.Integer, index=True)
    phasingStepType = db.Column(
        db.Enum(
            'PREPARE',
            'SUBSTRUCTUREDETERMINATION',
            'PHASING',
            'MODELBUILDING',
            'REFINEMENT',
            'LIGAND_FIT'))
    method = db.Column(db.String(45))
    solventContent = db.Column(db.String(45))
    enantiomorph = db.Column(db.String(45))
    lowRes = db.Column(db.String(45))
    highRes = db.Column(db.String(45))
    groupName = db.Column(db.String(45))
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())

    AutoProcScaling = db.relationship(
        'AutoProcScaling',
        primaryjoin='PhasingStep.autoProcScalingId == AutoProcScaling.autoProcScalingId')
    PhasingProgramRun = db.relationship(
        'PhasingProgramRun',
        primaryjoin='PhasingStep.programRunId == PhasingProgramRun.phasingProgramRunId')
    SpaceGroup = db.relationship(
        'SpaceGroup',
        primaryjoin='PhasingStep.spaceGroupId == SpaceGroup.spaceGroupId')


class PhasingHasScaling(db.Model):
    __tablename__ = 'Phasing_has_Scaling'

    phasingHasScalingId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    phasingAnalysisId = db.Column(
        db.ForeignKey(
            'PhasingAnalysis.phasingAnalysisId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related phasing analysis item')
    autoProcScalingId = db.Column(
        db.ForeignKey(
            'AutoProcScaling.autoProcScalingId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related autoProcScaling item')
    datasetNumber = db.Column(
        db.Integer,
        info='serial number of the dataset and always reserve 0 for the reference')
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())

    AutoProcScaling = db.relationship(
        'AutoProcScaling',
        primaryjoin='PhasingHasScaling.autoProcScalingId == AutoProcScaling.autoProcScalingId')
    PhasingAnalysi = db.relationship(
        'PhasingAnalysi',
        primaryjoin='PhasingHasScaling.phasingAnalysisId == PhasingAnalysi.phasingAnalysisId')


class PlateGroup(db.Model):
    __tablename__ = 'PlateGroup'

    plateGroupId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    storageTemperature = db.Column(db.String(45))


class PlateType(db.Model):
    __tablename__ = 'PlateType'

    PlateTypeId = db.Column(db.Integer, primary_key=True)
    experimentId = db.Column(db.Integer, index=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(45))
    shape = db.Column(db.String(45))
    rowCount = db.Column(db.Integer)
    columnCount = db.Column(db.Integer)


class Position(db.Model):
    __tablename__ = 'Position'

    positionId = db.Column(db.Integer, primary_key=True,
                           info='Primary key (auto-incremented)')
    relativePositionId = db.Column(
        db.ForeignKey(
            'Position.positionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='relative position, null otherwise')
    posX = db.Column(db.Float(asdecimal=True))
    posY = db.Column(db.Float(asdecimal=True))
    posZ = db.Column(db.Float(asdecimal=True))
    scale = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')

    parent = db.relationship(
        'Position',
        remote_side=[positionId],
        primaryjoin='Position.relativePositionId == Position.positionId')


class PreparePhasingDatum(db.Model):
    __tablename__ = 'PreparePhasingData'

    preparePhasingDataId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    phasingAnalysisId = db.Column(
        db.ForeignKey(
            'PhasingAnalysis.phasingAnalysisId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related phasing analysis item')
    phasingProgramRunId = db.Column(
        db.ForeignKey(
            'PhasingProgramRun.phasingProgramRunId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related program item')
    spaceGroupId = db.Column(
        db.ForeignKey(
            'SpaceGroup.spaceGroupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='Related spaceGroup')
    lowRes = db.Column(db.Float(asdecimal=True))
    highRes = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')

    PhasingAnalysi = db.relationship(
        'PhasingAnalysi',
        primaryjoin='PreparePhasingDatum.phasingAnalysisId == PhasingAnalysi.phasingAnalysisId')
    PhasingProgramRun = db.relationship(
        'PhasingProgramRun',
        primaryjoin='PreparePhasingDatum.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId')
    SpaceGroup = db.relationship(
        'SpaceGroup',
        primaryjoin='PreparePhasingDatum.spaceGroupId == SpaceGroup.spaceGroupId')


class Project(db.Model):
    __tablename__ = 'Project'

    projectId = db.Column(db.Integer, primary_key=True)
    personId = db.Column(db.ForeignKey('Person.personId'), index=True)
    title = db.Column(db.String(200))
    acronym = db.Column(db.String(100))
    owner = db.Column(db.String(50))

    Person = db.relationship(
        'Person', primaryjoin='Project.personId == Person.personId')
    Protein = db.relationship('Protein', secondary='Project_has_Protein')
    BLSession = db.relationship('BLSession', secondary='Project_has_Session')
    Shipping = db.relationship('Shipping', secondary='Project_has_Shipping')
    XFEFluorescenceSpectrum = db.relationship(
        'XFEFluorescenceSpectrum', secondary='Project_has_XFEFSpectrum')


t_Project_has_BLSample = db.Table(
    'Project_has_BLSample',
    db.Column(
        'projectId',
        db.ForeignKey(
            'Project.projectId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'blSampleId',
        db.ForeignKey(
            'BLSample.blSampleId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


t_Project_has_DCGroup = db.Table(
    'Project_has_DCGroup',
    db.Column(
        'projectId',
        db.ForeignKey(
            'Project.projectId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'dataCollectionGroupId',
        db.ForeignKey(
            'DataCollectionGroup.dataCollectionGroupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


t_Project_has_EnergyScan = db.Table(
    'Project_has_EnergyScan',
    db.Column(
        'projectId',
        db.ForeignKey(
            'Project.projectId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'energyScanId',
        db.ForeignKey(
            'EnergyScan.energyScanId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


t_Project_has_Person = db.Table(
    'Project_has_Person',
    db.Column(
        'projectId',
        db.ForeignKey(
            'Project.projectId',
            ondelete='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'personId',
        db.ForeignKey(
            'Person.personId',
            ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


t_Project_has_Protein = db.Table(
    'Project_has_Protein',
    db.Column(
        'projectId',
        db.ForeignKey(
            'Project.projectId',
            ondelete='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'proteinId',
        db.ForeignKey(
            'Protein.proteinId',
            ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


t_Project_has_Session = db.Table(
    'Project_has_Session',
    db.Column(
        'projectId',
        db.ForeignKey(
            'Project.projectId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'sessionId',
        db.ForeignKey(
            'BLSession.sessionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


t_Project_has_Shipping = db.Table(
    'Project_has_Shipping',
    db.Column(
        'projectId',
        db.ForeignKey(
            'Project.projectId',
            ondelete='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'shippingId',
        db.ForeignKey(
            'Shipping.shippingId',
            ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


class ProjectHasUser(db.Model):
    __tablename__ = 'Project_has_User'

    projecthasuserid = db.Column(db.Integer, primary_key=True)
    projectid = db.Column(db.ForeignKey(
        'Project.projectId'), nullable=False, index=True)
    username = db.Column(db.String(15))

    Project = db.relationship(
        'Project', primaryjoin='ProjectHasUser.projectid == Project.projectId')


t_Project_has_XFEFSpectrum = db.Table(
    'Project_has_XFEFSpectrum',
    db.Column(
        'projectId',
        db.ForeignKey(
            'Project.projectId',
            ondelete='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'xfeFluorescenceSpectrumId',
        db.ForeignKey(
            'XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId',
            ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


class Proposal(db.Model):
    __tablename__ = 'Proposal'
    __table_args__ = (
        db.Index('Proposal_FKIndexCodeNumber',
                 'proposalCode', 'proposalNumber'),
    )

    proposalId = db.Column(db.Integer, primary_key=True)
    personId = db.Column(
        db.ForeignKey(
            'Person.personId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    title = db.Column(db.String(200, 'utf8mb4_unicode_ci'))
    proposalCode = db.Column(db.String(45))
    proposalNumber = db.Column(db.String(45))
    proposalType = db.Column(db.String(2), info='Proposal type: MX, BX')
    bltimeStamp = db.Column(db.DateTime, nullable=False,
                            server_default=db.FetchedValue())
    externalId = db.Column(db.BINARY(16))
    state = db.Column(db.Enum('Open', 'Closed', 'Cancelled'),
                      server_default=db.FetchedValue())

    Person = db.relationship(
        'Person', primaryjoin='Proposal.personId == Person.personId')


class ProposalHasPerson(db.Model):
    __tablename__ = 'ProposalHasPerson'

    proposalHasPersonId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.ForeignKey(
        'Proposal.proposalId'), nullable=False, index=True)
    personId = db.Column(db.ForeignKey('Person.personId'),
                         nullable=False, index=True)

    Person = db.relationship(
        'Person', primaryjoin='ProposalHasPerson.personId == Person.personId')
    Proposal = db.relationship(
        'Proposal',
        primaryjoin='ProposalHasPerson.proposalId == Proposal.proposalId')


class Protein(db.Model):
    __tablename__ = 'Protein'
    __table_args__ = (
        db.Index('ProteinAcronym_Index', 'proposalId', 'acronym'),
    )

    proteinId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(
        db.ForeignKey(
            'Proposal.proposalId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    name = db.Column(db.String(255, 'utf8mb4_unicode_ci'))
    acronym = db.Column(db.String(45), index=True)
    description = db.Column(
        db.Text, info='A description/summary using words and sentences')
    hazardGroup = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue(),
        info='A.k.a. risk group')
    containmentLevel = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue(),
        info='A.k.a. biosafety level, which indicates the level of containment required')
    safetyLevel = db.Column(db.Enum('GREEN', 'YELLOW', 'RED'))
    molecularMass = db.Column(db.Float(asdecimal=True))
    proteinType = db.Column(db.String(45))
    sequence = db.Column(db.Text)
    personId = db.Column(db.Integer, index=True)
    bltimeStamp = db.Column(db.DateTime, nullable=False,
                            server_default=db.FetchedValue())
    isCreatedBySampleSheet = db.Column(
        db.Integer, server_default=db.FetchedValue())
    externalId = db.Column(db.BINARY(16))
    componentTypeId = db.Column(
        db.ForeignKey(
            'ComponentType.componentTypeId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    modId = db.Column(db.String(20))
    concentrationTypeId = db.Column(db.Integer)
    _global = db.Column('global', db.Integer, server_default=db.FetchedValue())

    ComponentType = db.relationship(
        'ComponentType',
        primaryjoin='Protein.componentTypeId == ComponentType.componentTypeId')
    Proposal = db.relationship(
        'Proposal', primaryjoin='Protein.proposalId == Proposal.proposalId')
    ComponentSubType = db.relationship(
        'ComponentSubType', secondary='Component_has_SubType')


class ProteinHasLattice(Protein):
    __tablename__ = 'Protein_has_Lattice'

    proteinId = db.Column(db.ForeignKey('Protein.proteinId'), primary_key=True)
    cell_a = db.Column(db.Float(asdecimal=True))
    cell_b = db.Column(db.Float(asdecimal=True))
    cell_c = db.Column(db.Float(asdecimal=True))
    cell_alpha = db.Column(db.Float(asdecimal=True))
    cell_beta = db.Column(db.Float(asdecimal=True))
    cell_gamma = db.Column(db.Float(asdecimal=True))


class ProteinHasPDB(db.Model):
    __tablename__ = 'Protein_has_PDB'

    proteinhaspdbid = db.Column(db.Integer, primary_key=True)
    proteinid = db.Column(db.ForeignKey(
        'Protein.proteinId'), nullable=False, index=True)
    pdbid = db.Column(db.ForeignKey('PDB.pdbId'), nullable=False, index=True)

    PDB = db.relationship(
        'PDB', primaryjoin='ProteinHasPDB.pdbid == PDB.pdbId')
    Protein = db.relationship(
        'Protein', primaryjoin='ProteinHasPDB.proteinid == Protein.proteinId')


class RigidBodyModeling(db.Model):
    __tablename__ = 'RigidBodyModeling'

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
    __tablename__ = 'RobotAction'

    robotActionId = db.Column(db.Integer, primary_key=True)
    blsessionId = db.Column(db.ForeignKey(
        'BLSession.sessionId'), nullable=False, index=True)
    blsampleId = db.Column(db.ForeignKey('BLSample.blSampleId'), index=True)
    actionType = db.Column(
        db.Enum('LOAD', 'UNLOAD', 'DISPOSE', 'STORE', 'WASH', 'ANNEAL'))
    startTimestamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())
    endTimestamp = db.Column(db.DateTime, nullable=False,
                             server_default=db.FetchedValue())
    status = db.Column(
        db.Enum('SUCCESS', 'ERROR', 'CRITICAL', 'WARNING', 'COMMANDNOTSENT'))
    message = db.Column(db.String(255))
    containerLocation = db.Column(db.SmallInteger)
    dewarLocation = db.Column(db.SmallInteger)
    sampleBarcode = db.Column(db.String(45))
    xtalSnapshotBefore = db.Column(db.String(255))
    xtalSnapshotAfter = db.Column(db.String(255))

    BLSample = db.relationship(
        'BLSample',
        primaryjoin='RobotAction.blsampleId == BLSample.blSampleId')
    BLSession = db.relationship(
        'BLSession',
        primaryjoin='RobotAction.blsessionId == BLSession.sessionId')


class Run(db.Model):
    __tablename__ = 'Run'

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
    __tablename__ = 'SW_onceToken'

    onceTokenId = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(128))
    personId = db.Column(db.ForeignKey('Person.personId'), index=True)
    proposalId = db.Column(db.ForeignKey('Proposal.proposalId'), index=True)
    validity = db.Column(db.String(200))
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())

    Person = db.relationship(
        'Person', primaryjoin='SWOnceToken.personId == Person.personId')
    Proposal = db.relationship(
        'Proposal',
        primaryjoin='SWOnceToken.proposalId == Proposal.proposalId')


class SafetyLevel(db.Model):
    __tablename__ = 'SafetyLevel'

    safetyLevelId = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(45))
    description = db.Column(db.String(45))


class SamplePlate(db.Model):
    __tablename__ = 'SamplePlate'

    samplePlateId = db.Column(db.Integer, primary_key=True)
    experimentId = db.Column(db.ForeignKey(
        'Experiment.experimentId'), nullable=False, index=True)
    plateGroupId = db.Column(db.ForeignKey(
        'PlateGroup.plateGroupId'), index=True)
    plateTypeId = db.Column(db.ForeignKey('PlateType.PlateTypeId'), index=True)
    instructionSetId = db.Column(db.ForeignKey(
        'InstructionSet.instructionSetId'), index=True)
    boxId = db.Column(db.Integer)
    name = db.Column(db.String(45))
    slotPositionRow = db.Column(db.String(45))
    slotPositionColumn = db.Column(db.String(45))
    storageTemperature = db.Column(db.String(45))

    Experiment = db.relationship(
        'Experiment',
        primaryjoin='SamplePlate.experimentId == Experiment.experimentId')
    InstructionSet = db.relationship(
        'InstructionSet',
        primaryjoin='SamplePlate.instructionSetId == InstructionSet.instructionSetId')
    PlateGroup = db.relationship(
        'PlateGroup',
        primaryjoin='SamplePlate.plateGroupId == PlateGroup.plateGroupId')
    PlateType = db.relationship(
        'PlateType',
        primaryjoin='SamplePlate.plateTypeId == PlateType.PlateTypeId')


class SamplePlatePosition(db.Model):
    __tablename__ = 'SamplePlatePosition'

    samplePlatePositionId = db.Column(db.Integer, primary_key=True)
    samplePlateId = db.Column(db.ForeignKey(
        'SamplePlate.samplePlateId'), nullable=False, index=True)
    rowNumber = db.Column(db.Integer)
    columnNumber = db.Column(db.Integer)
    volume = db.Column(db.String(45))

    SamplePlate = db.relationship(
        'SamplePlate',
        primaryjoin='SamplePlatePosition.samplePlateId == SamplePlate.samplePlateId')


class SaxsDataCollection(db.Model):
    __tablename__ = 'SaxsDataCollection'

    dataCollectionId = db.Column(db.Integer, primary_key=True)
    experimentId = db.Column(db.ForeignKey(
        'Experiment.experimentId'), nullable=False, index=True)
    comments = db.Column(db.String(5120))

    Experiment = db.relationship(
        'Experiment',
        primaryjoin='SaxsDataCollection.experimentId == Experiment.experimentId')


class ScanParametersModel(db.Model):
    __tablename__ = 'ScanParametersModel'

    scanParametersModelId = db.Column(db.Integer, primary_key=True)
    scanParametersServiceId = db.Column(
        db.ForeignKey(
            'ScanParametersService.scanParametersServiceId',
            onupdate='CASCADE'),
        index=True)
    dataCollectionPlanId = db.Column(db.ForeignKey(
        'DiffractionPlan.diffractionPlanId', onupdate='CASCADE'), index=True)
    modelNumber = db.Column(db.Integer)
    start = db.Column(db.Float(asdecimal=True))
    stop = db.Column(db.Float(asdecimal=True))
    step = db.Column(db.Float(asdecimal=True))
    array = db.Column(db.Text)

    DiffractionPlan = db.relationship(
        'DiffractionPlan',
        primaryjoin='ScanParametersModel.dataCollectionPlanId == DiffractionPlan.diffractionPlanId')
    ScanParametersService = db.relationship(
        'ScanParametersService',
        primaryjoin='ScanParametersModel.scanParametersServiceId == ScanParametersService.scanParametersServiceId')


class ScanParametersService(db.Model):
    __tablename__ = 'ScanParametersService'

    scanParametersServiceId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(45))


class Schedule(db.Model):
    __tablename__ = 'Schedule'

    scheduleId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))


class ScheduleComponent(db.Model):
    __tablename__ = 'ScheduleComponent'

    scheduleComponentId = db.Column(db.Integer, primary_key=True)
    scheduleId = db.Column(
        db.ForeignKey(
            'Schedule.scheduleId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    inspectionTypeId = db.Column(db.ForeignKey(
        'InspectionType.inspectionTypeId', ondelete='CASCADE'), index=True)
    offset_hours = db.Column(db.Integer)

    InspectionType = db.relationship(
        'InspectionType',
        primaryjoin='ScheduleComponent.inspectionTypeId == InspectionType.inspectionTypeId')
    Schedule = db.relationship(
        'Schedule',
        primaryjoin='ScheduleComponent.scheduleId == Schedule.scheduleId')


class SchemaStatu(db.Model):
    __tablename__ = 'SchemaStatus'

    schemaStatusId = db.Column(db.Integer, primary_key=True)
    scriptName = db.Column(db.String(100), nullable=False, unique=True)
    schemaStatus = db.Column(db.String(10))
    recordTimeStamp = db.Column(
        db.DateTime, nullable=False, server_default=db.FetchedValue())


class Screen(db.Model):
    __tablename__ = 'Screen'

    screenId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    proposalId = db.Column(db.ForeignKey('Proposal.proposalId'), index=True)
    _global = db.Column('global', db.Integer)

    Proposal = db.relationship(
        'Proposal', primaryjoin='Screen.proposalId == Proposal.proposalId')


class ScreenComponent(db.Model):
    __tablename__ = 'ScreenComponent'

    screenComponentId = db.Column(db.Integer, primary_key=True)
    screenComponentGroupId = db.Column(
        db.ForeignKey('ScreenComponentGroup.screenComponentGroupId'),
        nullable=False,
        index=True)
    componentId = db.Column(db.ForeignKey('Protein.proteinId'), index=True)
    concentration = db.Column(db.Float)
    pH = db.Column(db.Float)

    Protein = db.relationship(
        'Protein',
        primaryjoin='ScreenComponent.componentId == Protein.proteinId')
    ScreenComponentGroup = db.relationship(
        'ScreenComponentGroup',
        primaryjoin='ScreenComponent.screenComponentGroupId == ScreenComponentGroup.screenComponentGroupId')


class ScreenComponentGroup(db.Model):
    __tablename__ = 'ScreenComponentGroup'

    screenComponentGroupId = db.Column(db.Integer, primary_key=True)
    screenId = db.Column(db.ForeignKey('Screen.screenId'),
                         nullable=False, index=True)
    position = db.Column(db.SmallInteger)

    Screen = db.relationship(
        'Screen',
        primaryjoin='ScreenComponentGroup.screenId == Screen.screenId')


class Screening(db.Model):
    __tablename__ = 'Screening'

    screeningId = db.Column(db.Integer, primary_key=True)
    diffractionPlanId = db.Column(
        db.Integer, index=True, info='references DiffractionPlan')
    dataCollectionGroupId = db.Column(db.ForeignKey(
        'DataCollectionGroup.dataCollectionGroupId'), index=True)
    dataCollectionId = db.Column(db.Integer)
    bltimeStamp = db.Column(db.DateTime, nullable=False,
                            server_default=db.FetchedValue())
    programVersion = db.Column(db.String(45))
    comments = db.Column(db.String(255))
    shortComments = db.Column(db.String(20))
    xmlSampleInformation = db.Column(db.LONGBLOB)

    DataCollectionGroup = db.relationship(
        'DataCollectionGroup',
        primaryjoin='Screening.dataCollectionGroupId == DataCollectionGroup.dataCollectionGroupId')


class ScreeningInput(db.Model):
    __tablename__ = 'ScreeningInput'

    screeningInputId = db.Column(db.Integer, primary_key=True)
    screeningId = db.Column(
        db.ForeignKey(
            'Screening.screeningId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    diffractionPlanId = db.Column(
        db.Integer, info='references DiffractionPlan table')
    beamX = db.Column(db.Float)
    beamY = db.Column(db.Float)
    rmsErrorLimits = db.Column(db.Float)
    minimumFractionIndexed = db.Column(db.Float)
    maximumFractionRejected = db.Column(db.Float)
    minimumSignalToNoise = db.Column(db.Float)
    xmlSampleInformation = db.Column(db.LONGBLOB)

    Screening = db.relationship(
        'Screening',
        primaryjoin='ScreeningInput.screeningId == Screening.screeningId')


class ScreeningOutput(db.Model):
    __tablename__ = 'ScreeningOutput'

    screeningOutputId = db.Column(db.Integer, primary_key=True)
    screeningId = db.Column(
        db.ForeignKey(
            'Screening.screeningId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
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
        db.Integer, nullable=False, server_default=db.FetchedValue())
    mosaicityEstimated = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue())
    rankingResolution = db.Column(db.Float(asdecimal=True))
    program = db.Column(db.String(45))
    doseTotal = db.Column(db.Float(asdecimal=True))
    totalExposureTime = db.Column(db.Float(asdecimal=True))
    totalRotationRange = db.Column(db.Float(asdecimal=True))
    totalNumberOfImages = db.Column(db.Integer)
    rFriedel = db.Column(db.Float(asdecimal=True))
    indexingSuccess = db.Column(
        db.Integer, nullable=False, server_default=db.FetchedValue())
    screeningSuccess = db.Column(db.Integer, server_default=db.FetchedValue())

    Screening = db.relationship(
        'Screening',
        primaryjoin='ScreeningOutput.screeningId == Screening.screeningId')


class ScreeningOutputLattice(db.Model):
    __tablename__ = 'ScreeningOutputLattice'

    screeningOutputLatticeId = db.Column(db.Integer, primary_key=True)
    screeningOutputId = db.Column(
        db.ForeignKey(
            'ScreeningOutput.screeningOutputId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
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

    ScreeningOutput = db.relationship(
        'ScreeningOutput',
        primaryjoin='ScreeningOutputLattice.screeningOutputId == ScreeningOutput.screeningOutputId')


class ScreeningRank(db.Model):
    __tablename__ = 'ScreeningRank'

    screeningRankId = db.Column(db.Integer, primary_key=True)
    screeningRankSetId = db.Column(
        db.ForeignKey(
            'ScreeningRankSet.screeningRankSetId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    screeningId = db.Column(
        db.ForeignKey(
            'Screening.screeningId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    rankValue = db.Column(db.Float)
    rankInformation = db.Column(db.String(1024))

    Screening = db.relationship(
        'Screening',
        primaryjoin='ScreeningRank.screeningId == Screening.screeningId')
    ScreeningRankSet = db.relationship(
        'ScreeningRankSet',
        primaryjoin='ScreeningRank.screeningRankSetId == ScreeningRankSet.screeningRankSetId')


class ScreeningRankSet(db.Model):
    __tablename__ = 'ScreeningRankSet'

    screeningRankSetId = db.Column(db.Integer, primary_key=True)
    rankEngine = db.Column(db.String(255))
    rankingProjectFileName = db.Column(db.String(255))
    rankingSummaryFileName = db.Column(db.String(255))


class ScreeningStrategy(db.Model):
    __tablename__ = 'ScreeningStrategy'

    screeningStrategyId = db.Column(db.Integer, primary_key=True)
    screeningOutputId = db.Column(
        db.ForeignKey(
            'ScreeningOutput.screeningOutputId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    phiStart = db.Column(db.Float)
    phiEnd = db.Column(db.Float)
    rotation = db.Column(db.Float)
    exposureTime = db.Column(db.Float)
    resolution = db.Column(db.Float)
    completeness = db.Column(db.Float)
    multiplicity = db.Column(db.Float)
    anomalous = db.Column(db.Integer, nullable=False,
                          server_default=db.FetchedValue())
    program = db.Column(db.String(45))
    rankingResolution = db.Column(db.Float)
    transmission = db.Column(
        db.Float,
        info='Transmission for the strategy as given by the strategy program.')

    ScreeningOutput = db.relationship(
        'ScreeningOutput',
        primaryjoin='ScreeningStrategy.screeningOutputId == ScreeningOutput.screeningOutputId')


class ScreeningStrategySubWedge(db.Model):
    __tablename__ = 'ScreeningStrategySubWedge'

    screeningStrategySubWedgeId = db.Column(
        db.Integer, primary_key=True, info='Primary key')
    screeningStrategyWedgeId = db.Column(
        db.ForeignKey(
            'ScreeningStrategyWedge.screeningStrategyWedgeId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='Foreign key to parent table')
    subWedgeNumber = db.Column(
        db.Integer, info='The number of this subwedge within the wedge')
    rotationAxis = db.Column(db.String(45), info='Angle where subwedge starts')
    axisStart = db.Column(db.Float, info='Angle where subwedge ends')
    axisEnd = db.Column(db.Float, info='Exposure time for subwedge')
    exposureTime = db.Column(db.Float, info='Transmission for subwedge')
    transmission = db.Column(db.Float)
    oscillationRange = db.Column(db.Float)
    completeness = db.Column(db.Float)
    multiplicity = db.Column(db.Float)
    doseTotal = db.Column(db.Float, info='Total dose for this subwedge')
    numberOfImages = db.Column(
        db.Integer, info='Number of images for this subwedge')
    comments = db.Column(db.String(255))
    resolution = db.Column(db.Float)

    ScreeningStrategyWedge = db.relationship(
        'ScreeningStrategyWedge',
        primaryjoin='ScreeningStrategySubWedge.screeningStrategyWedgeId == ScreeningStrategyWedge.screeningStrategyWedgeId')


class ScreeningStrategyWedge(db.Model):
    __tablename__ = 'ScreeningStrategyWedge'

    screeningStrategyWedgeId = db.Column(
        db.Integer, primary_key=True, info='Primary key')
    screeningStrategyId = db.Column(
        db.ForeignKey(
            'ScreeningStrategy.screeningStrategyId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='Foreign key to parent table')
    wedgeNumber = db.Column(
        db.Integer, info='The number of this wedge within the strategy')
    resolution = db.Column(db.Float)
    completeness = db.Column(db.Float)
    multiplicity = db.Column(db.Float)
    doseTotal = db.Column(db.Float, info='Total dose for this wedge')
    numberOfImages = db.Column(
        db.Integer, info='Number of images for this wedge')
    phi = db.Column(db.Float)
    kappa = db.Column(db.Float)
    chi = db.Column(db.Float)
    comments = db.Column(db.String(255))
    wavelength = db.Column(db.Float(asdecimal=True))

    ScreeningStrategy = db.relationship(
        'ScreeningStrategy',
        primaryjoin='ScreeningStrategyWedge.screeningStrategyId == ScreeningStrategy.screeningStrategyId')


class SessionType(db.Model):
    __tablename__ = 'SessionType'

    sessionTypeId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(
        db.ForeignKey(
            'BLSession.sessionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    typeName = db.Column(db.String(31), nullable=False)

    BLSession = db.relationship(
        'BLSession',
        primaryjoin='SessionType.sessionId == BLSession.sessionId')


class SessionHasPerson(db.Model):
    __tablename__ = 'Session_has_Person'

    sessionId = db.Column(
        db.ForeignKey(
            'BLSession.sessionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    personId = db.Column(
        db.ForeignKey(
            'Person.personId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
    role = db.Column(
        db.Enum(
            'Local Contact',
            'Local Contact 2',
            'Staff',
            'Team Leader',
            'Co-Investigator',
            'Principal Investigator',
            'Alternate Contact'))
    remote = db.Column(db.Integer, server_default=db.FetchedValue())

    Person = db.relationship(
        'Person', primaryjoin='SessionHasPerson.personId == Person.personId')
    BLSession = db.relationship(
        'BLSession',
        primaryjoin='SessionHasPerson.sessionId == BLSession.sessionId')


class Shipping(db.Model):
    __tablename__ = 'Shipping'

    shippingId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(
        db.ForeignKey(
            'Proposal.proposalId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        server_default=db.FetchedValue())
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
    sendingLabContactId = db.Column(db.ForeignKey(
        'LabContact.labContactId'), index=True)
    returnLabContactId = db.Column(db.ForeignKey(
        'LabContact.labContactId'), index=True)
    returnCourier = db.Column(db.String(45))
    dateOfShippingToUser = db.Column(db.DateTime)
    shippingType = db.Column(db.String(45))
    safetyLevel = db.Column(db.String(8))

    Proposal = db.relationship(
        'Proposal', primaryjoin='Shipping.proposalId == Proposal.proposalId')
    LabContact = db.relationship(
        'LabContact',
        primaryjoin='Shipping.returnLabContactId == LabContact.labContactId')
    LabContact1 = db.relationship(
        'LabContact',
        primaryjoin='Shipping.sendingLabContactId == LabContact.labContactId')


t_ShippingHasSession = db.Table(
    'ShippingHasSession',
    db.Column('shippingId', db.ForeignKey('Shipping.shippingId'),
              primary_key=True, nullable=False, index=True),
    db.Column('sessionId', db.ForeignKey('BLSession.sessionId'),
              primary_key=True, nullable=False, index=True)
)


class SpaceGroup(db.Model):
    __tablename__ = 'SpaceGroup'

    spaceGroupId = db.Column(db.Integer, primary_key=True, info='Primary key')
    geometryClassnameId = db.Column(
        db.ForeignKey(
            'GeometryClassname.geometryClassnameId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    spaceGroupNumber = db.Column(db.Integer, info='ccp4 number pr IUCR')
    spaceGroupShortName = db.Column(
        db.String(45), index=True, info='short name without blank')
    spaceGroupName = db.Column(db.String(45), info='verbose name')
    bravaisLattice = db.Column(db.String(45), info='short name')
    bravaisLatticeName = db.Column(db.String(45), info='verbose name')
    pointGroup = db.Column(db.String(45), info='point group')
    MX_used = db.Column(
        db.Integer,
        nullable=False,
        server_default=db.FetchedValue(),
        info='1 if used in the crystal form')

    GeometryClassname = db.relationship(
        'GeometryClassname',
        primaryjoin='SpaceGroup.geometryClassnameId == GeometryClassname.geometryClassnameId')


class Speciman(db.Model):
    __tablename__ = 'Specimen'

    specimenId = db.Column(db.Integer, primary_key=True)
    experimentId = db.Column(db.ForeignKey(
        'Experiment.experimentId'), nullable=False, index=True)
    bufferId = db.Column(db.ForeignKey('Buffer.bufferId'), index=True)
    macromoleculeId = db.Column(db.ForeignKey(
        'Macromolecule.macromoleculeId'), index=True)
    samplePlatePositionId = db.Column(db.ForeignKey(
        'SamplePlatePosition.samplePlatePositionId'), index=True)
    safetyLevelId = db.Column(db.ForeignKey(
        'SafetyLevel.safetyLevelId'), index=True)
    stockSolutionId = db.Column(db.ForeignKey(
        'StockSolution.stockSolutionId'), index=True)
    code = db.Column(db.String(255))
    concentration = db.Column(db.String(45))
    volume = db.Column(db.String(45))
    comments = db.Column(db.String(5120))

    Buffer = db.relationship(
        'Buffer', primaryjoin='Speciman.bufferId == Buffer.bufferId')
    Experiment = db.relationship(
        'Experiment',
        primaryjoin='Speciman.experimentId == Experiment.experimentId')
    Macromolecule = db.relationship(
        'Macromolecule',
        primaryjoin='Speciman.macromoleculeId == Macromolecule.macromoleculeId')
    SafetyLevel = db.relationship(
        'SafetyLevel',
        primaryjoin='Speciman.safetyLevelId == SafetyLevel.safetyLevelId')
    SamplePlatePosition = db.relationship(
        'SamplePlatePosition',
        primaryjoin='Speciman.samplePlatePositionId == SamplePlatePosition.samplePlatePositionId')
    StockSolution = db.relationship(
        'StockSolution',
        primaryjoin='Speciman.stockSolutionId == StockSolution.stockSolutionId')


class StockSolution(db.Model):
    __tablename__ = 'StockSolution'

    stockSolutionId = db.Column(db.Integer, primary_key=True)
    proposalId = db.Column(db.Integer, nullable=False,
                           server_default=db.FetchedValue())
    bufferId = db.Column(db.ForeignKey('Buffer.bufferId'),
                         nullable=False, index=True)
    macromoleculeId = db.Column(db.ForeignKey(
        'Macromolecule.macromoleculeId'), index=True)
    instructionSetId = db.Column(db.ForeignKey(
        'InstructionSet.instructionSetId'), index=True)
    boxId = db.Column(db.Integer)
    name = db.Column(db.String(45))
    storageTemperature = db.Column(db.String(55))
    volume = db.Column(db.String(55))
    concentration = db.Column(db.String(55))
    comments = db.Column(db.String(255))

    Buffer = db.relationship(
        'Buffer', primaryjoin='StockSolution.bufferId == Buffer.bufferId')
    InstructionSet = db.relationship(
        'InstructionSet',
        primaryjoin='StockSolution.instructionSetId == InstructionSet.instructionSetId')
    Macromolecule = db.relationship(
        'Macromolecule',
        primaryjoin='StockSolution.macromoleculeId == Macromolecule.macromoleculeId')


class Stoichiometry(db.Model):
    __tablename__ = 'Stoichiometry'

    stoichiometryId = db.Column(db.Integer, primary_key=True)
    hostMacromoleculeId = db.Column(db.ForeignKey(
        'Macromolecule.macromoleculeId'), nullable=False, index=True)
    macromoleculeId = db.Column(db.ForeignKey(
        'Macromolecule.macromoleculeId'), nullable=False, index=True)
    ratio = db.Column(db.String(45))

    Macromolecule = db.relationship(
        'Macromolecule',
        primaryjoin='Stoichiometry.hostMacromoleculeId == Macromolecule.macromoleculeId')
    Macromolecule1 = db.relationship(
        'Macromolecule',
        primaryjoin='Stoichiometry.macromoleculeId == Macromolecule.macromoleculeId')


class Structure(db.Model):
    __tablename__ = 'Structure'

    structureId = db.Column(db.Integer, primary_key=True)
    macromoleculeId = db.Column(db.ForeignKey(
        'Macromolecule.macromoleculeId'), index=True)
    crystalId = db.Column(db.ForeignKey('Crystal.crystalId'), index=True)
    blSampleId = db.Column(db.ForeignKey('BLSample.blSampleId'), index=True)
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
    proposalId = db.Column(db.ForeignKey('Proposal.proposalId'), index=True)
    uniprotId = db.Column(db.String(45))

    BLSample = db.relationship(
        'BLSample', primaryjoin='Structure.blSampleId == BLSample.blSampleId')
    Crystal = db.relationship(
        'Crystal', primaryjoin='Structure.crystalId == Crystal.crystalId')
    Macromolecule = db.relationship(
        'Macromolecule',
        primaryjoin='Structure.macromoleculeId == Macromolecule.macromoleculeId')
    Proposal = db.relationship(
        'Proposal', primaryjoin='Structure.proposalId == Proposal.proposalId')


class SubstructureDetermination(db.Model):
    __tablename__ = 'SubstructureDetermination'

    substructureDeterminationId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    phasingAnalysisId = db.Column(
        db.ForeignKey(
            'PhasingAnalysis.phasingAnalysisId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related phasing analysis item')
    phasingProgramRunId = db.Column(
        db.ForeignKey(
            'PhasingProgramRun.phasingProgramRunId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related program item')
    spaceGroupId = db.Column(
        db.ForeignKey(
            'SpaceGroup.spaceGroupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True,
        info='Related spaceGroup')
    method = db.Column(db.Enum('SAD', 'MAD', 'SIR', 'SIRAS', 'MR',
                       'MIR', 'MIRAS', 'RIP', 'RIPAS'), info='phasing method')
    lowRes = db.Column(db.Float(asdecimal=True))
    highRes = db.Column(db.Float(asdecimal=True))
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')

    PhasingAnalysi = db.relationship(
        'PhasingAnalysi',
        primaryjoin='SubstructureDetermination.phasingAnalysisId == PhasingAnalysi.phasingAnalysisId')
    PhasingProgramRun = db.relationship(
        'PhasingProgramRun',
        primaryjoin='SubstructureDetermination.phasingProgramRunId == PhasingProgramRun.phasingProgramRunId')
    SpaceGroup = db.relationship(
        'SpaceGroup',
        primaryjoin='SubstructureDetermination.spaceGroupId == SpaceGroup.spaceGroupId')


class Subtraction(db.Model):
    __tablename__ = 'Subtraction'

    subtractionId = db.Column(db.Integer, primary_key=True)
    dataCollectionId = db.Column(db.ForeignKey(
        'SaxsDataCollection.dataCollectionId'), nullable=False, index=True)
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
    sampleOneDimensionalFiles = db.Column(
        db.ForeignKey('FrameList.frameListId'), index=True)
    bufferOnedimensionalFiles = db.Column(
        db.ForeignKey('FrameList.frameListId'), index=True)
    sampleAverageFilePath = db.Column(db.String(255))
    bufferAverageFilePath = db.Column(db.String(255))

    FrameList = db.relationship(
        'FrameList',
        primaryjoin='Subtraction.bufferOnedimensionalFiles == FrameList.frameListId')
    SaxsDataCollection = db.relationship(
        'SaxsDataCollection',
        primaryjoin='Subtraction.dataCollectionId == SaxsDataCollection.dataCollectionId')
    FrameList1 = db.relationship(
        'FrameList',
        primaryjoin='Subtraction.sampleOneDimensionalFiles == FrameList.frameListId')


class SubtractionToAbInitioModel(db.Model):
    __tablename__ = 'SubtractionToAbInitioModel'

    subtractionToAbInitioModelId = db.Column(db.Integer, primary_key=True)
    abInitioId = db.Column(db.ForeignKey(
        'AbInitioModel.abInitioModelId'), index=True)
    subtractionId = db.Column(db.ForeignKey(
        'Subtraction.subtractionId'), index=True)

    AbInitioModel = db.relationship(
        'AbInitioModel',
        primaryjoin='SubtractionToAbInitioModel.abInitioId == AbInitioModel.abInitioModelId')
    Subtraction = db.relationship(
        'Subtraction',
        primaryjoin='SubtractionToAbInitioModel.subtractionId == Subtraction.subtractionId')


class Superposition(db.Model):
    __tablename__ = 'Superposition'

    superpositionId = db.Column(db.Integer, primary_key=True)
    subtractionId = db.Column(db.Integer, nullable=False, index=True)
    abinitioModelPdbFilePath = db.Column(db.String(255))
    aprioriPdbFilePath = db.Column(db.String(255))
    alignedPdbFilePath = db.Column(db.String(255))
    creationDate = db.Column(db.DateTime)


class UntrustedRegion(db.Model):
    __tablename__ = 'UntrustedRegion'

    untrustedRegionId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    detectorId = db.Column(
        db.ForeignKey(
            'Detector.detectorId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    x1 = db.Column(db.Integer, nullable=False)
    x2 = db.Column(db.Integer, nullable=False)
    y1 = db.Column(db.Integer, nullable=False)
    y2 = db.Column(db.Integer, nullable=False)

    Detector = db.relationship(
        'Detector',
        primaryjoin='UntrustedRegion.detectorId == Detector.detectorId')


class UserGroup(db.Model):
    __tablename__ = 'UserGroup'

    userGroupId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(31), nullable=False, unique=True)


t_UserGroup_has_Permission = db.Table(
    'UserGroup_has_Permission',
    db.Column(
        'userGroupId',
        db.ForeignKey(
            'UserGroup.userGroupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'permissionId',
        db.ForeignKey(
            'Permission.permissionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


t_UserGroup_has_Person = db.Table(
    'UserGroup_has_Person',
    db.Column(
        'userGroupId',
        db.ForeignKey(
            'UserGroup.userGroupId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False),
    db.Column(
        'personId',
        db.ForeignKey(
            'Person.personId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True))


class Workflow(db.Model):
    __tablename__ = 'Workflow'

    workflowId = db.Column(db.Integer, primary_key=True,
                           info='Primary key (auto-incremented)')
    workflowTitle = db.Column(db.String(255))
    workflowType = db.Column(
        db.Enum(
            'Characterisation',
            'Undefined',
            'BioSAXS Post Processing',
            'EnhancedCharacterisation',
            'LineScan',
            'MeshScan',
            'Dehydration',
            'KappaReorientation',
            'BurnStrategy',
            'XrayCentering',
            'DiffractionTomography',
            'TroubleShooting',
            'VisualReorientation',
            'HelicalCharacterisation',
            'GroupedProcessing',
            'MXPressE',
            'MXPressO',
            'MXPressL',
            'MXScore',
            'MXPressI',
            'MXPressM',
            'MXPressA',
            'CollectAndSpectra',
            'LowDoseDC',
            'EnergyInterleavedMAD',
            'MXPressF',
            'MXPressH',
            'MXPressP',
            'MXPressP_SAD',
            'MXPressR',
            'MXPressR_180',
            'MXPressR_dehydration',
            'MeshAndCollect',
            'MeshAndCollectFromFile'))
    workflowTypeId = db.Column(db.Integer)
    comments = db.Column(db.String(1024))
    status = db.Column(db.String(255))
    resultFilePath = db.Column(db.String(255))
    logFilePath = db.Column(db.String(255))
    recordTimeStamp = db.Column(
        db.DateTime, info='Creation or last update date/time')


class WorkflowDehydration(db.Model):
    __tablename__ = 'WorkflowDehydration'

    workflowDehydrationId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    workflowId = db.Column(
        db.ForeignKey(
            'Workflow.workflowId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related workflow')
    dataFilePath = db.Column(db.String(255))
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info='Creation or last update date/time')

    Workflow = db.relationship(
        'Workflow',
        primaryjoin='WorkflowDehydration.workflowId == Workflow.workflowId')


class WorkflowMesh(db.Model):
    __tablename__ = 'WorkflowMesh'

    workflowMeshId = db.Column(
        db.Integer, primary_key=True, info='Primary key (auto-incremented)')
    workflowId = db.Column(
        db.ForeignKey(
            'Workflow.workflowId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True,
        info='Related workflow')
    bestPositionId = db.Column(db.Integer, index=True)
    bestImageId = db.Column(db.ForeignKey(
        'Image.imageId', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    value1 = db.Column(db.Float(asdecimal=True))
    value2 = db.Column(db.Float(asdecimal=True))
    value3 = db.Column(db.Float(asdecimal=True), info='N value')
    value4 = db.Column(db.Float(asdecimal=True))
    cartographyPath = db.Column(db.String(255))
    recordTimeStamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.FetchedValue(),
        info='Creation or last update date/time')

    Image = db.relationship(
        'Image', primaryjoin='WorkflowMesh.bestImageId == Image.imageId')
    Workflow = db.relationship(
        'Workflow',
        primaryjoin='WorkflowMesh.workflowId == Workflow.workflowId')


class WorkflowStep(db.Model):
    __tablename__ = 'WorkflowStep'

    workflowStepId = db.Column(db.Integer, primary_key=True)
    workflowId = db.Column(db.ForeignKey(
        'Workflow.workflowId'), nullable=False, index=True)
    workflowStepType = db.Column(db.String(45))
    status = db.Column(db.String(45))
    folderPath = db.Column(db.String(1024))
    imageResultFilePath = db.Column(db.String(1024))
    htmlResultFilePath = db.Column(db.String(1024))
    resultFilePath = db.Column(db.String(1024))
    comments = db.Column(db.String(2048))
    crystalSizeX = db.Column(db.String(45))
    crystalSizeY = db.Column(db.String(45))
    crystalSizeZ = db.Column(db.String(45))
    maxDozorScore = db.Column(db.String(45))
    recordTimeStamp = db.Column(db.DateTime)

    Workflow = db.relationship(
        'Workflow',
        primaryjoin='WorkflowStep.workflowId == Workflow.workflowId')


class WorkflowType(db.Model):
    __tablename__ = 'WorkflowType'

    workflowTypeId = db.Column(db.Integer, primary_key=True)
    workflowTypeName = db.Column(db.String(45))
    comments = db.Column(db.String(2048))
    recordTimeStamp = db.Column(db.DateTime)


class XFEFluorescenceSpectrum(db.Model):
    __tablename__ = 'XFEFluorescenceSpectrum'

    xfeFluorescenceSpectrumId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(
        db.ForeignKey(
            'BLSession.sessionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    blSampleId = db.Column(
        db.ForeignKey(
            'BLSample.blSampleId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        index=True)
    fittedDataFileFullPath = db.Column(db.String(255))
    scanFileFullPath = db.Column(db.String(255))
    jpegScanFileFullPath = db.Column(db.String(255))
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    filename = db.Column(db.String(255))
    energy = db.Column(db.Float)
    exposureTime = db.Column(db.Float)
    axisPosition = db.Column(db.Float)
    beamTransmission = db.Column(db.Float)
    annotatedPymcaXfeSpectrum = db.Column(db.String(255))
    beamSizeVertical = db.Column(db.Float)
    beamSizeHorizontal = db.Column(db.Float)
    crystalClass = db.Column(db.String(20))
    comments = db.Column(db.String(1024))
    flux = db.Column(db.Float(asdecimal=True),
                     info='flux measured before the xrfSpectra')
    flux_end = db.Column(db.Float(asdecimal=True),
                         info='flux measured after the xrfSpectra')
    workingDirectory = db.Column(db.String(512))
    blSubSampleId = db.Column(db.ForeignKey(
        'BLSubSample.blSubSampleId'), index=True)

    BLSample = db.relationship(
        'BLSample',
        primaryjoin='XFEFluorescenceSpectrum.blSampleId == BLSample.blSampleId')
    BLSubSample = db.relationship(
        'BLSubSample',
        primaryjoin='XFEFluorescenceSpectrum.blSubSampleId == BLSubSample.blSubSampleId')
    BLSession = db.relationship(
        'BLSession',
        primaryjoin='XFEFluorescenceSpectrum.sessionId == BLSession.sessionId')


class XRFFluorescenceMapping(db.Model):
    __tablename__ = 'XRFFluorescenceMapping'

    xrfFluorescenceMappingId = db.Column(db.Integer, primary_key=True)
    xrfFluorescenceMappingROIId = db.Column(
        db.ForeignKey(
            'XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    dataCollectionId = db.Column(
        db.ForeignKey(
            'DataCollection.dataCollectionId',
            ondelete='CASCADE',
            onupdate='CASCADE'),
        nullable=False,
        index=True)
    imageNumber = db.Column(db.Integer, nullable=False)
    counts = db.Column(db.Integer, nullable=False)

    DataCollection = db.relationship(
        'DataCollection',
        primaryjoin='XRFFluorescenceMapping.dataCollectionId == DataCollection.dataCollectionId')
    XRFFluorescenceMappingROI = db.relationship(
        'XRFFluorescenceMappingROI',
        primaryjoin='XRFFluorescenceMapping.xrfFluorescenceMappingROIId == XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId')


class XRFFluorescenceMappingROI(db.Model):
    __tablename__ = 'XRFFluorescenceMappingROI'

    xrfFluorescenceMappingROIId = db.Column(db.Integer, primary_key=True)
    startEnergy = db.Column(db.Float, nullable=False)
    endEnergy = db.Column(db.Float, nullable=False)
    element = db.Column(db.String(2))
    edge = db.Column(
        db.String(2), info='In future may be changed to enum(K, L)')
    r = db.Column(db.Integer, info='R colour component')
    g = db.Column(db.Integer, info='G colour component')
    b = db.Column(db.Integer, info='B colour component')


t_v_dewarBeamlineByWeek = db.Table(
    'v_dewarBeamlineByWeek',
    db.Column('Week', db.Integer, nullable=False),
    db.Column('ID14', db.Integer, nullable=False),
    db.Column('ID23', db.Integer, nullable=False),
    db.Column('ID29', db.Integer, nullable=False),
    db.Column('BM14', db.Integer, nullable=False)
)


t_v_dewarByWeek = db.Table(
    'v_dewarByWeek',
    db.Column('Week', db.Integer, nullable=False),
    db.Column('Dewars Tracked', db.Integer, nullable=False),
    db.Column('Dewars Non-Tracked', db.Integer, nullable=False)
)


t_v_dewarByWeekTotal = db.Table(
    'v_dewarByWeekTotal',
    db.Column('Week', db.Integer, nullable=False),
    db.Column('Dewars Tracked', db.Integer, nullable=False),
    db.Column('Dewars Non-Tracked', db.Integer, nullable=False),
    db.Column('Total', db.Integer, nullable=False)
)


t_v_dewarList = db.Table(
    'v_dewarList',
    db.Column('proposal', db.Integer, nullable=False),
    db.Column('shippingName', db.Integer, nullable=False),
    db.Column('dewarName', db.Integer, nullable=False),
    db.Column('barCode', db.Integer, nullable=False),
    db.Column('creationDate', db.Integer, nullable=False),
    db.Column('shippingType', db.Integer, nullable=False),
    db.Column('nbEvents', db.Integer, nullable=False),
    db.Column('dewarStatus', db.Integer, nullable=False),
    db.Column('shippingStatus', db.Integer, nullable=False),
    db.Column('nbSamples', db.Integer, nullable=False)
)


t_v_dewarProposalCode = db.Table(
    'v_dewarProposalCode',
    db.Column('proposalCode', db.Integer, nullable=False),
    db.Column('COUNT(*)', db.Integer, nullable=False)
)


t_v_dewarProposalCodeByWeek = db.Table(
    'v_dewarProposalCodeByWeek',
    db.Column('Week', db.Integer, nullable=False),
    db.Column('MX', db.Integer, nullable=False),
    db.Column('FX', db.Integer, nullable=False),
    db.Column('BM14U', db.Integer, nullable=False),
    db.Column('BM161', db.Integer, nullable=False),
    db.Column('BM162', db.Integer, nullable=False),
    db.Column('Others', db.Integer, nullable=False)
)


t_v_dewar_summary = db.Table(
    'v_dewar_summary',
    db.Column('shippingName', db.Integer, nullable=False),
    db.Column('deliveryAgent_agentName', db.Integer, nullable=False),
    db.Column('deliveryAgent_shippingDate', db.Integer, nullable=False),
    db.Column('deliveryAgent_deliveryDate', db.Integer, nullable=False),
    db.Column('deliveryAgent_agentCode', db.Integer, nullable=False),
    db.Column('deliveryAgent_flightCode', db.Integer, nullable=False),
    db.Column('shippingStatus', db.Integer, nullable=False),
    db.Column('bltimeStamp', db.Integer, nullable=False),
    db.Column('laboratoryId', db.Integer, nullable=False),
    db.Column('isStorageShipping', db.Integer, nullable=False),
    db.Column('creationDate', db.Integer, nullable=False),
    db.Column('Shipping_comments', db.Integer, nullable=False),
    db.Column('sendingLabContactId', db.Integer, nullable=False),
    db.Column('returnLabContactId', db.Integer, nullable=False),
    db.Column('returnCourier', db.Integer, nullable=False),
    db.Column('dateOfShippingToUser', db.Integer, nullable=False),
    db.Column('shippingType', db.Integer, nullable=False),
    db.Column('dewarId', db.Integer, nullable=False),
    db.Column('shippingId', db.Integer, nullable=False),
    db.Column('dewarCode', db.Integer, nullable=False),
    db.Column('comments', db.Integer, nullable=False),
    db.Column('storageLocation', db.Integer, nullable=False),
    db.Column('dewarStatus', db.Integer, nullable=False),
    db.Column('isStorageDewar', db.Integer, nullable=False),
    db.Column('barCode', db.Integer, nullable=False),
    db.Column('firstExperimentId', db.Integer, nullable=False),
    db.Column('customsValue', db.Integer, nullable=False),
    db.Column('transportValue', db.Integer, nullable=False),
    db.Column('trackingNumberToSynchrotron', db.Integer, nullable=False),
    db.Column('trackingNumberFromSynchrotron', db.Integer, nullable=False),
    db.Column('type', db.Integer, nullable=False),
    db.Column('isReimbursed', db.Integer, nullable=False),
    db.Column('sessionId', db.Integer, nullable=False),
    db.Column('beamlineName', db.Integer, nullable=False),
    db.Column('sessionStartDate', db.Integer, nullable=False),
    db.Column('sessionEndDate', db.Integer, nullable=False),
    db.Column('beamLineOperator', db.Integer, nullable=False),
    db.Column('nbReimbDewars', db.Integer, nullable=False),
    db.Column('proposalId', db.Integer, nullable=False),
    db.Column('containerId', db.Integer, nullable=False),
    db.Column('containerType', db.Integer, nullable=False),
    db.Column('capacity', db.Integer, nullable=False),
    db.Column('beamlineLocation', db.Integer, nullable=False),
    db.Column('sampleChangerLocation', db.Integer, nullable=False),
    db.Column('containerStatus', db.Integer, nullable=False),
    db.Column('containerCode', db.Integer, nullable=False)
)


t_v_em_2dclassification = db.Table(
    'v_em_2dclassification',
    db.Column('proposalId', db.Integer, nullable=False),
    db.Column('sessionId', db.Integer, nullable=False),
    db.Column('imageDirectory', db.Integer, nullable=False),
    db.Column('particlePickerId', db.Integer, nullable=False),
    db.Column('particleClassificationGroupId', db.Integer, nullable=False),
    db.Column('particleClassificationId', db.Integer, nullable=False),
    db.Column('classNumber', db.Integer, nullable=False),
    db.Column('classImageFullPath', db.Integer, nullable=False)
)


t_v_em_classification = db.Table(
    'v_em_classification',
    db.Column('proposalId', db.Integer, nullable=False),
    db.Column('sessionId', db.Integer, nullable=False),
    db.Column('imageDirectory', db.Integer, nullable=False),
    db.Column('particlePickerId', db.Integer, nullable=False),
    db.Column('numberOfParticles', db.Integer, nullable=False),
    db.Column('particleClassificationGroupId', db.Integer, nullable=False),
    db.Column('particleClassificationId', db.Integer, nullable=False),
    db.Column('classNumber', db.Integer, nullable=False),
    db.Column('classImageFullPath', db.Integer, nullable=False),
    db.Column('particlesPerClass', db.Integer, nullable=False),
    db.Column('classDistribution', db.Integer, nullable=False),
    db.Column('rotationAccuracy', db.Integer, nullable=False),
    db.Column('translationAccuracy', db.Integer, nullable=False),
    db.Column('estimatedResolution', db.Integer, nullable=False),
    db.Column('overallFourierCompleteness', db.Integer, nullable=False)
)


t_v_em_movie = db.Table(
    'v_em_movie',
    db.Column('Movie_movieId', db.Integer, nullable=False),
    db.Column('Movie_dataCollectionId', db.Integer, nullable=False),
    db.Column('Movie_movieNumber', db.Integer, nullable=False),
    db.Column('Movie_movieFullPath', db.Integer, nullable=False),
    db.Column('Movie_positionX', db.Integer, nullable=False),
    db.Column('Movie_positionY', db.Integer, nullable=False),
    db.Column('Movie_micrographFullPath', db.Integer, nullable=False),
    db.Column('Movie_micrographSnapshotFullPath', db.Integer, nullable=False),
    db.Column('Movie_xmlMetaDataFullPath', db.Integer, nullable=False),
    db.Column('Movie_dosePerImage', db.Integer, nullable=False),
    db.Column('Movie_createdTimeStamp', db.Integer, nullable=False),
    db.Column('MotionCorrection_motionCorrectionId',
              db.Integer, nullable=False),
    db.Column('MotionCorrection_movieId', db.Integer, nullable=False),
    db.Column('MotionCorrection_firstFrame', db.Integer, nullable=False),
    db.Column('MotionCorrection_lastFrame', db.Integer, nullable=False),
    db.Column('MotionCorrection_dosePerFrame', db.Integer, nullable=False),
    db.Column('MotionCorrection_doseWeight', db.Integer, nullable=False),
    db.Column('MotionCorrection_totalMotion', db.Integer, nullable=False),
    db.Column('MotionCorrection_averageMotionPerFrame',
              db.Integer, nullable=False),
    db.Column('MotionCorrection_driftPlotFullPath',
              db.Integer, nullable=False),
    db.Column('MotionCorrection_micrographFullPath',
              db.Integer, nullable=False),
    db.Column('MotionCorrection_micrographSnapshotFullPath',
              db.Integer, nullable=False),
    db.Column('MotionCorrection_correctedDoseMicrographFullPath',
              db.Integer, nullable=False),
    db.Column('MotionCorrection_patchesUsed', db.Integer, nullable=False),
    db.Column('MotionCorrection_logFileFullPath', db.Integer, nullable=False),
    db.Column('CTF_CTFid', db.Integer, nullable=False),
    db.Column('CTF_motionCorrectionId', db.Integer, nullable=False),
    db.Column('CTF_spectraImageThumbnailFullPath', db.Integer, nullable=False),
    db.Column('CTF_spectraImageFullPath', db.Integer, nullable=False),
    db.Column('CTF_defocusU', db.Integer, nullable=False),
    db.Column('CTF_defocusV', db.Integer, nullable=False),
    db.Column('CTF_angle', db.Integer, nullable=False),
    db.Column('CTF_crossCorrelationCoefficient', db.Integer, nullable=False),
    db.Column('CTF_resolutionLimit', db.Integer, nullable=False),
    db.Column('CTF_estimatedBfactor', db.Integer, nullable=False),
    db.Column('CTF_logFilePath', db.Integer, nullable=False),
    db.Column('CTF_createdTimeStamp', db.Integer, nullable=False),
    db.Column('Proposal_proposalId', db.Integer, nullable=False),
    db.Column('BLSession_sessionId', db.Integer, nullable=False)
)


t_v_em_stats = db.Table(
    'v_em_stats',
    db.Column('proposalId', db.Integer, nullable=False),
    db.Column('sessionId', db.Integer, nullable=False),
    db.Column('imageDirectory', db.Integer, nullable=False),
    db.Column('movieId', db.Integer, nullable=False),
    db.Column('movieNumber', db.Integer, nullable=False),
    db.Column('createdTimeStamp', db.Integer, nullable=False),
    db.Column('motionCorrectionId', db.Integer, nullable=False),
    db.Column('dataCollectionId', db.Integer, nullable=False),
    db.Column('totalMotion', db.Integer, nullable=False),
    db.Column('averageMotionPerFrame', db.Integer, nullable=False),
    db.Column('lastFrame', db.Integer, nullable=False),
    db.Column('dosePerFrame', db.Integer, nullable=False),
    db.Column('defocusU', db.Integer, nullable=False),
    db.Column('defocusV', db.Integer, nullable=False),
    db.Column('resolutionLimit', db.Integer, nullable=False),
    db.Column('estimatedBfactor', db.Integer, nullable=False),
    db.Column('angle', db.Integer, nullable=False)
)


t_v_energyScan = db.Table(
    'v_energyScan',
    db.Column('energyScanId', db.Integer, nullable=False),
    db.Column('sessionId', db.Integer, nullable=False),
    db.Column('blSampleId', db.Integer, nullable=False),
    db.Column('fluorescenceDetector', db.Integer, nullable=False),
    db.Column('scanFileFullPath', db.Integer, nullable=False),
    db.Column('choochFileFullPath', db.Integer, nullable=False),
    db.Column('jpegChoochFileFullPath', db.Integer, nullable=False),
    db.Column('element', db.Integer, nullable=False),
    db.Column('startEnergy', db.Integer, nullable=False),
    db.Column('endEnergy', db.Integer, nullable=False),
    db.Column('transmissionFactor', db.Integer, nullable=False),
    db.Column('exposureTime', db.Integer, nullable=False),
    db.Column('synchrotronCurrent', db.Integer, nullable=False),
    db.Column('temperature', db.Integer, nullable=False),
    db.Column('peakEnergy', db.Integer, nullable=False),
    db.Column('peakFPrime', db.Integer, nullable=False),
    db.Column('peakFDoublePrime', db.Integer, nullable=False),
    db.Column('inflectionEnergy', db.Integer, nullable=False),
    db.Column('inflectionFPrime', db.Integer, nullable=False),
    db.Column('inflectionFDoublePrime', db.Integer, nullable=False),
    db.Column('xrayDose', db.Integer, nullable=False),
    db.Column('startTime', db.Integer, nullable=False),
    db.Column('endTime', db.Integer, nullable=False),
    db.Column('edgeEnergy', db.Integer, nullable=False),
    db.Column('filename', db.Integer, nullable=False),
    db.Column('beamSizeVertical', db.Integer, nullable=False),
    db.Column('beamSizeHorizontal', db.Integer, nullable=False),
    db.Column('crystalClass', db.Integer, nullable=False),
    db.Column('comments', db.Integer, nullable=False),
    db.Column('flux', db.Integer, nullable=False),
    db.Column('flux_end', db.Integer, nullable=False),
    db.Column('remoteEnergy', db.Integer, nullable=False),
    db.Column('remoteFPrime', db.Integer, nullable=False),
    db.Column('remoteFDoublePrime', db.Integer, nullable=False),
    db.Column('BLSample_sampleId', db.Integer, nullable=False),
    db.Column('name', db.Integer, nullable=False),
    db.Column('code', db.Integer, nullable=False),
    db.Column('acronym', db.Integer, nullable=False),
    db.Column('BLSession_proposalId', db.Integer, nullable=False)
)


t_v_hour = db.Table(
    'v_hour',
    db.Column('num', db.Integer, nullable=False)
)


t_v_logonByHour = db.Table(
    'v_logonByHour',
    db.Column('Hour', db.Integer, nullable=False),
    db.Column('Distinct logins', db.Integer, nullable=False),
    db.Column('Total logins', db.Integer, nullable=False)
)


t_v_logonByMonthDay = db.Table(
    'v_logonByMonthDay',
    db.Column('Day', db.Integer, nullable=False),
    db.Column('Distinct logins', db.Integer, nullable=False),
    db.Column('Total logins', db.Integer, nullable=False)
)


t_v_logonByWeek = db.Table(
    'v_logonByWeek',
    db.Column('Week', db.Integer, nullable=False),
    db.Column('Distinct logins', db.Integer, nullable=False),
    db.Column('Total logins', db.Integer, nullable=False)
)


t_v_logonByWeekDay = db.Table(
    'v_logonByWeekDay',
    db.Column('Day', db.Integer, nullable=False),
    db.Column('Distinct logins', db.Integer, nullable=False),
    db.Column('Total logins', db.Integer, nullable=False)
)


t_v_monthDay = db.Table(
    'v_monthDay',
    db.Column('num', db.Integer, nullable=False)
)


t_v_mx_autoprocessing_stats = db.Table(
    'v_mx_autoprocessing_stats',
    db.Column('autoProcScalingStatisticsId', db.Integer, nullable=False),
    db.Column('autoProcScalingId', db.Integer, nullable=False),
    db.Column('scalingStatisticsType', db.Integer, nullable=False),
    db.Column('resolutionLimitLow', db.Integer, nullable=False),
    db.Column('resolutionLimitHigh', db.Integer, nullable=False),
    db.Column('rMerge', db.Integer, nullable=False),
    db.Column('rMeasWithinIPlusIMinus', db.Integer, nullable=False),
    db.Column('rMeasAllIPlusIMinus', db.Integer, nullable=False),
    db.Column('rPimWithinIPlusIMinus', db.Integer, nullable=False),
    db.Column('rPimAllIPlusIMinus', db.Integer, nullable=False),
    db.Column('fractionalPartialBias', db.Integer, nullable=False),
    db.Column('nTotalObservations', db.Integer, nullable=False),
    db.Column('nTotalUniqueObservations', db.Integer, nullable=False),
    db.Column('meanIOverSigI', db.Integer, nullable=False),
    db.Column('completeness', db.Integer, nullable=False),
    db.Column('multiplicity', db.Integer, nullable=False),
    db.Column('anomalousCompleteness', db.Integer, nullable=False),
    db.Column('anomalousMultiplicity', db.Integer, nullable=False),
    db.Column('recordTimeStamp', db.Integer, nullable=False),
    db.Column('anomalous', db.Integer, nullable=False),
    db.Column('ccHalf', db.Integer, nullable=False),
    db.Column('ccAno', db.Integer, nullable=False),
    db.Column('sigAno', db.Integer, nullable=False),
    db.Column('ISA', db.Integer, nullable=False),
    db.Column('dataCollectionId', db.Integer, nullable=False),
    db.Column('strategySubWedgeOrigId', db.Integer, nullable=False),
    db.Column('detectorId', db.Integer, nullable=False),
    db.Column('blSubSampleId', db.Integer, nullable=False),
    db.Column('dataCollectionNumber', db.Integer, nullable=False),
    db.Column('startTime', db.Integer, nullable=False),
    db.Column('endTime', db.Integer, nullable=False),
    db.Column('sessionId', db.Integer, nullable=False),
    db.Column('proposalId', db.Integer, nullable=False),
    db.Column('beamLineName', db.Integer, nullable=False)
)


t_v_mx_experiment_stats = db.Table(
    'v_mx_experiment_stats',
    db.Column('startTime', db.Integer, nullable=False),
    db.Column('Images', db.Integer, nullable=False),
    db.Column('Transmission', db.Integer, nullable=False),
    db.Column('Res. (corner)', db.Integer, nullable=False),
    db.Column('En. (Wave.)', db.Integer, nullable=False),
    db.Column('Omega start (total)', db.Integer, nullable=False),
    db.Column('Exposure Time', db.Integer, nullable=False),
    db.Column('Flux', db.Integer, nullable=False),
    db.Column('Flux End', db.Integer, nullable=False),
    db.Column('Detector Distance', db.Integer, nullable=False),
    db.Column('X Beam', db.Integer, nullable=False),
    db.Column('Y Beam', db.Integer, nullable=False),
    db.Column('Kappa', db.Integer, nullable=False),
    db.Column('Phi', db.Integer, nullable=False),
    db.Column('Axis Start', db.Integer, nullable=False),
    db.Column('Axis End', db.Integer, nullable=False),
    db.Column('Axis Range', db.Integer, nullable=False),
    db.Column('Beam Size X', db.Integer, nullable=False),
    db.Column('Beam Size Y', db.Integer, nullable=False),
    db.Column('beamLineName', db.Integer, nullable=False),
    db.Column('comments', db.Integer, nullable=False),
    db.Column('proposalNumber', db.Integer, nullable=False)
)


t_v_mx_sample = db.Table(
    'v_mx_sample',
    db.Column('BLSample_blSampleId', db.Integer, nullable=False),
    db.Column('BLSample_diffractionPlanId', db.Integer, nullable=False),
    db.Column('BLSample_crystalId', db.Integer, nullable=False),
    db.Column('BLSample_containerId', db.Integer, nullable=False),
    db.Column('BLSample_name', db.Integer, nullable=False),
    db.Column('BLSample_code', db.Integer, nullable=False),
    db.Column('BLSample_location', db.Integer, nullable=False),
    db.Column('BLSample_holderLength', db.Integer, nullable=False),
    db.Column('BLSample_loopLength', db.Integer, nullable=False),
    db.Column('BLSample_loopType', db.Integer, nullable=False),
    db.Column('BLSample_wireWidth', db.Integer, nullable=False),
    db.Column('BLSample_comments', db.Integer, nullable=False),
    db.Column('BLSample_completionStage', db.Integer, nullable=False),
    db.Column('BLSample_structureStage', db.Integer, nullable=False),
    db.Column('BLSample_publicationStage', db.Integer, nullable=False),
    db.Column('BLSample_publicationComments', db.Integer, nullable=False),
    db.Column('BLSample_blSampleStatus', db.Integer, nullable=False),
    db.Column('BLSample_isInSampleChanger', db.Integer, nullable=False),
    db.Column('BLSample_lastKnownCenteringPosition',
              db.Integer, nullable=False),
    db.Column('BLSample_recordTimeStamp', db.Integer, nullable=False),
    db.Column('BLSample_SMILES', db.Integer, nullable=False),
    db.Column('Protein_proteinId', db.Integer, nullable=False),
    db.Column('Protein_name', db.Integer, nullable=False),
    db.Column('Protein_acronym', db.Integer, nullable=False),
    db.Column('Protein_proteinType', db.Integer, nullable=False),
    db.Column('Protein_proposalId', db.Integer, nullable=False),
    db.Column('Person_personId', db.Integer, nullable=False),
    db.Column('Person_familyName', db.Integer, nullable=False),
    db.Column('Person_givenName', db.Integer, nullable=False),
    db.Column('Person_emailAddress', db.Integer, nullable=False),
    db.Column('Container_containerId', db.Integer, nullable=False),
    db.Column('Container_code', db.Integer, nullable=False),
    db.Column('Container_containerType', db.Integer, nullable=False),
    db.Column('Container_containerStatus', db.Integer, nullable=False),
    db.Column('Container_beamlineLocation', db.Integer, nullable=False),
    db.Column('Container_sampleChangerLocation', db.Integer, nullable=False),
    db.Column('Dewar_code', db.Integer, nullable=False),
    db.Column('Dewar_dewarId', db.Integer, nullable=False),
    db.Column('Dewar_storageLocation', db.Integer, nullable=False),
    db.Column('Dewar_dewarStatus', db.Integer, nullable=False),
    db.Column('Dewar_barCode', db.Integer, nullable=False),
    db.Column('Shipping_shippingId', db.Integer, nullable=False),
    db.Column('sessionId', db.Integer, nullable=False),
    db.Column('BLSession_startDate', db.Integer, nullable=False),
    db.Column('BLSession_beamLineName', db.Integer, nullable=False)
)


t_v_phasing = db.Table(
    'v_phasing',
    db.Column('BLSample_blSampleId', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_autoProcIntegrationId',
              db.Integer, nullable=False),
    db.Column('AutoProcIntegration_dataCollectionId',
              db.Integer, nullable=False),
    db.Column('AutoProcIntegration_autoProcProgramId',
              db.Integer, nullable=False),
    db.Column('AutoProcIntegration_startImageNumber',
              db.Integer, nullable=False),
    db.Column('AutoProcIntegration_endImageNumber',
              db.Integer, nullable=False),
    db.Column('AutoProcIntegration_refinedDetectorDistance',
              db.Integer, nullable=False),
    db.Column('AutoProcIntegration_refinedXBeam', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_refinedYBeam', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_rotationAxisX', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_rotationAxisY', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_rotationAxisZ', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_beamVectorX', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_beamVectorY', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_beamVectorZ', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_cell_a', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_cell_b', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_cell_c', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_cell_alpha', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_cell_beta', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_cell_gamma', db.Integer, nullable=False),
    db.Column('AutoProcIntegration_recordTimeStamp',
              db.Integer, nullable=False),
    db.Column('AutoProcIntegration_anomalous', db.Integer, nullable=False),
    db.Column('SpaceGroup_spaceGroupId', db.Integer, nullable=False),
    db.Column('SpaceGroup_geometryClassnameId', db.Integer, nullable=False),
    db.Column('SpaceGroup_spaceGroupNumber', db.Integer, nullable=False),
    db.Column('SpaceGroup_spaceGroupShortName', db.Integer, nullable=False),
    db.Column('SpaceGroup_spaceGroupName', db.Integer, nullable=False),
    db.Column('SpaceGroup_bravaisLattice', db.Integer, nullable=False),
    db.Column('SpaceGroup_bravaisLatticeName', db.Integer, nullable=False),
    db.Column('SpaceGroup_pointGroup', db.Integer, nullable=False),
    db.Column('SpaceGroup_MX_used', db.Integer, nullable=False),
    db.Column('PhasingStep_phasingStepId', db.Integer, nullable=False),
    db.Column('PhasingStep_previousPhasingStepId', db.Integer, nullable=False),
    db.Column('PhasingStep_programRunId', db.Integer, nullable=False),
    db.Column('PhasingStep_spaceGroupId', db.Integer, nullable=False),
    db.Column('PhasingStep_autoProcScalingId', db.Integer, nullable=False),
    db.Column('PhasingStep_phasingAnalysisId', db.Integer, nullable=False),
    db.Column('PhasingStep_phasingStepType', db.Integer, nullable=False),
    db.Column('PhasingStep_method', db.Integer, nullable=False),
    db.Column('PhasingStep_solventContent', db.Integer, nullable=False),
    db.Column('PhasingStep_enantiomorph', db.Integer, nullable=False),
    db.Column('PhasingStep_lowRes', db.Integer, nullable=False),
    db.Column('PhasingStep_highRes', db.Integer, nullable=False),
    db.Column('PhasingStep_recordTimeStamp', db.Integer, nullable=False),
    db.Column('DataCollection_dataCollectionId', db.Integer, nullable=False),
    db.Column('DataCollection_dataCollectionGroupId',
              db.Integer, nullable=False),
    db.Column('DataCollection_strategySubWedgeOrigId',
              db.Integer, nullable=False),
    db.Column('DataCollection_detectorId', db.Integer, nullable=False),
    db.Column('DataCollection_blSubSampleId', db.Integer, nullable=False),
    db.Column('DataCollection_dataCollectionNumber',
              db.Integer, nullable=False),
    db.Column('DataCollection_startTime', db.Integer, nullable=False),
    db.Column('DataCollection_endTime', db.Integer, nullable=False),
    db.Column('DataCollection_runStatus', db.Integer, nullable=False),
    db.Column('DataCollection_axisStart', db.Integer, nullable=False),
    db.Column('DataCollection_axisEnd', db.Integer, nullable=False),
    db.Column('DataCollection_axisRange', db.Integer, nullable=False),
    db.Column('DataCollection_overlap', db.Integer, nullable=False),
    db.Column('DataCollection_numberOfImages', db.Integer, nullable=False),
    db.Column('DataCollection_startImageNumber', db.Integer, nullable=False),
    db.Column('DataCollection_numberOfPasses', db.Integer, nullable=False),
    db.Column('DataCollection_exposureTime', db.Integer, nullable=False),
    db.Column('DataCollection_imageDirectory', db.Integer, nullable=False),
    db.Column('DataCollection_imagePrefix', db.Integer, nullable=False),
    db.Column('DataCollection_imageSuffix', db.Integer, nullable=False),
    db.Column('DataCollection_fileTemplate', db.Integer, nullable=False),
    db.Column('DataCollection_wavelength', db.Integer, nullable=False),
    db.Column('DataCollection_resolution', db.Integer, nullable=False),
    db.Column('DataCollection_detectorDistance', db.Integer, nullable=False),
    db.Column('DataCollection_xBeam', db.Integer, nullable=False),
    db.Column('DataCollection_yBeam', db.Integer, nullable=False),
    db.Column('DataCollection_xBeamPix', db.Integer, nullable=False),
    db.Column('DataCollection_yBeamPix', db.Integer, nullable=False),
    db.Column('DataCollection_comments', db.Integer, nullable=False),
    db.Column('DataCollection_printableForReport', db.Integer, nullable=False),
    db.Column('DataCollection_slitGapVertical', db.Integer, nullable=False),
    db.Column('DataCollection_slitGapHorizontal', db.Integer, nullable=False),
    db.Column('DataCollection_transmission', db.Integer, nullable=False),
    db.Column('DataCollection_synchrotronMode', db.Integer, nullable=False),
    db.Column('DataCollection_xtalSnapshotFullPath1',
              db.Integer, nullable=False),
    db.Column('DataCollection_xtalSnapshotFullPath2',
              db.Integer, nullable=False),
    db.Column('DataCollection_xtalSnapshotFullPath3',
              db.Integer, nullable=False),
    db.Column('DataCollection_xtalSnapshotFullPath4',
              db.Integer, nullable=False),
    db.Column('DataCollection_rotationAxis', db.Integer, nullable=False),
    db.Column('DataCollection_phiStart', db.Integer, nullable=False),
    db.Column('DataCollection_kappaStart', db.Integer, nullable=False),
    db.Column('DataCollection_omegaStart', db.Integer, nullable=False),
    db.Column('DataCollection_resolutionAtCorner', db.Integer, nullable=False),
    db.Column('DataCollection_detector2Theta', db.Integer, nullable=False),
    db.Column('DataCollection_undulatorGap1', db.Integer, nullable=False),
    db.Column('DataCollection_undulatorGap2', db.Integer, nullable=False),
    db.Column('DataCollection_undulatorGap3', db.Integer, nullable=False),
    db.Column('DataCollection_beamSizeAtSampleX', db.Integer, nullable=False),
    db.Column('DataCollection_beamSizeAtSampleY', db.Integer, nullable=False),
    db.Column('DataCollection_centeringMethod', db.Integer, nullable=False),
    db.Column('DataCollection_averageTemperature', db.Integer, nullable=False),
    db.Column('DataCollection_actualCenteringPosition',
              db.Integer, nullable=False),
    db.Column('DataCollection_beamShape', db.Integer, nullable=False),
    db.Column('DataCollection_flux', db.Integer, nullable=False),
    db.Column('DataCollection_flux_end', db.Integer, nullable=False),
    db.Column('DataCollection_totalAbsorbedDose', db.Integer, nullable=False),
    db.Column('DataCollection_bestWilsonPlotPath', db.Integer, nullable=False),
    db.Column('DataCollection_imageQualityIndicatorsPlotPath',
              db.Integer, nullable=False),
    db.Column('DataCollection_imageQualityIndicatorsCSVPath',
              db.Integer, nullable=False),
    db.Column('PhasingProgramRun_phasingProgramRunId',
              db.Integer, nullable=False),
    db.Column('PhasingProgramRun_phasingCommandLine',
              db.Integer, nullable=False),
    db.Column('PhasingProgramRun_phasingPrograms', db.Integer, nullable=False),
    db.Column('PhasingProgramRun_phasingStatus', db.Integer, nullable=False),
    db.Column('PhasingProgramRun_phasingMessage', db.Integer, nullable=False),
    db.Column('PhasingProgramRun_phasingStartTime',
              db.Integer, nullable=False),
    db.Column('PhasingProgramRun_phasingEndTime', db.Integer, nullable=False),
    db.Column('PhasingProgramRun_phasingEnvironment',
              db.Integer, nullable=False),
    db.Column('PhasingProgramRun_phasingDirectory',
              db.Integer, nullable=False),
    db.Column('PhasingProgramRun_recordTimeStamp', db.Integer, nullable=False),
    db.Column('Protein_proteinId', db.Integer, nullable=False),
    db.Column('BLSession_sessionId', db.Integer, nullable=False),
    db.Column('BLSession_proposalId', db.Integer, nullable=False),
    db.Column('PhasingStatistics_phasingStatisticsId',
              db.Integer, nullable=False),
    db.Column('PhasingStatistics_metric', db.Integer, nullable=False),
    db.Column('PhasingStatistics_statisticsValue', db.Integer, nullable=False)
)


t_v_sample = db.Table(
    'v_sample',
    db.Column('proposalId', db.Integer, nullable=False),
    db.Column('shippingId', db.Integer, nullable=False),
    db.Column('dewarId', db.Integer, nullable=False),
    db.Column('containerId', db.Integer, nullable=False),
    db.Column('blSampleId', db.Integer, nullable=False),
    db.Column('proposalCode', db.Integer, nullable=False),
    db.Column('proposalNumber', db.Integer, nullable=False),
    db.Column('creationDate', db.Integer, nullable=False),
    db.Column('shippingType', db.Integer, nullable=False),
    db.Column('barCode', db.Integer, nullable=False),
    db.Column('shippingStatus', db.Integer, nullable=False)
)


t_v_sampleByWeek = db.Table(
    'v_sampleByWeek',
    db.Column('Week', db.Integer, nullable=False),
    db.Column('Samples', db.Integer, nullable=False)
)


t_v_saxs_datacollection = db.Table(
    'v_saxs_datacollection',
    db.Column('Subtraction_subtractionId', db.Integer, nullable=False),
    db.Column('MeasurementToDataCollection_dataCollectionId',
              db.Integer, nullable=False),
    db.Column('MeasurementToDataCollection_dataCollectionOrder',
              db.Integer, nullable=False),
    db.Column('MeasurementToDataCollection_measurementToDataCollectionId',
              db.Integer, nullable=False),
    db.Column('Specimen_specimenId', db.Integer, nullable=False),
    db.Column('Measurement_code', db.Integer, nullable=False),
    db.Column('Measurement_measurementId', db.Integer, nullable=False),
    db.Column('Buffer_bufferId', db.Integer, nullable=False),
    db.Column('Buffer_proposalId', db.Integer, nullable=False),
    db.Column('Buffer_safetyLevelId', db.Integer, nullable=False),
    db.Column('Buffer_name', db.Integer, nullable=False),
    db.Column('Buffer_acronym', db.Integer, nullable=False),
    db.Column('Buffer_pH', db.Integer, nullable=False),
    db.Column('Buffer_composition', db.Integer, nullable=False),
    db.Column('Buffer_comments', db.Integer, nullable=False),
    db.Column('Macromolecule_macromoleculeId', db.Integer, nullable=False),
    db.Column('Macromolecule_proposalId', db.Integer, nullable=False),
    db.Column('Macromolecule_safetyLevelId', db.Integer, nullable=False),
    db.Column('Macromolecule_name', db.Integer, nullable=False),
    db.Column('Macromolecule_acronym', db.Integer, nullable=False),
    db.Column('Macromolecule_extintionCoefficient',
              db.Integer, nullable=False),
    db.Column('Macromolecule_molecularMass', db.Integer, nullable=False),
    db.Column('Macromolecule_sequence', db.Integer, nullable=False),
    db.Column('Macromolecule_contactsDescriptionFilePath',
              db.Integer, nullable=False),
    db.Column('Macromolecule_symmetry', db.Integer, nullable=False),
    db.Column('Macromolecule_comments', db.Integer, nullable=False),
    db.Column('Macromolecule_refractiveIndex', db.Integer, nullable=False),
    db.Column('Macromolecule_solventViscosity', db.Integer, nullable=False),
    db.Column('Macromolecule_creationDate', db.Integer, nullable=False),
    db.Column('Specimen_experimentId', db.Integer, nullable=False),
    db.Column('Specimen_bufferId', db.Integer, nullable=False),
    db.Column('Specimen_samplePlatePositionId', db.Integer, nullable=False),
    db.Column('Specimen_safetyLevelId', db.Integer, nullable=False),
    db.Column('Specimen_stockSolutionId', db.Integer, nullable=False),
    db.Column('Specimen_code', db.Integer, nullable=False),
    db.Column('Specimen_concentration', db.Integer, nullable=False),
    db.Column('Specimen_volume', db.Integer, nullable=False),
    db.Column('Specimen_comments', db.Integer, nullable=False),
    db.Column('SamplePlatePosition_samplePlatePositionId',
              db.Integer, nullable=False),
    db.Column('SamplePlatePosition_samplePlateId', db.Integer, nullable=False),
    db.Column('SamplePlatePosition_rowNumber', db.Integer, nullable=False),
    db.Column('SamplePlatePosition_columnNumber', db.Integer, nullable=False),
    db.Column('SamplePlatePosition_volume', db.Integer, nullable=False),
    db.Column('samplePlateId', db.Integer, nullable=False),
    db.Column('experimentId', db.Integer, nullable=False),
    db.Column('plateGroupId', db.Integer, nullable=False),
    db.Column('plateTypeId', db.Integer, nullable=False),
    db.Column('instructionSetId', db.Integer, nullable=False),
    db.Column('SamplePlate_boxId', db.Integer, nullable=False),
    db.Column('SamplePlate_name', db.Integer, nullable=False),
    db.Column('SamplePlate_slotPositionRow', db.Integer, nullable=False),
    db.Column('SamplePlate_slotPositionColumn', db.Integer, nullable=False),
    db.Column('SamplePlate_storageTemperature', db.Integer, nullable=False),
    db.Column('Experiment_experimentId', db.Integer, nullable=False),
    db.Column('Experiment_sessionId', db.Integer, nullable=False),
    db.Column('Experiment_proposalId', db.Integer, nullable=False),
    db.Column('Experiment_name', db.Integer, nullable=False),
    db.Column('Experiment_creationDate', db.Integer, nullable=False),
    db.Column('Experiment_experimentType', db.Integer, nullable=False),
    db.Column('Experiment_sourceFilePath', db.Integer, nullable=False),
    db.Column('Experiment_dataAcquisitionFilePath',
              db.Integer, nullable=False),
    db.Column('Experiment_status', db.Integer, nullable=False),
    db.Column('Experiment_comments', db.Integer, nullable=False),
    db.Column('Measurement_priorityLevelId', db.Integer, nullable=False),
    db.Column('Measurement_exposureTemperature', db.Integer, nullable=False),
    db.Column('Measurement_viscosity', db.Integer, nullable=False),
    db.Column('Measurement_flow', db.Integer, nullable=False),
    db.Column('Measurement_extraFlowTime', db.Integer, nullable=False),
    db.Column('Measurement_volumeToLoad', db.Integer, nullable=False),
    db.Column('Measurement_waitTime', db.Integer, nullable=False),
    db.Column('Measurement_transmission', db.Integer, nullable=False),
    db.Column('Measurement_comments', db.Integer, nullable=False),
    db.Column('Measurement_imageDirectory', db.Integer, nullable=False),
    db.Column('Run_runId', db.Integer, nullable=False),
    db.Column('Run_timePerFrame', db.Integer, nullable=False),
    db.Column('Run_timeStart', db.Integer, nullable=False),
    db.Column('Run_timeEnd', db.Integer, nullable=False),
    db.Column('Run_storageTemperature', db.Integer, nullable=False),
    db.Column('Run_exposureTemperature', db.Integer, nullable=False),
    db.Column('Run_spectrophotometer', db.Integer, nullable=False),
    db.Column('Run_energy', db.Integer, nullable=False),
    db.Column('Run_creationDate', db.Integer, nullable=False),
    db.Column('Run_frameAverage', db.Integer, nullable=False),
    db.Column('Run_frameCount', db.Integer, nullable=False),
    db.Column('Run_transmission', db.Integer, nullable=False),
    db.Column('Run_beamCenterX', db.Integer, nullable=False),
    db.Column('Run_beamCenterY', db.Integer, nullable=False),
    db.Column('Run_pixelSizeX', db.Integer, nullable=False),
    db.Column('Run_pixelSizeY', db.Integer, nullable=False),
    db.Column('Run_radiationRelative', db.Integer, nullable=False),
    db.Column('Run_radiationAbsolute', db.Integer, nullable=False),
    db.Column('Run_normalization', db.Integer, nullable=False),
    db.Column('Merge_mergeId', db.Integer, nullable=False),
    db.Column('Merge_measurementId', db.Integer, nullable=False),
    db.Column('Merge_frameListId', db.Integer, nullable=False),
    db.Column('Merge_discardedFrameNameList', db.Integer, nullable=False),
    db.Column('Merge_averageFilePath', db.Integer, nullable=False),
    db.Column('Merge_framesCount', db.Integer, nullable=False),
    db.Column('Merge_framesMerge', db.Integer, nullable=False),
    db.Column('Merge_creationDate', db.Integer, nullable=False),
    db.Column('Subtraction_dataCollectionId', db.Integer, nullable=False),
    db.Column('Subtraction_rg', db.Integer, nullable=False),
    db.Column('Subtraction_rgStdev', db.Integer, nullable=False),
    db.Column('Subtraction_I0', db.Integer, nullable=False),
    db.Column('Subtraction_I0Stdev', db.Integer, nullable=False),
    db.Column('Subtraction_firstPointUsed', db.Integer, nullable=False),
    db.Column('Subtraction_lastPointUsed', db.Integer, nullable=False),
    db.Column('Subtraction_quality', db.Integer, nullable=False),
    db.Column('Subtraction_isagregated', db.Integer, nullable=False),
    db.Column('Subtraction_concentration', db.Integer, nullable=False),
    db.Column('Subtraction_gnomFilePath', db.Integer, nullable=False),
    db.Column('Subtraction_rgGuinier', db.Integer, nullable=False),
    db.Column('Subtraction_rgGnom', db.Integer, nullable=False),
    db.Column('Subtraction_dmax', db.Integer, nullable=False),
    db.Column('Subtraction_total', db.Integer, nullable=False),
    db.Column('Subtraction_volume', db.Integer, nullable=False),
    db.Column('Subtraction_creationTime', db.Integer, nullable=False),
    db.Column('Subtraction_kratkyFilePath', db.Integer, nullable=False),
    db.Column('Subtraction_scatteringFilePath', db.Integer, nullable=False),
    db.Column('Subtraction_guinierFilePath', db.Integer, nullable=False),
    db.Column('Subtraction_substractedFilePath', db.Integer, nullable=False),
    db.Column('Subtraction_gnomFilePathOutput', db.Integer, nullable=False),
    db.Column('Subtraction_sampleOneDimensionalFiles',
              db.Integer, nullable=False),
    db.Column('Subtraction_bufferOnedimensionalFiles',
              db.Integer, nullable=False),
    db.Column('Subtraction_sampleAverageFilePath', db.Integer, nullable=False),
    db.Column('Subtraction_bufferAverageFilePath', db.Integer, nullable=False)
)


t_v_session = db.Table(
    'v_session',
    db.Column('sessionId', db.Integer, nullable=False),
    db.Column('expSessionPk', db.Integer, nullable=False),
    db.Column('beamLineSetupId', db.Integer, nullable=False),
    db.Column('proposalId', db.Integer, nullable=False),
    db.Column('projectCode', db.Integer, nullable=False),
    db.Column('BLSession_startDate', db.Integer, nullable=False),
    db.Column('BLSession_endDate', db.Integer, nullable=False),
    db.Column('beamLineName', db.Integer, nullable=False),
    db.Column('scheduled', db.Integer, nullable=False),
    db.Column('nbShifts', db.Integer, nullable=False),
    db.Column('comments', db.Integer, nullable=False),
    db.Column('beamLineOperator', db.Integer, nullable=False),
    db.Column('visit_number', db.Integer, nullable=False),
    db.Column('bltimeStamp', db.Integer, nullable=False),
    db.Column('usedFlag', db.Integer, nullable=False),
    db.Column('sessionTitle', db.Integer, nullable=False),
    db.Column('structureDeterminations', db.Integer, nullable=False),
    db.Column('dewarTransport', db.Integer, nullable=False),
    db.Column('databackupFrance', db.Integer, nullable=False),
    db.Column('databackupEurope', db.Integer, nullable=False),
    db.Column('operatorSiteNumber', db.Integer, nullable=False),
    db.Column('BLSession_lastUpdate', db.Integer, nullable=False),
    db.Column('BLSession_protectedData', db.Integer, nullable=False),
    db.Column('Proposal_title', db.Integer, nullable=False),
    db.Column('Proposal_proposalCode', db.Integer, nullable=False),
    db.Column('Proposal_ProposalNumber', db.Integer, nullable=False),
    db.Column('Proposal_ProposalType', db.Integer, nullable=False),
    db.Column('Person_personId', db.Integer, nullable=False),
    db.Column('Person_familyName', db.Integer, nullable=False),
    db.Column('Person_givenName', db.Integer, nullable=False),
    db.Column('Person_emailAddress', db.Integer, nullable=False)
)


t_v_tracking_shipment_history = db.Table(
    'v_tracking_shipment_history',
    db.Column('Dewar_dewarId', db.Integer, nullable=False),
    db.Column('Dewar_code', db.Integer, nullable=False),
    db.Column('Dewar_comments', db.Integer, nullable=False),
    db.Column('Dewar_dewarStatus', db.Integer, nullable=False),
    db.Column('Dewar_barCode', db.Integer, nullable=False),
    db.Column('Dewar_firstExperimentId', db.Integer, nullable=False),
    db.Column('Dewar_trackingNumberToSynchrotron', db.Integer, nullable=False),
    db.Column('Dewar_trackingNumberFromSynchrotron',
              db.Integer, nullable=False),
    db.Column('Dewar_type', db.Integer, nullable=False),
    db.Column('Shipping_shippingId', db.Integer, nullable=False),
    db.Column('Shipping_proposalId', db.Integer, nullable=False),
    db.Column('Shipping_shippingName', db.Integer, nullable=False),
    db.Column('deliveryAgent_agentName', db.Integer, nullable=False),
    db.Column('Shipping_deliveryAgent_shippingDate',
              db.Integer, nullable=False),
    db.Column('Shipping_deliveryAgent_deliveryDate',
              db.Integer, nullable=False),
    db.Column('Shipping_shippingStatus', db.Integer, nullable=False),
    db.Column('Shipping_returnCourier', db.Integer, nullable=False),
    db.Column('Shipping_dateOfShippingToUser', db.Integer, nullable=False),
    db.Column('DewarTransportHistory_DewarTransportHistoryId',
              db.Integer, nullable=False),
    db.Column('DewarTransportHistory_dewarStatus', db.Integer, nullable=False),
    db.Column('DewarTransportHistory_storageLocation',
              db.Integer, nullable=False),
    db.Column('DewarTransportHistory_arrivalDate', db.Integer, nullable=False)
)


t_v_week = db.Table(
    'v_week',
    db.Column('num', db.Integer, nullable=False)
)


t_v_weekDay = db.Table(
    'v_weekDay',
    db.Column('day', db.Integer, nullable=False)
)


t_v_xfeFluorescenceSpectrum = db.Table(
    'v_xfeFluorescenceSpectrum',
    db.Column('xfeFluorescenceSpectrumId', db.Integer, nullable=False),
    db.Column('sessionId', db.Integer, nullable=False),
    db.Column('blSampleId', db.Integer, nullable=False),
    db.Column('fittedDataFileFullPath', db.Integer, nullable=False),
    db.Column('scanFileFullPath', db.Integer, nullable=False),
    db.Column('jpegScanFileFullPath', db.Integer, nullable=False),
    db.Column('startTime', db.Integer, nullable=False),
    db.Column('endTime', db.Integer, nullable=False),
    db.Column('filename', db.Integer, nullable=False),
    db.Column('energy', db.Integer, nullable=False),
    db.Column('exposureTime', db.Integer, nullable=False),
    db.Column('beamTransmission', db.Integer, nullable=False),
    db.Column('annotatedPymcaXfeSpectrum', db.Integer, nullable=False),
    db.Column('beamSizeVertical', db.Integer, nullable=False),
    db.Column('beamSizeHorizontal', db.Integer, nullable=False),
    db.Column('crystalClass', db.Integer, nullable=False),
    db.Column('comments', db.Integer, nullable=False),
    db.Column('flux', db.Integer, nullable=False),
    db.Column('flux_end', db.Integer, nullable=False),
    db.Column('workingDirectory', db.Integer, nullable=False),
    db.Column('BLSample_sampleId', db.Integer, nullable=False),
    db.Column('BLSession_proposalId', db.Integer, nullable=False)
)
