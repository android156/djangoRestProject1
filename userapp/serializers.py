from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import AppUser


class UserModelSerializerAll(ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'


class UserModelSerializerForToDo(HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        # fields = '__all__'
        fields = ['first_name', 'last_name']


class UserModelSerializerForProject(HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        # fields = '__all__'
        fields = ['user_name', 'uid']


