import common.utils as utils
 
table_schema = """
    DROP TABLE IF EXISTS everything;
    CREATE TABLE everything (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exercise TEXT NOT NULL,
        reps INTEGER,
        target_reps INTEGER,
        date TEXT NOT NULL,
        time TEXT,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    );
"""


def create_table(connection, cursor) -> None:
    try:
        choice = utils.user_input(
            prompt="--> 🚨 EXISTING DATA WILL BE LOST!\nProceed [y/n]? ▶ ",
            use_lower=True
        )
        if choice != 'y':
            return
        
        cursor.executescript(table_schema)
        connection.commit()
        print("-> ✅ TABLE (RE)CREATED\n")
    
    except ValueError as ve:
        if "returning" in str(ve):
            print()
            return
        print(f"--> ❌ PROBLEM: {ve}")
    except Exception as e:
        print(f"--> ❌ PROBLEM: {e}")
        print("-> ⚠️ TABLE NOT (RE)CREATED\n")
        connection.rollback()
        