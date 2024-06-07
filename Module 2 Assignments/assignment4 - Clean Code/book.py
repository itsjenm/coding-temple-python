'''
Building a Modular Online Bookstore System



Task 1: Designing the Book Module

Create a module for managing book-related functionalities. 
This includes classes and functions for book attributes, book availability, and any other book-specific operations.

Problem Statement:

The bookstore system requires a dedicated module for handling various aspects related to books, such as title, author, price, and stock status.

'''

class Book:
    # Define book attributes and methods
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

# Additional functions related to book management
    def display_info(self):
        print("Book Information:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock} available")
        

    def set_price(self, price):
        if price >= 0:
            self.price = price
        else:
            print("Price cannot be negative.")


    def increase_stock(self, quantity):
        if quantity >= 0:
            self.stock += quantity
        else:
            print("Quantity cannot be negative.")
    

    def decrease_stock(self, quantity):
        if quantity >= 0:
            if self.stock >= quantity:
                self.stock -= quantity
            else:
                print("Insufficient stock.")
        else:
            print("Quantity cannot be negative.")