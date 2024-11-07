def get_valid_age():
    """Helper function to ensure age is entered as a valid integer."""
    while True:
        try:
            return int(input("Enter your age: "))  
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")

def get_user_info():
    """Collect user information including name, town and age."""
    name = input("Enter your name: ")
    hometown = input("Enter your hometown: ")
    age = get_valid_age()  

    
    return {
        "name": name,
        "hometown": town
        "age": age
    }

def display_user_info(user_info):
    """Display the user information."""
    print("\nYour Information:")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")


user_info = get_user_info()
display_user_info(user_info)
