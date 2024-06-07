# Import the random module to generate random dice rolls
# Use a while loop to keep rolling the dice until the same number appears on both
# In each iteration, simulate rolling two dice
# Check if the two dice have the same number. If they do, exit the loop.
# Print out the result of each roll and a message when both dice match

import random

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice1: {dice1}, Dice 2: {dice2}")
    if dice1 == dice2:
        print(f"Both dice landed on {dice1}.")
        break