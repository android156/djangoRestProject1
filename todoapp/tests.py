from django.test import TestCase
from mixer import factory
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .models import Project, ToDo
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

    def test_edit_project_admin(self):
        user = AppUser.objects.create(first_name='Юра', last_name='Лужков', user_name='luzhok',
                                      email='luzhok@moscow.ru', user_category=AppUser.MANAGER_STATUS)
        project = Project.objects.create(name='Точечная застройка')
        print(project)
        admin = User.objects.create_superuser('admin156', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin156', password='admin123456')

        data = {
            'name': 'Ренновация',
            # 'users': [1, 2] - это поле не хочет менять, хоть убейся. Вероятно дело в отношениях мэни ту мэни
        }

        # patch работает, а пут нет
        response = self.client.patch(f'/api/projects/{project.uid}/', data)

        print(self.client.get(f'/api/projects/{project.uid}/').data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(uid=project.uid)
        self.assertEqual(project.name, 'Ренновация')

    def test_get_todo_list(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_todo_admin(self):
        user = AppUser.objects.create(first_name='Юра', last_name='Лужков', user_name='luzhok',
                                      email='luzhok@moscow.ru', user_category=AppUser.MANAGER_STATUS)
        user2 = AppUser.objects.create(first_name='Василий', last_name='Блаженный', user_name='crazy_vasya',
                                       email='crazyV@moscow.ru')
        project = Project.objects.create(name='Стройка века в Москве',)


        print(user)
        print(user2)
        print(project)
        # Так не работает

        project.users.add(user)
        project.save()
        print(project.users)

        # Так тоже не работает
        project.users.create(first_name='Саня', last_name='Копытин', user_name='kopyto',
                                       email='sanya_kopyto@mail.ru')
        project.save()
        print(project.users)
        # И так тоже не работает
        user2.project_set.add(project)
        project.save()
        print(project.users)

        # Юзеров хрен в проект добавишь, проклятие ManyToManyField

        todo = ToDo.objects.create(text='Построить 1-ую башню Кремля', project=project, user=user)
        admin = User.objects.create_superuser('admin156', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin156', password='admin123456')

        # пут работает, когда все обязательные поля заполнены, вон оно как
        response = self.client.put(f'/api/todo/{todo.uid}/',
                                   {'text': 'Построить 2-ую башню Кремля',
                                    'user': user2.uid,
                                    'project': project.uid
                                    })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = ToDo.objects.get(uid=todo.uid)
        self.assertEqual(todo.text, 'Построить 2-ую башню Кремля')


    def test_edit_mixer(self):
        user = mixer.blend(AppUser, user_name='terminator')
        print('Юзер: ', user)
        project = mixer.blend(Project, description='Не простыня, а норм описание')
        print('Проджект: ', project)
        todo = mixer.blend(ToDo, user__user_name='Sarah_Conor')
        admin = User.objects.create_superuser('admin156', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin156', password='admin123456')
        print('Старое задание:', todo)
        response = self.client.put(f'/api/todo/{todo.uid}/',
                                   {'text': 'Построить 2-ую башню Кремля',
                                    'user': user.uid,
                                    'project': project.uid
                                    })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = ToDo.objects.get(uid=todo.uid)
        print('Новое задание:', todo)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(todo.text, 'Построить 2-ую башню Кремля')
