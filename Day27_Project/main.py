# Udemy 100 Projects in 100 days
# Day 27 Project
# MILES TO KM TKINTER GUI
# Skills: tkinter, window, components
# Notes:

from tkinter import *


def button_clicked():
    miles = int(miles_input.get())
    km = round(miles * 1.609, 1)  # Round to 1 decimal point
    km_result_label.config(text=f"{km}")


# Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=180)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
# user_input.config(padx=10, pady=10)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)
km_result_label.config(padx=10, pady=10)

km_label = Label(text="km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)
calc_button.config(padx=10, pady=10)

window.mainloop()
