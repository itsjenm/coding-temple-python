'''
Advanced List Methods and Identity Operators

Objective:
The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

Problem Statement:
You have two lists of student names. One list contains 
the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

'''

# TODO Task 1: Given the two lists: Find out which students both submitted their assignments and attended the class
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

common_students = [student for student in submitted if student in attended]
print(common_students)
# TODO Task 2: Check if the two lists are identical in terms of their content, regardless of order.
submitted.sort()
attended.sort() 

are_identical = submitted == attended
print(are_identical)

# TODO Task 3: Using list methods, remove any student from the attended list who did not submit their assignment
attended.remove("Eve")
attended.remove("Frank")
print(attended)

