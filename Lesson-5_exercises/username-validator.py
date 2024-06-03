'''
Asks user to enter a username and then checks whether the username is valid


'''

while True:
    username = input("Enter your desidered username: ")

    if 5 <= len(username) <= 15:
        print("Username is valid!")
    else:
        print("Username needs to be between 5 and 15 characters long")
    
    continue_input = input("Do you want to try another username? (yes/no)").lower()
    if continue_input != 'yes':
        break
