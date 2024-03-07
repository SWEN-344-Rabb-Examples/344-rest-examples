from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db import example
from db.swen344_db_utils import *
import json



# Bsic handler for Food items
class Food(Resource):
    def get(self):
            sql = "SELECT * from food"
            return exec_get_all(sql)



# Bsic handler for drink items
class Drink(Resource):
    def get(self):
            sql = "SELECT * from drink"
            return exec_get_all(sql)




        