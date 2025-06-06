#Asking Questions
#Checking if answer is correct
#Checking if at end of Question List

from main import question_bank


class QuizBrain:
    question_no = 0
    question_bank = []
    score = 0

    def next_question(self):
        self.question_no += 1

    def end_of_list(self):
        if self.question_no == len(self.question_bank):
            return True

    def __init__(self, questionbank):
        self.question_no = 0
        self.question_bank = questionbank
        self.score = 0

        for question in question_bank:
            if self.end_of_list():
                break
            self.next_question()
            print("Q." + str(self.question_no) + " " + str(question.Q) + "(True/False)")
            answer = input()
            if answer == question.A:
                self.score += 1
                print("Correct!!")
                print("Your score is " + str(self.score) + "\n")
            else:
                print("Wrong")
                print("Your score is " + str(self.score) + "\n")


quiz = QuizBrain(question_bank)
