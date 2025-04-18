import sqlite3
import uuid
from sql_queries import *
from function import *

# create sql connection object
conn = sqlite3.connect('flight_management_database.db')

#cursor.execute("CREATE DATABASE FLIGHTMGMT; ")


#import database
with open('db_setup.sql', 'r') as sql_file:
    sql_script = sql_file.read()

cursor = conn.cursor()
cursor.executescript(sql_script)
conn.commit()
conn.close()
