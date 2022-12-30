from PythonWorkBook55.python import question_data
from python2 import Question
from python3 import QuizBrain 
from python4 import QuizInterface

question_bank = []
for question in question_data:
    question_text =question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz =QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)