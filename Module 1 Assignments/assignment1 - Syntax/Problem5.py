'''
Problem 5: Understanding Assignments and Comparisons

Objective: Get a grasp on how assignment operators work and how to compare
values using comparison operators

    Task 1: Value Swapping
    - swap the values of two given numbers using assignment operators (=)
    and then comparing them to ensure they have been swapped

'''

num1 = 7
num2 = 5
num1, num2 = num2, num1

is_swapped = num1 == 5 and num2 == 7
print(is_swapped)

