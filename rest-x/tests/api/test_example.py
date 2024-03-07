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
        post_rest_call(self, f'{TestExample.base_url}/init')
        print("DB Should be reset now")
        result = get_rest_call(self, TestExample.base_url)
        print(result)
        print(
            """
            Items of note:
            1. DB is initialized from server side.  API is provided to make the request from the client
            2. Can also auto-load from the server side (see server.py)
            3. Different types of methods to send params
                - In URL (test_01)
                - As query string (test_02)
                - In HTML body (test_03).  This includes format params in body as json
            4. Some extra code in exec_commit to get the PK of the INSERTed row
            5. Some extra code in api for GET to format return data as json
            """
        )
        print("Press <Enter> to continue")
        input()

    def test_01_url_param(self):
        """API with param in URL path"""
        print(f"The URL used is: {TestExample.base_url}/2")
        result = get_rest_call(self, f'{TestExample.base_url}/2')
        print(f"ID 2 content\n{result}\n")

    def test_02_query_string_param(self):
        """API with param in query string"""
        print(f"The URL used is: {TestExample.base_url}/?id=3")
        result = get_rest_call(self, f'{TestExample.base_url}/?id=3')
        print(f"ID 3 content\n{result}\n")


    def test_03_html_param(self):
        """API with params in html body"""
        print(f"The URL used is: {TestExample.base_url} ... but there is json data in the body")
        print("Current contents are:")
        result = get_rest_call(self,TestExample.base_url)
        print(f'{result}\n')
        _food = "goat curry"
        _drink = "lassi"
        _price = "17.50"
        data = dict(food=f'{_food}', drink=_drink, price=_price)
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        result = post_rest_call(self,TestExample.base_url, jdata, hdr )
        print(f"Result [the PK of  the new row]:{result}")
        result = get_rest_call(self, TestExample.base_url)
        print(f"New contents are:\n{result}\n")

    def test_04_menu_taxes(self):
        """With taxes"""
        result = get_rest_call(self, TestExample.base_url+'/menu_taxes')
        print(result)

    def test_05_books(self):
        post_rest_call(self, f'{TestExample.base_url}/init')
        print("DB Should be reset now")
        print("********All books***********")
        result = get_rest_call(self, TestExample.base_url+'/books')
        self.print_list(result)
        result = get_rest_call(self, TestExample.base_url+'/books?author=Asimov')
        print("********Search 'asimov'***********")
        self.print_list(result)
        result = get_rest_call(self, TestExample.base_url+'/books?author=asimov&title=r')
        print("********Search 'asimov, r'***********")
        self.print_list(result)
        result = get_rest_call(self, TestExample.base_url+'/books?author=asimov&title=r&summary=m')
        print("********Search 'a, r, m'***********")
        self.print_list(result)

    def print_list(self,list):
        for row in list:
            for field in row:
                print(field,end = ',')
            print("")
        print("")
        

    def test_06_bad_delete(self):
        d1 = "data1"
        d2 = "data2"
        data = dict(d1=d1, d2=d2)
        jdata = json.dumps(data)
        hdr = {'content-type': 'application/json'}
        result = delete_rest_call(self,TestExample.base_url+'/books', jdata, hdr )


        
