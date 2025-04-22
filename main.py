from db_import import import_db
from menu_functions import welcome, start_menu, execute_menu_choice

def main():
   import_db()
   welcome()
   run = True
   while(run):
      choice = start_menu()
      execute_menu_choice(choice)
      print("\nquery completed\n")
   exit()

if __name__ == "__main__":
    main()

