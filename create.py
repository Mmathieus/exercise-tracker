import utils
 
table_schema = """
    DROP TABLE IF EXISTS everything;
    CREATE TABLE everything (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exercise TEXT NOT NULL,
        actual_reps INTEGER,
        target_reps INTEGER,
        date TEXT NOT NULL,
        time TEXT,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    );
"""

def create_table(connection, cursor):
    try:
        choice = input("--> ⚠️ EXISTING DATA WILL BE LOST!\nproceed [y/n]? ").strip().lower()
        if choice != 'y': return
        cursor.executescript(table_schema)
        connection.commit()
        print("-> ✅ TABLE (RE)CREATED\n")
    except Exception as e:
        print("-> ⚠️ TABLE NOT (RE)CREATED")
        connection.rollback()
        utils.handle_error(e, __file__)