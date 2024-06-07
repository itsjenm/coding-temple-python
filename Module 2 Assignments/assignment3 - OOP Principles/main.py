from budget_category import BudgetCategory
from product import Product, Book, Electronic, Clothing

# Task 1 - Budget Category Test
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

print()

# Task 2: Product Catalog Functionality
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_electronic = Electronic("456", "Smartphone", 499.99, "64GB, 4GB RAM")
my_clothing = Clothing("789", "T-Shirt", 19.99, "M")

my_book.display_info()
print()
my_electronic.display_info()
print()
my_clothing.display_info()