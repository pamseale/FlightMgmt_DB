import sqlite3
import uuid
from function import *

# create sql connection object
conn = sqlite3.connect('flight_management_database.db')

#import database
def import_db(conn):
   with open('db_setup.sql', 'r') as sql_file:
      sql_script = sql_file.read()
   cursor = conn.cursor()
   cursor.executescript(sql_script)
   conn.commit()
   conn.close()

import_db(conn)

run = True
# start menu
welcome()

while(run):
   menu_choice = start_menu()
   execute_start_menu_choice(menu_choice)
   print("\nquery completed\n")

exit()
