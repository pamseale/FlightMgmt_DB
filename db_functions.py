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
    column_names = ["Flight no.", "Plane", "Dep", "Arr", "Pilot", "First Officer", "Relief Captain", "Departure (sch.)", "Arrival (sch.)", "Departure (act.)", "Arrival (act)"]
    display_table(conn, 'view_flights', column_names)

def display_airports():
    print("\nAll airport information:\n")
    column_names = []
    display_table(conn, 'airport', column_names)

def display_staff():
    print("\nAll staff information:\n")
    column_names = []
    display_table(conn, 'staff', column_names)


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


"""def display_table(conn, table_name):
    conn = sqlite3.connect('flight_management_database.db')
    conn.row_factory = dict_factory
    for row in conn.execute("SELECT ID FROM flight as flight_number"):
        print(row)
#
#     cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    res = conn.execute(query)
    rows = res.fetchall()
    for row in rows:
        row.keys()
        row['ID']
        print(row['ID'])"""

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def display_all_from_table(conn, table_name):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    try:
        cursor.execute(query)
        rows_all = cursor.fetchall()
        row_one = cursor.fetchone()
        col_names = row_one.keys()
        print(f"\nData from table '{table_name}':")
        for row in rows_all:
            print(row)
            print(col_names['ID'])
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
#    finally:
    #    close(conn)

def display_view(conn, view_name):
    cursor = conn.cursor()
    query = f"SELECT * FROM {view_name}"
    cursor.execute(query).fetchall()

#    print(conn.execute("SELECT * FROM flight_view").fetchall())
#    cursor = conn.cursor()
    query = f"{view_name}"
    try:
        print(conn.execute("SELECT * FROM flight_view").fetchall())
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)

def execute(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)

def close(conn):
    try:
       conn.close()
    except sqlite3.Error as e:
       print("An error occurred:", e)


"""def drop_table(conn, table_name):
    cursor = conn.cursor()
    query = f"DROP TABLE IF EXISTS {table_name}"
    try:
      cursor.execute(query)
      conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
#    finally:
    #    close(conn)

def create_table(conn, table_name):
    cursor = conn.cursor()
    query = f"CREATE TABLE IF NOT EXISTS {table_name}"
    try:
      cursor.execute(query)
      conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
#    finally:
    #    close(conn)"""