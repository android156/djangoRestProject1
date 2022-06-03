from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from todoapp.models import Project, ToDo
from todoapp.views import ToDoModelViewSet, ProjectModelViewSet
from userapp.views import AppUserModelViewSet
from .views import MessageModelViewSet
from userapp.models import AppUser
from .models import Message
from django.contrib.auth.models import User

from django.test import TestCase


# Create your tests here.


class TestMessagesSet2(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/messages/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_message_admin(self):
        user = AppUser.objects.create(first_name='Юра', last_name='Лужков', user_name='luzhok',
                                      email='luzhok@moscow.ru', user_category=AppUser.MANAGER_STATUS)
        user2 = AppUser.objects.create(first_name='Василий', last_name='Блаженный', user_name='crazy_vasya',
                                       email='crazyV@moscow.ru')
        user3 = mixer.blend(AppUser, uid='00000000-0000-0000-0000-000000000000')
        user4 = mixer.blend(AppUser, uid='11111111-0000-0000-0000-000000000000')

        # ТУТ РАБОТАЕТ ЭТО!!!
        message = Message.objects.create(text='Тестовое сообщение1', sender=user)
        message.recipients.add(user3)
        message.save()

        # ТУТ РАБОТАЕТ И ЭТО!!!
        message.recipients.create(first_name='Саня', last_name='Копытин', user_name='kopyto',
                                  email='sanya_kopyto@mail.ru')
        message.save()

        # Через _set и related не работает.

        # message.recipients_set.create(first_name='Петя', last_name='Скунсов', user_name='skuns',
        #                               email='skuns1945@mail.ru')
        # message.recipients_set.add(user4)
        # message.save()
        #
        # print(message.related.all())

        print(message)
        admin = User.objects.create_superuser('admin156', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin156', password='admin123456')

        message2 = mixer.blend(Message, recipients=[user.uid, user2.uid])

        data = {
            'text': 'Тестовое сообщение2',
            'sender': user2.uid,
            'recipients': [user2.uid, ]
        }
        print(f"Старое сообщение1 {self.client.get(f'/api/messages/{message.uid}/').data}")
        # patch и put работают!!!
        response = self.client.put(f'/api/messages/{message.uid}/', data)
        print(f"Новое сообщение1 {self.client.get(f'/api/messages/{message.uid}/').data}")
        print(f"Сообщение из миксера {self.client.get(f'/api/messages/{message2.uid}/').data}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        message = Message.objects.get(uid=message.uid)
        self.assertEqual(message.text, 'Тестовое сообщение2')
        self.assertEqual(message.sender.uid, user2.uid)


