'''
Python Sets Adventure

Task 1: Flight Route Comparison

Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. Write a Python program to find out:

'''

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# TODO: Destinations that both airlines fly to.
common_destinations = our_routes.intersection(competitor_routes)
print(f"Destinations both airlines fly to: {common_destinations}")

# TODO: Destinations unique to your airline.
unique_our_routes = our_routes.difference(competitor_routes)
print(f"Destinations unique to our airline: {unique_our_routes}")

# TODO: Whether there are any destinations that neither airline shares.
neither_shared = our_routes.symmetric_difference(competitor_routes)
print(f"Destinations that neither airline shares: {neither_shared}")





