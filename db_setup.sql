DROP TABLE IF EXISTS flight;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS airport_status;
DROP TABLE IF EXISTS plane;
DROP TABLE IF EXISTS pilot;

DROP VIEW IF EXISTS view_all_flights;
DROP VIEW IF EXISTS view_all_airports;
DROP VIEW IF EXISTS view_all_pilots;


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
    FOREIGN KEY (pilot_ID) REFERENCES pilot(ID),
    FOREIGN KEY (first_officer_ID) REFERENCES pilot(ID),
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS airport (
    ID VARCHAR(20) NOT NULL,
    IATA_code  VARCHAR(3) NOT NULL,
    airport_name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    continent VARCHAR(255) NOT NULL,
    status INT NOT NULL,
    FOREIGN KEY (status) REFERENCES airport(ID),
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

CREATE TABLE IF NOT EXISTS pilot (
    ID VARCHAR(20) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    forename VARCHAR(255) NOT NULL,
    PRIMARY KEY (ID)
    );

INSERT INTO flight VALUES ('FLID001', 'US1549', 'PLID001', 'LGA', 'SEA', 'STID001', 'STID002', '2025-06-10 07:20:00', '2025-06-10 08:30:00');
INSERT INTO flight VALUES ('FLID002', 'AFR447', 'PLID002', 'GIG', 'CDG', 'STID003', 'STID004', '2025-06-11 22:29:00', '2025-06-12 09:03:00');
INSERT INTO flight VALUES ('FLID003', 'MH370', 'PLID003', 'KUL', 'PEK', 'STID005', 'STID006', '2025-06-15 00:30:00', '2025-06-15 06:55:00');
INSERT INTO flight VALUES ('FLID004', '4U9525', 'PLID004', 'BCN', 'DUS', 'STID007', 'STID008', '2025-07-01 10:00:00', '2025-07-01 11:30:00');
INSERT INTO flight VALUES ('FLID005', 'JT610', 'PLID005', 'CGK', 'PGK', 'STID009', 'STID010', '2025-07-15 06:20:00', '2025-07-15 06:33:00');
INSERT INTO flight VALUES ('FLID006', 'UA232', 'PLID006', 'DEN', 'SUX', 'STID011', 'STID012', '2025-07-20 14:09:00', '2025-07-20 16:00:00');
INSERT INTO flight VALUES ('FLID007', 'AA1234', 'PLID001', 'LGA', 'SEA', 'STID001', 'STID002', '2025-06-10 15:30:00', '2025-06-10 18:30:00');
INSERT INTO flight VALUES ('FLID008', 'AFR123', 'PLID002', 'CDG', 'SEA', 'STID003', 'STID004', '2025-06-10 23:00:00', '2025-06-11 10:15:00');
INSERT INTO flight VALUES ('FLID009', 'MH999', 'PLID003', 'KUL', 'SEA', 'STID005', 'STID006', '2025-06-10 08:00:00', '2025-06-10 15:00:00');
INSERT INTO flight VALUES ('FLID010', 'UA5678', 'PLID004', 'DUS', 'BCN', 'STID007', 'STID008', '2025-06-12 12:45:00', '2025-06-12 14:00:00');
INSERT INTO flight VALUES ('FLID011', 'JT123', 'PLID005', 'CGK', 'PGK', 'STID009', 'STID010', '2025-07-05 06:00:00', '2025-07-05 06:20:00');
INSERT INTO flight VALUES ('FLID012', 'UA777', 'PLID006', 'DEN', 'SUX', 'STID011', 'STID012', '2025-07-05 12:30:00', '2025-07-05 13:45:00');
INSERT INTO flight VALUES ('FLID013', 'BA5390', 'PLID005', 'BIR', 'MAL', 'STID003', 'STID006', '2025-06-10 07:20:00', '2025-06-10 10:15:00');


INSERT INTO airport VALUES ('APID001', 'LGA', 'LaGuardia Airport', 'New York City', 'USA', 'North America', 1);
INSERT INTO airport VALUES ('APID002', 'SEA', 'Seattle Tacoma International Airport', 'Seattle', 'USA', 'North America', 1);
INSERT INTO airport VALUES ('APID003', 'GIG', 'Rio de Janeiro Galeão International Airport', 'Rio de Janeiro', 'Brazil', 'South America', 1);
INSERT INTO airport VALUES ('APID004', 'CDG', 'Charles de Gaulle Airport', 'Paris', 'France', 'Europe', 2);
INSERT INTO airport VALUES ('APID005', 'KUL', 'Kuala Lumpur International Airport', 'Kuala Lumpur', 'Malaysia', 'Asia', 1);
INSERT INTO airport VALUES ('APID006', 'PEK', 'Beijing Capital International Airport', 'Beijing', 'China', 'Asia', 3);
INSERT INTO airport VALUES ('APID007', 'BCN', 'Barcelona El Prat Airport', 'Barcelona', 'Spain', 'Europe', 1);
INSERT INTO airport VALUES ('APID008', 'DUS', 'Düsseldorf Airport', 'Düsseldorf', 'Germany', 'Europe', 1);
INSERT INTO airport VALUES ('APID009', 'CGK', 'Soekarno Hatta International Airport', 'Jakarta', 'Indonesia', 'Asia', 1);
INSERT INTO airport VALUES ('APID010', 'PGK', 'Depati Amir Airport', 'Pangkal Pinang', 'Indonesia', 'Asia', 3);
INSERT INTO airport VALUES ('APID011', 'DEN', 'Denver International Airport', 'Denver', 'USA', 'North America', 1);
INSERT INTO airport VALUES ('APID012', 'SUX', 'Sioux Gateway Airport', 'Sioux City', 'USA', 'North America', 1);
INSERT INTO airport VALUES ('APID013', 'BIR', 'Birmingham Airport', 'Birmingham', 'UK', 'Europe', 1);
INSERT INTO airport VALUES ('APID014', 'MAL', 'Malaga Airport', 'Malaga', 'Spain', 'Europe', 1);

INSERT INTO airport_status VALUES (1, 'open');
INSERT INTO airport_status VALUES (2, 'open: alert');
INSERT INTO airport_status VALUES (3, 'closed');

INSERT INTO plane VALUES ('PLID001', 'N106US', 'Airbus A320-214', 1984, 2, 3, 150); -- US Airways Flight 1549 (Airbus A320)
INSERT INTO plane VALUES ('PLID002', 'F-GZCP', 'Airbus A330-203', 2005, 3, 9, 216); -- Air France Flight 447 (Airbus A330)
INSERT INTO plane VALUES ('PLID003', '9M-MRO', 'Boeing 777-200ER', 1997, 3, 10, 282); -- Malaysia Airlines Flight MH370 (Boeing 777)
INSERT INTO plane VALUES ('PLID004', 'D-AIPX', 'Airbus A320-211', 1990, 2, 4, 150); -- Germanwings Flight 9525 (Airbus A320)
INSERT INTO plane VALUES ('PLID005', 'PK-LQP', 'Boeing 737-8U3', 2015, 2, 3, 189); -- Lion Air Flight 610 (Boeing 737 Max)
INSERT INTO plane VALUES ('PLID006', 'N181UA', 'McDonnell Douglas DC-10-10', 1970, 3, 6, 270); -- United Airlines Flight 232 (McDonnell Douglas DC-10)
INSERT INTO plane VALUES ('PLID007', 'G-BGJL', 'Boeing 737-436', 1989, 2, 2, 148); -- Boeing 737-400 (used for BA5390)

INSERT INTO pilot VALUES ('STID001', 'Sullenberger', 'Chesley'); -- US Airways Flight 1549 (Captain)
INSERT INTO pilot VALUES ('STID002', 'Skiles', 'Jeffrey'); -- US Airways Flight 1549 (First Officer)
INSERT INTO pilot VALUES ('STID003', 'Chavarria', 'Marc'); -- Air France Flight 447 (Captain)
INSERT INTO pilot VALUES ('STID004', 'Pinto', 'David'); -- Air France Flight 447 (First Officer)
INSERT INTO pilot VALUES ('STID005', 'Zaharie', 'Shah'); -- Malaysia Airlines Flight MH370 (Captain)
INSERT INTO pilot VALUES ('STID006', 'Fariq', 'Abdul'); -- Malaysia Airlines Flight MH370 (First Officer)
INSERT INTO pilot VALUES ('STID007', 'Lubitz', 'Andreas'); -- Germanwings Flight 9525 (Co-pilot)
INSERT INTO pilot VALUES ('STID008', 'Wunderlich', 'Patrick'); -- Germanwings Flight 9525 (Captain)
INSERT INTO pilot VALUES ('STID009', 'Sari', 'Raimond'); -- Lion Air Flight 610 (Captain)
INSERT INTO pilot VALUES ('STID010', 'Supriatna', 'Hanafi'); -- Lion Air Flight 610 (First Officer)
INSERT INTO pilot VALUES ('STID011', 'McDaniel', 'Dennis'); -- United Airlines Flight 232 (Captain)
INSERT INTO pilot VALUES ('STID012', 'Campbell', 'Michael'); -- United Airlines Flight 232 (First Officer)
INSERT INTO pilot VALUES ('STID013', 'Lancaster', 'Timothy'); -- Captain Timothy Lancaster
INSERT INTO pilot VALUES ('STID014', 'Atchison', 'Alastair'); -- First Officer Alastair Atchison

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
LEFT JOIN pilot AS pt ON pt.ID=f.pilot_ID 
LEFT JOIN pilot AS fo ON fo.ID=f.first_officer_ID
ORDER BY DATE(f.date_dep_scheduled);

CREATE VIEW IF NOT EXISTS view_all_airports AS
SELECT 
    a.IATA_code,
    a.airport_name,
    a.city,
    a.country,
    a.continent,
    st.status_desc
FROM airport as a
LEFT JOIN airport_status AS st ON st.ID=a.status
ORDER BY a.IATA_code;

CREATE VIEW IF NOT EXISTS view_all_pilots AS
SELECT * FROM pilot
ORDER BY ID;


