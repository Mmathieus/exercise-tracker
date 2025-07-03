import common.utils as utils
import common.validator as validator

delete_schema = "DELETE FROM everything WHERE {column} = ?;"


def delete_record(connection, cursor):
    try:
        utils.display_menu(title="", options={}, show_legend=True)

        column = utils.user_input(
            prompt="Searching column ▶ ",
            use_lower=True,
            mandatory=True,
            validation_func=validator.validate_column_name,
            validation_args=(cursor, True),
            with_symbols=True
        )
        value = utils.user_input(
            prompt="Searching value ▶ ",
            mandatory=True,
            with_symbols=True
        )

        if not utils.records_exist(cursor=cursor, where_col=column, where_val=value):
            print("-> 🔍 NO RECORD(S) TO DELETE\n")
            return
        
        cursor.execute(delete_schema.format(column=column), (value,))
        connection.commit()
        print("-> ✅ RECORD(S) DELETED\n")
    
    except ValueError as ve:
        if "returning" in str(ve):
            print()
            return
        print(f"--> ❌ PROBLEM: {ve}")
    except Exception as e:
        print(f"--> ❌ PROBLEM: {e}")
        print("-> ⚠️ RECORD(S) NOT DELETED\n")
        connection.rollback()