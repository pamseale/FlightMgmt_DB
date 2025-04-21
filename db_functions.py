import sqlite3
from function import *
from menu_functions import *
from input_validation_functions import *

# create sql connection object
conn = sqlite3.connect('flight_management_database.db')

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

# add numbering to each row
def add_numbering(rows):
    numbered_rows = [] # empty list
    for i, row in enumerate(rows):
        list_of_rows = list(row) # create a list from cursor.fetchall() command
        row_number = i+1 # starts at 1 instead of 0
        numbered_row = [row_number] + list_of_rows
        numbered_rows.append(numbered_row)
    return numbered_rows
    #numbered_rows = [[i + 1] + list(row) for i, row in enumerate(rows)]

# calculate padding for printing column headers
def calc_padding(rows, column_names):
    columns = list(zip(*rows)) if rows else [[] for _ in column_names]
    col_widths = [
        max(len(str(item)) if item is not None else 0 for item in col + (header,))
        for col, header in zip(columns, column_names)]
    return col_widths

# add padding to column headers
def add_padding(col_widths):
    format_str = " | ".join(f"{{:<{width}}}" for width in col_widths)
    return format_str
    

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

def print_staff_amend_menu():
    print("\nYou have permission to update the following records:/n")
    print("1. Surname")
    print("2. Forename")
    print("3. Role")
    print("\n Which value would you like to update?\n")

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
    else:
        return "no"

def new_value():
    new_value = input("What would you like the new value to be?")
    return new_value


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
        value_to_update = str(staff_amend_menu())
        updated_value = new_value()
        sql = f"UPDATE {table_name} SET {value_to_update} = ? WHERE ID = ?"
        cursor.execute(sql, (updated_value, record_id))
        conn.commit()
        print(f"Updated record (ID: {record_id})")
    else:
        print(f"Row {record_no} does not exist.")
    conn.close