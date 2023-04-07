from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system as sys
sys("cls")
question_bank = []
for question in range(len(question_data)):
    question_loop = Question(question_data[question]["text"],question_data[question]["answer"])
    question_bank.append(question_loop)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")

