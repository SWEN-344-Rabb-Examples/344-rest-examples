from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db import example
from db.swen344_db_utils import *
import json

from db.example import rebuild_tables

class Init(Resource):
    def post(self):
        rebuild_tables()

class Menu(Resource):
    def get(self):
        """Checks for query string, if none, returns all"""
        id = request.args.get('id')
        parser = reqparse.RequestParser()
        parser.add_argument('id', location='args')
        parser_args = parser.parse_args() 
        print('Parser Args with location=args; id='+parser_args['id'])

        #Commented out below, because this will FAIL (there is no param data in the body!)
        """
        parser2 = reqparse.RequestParser()
        parser2.add_argument('id')
        breakpoint()
        parser_args2 = parser2.parse_args() 
        print('Parser Args withOUT location=args; id='+parser_args2['id'])
        """

        if (id == None):
            print("No query string, returning all rows")
            sql = "SELECT row_to_json(menu_table.*) FROM menu_table"
            sql = """SELECT row_to_json 
            ( (SELECT ColumnName FROM (SELECT food,drink,price) AS ColumnName (food, drink, price))  ) FROM menu_table
            """
            return exec_get_all(sql)
        else:
            print(f"Query string id is:{id}")
            #sql = "SELECT * FROM MENU_TABLE WHERE id=%s"
            sql = "SELECT row_to_json(menu_table.*) FROM menu_table WHERE id=%s"
            result =  exec_get_all(sql, (id,))
            #breakpoint()
            return result

    def post(self):
        """Extracts data from body and adds a row"""
        parser = reqparse.RequestParser()
        parser.add_argument('food', type=str)
        parser.add_argument('drink', type=str)
        parser.add_argument('price', type=str)
        args = parser.parse_args()
        food = args['food']
        drink = args['drink']
        price = args['price']
        sql = """INSERT INTO menu_table (food, drink,price)
                    VALUES (%s, %s, %s) RETURNING id"""
        result = exec_commit(sql, (food, drink, price))
        return result

class MenuItem(Resource):
    def get(self, id):
        print(f"Getting menu item:{id}")
        return exec_get_one("SELECT id, food, drink, price FROM menu_table WHERE id=%s", (id,))

class MenuItemTaxes(Resource):
    def get(self):
        print("Getting data with taxes")
        #This one will fail -- do you know why?
        #result = exec_get_all("SELECT * FROM menu_table")
        #This will work!
        result = exec_get_all("SELECT id, food, drink, price, CAST (tax AS float) FROM menu_table")

        return result