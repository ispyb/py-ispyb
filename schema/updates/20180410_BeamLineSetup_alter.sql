INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('20180410_BeamLineSetup_alter.sql', 'ONGOING');

ALTER TABLE BeamLineSetup
  ADD detectorId int(11) AFTER beamLineSetupId,
  ADD beamSizeXMin float COMMENT 'unit: um',
  ADD beamSizeXMax float COMMENT 'unit: um',
  ADD beamSizeYMin float COMMENT 'unit: um',
  ADD beamSizeYMax float COMMENT 'unit: um',
  ADD energyMin float COMMENT 'unit: eV',
  ADD energyMax float COMMENT 'unit: eV',
  ADD omegaMin float COMMENT 'unit: degrees',
  ADD omegaMax float COMMENT 'unit: degrees',
  ADD kappaMin float COMMENT 'unit: degrees',
  ADD kappaMax float COMMENT 'unit: degrees',
  ADD phiMin float COMMENT 'unit: degrees',
  ADD phiMax float COMMENT 'unit: degrees',
  ADD goniostatMaxOscillationWidth double COMMENT 'unit: degrees' AFTER goniostatMaxOscillationSpeed,
  ADD maxExposureTimePerImage float  COMMENT 'unit: seconds' AFTER maxExpTimePerDataCollection,
  ADD maxTransmission double COMMENT 'unit: percentage' AFTER goniostatMinOscillationWidth,
  ADD active boolean NOT NULL DEFAULT 0 COMMENT 'Whether the BeamLineSetup is active (1) or not (0)',
  ADD numberOfImagesMax mediumint unsigned,
  ADD numberOfImagesMin mediumint unsigned,
  ADD boxSizeXMin double COMMENT 'For gridscans, unit: um',
  ADD boxSizeXMax double COMMENT 'For gridscans, unit: um',
  ADD boxSizeYMin double COMMENT 'For gridscans, unit: um',
  ADD boxSizeYMax double COMMENT 'For gridscans, unit: um',
  ADD CONSTRAINT BeamLineSetup_ibfk_1 FOREIGN KEY (detectorId) REFERENCES Detector(detectorId) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- ALTER TABLE BeamLineSetup
--   MODIFY active boolean NOT NULL DEFAULT 0;

UPDATE SchemaStatus SET schemaStatus = 'DONE' where scriptName = '20180410_BeamLineSetup_alter.sql';
