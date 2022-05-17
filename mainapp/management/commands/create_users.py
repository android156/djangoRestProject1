from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mainapp.models import AppUser
import json, os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('app_users')
        super_user = User.objects.create_superuser('admin', 'admin@todo.ru', 'admin')

