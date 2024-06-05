'''
Advanced Text Processing with Python Regex


Task 1: Advanced Data Extraction

Problem Statement:
Develop a script to extract specific information from a formatted text. 
The text contains data entries delimited by semicolons and formatted as 'Key: Value'. 
Extract the value corresponding to a specific key.

Expected Outcome:

Correctly identify and categorize valid and invalid URLs from the list.
Use regex to validate the format of each URL.

'''

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# Extract the Occupation from the text
occupation_pattern = r"Occupation:\s*([^;]+)"


# Extract the Occupation value using re.search() and group(1)
match = re.search(occupation_pattern, text)
if match:
    occupation = match.group(1).strip()
    print(f"Occupation: {occupation}")
else:
    print("Occupation not found in the text")

