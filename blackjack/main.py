from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def choose_card():
    #return random.sample(cards, nb_cards)
    return random.choice(cards)

points_limit = 21
for i in range(2):
    user_cards.append(choose_card())
    computer_cards.append(choose_card())

user_score = sum(user_cards)
computer_score = sum(computer_cards)


print(logo)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer first card: {computer_cards[0]}")

get_new_card = 'y'
end_game = False
while get_new_card == 'y':
    get_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_new_card == 'y':
        user_cards.append(choose_card())
        user_score += user_cards[-1]
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")
    if user_score == points_limit:
        get_new_card = 'n'
        end_game = True
    elif user_score > points_limit:
        get_new_card = 'n'
        end_game = True


if not end_game:
    while computer_score <= user_score and computer_score <= points_limit:
        computer_cards.append(choose_card())
        computer_score += computer_cards[-1]
        if computer_score > user_score and computer_score <= points_limit:
            end_game = True
        elif computer_score > user_score and computer_score > points_limit:
            end_game = True
        elif computer_score == user_score and computer_score == points_limit:
            end_game = True

## Check solutions:
print(f"Computer cards: {computer_cards}, current score: {computer_score}")
if user_score == points_limit and len(user_cards) == 2:
    print("You win! BlackJack :D")
elif computer_score == points_limit and len(computer_cards) == 2:
    print("You lose :( Computer has BlackJack ...")
elif user_score > computer_score and user_score <= points_limit:
    print("You win ! :)")
elif user_score < computer_score and computer_score <= points_limit:
    print("You lose :( ")
elif user_score == computer_score and computer_score <= points_limit:
    print("Draw ! ")
elif user_score <= points_limit and computer_score > points_limit:
    print("You win ! :)")
else:
    print("Some not coded case ... !!!")

