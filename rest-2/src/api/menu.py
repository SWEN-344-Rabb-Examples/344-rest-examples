from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db import example
from db.swen344_db_utils import *
import json

from db.example import rebuild_tables


# Attempts to do double duty by checking for the query string
#If no query string, assume everything is returned, else process the parameter
# NOTE: Code is left 'in-line' for simplicity of demos ... some of this normally would be separated into 'helper' functions :)
class Menu(Resource):
    def get(self):
        """Checks for query string, if none, returns all"""
        id = request.args.get('id')
        format = request.args.get('format', default="none")
        coupon = request.args.get('coupon', default='empty')
        sql = ""
        if (coupon == 'request'):
            coup = {'coupon_code': '34895uweofkhf'}
            output = json.dumps(coup)
            return output
            
        if (id == None):
            print("No query string, returning all rows, format = "+ format)
            if (format == 'none'):
                sql = """SELECT food.name, drink.name, price FROM pairings_menu
                INNER JOIN food on food.id=food_id
                INNER JOIN drink on drink.id=drink_id"""
            if (format == 'headings'):
                sql = """
                select row_to_json(menu) from
                        (select food.name as food, drink.name as drink, price FROM pairings_menu 
                            INNER JOIN food on food.id=food_id
                            INNER JOIN drink on drink.id=drink_id) menu
                    """
            return exec_get_all(sql)
        else:
            print(f"Query string id is:{id}")
            #sql = "SELECT * FROM MENU_TABLE WHERE id=%s"
            sql = "SELECT row_to_json(pairings_menu.*) FROM pairings_menu WHERE id=%s"
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
        #First add the food item
        sql = """INSERT INTO food (name)
                    VALUES (%s) RETURNING id"""
        result = exec_commit_with_id(sql, (food,))
        food_id = result[0][0]

        #Now add the drink item
        sql = """INSERT INTO drink (name)
                    VALUES (%s) RETURNING id"""
        result = exec_commit_with_id(sql, (drink,))
        drink_id = result[0][0]
        sql = """INSERT INTO pairings_menu (food_id, drink_id, price)
                    VALUES (%s, %s, %s) RETURNING id"""
        result = exec_commit_with_id(sql, (food_id, drink_id, price))
        return result

    def put(self):
        """Extracts data from body and adds a row"""
        parser = reqparse.RequestParser()
        parser.add_argument('food', type=str)
        parser.add_argument('drink', type=str)
        parser.add_argument('price', type=str)
        args = parser.parse_args()
        food = args['food']
        drink = args['drink']
        price = args['price']
        #First find the food row that relates to the food item
        sql = """SELECT pairings_menu.id  FROM pairings_menu 
            INNER JOIN food on food.id=food_id
            INNER JOIN drink on drink.id=drink_id 
            WHERE food.name=%s 
            """
        result = exec_get_one(sql, (food,))
        menu_id = result[0]
        #Now find the drink row that relates to the drink item -- has to be in the table
        sql = """SELECT id  FROM drink 
            WHERE name=%s
            """
        result = exec_get_one(sql, (drink,))
        drink_id = result[0]

        #Now find the food row that relates to the food item
        sql = """SELECT id  FROM food 
            WHERE name=%s
            """
        result = exec_get_one(sql, (food,))
        food_id = result[0]

        #Now change the data the drink item
        sql = """UPDATE pairings_menu SET drink_id=%s, price=%s
                   WHERE id=%s RETURNING id"""
        result = exec_commit_with_id(sql, (drink_id,price, menu_id))
        print("PUT: returning " + str(result))
        return result

# MenuItem ends up being a new class, since the URL signature  is different
# and add_resource requires an unambiguous definition
# This is, therefore and ALTERNATE was to get a menu item by ID
class MenuItem(Resource):
    def get(self, id):
        print(f"Getting menu item:{id}")
        return exec_get_one("""SELECT pairings_menu.id, food.name, drink.name, price FROM pairings_menu 
        INNER JOIN food on food.id=food_id
        INNER JOIN drink on drink.id=drink_id
        WHERE pairings_menu.id=%s""", (id,))

class MenuItemTaxes(Resource):
    def get(self):
        print("Getting data with taxes")
        #This one will fail -- do you know why?
        #result = exec_get_all("SELECT * FROM menu_table")
        #This will work!
        result = exec_get_all("""SELECT pairings_menu.id, food.name, drink.name, price, CAST (tax AS float) 
                FROM pairings_menu
                INNER JOIN food on food.id=food_id
                INNER JOIN drink on drink.id=drink_id
                """)

        return result

class MenuItemTaxesDirect(Resource):
    def get(self):
        print("Getting data with taxes")
        #This one will fail -- do you know why?
        result = exec_get_all("""SELECT pairings_menu.id, food.name, drink.name, price, tax  
                FROM pairings_menu
                INNER JOIN food on food.id=food_id
                INNER JOIN drink on drink.id=drink_id
                """)

        return result
        