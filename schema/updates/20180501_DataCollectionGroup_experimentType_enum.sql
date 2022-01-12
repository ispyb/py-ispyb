INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('20180501_DataCollectionGroup_experimentType_enum.sql', 'ONGOING');

ALTER TABLE DataCollectionGroup MODIFY experimentType enum('SAD','SAD - Inverse Beam','OSC','Collect - Multiwedge','MAD','Helical','Multi-positional','Mesh','Burn','MAD - Inverse Beam','Characterization','Dehydration','tomo','experiment','EM','PDF','PDF+Bragg','Bragg','single particle', 'Serial Fixed', 'Serial Jet'), ALGORITHM=INPLACE;

UPDATE SchemaStatus SET schemaStatus = 'DONE' where scriptName = '20180501_DataCollectionGroup_experimentType_enum.sql';
