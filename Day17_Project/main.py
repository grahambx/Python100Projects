# Udemy 100 Projects in 100 days
# Day 17 Project
# QUIZ MACHINE
# Skills: OOP, Modules, Libraries, Classes, Objects
# Notes:

from data import question_data                # Question data in JSON KVP format
from question_model import Question           # Class Used to convert questions from above into a question object
from quiz_brain import QuizBrain              # Class used to run a quiz for duration of questions

# Use Question object to convert all input questions into Question objects that are added to Question bank
question_bank = []
for question in question_data:
    question_bank.append(Question(question))

# Initiate a quiz object from class
quiz = QuizBrain(question_bank)

# loop through questions in quiz object
while quiz.still_has_questions():
    quiz.next_question()

# final output
print("You've finished the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
