BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

french = pandas.read_csv("data/Arabic.csv")
english = french.to_dict(orient="records")
current_card = {}
english = {}

back_image = PhotoImage(file="images/card_back.png")

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Arabic.csv")
    english = original_data.to_dict(orient="records")
else:
    english = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(english)
    canvas.itemconfig(title_text, text="Arabic", fill="black")
    canvas.itemconfig(word_text, text=current_card["Arabic"], fill="black")
    canvas.itemconfig(front_image, image=my_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(front_image, image=back_image)


def is_known():
    english.remove(current_card)
    data = pandas.DataFrame(english)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
my_image = PhotoImage(file="card_front.png")
front_image = canvas.create_image(410, 280, image=my_image)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
