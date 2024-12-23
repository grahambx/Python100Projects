# Udemy 100 Projects in 100 days
# Day 30 Project
# PASSWORD MANAGER APP V2
# Skills: tkinter, window, canvas, Gui Loops, messagebox, clipboard, columnspan, list comprehension, Exceptions, json
# Notes: Day05 > Day29 > Day30

from random import choice, randint, shuffle
import pyperclip  # allows you to copy or paste to os clipboard
from tkinter import *
from tkinter import messagebox
import json
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
    website = entry_site.get()
    email = entry_email.get()
    password = entry_pass.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oi!!!", message="Ensure website and password added")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Read existing data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                # Create and Write full file back
                json.dump(new_data, file, indent=4)
        else:
            # Add new_data to existing data
            data.update(new_data)
            with open("data.json", mode="w") as file:
                # Write full file back
                json.dump(data, file, indent=4)
        finally:
            entry_pass.delete(0, END)  # from 1st char to end
            entry_site.delete(0, END)


def search_site():
    website = entry_site.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No Data File found")
    else:
        # I originally wrote below as try except statement, if else is clearer
        # guidance is if you can easily use an if else then use it
        # in the above opening of a file the easiest way is just to try to open it
        # this also creates a specific exception to handle
        # Another way to think of it is an Exception should be rare, whereas if else will frequently have
        # different outcomes
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showwarning(title=f"{website}", message=f" Website:     {website}\n Email:          {email}\n "
                                                               f"Password:   {password}")
        else:
            messagebox.showwarning(title="Website not Found", message=f"No results for:    {website}")


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

entry_site = Entry(width=30)
entry_site.grid(column=1, row=1)
entry_site.focus()

entry_email = Entry(width=56)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "madeup@gmail.com")  # note can use END index to insert after any existing string

entry_pass = Entry(width=30)
entry_pass.grid(column=1, row=3)

button_generate = Button(text="Generate Password", width=21, command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=48, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)

button_search = Button(text="Search", width=21, command=search_site, bg="cyan")
button_search.grid(column=2, row=1)

window.mainloop()
