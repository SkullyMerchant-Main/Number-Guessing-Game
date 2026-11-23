import random

lowest_int = 1
highest_int = 0
attempts = 10
names = []
scores = []


def menu():
    global answer, highest_int

    print("Welcome to Ethan's Number Guessing Game.\n")
    print("Choose a difficulty:\n 1) Easy mode [1 - 100]\n  2) Medium mode [1 - 500]\n 3) Hard mode [1 - 1000] \n")
    difficulty = int(input("> "))
    if difficulty == 1:
        highest_int = 100
        answer = random.randint(lowest_int, highest_int)
    elif difficulty == 2:
        highest_int = 500
        answer = random.randint(lowest_int, highest_int)
    else:
        highest_int = 1000
        answer = random.randint(lowest_int, highest_int)


def maingame():
    global guesscount, limit

    guesscount = 0
    random_limit = random.randint(5, 10)
    limit = random_limit
    print(f"You have {limit} trys")

    while guesscount < limit:
        try:
            user_input = int(input("Guess the number:"))

            if user_input < lowest_int or user_input > highest_int:
                print(f"Please enter a valid number between {lowest_int} and {highest_int}")
                continue

            guesscount += 1
            if user_input == answer:
                leaderboard()
            elif user_input > answer:
                print("Too high! Try again.")
            elif user_input < answer:
                print("Too low! Try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 1000")
            continue

    if guesscount == limit:
        print(f"Correct number was {answer}")

def leaderboard():
    print(f"Correct!")
    print(f"Enter your name to be added to the leaderboard:")
    names.append(input("> "))
    scores.append(guesscount)
    leaderboard = [f"{i+1} {name}: {score} "
            for i, (name, score) in
                enumerate(zip(names, scores))]
    print("\n".join(leaderboard))
    playagain()

def playagain():
    while True:
        again = input("Would you like to play? (y/n): ")
        if again.lower() == "y":
            menu()
            maingame()
            break
        elif again.lower() == "n":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

while isPlaying := True:
    playagain()

    
