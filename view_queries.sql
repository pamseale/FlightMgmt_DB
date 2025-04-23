-- view_all_flights
SELECT 
    f.ID,
    f.plane_ID,
    f.airport_dep_ID,
    DATE(f.date_dep_scheduled),
    TIME(f.date_dep_scheduled),
    f.airport_arr_ID,
    DATE(f.date_arr_scheduled),
    TIME(f.date_arr_scheduled),
    p.surname AS pilot,
    fo.surname AS first_officer, 
    rc.surname AS relief_captain 
FROM flight as f 
LEFT JOIN staff as p ON p.ID=f.pilot_ID 
LEFT JOIN staff as fo ON fo.ID=f.first_officer_ID 
LEFT JOIN staff as rc ON rc.ID=f.relief_captain_ID;

-- view_flights_by_pilot
SELECT 
    f.ID,
    f.plane_ID,
    f.airport_dep_ID,
    DATE(f.date_dep_scheduled) AS dep_date,
    TIME(f.date_dep_scheduled) AS dep_time,
    f.airport_arr_ID,
    DATE(f.date_dep_scheduled) AS arr_date,
    TIME(f.date_dep_scheduled) AS arr_time
FROM flight as f 
INNER JOIN staff as s ON s.ID=f.pilot_ID 
WHERE f.pilot_ID = ?;

-- view_flights_by_dep_aiport
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

-- view_flights_by_date
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

-- view_airports
SELECT 
    a.ID,
    a.name,
    a.city,
    a.country,
    a.continent,
    a.airport_status_ID
FROM airport as a;

-- view_staff
SELECT 
    s.ID,
    s.surname,
    s.forename,
    s.role,
    s.license_ID,
    s.license_status
FROM staff as s;

-- view_pilots
SELECT 
    s.ID,
    s.surname,
    s.forename,
    s.license_ID,
    s.license_status
FROM staff as s
WHERE s.role = 'pilot';

-- view_pilots_with_flights
SELECT 
    s.ID,
    s.surname,
    s.forename,
    s.role,
    s.license_ID,
    s.license_status
FROM staff as s
LEFT JOIN flight as f ON f.pilot_ID=s.ID
WHERE s.role = 'pilot';
