from sql_queries import *

import sqlite3
conn = sqlite3.connect('flight management database')
cursor = conn.cursor()


class Database:

    def __init__(self, db_path):
  #      self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        print(f"Connected to {self.db_path}")
"""
    def commit(self):
        try:

        if self.conn:
            self.conn.commit()


    def close(self, commit=True):
        try:
            self.conn.close()
            print("Connection closed.")
        except sqlite3.Error as e:
            print("An error occurred:", e)

    """

    def execute(self, query, params=None):
        if not self.cursor:
            self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)


    def execute(self, query, params = None):
        self.cursor.execute(query, params or ())

    def create_all_tables(self, conn):
            self.execute(sql_create_staff)
            self.execute(sql_create_airport)
            self.execute(sql_create_airport_status)
            self.commit()

#    def create_table(conn, query):
#        query = f"CREATE TABLE IF NOT EXISTS {query}"
#        try:
#            cursor.execute(query)
#        except sqlite3.Error as e:
#            print("An error occurred:", e)
#        finally:
#            conn.commit()
#            conn.close()

    def select_all_from_table(conn, table_name):
        query = f"SELECT * FROM {table_name}"       
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            print(f"\nData from table '{table_name}':")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print("An error occurred:", e)
        finally:
            conn.commit()
            #conn.close()



            """

if __name__ == "__main__":
    
    db = Database('store')
    db.execute("DROP TABLE IF EXISTS airport_status")
    db.execute("DROP TABLE IF EXISTS airport")
    db.execute("DROP TABLE IF EXISTS staff")

#    db.create_all_tables
    db.execute(sql_create_staff)
    db.execute(sql_create_airport)
    db.execute(sql_create_airport_status)

    db.execute(staff_record_1)
    db.execute(airport_record_1)
    db.execute(airport_record_2)
    db.execute(airport_record_3)
    db.execute(airport_status_record_1)
    db.execute(airport_status_record_2)
    db.execute(airport_status_record_3)

    db.select_all_from_table('staff')

    db.close()
    print(db.conn.total_changes)
"""