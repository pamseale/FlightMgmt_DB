flight_dict = {
    "table_name": "flight",
    "display_headers":["No.", "Flight no.", "Plane Reg", "Dep", "Dep Date", "Dep time", "Arr", "Arr Date", "Arr time", "Pilot in Command", "First Officer"],
    "actual_headers":["plane_ID", "airport_dep_ID", "date_dep_scheduled", "airport_arr_ID", "date_arr_scheduled", "pilot_ID", "first_officer_ID", "relief_captain_ID"],
    "amend_options":["1. Departure time", "2. Arrival time"],
    "query_names": ["SELECT * FROM view_all_flights", "SELECT * FROM view_flights_by_pilot", "SELECT * FROM view_flights_by_pilot WHERE f.pilot_ID = ?", "SELECT * FROM view_flights_by_dep_aiport", "SELECT * FROM view_flights_by_date", "view_flights_by_pilot"]
}

staff_dict = {
    "table_name": "staff",
    "display_headers":["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"],
    "actual_headers":["ID", "surname", "forname", "role", "license_ID", "license_status"],
    "amend_options": [ "1. Surname", "2. Forename", "3. Role" ],
    "query_names": ["SELECT * FROM view_all_staff", "SELECT * FROM view_pilots", "SELECT * FROM view_pilots_with_flights"]
}

airport_dict = {
    "table_name": "airport",
    "display_headers":["No.", "IATA Code", "Name", "City", "Country", "Continent", "Status"],
    "actual_headers":["ID", "name", "city", "country", "continent", "status"],
    "amend_options": [ "1. Name", "2. Status" ],
    "query_names": ["SELECT * FROM view_all_airports"]
}