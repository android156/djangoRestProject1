from rest_framework.serializers import ModelSerializer

from messageapp.models import Message


class MessageModelSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'