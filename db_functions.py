import sqlite3
from function import *
from menu_functions import *

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
    with open(file_path, "r") as file:
        content = file.read()
    # Split file at comments
    sections = content.split('-- ')
    for section in sections:
        if not section.strip():
            continue
        if section.startswith(query_name):
            return section[len(query_name):].strip()
    raise ValueError(f"Query not found.")

def display_flights():
    print("\nAll flight information:\n")
    column_names = ["No.", "Flight no.", "Plane", "Dep", "Arr", "Pilot", "First Officer", "Relief Captain", "Departure (sch.)", "Arrival (sch.)", "Departure (act.)", "Arrival (act)"]
    display_table(conn, 'view_flights', column_names)

def display_airports():
    print("\nAll airport information:\n")
    column_names = ["No.", "Code", "Name", "City", "Country", "Continent", "Status"]
    display_table(conn, 'view_airports', column_names)

def display_staff():
    print("\nAll staff information:\n")
    column_names = ["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"]
    display_table(conn, 'view_staff', column_names)


def display_table(conn, query_name, display_column_names):
    conn = sqlite3.connect('flight_management_database.db')
    cursor = conn.cursor()
    query = load_query("view_queries.sql", query_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = list(zip(*rows)) if rows else [[] for _ in display_column_names]
    col_widths = [max(len(str(item)) for item in col + (header,)) for col, header in zip(columns, display_column_names)]
    format_str = " | ".join(f"{{:<{width}}}" for width in col_widths)
    print(format_str.format(*display_column_names))
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    for row in rows:
        safe_row = [str(item) if item is not None else "" for item in row]
        print(format_str.format(*safe_row))


def row_count(conn, table_name):
    cursor = conn.cursor()
    num_rows = cursor.execute(f"SELECT COUNT(*) from {table_name}")
    for row in num_rows :
        print(row[0])
    return num_rows

def remove_record(conn, table_name, record_no):
    cursor = conn.cursor()
    num_rows = cursor.execute(f"DELETE from {table_name} WHERE rowid = {record_no} ")
    for row in num_rows :
        print(row[0])
    return num_rows

def remove_staff():
    conn = sqlite3.connect('flight_management_database.db')
    #cursor = conn.cursor()
    column_names = ["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"]
    display_table(conn, 'view_staff', column_names)
    print("\nWhich record would you like to delete?\n")
    num_rows = row_count(conn, 'staff')
    valid_input = request_and_validate(1, num_rows)
    #    record_ID = cursor.execute(f"SELECT COUNT(*) from 'staff")
    remove_record(conn, 'staff', valid_input)