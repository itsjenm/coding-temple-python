'''
Advanced Data Handling with Python

Objective:
The aim of this assignment is to deepen your knowledge and practical skills in handling complex data structures using Python. 
You will work on real-world inspired tasks that require advanced manipulation of dictionaries, nested collections, and implementing custom functions for specific data processing needs.

'''

# Task 1: Hotel Room Booking Tracker
# Develop a program that:

# Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
# Implement functions to:
# Book a room (mark as booked and assign to a customer).
# Check-out a customer (mark room as available and remove customer name).
# Display the status of all rooms.

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def booking_room(hotel_rooms, customer_name):
    """
    This function changes the status of a room to "booked" and assigns to a customer

    """
    for room_number, details in hotel_rooms.items():
        if details["status"] == "available":
            details["status"] = "booked"
            details["customer"] = customer_name
            print(f"Room {room_number} has been booked by {customer_name}.")
            return
    print("No available rooms to book.")
    

        
def check_out(hotel_rooms, customer_name):
    """
    This function checks out a customer and marks room as available

    """
    found = False
    for room_number, details in hotel_rooms.items():
        if details["customer"] == customer_name:
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(f"{customer_name} has checked out of room {room_number}.")
            found = True
            break
    if not found:
        print(f"No room found for customer {customer_name}")


def display_rooms(hotel_rooms):
    """
    This function displays the satus of each room

    """
    for room_number, details in hotel_rooms.items():
        status = details["status"]
        customer = details["customer"]
        print(f"Room {room_number}: Status - {status}, Customer - {customer}")


booking_room(hotel_rooms, "jenny")
print(hotel_rooms)
check_out(hotel_rooms, "jenny")
display_rooms(hotel_rooms)