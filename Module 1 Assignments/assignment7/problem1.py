'''
Exceptional Weather Forecast

Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application 
that gracefully handles unexpected user input and provides user-friendly error messages.

'''

# Task 1: Start

# TODO: Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.
# TODO: Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.

user_input = input("Enter the temperature in Fahrenheit: ")

def get_temperature(temperature):
    while True:
        try:
            temperature = float(user_input)
            print(f"The temperature you entered is {temperature}F.")
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for the temperature")

# Run the program
get_temperature(user_input)


# Task 2: Temperature Conversion

# TODO: Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9
# TODO: Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

def temp_conversion(temperature):
    try:
        celsius_temp = (temperature - 32) * 5/9
        print(f"The temperature in celsius is {celsius_temp}")
        return celsius_temp
    except (ZeroDivisionError, OverflowError) as e:
        print("Error occured during conversion: {e}")
        return None
    
# Run the program
temp_conversion(int(user_input))