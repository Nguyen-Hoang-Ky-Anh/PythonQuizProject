from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

LEVEL_CHOICES = (
    ('Beginner', 'Beginner'),
    ('Elementary', 'Elementary'),
    ('Pre-intermediate', 'Pre-intermediate'),
    ('Intermediate', 'Intermediate'),
    ('Upper-intermediate', 'Upper-intermediate'),
    ('Advanced', 'Advanced'),
)
    
LEARNING_STYLE_CHOICES = (
    ('Visual', 'Visual'),
    ('Auditory', 'Auditory'),
    ('Kinesthetic', 'Kinesthetic'),
    ('Reading/Writing', 'Reading/Writing'),
)
class User(AbstractUser):
    # ví dụ thêm role
    is_admin = models.BooleanField(default=False)
    
    age = models.PositiveIntegerField(null=True, blank=True)
    declared_level = models.CharField(max_length=20, choices=LEVEL_CHOICES, null=True, blank=True)
    goals = models.TextField(null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    referred_frequency = models.CharField(max_length=100, null=True, blank=True)
    motivation_level = models.PositiveSmallIntegerField(null=True, blank=True)  # 1-5
    learning_style = models.CharField(max_length=20, choices=LEARNING_STYLE_CHOICES, null=True, blank=True)
    
    def is_learner(self):
        return self.user_type == 'learner'
    
    def is_admin(self):
        return self.user_type == 'admin'
    
    