# use loops in conjuction with random selections, simulating 
# real-world scenarios where random draws or selections
# are required

import random

name = ["Alex", "Sam", "Sarah"]

while "Alex" not in random.choices(name, k=1):
    pass
print("Congratulations, Alex you've won!")

