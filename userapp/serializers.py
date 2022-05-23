from rest_framework.serializers import HyperlinkedModelSerializer
from .models import AppUser


class UserModelSerializerAll(HyperlinkedModelSerializer):
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
        fields = ['user_name']


