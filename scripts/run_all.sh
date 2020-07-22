# Generates sqlalchemy db models
bash generate_core_models.sh
bash generate_ssx_models.sh

# Generates marshmallow and flask schemas
python3 generate_core_schemas.py
python3 generate_ssx_schemas.py
