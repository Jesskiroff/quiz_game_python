
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


question_1 = Question("The question model works.", "True")
question_2 = Question("2 + 2 equals 5.", "False")

print(question_1.text)