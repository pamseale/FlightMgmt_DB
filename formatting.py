
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
    """

    columns = list(zip(*rows)) if rows else [[] for _ in column_names]
    col_widths = [
        max(len(str(item)) if item is not None else 0 for item in list(col) + [header])
 #   col_widths = [
  #      max(len(str(item)) if item is not None else 0 for item in col + [header])
        for col, header in zip(columns, column_names)]"""
    return widths

# add padding to column headersß
def add_padding(col_widths):
    format_str = " | ".join(f"{{:<{width}}}" for width in col_widths)
    return format_str

def get_column_width(col, header):
    return max(len(str(item)) if item is not None else 0 for item in list(col) + [header])