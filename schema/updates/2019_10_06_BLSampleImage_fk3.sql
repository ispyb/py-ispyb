INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_10_06_BLSampleImage_fk3.sql', 'ONGOING');

ALTER TABLE BLSampleImage
  MODIFY blSampleImageScoreId int(11) unsigned DEFAULT NULL,
  ADD CONSTRAINT BLSampleImage_fk3 FOREIGN KEY (blSampleImageScoreId) REFERENCES BLSampleImageScore(blSampleImageScoreId) ON DELETE NO ACTION ON UPDATE CASCADE;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_10_06_BLSampleImage_fk3.sql';
