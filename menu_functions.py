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

def flight_view_menu():
    print_flight_view_menu()
    num_options = 4
    valid_input = request_and_validate(1, num_options)
    return valid_input

def print_start_menu():
    print("\nWould you like to view, edit or update:")
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

def print_flight_view_menu():
    print("Would you like to:")
    print(f"1. View all flight data")
    print(f"2. View data by pilot")
    print(f"3. View data by destination")
    print(f"4. View data by departure date")

def execute_start_menu_choice(choice):
    if choice == "1":
        dict = flight_dict
    if choice == "2":
        dict = staff_dict
    if choice == "3":
        dict = airport_dict
    if choice == 'E':
        exit()
    choice = main_menu(dict['table_name'])
    execute_sub_menu_choice(choice, dict)


def execute_sub_menu_choice(choice, dict):
    if choice == "1":
        choice = flight_view_menu()
        if choice == "1":
            query = 'view_flights'
            display_table(dict, query)
            return
        if choice == "2":
            query = ""
            display_table(dict, query)
            return
        if choice == "3":
            query = ""
            display_table(dict, query)
            return
        if choice == "4":
            query = ""
            display_table(dict, query)
            return
        return
    if choice == "2":
        add_record(dict)
        return
    if choice == "3":
        update_record(dict)
        return
    if choice == "4":
        remove_record(dict)
        return
    if choice == 'E':
        exit()


def get_new_flight_record():
    id = input("Enter the flight ID (max 6 characters): ")
    plane = input("Enter the plane ID:  ")
    dep_airport = input("Enter the departure airport code (max 3 characters):  ")
    arr_airport = input("Enter the ariival airport code (max 3 characters):  ")
    pilot = input("Enter the pilot's staff ID:  ")
    first_officer = input("Enter the first officer's staff ID, if applicable:  ")
    relief_captain = input("Enter the relief captain's staff ID, if applicable:  ")
    date_dep_sch = input("Enter the scheduled departure date and time in the following format YYYY-MM-DD HH:MM:SS:  ")
    date_arr_sch = input("Enter the scheduled arrival date and time in the following format YYYY-MM-DD HH:MM:SS:  ")
    date_dep_act = input("Enter the actual departure date and time in the following format YYYY-MM-DD HH:MM:SS:  ")
    date_arr_act = input("Enter the actual departure date and time in the following format YYYY-MM-DD HH:MM:SS:  ")
    return id, plane, dep_airport, arr_airport, pilot, first_officer, relief_captain, date_dep_sch, date_arr_sch, date_dep_act, date_arr_act

def get_new_staff_record():
    id = input("Enter the staff ID in the following format: STID0000  ")
    surname = input("Enter the staff member's surname:  ")
    forename = input("Enter the staff member's forename:  ")
    role = input("Enter the staff member's role:  ")
    license = input("Enter the license number, if applicable:  ")
    license_status = input("Enter the license status, if applicable:  ")
    return id, surname, forename, role, license, license_status

def get_new_airport_record():
    id = input("Enter the airport ID in the following format: AAA  ")
    name = input("Enter the airport name:  ")
    city = input("Enter the airport's nearest city:  ")
    country = input("Enter the country in which the airport is located:  ")
    continent = input("Enter the continent:  ")
    status = input("Enter the airport's current status (open, closed, warning in place):  ")
    return id, name, city, country, continent, status