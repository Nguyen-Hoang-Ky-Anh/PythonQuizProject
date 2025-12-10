from django.http import JsonResponse
from quizzes.models import Question
from ai_model.ai_model import ask_ai

def ai_quiz_check_view(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return JsonResponse({"error": "Câu hỏi không tồn tại."})

    ai_reply = ask_ai(question.question)

    is_correct = question.correct_answer.lower() in ai_reply.lower()

    return JsonResponse({
        "question": question.question,
        "correct_answer": question.correct_answer,
        "ai_reply": ai_reply,
        "is_correct": is_correct,
    })
