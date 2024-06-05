'''
Python Regex Challenge: Enhancing E-Commerce Operations


Task 1: Product Description Keyword Tagging

Problem Statement:
You have a list of product descriptions. 
Your task is to tag each product based on keywords in the description. 
For instance, tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' based on relevant keywords found in their descriptions.


Expected Outcome:

Convert all price formats in the string to a standardized 'USD XX.XX' format.
Use re.sub() to perform the necessary replacements and format transformations.

'''

import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory for $500 price",
    "Cotton t-shirt in medium size for $20.99",
    "Stainless steel kitchen knife set priced at $49.95"
]

def process_product_data(description):
    # Regular expression pattern to match price formats
    price_pattern = r"\$([0-9,]+(?:\.[0-9]{2})?)"

    # Function to replace price formats with 'USD XX.XX' format
    def format_price(match):
        price = match.group(1).replace(',', '')  # Remove comma separators
        return f"USD {price}"

    # Define keywords for each category
    electronics_keywords = {"smartphone", "tablet", "laptop", "camera"}
    apparel_keywords = {"t-shirt", "shirt", "dress", "pants"}
    home_kitchen_keywords = {"kitchen", "knife", "cookware", "utensils"}

    # Function to tag products based on keywords
    def tag_product(description):
        description_lower = description.lower()  # Convert description to lowercase for case-insensitive matching
        if any(keyword in description_lower for keyword in electronics_keywords):
            return "Electronics"
        elif any(keyword in description_lower for keyword in apparel_keywords):
            return "Apparel"
        elif any(keyword in description_lower for keyword in home_kitchen_keywords):
            return "Home & Kitchen"
        else:
            return "Other"

    # Replace price formats in the description
    formatted_description = re.sub(price_pattern, format_price, description)

    # Tag the product description
    tag = tag_product(description)
    
    return formatted_description, tag


# Process each product description and display the results
for i, description in enumerate(descriptions, start=1):
    formatted_description, tag = process_product_data(description)
    print(f"Product {i}: {formatted_description} - Tag: {tag}")
