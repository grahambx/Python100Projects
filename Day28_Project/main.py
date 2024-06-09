# Udemy 100 Projects in 100 days
# Day 28 Project
# POMODORO GUI APP
# Skills: tkinter, window, canvas, Gui Loops, Colorhunt, Global,
# Notes:

from tkinter import *
import math

# Can use colorhunt.co to get colour palette themes that give hexcode
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# below, reps needs to be global as accessed in multiple functions. As using a GUI based program code needs to get
# to window.mainloop() where it sits listening. Everything then has to be defined behind window actions like clicking
# buttons
reps = 0
# below object will be mapped to windows.after method, but needs to be access from 2 functions so need to declare
# as global, can use None keyword and it will be changed later
timer = None


def start_timer():
    """Timer Mechanism, tracks position in Pomodoro sequence 'reps'.
    Defines next part of sequence and calls the count_down.
    Updates Pomodoro Header text as per pomodoro phase"""
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label_header.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label_header.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label_header.config(text="Work", fg=GREEN)


def count_down(count):
    """Countdown Mechanism. Takes duration from start_timer function based on current pomodoro phase.
    Resolves the clock text. Creates a windows.after() loop to act as the countdown mechanism
    Once at 00:00 i) calls start_timer to move to next pomodoro phase ii) recalculates completed work phases
    iii) updates this as a displayed string of ticks"""
    # show 4:02 instead of 4:2 in timer text
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # create a timer loop using window.after, needs to be global as can be cancelled by timer_rest()
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    # below requirements when timer hits 00:00
    else:
        start_timer()
        checks_needed = math.floor(reps / 2)
        string = ""
        for i in range(checks_needed):
            string += "✔"
        label_track.config(text=string, fg=GREEN)


def reset_timer():
    """Timer Reset Function. Resets the 'reps' count and all labels back to default.
    Cancels the window_after object which is set in the count_down function and acts as our timer"""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")  # Note different methods to change canvas vs window objects
    label_header.config(text="Timer", fg=GREEN)  # above is canvas object, here and below are window objects
    label_track.config(text="", fg=GREEN)
    global reps
    reps = 0


# Window Object set up
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas object to hold the pomodoro graphic and count down text
# Note import a png in Pycharm, open to see size and half it to centre
# PhotoImage object defined 1st as this is only class create_image() can accept
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# The remainder of the tkinter objects to be displayed in window
label_header = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
label_header.grid(column=1, row=0)

button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

label_track = Label(text="", bg=YELLOW, fg=GREEN)
label_track.grid(column=1, row=3)

window.mainloop()
