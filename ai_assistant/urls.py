from django.urls import path
from . import views

urlpatterns = [
    path("user-challenge/", views.user_challenge_view, name="user_challenge"),
    path("ai-quiz/<int:question_id>/", views.ai_quiz_check_view, name="ai_quiz_check"),
]
