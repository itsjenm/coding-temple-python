'''
Problem 6: Exploring Logical Operations and Precedence

Objective: Grasp the concept of logical operations and understand
how operator precedence can affect the outcome of an operation

    Task 1: Validating Calculations
    - Calculate the value of a particular arithmetic expression twice: once normally
    and once using parenthesis. Then compare the two results

'''
expression = 5 ** 2 - 3 + 1 
expression_w_parenthesis = (5 ** 2) - (3 + 1)

is_equal = expression == expression_w_parenthesis
print(is_equal)

'''
    Task 2: Mix and Match 
    - Combine arithmetic (+), logical (or), and comparison (>) operations in 
    a single expression and predict the outcome. 

'''

mixed_expression = ((3 + 5) or (2 + 6 )) > 7 # Prediction: TRUE
print(mixed_expression) # Outcome: TRUE