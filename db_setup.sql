DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS license_status;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS airport_status;
DROP TABLE IF EXISTS plane;
DROP TABLE IF EXISTS flight;
DROP VIEW IF EXISTS flight_view;


CREATE TABLE IF NOT EXISTS staff (
    ID VARCHAR(20) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    forename VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL,
    license_ID VARCHAR(20),
    license_status VARCHAR(20),
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS license_status (
    ID VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS airport (
    ID VARCHAR(3) NOT NULL,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    continent VARCHAR(255) NOT NULL,
    airport_status_ID VARCHAR(20) NOT NULL,
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS airport_status (
    status VARCHAR(20) NOT NULL,
    PRIMARY KEY (status)
    );

CREATE TABLE IF NOT EXISTS plane (
    ID VARCHAR(20) NOT NULL,
    type VARCHAR(255),
    year_manufacture YEAR,
    num_pilots INT,
    num_cabin_crew INT,
    passenger_capacity INT,
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS flight (
    ID VARCHAR(20) NOT NULL,
    plane_ID VARCHAR(20) NOT NULL,
    airport_dep_ID VARCHAR(3) NOT NULL,
    airport_arr_ID VARCHAR(3) NOT NULL,
    pilot_ID VARCHAR(20) NOT NULL,
    first_officer_ID VARCHAR(20),
    relief_captain_ID VARCHAR(20),
    date_dep_scheduled DATETIME NOT NULL,
    date_arr_scheduled DATETIME NOT NULL,
    date_dep_actual DATETIME,
    date_arr_actual DATETIME,
    FOREIGN KEY (plane_ID) REFERENCES plane(ID),
    FOREIGN KEY (airport_dep_ID) REFERENCES airport(ID),
    FOREIGN KEY (airport_arr_ID) REFERENCES airport(ID),
    FOREIGN KEY (pilot_ID) REFERENCES staff(ID),
    FOREIGN KEY (first_officer_ID) REFERENCES staff(ID),
    FOREIGN KEY (relief_captain_ID) REFERENCES staff(ID),
    PRIMARY KEY (ID)
    );


INSERT INTO staff VALUES ('STID0001', 'Lancaster', 'Timothy', 'pilot', 'AV027691', 'current');
INSERT INTO staff VALUES ('STID0002', 'Aitchison', 'Alastair', 'pilot', 'AV512944', 'current');
INSERT INTO staff VALUES ('STID0003', 'Ogden', 'Nigel', 'cabin crew', NULL, NULL);
INSERT INTO staff VALUES ('STID0004', 'Dubois', 'Marc', 'pilot', 'AV107369', 'current');
INSERT INTO staff VALUES ('STID0005', 'Robert', 'David', 'pilot', 'AV969312', 'current');
INSERT INTO staff VALUES ('STID0006', 'Bonin', 'Pierre-Cedric', 'pilot', 'AV295581', 'current');
INSERT INTO staff VALUES ('STID0007', 'Danilov', 'Andrey', 'pilot', 'AV853011', 'current');
INSERT INTO staff VALUES ('STID0008', 'Piskaryov', 'Igor', 'pilot', 'AV669301', 'current');
INSERT INTO staff VALUES ('STID0009', 'Kudrinsky', 'Yaroslav', 'pilot', 'AV208218', 'current');

INSERT INTO airport VALUES ('BIR', 'Birmingham Airport', 'Birmingham', 'UK', 'Europe', 'open');
INSERT INTO airport VALUES ('MAL', 'Malaga Airport', 'Malaga', 'Spain', 'Europe', 'open');
INSERT INTO airport VALUES ('GIG', 'Galeão International Airport', 'Rio de Janeiro', 'Brazil', 'South America', 'open');
INSERT INTO airport VALUES ('CDG', 'Charles de Gaulle Airport', 'Paris', 'France', 'Europe', 'open');
INSERT INTO airport VALUES ('SVO', 'Sheremetyevo International Airport', 'Moscow', 'Russia', 'Europe', 'open');
INSERT INTO airport VALUES ('HKG', 'Kai Tak International Airport', 'Kowloon', 'Hong Kong', 'Asia', 'open');

INSERT INTO airport_status VALUES ('open');
INSERT INTO airport_status VALUES ('closed');
INSERT INTO airport_status VALUES ('warning in place');

INSERT INTO plane VALUES ('G-BJRT', 'BAC One-Eleven 528FL', 1971, 2, 4, 81);
INSERT INTO plane VALUES ('F-GZCP', 'Airbus A330-203', 2005, 3, 9, 216);
INSERT INTO plane VALUES ('F-OGQS', 'Airbus A310-304', 1992, 3, 9, 63);

INSERT INTO flight VALUES ('BA5390', 'G-BJRT', 'BIR', 'MAL', 'STID0001', 'STID0002', NULL, '1990-06-10 07:20:00', '1990-06-10 10:15:00', '1990-06-10 07:20:00', '1990-06-10 08:55:00');
INSERT INTO flight VALUES ('AFR447', 'F-GZCP', 'GIG', 'CDG', 'STID0004', 'STID0005', NULL, '2009-05-31 22:29:00', '2009-05-31 09:03:00', '2009-05-31 22:29:00', '2009-05-31 09:03:00');
INSERT INTO flight VALUES ('AFL593', 'F-OGQS', 'SVO', 'HKG', 'STID0007', 'STID0008', 'STID0009', '1994-03-22 10:39:00', '1994-05-31 00:46:00', '1994-03-22 10:39:00', '1994-05-31 00:46:00');

CREATE VIEW IF NOT EXISTS flight_view AS SELECT * FROM flight;