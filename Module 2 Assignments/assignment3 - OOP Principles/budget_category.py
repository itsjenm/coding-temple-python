'''
Encapsulation in Personal Budget Management

Problem Statement: 
You are required to build a Personal Budget Management application. 
The application will manage budget categories like food, entertainment, utilities, etc., 
ensuring that budget details remain private and are accessed or modified through public methods.

'''

# Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, category_name='misc', budget=200):
        self.__category_name = category_name
        self.__budget = budget
        self.__remaining_budget = budget

    # Task 2: Implement Getters and Setters
    def set_category_name(self, category_name):
        self.__category_name = category_name

    def set_budget(self, budget):
        if budget > 0:
            self.__budget = budget
            self.__remaining_budget = budget 
    
    def get_category_name(self):
        return self.__category_name
    
    def get_budget(self):
        return self.__budget

    def get_remaining_budget(self):
        return self.__remaining_budget

    # Task 3: Add Budget Functionality
    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
            else:
                raise ValueError("Expense exceeds the remaining budget.")
        else:
            raise ValueError("Expense amount must be a positive number.")
        
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")


