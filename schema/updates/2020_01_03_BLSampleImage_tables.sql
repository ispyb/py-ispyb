INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2020_01_03_BLSampleImage_tables.sql', 'ONGOING');

CREATE TABLE BLSampleImageAutoScoreSchema (
  blSampleImageAutoScoreSchemaId tinyint(3) unsigned auto_increment PRIMARY KEY,
  schemaName varchar(25) NOT NULL COMMENT 'Name of the schema e.g. Hampton, MARCO',
  enabled tinyint(1) DEFAULT 1 COMMENT 'Whether this schema is enabled (could be configurable in the UI)'
) COMMENT 'Scoring schema name and whether it is enabled';

CREATE TABLE BLSampleImageAutoScoreClass (
  blSampleImageAutoScoreClassId tinyint(3) unsigned auto_increment PRIMARY KEY,
  blSampleImageAutoScoreSchemaId tinyint(3) unsigned,
  scoreClass varchar(15) NOT NULL COMMENT 'Thing being scored e.g. crystal, precipitant',
  CONSTRAINT BLSampleImageAutoScoreClass_fk1 FOREIGN KEY (blSampleImageAutoScoreSchemaId) REFERENCES BLSampleImageAutoScoreSchema(blSampleImageAutoScoreSchemaId) ON DELETE NO ACTION ON UPDATE CASCADE
) COMMENT 'The automated scoring classes - the thing being scored';

CREATE TABLE BLSampleImage_has_AutoScoreClass (
  blSampleImageId int(11) unsigned NOT NULL,
  blSampleImageAutoScoreClassId tinyint(3) unsigned,
  probability float,
  PRIMARY KEY (blSampleImageId, blSampleImageAutoScoreClassId),
  CONSTRAINT BLSampleImage_has_AutoScoreClass_fk1 FOREIGN KEY (blSampleImageId) REFERENCES BLSampleImage(blSampleImageId) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT BLSampleImage_has_AutoScoreClass_fk2 FOREIGN KEY (blSampleImageAutoScoreClassId) REFERENCES BLSampleImageAutoScoreClass(blSampleImageAutoScoreClassId) ON DELETE CASCADE ON UPDATE CASCADE
) COMMENT 'Many-to-many relationship between drop images and thing being scored, as well as the actual probability (score) that the drop image contains that thing';

INSERT INTO BLSampleImageAutoScoreSchema (
  blSampleImageAutoScoreSchemaId, schemaName, enabled)
  VALUES (1, 'MARCO', 1);

INSERT INTO BLSampleImageAutoScoreClass (
  blSampleImageAutoScoreClassId, blSampleImageAutoScoreSchemaId, scoreClass)
VALUES
  (1, 1, 'clear'),
  (2, 1, 'crystal'),
  (3, 1, 'precipitant'),
  (4, 1, 'other');

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2020_01_03_BLSampleImage_tables.sql';
