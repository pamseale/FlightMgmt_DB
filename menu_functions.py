from dictionaries import flight_dict, staff_dict, airport_dict
from db_functions import display_records, update_record, add_record, remove_record
from get_new_record_functions import *
from input_validation import request_and_validate


def welcome():
    print("_________________________           ____")
    print("|                         \         \   \__      _____")
    print("|      WELCOME TO          \_________\   \/_______\___\_____________")
    print("|     FLIGHT MANAGER       /         < /_/   .....................  `-.")
    print("|_________________________/            `-----------,----,--------------'")
    print("                                                 _/____/")


def start_menu():
    print_start_menu() # flight, pilot or airport
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
    print(f"1. View {table_name} data")
    print(f"2. Add {table_name} data")
    print(f"3. Amend {table_name} data")
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

def amend_menu(dict):
    print_amend_options(dict)
    num_options = len.dict['amend_options']()
    valid_input = request_and_validate(1, num_options)
    return valid_input




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
        print("1. View flight information")
        view_filter = flight_view_menu() # all, by pilot, destination or departure date
        if view_filter == "1": # all
            query = 'view_all_flights'
            display_records(dict, query)
            return
        if view_filter == "2": # by pilot
            query = 'view_pilots'
            display_records(staff_dict, query)
            query = 'view_flights_by_pilot'
            print("\n")
            filter_id = get_filter_id('pilot')
            display_records(dict, query, filter_id)
            return
        if view_filter == "3": # by destination
            query = 'view_airports'
            display_records(airport_dict, query)
            query = 'view_flights_by_dep_aiport'
            print("\n")
            filter_id = get_filter_id('airport')
            display_records(dict, query, filter_id)
            return
        if view_filter == "4": # by departure date
            query = 'view_all_flights'
            display_records(dict, query)
            query = 'view_flights_by_date'
            print("\n")
            filter_id = get_filter_id('date')
            display_records(dict, query, filter_id)
            return
      
    if choice == "3":
        dict = airport_dict
        print("3. View pilot schedules")

    if choice == "4":
        print("4. Assign pilot to flight")

    if (choice == '2' or '5' or '6'):

        if choice == "2":
            dict = flight_dict
            print("2. View, add or amend flight information")  
         #   table_name = 'flight'
            execute_VAAR_menu_choice(dict)
#
        if choice == "5":
            dict = airport_dict
            print("5. View or update airport information")
       #     table_name = 'airport'
            execute_VAAR_menu_choice(dict)


        if choice == "6":
            dict = staff_dict
            print("6. View or update staff information")
           # table_name = 'staff'
            



def execute_VAAR_menu_choice(dict):
                
    #print_VAAR_menu(table_name)
    choice_vaar = VAAR_menu(dict['table_name']) # view add amend remove 


    if choice_vaar == "1": # view

        #if dict['table_name'] == 'flight':
            
        # else:
        query = dict['query_names'][0]
        display_records(dict, query)
        return

    if choice_vaar == "2": # add
        add_record(dict)
        return
    if choice_vaar == "3": # amend
        #amend_choice = amend_menu(dict)
        update_record(dict)
        return
    if choice_vaar == "4": # remove
        remove_record(dict)
        return
    if choice_vaar == 'E':
        exit()

