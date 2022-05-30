from django.test import TestCase
from mixer import factory
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .models import Project
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


class TestProjectViewSet2(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = AppUser.objects.create(first_name='Юра', last_name='Лужков', user_name='luzhok',
                                      email='luzhok@moscow.ru', user_category=AppUser.MANAGER_STATUS)
        project = Project.objects.create(name='Точечная застройка')
        print(project)
        admin = User.objects.create_superuser('admin156', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin156', password='admin123456')
        response = self.client.put(f'/api/projects/{project.uid}/', {'name': 'Ренновация'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(uid=project.uid)
        self.assertEqual(project.name, 'Ренновация')
