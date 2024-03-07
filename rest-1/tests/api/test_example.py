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

# py -m unittest -v tests.api.test_example.TestExample.test_01_url_param
    def test_01_url_param(self):
        """API with param in URL path for menu"""
        print(f"The URL used is: {TestExample.base_url}/menu/2")
        result = get_rest_call(self, f'{TestExample.base_url}/menu/2')
        print(f"ID 2 content\n{result}\n")

# py -m unittest -v tests.api.test_example.TestExample.test_02_query_string_param
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


# py -m unittest -v tests.api.test_example.TestExample.test_03_menu_taxes
    def test_03_menu_taxes(self):
        """With taxes"""
        result = get_rest_call(self, TestExample.base_url+'/menu_taxes')
        print(result)

# py -m unittest -v tests.api.test_example.TestExample.test_04_menu_taxes
    def test_04_menu_taxes(self):
        """With taxes -- failure case"""
        #result = get_rest_call(self, TestExample.base_url+'/menu_taxes_direct')
        #print(result)

# py -m unittest -v tests.api.test_example.TestExample.test_05_dates
    def test_05_dates(self):
        result = get_rest_call(self,'http://localhost:5000/dates')
        print(result)
