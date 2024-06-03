'''
The Quiz Game 

Objective: The aim of this assignment is to create a quiz game that asks questions and checks answers.

'''

# Task 1: Develop a list of questions and answers
questions_list = ["what is your favorite food? ", "Do you have pets? ", "How many siblings do you have? "]
answers_list = ["italian", "yes", "8"]

# Task 2: Write a function that quizzes the user and takes their answers
def quiz_game(questions_list):
    answers = []
    score = 0
    for question in questions_list:
        answers.append(input(question))

    # Task 3: Score the quiz and give the user feedback on their performance
    for correct in answers_list:
        for guesses in answers:
            if correct == guesses:
                score += 1
    if score == 3:
        print(f"You got all of them correct. You won!")
    else:
        print(f"You got only {score} correct. Nice try!")


# Run the tests
quiz_game(questions_list)