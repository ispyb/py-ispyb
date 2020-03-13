import sqlalchemy

class DatabaseProposals(object):

    def __init__(self, engine, connection, metadata):
        self.engine = engine
        self.connection = connection
        self.metadata = metadata

    def get_all_proposals(self):
        proposal_table = sqlalchemy.Table('Proposal', self.metadata, autoload=True, autoload_with=self.engine)
        query = sqlalchemy.select([proposal_table])
        result_proxy = self.connection.execute(query)
        result_set = result_proxy.fetchall()
        return result_set
