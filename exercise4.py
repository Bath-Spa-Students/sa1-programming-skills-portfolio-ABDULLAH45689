## Exercise 4: Primitive Quiz - 30 Marks

#In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.3. If the answer is incorrect, the program should print a message saying the answer is wrong.


country = input("what is the capital of france:")
if country == "Paris":
    print("answer is correct")
else:
    print("answer is wrong")

### Advanced Requirements:
#Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
#Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.

country = input("What is the capital of France? ")
if country.lower() == "paris":
    print("Answer is correct!")
else:
    print("Answer is wrong.")


country = input("What is the capital of ENGLAND? ")
if country.lower() == "london":
    print("Answer is correct!")
else:
    print("Answer is wrong.")

country = input("What is the capital of germany? ")
if country.lower() == "berlin":
    print("Answer is correct!")
else:
    print("Answer is wrong.")

country = input("What is the capital of ITALY? ")
if country.lower() == "rome":
    print("Answer is correct!")
else:
    print("Answer is wrong.")

country = input("What is the capital of GREECE? ")
if country.lower() == "athens":
    print("Answer is correct!")
else:
    print("Answer is wrong.")  

country = input("What is the capital of SPAIN? ")
if country.lower() == "madrid":
    print("Answer is correct!")
else:
    print("Answer is wrong.")

country = input("What is the capital of IRELAND? ")
if country.lower() == "dublin":
    print("Answer is correct!")
else:
    print("Answer is wrong.")

country = input("What is the capital of RUSSIA? ")
if country.lower() == "moscow":
    print("Answer is correct!")
else:
    print("Answer is wrong.")

country = input("What is the capital of NORWAY? ")
if country.lower() == "oslo":
    print("Answer is correct!")
else:
    print("Answer is wrong.")

country = input("What is the capital of BULGARIA? ")
if country.lower() == "sofia":
    print("Answer is correct!")
else:
    print("Answer is wrong.")