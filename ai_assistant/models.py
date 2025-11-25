from django.db import models
from users.models import User
from quizzes.models import Quiz

# Create your models here.
class AIFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.user.username} - {self.quiz.title}"