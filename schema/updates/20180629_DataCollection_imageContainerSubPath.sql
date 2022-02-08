INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('20180629_DataCollection_imageContainerSubPath.sql', 'ONGOING');

-- pt-online-schema-change --execute --alter-foreign-keys-method=auto --alter "ADD imageContainerSubPath VARCHAR(255) COMMENT 'Internal path of a HDF5 file pointing to the data for this data collection' AFTER imageSuffix" D=ispyb,t=DataCollection,h=localhost

ALTER TABLE DataCollection ADD imageContainerSubPath VARCHAR(255) COMMENT 'Internal path of a HDF5 file pointing to the data for this data collection' AFTER imageSuffix, ALGORITHM=INPLACE;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '20180629_DataCollection_imageContainerSubPath.sql';
