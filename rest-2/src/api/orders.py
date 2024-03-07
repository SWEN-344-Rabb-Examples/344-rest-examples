from email.policy import default
from flask_restful import Resource, reqparse, request  #NOTE: Import from flask_restful, not python
from db import example
from db.swen344_db_utils import *
import json



# Attempts to do double duty by checking for the query string
#If no query string, assume everything is returned, else process the parameter
# NOTE: Code is left 'in-line' for simplicity of demos ... some of this normally would be separated into 'helper' functions :)
class Orders(Resource):
    def get(self):
        """Checks for query string, if none, returns all"""
        id = request.args.get('id')
        format = request.args.get('format', default="none")
        sql = ""
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
        """Extracts data from query string and header and adds a row"""
        menu_id = request.args.get('menu_id')
        #Now get the coupon, if any
        coupon = request.headers.get('coupon_code', default="")
        print("Server coupon:" + str(coupon))
        sql = "SELECT price from pairings_menu WHERE id=%s"
        result = exec_get_one(sql, (menu_id,))
        price = result[0]
        priceFloat = float(price)
        basePrice = priceFloat
        if (len(coupon) > 0):
            priceFloat = priceFloat*0.9 # 10% discount
        return_data = {'discounted_price': priceFloat, 'original_price:': basePrice}
        return return_data

