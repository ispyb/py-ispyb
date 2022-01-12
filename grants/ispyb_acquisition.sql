-- Create the processing application role.
CREATE ROLE IF NOT EXISTS ispyb_acquisition;

-- You must also create a database user and grant this role to them, e.g.
-- CREATE USER gda@'%' IDENTIFIED BY 'the_gda_password';
-- GRANT ispyb_acquisition to gda@'%';
-- SET DEFAULT ROLE ispyb_acquisition FOR gda@'%';

-- Grants for ispyb_acquisition
GRANT SELECT ON `AdminVar` TO 'ispyb_acquisition';

GRANT EXECUTE ON PROCEDURE retrieve_test TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_container_ls_position TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_container_info TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_container_on_gonio TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE update_container_ls_position TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE update_container_status TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_containers_on_beamline_with_status TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE finish_container TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_container_ls_queue TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_container_queue_timestamp TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_container_queue_most_recent_completed_timestamp TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_container_subsamples TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE insert_container_error TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE clear_container_error TO 'ispyb_acquisition';

GRANT EXECUTE ON PROCEDURE retrieve_session_id TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_dc_infos_for_subsample TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE upsert_dc_group TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE upsert_dc_main TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE update_dc_experiment TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE update_dc_machine TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE upsert_sample_image_analysis TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE upsert_dcg_grid TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE update_dc_position TO 'ispyb_acquisition';

GRANT EXECUTE ON PROCEDURE `update_dc_experiment_v2` TO 'ispyb_acquisition';

GRANT EXECUTE ON PROCEDURE `upsert_dc_main_v2` TO 'ispyb_acquisition';

GRANT EXECUTE ON PROCEDURE `upsert_dc_main_v3` TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE `upsert_dc_group_v2` TO 'ispyb_acquisition';

GRANT EXECUTE ON PROCEDURE `retrieve_container_subsamples_v2` TO 'ispyb_acquisition';

GRANT EXECUTE ON PROCEDURE upsert_dc_group_v3 TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_dc_group TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_dc_group_v2 TO 'ispyb_acquisition';

GRANT EXECUTE ON PROCEDURE retrieve_sleeve TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE retrieve_sleeves TO 'ispyb_acquisition';
GRANT EXECUTE ON PROCEDURE upsert_sleeve TO 'ispyb_acquisition';
