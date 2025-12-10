from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from quizzes.models import Question
from ai_model.ai_model import ask_ai_for_quiz

def user_vs_ai(request):
question = Question.objects.order_by("?").first()  # random 1 câu

```
user_answer = None
ai_answer = None
result_user = None
result_ai = None

if request.method == "POST":
    user_answer = request.POST.get("answer")

    # AI trả lời
    ai_answer = ask_ai_for_quiz(
        question_text := f"Câu hỏi: {question.text}\nA: {question.option_a}\nB: {question.option_b}\nC: {question.option_c}\nD: {question.option_d}\nTrả lời theo A/B/C/D.",
        correct_answer=question.correct_answer
    )

    # Check user
    result_user = (user_answer.upper() == question.correct_answer.upper())

    # Check AI
    result_ai = (question.correct_answer.upper() in ai_answer.upper())

return render(request, "user_challenge.html", {
    "question": question,
    "user_answer": user_answer,
    "ai_answer": ai_answer,
    "result_user": result_user,
    "result_ai": result_ai,
})
```
