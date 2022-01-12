INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_12_20_DataCollectionGroup_scanParameters.sql', 'ONGOING');

ALTER TABLE DataCollectionGroup ADD scanParameters JSON CHECK (JSON_VALID(scanParameters)), ALGORITHM=INSTANT;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_12_20_DataCollectionGroup_scanParameters.sql';



