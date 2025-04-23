import sqlite3

from input_validation import request_and_validate
from formatting import *
from get_new_record_functions import *

db_filename = 'flight_management_database.db'
queries_filename = 'queries.sql'

def execute_query(query):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    sql = load_query(queries_filename, query)


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
            query = load_query(queries_filename, 'view_all_flights')
            cursor.execute(query)
       #     display_table(dict, 'view_flights')
            return
        if choice == "2": # by pilot
            query = 'view_flights_by_pilot'
            load_query(queries_filename, query)
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

def display_records(dict, query, args=None):
    #table_name = dict['table_name']
    #print(f"\{dict['table_name']} information:\n")
    # create connection object
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    # get SQL query from file and execute
    sql = load_query(queries_filename, query)
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
    for opt in dict['amend_options']:
        print (opt)
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
    column_name = dict['actual_headers'][index]
    return column_name
    

def new_value():
    new_value = input("What would you like the new value to be?")
    return new_value


def update_record(dict):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    query = dict['query_names'][0]
    display_records(dict, query)
    num_rows = row_count(conn, dict['table_name'])
    print("\nWhich record would you like to change?\n")
    record_no = request_and_validate(1, num_rows)
    index = int(record_no) - 1
    cursor.execute(f"SELECT * from {dict['table_name']} ")
    rows = cursor.fetchall()
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
        return get_new_flight_values()
    if table == 'staff':
        return get_new_staff_values()
    if table == 'airport':
        return get_new_airport_values()


def add_record(dict):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * from {dict['table_name']} LIMIT 1")
    column_names = [desc[0] for desc in cursor.description]
    columns_str = ', '.join(column_names)  # joins into one string
    placeholders = ', '.join(['?'] * len(column_names))  # creates '?, ?, ?, ?'
    args = get_new_record_values(dict['table_name'])
    if len(args) != len(column_names):
        raise ValueError(f"Mismatch: table '{dict['table_name']}' expects {len(column_names)} values, but got ({placeholders})")
    sql = f"INSERT INTO {dict['table_name']} ({columns_str}) VALUES ({placeholders})"
    cursor.execute(sql, args)
    conn.commit()        
    print(f"Record added ({args[1]})")
    conn.close

def remove_record(dict):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    query = dict['query_names'][0]
    display_records(dict, query)
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