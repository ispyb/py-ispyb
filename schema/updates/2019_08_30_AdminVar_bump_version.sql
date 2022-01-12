INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_08_30_AdminVar_bump_version.sql', 'ONGOING');

UPDATE AdminVar SET `value` = '1.6.2' WHERE `name` = 'schemaVersion';

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_08_30_AdminVar_bump_version.sql';
