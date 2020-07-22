USER="mxuser"
PWD="mxpass"
HOST="localhost"
DB_NAME="ispyb_ssx"

flask-sqlacodegen --flask --outfile ../ispyb_ssx/models.py mysql://$USER:$PWD@$HOST/$DB_NAME

sed -i -e 's/db = SQLAlchemy()/from app.extensions import db/g' ../ispyb_ssx/models.py
