'''
Quick Decisions: The Event Planner

'''

# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
print("large hall" if attendees > 100 else "conference room")

# Task 2: Venue selection
print("audio system" if attendees > 100 else "projector")

# Task 3: Catering choices
food = input("What is your food preference? (vegetarian/regular) ")
print("Veggie Delight Caterers" if food == 'vegetarian' else 'Gourmet Meals Caterers')