from dictionaries import flight_dict, staff_dict, airport_dict
from db_functions import display_records, update_record, add_record, remove_record
from file_handler import load_query_from_file
from get_new_values import *
from input_validation import request_and_validate


def welcome():
    print("_________________________           ____")
    print("|                         \         \   \__      _____")
    print("|      WELCOME TO          \_________\   \/_______\___\_____________")
    print("|     FLIGHT MANAGER       /         < /_/   .....................  `-.")
    print("|_________________________/            `-----------,----,--------------'")
    print("                                                 _/____/")


def start_menu():
    print_start_menu()
    num_options = 6
    valid_input = request_and_validate(1, num_options)
    return valid_input


def print_start_menu():
    print("\nWould you like to: ")
    print("1. View flight information")
    print("2. Add, remove or update flight information")
    print("3. View pilot schedules")
    print("4. Assign pilot to flight")
    print("5. View or change airport information")
    print("6. View or change staff information")


def VAAR_menu(option):
    print_VAAR_menu(option) # view add amend or remove
    num_options = 4
    valid_input = request_and_validate(1, num_options)
    return valid_input


def print_VAAR_menu(table_name):
    print("Would you like to:")
    print(f"1. View {table_name} information")
    print(f"2. Add a new {table_name} record")
    print(f"3. Update {table_name} information")
    if table_name == 'airport':
        print(f"4. Remove an {table_name} record from the database")
    else:
        print(f"4. Remove a {table_name} record from the database")


def flight_view_menu():
    print_flight_view_menu() # flights by all, pilot, dest, date
    num_options = 4
    valid_input = request_and_validate(1, num_options)
    return valid_input


def print_flight_view_menu():
    print("Would you like to:")
    print(f"1. View all flight data")
    print(f"2. View flights by pilot")
    print(f"3. View flights by destination")
    print(f"4. View flights by departure date")


def print_amend_options(dict):
    print("\nYou have permission to update the following records:\n")
    for opt in dict['amend_options']:
        print (opt)
    print("\n")


def get_filter_id(filter):
    if filter == 'date':
        filter_id = input("\nEnter the " + filter + " you would like to filter by in the format YYYY-MM-DD : ")
    else:
        filter_id = input("\nEnter the ID of the " + filter + " you would like to filter by:  ")
    return filter_id


def execute_menu_choice(choice):

    if choice == 'E':
        exit()

    if choice == "1":
        dict = flight_dict
        view_filter = flight_view_menu() # all, by pilot, destination or departure date

        if view_filter == "1": # all
            query = dict['query_names'][0]
            display_records(dict, query)
            return
        if view_filter == "2": # by pilot
            # display all pilots and get user to select
            dict = staff_dict
            query = dict['query_names'][1]
            display_records(dict, query)
            filter_id = get_filter_id('pilot')
            # display flights by selected pilot
            dict = flight_dict
            query = load_query_from_file('queries.sql', 'query_flights_by_pilot')
            print(query)
            print("filter ID = " + filter_id)
            display_records(dict, query, filter_id)
            return
        if view_filter == "3": # by destination
            dict = airport_dict
            query = dict['query_names'][0]
            display_records(dict, query)
            filter_id = get_filter_id('airport')
            dict = flight_dict
            query = load_query_from_file('queries.sql', 'query_flights_by_dep_airport')
            display_records(dict, query, filter_id)
            return
        if view_filter == "4": # by departure date
            dict = flight_dict
            filter_id = get_filter_id('date')
            query = load_query_from_file('queries.sql', 'query_flights_by_date')
            display_records(dict, query, filter_id)
            return
        
    if choice == "3":
        dict = airport_dict
        print("Which pilot's schedule would you like to view?")
        query = 'view_pilots'
        display_records(staff_dict, query)
        query = 'view_flights_by_pilot'
        print("\n")
        filter_id = get_filter_id('pilot')
        display_records(dict, query, filter_id)
        return

    if choice == "4":
        print("4. Assign pilot to flight")

    if (choice == '2' or '5' or '6'):
        if choice == "2":
            dict = flight_dict
        if choice == "5":
            dict = airport_dict
        if choice == "6":
            dict = staff_dict
        execute_VAAR_menu_choice(dict)


def execute_VAAR_menu_choice(dict):
                
    choice_vaar = VAAR_menu(dict['table_name']) # view add amend remove 

    if choice_vaar == "1": # view
        query = dict['query_names'][0]
        display_records(dict, query)
        return

    if choice_vaar == "2": # add
        add_record(dict)
        return
    
    if choice_vaar == "3": # amend
        update_record(dict)
        return
    
    if choice_vaar == "4": # remove
        remove_record(dict)
        return
    
    if choice_vaar == 'E':
        exit()

