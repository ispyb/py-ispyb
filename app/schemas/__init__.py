from ispyb import api

from ispyb.schemas.auto_proc import auto_proc_dict, AutoProcSchema
f_auto_proc_schema = api.model('AutoProc', auto_proc_dict)
ma_auto_proc_schema = AutoProcSchema()

from ispyb.schemas.auto_proc_integration import auto_proc_integration_dict, AutoProcIntegrationSchema
f_auto_proc_integration_schema = api.model('AutoProcIntegration', auto_proc_integration_dict)
ma_auto_proc_integration_schema = AutoProcIntegrationSchema()

from ispyb.schemas.auto_proc_program import auto_proc_program_dict, AutoProcProgramSchema
f_auto_proc_program_schema = api.model('AutoProcProgram', auto_proc_program_dict)
ma_auto_proc_program_schema = AutoProcProgramSchema()

from ispyb.schemas.auto_proc_program_attachment import auto_proc_program_attachment_dict, AutoProcProgramAttachmentSchema
f_auto_proc_program_attachment_schema = api.model('AutoProcProgramAttachment', auto_proc_program_attachment_dict)
ma_auto_proc_program_attachment_schema = AutoProcProgramAttachmentSchema()

from ispyb.schemas.auto_proc_program_message import auto_proc_program_message_dict, AutoProcProgramMessageSchema
f_auto_proc_program_message_schema = api.model('AutoProcProgramMessage', auto_proc_program_message_dict)
ma_auto_proc_program_message_schema = AutoProcProgramMessageSchema()

from ispyb.schemas.auto_proc_scaling import auto_proc_scaling_dict, AutoProcScalingSchema
f_auto_proc_scaling_schema = api.model('AutoProcScaling', auto_proc_scaling_dict)
ma_auto_proc_scaling_schema = AutoProcScalingSchema()

from ispyb.schemas.auto_proc_scaling_statistics import auto_proc_scaling_statistics_dict, AutoProcScalingStatisticsSchema
f_auto_proc_scaling_statistics_schema = api.model('AutoProcScalingStatistics', auto_proc_scaling_statistics_dict)
ma_auto_proc_scaling_statistics_schema = AutoProcScalingStatisticsSchema()

from ispyb.schemas.session import session_dict, SessionSchema
f_session_schema = api.model('Session', session_dict)
ma_session_schema = SessionSchema()

from ispyb.schemas.beam_line_setup import beam_line_setup_dict, BeamLineSetupSchema
f_beam_line_setup_schema = api.model('BeamLineSetup', beam_line_setup_dict)
ma_beam_line_setup_schema = BeamLineSetupSchema()

from ispyb.schemas.container import container_dict, ContainerSchema
f_container_schema = api.model('Container', container_dict)
ma_container_schema = ContainerSchema()

from ispyb.schemas.crystal import crystal_dict, CrystalSchema
f_crystal_schema = api.model('Crystal', crystal_dict)
ma_crystal_schema = CrystalSchema()

from ispyb.schemas.data_collection import data_collection_dict, DataCollectionSchema
f_data_collection_schema = api.model('DataCollection', data_collection_dict)
ma_data_collection_schema = DataCollectionSchema()

from ispyb.schemas.data_collection_group import data_collection_group_dict, DataCollectionGroupSchema
f_data_collection_group_schema = api.model('DataCollectionGroup', data_collection_group_dict)
ma_data_collection_group_schema = DataCollectionGroupSchema()

from ispyb.schemas.detector import detector_dict, DetectorSchema
f_detector_schema = api.model('Detector', detector_dict)
ma_detector_schema = DetectorSchema()

from ispyb.schemas.energy_scan import energy_scan_dict, EnergyScanSchema
f_energy_scan_schema = api.model('EnergyScan', energy_scan_dict)
ma_energy_scan_schema = EnergyScanSchema()

from ispyb.schemas.image_quality_indicators import image_quality_indicators_dict, ImageQualityIndicatorsSchema
f_image_quality_indicators_schema = api.model('ImageQualityIndicators', image_quality_indicators_dict)
ma_image_quality_indicators_schema = ImageQualityIndicatorsSchema()

from ispyb.schemas.person import person_dict, PersonSchema
f_person_schema = api.model('Person', person_dict)
ma_person_schema = PersonSchema()

from ispyb.schemas.proposal import proposal_dict, ProposalSchema
f_proposal_schema = api.model('Proposal', proposal_dict)
ma_proposal_schema = ProposalSchema()

from ispyb.schemas.protein import protein_dict, ProteinSchema
f_protein_schema = api.model('Protein', protein_dict)
ma_protein_schema = ProteinSchema()

from ispyb.schemas.robot_action import robot_action_dict, RobotActionSchema
f_robot_action_schema = api.model('RobotAction', robot_action_dict)
ma_robot_action_schema = RobotActionSchema()

from ispyb.schemas.screening import screening_dict, ScreeningSchema
f_screening_schema = api.model('Screening', screening_dict)
ma_screening_schema = ScreeningSchema()

from ispyb.schemas.shipping import shipping_dict, ShippingSchema
f_shipping_schema = api.model('Shipping', shipping_dict)
ma_shipping_schema = ShippingSchema()

