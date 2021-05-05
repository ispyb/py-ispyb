# Generates sqlalchemy db models
bash generate_core_models.sh ../ispyb_core_config.yml
bash generate_ssx_models.sh ../ispyb_ssx_config.yml
bash generate_em_models.sh ../ispyb_em_config.yml

# Generates marshmallow and flask schemas
python3 generate_core_schemas.py
python3 generate_ssx_schemas.py
python3 generate_em_schemas.py
