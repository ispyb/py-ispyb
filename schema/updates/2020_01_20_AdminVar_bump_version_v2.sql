INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2020_01_20_AdminVar_bump_version_v2.sql', 'ONGOING');

UPDATE AdminVar SET `value` = '1.10.4' WHERE `name` = 'schemaVersion';

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2020_01_20_AdminVar_bump_version_v2.sql';

