from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip



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
    s_website = entry_website.get()
    s_username = entry_username.get()
    s_password = entry_password.get()

    if len(s_website) == 0 or len(s_username) == 0 or len(s_password) == 0:
        messagebox.showinfo(title="Oops", message="None of the fields should be empty!")
    else:
        is_ok = messagebox.askokcancel(title=s_website, message=f"These are the details entered: \nEmail: {s_username} "
                               f"\n Password: {s_password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{s_website} | {s_username} | {s_password}\n")
            # clear fields:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


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
canvas.grid(row=0,column=1)
label_website = Label(text="Website:", bg=WHITE, fg=FONT_COLOR, font=(FONT_NAME, FONT_SIZE))
label_website.grid(row=1, column=0, sticky=NE)
label_username = Label(text="Email/Username:", bg=WHITE, fg=FONT_COLOR, font=(FONT_NAME, FONT_SIZE))
label_username.grid(row=2, column=0, sticky=NE)
label_passwrd = Label(text="Password:", bg=WHITE, fg=FONT_COLOR, font=(FONT_NAME, FONT_SIZE))
label_passwrd.grid(row=3, column=0, sticky=E)

entry_website = Entry(width=43)
entry_website.insert(END, string="")
entry_website.grid(row=1, column=1, columnspan=2)
entry_username = Entry(width=43)
entry_username.insert(0, string="piotr.czeczko@gmail.com")
entry_username.grid(row=2, column=1, columnspan=2)
entry_password = Entry(width=24)
entry_password.insert(END, string="")
entry_password.grid(row=3, column=1, sticky=E)
button_generate_password = Button(text="Generate Password", command=generate_password, highlightthickness=0)
button_generate_password.grid(row=3, column=2, sticky=NW)
button_add = Button(text="Add", width=41, command=save, highlightthickness=0)
button_add.grid(row=4, column=1, columnspan=2)



window.mainloop()
