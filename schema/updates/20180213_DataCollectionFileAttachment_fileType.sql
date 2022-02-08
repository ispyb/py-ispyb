INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('20180213_DataCollectionFileAttachment_fileType.sql', 'ONGOING');

ALTER TABLE DataCollectionFileAttachment 
  MODIFY fileType ENUM('snapshot','log','xy','recip', 'pia') 
    COMMENT 'snapshot: image file, usually of the sample. log: a text file with logging info. xy: x and y data in text format. recip: a reciprocal space viewer file. pia: per image analysis';

UPDATE SchemaStatus SET schemaStatus = 'DONE' where scriptName = '20180213_DataCollectionFileAttachment_fileType.sql';