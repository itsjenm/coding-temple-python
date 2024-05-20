'''
Decisions at the Crossroad
Task 1: Code Correction

You are provided with a Python script that uses conditional statements to 
tell if a number is positive, negative, or zero, but it has some errors. 
Identify and fix them.

'''

# Buggy code:

# number = input("Enter a number: ")

# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

# corrected code:

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


'''

The Greatest Showdown

Objective: Harness the power of conditional statements to compare and determine values.

Task 1: Identify the Greatest 

Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.

Task 2: Identify the smallest

Extend your program from Task 1 to also determine the smallest number among the three and print it out.

Task 3: Equality Check

Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".

'''

# Task 1

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))


# Identifying the greatest number
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print("Greatest number:", greatest)

# Task 2: Identify the smallest
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print("Smallest number:", smallest)

# Task 3: Equality Check
if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("There are two numbers equal to each other.")
else:
    print("All numbers are different.")


'''
Leap Year Explorer

Task 1: Leap Year Checker

Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

'''

# Task 1

year = int(input("Enter a year: "))

if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print(year, "is a leap year!")
else:
    print("Not a leap year!")