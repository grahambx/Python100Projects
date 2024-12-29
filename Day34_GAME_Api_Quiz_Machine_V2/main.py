# Day 34 Project
# QUIZ MACHINE V2
# Skills: tkinter, OOP, API
# Notes: Day17 > Day34

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# take the questions from data.question_data and turn into list of tuples (question, answer)
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Note have created a Question class, see question_model, don't think this is strictly necessary
    # but helps enforce integrity?
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuiBrain object using the question_bank, then create a UI passing in this quiz object
# Note the UI controls the loop etc
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
