table_size = int(input("Enter the size of the multiplication table: "))

for row in range(1, table_size + 1):
    for col in range(1, table_size + 1):
        product = row * col
        print(f"{product} \t", end="")
    print()

