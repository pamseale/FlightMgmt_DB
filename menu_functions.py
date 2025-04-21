from db_functions import *
from input_validation import *

def welcome():
    print("_________________________           ____")
    print("|                         \         \   \__      _____")
    print("|      WELCOME TO          \_________\   \/_______\___\_____________")
    print("|     FLIGHT MANAGER       /         < /_/   .....................  `-.")
    print("|_________________________/            `-----------,----,--------------'")
    print("                                                 _/____/")


def start_menu():
    print_start_menu()
    num_options = 3
    valid_input = request_and_validate(1, num_options)
    return valid_input

def main_menu(option):
    print_sub_menu(option)
    num_options = 4
    valid_input = request_and_validate(1, num_options)
    return valid_input

def staff_amend_menu():
    print_staff_amend_menu()
    num_options = 4
    valid_input = request_and_validate(1, num_options)
    return valid_input

def print_start_menu():
    print("Would you like to view, edit or update:")
    print("1. Flight information")
    print("2. Pilot or staff records")
    print("3. Airport information")

def print_sub_menu(table_name):
    print("Would you like to:")
    print(f"1. View {table_name} data")
    print(f"2. Add {table_name} data")

    print(f"3. Amend {table_name} data")
    if table_name == 'airport':
        print(f"4. Remove an {table_name} record from the database")
    else:
        print(f"4. Remove a {table_name} record from the database")

def execute_start_menu_choice(choice):
    if choice == "1":
        choice = main_menu('flight')
        execute_sub_menu_choice(choice, flight_dict)
        return
    if choice == "2":
        choice = main_menu('staff')
        execute_sub_menu_choice(choice, staff_dict)
        return
    if choice == "3":
        choice = main_menu('airport')
        execute_sub_menu_choice(choice, airport_dict)
        return
    if choice == 'E':
        exit()


def execute_flight_menu_choice(choice):
    table_name = 'flight'
    column_names = ["No.", "Flight no.", "Plane", "Dep", "Arr", "Pilot", "First Officer", "Relief Captain", "Departure (sch.)", "Arrival (sch.)", "Departure (act.)", "Arrival (act)"]
    query_view = 'view_flights'

    if choice == "1":
        display_table(dict, query_view, table_name, column_names)
        return
    if choice == "2":
        add_record(query_view, table_name, column_names)
        return
    if choice == "3":
        amend_record(query_view, table_name, column_names)
        return
    if choice == "4":
        remove_record(query_view, table_name, column_names)
        return
    if choice == 'E':
        exit()

def execute_staff_menu_choice(choice):
    table_name = 'staff'
    column_names = ["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"]
    query_view = 'view_staff'

    if choice == "1":
        display_table(dict, query_view, table_name, column_names)
    if choice == "2":
        add_record(query_view, table_name, column_names)
    if choice == "3":
        amend_record(query_view, table_name, column_names)
    if choice == "4":
        remove_record(query_view, table_name, column_names)
    if choice == 'E':
        exit()

def execute_airport_menu_choice(choice):
    table_name = 'airport'
    column_names = ["No.", "Code", "Name", "City", "Country", "Continent", "Status"]
    query_view = 'view_airports'

    if choice == "1":
        display_table(query_view, table_name, column_names)
    if choice == "2":
        add_record(query_view, table_name, column_names)
    if choice == "3":
        amend_record(query_view, table_name, column_names)
    if choice == "4":
        remove_record(query_view, table_name, column_names)
    if choice == 'E':
        exit()

def execute_sub_menu_choice(choice, dict):
    if choice == "1":
        display_table(dict)
        return
    if choice == "2":
        add_record(dict)
        return
    if choice == "3":
        amend_record(dict)
        return
    if choice == "4":
        remove_record(dict)
        return
    if choice == 'E':
        exit()