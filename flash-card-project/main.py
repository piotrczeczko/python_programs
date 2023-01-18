import random
import tkinter
from tkinter import *
import pandas as pd
from random import randrange, choice

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

####################################################
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient="records")
#print(to_learn)
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn) <= 0:
        canvas.itemconfig(card_title, text="English", fill="black")
        canvas.itemconfig(card_word, text="No more words!", fill="black")
        button_right.config(state=DISABLED)
        button_wrong.config(state=DISABLED)
    else:
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_background, image=image_card_front)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=image_card_back)


def if_learned_all():
    if len(to_learn) <= 0:
        canvas.itemconfig(card_title, text="English", fill="black")
        canvas.itemconfig(card_word, text="No more words!", fill="black")
        button_right.config(state=DISABLED)
        button_wrong.config(state=DISABLED)
    else:
        next_card()


def is_known():
    if len(to_learn) <= 0:
        canvas.itemconfig(card_title, text="English", fill="black")
        canvas.itemconfig(card_word, text="No more words!", fill="black")
    else:
        to_learn.remove(current_card)
        data = pd.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        if_learned_all()
        #next_card()

window = tkinter.Tk()
window.title("Flash Cards v1.0")
window.config(width=900, height=626, padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image_card_front = PhotoImage(file="images/card_front.png")
image_card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=image_card_front)
card_title = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=0)
image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=1)
#show_language_name()
next_card()


#window.after_cancel()

window.mainloop()