-- query_flights_by_pilot
SELECT 
    f.ID,
    f.plane_ID,
    f.airport_dep_ID,
    DATE(f.date_dep_scheduled) AS dep_date,
    TIME(f.date_dep_scheduled) AS dep_time,
    f.airport_arr_ID,
    DATE(f.date_arr_scheduled) AS arr_date,
    TIME(f.date_arr_scheduled) AS arr_time
FROM flight as f 
LEFT JOIN pilot as p ON p.ID=f.pilot_ID
WHERE f.pilot_ID = ?;


-- query_flights_by_dep_airport
SELECT 
    f.ID,
    f.plane_ID,
    f.airport_dep_ID,
    DATE(f.date_dep_scheduled) AS dep_date,
    TIME(f.date_dep_scheduled) AS dep_time,
    f.airport_arr_ID,
    DATE(f.date_dep_scheduled) AS arr_date,
    TIME(f.date_dep_scheduled) AS arr_time,
    p.surname AS pilot,
    fo.surname AS first_officer
FROM flight as f 
LEFT JOIN pilot as p ON p.ID=f.pilot_ID 
LEFT JOIN pilot as fo ON fo.ID=f.first_officer_ID 
WHERE airport_dep_ID = ?;

-- query_flights_by_date
SELECT 
    f.ID,
    f.plane_ID,
    f.airport_dep_ID,
    DATE(f.date_dep_scheduled) AS dep_date,
    TIME(f.date_dep_scheduled) AS dep_time,
    f.airport_arr_ID,
    DATE(f.date_dep_scheduled) AS arr_date,
    TIME(f.date_dep_scheduled) AS arr_time,
    p.surname AS pilot,
    fo.surname AS first_officer
FROM flight as f 
LEFT JOIN pilot as p ON p.ID=f.pilot_ID 
LEFT JOIN pilot as fo ON fo.ID=f.first_officer_ID 
WHERE DATE(date_dep_scheduled) = ?;


-- view_pilots
SELECT * FROM pilot;

-- view_pilots_with_flights_assigned
SELECT 
    p.ID,
    p.surname,
    p.forename
FROM pilot as p
INNER JOIN flight as f ON f.pilot_ID=p.ID

-- get_last_record
SELECT ID,
FROM ?
ORDER BY ID DESC
LIMIT 1;

-- count_flights_to_destinations
SELECT
    a.airport_name,
    COUNT(*) AS flight_count 
FROM flight AS f
LEFT JOIN airport AS a ON f.airport_arr_ID=a.IATA_code
GROUP BY f.airport_arr_ID
ORDER BY flight_count DESC;

-- count_flights_to_destinations_greater_1
SELECT
    a.airport_name,
    COUNT(*) AS flight_count
FROM flight AS f
LEFT JOIN airport AS a ON f.airport_arr_ID=a.IATA_code
GROUP BY f.airport_arr_ID
HAVING flight_count >1
ORDER BY flight_count DESC;
