
# queries to create tables
sql_create_staff = "CREATE TABLE IF NOT EXISTS staff (ID VARCHAR(6) NOT NULL, surname VARCHAR(20) NOT NULL, forename VARCHAR(20) NOT NULL, role VARCHAR(4), availability VARCHAR(4), license_ID VARCHAR(20), PRIMARY KEY (ID));"
sql_create_airport = "CREATE TABLE IF NOT EXISTS airport (ID VARCHAR(3) NOT NULL, city varchar(255), country varchar(255), continent varchar(255), status varchar(20), PRIMARY KEY (ID));"
sql_create_airport_status = "CREATE TABLE IF NOT EXISTS airport_status (ID VARCHAR(4) NOT NULL, status VARCHAR(20) NOT NULL, PRIMARY KEY (ID));"
sql_create_plane = "CREATE TABLE IF NOT EXISTS plane (ID VARCHAR(6) NOT NULL, make VARCHAR(255), model VARCHAR(255), manufacturer VARCHAR(255), status VARCHAR(20), capacity INT, cabin_crew_size INT, current_location VARCHAR(3), FOREIGN KEY (current_location) REFERENCES airport(ID), PRIMARY KEY (ID));"
#sql_create_staff = '''CREATE TABLE IF NOT EXISTS staff (ID VARCHAR(6) NOT NULL, surname VARCHAR(20) NOT NULL, forename VARCHAR(20) NOT NULL, role VARCHAR(4), availability VARCHAR(4), license_ID VARCHAR(20), PRIMARY KEY (ID));'''


# queries to create records
staff_record_1 = "INSERT INTO staff VALUES ('STID000001', 'Bloggs', 'Joe', 'PL1', 'AVID01', 'AV027639');"
staff_record_2 = "INSERT INTO staff VALUES ('STID000002', 'Bloggs', 'Alex', 'PL1', 'AVID01', 'AV027639');"
staff_record_3 = "INSERT INTO staff VALUES ('STID000003', 'Bloggs', 'Amy', 'PL1', 'AVID01', 'AV027639');"
staff_record_4 = "INSERT INTO staff VALUES ('STID000004', 'Bloggs', 'Xan', 'PL1', 'AVID01', 'AV027639');"

airport_record_1 = "INSERT INTO airport (ID, city, country, continent, status) VALUES ('EDI', 'Edinburgh', 'UK', 'Europe', 'ASID01');"
airport_record_2 = "INSERT INTO airport (ID, city, country, continent, status) VALUES ('LON', 'London', 'UK', 'Europe', 'ASID01');"
airport_record_3 = "INSERT INTO airport (ID, city, country, continent, status) VALUES ('MUN', 'Munich', 'Germany', 'Europe', 'ASID02');"

airport_status_record_1 = "INSERT INTO airport_status VALUES ('ASID01', 'open');"
airport_status_record_2 = "INSERT INTO airport_status VALUES ('ASID02', 'closed');"
airport_status_record_3 = "INSERT INTO airport_status VALUES ('ASID03', 'warning in place');"

#.sql file

