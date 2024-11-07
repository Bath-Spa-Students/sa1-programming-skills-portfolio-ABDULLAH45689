# Initialize list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Let the user input the term to search
name_search = input("Enter the name you want to search for: ")

# Search term in list
if name_search in names:
    print(f"{name_search} is in the list.")
else:
    print(f"{name_search} is not in the list.")