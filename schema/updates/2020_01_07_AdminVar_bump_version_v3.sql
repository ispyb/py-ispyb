INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2020_01_07_AdminVar_bump_version_v3.sql', 'ONGOING');

UPDATE AdminVar SET `value` = '1.10.2' WHERE `name` = 'schemaVersion';

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2020_01_07_AdminVar_bump_version_v3.sql';
