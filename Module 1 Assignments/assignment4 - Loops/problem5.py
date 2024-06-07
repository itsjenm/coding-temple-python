'''
Looping Lists - The Rhythm of Repetition

Objective:
Dive into the heart of Python loops with a musical twist. Your task is to explore different ways of looping through lists, each with its unique style and purpose. 
By the end of this assignment, you will be able to control your loops like a DJ controls the tracks, ensuring each element gets its time to shine.

Task 1: The for Loop DJ Set
Using the provided genres list, write a for loop that prints out each genre with a custom message. 
Extend this task by adding a counter that displays the number of the track before the genre.

Task 2: The Remix Artist with while
Convert the for loop from Task 1 into a while loop. Ensure it performs the same function but also includes a condition to stop the loop if a certain genre is played for instance Hip-hop.

Task 3: Light Show Technician Loop
Using the range() function, loop through the genres list by index. For each genre, print out the track number and a message that the light show is ready. 
Modify the loop to skip a genre if it's not suitable for the light show, for instance Classical genre.

'''

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Task 1: The for loop DJ Set
counter = 0

for genre in genres:
    counter += 1
    print(f"DJ's mixes: Track number: {counter} genre: {genre}")


# Task 2: The Remix Artist with while
indeces = 0
while counter < len(genres):
    counter += 1
    print(f"DJ's mixes: Track number: {counter} genre: {genres[counter -1]}")
    if genres[counter -1] == 'Hip-hop':
        print("time to dance")
        break

# Task 3: The Light Show Technician Loop
for i in range(len(genres)):
    counter += 1
    genre = genres[counter - 1]
    if genre == 'Classical':
        continue
    print(f"Genre: {genre}, Track number: {counter}, light show is ready")
    