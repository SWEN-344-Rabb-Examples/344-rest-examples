import unittest
from tests.test_utils import *
import json
import platform

class TestExample(unittest.TestCase):
    base_url = 'http://localhost:5000'
#    def setUp(self):
#        rebuild_tables()
#        insert_test_data()

    def test_00_db(self):
        print("Running on:" + platform.system())
        print("\n\n")
        """Initialize DB using API call"""
        post_rest_call(self, f'{TestExample.base_url}/manage/init')
        print("DB Should be reset now")

        version = get_rest_call(self, self.base_url + '/manage/version')
        print("DB Connection test: Version is:" + str(version))
        print(
            """
            A simple program to manage a 'pairings' menu.
            You can also get a nice discount if you get a coupon
            This will exercise: POST, PUT and also using HTTP header for data
            NOTE: No orders are actually added to the DB yet ... just use your imagination!
            """
        )
        print("Press <Enter> to continue")
        input()

    def test_01_url_param(self):
        """API with param in URL path for menu"""
        print(f"The URL used is: {TestExample.base_url}/menu/2")
        result = get_rest_call(self, f'{TestExample.base_url}/menu/2')
        print(f"ID 2 content\n{result}\n")

    def test_02_query_string_param(self):
        """API with param in query string"""
        print(f"The URL used is: {TestExample.base_url}/menu?id=3")
        result = get_rest_call(self, f'{TestExample.base_url}/menu?id=3')
        print(f"ID 3 content: No format\n{result}\n")

        print(f"The URL used is: {TestExample.base_url}/menu")
        result = get_rest_call(self, f'{TestExample.base_url}/menu')
        print(f"Menu: no format\n{result}\n")

        print(f"The URL used is: {TestExample.base_url}/menu?format=headings")
        result = get_rest_call(self, f'{TestExample.base_url}/menu?format=headings')
        print(f"Menu content: headings format\n{result}\n")

    def test_03_menu_taxes(self):
        """With taxes"""
        result = get_rest_call(self, TestExample.base_url+'/menu_taxes')
        print(result)

    def test_04_menu_taxes(self):
        """With taxes -- failure case"""
        #result = get_rest_call(self, TestExample.base_url+'/menu_taxes_direct')
        #print(result)

# py -m unittest -v tests.api.test_example.TestExample.test_05_html_param_post
    def test_05_html_param_post(self):
        """API with POST params in html body"""
        print(f"The URL used is: {TestExample.base_url} ... but there is json data in the body of the POST")

        print("Current contents are:")
        result = get_rest_call(self,TestExample.base_url+'/menu')
        print(f'{result}\n')

        #Variables for the data to be sent
        _food = "goat curry"
        _drink = "lassi"
        _price = "17.50"

        print(f'Want to add {_food} and {_drink}; we will use a POST API')
        data = dict(food=f'{_food}', drink=_drink, price=_price)
        data = dict(food=_food, drink=_drink, price=_price)
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        result = post_rest_call(self,TestExample.base_url+'/menu', jdata, hdr )
        print(f"Result [the PK of  the new row]:{result}")

        result = get_rest_call(self, TestExample.base_url+'/menu')
        print(f"New contents are:\n{result}\n")


# py -m unittest -v tests.api.test_example.TestExample.test_06_html_param_put
    def test_06_html_param_put(self):
        """API with PUT params in html body"""
        print(f"The URL used is: {TestExample.base_url} ... but there is json data in the body of the PUT")

        print("Current contents are:")
        result = get_rest_call(self,TestExample.base_url+'/menu')
        print(f'{result}\n')

        #Variables for the data to be sent
        _food = "tempura"
        _drink = "kirin"
        _price = "19.50"

        print(f'Want to modify the {_food} pairing to {_food} and {_drink}; we will use a PUT API')
        data = dict(food=_food, drink=_drink, price=_price)
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        result = put_rest_call(self,TestExample.base_url+'/menu', jdata, hdr )

        result = get_rest_call(self, TestExample.base_url+'/menu')
        print(f"New contents are:\n{result}\n")


# py -m unittest -v tests.api.test_example.TestExample.test_07_json_and_headers
    def test_07_json_and_headers(self):
        """Get a coupon code and place an order with the coupon code in the header"""
        print(f"The URL used is: {TestExample.base_url}/menu?coupon=request")

        result = get_rest_call(self,TestExample.base_url+'/menu?coupon=request')
        print(f'{result}\n')
        j_result = json.loads(result)
        code  = j_result['coupon_code']
        print("With the code in hand, place an order with the coupon in the header")
        header = {'coupon_code': code, 'content-type': 'application/json'}
        #No body content in this case...
        result = post_rest_call(self,TestExample.base_url+'/menu_orders?menu_id=1',"", header)
        print("Return from order:" + str(result))
