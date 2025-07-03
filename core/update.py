import common.utils as utils
import common.validator as validator

update_schema = """ UPDATE everything
                    SET {setting_col} = ?, updated_at = ?
                    WHERE {whering_col} = ?;
                """


def update_record(connection, cursor):
    try:
        utils.display_menu(title="", options={}, show_legend=True)

        changing_column = utils.user_input(
            prompt="Updating column ▶ ",
            use_lower=True,
            mandatory=True,
            validation_func=validator.validate_column_name,
            validation_args=(cursor, False),
            with_symbols=True
        )
        changed_value = utils.user_input(
            prompt="Updated value ▶ ",
            mandatory=True,
            validation_func=validator.validate_integer_type,
            validation_args=(changing_column,),
            with_symbols=True
        )
        searching_column = utils.user_input(
            prompt="Searching column ▶ ",
            use_lower=True,
            mandatory=True,
            validation_func=validator.validate_column_name,
            validation_args=(cursor, True),
            with_symbols=True
        )
        searched_value = utils.user_input(
            prompt="Searching value ▶ ",
            mandatory=True,
            validation_func=validator.validate_integer_type,
            validation_args=(searching_column,),
            with_symbols=True
        )
        

        records_found = utils.records_exist(
            cursor=cursor,
            where_col=searching_column, 
            where_val=searched_value
        )
        if not records_found:
            print("-> 🔍 NO RECORD(S) TO UPDATE\n")
            return

        cursor.execute(
            update_schema.format(
                setting_col=changing_column,
                whering_col=searching_column
            ),
            (changed_value, utils.get_date_time_format(type="both"), searched_value)
        )
        connection.commit()
        print("-> ✅ RECORD(S) UPDATED\n")
    
    except ValueError as ve:
        if "returning" in str(ve):
            print()
            return
        print(f"--> ❌ PROBLEM: {ve}")
    except Exception as e:
        print(f"--> ❌ PROBLEM: {e}")
        print("-> ⚠️ RECORD(S) NOT UPDATED\n")
        connection.rollback()
