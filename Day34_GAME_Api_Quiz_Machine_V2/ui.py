# This is the UI for the quiz, called by main
# Requires a QuizBrain object to be passed in by main (this also will have the questions)
# Uses window.mainloop()
# This is all UI settings and reaches into the QuizBrain object and its methods as needed, outcomes result in UI changes

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # create score
        # TODO: Score board needs to update
        self.label_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "bold"))
        self.label_score.grid(row=0, column=1)

        # create question card as canvas
        self.canvas = Canvas(width=400, height=250, bg="white", highlightthickness=0)
        self.card_text = self.canvas.create_text(
            200,
            125,
            width=380,
            text="test",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # create true / false buttons
        # TODO: Add commands
        img_false = PhotoImage(file="images/false.png")
        img_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=img_true, highlightthickness=0, command=self.check_if_true)
        self.button_true.grid(row=2, column=0)
        self.button_false = Button(image=img_false, highlightthickness=0, command=self.check_if_false)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.label_score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.card_text, text=q_text)
        else:
            self.canvas.itemconfig(self.card_text, text="You have finished the Quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_if_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_if_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
