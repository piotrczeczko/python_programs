import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x','y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z'
           ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

welcome = "Welcome to the PyPassword Generator!\n"

print(welcome)
nb_letters = int(input("How many letters would you like in your password?\n"))
nb_symbols = int(input("How many symbols would you like?\n"))
nb_numbers = int(input("How many numbers would you like?\n"))

password = []
for x in range(0,nb_letters):
    #password.append(letters[random.randint(0, len(letters)-1)])
    password.append(random.choice(letters))

for x in range(0,nb_symbols):
    #password.append(symbols[random.randint(0, len(symbols)-1)])
    password.append(random.choice(symbols))

for x in range(0,nb_numbers):
    #password.append(numbers[random.randint(0, len(numbers)-1)])
    password.append(random.choice(numbers))

random.shuffle(password)
password = ''.join(password)

print(f"Here is your password: {password}")