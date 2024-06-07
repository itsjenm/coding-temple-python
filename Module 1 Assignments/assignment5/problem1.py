'''
The Calculator App

Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

'''

# Task 1: Create functions for each arithmetic operation 


def addition(num1, num2):
    result = num1 + num2
    print(result)

def subtraction(num1, num2):
    result = num1 - num2
    print(result)

def multiplication(num1, num2):
    result = num1 * num2
    print(result)

def division(num1, num2):
    # Task 3: Ensure your program can handle division by zero and other potential errors.
    if num2 == 0: 
        print('you cannot divide by zero, pick another number')
        return
    result = num1 / num2
    print(result)
    

        

# Task 2: Implement user input to receive numbers and an operation choice
operation_choice = input("What operation do you want to use? (addition/multiplication/subtraction/division) ")

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

if operation_choice == 'addition':
    addition(num1, num2)
elif operation_choice == 'multiplication':
    multiplication(num1, num2)
elif operation_choice == 'subtraction':
    subtraction(num1, num2)
elif operation_choice == 'division':
    division(num1, num2)
