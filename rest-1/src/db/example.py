import os
from .swen344_db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/test_data.sql')

def list_examples():
    """Basic data load on server
    """
    return exec_get_all('SELECT * FROM menu_table')
