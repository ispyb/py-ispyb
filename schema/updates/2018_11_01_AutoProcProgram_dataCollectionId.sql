INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_11_01_AutoProcProgram_dataCollectionId.sql', 'ONGOING');

-- Warning: This will take a while to complete at least on MariaDB 10.2 

SET foreign_key_checks=OFF;
ALTER TABLE AutoProcProgram
  ADD dataCollectionId int(11) unsigned,
  ADD CONSTRAINT AutoProcProgram_fk3 FOREIGN KEY (dataCollectionId) REFERENCES DataCollection(dataCollectionId),
  ALGORITHM=INPLACE;
SET foreign_key_checks=ON;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_11_01_AutoProcProgram_dataCollectionId.sql';
