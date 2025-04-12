from data import qa_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for qst in qa_data:
    q = Question(qst["question"], qst["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final SCORE:{quiz.score}/{len(question_bank)}")