URI="$(grep SQLALCHEMY_DATABASE_URI $1)"
URI="$(echo "$URI"  | tr -d '"' | tr -d ' ' | sed -e "s/SQLALCHEMY_DATABASE_URI://")"
echo "111"
echo $URI
flask-sqlacodegen --flask --nobackrefs --noviews --outfile ../ispyb_core/models.py $URI
echo "222"
sed -i -e 's/db = SQLAlchemy()/from app.extensions import db/g' ../ispyb_core/models.py
sed -i -e 's/class AutoProcStatu(db.Model)/class AutoProcStatus(db.Model)/g' ../ispyb_core/models.py
sed -i -e 's/AutoProcStatu.autoProcIntegrationId/AutoProcStatus.autoProcIntegrationId/g' ../ispyb_core/models.py
