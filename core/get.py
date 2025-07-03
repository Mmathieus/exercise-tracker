from tabulate import tabulate
import common.utils as utils
import common.validator as validator


def get_records(cursor):
    select_schema = "SELECT * FROM everything"
    where_clauses, parameters = [], []

    try:
        first_choices = {'0': "No", '1': "Yes"}
        utils.display_menu(title="FILTER RECORDS?", options=first_choices)

        filtering_choice = utils.user_input(
            prompt="Filter ▶ ",
            validation_func=validator.validate_selected_choice,
            validation_args=(first_choices,)
        )

        if filtering_choice == '1':
            second_choices = {'1' : "Exercise", '2' : "Date", '3' : "Exercise & Date"}
            utils.display_menu(
                title="SELECT COLUMN(S)",
                options=second_choices,
                show_legend=True
            )
            
            filtering_column_choice = utils.user_input(
                prompt="Column ▶ ",
                validation_func=validator.validate_selected_choice,
                validation_args=(second_choices,)
            )

            if filtering_column_choice in ('1','3'):
                exercise_choice = utils.user_input(
                    prompt="Exercise ▶ ",
                    mandatory=True,
                    with_symbols=True
                )
                parameters.append(exercise_choice)
                where_clauses.append("exercise = ?")
            
            if filtering_column_choice in ('2','3'):
                date_choice = utils.user_input(
                    prompt="Date (YYYY-MM-DD) ▶ ",
                    mandatory=True,
                    validation_func=validator.validate_date_format,
                    with_symbols=True
                )
                parameters.append(date_choice)
                where_clauses.append("date = ?")
            
            if parameters != []:
                select_schema += " WHERE " + " AND ".join(where_clauses)
        
        select_schema += ";"
            
        cursor.execute(select_schema, parameters)
        
        records = cursor.fetchall()
        if records == []:
            print("-> ℹ️ NO RECORDS\n")
            return

        print(
            tabulate(
                tabular_data=records,
                headers=[desc[0] for desc in cursor.description],
                tablefmt="psql",
                stralign="center",
                numalign="center"
            ), '\n'
        )
    
    except ValueError as ve:
        if "returning" in str(ve):
            print()
            return
        print(f"--> ❌ PROBLEM: {ve}")
    except Exception as e:
        print(f"--> ❌ PROBLEM: {e}")
        print("-> ⚠️ RECORDS NOT RETRIEVED\n")