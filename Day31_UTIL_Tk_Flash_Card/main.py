# Day 31 Project
# FLASH CARD APP
# Skills: tkinter, window, canvas, window.after, exceptions, pandas, csv
# Notes: Day05 > Day29 > Day30

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Need an original list of card and a still to learn list csvs
# Still to learn will not exist on first run to catch this
try:
    data = pandas.read_csv("data/spanish_words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    # create a new current_card with random record (Spanish + English)
    # Cards will flip to show answers after 3 seconds. when clicking next card we have to cancel the timer
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    # Set canvas items for a new card being shown, note flip_card called at end will flip these values too
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_value, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(canvas_img, image=img_card_front)

    # reset the timer for 3 seconds, after this call the flip_card function to flip card
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # 3 seconds after a card is shown this will run flipping to back of card and setting canvas values
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_value, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=img_card_back)


def user_card_right():
    # user clicks the tick to say "yes i know this" so we remove it from the to_learn list and overwrite the
    # to_learn file with the reduced dataset
    global current_card, to_learn
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/spanish_words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Need to start a flip timer on 1st run
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

# create right (user knew answer = has learnt) and wrong buttons
button_wrong = Button(image=img_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)
button_right = Button(image=img_right, highlightthickness=0, command=user_card_right)
button_right.grid(row=1, column=1)

# Call the next_card after UI created, so we always start with a card showing
# A function call like this to initialise needs to happen before the mainloop
# Note higher in the UI section we also start the timer for the first card
next_card()

window.mainloop()
