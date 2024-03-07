from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db import example
from db.swen344_db_utils import *
import json

from db.example import rebuild_tables

#Code all in one place for demo purposes ...

class Books(Resource):
    def get(self):
        count = len(request.args)
        print(f"/books received {count} parameter(s)")
        if (count == 0):
            sql = 'select * from books'
            return exec_get_all(sql)
        else:
            sql = "SELECT * from BOOKS WHERE "
            params = []
            for i, key in enumerate(request.args.keys()):
                value = request.args[key]
                sql = f"{sql} {key} ILIKE %s"
                params.append(f"%{value}%")
                if (i < count-1):
                    sql = sql + " AND "
            print(sql)
            print(params)
            result = exec_get_all(sql, params)
            return result
        
    def delete(self):
        print("Delete API call")
        print(request.data)
            

