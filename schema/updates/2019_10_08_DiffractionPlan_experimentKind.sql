INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_10_08_DiffractionPlan_experimentKind.sql', 'ONGOING');

ALTER TABLE DiffractionPlan
  MODIFY `experimentKind` enum('Default','MXPressE','MXPressO','MXPressE_SAD','MXScore','MXPressM','MAD','SAD','Fixed','Ligand binding','Refinement','OSC','MAD - Inverse Beam','SAD - Inverse Beam','MESH','XFE', 'Stepped transmission') DEFAULT NULL;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_10_08_DiffractionPlan_experimentKind.sql';
