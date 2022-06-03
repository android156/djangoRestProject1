from rest_framework.serializers import ModelSerializer

from messageapp.models import Message


class MessageModelSerializer(ModelSerializer):

    class Meta:
        model = Message
        # fields = '__all__'
        exclude = ('updated', 'sent')


class MessageModelSerializerAll(ModelSerializer):
    class Meta:
        model = Message
        # fields = '__all__'
        fields = '__all__'


