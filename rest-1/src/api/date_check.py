from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db.swen344_db_utils import *





class DateCheck(Resource):
    def get(self):
        sql = "select * from dates_x"
        sql = "select id, name, to_char(the_date, 'MM/DD/YYYY') from dates_x"
        #sql = 'select id, name, cast(the_date as text) from dates_x'
        result = exec_get_all(sql)
        return result

