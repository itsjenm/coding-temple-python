'''
Task 3: Custom Module with Aliases

Problem Statement: Create a custom module named text_utils.py with functions for string manipulation (e.g., reversing a string, capitalizing). 
In your main script, import this module using an alias and utilize its functions.

'''

def capitalize_string(s):
    """Capitalizes the first letter of each word in the string."""
    return s.title()


def reverse_string(s):
    """Reverses the given string."""
    return s[::-1]