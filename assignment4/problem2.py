'''
Double Scoop with Nested Loops

Objective:
The aim of this assignment is to practice using nested loops in Python. 
You will correct a nested loop code snippet, simulate a mood tracker, and generate a multiplication table.

Task 1: Your Mood Tracker
Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. 
Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. 
For each time, randomly select a mood from a predefined list and print it.

'''

import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["morning", "afternooon", "evening"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

for i in range(len(days)):
    for time in times_of_day:
        print(f"On {days[i]} {time} you were {random.choice(moods)}")
