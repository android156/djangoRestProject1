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
    # todo
    # # Переопределили апдэйт, чтоб можно было менять нагорячую
    # def update(self, instance, validated_data):
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.project = validated_data.get('project', instance.project)
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.is_active = validated_data.get('is_active', instance.is_active)
    #     return instance


class ToDoModelSerializerForApiView(ModelSerializer):
    user = UserModelSerializerForToDo()
    project = ProjectModelSerializerForToDo()

    class Meta:
        model = ToDo
        fields = '__all__'