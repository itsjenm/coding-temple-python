'''
Allow users to find the index of characters in a book or a document

'''

def find_character_index(text, character):
    if len(character) == 1:
        index = text.find(character)
        if index == -1:
            return f"The character '{character}' is not present in the text."
        else:
            return f"The index of the character '{character}' is: {index}"
    else:
        return "Plese enter only a single character."

while True:
    text_input = input("Enter a line of text from the book: ")
    char_input = input("Enter the character to find: ")

    result = find_character_index(text_input, char_input)
    print(result)

    continue_search = input("Do you want to search for another character? (yes/no): ").lower()
    if continue_search != 'yes':
        break
    