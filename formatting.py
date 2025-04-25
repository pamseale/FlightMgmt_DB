
# add numbering to each row
def add_numbering(rows):
    numbered_rows = [] # empty list
    for i, row in enumerate(rows):
        list_of_rows = list(row) # create a list from cursor.fetchall() command
        row_number = i+1 # starts at 1 instead of 0
        numbered_row = [row_number] + list_of_rows
        numbered_rows.append(numbered_row)
    return numbered_rows

# calculate padding for printing column headers
def calc_padding(rows, column_names):
    columns = list(zip(*rows)) if rows else [[] for _ in column_names]
    # Ensure each column is a list for safe concatenation with [header]
    widths = [
        max(len(str(item)) if item is not None else 0 for item in list(col) + [header])
        for col, header in zip(columns, column_names)
    ]
    return widths

# add padding to column headers
def add_padding(col_widths):
    format_str = " | ".join(f"{{:<{width}}}" for width in col_widths)
    return format_str

# get the maximum column width from a header
def get_column_width(col, header):
    return max(len(str(item)) if item is not None else 0 for item in list(col) + [header])

def format_and_print(dict, rows):
    numbered_rows = add_numbering(rows)
    col_widths = calc_padding(numbered_rows, dict['display_headers'])
    headers = add_padding(col_widths)
    print("\n")
    print(headers.format(*dict['display_headers']))
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    # allow for NULL value entries
    for row in numbered_rows:
        safe_row = [str(item) if item is not None else "" for item in row]
        print(headers.format(*safe_row))