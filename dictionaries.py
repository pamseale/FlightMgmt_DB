flight_dict = {
    "table_name": "flight",
    "display_headers":["No.", "Flight no.", "Plane", "Dep", "Arr", "Pilot", "First Officer", "Relief Captain", "Departure (sch.)", "Arrival (sch.)", "Departure (act.)", "Arrival (act)"],
    "actual_headers":["plane_ID", "airport_dep_ID", "airport_arr_ID", "pilot_ID", "first_officer_ID", "relief_captain_ID", "date_dep_scheduled", "date_arr_scheduled", "date_dep_actual", "date_dep_actual"],
    "amend_options":["1. Plane", "2. Departure airport", "3. Arrival airport", "4. Pilot", "5. First Officer", "6. Relief Captain", "7. Scheduled departure date/time", "8. Scheduled arrival date/time", "9. Actual departure date/time", "10. Actual arrival date/time"],
    "query_names": ["view_all_flights", "view_flights_by_pilot"]
}

"""    "amend_options": [  {'display': "1. Plane", 'col': "plane_ID"},
                        {'display': "2. Departure airport", 'col': "airport_dep_ID"},
                        {'display': "3. Arrival airport", 'col': "airport_arr_ID"},
                        {'display': "4. Pilot", 'col': "pilot_ID"},
                        {'display': "5. First Officer", 'col': "first_officer_ID"},
                        {'display': "6. Relief Captain", 'col': "relief_captain_ID"},
                        {'display': "7. Scheduled departure date/time", 'col': "date_dep_scheduled"},
                        {'display': "8. Scheduled arrival date/time", 'col': "date_arr_scheduled"},
                        {'display': "9. Actual departure date/time", 'col': "date_dep_actual"},
                        {'display': "10. Actual arrival date/time", 'col': "date_dep_actual"} ],"""
staff_dict = {
    "table_name": "staff",
    "col_headers":["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"],
    "amend_options": [  {'display': "1. Surname", 'col': "surname"},
                        {'display': "2. Forename", 'col': "forename"},
                        {'display': "3. Role", 'col': "role"} ],
    "query_names": ["view_staff"]
}

airport_dict = {
    "table_name": "airport",
    "col_headers":["No.", "Code", "Name", "City", "Country", "Continent", "Status"],
    "amend_options": [  {'display': "1. Name", 'col': "name"},
                        {'display': "2. Status", 'col': "status"} ],
    "query_names": ["view_airports"]
}