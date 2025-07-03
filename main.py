import sqlite3
import common.utils as utils
import core.create as create
import core.get as get
import core.insert as insert
import core.update as update
import core.delete as delete

try:
    options = {
        "table": (
            "New empty table will be created",
            lambda: create.create_table(connection=conn, cursor=curr)
        ),
        "select": (
            "Filter and retrieve existing records",
            lambda: get.get_records(cursor=curr)
        ),
        "insert": (
            "Insert new record with few options into the table",
            lambda: insert.insert_record(connection=conn, cursor=curr)
        ),
        "update": (
            "Update existing record value",
            lambda: update.update_record(connection=conn, cursor=curr)
        ),
        "delete": (
            "Delete existing record",
            lambda: delete.delete_record(connection=conn, cursor=curr)
        ),
        "q": ("Exit the program", None)
    }
    menu_options = {key: desc for key, (desc, _) in options.items()}

    # Add 'help' to option menu
    options["help"] = (
        "See available commands",
        lambda: utils.display_menu(title="MAIN MENU", options=menu_options)
    )
    menu_options["help"] = "See available commands"


    with sqlite3.connect("data/exercise.db") as conn:
        curr = conn.cursor()
        print("--> 🟢 CONNECTION CREATED\n")
        
        while True:
            try:
                command = input("➤ ").strip().lower()
                if command in options:
                    if command == 'q':
                        break
                    action = options[command][1]
                    action()
            
            except (KeyboardInterrupt, EOFError):
                print()
                break
            
except Exception as e:
    print(f"--> ❌ PROBLEM: {e}")
finally:
    print("\n--> 🔴 CONNECTION CLOSED")
