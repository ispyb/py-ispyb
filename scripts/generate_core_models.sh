URI="$(grep SQLALCHEMY_DATABASE_URI $1)"
URI="$(echo "$URI"  | tr -d '"' | tr -d ' ' | sed -e "s/SQLALCHEMY_DATABASE_URI://")"
echo "Generating SqlAlchemy models in pyispyb/core/models.py ..."

flask-sqlacodegen --flask --nobackrefs  --outfile ../pyispyb/core/models.py $URI


sed -i -e 's/db = SQLAlchemy()/from pyispyb.app.extensions import db/g' ../pyispyb/core/models.py
sed -i -e 's/class AutoProcStatu(db.Model)/class AutoProcStatus(db.Model)/g' ../pyispyb/core/models.py
sed -i -e 's/AutoProcStatu.autoProcIntegrationId/AutoProcStatus.autoProcIntegrationId/g' ../pyispyb/core/models.py

echo "Done!"
