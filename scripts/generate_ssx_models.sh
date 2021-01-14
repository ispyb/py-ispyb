URI="$(grep SQLALCHEMY_DATABASE_URI $1)"
URI="$(echo "$URI"  | tr -d '"' | tr -d ' ' | sed -e "s/SQLALCHEMY_DATABASE_URI://")"
flask-sqlacodegen --flask --nobackrefs --noviews --outfile ../ispyb_ssx/models.py $URI

sed -i -e 's/db = SQLAlchemy()/from pyispyb.app.extensions import db/g' ../ispyb_ssx/models.py
