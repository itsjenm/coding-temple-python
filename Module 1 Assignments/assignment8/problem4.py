'''
Python Essentials for Business Analytics

Objective:
This assignment aims to strengthen your proficiency in Python by tackling challenges that simulate real-world business analytics scenarios. 
You'll practice copying dictionaries, utilizing built-in methods, managing nested collections, and implementing try-except blocks for error handling.

'''

# Task 1: Sales Data Cloning and Modification

# Gain practical experience in copying dictionaries and modifying data, crucial skills in data analysis.

# You have a dictionary representing weekly sales data for a store. Your task is to create a deep copy of this data and update the sales figures for a specific week.

import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

# TODO: Create a deep copy of weekly_sales.
# TODO: Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.

reproduced_weekly_sales = copy.deepcopy(weekly_sales)
reproduced_weekly_sales["Week 2"]["Electronics"] = 18000
print(f"Original: {weekly_sales}")
print(f"New: {reproduced_weekly_sales}")
