import sqlalchemy
from .database_proposals import DatabaseProposals

db_engine = sqlalchemy.create_engine('mysql://test_user:test_pwd@localhost/test_db')
db_connection = db_engine.connect()
db_metadata = sqlalchemy.MetaData()

db_proposals = DatabaseProposals(db_engine, db_connection, db_metadata)
