from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cesar(start_text, shift_amount, cipher_direction):
    cipher_text = ''
    max_letters = len(alphabet)
    if shift_amount >= len(alphabet):
        shift_amount = shift_amount % max_letters
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position >= max_letters:
                new_position = new_position - max_letters
            elif new_position < 0:
                new_position = max_letters + new_position
            new_letter = alphabet[new_position]
        else:
            new_letter = char

        cipher_text += new_letter
    print(f"The {cipher_direction}d text is {cipher_text}")


print(logo)
play_again = 'yes'
while play_again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cesar(cipher_direction=direction, start_text=text, shift_amount=shift)
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

print("Goodbye.")

