import random
from django.http import JsonResponse
from django.shortcuts import render

QUESTIONS = [
    {"question": "What is the capital of France?",
     "options": ["Paris", "London", "Rome", "Berlin"],
     "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?",
     "options": ["Earth", "Mars", "Venus", "Saturn"],
     "answer": "Mars"},
    {"question": "2 + 2 = ?",
     "options": ["3", "4", "5", "6"],
     "answer": "4"},
]

def ai_challenge_page(request):
    return render(request, "ai_challenge.html")

def get_ai_quiz_question(request):
    question = random.choice(QUESTIONS)
    return JsonResponse({
        "question": question["question"],
        "options": question["options"],
    })

def ai_answer_question(request):
    question_text = request.GET.get("question")

    q = next(item for item in QUESTIONS if item["question"] == question_text)
    correct_answer = q["answer"]

    ai_skill = 0.55  # AI không quá giỏi

    if random.random() < ai_skill:
        ai_answer = correct_answer
    else:
        ai_answer = random.choice([o for o in q["options"] if o != correct_answer])

    return JsonResponse({
        "ai_answer": ai_answer,
        "correct_answer": correct_answer,
        "is_correct": ai_answer == correct_answer,
    })
