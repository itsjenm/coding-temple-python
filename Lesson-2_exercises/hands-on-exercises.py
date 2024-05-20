'''

Write a program that suggests a movie genre to users
based on their current mood and the day's weather

'''

mood = input("What is current mood? (happy/sad/adventurous) ")
weather = input("What is the weather like (sunny/rainy)? ")

if mood == 'happy':
    if weather == 'sunny':
        print("I recommend a Comedy")
    elif weather != 'sunny':
        print('I recommend a Romantic movie')
elif mood == 'sad':
    print('I recommend a Drama')
else:
    print('I recommend an Adventure movie')


'''

You are programming a smart wardrobe assistant that suggests
outfits to users based on the day's temperature and the type
of event

'''

temperature = float(input("What is the temperature like? (in Celsius) "))
event = input("What type of event? (formal/casual) ")

if temperature <= 15:
    if event == 'formal':
        print("Warm formal suit")
    elif event == 'casual':
        print("Cozy sweater and jeans")
elif temperature >= 15 and event == 'formal':
    print("Light formal suit")
else:
    print("T-shirt and shorts")


'''

write a program that: 
1. asks for the users grade (a/b/c)
2. asks if they are part of a sports team (yes/no)
3. asks if they are part of the drama club (yes/no)\
4. determine the discount percentage based on criteria
5. displays the discount percentage

'''

grade = input("What is your grade? (A/B/C) ").lower()
sports = input("Are you part of the sports team? (yes/no) ")
club = input("Are you part of the drama club? (yes/no) ")

discount = 0

if grade == 'a':
    if sports == 'yes':
        discount = 20
    else:
        discount = 10
elif grade == 'b':
    if club == 'yes':
        discount = 15

print(f"You are eligible for a {discount}% discount. ")


'''
write a program that:
1. asks the user for their age
2. determine if the user is old enough to access the games 
3. displays the appropiate message to the user

'''

age = int(input("What is your age? "))
print('You can drive!' if age >= 18 else 'Not yet!')


'''
write a program that:
1. asks for the users meal type preference (veg/non-veg)
2. asks for the user dietary preference (sugar-free/regular)
3. determine the dish
4. display the recommended dish 

'''

meal = input("Do you have a meal type preferance? (veg/non-veg) ")
diet = input("Do you have a dietary preference? (sugar-free/regular) ")


if meal == 'veg':
    if diet == 'sugar-free':
        print('fruit salad')
    else:
        print('Veg cake')
if meal == 'non-veg':
    if diet == 'sugar-free':
        print('Sugar-free ice cream')
    else:
        print('Chocolate brownie')
