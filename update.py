import utils

update_schema = "UPDATE everything SET {column_1} = ?, updated_at = ? WHERE {column_2} = ?;"

def get_changes_from_user():
    if not (set_column := input("Column to update: ").strip()): return None
    set_value = input("Updated value: ").strip()
    where_column = input("Key column: ").strip()
    where_value = input("Key value: ").strip()
    return (set_column, set_value, where_column, where_value)  


def update_record(connection, cursor):
    try:
        if (changes_specified := get_changes_from_user()) is None: return
        set_column, set_value, where_column, where_value = changes_specified
        
        if utils.validate_column_choice(cursor=cursor, column_to_validate=set_column, everything=False) is not True:
            print("-> INVALID 'setting' COLUMN OR COLUMN'S NAME.\n")
            return
        if utils.validate_column_choice(cursor=cursor, column_to_validate=where_column, everything=True) is not True:
            print("-> INVALID 'searching' COLUMN OR COLUMN'S NAME.\n")
            return
        
        if utils.records_exist(cursor=cursor, col=where_column, val=where_value) is not True:
            print("-> NO RECORD(S) TO UPDATE.\n")
            return

        cursor.execute(update_schema.format(column_1=set_column, column_2=where_column),
                       (set_value, utils.get_date_time_format(type="both"), where_value))
        connection.commit()
        print("-> ✅ RECORD(S) UPDATED\n")
    except Exception as e:
        print("-> ⚠️ RECORD(S) NOT UPDATED")
        utils.handle_error(e, __file__)
