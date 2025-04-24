def get_new_flight_values():
    id = input("Enter the flight no. (max 6 characters): ")
    plane = input("Enter the plane ID:  ")
    dep_airport = input("Enter the departure airport code (max 3 characters):  ")
    date_dep = input("Enter the scheduled departure date and time in the following format YYYY-MM-DD HH:MM:SS:  ")
    arr_airport = input("Enter the ariival airport code (max 3 characters):  ")
    date_arr = input("Enter the scheduled arrival date and time in the following format YYYY-MM-DD HH:MM:SS:  ")
    pilot = input("Enter the pilot's staff ID:  ")
    first_officer = input("Enter the first officer's staff ID, if applicable:  ")
    return id, plane, dep_airport, date_dep, arr_airport, date_arr, pilot, first_officer

def get_new_staff_values():
    id = input("Enter the staff ID in the following format: STID0000  ")
    surname = input("Enter the staff member's surname:  ")
    forename = input("Enter the staff member's forename:  ")
    role = input("Enter the staff member's role:  ")
    return id, surname, forename, role

def get_new_airport_values():
    id = input("Enter the airport ID in the following format: AAA  ")
    name = input("Enter the airport name:  ")
    city = input("Enter the airport's nearest city:  ")
    country = input("Enter the country in which the airport is located:  ")
    continent = input("Enter the continent:  ")
    status = input("Enter the airport's current status: \n1: open, \n2: open: alert, \n3: closed   ")
    return id, name, city, country, continent, status