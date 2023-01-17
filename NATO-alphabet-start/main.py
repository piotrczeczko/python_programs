import pandas
#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(letter_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Please provide the word: ").upper()
    try:
        word_spelled_nato = [letter_dict[i] for i in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(word_spelled_nato)


generate_phonetic()


