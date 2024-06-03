'''
Build a program to manage an e-commerce product catalog efficiently

adding product categories
adding products
displaying all available catagories
product searches

'''

# 1. Initialize a dictionary to represent your product

catalog = {
    "Electronics": ["Laptop", "Smartphone"],
    "Books": ["Fiction", "Non-Fiction"],

}

# 2. Implement functions 
def add_category(catalog, category):
    if category not in catalog:
        catalog[category] = []
        print(f"Category '{category}' added.")
    else: 
        print(f"Category '{category}' already exists.")

def add_product(catalog, category, product):
    try:
        if product not in catalog[category]:
            catalog[category].append(product)
            print(f"Product {product} added to {category}.")
        else:
            print(f"Product '{product}' already exist in {category}.")
    except KeyError:
        print(f"Category '{category}' does not exist.")

def display_categories(catalog):
    for category, products in catalog.items():
        print(f"{category}: {', '.join(products)}")

def search_product(catalog, product):
    found = False
    for category, products in catalog.items():
        if product.lower() in [p.lower() for p in products]:
            found = True
            print(f"Product '{product}' was found.")
            break
    if not found:
        print(f"Product '{product}' not found.")


add_category(catalog, "Clothing")
add_product(catalog, "Electronics", "Camera")
display_categories(catalog)
search_product(catalog, "laptop")