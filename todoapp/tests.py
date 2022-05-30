import json
from django.test import TestCase
from mixer import factory
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ToDoModelViewSet, ProjectModelViewSet
from userapp.views import AppUserModelViewSet
from userapp.models import AppUser
from django.contrib.auth.models import User


class TestProjectViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/',
                               {
                                   'first_name': 'Юра',
                                   'last_name': 'Лужков',
                                   'user_name': 'luzhok',
                                   'email': 'luzhok@moscow.ru',
                                   'user_category': AppUser.MANAGER_STATUS,
                               }, format='json')
        view = AppUserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()

        request = factory.post('/api/users/',
                               {
                                   'first_name': 'Юра',
                                   'last_name': 'Лужков',
                                   'user_name': 'luzhok',
                                   'email': 'luzhok@moscow.ru',
                                   'user_category': AppUser.MANAGER_STATUS,
                               }, format='json')
        admin = User.objects.create_superuser('admin156', 'admin@admin.com',
                                              'admin123456')
        force_authenticate(request, admin)
        view = AppUserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = AppUser.objects.create(first_name='Юра', last_name='Лужков', user_name='luzhok',
                                        email='luzhok@moscow.ru', user_category=AppUser.MANAGER_STATUS)
        client = APIClient()
        response = client.get(f'/api/users/{user.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_edit_guest(self):
        user = AppUser.objects.create(first_name='Юра', last_name='Лужков', user_name='luzhok',
                                      email='luzhok@moscow.ru', user_category=AppUser.MANAGER_STATUS)

        client = APIClient()
        response = client.put(f'/api/users/{user.uid}/', {
                                   'first_name': 'Ваня',
                                   'last_name': 'Внуков',
                               })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print(response.data)

    def test_edit_admin(self):
        user = AppUser.objects.create(first_name='Юра', last_name='Лужков', user_name='luzhok',
                                      email='luzhok@moscow.ru', user_category=AppUser.MANAGER_STATUS)
        print(user)
        client = APIClient()
        admin = User.objects.create_superuser('admin156', 'admin@admin.com', 'admin123456')
        client.login(username='admin156', password='admin123456')
        response = client.patch(f'/api/users/{user.uid}/', {
            'first_name': 'Ваня',
            'last_name': 'Внуков',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = AppUser.objects.get(uid=user.uid)
        self.assertEqual(user.first_name, 'Ваня')
        self.assertEqual(user.last_name, 'Внуков')
        print(response.data)
        client.logout()
