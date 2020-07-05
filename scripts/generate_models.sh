flask-sqlacodegen --flask --outfile ../ispyb_core/models.py mysql://mxuser:mxpass@localhost/pydb_test

sed -i -e 's/db = SQLAlchemy()/from app.extensions import db/g' ../ispyb_core/models.py
