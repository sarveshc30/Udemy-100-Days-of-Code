from question_model import Question
from data import question_data

question_bank = []

for i in range(12):
    new_question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(new_question)

print(question_bank)
