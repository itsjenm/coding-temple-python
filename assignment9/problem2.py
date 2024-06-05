'''
Python Data Structure Challenges in Real-World Scenarios

Objective:
This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. 
By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.

'''

# Task 1: Library System Enhancement

# Sharpen your skills in managing and modifying data within tuples and lists.
# You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately

def add_book(library, new_book):
    """
    Adds a new book to the library.
    Ensures no duplicate books are added.
    """

    if new_book not in library:
        library.append(new_book)
        print(f"Book '{new_book[0]}' by {new_book[1]} added to the library.")
    else:
        print(f"Book '{new_book[0]}' by {new_book[1]} is already in the library.")

# Example usage
new_book_1 = ("Fahrenheit 451", "Ray Bradbury")
new_book_2 = ("1984", "George Orwell")

add_book(library, new_book_1)  # Should add the book
add_book(library, new_book_2)  # Should not add the book as it's a duplicate

print(library)  # Display the updated library

