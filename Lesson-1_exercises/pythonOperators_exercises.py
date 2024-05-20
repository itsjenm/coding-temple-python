'''
Exercise 1: The Baker's Dilemma

    - If one cake requires 250 grams of flour and you have 
    2.5 kilograms of flour, how many cakes can you make 

'''  
flour_per_cake = 250
total_flour = 2.5 * 1000

num_of_cakes = total_flour // flour_per_cake
print(num_of_cakes)


'''
Exercise 2: Claiming Territories

    - use assignment operator to claim a variable kingdom with
    the value "Pythonland"

'''

kingdom = "Pythonland"
print(kingdom)

'''
Exercise 3: Fashion Contest

    - Given two shirts with prices shirt1 = 45 and shirt2 = 50. Use 
    a comparison operator to check if shirtw is cheaper than shirt2

'''
shirt1_price = 45
shirt2_price = 50

is_cheaper = shirt1_price < shirt2_price
print(is_cheaper)

'''
Exercise 4 : Rainy Day Dilemma

    - Whrite a logical operator to determine if you should take an umbrella if its either
    going to rain or going to rain hevily 

'''
going_to_rain = True
raining_heavily = False

take_umbrella = going_to_rain or raining_heavily
print(take_umbrella)

'''
Exercise 5: Royal Order

    - Evaluate the expression 3 + 5 * 2 - 8. What would be the order of operations? 

'''
result = 3 + 5 * 2 - 8
print(result)

'''
Exercise 6: The Pastry Fraction

    - You have 10 pastries and you want to divide them equally amoung 3 friends. How 
    many pastries does each friend get and how many are left?

'''

total_pastries = 10
friends = 3

serving_per_friends = total_pastries // friends 
pastries_left = total_pastries % friends 
print("Pastries for each friend", serving_per_friends)
print("Pastries left: ", pastries_left)

'''
Exercise 7: Kingdom Expansion 

    - You already have a kingdom named "Pythonland". Use the assignment operator to add 
    "is wonderful" to it

'''
kingdom += " is wonderful"
print(kingdom)

'''
Exercise 8: Royal Duel 

    - Two Knights have strength values of knight1 = 45 and knight2 = 50. Use a comparison 
    operator to determine if knight1 has the same strength as knight2

'''
knight1 = 45
knight2 = 50
has_same_strength = knight1 == knight2
print(has_same_strength)


'''
Exercise 9: Chef's Special 

    - A chef has two ingredients: eggs = True and flour = False. He can only 
    make pancakes if he has both. Determine if the chef can make pancakes

'''

eggs = True
flour = False
can_make_pancakes = eggs and flour
print(can_make_pancakes)

'''
Exercise 10: Medieval Architecture

    - A castle's height is 100 units and its moat's width is 50 units. If you double the 
    castle's height and have moat's width, what would be the new dimensions? 

'''

castle_height = 100
moat_width = 50
castle_height *= 2
moat_width /= 2
print(castle_height, moat_width)