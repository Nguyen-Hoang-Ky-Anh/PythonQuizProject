from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from ai_model.ai_model import ask_ai

def ai_page(request):
    return render(request, "ai_page.html")

def ask_ai_view(request):
    if request.method == "POST":
        user_question = request.POST.get("question", "")
        ai_reply = ask_ai(user_question)
        return JsonResponse({"answer": ai_reply})
    return JsonResponse({"error": "Invalid request"}, status=400)
