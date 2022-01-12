INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('20180413_BeamLineSetup_and_Detector_alter.sql', 'ONGOING');

ALTER TABLE BeamLineSetup
  ADD monoBandwidthMin double COMMENT 'unit: percentage',
  ADD monoBandwidthMax double COMMENT 'unit: percentage';

ALTER TABLE Detector
  ADD detectorRollMin double COMMENT 'unit: degrees',
  ADD detectorRollMax  double COMMENT 'unit: degrees';

UPDATE SchemaStatus SET schemaStatus = 'DONE' where scriptName = '20180413_BeamLineSetup_and_Detector_alter.sql';
