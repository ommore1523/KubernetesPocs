from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify


app = Flask(__name__)
api = Api(app)

CORS(app)


# ---------- DATABASE ---- CONNECTION ---

from database import DBPool
connection = DBPool('192.168.49.2',30008,'postgres','postgres', 'postgres')

import pandas.io.sql as sqlio

class DB:
    @staticmethod
    def read_data(query):
        try:
            conn = connection.getConnection()
            data = sqlio.read_sql_query(query, conn)
            # connection.closeConnection(conn)
            return data
        except Exception as err:
            raise err




@app.route("/")
def hello():
   
    return jsonify({"text":"hello"})

class Employees(Resource):
    def get(self):
        id_2 = DB.read_data("select * from sample_json where id=2")['data'].loc[0]
        return jsonify(id_2) 

class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        id_3 = DB.read_data("select * from sample_json where id=3")['data'].loc[0]
        return jsonify(id_3)  

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
    app.run(port=5002, host="0.0.0.0")