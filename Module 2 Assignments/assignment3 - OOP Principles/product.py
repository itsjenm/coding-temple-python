'''
Task 2: E-commerce Product Catalog System

'''

# Task 1: Create Base Product Class
class Product:
    # Constructor and common attributes
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        # General method to display product info
        print(f"Product: {self.name}")
        print(f"Product Id: ${self.product_id}")
        print(f"Product price: ${self.price:.2f}")
    
# Task 2: Implement Subclasses for Specific Products
class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

# Task 3: Override Display Method in Subclasses
    def display_info(self):
        # Overridden method for books
        super().display_info()
        print(f"Author: {self.author}")

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Specifications: {self.specs}")
      

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")


