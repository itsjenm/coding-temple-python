'''
Exploring Python Modules and Data Structures Assignment

Task 2: Contact List Manager

Problem Statement: Create a Python script using a custom module to manage a contact list. 
The script should allow adding, removing, and displaying contacts stored in a list.

'''

contacts = [
    {
        "name": "jenny m",
        "email": "jenny@example.com",
        "phone": 453-897-6777
    },
    {
        "name": "coco",
        "email": "coco@example.com",
        "phone": 345-555-3222
    },
    {
        "name": "biscuit",
        "email": "biscuit@example.com",
        "phone": 222-345-1222
    }
]

def add_contact(contact):
    return contacts.append(contact)


def remove_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]


def display_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")