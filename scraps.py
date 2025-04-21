"""
def amend_record(query_name, table_name, column_names):
    conn = sqlite3.connect('flight_management_database.db')
    cursor = conn.cursor()
    display_table(query_name, table_name, column_names)
    num_rows = row_count(conn, table_name)

    print("\nWhich record would you like to update?\n")
    record_no = request_and_validate(1, num_rows)



    cursor.execute(f"SELECT * from {table_name} ")
    rows = cursor.fetchall()
    index = int(record_no) - 1
    if 0 <= index < len(rows):
        record_id = rows[index][0]
    value_to_update = staff_amend_menu()
    amend_record(value_to_update)
    #    cursor.execute(f"SELECT * FROM {table_name} LIMIT 1")
     #   row = cursor.fetchone()
     #   column_names = [desc[0] for desc in cursor.description]
     #   if row:
     #       non_empty_columns = [name for name, value in zip(column_names, row) if value not in (None, "")]
     #       print("Non-empty fields for this record:")
     #       for col in non_empty_columns:
     #           print(col)
        #cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (record_id,))
    conn.commit()
    print(f"Updated record (ID: {record_id})")
    else:
        print(f"Row {record_no} does not exist.")
    conn.close


def amend_staff_record(query_name, table_name, column_names):
    conn = sqlite3.connect('flight_management_database.db')
    cursor = conn.cursor()
    display_table(query_name, table_name, column_names)
    num_rows = row_count(conn, table_name)
    print("\nWhich record would you like to update?\n")
    record_no = request_and_validate(1, num_rows)
    cursor.execute(f"SELECT * from {table_name} ")
    rows = cursor.fetchall()
    index = int(record_no) - 1
    if 0 <= index < len(rows):
        record_id = rows[index][0]
        cursor.execute(f"SELECT * FROM {table_name} WHERE id = ?", (record_id))
        row = cursor.fetchone()
        amend_record(, row)
        conn.commit()
        print(f"Updated record (ID: {record_id})")
    else:
        print(f"Row {record_no} does not exist.")
    conn.close
"""
"""

    print("1. Plane")
    print("2. Departure airport")
    print("3. Arrival airport")
    print("4. Pilot")
    print("5. First Officer")
    print("6. Relief Captain")
    print("7. Scheduled departure date/time")
    print("8. Scheduled arrival date/time")
    print("9. Actual departure date/time")
    print("10. Actual arrival date/time")
    print("\n Which value would you like to update?\n")

    
def execute_staff_amend_menu_choice(choice):
    table_name = 'staff'
    query_amend = 'amend_staff'

    if choice == "1":
        value = 'surname'
    if choice == "2":
        value = 'forname'
    if choice == "3":
        value = 'role'
    if choice == "4":
        value = 'license_status'
    if choice == 'E':
        exit()
    #amend(query_amend, table_name, value)
"""

"""    FOREIGN KEY (first_officer_ID) REFERENCES staff(ID),
    FOREIGN KEY (relief_captain_ID) REFERENCES staff(ID),"""
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


"""def print_flight_menu():
    print("Would you like to:")
    print("1. View flight data")
    print("2. Amend flight data")
    print("3. Remove a flight from the database")

def print_staff_menu():
    print("Would you like to:")
    print("1. View pilot or staff data")
    print("2. Amend pilot or staff data")
    print("3. Remove a staff record from the database")

def print_airport_menu():
    print("Would you like to:")
    print("1. View airport data")
    print("2. Amend airport data")
    print("3. Remove an airport from the database")"""

"""def remove_staff():
#    conn = sqlite3.connect('flight_management_database.db')
#    column_names = ["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"]
    display_table('view_staff', column_names)
    num_rows = row_count(conn, 'staff')
    print("\nWhich record would you like to delete?\n")
#    print(num_rows)
    valid_input = request_and_validate(1, num_rows)
    remove_record(conn, 'staff', int(valid_input))
    conn.commit
    conn.close"""
"""
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
"""


"""
def flight_menu():
    print_flight_menu()
    num_options = 3
    valid_input = request_and_validate(1, num_options)
    return valid_input

def staff_menu():
    print_staff_menu()
    num_options = 3
    valid_input = request_and_validate(1, num_options)
    return valid_input

def airport_menu():
    print_airport_menu()
    num_options = 3
    valid_input = request_and_validate(1, num_options)
    return valid_input
"""
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
        print(row['ID'])

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def display_all_from_table(conn, table_name):
    conn = sqlite3.connect('flight_management_database.db')
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
    finally:
        close(conn)

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
    #    close(conn)"""




"""


DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS airport_status;
DROP TABLE IF EXISTS plane;



drop_all_tables(conn)

create_all_tables(conn)

populate_all_tables(conn)





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



execute(conn, "DROP TABLE IF EXISTS airport_status")
execute(conn, "DROP TABLE IF EXISTS airport")
execute(conn, "DROP TABLE IF EXISTS staff")
execute(conn, "DROP TABLE IF EXISTS plane")

drop_table(conn, 'airport')
drop_table(conn, 'airport_status')
drop_table(conn, 'staff')
drop_table(conn, 'plane')

# create tables
execute(conn, sql_create_staff)
execute(conn, sql_create_airport)
execute(conn, sql_create_airport_status)
execute(conn, sql_create_plane)








display_all_from_table(conn, 'staff')
display_all_from_table(conn, 'airport')
display_all_from_table(conn, 'airport_status')
display_all_from_table(conn, 'plane')

#print("\nline changes: " + str(conn.total_changes))

# Close the connection
#close(conn)




assuming:
flight_IDs will always follow the format VARCHAR(8)
plane_IDs will always follow the format VARCHAR(8)
airports





for row in cursor:
   print("name = ", row[0])
   print("owner = ", row[1])
   print("species = ", row[2])
   print("sex = ", row[3])
   print("checkups = ", row[4])
   print("birth = ", row[5])
   print("death = ", row[6], "\n")


cursor.execute("SELECT * FROM airport")
row = cursor.fetchone()

#print(f"ID: {row[0]}")
#print(f"loc: {row[1]}")

   def play_again():
    # asks player if they would like to play again
    while True:
        ready = input("Would you like to play again? yes or no. ")
        if ready == "yes":
            print("\nExcellent! Lets get started.\n")
            break
        elif ready == "no":
            print(
                "\nIt's been real. Come back later if you change your mind.\n")
        else:
            print("\nSimple 'yes' or 'no' please. I'm not ChatGPT.\n")


            # Create a table with a GUID primary key (stored as text)
#cursor.execute(
#    CREATE TABLE IF NOT EXISTS users (
#        id TEXT PRIMARY KEY,
#        name TEXT
#    )
#)

# Insert a record
cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (guid, "John Doe"))
cursor.execute("INSERT INTO staff VALUES ('STID000001', 'Bloggs', 'Joe', 'PI1', 'AVID01', 'AV027639');")
cursor.execute("INSERT INTO airport (ID, city, country, continent, status) VALUES ('EDI', 'Edinburgh', 'UK', 'Europe', 'ASID01');")
cursor.execute("INSERT INTO airport (ID, city, country, continent, status) VALUES ('LON', 'London', 'UK', 'Europe', 'ASID01');")
cursor.execute("INSERT INTO airport (ID, city, country, continent, status) VALUES ('MUN', 'Munich', 'Germany', 'Europe', 'ASID02');")
cursor.execute("INSERT INTO airport_status VALUES ('ASID01', 'open');")
cursor.execute("INSERT INTO airport_status VALUES ('ASID02', 'closed');")
cursor.execute("INSERT INTO airport_status VALUES ('ASID03', 'warning');")


for row in cursor:
   print("name = ", row[0])
   print("owner = ", row[1])
   print("species = ", row[2])
   print("sex = ", row[3])
   print("checkups = ", row[4])
   print("birth = ", row[5])
   print("death = ", row[6], "\n")

query = CREATE TABLE airport (
    ID VARCHAR(3) NOT NULL,
    city varchar(255),
    country varchar(255),
    continent varchar(255),
    status enumerate,
    PRIMARY KEY (ID)
);")


def execute_query(conn, query):
    # executes sql query
    conn.execute(query)




query = CREATE TABLE airport (
    ID VARCHAR(3) NOT NULL,
    city varchar(255),
    country varchar(255),
    continent varchar(255),
    status enumerate,
    PRIMARY KEY (ID)
);")

#conn.execute("CREATE TABLE IF NOT EXISTS staff (ID VARCHAR(6) NOT NULL, surname VARCHAR(20) NOT NULL, forename VARCHAR(20) NOT NULL, role VARCHAR(4), availability VARCHAR(4), license_ID VARCHAR(20), PRIMARY KEY (ID));")
#conn.execute("INSERT INTO staff VALUES ('STID000001', 'Bloggs', 'Joe', 'PI1', 'AVID01', 'AV027639');")


#conn.execute("CREATE TABLE IF NOT EXISTS airport_status (ID VARCHAR(4) NOT NULL, status VARCHAR(20) NOT NULL, PRIMARY KEY (ID));")
#conn.execute("INSERT INTO airport_status VALUES ('ASID01', 'open');")
#conn.execute("INSERT INTO airport_status VALUES ('ASID02', 'closed');")
#conn.execute("INSERT INTO airport_status VALUES ('ASID03', 'warning');")


#conn.execute("CREATE TABLE IF NOT EXISTS airport (ID VARCHAR(6) NOT NULL, city varchar(255), country varchar(255), continent varchar(255), status varchar(4), PRIMARY KEY (ID));")
#conn.execute("INSERT INTO airport (status) SELECT status FROM enums WHERE 'status' = 'open';")
#conn.execute("INSERT INTO airport (ID, city, country, continent, status) VALUES ('EDI', 'Edinburgh', 'UK', 'Europe', 'ASID01');")
#conn.execute("INSERT INTO airport (ID, city, country, continent, status) VALUES ('LON', 'London', 'UK', 'Europe', 'ASID01');")
#conn.execute("INSERT INTO airport (ID, city, country, continent, status) VALUES ('MUN', 'Munich', 'Germany', 'Europe', 'ASID02');")





#conn.execute("CREATE TABLE 'flight' (flight_ID VARCHAR(8), plane_ID VARCHAR(8), airport_departure VARCHAR(3), , birth DATE, death DATE)")
#conn.execute("CREATE TABLE 'airport' (airport_ID VARCHAR(3), plane_ID VARCHAR(8), airport_departure VARCHAR(3), , birth DATE, death DATE)")
#conn.execute(
  #  CREATE TABLE 'airport' (airport_ID VARCHAR(3), plane_ID VARCHAR(8), airport_departure VARCHAR(3), , birth DATE, death DATE)")


assuming:
flight_IDs will always follow the format VARCHAR(8)
plane_IDs will always follow the format VARCHAR(8)
airports

CREATE TABLE plane (
    ID VARCHAR(6) NOT NULL,
    make varchar(255),
    model varchar(255),
    manufacturer varchar(255),
    status enumerate
    capacity int,
    cabin_crew_size int,
    current_location enumerate FOREIGN KEY REFERENCES airport(ID),

    PRIMARY KEY (ID)

);")


cursor = conn.execute("SELECT * from pet")

for row in cursor:
   print("name = ", row[0])
   print("owner = ", row[1])
   print("species = ", row[2])
   print("sex = ", row[3])
   print("checkups = ", row[4])
   print("birth = ", row[5])
   print("death = ", row[6], "\n")

conn.execute("DROP DATABASE pet;")

cursor = conn.execute("SELECT * from pet")

for row in cursor:
   print("name = ", row[0])
   print("owner = ", row[1])
   print("species = ", row[2])
   print("sex = ", row[3])
   print("checkups = ", row[4])
   print("birth = ", row[5])
   print("death = ", row[6], "\n")




#conn.execute("CREATE TABLE 'pet' (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE, death DATE)")

#conn.execute("INSERT INTO pet VALUES ( 'Poor Jasper', 'Gwen', 'cat', 'f', 5, '2001-02-04', null)")

#conn.execute(" UPDATE 'pet' SET death = '2000-05-01' WHERE owner = 'Gwen' AND name = 'Poor Jasper';" )

#cursor = conn.execute("SELECT * from pet")


for row in cursor:
   print("name = ", row[0])
   print("owner = ", row[1])
   print("species = ", row[2])
   print("sex = ", row[3])
   print("checkups = ", row[4])
   print("birth = ", row[5])
   print("death = ", row[6], "\n")




   def play_again():
    # asks player if they would like to play again
    while True:
        ready = input("Would you like to play again? yes or no. ")
        if ready == "yes":
            print("\nExcellent! Lets get started.\n")
            break
        elif ready == "no":
            print(
                "\nIt's been real. Come back later if you change your mind.\n")
        else:
            print("\nSimple 'yes' or 'no' please. I'm not ChatGPT.\n")
"""
""""
"""""
