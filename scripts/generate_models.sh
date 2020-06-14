flask-sqlacodegen --flask --outfile ../models.py mysql://mxuser:mxpass@localhost/pydb_test

sed -i -e 's/db = SQLAlchemy()/from app.extensions import db/g' ../models.py
