import sqlite3
import uuid
conn = sqlite3.connect('flight_management_database.db')

# Generate a GUID
guid = str(uuid.uuid4())

def check_in_range(value, low, high):
    result = False
    if low <= value <= high:
        result = True
    return result

def request_and_validate(low, high):
    while True:
        choice = input("Select a menu choice or 'E' to exit.")
        if choice == "E":
            exit()
        else:
            try:
                int(choice)
            except ValueError:
                print("invalid choice, please enter an integer")
            else:
                if low <= int(choice) <= high:
                    break
                else:
                    print("selection out of range, please choose a number between", low, " and", high)
    return choice


def print_start_menu():
    print("Would you like to view, edit or update:")
    print("1. Flight information")
    print("2. Pilot or staff records")
    print("3. Airport information")

def print_flight_menu():
    print("Would you like to:")
    print("1. View flight data")
    print("2. Amend flight data")
    print("3. Remove a flight from the database")

def print_staff_menu():
    print("Would you like to:")
    print("1. View pilot or staff data")
    print("2. Amend pilot or staff data")
    print("3. Remove a staff record from the database")

def print_airport_menu():
    print("Would you like to:")
    print("1. View airport data")
    print("2. Amend airport data")
    print("3. Remove an airport from the database")

def display_flights():
    display_all_from_table(conn, 'flight_view')
    execute(conn, "SELECT * FROM flight_view;")

def amend_flights():
    print("amend")
def remove_flights():
    print("remove")

def start_menu():
    print_start_menu()
    num_options = 3
    valid_input = request_and_validate(1, num_options)
    return valid_input

def flight_menu():
    print_flight_menu()
    num_options = 3
    valid_input = request_and_validate(1, num_options)
    return valid_input

def staff_menu():
    print_flight_menu()
    num_options = 3
    valid_input = request_and_validate(1, num_options)
    return valid_input

def airport_menu():
    print_flight_menu()
    num_options = 3
    valid_input = request_and_validate(1, num_options)
    return valid_input

def execute_start_menu_choice(choice):
    if choice == "1":
        choice = flight_menu()
        execute_flight_menu_choice(choice)
    if choice == "2":
        choice = staff_menu()
        execute_staff_menu_choice(choice)
    if choice == "3":
        choice = airport_menu()
        execute_airport_menu_choice(choice)
    if choice == 'E':
        exit()

def execute_flight_menu_choice(choice):
    if choice == "1": #view
        display_flights()
        #choice = view_flight_data_menu()
        #execute_view_flight_data_menu_choice(choice)
    if choice == "2": # amend
        amend_flights()
        #choice = view_pilot_data_menu()
        #execute_view_pilot_data_menu_choice(choice)
    if choice == "3": # remove
        remove_flight()
        #choice = view_airport_data_menu()
        #execute_view_airport_data_menu_choice(choice)
    if choice == 'E':
        exit()




def welcome():
    print("_________________________           ____")
    print("|                         \         \   \__      _____")
    print("|      WELCOME TO          \_________\   \/_______\___\_____________")
    print("|     FLIGHT MANAGER       /         < /_/   .....................  `-.")
    print("|_________________________/            `-----------,----,--------------'")
    print("                                                 _/____/")


def user_validation():
    pin = 1234
    while True:
        response = input("Please enter the PIN or 'E' to exit program.")
        if response == 1234:
            print("\nPIN accepted.\n") #menu_1
            break
        elif response == "E":
            print(
                "\nExiting program.\n")
        else:
            print("\nPIN not accepted, please try again.\n")


def drop_all_tables(conn):
    for table in table_list:
        drop_table(conn, table)

def drop_table(conn, table_name):
    cursor = conn.cursor()
    query = f"DROP TABLE IF EXISTS {table_name}"
    try:
      cursor.execute(query)
      conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
#    finally:
    #    close(conn)

def create_table(conn, table_name):
    cursor = conn.cursor()
    query = f"CREATE TABLE IF NOT EXISTS {table_name}"
    try:
      cursor.execute(query)
      conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
#    finally:
    #    close(conn)

def display_all_from_table(conn, table_name):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    try:
      cursor.execute(query)
      rows = cursor.fetchall()
      print(f"\nData from table '{table_name}':")
      for row in rows:
            print(row)
      conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
#    finally:
    #    close(conn)

def execute(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)

def close(conn):
    try:
       conn.close()
    except sqlite3.Error as e:
       print("An error occurred:", e)