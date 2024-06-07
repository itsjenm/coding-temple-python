'''
Python Regular Expressions Mastery


Problem Statement:

You are given a piece of code that is intended to extract email addresses from a given text. 
However, the code contains errors and does not function as expected. 
Your task is to identify and correct these errors.

Expected Outcome:

Correct the regex pattern to capture email addresses effectively.
Modify the code to handle different cases in email addresses.

'''

import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", text)
print(emails)

