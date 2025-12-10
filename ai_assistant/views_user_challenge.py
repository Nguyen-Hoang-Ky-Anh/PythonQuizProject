from django.shortcuts import render
from django.http import JsonResponse
from ai_model.ai_model import ask_ai

def user_challenge_view(request):
    if request.method == "POST":
        user_question = request.POST.get("question", "").strip()

        if not user_question:
            return JsonResponse({"error": "Bạn phải nhập câu hỏi!"})

        ai_answer = ask_ai(user_question)

        return JsonResponse({
            "question": user_question,
            "ai_answer": ai_answer
        })

    return render(request, "user-challenge.html")
