from django.db import models
from uuid import uuid4


# Create your models here.


class AppUser(models.Model):
    ADMIN_STATUS = 'A'
    MANAGER_STATUS = 'M'
    DEVELOPER_STATUS = 'D'
    status_name_dict = {
        'A': 'Администратор',
        'M': 'Менеджер проекта',
        'D': 'Разработчик',
    }
    CATEGORY_CHOICES = (
        (ADMIN_STATUS, status_name_dict[ADMIN_STATUS]),
        (MANAGER_STATUS, status_name_dict[MANAGER_STATUS]),
        (DEVELOPER_STATUS, status_name_dict[DEVELOPER_STATUS]),
    )
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    user_name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    user_category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.user_name} - {self.status_name_dict[self.user_category]}'
