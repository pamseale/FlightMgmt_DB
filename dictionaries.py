flight_dict = {
    "table_name": "flight",
    "display_headers":["No.", "Flight no.", "Plane", "Dep", "Dep Date", "Dep time", "Arr", "Arr Date", "Arr time", "Pilot", "First Officer", "Relief Captain"],
    "actual_headers":["plane_ID", "airport_dep_ID", "date_dep_scheduled", "airport_arr_ID", "date_arr_scheduled", "pilot_ID", "first_officer_ID", "relief_captain_ID"],
    "amend_options":["1. Departure time", "2. Arrival time"],
    "query_names": ["view_all_flights", "view_flights_by_pilot"]
}

staff_dict = {
    "table_name": "staff",
    "display_headers":["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"],
    "actual_headers":["ID", "surname", "forname", "role", "license_ID", "license_status"],
    "amend_options": [ "1. Surname", "2. Forename", "3. Role" ],
    "query_names": ["view_staff", "view_pilots"]
}

airport_dict = {
    "table_name": "airport",
    "display_headers":["No.", "Code", "Name", "City", "Country", "Continent", "Status"],
    "actual_headers":["ID", "name", "city", "country", "continent", "status"],
    "amend_options": [ "1. Name", "2. Status" ],
    "query_names": ["view_airports"]
}