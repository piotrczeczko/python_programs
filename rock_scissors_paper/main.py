# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''    ,--.--._
---" _, \___)
     / _/____)
     \//(____)
---\     (__)
    `-----"'''

paper = '''     _.-._
    | | | |_
    | | | | |
    | | | | |
  _ |  '-._ |
  \`\`-.'-._;
   \    '   |
    \  .`  /
     |    |'''

scissors = '''    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''



list_figures = [rock,scissors,paper]


def print_figures(user_choice, computer_choice):
    print("\n\n")
    print(list_figures[user_choice-1])
    print("     vs")
    print(list_figures[computer_choice-1])

def choose_figure():
    print("Choose: ")
    print("1. rock")
    print("2. scissors")
    print("3. paper")
    try:
        user_choice = int(input())
    except:
        user_choice = 5
    computer_choice = random.randint(1,3)
    return user_choice, computer_choice


def compare_results(user_choice, computer_choice):
    if user_choice == computer_choice:
        print_figures(user_choice, computer_choice)
        print("Draw!\nTry again...\n")
        return 1
    elif user_choice == 1 and computer_choice == 2:
        print_figures(user_choice, computer_choice)
        print("You win!")
        return 0
    elif user_choice == 1 and computer_choice == 3:
        print_figures(user_choice, computer_choice)
        print("You lose.\nTry again...\n")
        return 1
    elif user_choice == 2 and computer_choice == 1:
        print_figures(user_choice, computer_choice)
        print("You lose.\nTry again...\n")
        return 1
    elif user_choice == 2 and computer_choice == 3:
        print_figures(user_choice, computer_choice)
        print("You win!")
        return 0
    elif user_choice == 3 and computer_choice == 1:
        print_figures(user_choice, computer_choice)
        print("You win!")
        return 0
    elif user_choice == 3 and computer_choice == 2:
        print_figures(user_choice, computer_choice)
        print("You lose.\nTry again...\n")
        return 1
    else:
        print("You wrote invalid number!. You lose.\nTry again...\n")
        return 1


x = 1
while x == 1:
    user_choice, computer_choice = choose_figure()
    x = compare_results(user_choice, computer_choice)


