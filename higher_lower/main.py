from art import *
from replit import clear
import random

score_table = { "user1": 20,
                "user2": 50,
                "user3": 30,
                "user4": 1000,
                "user5": 1001,
                "user6": 1,
                "user7": 101,
                "user8": 201,
                "user9": 301,
                "user10": 11,
                }

# choose user and exclude already chosen:
def choose_person(chosen_A = None):
    user_numbers = len(score_table)
    if chosen_A is None:
        chosen_A = random.choice(list(score_table.items()))[0]
    chosen_B = chosen_A
    while chosen_A == chosen_B:
        chosen_B = random.choice(list(score_table.items()))[0]
    return chosen_A, chosen_B


user_A = None
user_B = None
end_game = False
current_score = 0
while not end_game:
    clear()
    print(logo)
    if user_A is not None:
        print(f"You're right! Current score: {current_score}")
    user_A, user_B = choose_person(user_A)
    print(f"Compare A: {user_A}")
    print(vs)
    print(f"Against B: {user_B}")
    user_choice = input(f"Who has more followers? Type 'A' or 'B': ").upper()
    if user_choice == "A" and score_table[user_A] >= score_table[user_B]:
        current_score += 1
    elif user_choice == "B" and score_table[user_B] >= score_table[user_A]:
        current_score += 1
        user_A = user_B
    else:
        end_game = True

print(f"Sorry, that's wrong. Final score: {current_score}")

