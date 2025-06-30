import utils

delete_schema = "DELETE FROM everything WHERE {column} = ?;"


def delete_record(connection, cursor):
    try:
        if not (column := input("Column: ").strip().lower()): return
        value = input("Value: ").strip()

        if not utils.validate_column_choice(cursor=cursor, column_to_validate=column, everything=True):
            print("-> INVALID COLUMN OR COLUMN'S NAME.\n")
            return

        if not utils.records_exist(cursor=cursor, col=column, val=value):
            print("-> NO RECORD(S) TO DELETE.\n")
            return
        
        cursor.execute(delete_schema.format(column=column), (value,))
        connection.commit()
        print("-> ✅ RECORD(S) DELETED\n")
    except Exception as e:
        print("-> ⚠️ RECORD(S) NOT DELETED")
        utils.handle_error(e, __file__)