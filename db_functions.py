import sqlite3

from input_validation import request_and_validate
from formatting import *
#from menu_functions import flight_view_menu

db_filename = 'flight_management_database.db'
"""
flight_dict = {
    "table_name": "flight",
    "display_headers":["No.", "Flight no.", "Plane", "Dep", "Arr", "Pilot", "First Officer", "Relief Captain", "Departure (sch.)", "Arrival (sch.)", "Departure (act.)", "Arrival (act)"],
    "actual_headers":["plane_ID", "airport_dep_ID", "airport_arr_ID", "pilot_ID", "first_officer_ID", "relief_captain_ID", "date_dep_scheduled", "date_arr_scheduled", "date_dep_actual", "date_dep_actual"],
    "amend_options":["1. Plane", "2. Departure airport", "3. Arrival airport", "4. Pilot", "5. First Officer", "6. Relief Captain", "7. Scheduled departure date/time", "8. Scheduled arrival date/time", "9. Actual departure date/time", "10. Actual arrival date/time"],
    "query_names": ["view_all_flights", "view_flights_by_pilot"]
}

    "amend_options": [  {'display': "1. Plane", 'col': "plane_ID"},
                        {'display': "2. Departure airport", 'col': "airport_dep_ID"},
                        {'display': "3. Arrival airport", 'col': "airport_arr_ID"},
                        {'display': "4. Pilot", 'col': "pilot_ID"},
                        {'display': "5. First Officer", 'col': "first_officer_ID"},
                        {'display': "6. Relief Captain", 'col': "relief_captain_ID"},
                        {'display': "7. Scheduled departure date/time", 'col': "date_dep_scheduled"},
                        {'display': "8. Scheduled arrival date/time", 'col': "date_arr_scheduled"},
                        {'display': "9. Actual departure date/time", 'col': "date_dep_actual"},
                        {'display': "10. Actual arrival date/time", 'col': "date_dep_actual"} ],
staff_dict = {
    "table_name": "staff",
    "col_headers":["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"],
    "amend_options": [  {'display': "1. Surname", 'col': "surname"},
                        {'display': "2. Forename", 'col': "forename"},
                        {'display': "3. Role", 'col': "role"} ],
    "query_names": ["view_staff"]
}

airport_dict = {
    "table_name": "airport",
    "col_headers":["No.", "Code", "Name", "City", "Country", "Continent", "Status"],
    "amend_options": [  {'display': "1. Name", 'col': "name"},
                        {'display': "2. Status", 'col': "status"} ],
    "query_names": ["view_airports"]
}


#import database
def import_db():
    # read .sql file
    with open('db_setup.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    # create db connection
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    # execute .sql file script
    cursor.executescript(sql_script)
    # commit chnages
    conn.commit()
    # close db connection
    conn.close()
"""


def load_query(file_path, query_name):
    # read query file
    with open(file_path, "r") as file:
        content = file.read()
    # split file in sections at each comment(--), effectively the query title
    sections = content.split('-- ')
    for section in sections:
#        if not section.strip():
#            continue
        if section.startswith(query_name):
            return section[len(query_name):].strip()
    # error message if query not found
    raise ValueError(f"Query {query_name} not found.")


def execute_sub_menu_choice(choice, dict):  # e.g. view flight
    conn = sqlite3.connect(db_filename)
    if choice == "1": # view
        filter = flight_view_menu() # all, by pilot, destination or departure date
        if filter == "1": # all
            query = load_query("view_queries.sql", 'view_all_flights')
            cursor.execute(query)
       #     display_table(dict, 'view_flights')
            return
        if choice == "2": # by pilot
            query = 'view_flights_by_pilot'
            load_query('view_queries.sql', query)
       #     display_table(dict, 'view_flights')
            return
        if choice == "3":
            print("by destination")
            return
    if choice == "2": # add
        add_record(dict)
        return
    if choice == "3": # amend
        update_record(dict)
        return
    if choice == "4": # remove
        remove_record(dict)
        return
    if choice == 'E':
        exit()

def display_all(dict, query, args=None):
    #table_name = dict['table_name']
    print(f"\{dict['table_name']} information:\n")
    # create connection object
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    # get SQL query from file and execute
    sql = load_query("view_queries.sql", query)
    print(sql)
    #cursor.execute(sql)

    if args:
        cursor.execute(sql, args)
    else:
        cursor.execute(sql)
    
    rows = cursor.fetchall()
    numbered_rows = add_numbering(rows)
    col_widths = calc_padding(numbered_rows, dict['display_headers'])
    headers = add_padding(col_widths)
    print(headers.format(*dict['display_headers']))
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    # allow for NULL value entries
    for row in numbered_rows:
        safe_row = [str(item) if item is not None else "" for item in row]
        print(headers.format(*safe_row))
    conn.commit
    conn.close

def display_filtered(dict, query, args=None):
    #table_name = dict['table_name']
    #print(f"\{dict['table_name']} information:\n")
    # create connection object
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    # get SQL query from file and execute
    sql = load_query("view_queries.sql", query)
  #  print(sql)
    print(args)

    print("\n")
    if args:
        cursor.execute(sql, (args,))
    else:
        cursor.execute(sql)
    rows = cursor.fetchall()
    numbered_rows = add_numbering(rows)
    col_widths = calc_padding(numbered_rows, dict['display_headers'])
    headers = add_padding(col_widths)
    print(headers.format(*dict['display_headers']))
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    # allow for NULL value entries
    for row in numbered_rows:
        safe_row = [str(item) if item is not None else "" for item in row]
        print(headers.format(*safe_row))
    conn.commit
    conn.close


def print_amend_options(dict):
    print("\nYou have permission to update the following records:\n")
    options = [opt['display'] for opt in dict['amend_options']]
    for option in options:
        print (option)
    print("\n")


def row_count(conn, table_name):
    cursor = conn.cursor()
    num_rows = cursor.execute(f"SELECT COUNT(*) from {table_name}")
    for row in num_rows :
        result = (row[0])
    return result


def get_col_to_update(dict):
    print_amend_options(dict)
    num_options = len(dict['amend_options'])
    valid_input = (request_and_validate(1, num_options))
    index = int(valid_input) - 1
    print(index)
    column_name = dict['amend_options'][index]['col']
    print(column_name)
    return column_name
    

def new_value():
    new_value = input("What would you like the new value to be?")
    return new_value


def update_record(dict):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    display_table(dict)
    num_rows = row_count(conn, dict['table_name'])
    print("\nWhich record would you like to change?\n")
    record_no = request_and_validate(1, num_rows)
    cursor.execute(f"SELECT * from {dict['table_name']} ")
    rows = cursor.fetchall()
    index = int(record_no) - 1
    if 0 <= index < len(rows):
        record_id = rows[index][0]
        col_to_update = get_col_to_update(dict)
        updated_value = new_value()
        sql = f"UPDATE {dict['table_name']} SET {col_to_update} = ? WHERE ID = ?"
        cursor.execute(sql, (updated_value, record_id))
        conn.commit()
        print(f"Updated record (ID: {record_id})")
    else:
        print(f"Row {record_no} does not exist.")
    conn.close


def get_new_record_values(table):
    if table == 'flight':
        return get_new_flight_record()
    if table == 'staff':
        return get_new_staff_record()
    if table == 'airport':
        return get_new_airport_record()


def add_record(dict):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * from {dict['table_name']} LIMIT 1")
    column_names = [desc[0] for desc in cursor.description]
    columns_str = ', '.join(column_names)  # joins into one string
    placeholders = ', '.join(['?'] * len(column_names))  # creates '?, ?, ?, ?'
    print(column_names)
    print(len(column_names))
    args = get_new_record_values(dict['table_name'])
    print(args)
    print(len(args))
    if len(args) != len(column_names):
        raise ValueError(f"Mismatch: table '{dict['table_name']}' expects {len(column_names)} values, but got ({placeholders})")
    sql = f"INSERT INTO {dict['table_name']} ({columns_str}) VALUES ({placeholders})"
    print(sql)
    cursor.execute(sql, args)
    conn.commit()        
    print(f"Record added ({args[1]})")
    conn.close

def remove_record(dict):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    display_table(dict)
    num_rows = row_count(conn, dict['table_name'])
    print("\nWhich record would you like to delete?\n")
    record_no = request_and_validate(1, num_rows)
    cursor.execute(f"SELECT * from {dict['table_name']} ")
    rows = cursor.fetchall()
    index = int(record_no) - 1
    if 0 <= index < len(rows):
        record_id = rows[index][0]
        cursor.execute(f"DELETE FROM {dict['table_name']} WHERE id = ?", (record_id,))
        conn.commit()
        print(f"Deleted record (ID: {record_id})")
    else:
        print(f"Row {record_no} does not exist.")
    conn.close