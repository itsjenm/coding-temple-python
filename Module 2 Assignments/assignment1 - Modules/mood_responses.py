'''
Python Modules and Data Handling Assignment

Task 1: Your Mood Today

Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today 
and responds with a custom message based on the mood entered.

'''

def mood_response(mood):
    mood.lower()
    if mood == "happy":
        return "You will have a great day today!"
    elif mood == "sad":
        return 'You sound like you need a big hug!'
    elif mood == "excited":
        return "I knew you could do it!"

