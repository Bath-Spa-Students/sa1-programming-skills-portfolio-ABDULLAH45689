# Initialize list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Let the user input the NAME to search
SEARCH_NAMES = input("Enter the name you want to search for: ")

# Search NAME in list
if SEARCH_NAMES in names:
    print(f"{SEARCH_NAMES} is in the list.")
else:
    print(f"{SEARCH_NAMES}  not in the list.")
