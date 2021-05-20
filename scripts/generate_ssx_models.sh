URI="$(grep SQLALCHEMY_DATABASE_URI $1)"
URI="$(echo "$URI"  | tr -d '"' | tr -d ' ' | sed -e "s/SQLALCHEMY_DATABASE_URI://")"
echo "Generating SqlAlchemy models in pyispyb/ssx/models.py ..."
flask-sqlacodegen --flask --nobackrefs --noviews --outfile ../pyispyb/ssx/models.py $URI

sed -i -e 's/db = SQLAlchemy()/from pyispyb.app.extensions import db/g' ../pyispyb/ssx/models.py

echo "Done!"
