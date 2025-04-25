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
LEFT JOIN staff as s ON s.ID=f.pilot_ID
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
LEFT JOIN staff as p ON p.ID=f.pilot_ID 
LEFT JOIN staff as fo ON fo.ID=f.first_officer_ID 
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
LEFT JOIN staff as p ON p.ID=f.pilot_ID 
LEFT JOIN staff as fo ON fo.ID=f.first_officer_ID 
WHERE DATE(date_dep_scheduled) = ?;


-- view_pilots
SELECT 
    s.ID,
    s.surname,
    s.forename
FROM staff as s
WHERE s.role = 'pilot';

-- view_pilots_with_flights_assigned
SELECT 
    s.ID,
    s.surname,
    s.forename,
    s.role
FROM staff as s
INNER JOIN flight as f ON f.pilot_ID=s.ID
WHERE s.role = 'pilot';

-- get_last_record
SELECT ID,
FROM ?
ORDER BY ID DESC
LIMIT 1;