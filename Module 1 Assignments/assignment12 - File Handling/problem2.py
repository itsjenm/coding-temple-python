'''
Regex-Powered Text Data Processing

Task 1: Email Extractor:

Problem Statement: Write a Python script to extract all email addresses from a given text file (contacts.txt). 
The file contains a mix of text and email addresses.

Expected Outcome: The script should output a list of all unique email addresses found in the file. 
Utilize regex to accurately identify email addresses amidst other text.

'''

import re

def extract_emails(filename):
    # Define a regex pattern for extracting email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    try:
        # Read the file contents
        with open(filename, 'r') as file:
            contents = file.read()
        
        # Find all matches of the email pattern
        emails = re.findall(email_pattern, contents)

        # Use a set to store unique email addresses
        unique_emails = set(emails)

        # Print or return the unique email address
        return list(unique_emails)
    
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the filename
filename = '/workspaces/coding-temple-python/assignment12/contacts.txt'
    
# Extract and print the email addresses
email_addresses = extract_emails(filename)
if email_addresses:
    print("Extracted email addresses:")
    for email in email_addresses:
        print(email)
