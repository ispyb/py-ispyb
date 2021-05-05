URI="$(grep SQLALCHEMY_DATABASE_URI $1)"
URI="$(echo "$URI"  | tr -d '"' | tr -d ' ' | sed -e "s/SQLALCHEMY_DATABASE_URI://")"
echo "Generating SqlAlchemy models in pyispyb/em/models.py ..."

flask-sqlacodegen --flask --nobackrefs --noviews --outfile ../pyispyb/em/models.py $URI


sed -i -e 's/db = SQLAlchemy()/from pyispyb.app.extensions import db/g' ../pyispyb/em/models.py
sed -i -e 's/class AutoProcStatu(db.Model)/class AutoProcStatus(db.Model)/g' ../pyispyb/em/models.py
sed -i -e 's/AutoProcStatu.autoProcIntegrationId/AutoProcStatus.autoProcIntegrationId/g' ../pyispyb/em/models.py

echo "Done!"
