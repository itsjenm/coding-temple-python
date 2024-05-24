inventory = [
    ["apple", 5],
    ["bananas", 2],
    ["oranges", 0],
    ["milk", 1],
    ["eggs", 12]
]

reorder_threshold = 3

for item in inventory:
    name, quantity = item
    if quantity < reorder_threshold:
        print(f"{name} needs to be reordered.")