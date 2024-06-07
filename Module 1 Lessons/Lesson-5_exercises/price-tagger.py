'''
The Precise Price tagger

'''

while True:
    price_input = float(input("Enter the price: "))
    rounded_price = round(price_input)

    print(f"Rounded Price: ${rounded_price}")

    new_price = input("Would you like to enter a new price? (yes/no) ").lower()
    if new_price != 'yes':
        break
