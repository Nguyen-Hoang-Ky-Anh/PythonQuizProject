from django.urls import path
from .views_user_challenge import user_challenge_view
from .views_ai_quiz import ai_quiz_check_view
from .views_ai_challenge import (
    ai_challenge_page,
    get_ai_quiz_question,
    ai_answer_question
)

urlpatterns = [
    path("user-challenge/", user_challenge_view, name="user_challenge"),
    path("ai-quiz/<int:question_id>/", ai_quiz_check_view, name="ai_quiz_check"),

    path("ai-challenge/", ai_challenge_page, name="ai_challenge"),
    path("ai-challenge/get-question/", get_ai_quiz_question, name="ai_get_question"),
    path("ai-challenge/answer/", ai_answer_question, name="ai_answer_question"),
]
