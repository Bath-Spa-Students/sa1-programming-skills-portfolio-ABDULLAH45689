# this is the  password
password = "12345"

# total  attempts
tottal_atemps = 5

# num of attempts beginning
attempts = 0

# While loop to continiusly ask for the password
while attempts < tottal_atemps:
    # Ask the user to input the password
    entered_password = input("Enter the password: ")
    
    # Check if the entered password is correct
    if entered_password == password:
        print("Password correct! Access granted.")
        break
    else:
        # plus 1 to the attempts counter
        attempts += 1
        # Inform the user of the remaining attempts
        remaining_attempts = tottal_atemps - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Incorrect password. You have reached the maximum attempts. Authorities have been alerted.")
           
