'''
Task 2: Contact List Manager

Main file

'''

import contacts_module

while True:
        print("\nContact List Manager")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact = {"name": name, "email": email, "phone": phone}
            contacts_module.add_contact(contact)
            print("Contact added successfully.")

        elif choice == '2':
            name = input("Enter the name of the contact to remove: ")
            contacts_module.remove_contact(name)
            print("Contact removed successfully.")

        elif choice == '3':
            contacts_module.display_contacts()

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

