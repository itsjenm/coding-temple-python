'''
Interactive Help Desk Bot

Objective:
The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for a SaaS application.
'''

# Task 1: Command Parser

# Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). 
# If a command is found, print a response related to the command.

def command_parser(text):
    keywords = ['help', 'issue', 'contact support']
    for key in keywords:
        if key in text.lower():
            print(f"Command {key} found: Responding accordingly...")
            return
            
    print("No predefined command found in the text")


# Example usage
user_input = input("Enter your query: ")
command_parser(user_input)


# Task 2: Issue Categorizer

# If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. 
# Print out the category of the issue for the support team.

def issue_categorizer(text):
    categories = ['login', 'performance', 'error']
    if 'issue' in text.lower():
        for category in categories:
            if category in text.lower():
                print(f"Issue category: {category}")
                return
    print("No specific issue category found")

# Example usage
issue_categorizer(user_input)