from tabulate import tabulate
import utils


def get_records(cursor):
    select_schema = """SELECT * FROM everything"""
    where_clauses = []
    parameters = []

    try:
        utils.display_menu("FILTER RECORDS?", {"1": "Yes", "0": "No"})
        if not (specific := input("choice: ").strip().lower()): return

        if specific == '1':
            utils.display_menu("COLUMNS FILTER", {"1" : "Exercise", "2" : "Date", "3" : "Exercise & Date"})
            if not (column_choice := input("filter choice: ").strip()): return
            
            if column_choice not in "123":
                print("INVALID OPTION.\n")
                return
            if column_choice in "13":
                if not (exercise_choice := input("exercise: ").strip()): return
                parameters.append(exercise_choice)
                where_clauses.append("""exercise = ?""")
            if column_choice in "23":
                if not (date_choice := input("date (YYYY-MM-DD): ").strip()): return
                parameters.append(date_choice)
                where_clauses.append("""date = ?""")
            
            if parameters != []:
                select_schema += " WHERE " + " AND ".join(where_clauses)
        
        select_schema += ";"
            
        cursor.execute(select_schema, parameters)
        
        records = cursor.fetchall()
        if records == []:
            print("-> ℹ️ NO RECORDS\n")
            return

        print(tabulate(records, headers=[desc[0] for desc in cursor.description], tablefmt="psql", stralign="center", numalign="center"))
    except Exception as e:
        print("-> ⚠️ RECORDS NOT RETRIEVED")
        utils.handle_error(e, __file__)