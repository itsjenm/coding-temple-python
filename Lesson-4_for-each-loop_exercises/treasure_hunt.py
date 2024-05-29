caves = [False, False, True, False, False]

for index, cave in enumerate(caves):
    if cave:
        print(f"Treasure fournd in cave {index + 1}!")
        break