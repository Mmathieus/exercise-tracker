from datetime import datetime

def validate_date_format(date, _):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")
    return True

def validate_time_format(time, _):
    try:
        datetime.strptime(time, "%H:%M:%S")
    except ValueError:
        raise ValueError("Invalid time format. Use HH:MM:SS")
    return True


def validate_integer_type(value, args):
    if args and args[0] not in {"id", "reps", "target_reps"}:
        return True
    try:
        if isinstance(int(value), int):
            return True
    except ValueError:
        raise ValueError("Number expected")


def validate_column_name(column_to_validate, args):
    cursor, with_every_column = args
    
    cursor.execute("PRAGMA table_info(everything)")
    table_columns = {row[1] for row in cursor.fetchall()}
    
    if not with_every_column:
        fixed_columns = {"id", "created_at", "updated_at"}
        table_columns -= fixed_columns
    
    if column_to_validate in table_columns:
        return True
    raise ValueError("Invalid column or column's name")

def validate_selected_choice(choice, args):
    dict_of_options, = args

    if choice not in dict_of_options:
        raise ValueError(f"Only {', '.join(dict_of_options.keys())} allowed")
    return True



