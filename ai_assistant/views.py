from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from ai_model.ai_model import ask_ai
from quizzes.models import Question


def user_challenge_view(request):
    """
    Trang cho người dùng nhập câu hỏi vào để hỏi AI.
    """
    if request.method == "POST":
        user_question = request.POST.get("question", "")

        if not user_question.strip():
            return JsonResponse({"error": "Bạn phải nhập câu hỏi!"})

        # Gửi câu hỏi đến AI
        ai_answer = ask_ai(user_question)

        return JsonResponse({
            "question": user_question,
            "ai_answer": ai_answer
        })

    return render(request, "user-challenge.html")
    


def ai_quiz_check_view(request, question_id):
    """
    AI trả lời câu hỏi trong hệ thống QUIZ và kiểm tra đúng/sai.
    """
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return JsonResponse({"error": "Câu hỏi không tồn tại."})

    # Gửi câu hỏi quiz cho AI
    ai_reply = ask_ai(question.question)

    # Kiểm tra đúng sai
    is_correct = question.correct_answer.lower() in ai_reply.lower()

    return JsonResponse({
        "question": question.question,
        "correct_answer": question.correct_answer,
        "ai_reply": ai_reply,
        "is_correct": is_correct
    })
