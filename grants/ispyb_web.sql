-- Create the web application role.
CREATE ROLE IF NOT EXISTS ispyb_web;

-- You must also create a database user and grant this role to them, e.g.
-- CREATE USER synchweb@'%' IDENTIFIED BY 'the_synchweb_password';
-- GRANT ispyb_web to synchweb@'%';
-- SET DEFAULT ROLE ispyb_web FOR synchweb@'%';

-- The grants for the web application role:
GRANT SELECT ON * TO 'ispyb_web';
GRANT SELECT, UPDATE, INSERT ON BLSession TO 'ispyb_web';
GRANT SELECT, INSERT ON SessionType TO 'ispyb_web';
GRANT SELECT, INSERT, UPDATE, DELETE ON BeamLineSetup TO 'ispyb_web';
GRANT UPDATE ON DataCollection TO 'ispyb_web';
GRANT SELECT, UPDATE ON EnergyScan TO 'ispyb_web';
GRANT SELECT, UPDATE ON XFEFluorescenceSpectrum TO 'ispyb_web';
GRANT UPDATE ON DataCollectionGroup TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON DataCollectionComment TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Shipping TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ShippingHasSession TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Dewar TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON DewarTransportHistory TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON DewarLocation TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON `Container` TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ContainerHistory TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ContainerQueue TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ContainerQueueSample TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BLSample TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BLSubSample TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BLSampleGroup TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BLSampleGroup_has_BLSample TO 'ispyb_web';
GRANT SELECT, INSERT, UPDATE ON Position TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Crystal TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Crystal_has_UUID TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Protein TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Protein_has_PDB TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON PDB TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON PDBEntry TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON DiffractionPlan TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ExperimentKindDetails TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON LabContact TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Person TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Laboratory TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON `Project` TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Project_has_BLSample TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Project_has_DCGroup TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Project_has_EnergyScan TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Project_has_Person TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Project_has_Protein TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Project_has_Session TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Project_has_Shipping TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Project_has_User TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Project_has_XFEFSpectrum TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON PHPSession TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON UserGroup_has_Permission TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Permission TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON UserGroup_has_Person TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON `UserGroup` TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON Component_has_SubType TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BLSampleType_has_Component TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ComponentSubType TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ConcentrationType TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ComponentType TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ComponentLattice TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON AdminActivity TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON AdminVar TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON DewarRegistry TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON DewarReport TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON ContainerRegistry TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ContainerRegistry_has_Proposal TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ContainerReport TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON BF_component TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BF_component_beamline TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BF_fault TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BF_subcomponent TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BF_subcomponent_beamline TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BF_system TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BF_system_beamline TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON CourierTermsAccepted TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON CalendarHash TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON Schedule TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON ScheduleComponent TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON Screen TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ScreenComponent TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ScreenComponentGroup TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ContainerInspection TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON ComponentSubType TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ComponentType TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON Component_has_SubType TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON ConcentrationType TO 'ispyb_web';

GRANT INSERT, UPDATE, DELETE ON BLSampleImageScore TO 'ispyb_web';
GRANT INSERT, UPDATE, DELETE ON BLSampleImage TO 'ispyb_web';

GRANT SELECT, INSERT, UPDATE ON Log4Stat TO 'ispyb_web';
GRANT SELECT, INSERT, UPDATE, DELETE ON SW_onceToken TO 'ispyb_web';

GRANT SELECT, INSERT, UPDATE, DELETE ON BLSample_has_DataCollectionPlan TO 'ispyb_web';
GRANT SELECT, INSERT, UPDATE ON Detector TO 'ispyb_web';
GRANT SELECT, INSERT, UPDATE, DELETE ON DataCollectionPlan_has_Detector TO 'ispyb_web';
GRANT SELECT, INSERT, UPDATE, DELETE ON ScanParametersModel TO 'ispyb_web';
GRANT SELECT, INSERT, UPDATE, DELETE ON ScanParametersService TO 'ispyb_web';

GRANT SELECT, INSERT, UPDATE, DELETE ON XRFFluorescenceMappingROI TO 'ispyb_web';
GRANT SELECT, INSERT, UPDATE, DELETE ON XRFFluorescenceMapping TO 'ispyb_web';

GRANT SELECT ON Movie TO 'ispyb_web';
GRANT SELECT ON `CTF` TO 'ispyb_web';
GRANT SELECT ON `MotionCorrection` TO 'ispyb_web';
GRANT SELECT ON `MotionCorrectionDrift` TO 'ispyb_web';
