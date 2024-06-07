'''
City Services Simulation: Python OOP and Modular Design


Task 4: Public Transportation Module

Problem Statement: 
Develop a Bus class as part of a public transportation module. 
Use class variables to represent common attributes like city name and base fare. 
Implement instance variables for specific attributes like route number and passenger capacity.

Expected Outcome: 
A Bus class with both class and instance variables, and a transportation module to manage different bus routes. 
A test script should demonstrate creating bus instances and accessing both class and instance attributes.

'''

class Bus:
    # Class variables
    city_name = "Metropolis"
    base_fare = 2.5

    def __init__(self, route_number, passenger_capacity):
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity

    def __str__(self):
        # Returns a string representation of the bus.
        return (f"Bus Route: {self.route_number}, Capacity: {self.passenger_capacity}, "
                f"City: {Bus.city_name}, Base Fare: {Bus.base_fare}")


bus1 = Bus(route_number="42", passenger_capacity=50)
bus2 = Bus(route_number="85", passenger_capacity=75)

print(bus1)
print(bus2)
    
print(f"City Name: {Bus.city_name}")
print(f"Base Fare: {Bus.base_fare}")