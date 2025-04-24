import sqlite3


def execute_sql_file(filename, database):
    # read .sql file
    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()
    # create db connection
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    # execute .sql file script
    cursor.executescript(sql_script)
    # commit chnages
    conn.commit()
    # close db connection
    conn.close()


def load_query_from_file(file_path, target_query):
    # read query file
    with open(file_path, "r") as file:
        content = file.read()
    # split file in sections at each comment(-- query_name)
    sections = content.split('-- ')
    for query in sections:
        # if correct query
        if query.startswith(target_query):
            # return query name
            return query[len(target_query):].strip()
    # error message if query not found
    raise ValueError(f"Query {target_query} not found.")
