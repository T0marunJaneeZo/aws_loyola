from django.contrib.auth.models import AbstractUser
from django.db import models

#　暫時的なクラス設計＿後々整形する
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin_staff', 'Admin Staff'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')

    def __str__(self):
        return self.username


