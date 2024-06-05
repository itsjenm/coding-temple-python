'''
Tuple Mastery in Python

Objective:
The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. 
By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

'''

# Task 1: Formatting Flight Itineraries

# Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination).
# The function should format and return a string that lists each itinerary. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:
# "Itinerary 1: Alice - From New York to London
# Itinerary 2: Bob - From Tokyo to San Francisco"

itinerary_list = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def format_itinerary(tuple_list):
    """
    A function that formats an itinerary list
    """
    
    for i, itinerary in enumerate(itinerary_list, start=1):
        print(f"Itinerary {i}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}")

format_itinerary(itinerary_list)