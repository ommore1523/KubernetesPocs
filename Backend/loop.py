from database import DBPool
import pandas.io.sql as sqlio

for i in range(1000):
    connection = DBPool('192.168.49.2',30008,'postgres','postgres', 'postgres')
    conn = connection.getConnection()
    query = "SELECT * FROM pg_catalog.pg_tables;"
    data = sqlio.read_sql_query(query, conn)