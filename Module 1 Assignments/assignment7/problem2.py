'''
The Recipe Ratio Adjuster

Objective: The aim of this assignment is to create a program that adjusts the quantities of a recipe based on the number of servings, 
handling any type of arithmetic errors or user input exceptions.

'''

# Task 1: Start

# TODO: Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.
# TODO: Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

def get_servings():
    while True:
        try:
            original_servings = int(input("Enter the number of servings the recipe is originally for: "))
            desired_servings = int(input("Enter the number of servings you wish to make: "))
            if original_servings <= 0 or desired_servings <= 0:
                print("Servings must be positive numbers. Please try again.")
                continue
            return original_servings, desired_servings
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Example usage
original_servings, desired_servings = get_servings()
# print(f"Original servings: {original_servings}, Desired servings: {desired_servings}")

# Task 2: Quantity Calculation

# TODO: Calculate the adjustment factor by dividing the desired servings by the original servings.
# TODO: Use a try block to catch any arithmetic errors that may occur during the calculation.

def quantity_calculation(original, desired):
    try:
        adjustment = desired / original
        print(f"The adjustment factor is {adjustment}")
        return adjustment
    except ZeroDivisionError:
        print("Error: The original number of servings cannot be zero")
        return None

adjustment_factor = quantity_calculation(original_servings, desired_servings)

# Task 3: Serving Success 

# TODO: If the calculation is successful, display the adjusted recipe quantities to the user.
# TODO: Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

def display_adjusted_recipe(adjustment_factor, recipe):
    adjusted_recipe = {}
    for ingredient, quantity in recipe.items():
        adjusted_recipe[ingredient] = quantity * adjustment_factor
        
    print("Adjusted recipe quantities:")
    for ingredient, quantity in adjusted_recipe.items():    
        print(f"{ingredient}: {quantity:.2f}")


# Test 
recipe = {
    "cups of flour": 2,
    "cup of sugar": 1,
    "cup of butter": 0.5
}

display_adjusted_recipe(adjustment_factor, recipe)
