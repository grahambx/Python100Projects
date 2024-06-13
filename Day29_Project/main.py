# Udemy 100 Projects in 100 days
# Day 29 Project
# PASSWORD MANAGER APP
# Skills: tkinter, window, canvas, Gui Loops, messagebox, clipboard, columnspan, list comprehension
# Notes: has repurposed and refined Day 5's password generate using list comprehension

from random import choice, randint, shuffle
import pyperclip  # allows you to copy or paste to os clipboard
from tkinter import *
from tkinter import messagebox
# messagebox is not a class, but a module of code, so have to specify it even though we have * (which is only classes)


def generate_password():
    """password generator - adapted from day 5, creates random password and adds to the entry box"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_pass.delete(0, END)
    entry_pass.insert(0, password)
    pyperclip.copy(password)  # can use .paste to extract from clipboard


def save_password():
    """Saves the website, login email and password to a text file.
    Runs some checks first to ensure values added"""
    site = entry_site.get()
    email = entry_email.get()
    password = entry_pass.get()

    to_save = f"{site} | {email} | {password}"
    if len(site) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oi!!!", message="Ensure website and password added")
    else:
        option = messagebox.askokcancel(title=str(entry_site),
                                        message=f"Are you sure you want to save the following?\n{to_save}")
        if option:
            with open("data.txt", mode="a") as file:
                file.write(f"{to_save}\n")
                entry_pass.delete(0, END)  # from 1st char to end
                entry_site.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


FONT = ("Arial", 14, "normal")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_site = Label(text="Website:", bg="white", font=FONT)
label_site.grid(column=0, row=1)

label_email = Label(text="Email/Username:", bg="white", font=FONT)
label_email.grid(column=0, row=2)

label_pass = Label(text="Password:", bg="white", font=FONT)
label_pass.grid(column=0, row=3)

entry_site = Entry(width=40)
entry_site.grid(column=1, row=1, columnspan=2)
entry_site.focus()

entry_email = Entry(width=40)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "madeup@gmail.com")  # note can use END index to insert after any existing string

entry_pass = Entry(width=21)
entry_pass.grid(column=1, row=3)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()
