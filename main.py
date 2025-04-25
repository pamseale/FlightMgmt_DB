import sqlite3
from file_handler import execute_sql_file
from menu_functions import welcome, start_menu, execute_menu_choice
from security import login

db_filename = 'flight_management_database.db'
db_setup_filename = 'db_setup.sql'

def main():

   print("--------------------------------------------------")
   print("----------------------[1234!]---------------------")
   print("--------------------------------------------------")

   verified_user = False
   while(verified_user == False):
      verified_user = login()

   execute_sql_file(db_setup_filename, db_filename)
   welcome()
   conn = sqlite3.connect(db_filename)

   run = True
   while(run):
      choice = start_menu()
      execute_menu_choice(choice, conn)
      print("\nquery completed\n")
   print("exiting program")
   conn.close()
   exit()

if __name__ == "__main__":
    main()
