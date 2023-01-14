import psycopg2


class DBPool:
    def __init__( self, host, port, dbName, user, password):
        self.pool = psycopg2.connect(
            database=dbName, host=host, port=port, user=user, password=password
        )

    def getConnection(self):
        return self.pool

    def closeConnection(self, connection):
        self.pool.putconn(connection, close=True)

