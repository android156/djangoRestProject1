from django.db import models
from uuid import uuid4

# Create your models here.


class User(models.Model):
    CATEGORY_CHOICES = (
        ('A', 'Администратор'),
        ('M', 'Менеджер проекта'),
        ('D', 'Разработчик'),
    )
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    user_name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    user_category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, blank=True)

