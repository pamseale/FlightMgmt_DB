import sqlite3
db_filename = 'flight_management_database.db'


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