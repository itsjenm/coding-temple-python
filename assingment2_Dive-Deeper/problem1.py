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
