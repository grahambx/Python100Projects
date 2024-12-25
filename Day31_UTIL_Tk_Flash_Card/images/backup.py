# Day 30 Project
# PASSWORD MANAGER APP V2
# Skills: tkinter, window, canvas, Gui Loops, messagebox, clipboard, columnspan, list comprehension, Exceptions, json
# Notes: Day05 > Day29 > Day30

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/spanish_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card_wrong():
    # create a current_card with random record (Spanish + English)
    # 3rd line current_card["Spanish"] is the key and will return the value
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_value, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(canvas_img, image=img_card_front)
    flip_timer = window.after(3000, func=flip_card)


def next_card_right():
    # create a current_card with random record (Spanish + English)
    # 3rd line current_card["Spanish"] is the key and will return the value
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    print(to_learn)
    print(current_card)
    print(len(to_learn))
    to_learn.remove(current_card)
    current_card = random.choice(to_learn)
    print(len(to_learn))

    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_value, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(canvas_img, image=img_card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_value, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=img_card_back)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# create image objects
img_card_front = PhotoImage(file="images/card_front.png")
img_card_back = PhotoImage(file="images/card_back.png")
img_wrong = PhotoImage(file="images/wrong.png")
img_right = PhotoImage(file="images/right.png")

# create card as a canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=img_card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_value = canvas.create_text(400, 300, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# create right and wrong buttons
button_wrong = Button(image=img_wrong, highlightthickness=0, command=next_card_wrong)
button_wrong.grid(row=1, column=0)
button_right = Button(image=img_right, highlightthickness=0, command=next_card_right)
button_right.grid(row=1, column=1)

# Call the next_card after UI created, so we always start with a card showing
# A function call like this to initialise needs to happen before the mainloop
next_card_wrong()

window.mainloop()
