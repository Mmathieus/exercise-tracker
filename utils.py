import os
from datetime import datetime

def display_menu(title, options):
    print(f"\n--- {title} ---")
    max_width = max(len(f"[{key}]") for key in options.keys()) + 1
    for key, value in options.items():
        key_part = f"[{key}]"
        print(f"{key_part:<{max_width}}- {value}")
    print()

def get_date_time_format(type):
    if type == "date":
        return datetime.now().strftime("%Y-%m-%d")
    elif type == "time":
        return datetime.now().strftime("%H:%M:%S")
    else:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
def validate_column_choice(cursor, column_to_validate, everything):
    cursor.execute("PRAGMA table_info(everything)")
    table_columns = [row[1] for row in cursor.fetchall()]
    if not everything:
        excluded = ["id", "created_at", "updated_at"]
        table_columns = [col for col in table_columns if col not in excluded]
    return column_to_validate in table_columns
    
def records_exist(cursor, col, val):
    count_sql = f"SELECT COUNT(*) FROM everything WHERE {col} = ?;"
    cursor.execute(count_sql, (val,))
    records_to_delete = cursor.fetchone()[0]
    return records_to_delete > 0

def handle_error(e, file_path):
    print(f"--> ❗ ISSUE IN {os.path.basename(file_path)}.")
    print(f"--> ❌ PROBLEM: {e}")