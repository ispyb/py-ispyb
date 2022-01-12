INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_11_01_DiffractionPlan_centeringMethod.sql', 'ONGOING');

ALTER TABLE DiffractionPlan
  ADD centeringMethod enum('xray', 'loop', 'diffraction', 'optical') NULL;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_11_01_DiffractionPlan_centeringMethod.sql';
