item_prices = [2.99, 5.49, 3.25, 13.99, 4.75]

total_cost = 0

for price in item_prices:
    total_cost += price
print(f"The total cost of the shopping cart is: ${total_cost:.2f}")