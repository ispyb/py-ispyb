USER="pydbusr"
PWD="pydbpwd"
HOST="ispyb.embl-hamburg.de"
DB_NAME="pydb"

flask-sqlacodegen --flask --nobackrefs --outfile ../ispyb_core/models.py mysql://$USER:$PWD@$HOST/$DB_NAME

sed -i -e 's/db = SQLAlchemy()/from app.extensions import db/g' ../ispyb_core/models.py
