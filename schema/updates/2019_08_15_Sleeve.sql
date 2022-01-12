INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_08_15_Sleeve.sql', 'ONGOING');

CREATE TABLE Sleeve (
  sleeveId tinyint unsigned PRIMARY KEY COMMENT 'The unique sleeve id 1...255 which also identifies its home location in the freezer',
  location tinyint unsigned COMMENT 'NULL == freezer, 1...255 for local storage locations',
  lastMovedToFreezer timestamp NOT NULL DEFAULT current_timestamp,
  lastMovedFromFreezer timestamp NULL DEFAULT current_timestamp
) COMMENT='Registry of ice-filled sleeves used to cool plates whilst on the goniometer';

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_08_15_Sleeve.sql';
