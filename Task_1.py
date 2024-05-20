import random

def quiz():
    questions = {
        "Who is the current president of India?":"Droupadi Murmu",
        "What is the capital of India?":"Delhi",
        "What is the national bird of India?":"Peacock",
        "what is the national animal of India":"Tiger",
    }
    score = 0

    for question, answer in questions.items():
        user_ans = input(question + " ")

        if user_ans.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry! The correct answer is {answer}.")

    print(f"Your final score is {score} out of {len(questions)}.")

def guess_game():
    num_guess = random.randint(1,100)
    guess = None
    attempts = 0

    while guess != num_guess:
        guess = int(input("Enter the number between 1 to 100: "))
        attempts += 1
        if guess < num_guess:
            print("Too low! Please Try Again.")

        elif guess > num_guess:
            print("TOO High! Please Try Again.")

    print(f"Great! You found the number in {attempts} attempts.")

print("Hello! Lets play a game.. ")
print("Which game you want to play: \n press 1 for quiz\n And press 2 for guess the number. ")
user_choise = int(input(" "))

if user_choise == 2:
    print("Rules of the game is: \n You enter the same number as computer choose.\nLets start..\n")
    guess_game()
elif user_choise ==1:
    print("Rules of the quiz game is:\n You seen some questions on screen. If you answer is correct, then your score is go high.\nLets start..\n ")    
    quiz()
else:
    print("Invalid Choise..")