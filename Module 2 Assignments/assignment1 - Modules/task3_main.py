'''
Task 3 : Custom Module with Aliases

Main file

'''

import text_utils as tu

sample_text = "hello world from python"
    
# Using capitalize_string function
capitalized_text = tu.capitalize_string(sample_text)
print(f"Capitalized: {capitalized_text}")
    
# Using reverse_string function
reversed_text = tu.reverse_string(sample_text)
print(f"Reversed: {reversed_text}")

