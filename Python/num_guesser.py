# 10 Jan
# Number Guesser

import random
def num_guess(x):
    random_number = random.randint(1, x) # output: return a random number for us to guess
    guess = 0 # we do this to not have 0 as a random number
    while num_guess != random_number:
        num_guess = int(input(f"Guess the number between 1 and {x}: ")) # Repeats until correct
        if num_guess < random_number:
            print("Sorry, guess again. Too low. ")
        elif num_guess > random_number:
            print("Sorry, guess again. Too high. ")  # Clues for the game

print(f"Good Job, you have guesed the number {random_number}!")

num_guess(10)

# Number Guesser for Computer to guess

def computer_guess(x):
    low = 1
    high = x # creating boundaries for guessing
    feedback = "" # we do this to not have the computer return a empty string
    