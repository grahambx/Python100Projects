class Question:
    """pass in a dictionary item to pull out values for defined question and answer keys"""
    def __init__(self, dict_item):
        self.text = dict_item["text"]
        self.answer = dict_item["answer"]
