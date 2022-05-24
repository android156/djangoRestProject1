from django.db import models
from uuid import uuid4

# Create your models here.
from userapp.models import AppUser


class Project(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    users = models.ManyToManyField(AppUser, blank=True)

    def __str__(self):
        return f'{self.name} - {self.description}'


class ToDo(models.Model):
    class Meta:
        ordering = ['-updated']

    uid = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(AppUser, verbose_name='Пользователь', db_index=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name='Проект', db_index=True, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст задания', blank=True)
    created = models.DateTimeField(verbose_name='Задание создано', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Задание обновлено', auto_now=True)
    is_active = models.BooleanField(verbose_name='Задание активно')

    def __str__(self):
        return f'{self.text} - Ответственный {self.user.user_name}, Проект {self.project.name}'
