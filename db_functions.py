import sqlite3
from input_validation import request_and_validate
from formatting import format_and_print
from get_new_values import get_new_flight_values, get_new_staff_values, get_new_airport_values

db_filename = 'flight_management_database.db'
queries_filename = 'queries.sql'

def display_records(conn, dict, sql, args=None):
    cursor = conn.cursor()
    if args:
        cursor.execute(sql, (args,))
    else:
        cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit
    format_and_print(dict, rows)


def row_count(conn, table_name):
    cursor = conn.cursor()
    num_rows = cursor.execute(f"SELECT COUNT(*) from {table_name}")
    for row in num_rows :
        result = (row[0])
    return result


def new_value():
    new_value = input("What would you like the new value to be?")
    return new_value


def get_record_index(conn, dict):
    # display all records
    sql = dict['query_names'][0]
    display_records(conn, dict, sql)
    # count rows
    num_rows = row_count(conn, dict['table_name'])

    # get which record to update
    print("\nWhich record would you like to change?\n")
    record_no = request_and_validate(1, num_rows)
    
    # get record index
    index = int(record_no) - 1
    return index

def get_col_to_update(dict):
    print_amend_options(dict)
    num_options = len(dict['amend_options'])
    valid_input = (request_and_validate(1, num_options))
    index = int(valid_input) - 1
    column_name = dict['amend_actual'][index]
    return column_name

def print_amend_options(dict):
    print("\nYou have permission to update the following records:\n")
    for opt in dict['amend_options']:
        print (opt)
    print("\n")

def update_record(conn, dict, record_index, column_to_update, updated_value):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * from {dict['table_name']} ")
    rows = cursor.fetchall()
    record_id = rows[record_index][0]
    sql = f"UPDATE {dict['table_name']} SET {column_to_update} = ? WHERE ID = ?"
    cursor.execute(sql, (updated_value, record_id))
    conn.commit()


def get_new_record_values(table, last_record_id):
    if table == 'flight':
        return get_new_flight_values(last_record_id)
    if table == 'staff':
        return get_new_staff_values(last_record_id)
    if table == 'airport':
        return get_new_airport_values(last_record_id)

def get_last_record_id(conn, dict):
    cursor = conn.cursor()
    sql = f"SELECT ID FROM {dict['table_name']} ORDER BY ID DESC LIMIT 1;"
    cursor.execute(sql)
    last_id = cursor.fetchone()
    conn.commit()        
    return  last_id

def get_col_names(conn, dict):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * from {dict['table_name']} LIMIT 1")
    column_names = [desc[0] for desc in cursor.description]
    conn.commit()        
    conn.close
    return column_names

def insert_new_data(conn, dict, columns_str, placeholders, args):
    cursor = conn.cursor()
    sql = f"INSERT INTO {dict['table_name']} ({columns_str}) VALUES ({placeholders})"
    cursor.execute(sql, args)
    conn.commit()        
    print(f"Record added ({args[1]})")
    conn.close

def add_record(conn, dict):
    
    # get last record id for incrementing
    last_id = get_last_record_id(conn, dict)

    # get column names for adding data into
    column_names = get_col_names(conn, dict)
    columns_str = ', '.join(column_names)  # joins into one string

    # get args for new data
    placeholders = ', '.join(['?'] * len(column_names))  # creates '?, ?, ?, ?'
    args = get_new_record_values(dict['table_name'], last_id)
    if len(args) != len(column_names):
        raise ValueError(f"Mismatch: table '{dict['table_name']}' expects {len(column_names)} values, but got ({placeholders})")
    
    # insert into table
    print(column_names)
    print(args)
    insert_new_data(conn, dict, columns_str, placeholders, args)

    # print updated table
    print(f"\nUpdated {dict['table_name']} records are as follows: \n")
    query = dict[dict['query_names'][0]]
    display_records(conn, dict, query)


def remove_record(conn, dict):
    cursor = conn.cursor()
    # display all records
    query = dict['query_names'][0]
    display_records(conn, dict, query)

    # count rows in table, 
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

