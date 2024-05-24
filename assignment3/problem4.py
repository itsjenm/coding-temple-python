'''
Deep Dive into Python Lists

Objective:
The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

Problem Statement:
You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

'''

# TODO Task 1: Given the lists: Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

filtered_students = [(student, grade, activity) for student, grade, activity in zip(students, grades, activities) if grade < 80]
print(filtered_students)

# TODO Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]
students_approved = [student for student, grade in zip(students, grades) if grade >= 80]

# TODO Task 3: Print the list students_approved
print(students_approved)