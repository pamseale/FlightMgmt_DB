from file_handler import execute_sql_file
from menu_functions import welcome, start_menu, execute_menu_choice

db_filename = 'flight_management_database.db'
db_setup_filename = 'db_setup.sql'

def main():
   execute_sql_file(db_setup_filename, db_filename)
   welcome()
   run = True
   while(run):
      choice = start_menu()
      execute_menu_choice(choice)
      print("\nquery completed\n")
   exit()

if __name__ == "__main__":
    main()
