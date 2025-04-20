import sqlite3
from function import *
from menu_functions import *
from db_functions import *

import_db()
welcome()
run = True
while(run):
   menu_choice = start_menu()
   execute_start_menu_choice(menu_choice)
   print("\nquery completed\n")
exit()
