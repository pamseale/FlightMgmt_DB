-- view_all_fs
CREATE VIEW IF NOT EXISTS view_all_fs AS
SELECT
    ID  AS 'Flight no.',
    plane_ID AS 'Plane',
    airport_dep_ID AS 'Dep',
    airport_arr_ID AS 'Arr',
    pilot_ID AS 'Pilot',
    first_officer_ID AS 'FO'
FROM flight;