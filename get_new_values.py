from dictionaries import *

def display_and_choose(dict, query):
    print(f"Which {dict['table_name']} would you like to use?")
    print(query)
    print("\n")
    record_id = input(f"Enter the required ID: ")
    return record_id

def increment_id(previous_id):
    if isinstance(previous_id, tuple):
        previous_id = previous_id[0] 
    prefix = previous_id[:-3]  # get everything but the last 3 chars i.e. the first four 'XXID'
    number = int(previous_id[-3:])  # Get the last 3 chars - numeric part, convert string to integer
    next_num = number + 1  # Increment the number
    next_id = f"{prefix}{next_num:03}"  # Format with leading zeros
    return next_id


def get_new_flight_values(last_id):
    id = increment_id(last_id)
    IATA_flight_no = input("Enter the IATA flight number: ")
    plane = input("Enter the plane ID:  ")
    dep_airport = input("Enter the departure airport code (max 3 characters):  ")
    arr_airport = input("Enter the arrival airport code (max 3 characters):  ")
    pilot = input("Enter the pilot's ID:  ")
    first_officer = input("Enter the first officer's ID, if applicable:  ")
    date_dep = input("Enter the scheduled departure date and time in the following format YYYY-MM-DD HH:MM:SS:  ")
    date_arr = input("Enter the scheduled arrival date and time in the following format YYYY-MM-DD HH:MM:SS:  ")
    return id, IATA_flight_no, plane, dep_airport, arr_airport, pilot, first_officer, date_dep, date_arr, 


def get_new_pilot_values(last_id):
    id = increment_id(last_id)
    surname = input("Enter the pilot's surname:  ")
    forename = input("Enter the pilot's forename:  ")
    return id, surname, forename


def get_new_airport_values(last_id):
    id = increment_id(last_id)
    IATA_code = input("Enter the IATA airport code:  ")
    name = input("Enter the airport name:  ")
    city = input("Enter the airport's nearest city:  ")
    country = input("Enter the country in which the airport is located:  ")
    continent = input("Enter the continent:  ")
    status = input("Enter the airport's current status: \n1: open, \n2: open: alert, \n3: closed   ")
    return id, IATA_code, name, city, country, continent, status