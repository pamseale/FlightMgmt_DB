def display_table(query_name, display_column_names):
    conn = sqlite3.connect('flight_management_database.db')
    cursor = conn.cursor()
    query = load_query("view_queries.sql", query_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    # add numbering to each row for user reference
    numbered_rows = [[i + 1] + list(row) for i, row in enumerate(rows)]

    # add padding to column widths by determining max width
    columns = list(zip(*numbered_rows)) if numbered_rows else [[] for _ in display_column_names]
    col_widths = [
        max(len(str(item)) if item is not None else 0 for item in col + (header,))
        for col, header in zip(columns, display_column_names)]
    format_str = " | ".join(f"{{:<{width}}}" for width in col_widths)

    # print column headings
    print(format_str.format(*display_column_names))
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    # allow for NULL value entries
    for row in numbered_rows:
        safe_row = [str(item) if item is not None else "" for item in row]
        print(format_str.format(*safe_row))
    conn.commit
    conn.close

def display_flights():
    print("\nAll flight information:\n")
    column_names = ["No.", "Flight no.", "Plane", "Dep", "Arr", "Pilot", "First Officer", "Relief Captain", "Departure (sch.)", "Arrival (sch.)", "Departure (act.)", "Arrival (act)"]
    display_table('view_flights', column_names)

def display_airports():
    print("\nAll airport information:\n")
    column_names = ["No.", "Code", "Name", "City", "Country", "Continent", "Status"]
    display_table('view_airports', column_names)

def display_staff():
    print("\nAll staff information:\n")
    column_names = ["No.", "Staff ID", "Surname", "Forname", "Role", "License no.", "License status"]
    display_table('view_staff', column_names)
