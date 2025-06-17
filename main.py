import sqlite3
import utils
import create, insert, get, update

try:
    options = {
        "table": ("New empty table will be created", lambda: create.create_table(connection=conn, cursor=curr)),
        "select": ("Filter and retrieve existing records", lambda: get.get_records(cursor=curr)),
        "insert": ("Insert new record with few options into the table", lambda: insert.insert_record(connection=conn, cursor=curr)),
        "update": ("Update existing record value", lambda: update.update_record(connection=conn, cursor=curr)),
        "q": ("Exit the program", None)
    }
    menu_options = {key: desc for key, (desc, _) in options.items()}

    # "help" option added
    options["help"] = ("See available commands", lambda: utils.display_menu(title="MAIN MENU", options=menu_options))
    menu_options["help"] = "See available commands"


    conn = sqlite3.connect("data/database.db")
    curr = conn.cursor()
    print("--> 🟢 CONNECTION CREATED\n")
    
    while True:
        command = input(": ").strip().lower()
        if command in options:
            if command == 'q':
                break
            action = options[command][1]
            action()
except Exception as e:
    utils.handle_error(e, __file__)

conn.close()
print("\n--> 🔴 CONNECTION CLOSED")
