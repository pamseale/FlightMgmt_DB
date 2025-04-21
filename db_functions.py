import sqlite3
from function import *
from menu_functions import *
from input_validation_functions import *

# create sql connection object
conn = sqlite3.connect('flight_management_database.db')

#flight_column_names = ["No.", "Flight no.", "Plane", "Dep", "Arr", "Pilot", "First Officer", "Relief Captain", "Departure (sch.)", "Arrival (sch.)", "Departure (act.)", "Arrival (act)"]
#staff_column_names = ["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"]
#airport_column_names = ["No.", "Code", "Name", "City", "Country", "Continent", "Status"]

#flight_view_query = 'view_flights'
#staff_view_query = 'view_staff'
#airport_view_query = 'view_airports'


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
    # split file in sections at each comment (--)
    sections = content.split('-- ')
    for section in sections:
        if not section.strip():
            continue
        if section.startswith(query_name):
            return section[len(query_name):].strip()
    raise ValueError(f"Query not found.")

#def display_data(query, table_name, column_names):
#    print(f"\nAll {table_name} information:\n")
#    display_table(query, column_names)

"""
def display_flights():
    print("\nAll flight information:\n")
    column_names = ["No.", "Flight no.", "Plane", "Dep", "Arr", "Pilot", "First Officer", "Relief Captain", "Departure (sch.)", "Arrival (sch.)", "Departure (act.)", "Arrival (act)"]
    display_table('view_flights', column_names)

def display_airports():
    print("\nAll airport information:\n")
    column_names = ["No.", "Code", "Name", "City", "Country", "Continent", "Status"]
    display_table('view_airports', column_names)

def display_staff():
    print("\nAll staff information:\n")
    column_names = ["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"]
    display_table('view_staff', column_names)
"""

def display_table(query_name, table_name, column_names):
    print(f"\nAll {table_name} information:\n")
    conn = sqlite3.connect('flight_management_database.db')
    cursor = conn.cursor()
    # get SQL query from file and execute
    query = load_query("view_queries.sql", query_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    # add numbering to each row for user reference
    all_numbered_rows = [] # empty list
    for i, row in enumerate(rows):
        list_of_rows = list(row) # create a list from cursor.fetchall() command
        row_number = i+1 # starts at 1 instead of 0
        numbered_row = [row_number] + list_of_rows
        all_numbered_rows.append(numbered_row)
    #numbered_rows = [[i + 1] + list(row) for i, row in enumerate(rows)]
    # add padding to column widths by determining max width
    columns = list(zip(*all_numbered_rows)) if all_numbered_rows else [[] for _ in column_names]
    col_widths = [
        max(len(str(item)) if item is not None else 0 for item in col + (header,))
        for col, header in zip(columns, column_names)]
    format_str = " | ".join(f"{{:<{width}}}" for width in col_widths)
    # print column headings
    print(format_str.format(*column_names))
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    # allow for NULL value entries
    for row in all_numbered_rows:
        safe_row = [str(item) if item is not None else "" for item in row]
        print(format_str.format(*safe_row))
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




