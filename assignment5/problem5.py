'''
The fitness tracker

Objective:
The aim of this assignment is to create a program that tracks fitness activities and calories burned.

'''

# Task 1: Develop a function to log different fitness activities and their duration. 
# For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, 
# Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

fitness_list = []

def fitness_log():
    activity = input("What type of activity would you like to log? ")
    duration = int(input("What is the activity duration in minutes? "))
    log_entry = (activity, duration)
    fitness_list.append(log_entry)
    print(f"Logged: {activity} for {duration} minutes")


# Task 2: Write a simple function that estimates calories burned based on the activity and duration. 
# For instance, Total calories burned = Duration (in minutes)*3.5
def calories_burned(activity, duration):
    calories_per_minute = 3.5
    total_calories = duration * calories_per_minute
    return total_calories
    

# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.
def fitness_summary():
    total_calories_burned = 0
    if fitness_list:
        print("Summary of today's fitness activities:")
        for activity, duration in fitness_list:
            calories = calories_burned(activity, duration)
            total_calories_burned += calories
            print(f"{activity} for {duration} minutes: {calories} calories burned")
        print(f"Total calories burned today: {total_calories_burned} calories")
    else: 
        print("No activities logged today.")

# Main function to run the fitness tracker program
def fitness_tracker():
    while True:
        print("\nOptions:")
        print("1. Log a new activity")
        print("2. View summary of activities and total calories burned")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            fitness_log()
        elif choice == '2':
            fitness_summary()
        elif choice == '3':
            print("Exiting the program. Stay fit!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the fitness tracker program
fitness_tracker()
