INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('20180328_ImageQualityIndicators_alter_table.sql', 'ONGOING');

ALTER TABLE ImageQualityIndicators
  MODIFY dataCollectionId int(11) unsigned NOT NULL FIRST,
  MODIFY imageNumber mediumint(8) unsigned NOT NULL AFTER dataCollectionId,
  DROP FOREIGN KEY _ImageQualityIndicators_ibfk3,
  DROP KEY ImageQualityIndicators_ibfk3,
  DROP PRIMARY KEY,
  DROP imageQualityIndicatorsId,
  ADD PRIMARY KEY (dataCollectionId, imageNumber);

-- pt-online-schema-change --execute --no-check-alter --alter "MODIFY dataCollectionId int(11) unsigned NOT NULL FIRST, MODIFY imageNumber mediumint(8) unsigned NOT NULL AFTER dataCollectionId, DROP FOREIGN KEY _ImageQualityIndicators_ibfk3, DROP KEY ImageQualityIndicators_ibfk3, DROP PRIMARY KEY, DROP imageQualityIndicatorsId, ADD PRIMARY KEY (dataCollectionId, imageNumber)" D=ispyb,t=ImageQualityIndicators,h=localhost

UPDATE SchemaStatus SET schemaStatus = 'DONE' where scriptName = '20180328_ImageQualityIndicators_alter_table.sql';
