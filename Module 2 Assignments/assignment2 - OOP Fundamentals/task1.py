'''
City Infrastructure Management System


'''

# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, owner):
        self.owner = owner

vehicle1 = Vehicle(34567, "TESLA", "Jenny m")
vehicle2 = Vehicle(32112, "SUV", "Coco")

vehicle1.update_owner("Bella")
print(vehicle1.owner, vehicle1.type, vehicle1.registration_number)
print(vehicle2.owner, vehicle2.type, vehicle2.registration_number)


