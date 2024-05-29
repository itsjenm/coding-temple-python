# Use list comprehension to generate the squares of numbers from 1 to 10.
# Each element in the new list should be the square of an integer from the original range.

squares = [number**2 for number in range(1,11)]

print(squares)

# start with a list of numbers from 1 to 20.
# use list comprehension to filter out the even numbers
# remember that an even number is divisible by 2 with no remainder

numbers = list(range(1, 21))

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

