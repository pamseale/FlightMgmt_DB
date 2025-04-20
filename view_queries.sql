-- view_flights
SELECT 
    f.ID,
    f.plane_ID,
    f.airport_dep_ID,
    f.airport_arr_ID,
    p.surname AS pilot,
    fo.surname AS first_officer, 
    rc.surname AS relief_captain 
FROM flight as f 
INNER JOIN staff as p ON p.ID=f.pilot_ID 
INNER JOIN staff as fo ON fo.ID=f.first_officer_ID 
INNER JOIN staff as rc ON rc.ID=f.relief_captain_ID;

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