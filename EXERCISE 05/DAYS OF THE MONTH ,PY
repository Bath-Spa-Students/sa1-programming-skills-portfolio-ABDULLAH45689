def is_leap_year(year):
    """Check if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year):
    """Return the number of days in a given month and year."""
    
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    
    if month == 2 and is_leap_year(year):
        return 29

    
    return month_days.get(month, None)

def get_valid_input(prompt, valid_range):
    """Get a valid input from the user within a specified range."""
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_range:
                return user_input
            else:
                print(f"Please enter password")
