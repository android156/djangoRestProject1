from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from userapp.serializers import UserModelSerializerForToDo, UserModelSerializerForProject
from .models import Project, ToDo


class ProjectModelSerializerAll(HyperlinkedModelSerializer):
    users = UserModelSerializerForProject(many=True)

    class Meta:
        model = Project
        # fields = '__all__'
        exclude = ['url']


class ProjectModelSerializerForToDo(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        exclude = ['url', 'link', 'users']


class ToDoModelSerializer(HyperlinkedModelSerializer):
    user = UserModelSerializerForToDo()
    project = ProjectModelSerializerForToDo()

    class Meta:
        model = ToDo
        fields = '__all__'


class ToDoModelSerializerForApiView(ModelSerializer):
    user = UserModelSerializerForToDo()
    project = ProjectModelSerializerForToDo()

    class Meta:
        model = ToDo
        fields = '__all__'