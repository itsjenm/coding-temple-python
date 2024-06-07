'''
User Input Data Processor

Objective:
The aim of this assignment is to process and format user input data.j

'''

# Task 1: Input Length Validator 

# Write a script that checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

def input_length_validator(first_name, last_name):
    if len(first_name) < 2:
        print("Error: Your first name has to be at least 2 characters long")
    elif len(last_name) < 2:
        print("Error: Your last name needs to be at least 2 characters long")
    elif len(first_name) >= 2 and len(last_name) >= 2:
        print("Name is valid.")


# Test
first_name = input("Enter your first name: ")
last_name = input("Enter you last name: ")
input_length_validator(first_name, last_name)


# Task 2: Password Complexity Checker

# Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. 
# If the password does not meet these criteria, print a message explaining the complexity requirements.

def password_checker(password): 
    if len(password) < 8:
        print("Error: Your passwords must be at least 8 chracters long")
        return
    
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)

    if not has_uppercase:
        print("Password must have at least one uppercase letter")
    elif not has_lowercase:
        print("Password must contain at least one lowercase letter")
    elif not has_number:
        print("Password must contain at least one number")
    else: 
        print("Password is valid")


# Test 
password = input("Enter a password: ")
password_checker(password)


# Task 3: Email Formatter

# Implement a script that ensures all user email addresses are in a standard format

def email_checker(email):
    if email.count('@') == 1:
        if email.count('.') == 1 and email[-4] == '.':
            print("Email is valid")
        else:
            print("Invalid email address: must contain '.' extension.")
    else:
        print("Invalid email address: must contain at least one '@'")

email = input("Enter your email address: ")
email_checker(email)
