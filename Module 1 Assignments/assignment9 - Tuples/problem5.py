'''
Advanced Tuple Techniques: Joining and Nesting in Python

Objective:
This assignment is designed to advance your understanding and application of joining and nesting tuples in Python. 
You will engage in tasks that require organizing and manipulating complex data structures, improving your problem-solving skills in handling multi-dimensional data.

'''

# Task 1: Product Catalog Merging
# Utilize tuple joining to combine multiple product catalogs.

# You are managing the product catalogs for an online store. 
# Each catalog is a tuple of products, and each product is a tuple containing the product name and price. 
# Merge multiple catalogs into a single tuple.

# Write a function to join two or more product catalogs into one.
# Display the combined catalog, ensuring that it maintains the order of products as they were in their original catalogs.

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))
catalog3 = (("Monitor", 300), ("Headphones", 150))

def join_catalog(*catalogs):
    '''
    A function that joins two or more product catalogs into one

    '''
    new_catalog = ()
    for catalog in catalogs:
        new_catalog += catalog
        
    for i, item in enumerate(new_catalog, start=1):
        print(f"{i}: Item: {item[0]}, \nPrice: {item[1]:.2f}\n")


join_catalog(catalog1, catalog2, catalog3)
