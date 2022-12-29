from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

#def choose_card(nb_cards=1):
def choose_card():
    #return random.sample(cards, nb_cards)
    return random.choice(cards)

points_limit = 21
for i in range(2):
#user_cards = choose_card(2)
    user_cards.append(choose_card())
    computer_cards.append(choose_card())

user_score = sum(user_cards)
computer_score = sum(computer_cards)
#computer_cards = choose_card(2)



print(logo)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer first card: {computer_cards[0]}")

get_new_card = 'y'
end_game = False
while get_new_card == 'y':
    get_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_new_card == 'y':
        #user_cards += choose_card()
        user_cards.append(choose_card())
        user_score += user_cards[-1]
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")
    if user_score == points_limit:
        get_new_card = 'n'
        print("You win! :D")
        end_game = True
    elif user_score > points_limit:
        get_new_card = 'n'
        print("You lose :(")
        end_game = True

if not end_game:
    # check computer cards:
    while computer_score <  user_score and computer_score <= points_limit:
        #computer_cards += choose_card()
        computer_cards.append(choose_card())
        computer_score += computer_cards[-1]
        if computer_score > user_score and computer_score <= points_limit:
            print(f"Computer cards: {computer_cards}, current score: {computer_score}")
            print("Computer win :(")
            end_game = True
        elif computer_score > user_score and computer_score > points_limit:
            print(f"Computer cards: {computer_cards}, current score: {computer_score}")
            print("You win! :)")
            end_game = True
        elif computer_score == user_score and computer_score == points_limit:
            print(f"Computer cards: {computer_cards}, current score: {computer_score}")
            print("Draw!")
            end_game = True


# starting_cards("user")
# starting_cards("computer")
# print(user_cards)
# print(computer_cards)

# Main program:
# get_another_card = 'y'
# while get_another_card == 'y':
#     choose_card()



# Your cards: [4, 10], current score: 14
# Computer's first card: 2
# Type 'y' to get another card, type 'n' to pass: