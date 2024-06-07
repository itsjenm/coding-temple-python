'''
Develop a feature that allows user to create a fun echo effect with their text posts.
'''

def generate_echo_text(text):
    if text:
        return ''.join([char * 2 for char in text])
    else:
        return "The input text cannot be empty. Please enter some text"
    

while True:
    user_input = input("Enter your text to echo: ")

    echo_text = generate_echo_text(user_input)
    print(f"Your echoed text is: {echo_text}")

    continue_echo = input("Do you want to create another echo text? (yes/no): ").lower()
    if continue_echo != 'yes':
        break

    
    