import utils

update_schema = "UPDATE everything SET {column_1} = ?, updated_at = ? WHERE {column_2} = ?;"

def get_changes_from_user():
    if not (set_column := input("Column to update: ").strip()): return None
    set_value = input("Updated value: ").strip()
    where_column = input("Key column: ").strip()
    where_value = input("Key value: ").strip()
    return (set_column, set_value, where_column, where_value)

def validate_columns_name(cursor, columns_to_validate):
    cursor.execute("PRAGMA table_info(everything)")
    table_columns = [row[1] for row in cursor.fetchall() if row[1] not in ["id", "created_at", "updated_at"]]
    return all(col in table_columns for col in columns_to_validate)
    

def update_record(connection, cursor):
    try:
        if (changes_specified := get_changes_from_user()) is None: return
        set_column, set_value, where_column, where_value = changes_specified
        if validate_columns_name(cursor=cursor, columns_to_validate=(set_column, where_column)) is not True:
            print("-> INVALID COLUMN(S) OR COLUMN(S) NAMES.\n")
            return
        cursor.execute(update_schema.format(column_1=set_column, column_2=where_column),
                       (set_value, utils.get_date_time_format(type="both"), where_value))
        connection.commit()
        print("-> ✅ RECORD UPDATED\n")
    except Exception as e:
        print("-> ⚠️ RECORD NOT UPDATED")
        utils.handle_error(e, __file__)
