# Generates sqlalchemy db models
bash generate_core_models.sh ../pyispyb.core_config.yml
bash generate_ssx_models.sh ../ispyb_ssx_config.yml

# Generates marshmallow and flask schemas
python3 generate_core_schemas.py
python3 generate_ssx_schemas.py
