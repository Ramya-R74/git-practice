import random

def calculate_score():
    # TODO: Need to implement scoring logic later
    # testing git stash functionality

def start_game():
    number_to_guess = random.randint(1, 10)
    print("Welcome to the Guessing Game!")
    print("Hint: The number is between 1 and 10! but mostly the system select number 6 and 8.")
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number_to_guess:
        print("You win!")
    else:
        print(f"You lost! The number was {number_to_guess}")

if __name__ == "__main__":
    start_game()