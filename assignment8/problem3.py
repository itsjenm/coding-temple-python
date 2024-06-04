'''
Python Programming Challenges for Customer Service Data Handling

Objective:
This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. 
You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

'''

# Task 1: Customer Service Ticket Tracker

# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
# Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(customer_name, issue):
    """
    A function that opens a new service ticket

    """

    ticket_id = f"Ticket{len(service_tickets) + 1:03d}"  # Generate a new ticket ID
    service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue, "Status": "open"}
    print(f"New ticket created: {ticket_id} for customer {customer_name}")
    

def update_ticket(ticket_id, new_status):
    """
    A function that updates the status of an existing ticket

    """
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} updated to status '{new_status}'.")
    else:
        print(f"Ticket {ticket_id} not found.")


def display_tickets(service_tickets, status_filter=None):
    """
    A function that displays all the service tickets

    """
    for ticket_id, details in service_tickets.items():
        if status_filter is None or details["Status"] == status_filter:
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")


open_ticket("jenny", "tech problem")

update_ticket("Ticket003", "closed")

display_tickets(service_tickets, status_filter='closed')
