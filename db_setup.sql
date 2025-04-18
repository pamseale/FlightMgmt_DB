CREATE TABLE IF NOT EXISTS staff (ID VARCHAR(20) NOT NULL, surname VARCHAR(20) NOT NULL, forename VARCHAR(20) NOT NULL, role VARCHAR(4), availability VARCHAR(4), license_ID VARCHAR(20), PRIMARY KEY (ID));
CREATE TABLE IF NOT EXISTS airport (ID VARCHAR(3) NOT NULL, city VARCHAR(255), country VARCHAR(255), continent VARCHAR(255), airport_status VARCHAR(20), PRIMARY KEY (ID));
CREATE TABLE IF NOT EXISTS airport_status (ID VARCHAR(4) NOT NULL, airport_status VARCHAR(20) NOT NULL, PRIMARY KEY (ID));
CREATE TABLE IF NOT EXISTS plane (ID VARCHAR(6) NOT NULL, make VARCHAR(255), model VARCHAR(255), manufacturer VARCHAR(255), plane_status VARCHAR(20), capacity INT, cabin_crew_size INT, current_location VARCHAR(3), FOREIGN KEY (current_location) REFERENCES airport(ID), PRIMARY KEY (ID));

INSERT INTO staff VALUES ('STID000001', 'Bloggs', 'Joe', 'PL1', 'AVID01', 'AV027639');
INSERT INTO staff VALUES ('STID000002', 'Bloggs', 'Alex', 'PL1', 'AVID01', 'AV027639');
INSERT INTO staff VALUES ('STID000003', 'Bloggs', 'Amy', 'PL1', 'AVID01', 'AV027639');
INSERT INTO staff VALUES ('STID000004', 'Bloggs', 'Xan', 'PL1', 'AVID01', 'AV027639');

INSERT INTO airport (ID, city, country, continent, airport_status) VALUES ('EDI', 'Edinburgh', 'UK', 'Europe', 'ASID01');
INSERT INTO airport (ID, city, country, continent, airport_status) VALUES ('LON', 'London', 'UK', 'Europe', 'ASID01');
INSERT INTO airport (ID, city, country, continent, airport_status) VALUES ('MUN', 'Munich', 'Germany', 'Europe', 'ASID02');

INSERT INTO airport_status VALUES ('ASID01', 'open');
INSERT INTO airport_status VALUES ('ASID02', 'closed');
INSERT INTO airport_status VALUES ('ASID03', 'warning in place');
