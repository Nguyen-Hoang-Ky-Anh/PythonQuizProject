from django.db import models
from users.models import User
from quizzes.models import Quiz, QuizAttempt
# Create your models here.
class ProgressRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    last_attempt = models.ForeignKey(QuizAttempt, on_delete=models.SET_NULL, null=True, blank=True)
    total_score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"