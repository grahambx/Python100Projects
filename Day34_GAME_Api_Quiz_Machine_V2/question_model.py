# This is effectively creating a class to make an object to make a tuple
# Not strictly necessary as very easy to put data in a tuple

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
