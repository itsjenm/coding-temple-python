'''
The Grade Analyzer

Objective:
The aim of this assignment is to analyze a set of grades and provide statistics.

'''


# Task 1: Code a function to calculate the average grade.
def grade_calculator(grade_list):
    average = 0
    for grade in grade_list:
        average = sum(grade_list) / len(grade_list)
    print(f'The grade list average is {round(average, 2)}%')

# Task 2: Implement a function to find the highest and lowest grade. 
def highest_grade(grade_list):
    highest = 0
    for grade in grade_list:
        highest = max(grade_list)
    print(f'{highest} is the highest grade in the list')

def lowest_grade(grade_list):
    lowest = 0
    for grade in grade_list:
        lowest = min(grade_list)
    print(f'{lowest} is the lowest grade in the list')

# Run the tests
grade_calculator([40, 70, 75, 80, 90, 100])
highest_grade([40, 70, 75, 80, 90, 100])
lowest_grade([40, 70, 75, 80, 90, 100])