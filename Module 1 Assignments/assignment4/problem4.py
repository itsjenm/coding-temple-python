'''
Python's Random Game Night

Objective:
The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.

Task 1: Random Choice Game
Create a game where a player has a list of items. They have to guess which item in the list was selected. 
Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.

'''

import random 

player_items = ["sword", "machete", "bat", 'rifle']

item_guess = input("Guess which item in the list was selected: ")
picked_item = random.choice(player_items)
guesses = 1

if item_guess == picked_item:
    print("Wow, you guessed it on the first try! Nice job!")

while item_guess != picked_item:
    guesses += 1
    item_guess = input("guess again: ")
    if item_guess == picked_item:
        print(f"You guessed correctly after {guesses} tries! The item is {item_guess}")
    
    
