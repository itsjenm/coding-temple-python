'''
Exploring Python's OS Module


Problem Statement: 
Create a Python script that lists all files and subdirectories in a given directory. 
Your script should prompt the user for the directory path and then display the contents.

Expected Outcome: 
The script should correctly list all files and subdirectories in the specified directory. 
Handle exceptions for invalid paths or inaccessible directories.

'''

import os

# Task 1: Directory Inspector
def list_directory_contents(path):
    # List and print all files and subdirectories in the given path
    try:
        # Check if the path exists and is a directory
        if not os.path.exists(path):
            print(f"The path '{path}' does not exist.")
            return
        if not os.path.isdir(path):
            print(f"The path '{path}' is not a directory.")
            return
        
        # List all files and subdirectories
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in contents:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"Directory: {item}")
            else:
                print(f"File: {item}")
    except PermissionError:
        print(f"Permission denied for accessing the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Task 2: File Size Reporter
def report_file_sizes(directory):
    # Iterate through files in the directory and print their names and sizes
    try:
        # Check if the path exists and is a directory
        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist.")
            return
        if not os.path.isdir(directory):
            print(f"The path '{directory}' is not a directory.")
            return

        # Iterate through files in the directory and print their names and sizes
        print(f"File sizes in the directory '{directory}':")
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                size = os.path.getsize(item_path)
                print(f"File: {item}, Size: {size} bytes")
            else:
                print(f"Skipping directory: {item}")

    except PermissionError:
        print(f"Permission denied for accessing the directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Task 3: File Extension Counter
def count_file_extensions(directory):
    # Count and print the number of files of each extension type in the directory
    try:
        # Check if the path exists and is a directory
        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist.")
            return
        if not os.path.isdir(directory):
            print(f"The path '{directory}' is not a directory.")
            return

        # Dictionary to store the count of each file extension
        extension_counts = {}

        # Iterate through files in the directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                _, ext = os.path.splitext(item)
                ext = ext.lower()  # Normalize the extension to lower case
                if ext in extension_counts:
                    extension_counts[ext] += 1
                else:
                    extension_counts[ext] = 1

        # Print the count of each file extension
        print(f"File extension counts in the directory '{directory}':")
        for ext, count in extension_counts.items():
            print(f"{ext.upper()}: {count}")

    except PermissionError:
        print(f"Permission denied for accessing the directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")



# Prompt the user for the directory path
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
report_file_sizes(directory_path)
count_file_extensions(directory_path)

# Run Example:
# Enter the directory path: assignment1
# Contents of the directory 'assignment1':
# File: Problem4.py
# File: Problem1.py
# File: Problem2.py
# File: Problem3.py
# File: Problem6.py
# File: Problem5.py