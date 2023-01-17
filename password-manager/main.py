import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FILE_NAME = "data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    entry_password.delete(0, END)
    entry_password.insert(0, string=password)
    #return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="None of the fields should be empty!")
    else:
        try:
            with open(FILE_NAME, "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(FILE_NAME, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(FILE_NAME, "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


def find_password():
    website = entry_website.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Website shouldn't be empty!")
    else:
        try:
            with open(FILE_NAME, "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
        else:
            if website in data:
                messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for website: {website}")



# ---------------------------- UI SETUP ------------------------------- #
WHITE = "white"
FONT_NAME = "arial"
FONT_COLOR = "black"
FONT_SIZE = 11
window = Tk()

window.title("Password Manager v1.0")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=WHITE)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
###
label_website = Label(text="Website:", bg=WHITE, fg=FONT_COLOR, font=(FONT_NAME, FONT_SIZE))
label_website.grid(row=1, column=0, sticky=NE)
entry_website = Entry(width=24)
entry_website.insert(END, string="")
entry_website.grid(row=1, column=1)
button_search = Button(text="Search", width=16, command=find_password, highlightthickness=0)
button_search.grid(row=1, column=2, sticky=NW)
###
label_username = Label(text="Email/Username:",bg=WHITE, fg=FONT_COLOR, font=(FONT_NAME, FONT_SIZE))
label_username.grid(row=2, column=0, sticky=NE)
entry_username = Entry(width=43)
entry_username.insert(0, string="piotr.czeczko@gmail.com")
entry_username.grid(row=2, column=1, columnspan=2)
###
label_passwrd = Label(text="Password:", bg=WHITE, fg=FONT_COLOR, font=(FONT_NAME, FONT_SIZE))
label_passwrd.grid(row=3, column=0, sticky=E)
entry_password = Entry(width=24)
entry_password.insert(END, string="")
entry_password.grid(row=3, column=1, sticky=E)
button_generate_password = Button(text="Generate Password", width=16, command=generate_password, highlightthickness=0)
button_generate_password.grid(row=3, column=2, sticky=NW)
###
button_add = Button(text="Add", width=41, command=save, highlightthickness=0)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
