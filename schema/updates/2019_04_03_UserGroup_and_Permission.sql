-- Warning: This assumes you have used exactly the same rows as previously found in the UserGroup, 
-- Permission and UserGroup_has_Permission tables in schema/data.sql.

INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_04_03_UserGroup_and_Permission.sql', 'ONGOING');

INSERT IGNORE INTO UserGroup (userGroupId, name) VALUES (17, 'bag_stats');
INSERT IGNORE INTO UserGroup (userGroupId, name) VALUES (20, 'bl_stats');
INSERT IGNORE INTO UserGroup (userGroupId, name) VALUES (24, 'temp_mx_admin');
INSERT IGNORE INTO UserGroup (userGroupId, name) VALUES (28, 'ship_manage');
INSERT IGNORE INTO UserGroup (userGroupId, name) VALUES (34, 'xpdf_admin');
INSERT IGNORE INTO UserGroup (userGroupId, name) VALUES (39, 'autocollect');

INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (20, 'pow_admin', 'Power Admin');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (23, 'all_dewars', 'View All Dewars');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (26, 'all_prop_stats', 'View All Proposal Stats');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (29, 'all_breakdown', 'View Aggregated Visit Breakdown Stats');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (32, 'disp_cont', 'VMXi Dispose Container');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (37, 'view_manifest', 'View Shipping Manifest');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (43, 'schedule_comp', 'typo fill in');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (49, 'xpdf_admin', 'XPDF Admin');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (55, 'edit_presets', 'Edit Beamline DC Presets');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (58, 'manage_params', 'Edit Beamline Parameter Limits');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (64, 'manage_detector', 'Manage Beamline Detector Limits');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (69, 'auto_dash', 'AutoCollect Dashboard');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (77, 'fault_admin', 'Edit Fault Categories');
INSERT IGNORE INTO Permission (permissionId, `type`, description) VALUES (80, 'fault_add', 'Add New Fault Reports');

INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (1, 11);
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (1, 20);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (1, 23);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (1, 49);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (2, 6);                                            
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (2, 23);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (2, 80);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (3, 7);                                            
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (3, 23);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (4, 20);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (5, 10);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (6, 8);                                            
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (6, 23);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (8, 6);                                            
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (8, 20);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (8, 23);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (8, 26);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (8, 29);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (8, 37);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (8, 49);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (10, 77);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (11, 32);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (11, 43);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (11, 55);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (11, 58);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (11, 64);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (17, 26);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (20, 29);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (24, 1);                                           
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (28, 23);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (28, 37);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (34, 49);                                          
INSERT IGNORE INTO UserGroup_has_Permission (userGroupId, permissionId) VALUES (39, 69);                                          

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_04_03_UserGroup_and_Permission.sql';
