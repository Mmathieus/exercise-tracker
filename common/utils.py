from datetime import datetime

def display_menu(title, options, show_legend=False):
    if options:
        print(f"\n╭─── {title} ───")
        
        max_width = max(len(f"[{key}]") for key in options.keys()) + 2
        for key, value in options.items():
            key_part = f"[{key}]"
            print(f"│ {key_part:<{max_width}}» {value}")
    
    if show_legend:
        if options:
            print("│")
            print("│─── Info ───")
        else:
            print("╭─── Info ───")
        
        print("│ ⭐  Required field")
        print("│ ⚪  Optional field")
    
    print()

def get_date_time_format(type):
    formats = {
        "date": "%Y-%m-%d",
        "time": "%H:%M:%S",
        "both": "%Y-%m-%d %H:%M:%S"
    }
    return datetime.now().strftime(formats.get(type, "%Y-%m-%d %H:%M:%S"))

def user_input(prompt, use_lower=False, mandatory=False,
               validation_func=None, validation_args=(),
               return_to_main=True, with_symbols=False):
    
    def get_input_value(prompt, use_lower, mandatory, with_symbols):
        symbol = ''
        if with_symbols:
            symbol = '⭐' if mandatory else '⚪'
        
        value = input(f"{symbol} {prompt}").strip()
        return value.lower() if use_lower else value
    
    while True:
        value = get_input_value(
            prompt=prompt,
            use_lower=use_lower,
            mandatory=mandatory,
            with_symbols=with_symbols
        )

        # Quit to main
        if value == "qq":
            raise ValueError("returning")
        
        # Empty input
        if not value:
            # Mandatory = asking again for input...
            if mandatory:
                continue
            # Optional input; Returning to main OR Assigning None and continuing
            if return_to_main:
                raise ValueError("returning")
            return None
        
        # Input has to be validated
        if validation_func:
            try:
                validation_func(value, validation_args)
            # Input is not validated, therefore asking for it again...
            except ValueError as ve:
                print(f"--> ❌ PROBLEM: {ve}")
                continue
        
        return value

def records_exist(cursor, where_col, where_val):
    cursor.execute(
        f"SELECT COUNT(*) FROM everything WHERE {where_col} = ?;",
        (where_val,)
    )
    records_to_delete = cursor.fetchone()[0]
    return records_to_delete > 0
