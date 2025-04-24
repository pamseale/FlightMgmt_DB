DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS airport_status;
DROP TABLE IF EXISTS plane;
DROP TABLE IF EXISTS flight;

DROP VIEW IF EXISTS view_all_flights;
DROP VIEW IF EXISTS view_all_staff;
DROP VIEW IF EXISTS view_all_airports;


CREATE TABLE IF NOT EXISTS staff (
    ID VARCHAR(20) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    forename VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL,
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS airport (
    ID VARCHAR(20) NOT NULL,
    IATA_code  VARCHAR(3) NOT NULL,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    continent VARCHAR(255) NOT NULL,
    airport_status INT NOT NULL,
    FOREIGN KEY (airport_status) REFERENCES airport(ID),
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS airport_status (
    ID int NOT NULL,
    status_desc VARCHAR(20) NOT NULL,
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS plane (
    ID VARCHAR(20) NOT NULL,
    IATA_reg VARCHAR(20) NOT NULL UNIQUE,
    type VARCHAR(255),
    year_manufacture YEAR,
    num_pilots INT,
    num_cabin_crew INT,
    passenger_capacity INT,
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS flight (
    ID VARCHAR(20) NOT NULL,
    IATA_flight_no VARCHAR(20) NOT NULL,
    plane_ID VARCHAR(20) NOT NULL,
    airport_dep_ID VARCHAR(3) NOT NULL,
    airport_arr_ID VARCHAR(3) NOT NULL,
    pilot_ID VARCHAR(20) NOT NULL,
    first_officer_ID VARCHAR(20),
    date_dep_scheduled DATETIME NOT NULL,
    date_arr_scheduled DATETIME NOT NULL,
    FOREIGN KEY (plane_ID) REFERENCES plane(ID),
    FOREIGN KEY (airport_dep_ID) REFERENCES airport(ID),
    FOREIGN KEY (airport_arr_ID) REFERENCES airport(ID),
    FOREIGN KEY (pilot_ID) REFERENCES staff(ID),
    FOREIGN KEY (first_officer_ID) REFERENCES staff(ID),
    PRIMARY KEY (ID)
    );


INSERT INTO staff VALUES ('STID001', 'Lancaster', 'Timothy', 'pilot');
INSERT INTO staff VALUES ('STID002', 'Aitchison', 'Alastair', 'pilot');
INSERT INTO staff VALUES ('STID003', 'Ogden', 'Nigel', 'cabin crew');
INSERT INTO staff VALUES ('STID004', 'Dubois', 'Marc', 'pilot');
INSERT INTO staff VALUES ('STID005', 'Robert', 'David', 'pilot');
INSERT INTO staff VALUES ('STID006', 'Bonin', 'Pierre-Cedric', 'pilot');
INSERT INTO staff VALUES ('STID007', 'Danilov', 'Andrey', 'pilot');
INSERT INTO staff VALUES ('STID008', 'Piskaryov', 'Igor', 'pilot');
INSERT INTO staff VALUES ('STID009', 'Kudrinsky', 'Yaroslav', 'pilot');
INSERT INTO staff VALUES ('STID010', 'Sullenberger', 'Chelsey', 'pilot');
INSERT INTO staff VALUES ('STID011', 'Skiles', 'Jeffrey', 'pilot');

INSERT INTO airport VALUES ('APID001', 'BIR', 'Birmingham Airport', 'Birmingham', 'UK', 'Europe', 1);
INSERT INTO airport VALUES ('APID002', 'MAL', 'Malaga Airport', 'Malaga', 'Spain', 'Europe', 1);
INSERT INTO airport VALUES ('APID003', 'GIG', 'Galeão International Airport', 'Rio de Janeiro', 'Brazil', 'South America', 2);
INSERT INTO airport VALUES ('APID004', 'CDG', 'Charles de Gaulle Airport', 'Paris', 'France', 'Europe', 1);
INSERT INTO airport VALUES ('APID005', 'SVO', 'Sheremetyevo International Airport', 'Moscow', 'Russia', 'Europe', 1);
INSERT INTO airport VALUES ('APID006', 'HKG', 'Kai Tak International Airport', 'Kowloon', 'Hong Kong', 'Asia', 1);
INSERT INTO airport VALUES ('APID007', 'LGA', 'LaGuardia Airport', 'New York', 'USA', 'North America', 1);
INSERT INTO airport VALUES ('APID008', 'SEA', 'Seattle-Tacoma International Airport', 'Seattle', 'USA', 'North America', 1);

INSERT INTO airport_status VALUES (1, 'open');
INSERT INTO airport_status VALUES (2, 'open: alert');
INSERT INTO airport_status VALUES (3, 'closed');

INSERT INTO plane VALUES ('PLID001', 'G-BJRT', 'BAC One-Eleven 528FL', 1971, 2, 4, 81);
INSERT INTO plane VALUES ('PLID002', 'F-GZCP', 'Airbus A330-203', 2005, 3, 9, 216);
INSERT INTO plane VALUES ('PLID003', 'F-OGQS', 'Airbus A310-304', 1992, 3, 9, 63);
INSERT INTO plane VALUES ('PLID004', 'N106US', 'Airbus A320-214', 1984, 2, 3, 150);

INSERT INTO flight VALUES ('FLID001', 'BA5390', 'PLID001', 'BIR', 'MAL', 'STID001', 'STID002', '1990-06-10 07:20:00', '1990-06-10 10:15:00');
INSERT INTO flight VALUES ('FLID002', 'AFR447', 'PLID002', 'GIG', 'CDG', 'STID004', 'STID005', '2009-05-31 22:29:00', '2009-05-31 09:03:00');
INSERT INTO flight VALUES ('FLID003', 'AFL593', 'PLID003', 'SVO', 'HKG', 'STID007', 'STID008', '1994-03-22 10:39:00', '1994-05-31 00:46:00');
INSERT INTO flight VALUES ('FLID004', 'US1549', 'PLID004', 'LGA', 'SEA', 'STID010', 'STID011', '2009-01-15 20:24:56', '2009-02-15 01:44:00');

CREATE VIEW IF NOT EXISTS view_all_flights AS
SELECT 
    f.IATA_flight_no,
    pl.IATA_reg,
    f.airport_dep_ID,
    DATE(f.date_dep_scheduled),
    TIME(f.date_dep_scheduled),
    f.airport_arr_ID,
    DATE(f.date_arr_scheduled),
    TIME(f.date_arr_scheduled),
    pt.surname,
    fo.surname
FROM flight as f
LEFT JOIN plane AS pl ON pl.ID=f.plane_ID
LEFT JOIN staff AS pt ON pt.ID=f.pilot_ID 
LEFT JOIN staff AS fo ON fo.ID=f.first_officer_ID;

CREATE VIEW IF NOT EXISTS view_all_airports AS
SELECT 
    a.IATA_code,
    a.name,
    a.city,
    a.country,
    a.continent,
    st.status_desc
FROM airport as a
LEFT JOIN airport_status AS st ON st.ID=a.airport_status;

CREATE VIEW IF NOT EXISTS view_all_staff AS
SELECT 
    s.ID,
    s.surname,
    s.forename,
    s.role
FROM staff as s;


