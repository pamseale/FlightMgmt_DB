
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
