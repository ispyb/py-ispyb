INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_07_17_BLSample_crystalId_default.sql', 'ONGOING');

ALTER TABLE BLSample MODIFY crystalId int(10) unsigned DEFAULT NULL;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_07_17_BLSample_crystalId_default.sql';

