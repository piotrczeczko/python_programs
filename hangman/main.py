import random
from replit import clear
from hangman_words import *
from hangman_art import *



# Randomly choose the word from the word_list:
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# create an empty list from chosen word:
display = ['_'] * word_length
nb_mistakes = 0
max_mistakes = len(hangmanpictures) - 1
end_game = False

clear()
print(logo)
while not end_game:
    guess_result = False
    #print(f'The word is: {chosen_word}')
    print(f"\n{' '.join(display)}\n")
    # Ask the user to guess a letter and assign their answer to a variable. Make guess lowercase.
    guess_letter = input("Guess a letter: ").lower()
    clear()
    print(logo)
    if guess_letter in display:
        guess_result = True
        print(f"You've already guessed the letter {guess_letter}. Try another one!")

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word
    letter_location = []
    for idx, letter in enumerate(chosen_word):
        if letter == guess_letter:
            letter_location.append(idx)
            display[idx] = letter
            guess_result = True

    if not guess_result:
        nb_mistakes += 1
        print(f"Given letter \"{guess_letter}\" is not in the word. You lose a life.")
    if '_' not in display:
        #print(f"\n{' '.join(display)}\n")
        print("You win!")
        end_game = True
    elif nb_mistakes == max_mistakes:
        #print(f"\n{' '.join(display)}\n")
        print("You lose :( ")
        print(f"The word was: {chosen_word}")
        end_game = True
    print(hangmanpictures[nb_mistakes])