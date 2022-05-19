from rest_framework.serializers import HyperlinkedModelSerializer
from .models import AppUser


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
