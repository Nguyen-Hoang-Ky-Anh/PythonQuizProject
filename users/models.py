from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # ví dụ thêm role
    is_admin = models.BooleanField(default=False)