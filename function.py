import sqlite3
import uuid
from sql_queries import *

# Generate a GUID
guid = str(uuid.uuid4())


# database functions


# represents the current item/element

table_list = ['airport', 'airport_status', 'staff', 'plane']


def drop_all_tables(conn):
    for table in table_list:
        drop_table(conn, table)


def create_all_tables(conn):
    # create tables
    execute(conn, sql_create_staff)
    execute(conn, sql_create_airport)
    execute(conn, sql_create_airport_status)
    execute(conn, sql_create_plane)

def populate_all_tables(conn):
    # populate tables
    execute(conn, staff_record_1)
    execute(conn, staff_record_2)
    execute(conn, staff_record_3)
    execute(conn, staff_record_4)
    execute(conn, airport_record_1)
    execute(conn, airport_record_2)
    execute(conn, airport_record_3)
    execute(conn, airport_status_record_1)
    execute(conn, airport_status_record_2)
    execute(conn, airport_status_record_3)


def drop_table(conn, table_name):
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
    #    close(conn)

def display_all_from_table(conn, table_name):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    try:
      cursor.execute(query)
      rows = cursor.fetchall()
      print(f"\nData from table '{table_name}':")
      for row in rows:
            print(row)
      conn.commit()
    except sqlite3.Error as e:
        print("An error occurred:", e)
#    finally:
    #    close(conn)

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