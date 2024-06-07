'''
The Shopping List Maker

Objective:
The aim of this assignment is to create a program that helps users make a shopping list.

'''

# Task 1: Write a function that lets the user add items to a list
def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f'{item} has been added to the list.')

# Task 2: Include a feature to remove items from the list 
def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'{item} has been removed from the list.')
    else:
        print(f'{item} is not in the list.')

# Task 3: Add a function that prints out the entire list in a formatted way
def print_list(shopping_list):
    if shopping_list:
        print("Your shopping list:")
        for index, item in enumerate(shopping_list, start=1):
            print(f'{index}. {item}')
    else:
        print("Your shopping list is empty")

def shopping_list_maker():
    shopping_list = []
    while True:
        print("\nOptions")
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Exiting the program. Goodbye! ")
            break
        else: 
            print("Invalid choice. Please select a valid option.")

# Run the shopping list maker program
shopping_list_maker()
