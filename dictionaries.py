flight_dict = {
    "table_name": "flight",
    "display_headers":["No.", "Flight no.", "Plane", "Dep", "Dep Date", "Dep time", "Arr", "Arr Date", "Arr time", "Pilot in Command", "First Officer"],
    "actual_headers":["plane_ID", "airport_dep_ID", "date_dep_scheduled", "airport_arr_ID", "date_arr_scheduled", "pilot_ID", "first_officer_ID", "relief_captain_ID"],
    "amend_options":["1. Departure time", "2. Arrival time"],
    "amend_actual":["date_dep_scheduled", "date_dep_scheduled"],
    "query_names": ["SELECT * FROM view_all_flights"]
}

staff_dict = {
    "table_name": "staff",
    "display_headers":["No.", "Staff ID", "Surname", "Forname", "Role"],
    "actual_headers":["ID", "surname", "forname", "role"],
    "amend_options": [ "1. Surname", "2. Forename", "3. Role" ],
    "amend_actual":["surname", "forename", "role"],
    "query_names": ["SELECT * FROM view_all_staff"]
}

airport_dict = {
    "table_name": "airport",
    "display_headers":["No.", "IATA Code", "Name", "City", "Country", "Continent", "Status"],
    "actual_headers":["ID", "name", "city", "country", "continent", "status"],
    "amend_options": [ "1. Name", "2. Status" ],
    "amend_actual":["name", "status"],
    "query_names": ["SELECT * FROM view_all_airports"]
}