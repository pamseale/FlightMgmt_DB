from dictionaries import flight_dict, pilot_dict, airport_dict
from db_functions import display_records, add_record, update_record, remove_record, get_record_index, get_col_to_update, new_value
from file_handler import load_query_from_file
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
    num_options = 8
    valid_input = request_and_validate(1, num_options)
    return valid_input


def print_start_menu():
    print("\nWould you like to: ")
    print("1. View flight information")
    print("2. Add, remove or update flight information")
    print("3. View pilot schedules")
    print("4. Assign pilot to flight")
    print("5. View or change airport information")
    print("6. View or change pilot information")
    print("7. View flights to destinations")
    print("8. View flights to destinations with more than one flight")




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
    print_flight_view_menu() # flights by all, pilot, dest, or date
    num_options = 4
    valid_input = request_and_validate(1, num_options)
    return valid_input


def print_flight_view_menu():
    print("Would you like to:")
    print(f"1. View all flight data")
    print(f"2. View flights by pilot")
    print(f"3. View flights by destination")
    print(f"4. View flights by departure date")


def get_filter_id(filter):
    if filter == 'date':
        filter_id = input("\nEnter the " + filter + " you would like to filter by in the format YYYY-MM-DD : ")
    else:
        filter_id = input("\nEnter the ID of the " + filter + " you would like to filter by:  ")
    return filter_id

def get_record_id(record):
    record_id = input("\nEnter the ID of your selected " + record + ":  ")
    return record_id

def execute_menu_choice(choice, conn):

    if choice == 'E':
        conn.close()
        exit()

    if choice == "1":
        dict = flight_dict
        view_filter = flight_view_menu() # all, by pilot, destination or departure date

        if view_filter == "1": # all
            query = dict['query_names'][0]
            display_records(conn, dict, query)
            return
        
        if view_filter == "2": # by pilot
            # display all pilots and get user to select
            dict = pilot_dict
            query = "SELECT * FROM view_pilots"
            display_records(conn, dict, query)
            filter_id = get_filter_id('pilot')
            # display flights by selected pilot
            dict = flight_dict
            query = load_query_from_file('queries.sql', 'query_flights_by_pilot')
            print("filter = " + filter_id)
            display_records(conn, dict, query, filter_id)
            return
        
        if view_filter == "3": # by destination
            dict = airport_dict
            query = dict['query_names'][0]
            display_records(conn, dict, query)
            filter_id = get_filter_id('airport')
            dict = flight_dict
            query = load_query_from_file('queries.sql', 'query_flights_by_dep_airport')
            print("filter = " + filter_id)
            display_records(conn, dict, query, filter_id)
            return
        
        if view_filter == "4": # by departure date
            dict = flight_dict
            filter_id = get_filter_id('date')
            query = load_query_from_file('queries.sql', 'query_flights_by_date')
            print("filter = " + filter_id)
            display_records(conn, dict, query, filter_id)
            return
        
    if choice == "3":
        dict = airport_dict
        print("\n")
        print("Which pilot's schedule would you like to view?")
        print("\n")
        query = load_query_from_file('queries.sql', 'view_pilots_with_flights_assigned')
        display_records(conn, pilot_dict, query)
        filter_id = get_filter_id('pilot')
        query = load_query_from_file('queries.sql', 'query_flights_by_pilot')
        print("\n")
        display_records(conn, dict, query, filter_id)
        return

    if choice == "4":
        print("4. Assign pilot to flight")
        cursor = conn.cursor()
        dict = pilot_dict
        print("Which pilot would you like to assign?")
        sql = load_query_from_file('queries.sql', 'view_pilots')
        display_records(conn, pilot_dict, sql)
        pilot_id = get_record_id('pilot')
        print(pilot_id)
        updated_value = pilot_id
        print("Which flight would you like to  would you like to assign this pilot to?")
        query = flight_dict['query_names'][0]
        display_records(conn, flight_dict, query)
        flight_id = get_record_id('flight')
        print(flight_id)
        col_to_update = 'pilot_ID'
        sql = f"UPDATE {flight_dict['table_name']} SET pilot_ID = ? WHERE ID = ?"
        cursor.execute(sql, (pilot_id, flight_id))
        sql = f"UPDATE {'flight'} SET {col_to_update} = ? WHERE ID = ?"
        cursor.execute(sql, (updated_value, flight_id))
        conn.commit()


    if (choice == ('2' or '5' or '6')):
        if choice == "2":
            dict = flight_dict
        if choice == "5":
            dict = airport_dict
        if choice == "6":
            dict = pilot_dict
        execute_VAAR_menu_choice(conn, dict)

    if (choice == '7'):
        cursor = conn.cursor()
        query = load_query_from_file('queries.sql', 'count_flights_to_destinations')
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"Destination: {row[0]}, Number of flights: {row[1]}") 
    
    if (choice == '8'):
        cursor = conn.cursor()
        query = load_query_from_file('queries.sql', 'count_flights_to_destinations_greater_1')
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"Destination: {row[0]}, {row[1]} flights") 


def execute_VAAR_menu_choice(conn, dict):
                
    choice_vaar = VAAR_menu(dict['table_name']) # view add amend remove 

    if choice_vaar == "1": # view
        query = dict['query_names'][0]
        display_records(conn, dict, query)
        return

    if choice_vaar == "2": # add
        add_record(conn, dict)
        return
    
    if choice_vaar == "3": # amend
        index = get_record_index(conn, dict)
        col_to_update = get_col_to_update(dict)
        updated_value = new_value()
        update_record(conn, dict, index, col_to_update, updated_value)
        return
    
    if choice_vaar == "4": # remove

        remove_record(conn, dict)
        return
    
    if choice_vaar == 'E':
        conn.close()
        exit()

