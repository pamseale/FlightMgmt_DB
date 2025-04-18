DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS license_status;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS airport_status;
DROP TABLE IF EXISTS plane;
DROP TABLE IF EXISTS flight;


CREATE TABLE IF NOT EXISTS staff (
    ID VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    forename VARCHAR(20) NOT NULL,
    role VARCHAR(20),
    license_ID VARCHAR(20),
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS license_status (
    ID VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS airport (
    ID VARCHAR(3) NOT NULL,
    city VARCHAR(255),
    country VARCHAR(255),
    continent VARCHAR(255),
    airport_status_ID VARCHAR(6),
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
    plane_status VARCHAR(20),
    capacity INT,
    cabin_crew_size INT,
    PRIMARY KEY (ID)
    );

CREATE TABLE IF NOT EXISTS flight (
    ID VARCHAR(6) NOT NULL,
    plane_ID VARCHAR(20),
    airport_dep_ID VARCHAR(3),
    airport_arr_ID VARCHAR(3),
    pilot_ID VARCHAR(20),
    copilot_ID VARCHAR(20),
    date_dep_scheduled DATETIME,
    date_arr_scheduled DATETIME,
    date_dep_actual DATETIME,
    date_arr_actual DATETIME,
    FOREIGN KEY (plane_ID) REFERENCES plane(ID),
    FOREIGN KEY (airport_dep_ID) REFERENCES airport(ID),
    FOREIGN KEY (airport_arr_ID) REFERENCES airport(ID),
    FOREIGN KEY (pilot_ID) REFERENCES staff(ID),
    FOREIGN KEY (copilot_ID) REFERENCES staff(ID),
    PRIMARY KEY (ID)
    );


INSERT INTO staff VALUES ('STID0001', 'Lancaster', 'Timothy', 'pilot', 'AV02769');
INSERT INTO staff VALUES ('STID0002', 'Aitchison', 'Alastair', 'pilot', 'AV51294');
INSERT INTO staff (ID, surname, forename, role ) VALUES ('STID0003', 'Ogden', 'Nigel', 'cabin crew');


INSERT INTO airport VALUES ('BIR', 'Birmingham', 'UK', 'Europe', 'open');
INSERT INTO airport VALUES ('MAL', 'Malaga', 'Spain', 'Europe', 'open');

INSERT INTO airport_status VALUES ('open');
INSERT INTO airport_status VALUES ('closed');
INSERT INTO airport_status VALUES ('warning in place');

INSERT INTO license_status VALUES ('AV02769', 'current');
INSERT INTO license_status VALUES ('AV51294', 'current');

INSERT INTO plane VALUES ('G-BJRT', 'BAC One-Eleven 528FL', 1971, 'repair', 87, 4);

INSERT INTO flight VALUES ('BA5390', 'G-BJRT', 'BIR', 'MAL', 'STID0001', 'STID0002', '1990-06-10 07:20:00', '1990-06-10 10:15:00', '1990-06-10 07:20:00', '1990-06-10 08:55:00');

