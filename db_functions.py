import sqlite3
from function import *
from menu_functions import *
from input_validation import *
from formatting import *

# create sql connection object
conn = sqlite3.connect('flight_management_database.db')


flight_dict = {
    "table_name": "flight",
    "col_headers":["No.", "Flight no.", "Plane", "Dep", "Arr", "Pilot", "First Officer", "Relief Captain", "Departure (sch.)", "Arrival (sch.)", "Departure (act.)", "Arrival (act)"],
    "amend_options": ["1. Plane", "2. Departure airport", "3. Arrival airport", "4. Pilot", "5. First Officer", "6. Relief Captain", "7. Scheduled departure date/time", "8. Scheduled arrival date/time", "9. Actual departure date/time", "10. Actual arrival date/time"],
    "query_view": "view_flights"
}

staff_dict = {
    "table_name": "staff",
    "col_headers":["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"],
    "amend_options": ["1. Surname", "2. Forename", "3. Role"],
    "query_view": "view_staff"
}

airport_dict = {
    "table_name": "airport",
    "col_headers":["No.", "Code", "Name", "City", "Country", "Continent", "Status"],
    "amend_options": ["1. Name", "2. Status"],
    "query_view": "view_airports"
}


#import database
def import_db():
   with open('db_setup.sql', 'r') as sql_file:
      sql_script = sql_file.read()
   cursor = conn.cursor()
   cursor.executescript(sql_script)
   conn.commit()
   conn.close()

def load_query(file_path, query_name):
    # read query file
    with open(file_path, "r") as file:
        content = file.read()
    # split file in sections at each comment(--), effectively the query title
    sections = content.split('-- ')
    for section in sections:
        if not section.strip():
            continue
        if section.startswith(query_name):
            return section[len(query_name):].strip()
    # error message if query not found
    raise ValueError(f"Query {query_name} not found.")

    

def display_table(query_name, table_name, column_names):
    print(f"\nAll {table_name} information:\n")
    # create connection object
    conn = sqlite3.connect('flight_management_database.db')
    cursor = conn.cursor()
    # get SQL query from file and execute
    query = load_query("view_queries.sql", query_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    numbered_rows = add_numbering(rows)
    col_widths = calc_padding(numbered_rows, column_names)
    headers = add_padding(col_widths)
    print(headers.format(*column_names))
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    # allow for NULL value entries
    for row in numbered_rows:
        safe_row = [str(item) if item is not None else "" for item in row]
        print(headers.format(*safe_row))
    conn.commit
    conn.close

def row_count(conn, table_name):
    cursor = conn.cursor()
    num_rows = cursor.execute(f"SELECT COUNT(*) from {table_name}")
    for row in num_rows :
        result = (row[0])
    return result

def remove_record(query_name, table_name, column_names):
    conn = sqlite3.connect('flight_management_database.db')
    cursor = conn.cursor()
    display_table(query_name, table_name, column_names)
    num_rows = row_count(conn, table_name)
    print("\nWhich record would you like to delete?\n")
    record_no = request_and_validate(1, num_rows)
    cursor.execute(f"SELECT * from {table_name} ")
    rows = cursor.fetchall()
    index = int(record_no) - 1
    if 0 <= index < len(rows):
        record_id = rows[index][0]
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (record_id,))
        conn.commit()
        print(f"Deleted record (ID: {record_id})")
    else:
        print(f"Row {record_no} does not exist.")
    conn.close

def print_amend_options(dict):
    print("\nYou have permission to update the following records:\n")
    if 'amend_options' in dict:
        for item in dict['amend_options']:
            print(item)
    else:
        print("not found")

def print_staff_amend_menu():
    print("\nYou have permission to update the following records:/n")
    print("1. Surname")
    print("2. Forename")
    print("3. Role")
    print("\n Which value would you like to update?\n")

def print_airport_amend_menu():
    print("\nYou have permission to update the following records:/n")
    print("1. Name")
    print("2. Status")
    print("\n Which value would you like to update?\n")

def flight_amend_menu():
    print_amend_options(flight_dict)
    num_options = 8
    valid_input = request_and_validate(1, num_options)
    if valid_input == '1':
        return "plane_ID"
    if valid_input == '2':
        return "airport_dep_ID"
    if valid_input == '3':
        return "airport_arr_ID" 
    if valid_input == '4':
        return "pilot_ID"
    if valid_input == '5':
        return "first_officer_ID"
    if valid_input == '6':
        return "relief_captain_ID" 
    if valid_input == '7':
        return "date_dep_scheduled"
    if valid_input == '8':
        return "date_arr_scheduled"
    if valid_input == '9':
        return "date_dep_actual"
    if valid_input == '10':
        return "date_arr_actual"


def staff_amend_menu():
    print_staff_amend_menu()
    num_options = 3
    valid_input = request_and_validate(1, num_options)
    if valid_input == '1':
        return "surname"
    if valid_input == '2':
        return "forename"
    if valid_input == '3':
        return "role" 

def airport_amend_menu():
    print_airport_amend_menu()
    num_options = 2
    valid_input = request_and_validate(1, num_options)
    if valid_input == '1':
        return "name"
    if valid_input == '2':
        return "airport_status_ID"
    
def new_value():
    new_value = input("What would you like the new value to be?")
    return new_value

def get_airport_record():
    id = input("Enter the airport ID in the following format: AAA  ")
    name = input("Enter the airport name:  ")
    city = input("Enter the airport's nearest city:  ")
    country = input("Enter the country in which the airport is located:  ")
    continent = input("Enter the continent:  ")
    status = input("Enter the airport's current status (open, closed, warning in place):  ")
    return id, name, city, country, continent, status


def amend_record(query_name, table_name, column_names):
    conn = sqlite3.connect('flight_management_database.db')
    cursor = conn.cursor()
    display_table(query_name, table_name, column_names)
    num_rows = row_count(conn, table_name)
    print("\nWhich record would you like to change?\n")
    record_no = request_and_validate(1, num_rows)
    cursor.execute(f"SELECT * from {table_name} ")
    rows = cursor.fetchall()
    index = int(record_no) - 1
    if 0 <= index < len(rows):
        record_id = rows[index][0]
        value_to_update = str(flight_amend_menu())
        updated_value = new_value()
        sql = f"UPDATE {table_name} SET {value_to_update} = ? WHERE ID = ?"
        cursor.execute(sql, (updated_value, record_id))
        conn.commit()
        print(f"Updated record (ID: {record_id})")
    else:
        print(f"Row {record_no} does not exist.")
    conn.close


def add_record(query_name, table_name, column_names):
    conn = sqlite3.connect('flight_management_database.db')
    cursor = conn.cursor()
    column_names = ["No.", "Code", "Name", "City", "Country", "Continent", "Status"]
    args = get_airport_record()
    sql = "INSERT INTO airport (ID, name, city, country, continent, airport_status_ID) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, args)
    conn.commit()        
    print(f"Record added ({args[1]})")
    conn.close