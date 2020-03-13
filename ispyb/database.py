import os
import sys

import configparser
import sqlalchemy
from .database_proposals import DatabaseProposals


config = configparser.ConfigParser()
config_filename = os.path.join(os.path.dirname(__file__), "../config.cfg")
config.read(config_filename)

db_engine = sqlalchemy.create_engine(
    "%s://%s:%s@%s/%s"
    % (
        config["db_connection"]["engine"],
        config["db_connection"]["usr"],
        config["db_connection"]["pwd"],
        config["db_connection"]["host"],
        config["db_connection"]["db_name"],
    )
)
db_connection = db_engine.connect()
db_metadata = sqlalchemy.MetaData()

db_proposals = DatabaseProposals(db_engine, db_connection, db_metadata, config)
