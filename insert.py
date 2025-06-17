import utils

full_insert = """ INSERT INTO everything (exercise, actual_reps, target_reps, date, time, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?); """

partial_insert = """ INSERT INTO everything (exercise, target_reps, date, time, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?); """


def get_info_from_user(type):
    date = input("date (YYYY-MM-DD): ").strip() or "unknown" if type == "partial" else None
    time = input("time (HH:MM:SS) (optional): ").strip() or None if type == "partial" else None
    exercise = input("exercise: ").strip() or "unknown"
    reps = input("actual reps: ").strip() or None if type == "full" else None
    reps_expected = input("target reps (optional): ").strip() or None

                    #! FULL                                                       # PARTIAL
    return (exercise, reps, reps_expected) if type == "full" else (exercise, reps_expected, date, time)
    

def insert_record(connection, cursor):
    try:
        utils.display_menu("INSERT RECORD MENU", {"1": "Full (exercise done!)", "0": "Partial (exercise in future)"})
        if not (choice := input("choice: ")): return
        
        if choice == '1':
            values = get_info_from_user(type="full")
            other_values = (utils.get_date_time_format(type="date"),
                            utils.get_date_time_format(type="time"),
                            utils.get_date_time_format(type="both"), 
                            utils.get_date_time_format(type="both"))
        
        elif choice == '2':
            values = get_info_from_user(type="partial")
            other_values = (utils.get_date_time_format(type="both"), utils.get_date_time_format(type="both"))

        cursor.execute(full_insert if choice == '1' else partial_insert, values + other_values)
        connection.commit()
        print("-> ✅ RECORD INSERTED\n")
    except Exception as e:
        print("-> ⚠️ RECORD NOT INSERTED")
        connection.rollback()
        utils.handle_error(e, __file__)