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

def handle_error(e, file_path):
    print(f"--> ❗ ISSUE IN {os.path.basename(file_path)}.")
    print(f"--> ❌ PROBLEM: {e}")