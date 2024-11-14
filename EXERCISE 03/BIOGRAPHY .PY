# Define variables for personal information
full_name = "abdullah"  # Full name as string
city = "Lahore"          # Hometown as string
years_old = 25            # Age as integer

# Store information in a dictionary with descriptive keys
personal_info = {
    "Full Name": full_name,  # Key "Full Name" with the value of full_name
    "City": city,            # Key "City" with the value of city
    "Age": years_old         # Key "Age" with the value of years_old
}

# Display the initial information
print(f"{personal_info['Full Name']}\n{personal_info['City']}\n{personal_info['Age']}")

# Prompt the user to enter their full name, removing any extra whitespace
user_full_name = input("Enter your full name: ").strip()  # .strip() Removes extra spaces around input

# Prompt the user to enter their city, removing any extra whitespace
user_city = input("Enter your city: ").strip()  # .strip() Removes extra spaces around input

# Prompt the user for their age in a loop to ensure valid input
while True:
    try:
        # Convert the input to an integer
        user_age = int(input("Enter your age: "))
        break  # Exit the loop if conversion is successful
    except ValueError:
        # Display an error if input is not a valid integer
        print("Invalid input. Please enter a numerical value for age.")

# Display the collected information
print("\nUser Information:")
print(f"Full Name: {user_full_name}")
print(f"City: {user_city}")
print(f"Age: {user_age}") 
