import common.utils as utils
import common.validator as validator

insert_schema = "INSERT INTO everything VALUES (NULL, ?, ?, ?, ?, ?, ?, ?);"

def get_insert_info(type_of_insert):
    exercise, reps, reps_expected, date, time = None, None, None, None, None

    exercise = utils.user_input(prompt="Exercise ▶ ", mandatory=True, with_symbols=True)

    if type_of_insert in ('1', '2'):
        reps = utils.user_input(
            prompt="Reps (done) ▶ ",
            mandatory=True,
            validation_func=validator.validate_integer_type,
            with_symbols=True
        )
    
    reps_expected = utils.user_input(
        prompt="Reps (target) ▶ ",
        validation_func=validator.validate_integer_type,
        return_to_main=False,
        with_symbols=True
    )

    if type_of_insert in ('1', '3'):
        date = utils.user_input(
            prompt="Date (YYYY-MM-DD) ▶ ",
            mandatory=True,
            validation_func=validator.validate_date_format,
            with_symbols=True
        )
        time = utils.user_input(
            prompt="Time (HH:MM:SS) ▶",
            validation_func=validator.validate_time_format,
            return_to_main=False,
            with_symbols=True
        )
    
    if type_of_insert == '2':
        date = utils.get_date_time_format(type="date")
        time = utils.get_date_time_format(type="time")

    current_TMSTMP = utils.get_date_time_format(type="both")

    return (exercise, reps, reps_expected, date, time, current_TMSTMP, current_TMSTMP)


def insert_record(connection, cursor):
    try:
        first_choice_dict = {
            '1': "Exercise from the past",
            '2': "Just completed exercise",
            '3': "Upcoming exercise"
        }
        utils.display_menu("SELECT INSERT", first_choice_dict, show_legend=True)
        
        insert_type = utils.user_input(
            prompt="Insert ▶ ",
            validation_func=validator.validate_selected_choice,
            validation_args=(first_choice_dict,)
        )
        
        values = get_insert_info(type_of_insert=insert_type)

        cursor.execute(insert_schema, values)
        connection.commit()
        print("-> ✅ RECORD INSERTED\n")
    
    except ValueError as ve:
        if "returning" in str(ve):
            print()
            return
        print(f"--> ❌ PROBLEM: {ve}")
    except Exception as e:
        print(f"--> ❌ PROBLEM: {e}")
        print("-> ⚠️ RECORD NOT INSERTED\n")
        connection.rollback()