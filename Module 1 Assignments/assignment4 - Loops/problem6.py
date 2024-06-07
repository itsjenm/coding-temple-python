'''
Advanced Looping Techniques

Objective:
Advance your looping skills by exploring more complex list manipulations. 
You will learn to selectively loop through parts of a list, use list comprehensions for concise code, and generate numerical lists with Python's range function.

Task 1: The Selective DJ
Loop through a slice of the genres list from the previous question and print out the genres. 
Use slicing to create a sublist of genres from the second to the fourth track.

Task 2: The One-Liner Band with List Comprehensions
Use a list comprehension to create a new list that contains each genre with the word "Music" appended to it. 
Print this new list.

Task 3: Numerical Beats with range
Write a loop using range() to print out a countdown from 10 to 1, followed by the message "The beat drops now!".

'''

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Task 1: The Selective DJ
sublist_genres = genres[1:4]
print(sublist_genres)

# Task 2: The One-Liner Band with List Comprehensions
new_playlist = [genre + " Music" for genre in genres]
print(new_playlist)

# Task 3: Numerical Beats with range
for i in range(10, 0, -1):
    print(i)
print("The beat drops now!")