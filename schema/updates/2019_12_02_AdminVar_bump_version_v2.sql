INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_12_02_AdminVar_bump_version_v2.sql', 'ONGOING');

UPDATE AdminVar SET `value` = '1.9.1' WHERE `name` = 'schemaVersion';

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_12_02_AdminVar_bump_version_v2.sql';
