'''

Nested Decision: The adventure Game

'''


# Task 1: Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == 'cross a river':
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    # Task 2: Setting the scene
    action = input("light a torch or proceed in the dark? ")
    if action == 'light a torch':
        print("You woke the bats!")
    elif action == 'proceed in the dark':
        print('You found diamonds!')
    else:
        pass
    # Task 3: Default Path
elif place != 'forest' or 'cave':
    pass









