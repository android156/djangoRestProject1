import json
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from userapp.models import AppUser


JSON_PATH = 'userapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-16') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('app_users')
        AppUser.objects.all().delete()
        for user in users:
            new_user = AppUser(**user)
            new_user.save()
        User.objects.all().delete()
        super_user = User.objects.create_superuser('admin', 'admin@todo.ru', 'admin')
