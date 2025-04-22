-- view_all_flights
SELECT 
    f.ID,
    f.plane_ID,
    f.airport_dep_ID,
    f.airport_arr_ID,
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
    f.airport_arr_ID,
    p.surname AS pilot,
    fo.surname AS first_officer, 
    rc.surname AS relief_captain 
FROM flight as f 
LEFT JOIN staff as p ON p.ID=f.pilot_ID 
LEFT JOIN staff as fo ON fo.ID=f.first_officer_ID 
LEFT JOIN staff as rc ON rc.ID=f.relief_captain_ID
WHERE p.ID = ?;

-- view_flights_by_dep_aiport
SELECT 
    f.ID,
    f.plane_ID,
    f.airport_dep_ID,
    f.airport_arr_ID,
    p.surname AS pilot,
    fo.surname AS first_officer, 
    rc.surname AS relief_captain 
FROM flight as f 
LEFT JOIN staff as p ON p.ID=f.pilot_ID 
LEFT JOIN staff as fo ON fo.ID=f.first_officer_ID 
LEFT JOIN staff as rc ON rc.ID=f.relief_captain_ID
WHERE airport_dep_ID = ?;

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
