from art import logo
import random
from replit import clear

def check_the_guess(proper_number, user_number):
    if proper_number == user_number:
        print(f"You got it! The answer was {proper_number}.")
        return True, True
    elif proper_number > user_number:
        print("Too low.")
        return False, False
    else:
        print("Too high.")
        return False, False

clear()
print(logo)
welcome_message = "Welcome to the Number Guessing Game!"
min_number = 1
max_number = 100
game_level = { "easy": 10,
               "hard": 5,
               }

print(f"I'm thinking of a number between {min_number} and {max_number}.")
generated_number = random.randint(min_number, max_number)
#print(f"Pssst, the correct answer is {generated_number}")
chosen_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if chosen_level in game_level.keys():
    number_of_attempts = game_level[chosen_level]
    end_game = False
    while number_of_attempts > 0 and not end_game:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_guess = int(input(f"Make a guess: "))
        guess_result, end_game = check_the_guess(generated_number, user_guess)
        if not guess_result:
            print("Guess again.")
            number_of_attempts -= 1
else:
    print("No such game level :( ")


# Choose a difficulty. Type 'easy' or 'hard': hard


# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Pssst, the correct answer is 47
# Choose a difficulty. Type 'easy' or 'hard': hard
# You have 5 attempts remaining to guess the number.
# Make a guess: 50
# Too high.
# Guess again.
# You have 4 attempts remaining to guess the number.
# Make a guess: 25
# Too low.
# Guess again.
# You have 3 attempts remaining to guess the number.
# Make a guess: 40
# Too low.
# Guess again.
# You have 2 attempts remaining to guess the number.
# Make a guess: 45
# Too low.
# Guess again.
# You have 1 attempts remaining to guess the number.
# Make a guess: 46
# Too low.
# You've run out of guesses, you lose.