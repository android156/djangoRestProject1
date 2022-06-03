from uuid import uuid4

from django.db import models

# Create your models here.
from userapp.models import AppUser


class Message(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    text = models.TextField(verbose_name='Текст сообщения', blank=True)
    sender = models.ForeignKey(AppUser, related_name='user_sender', verbose_name='Отправитель',
                               on_delete=models.CASCADE)
    recipients = models.ManyToManyField(AppUser, related_name='user_recipients', verbose_name='Получатели',
                                        db_index=True, blank=True)
    created = models.DateTimeField(verbose_name='Задание создано', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Задание обновлено', auto_now=True)
    sent = models.DateTimeField(verbose_name='Отправлено', blank=True, null=True)
